#!/usr/bin/env python3
"""publish/queue/*.json 중 승인(approved)되고 게시 시각이 지난 항목을 인스타 릴스로 게시한다.

큐 형식 (예: publish/queue/ep08.json)
{"id":"ep08","video":"publish/media/ep08.mp4","cover":"publish/media/ep08.jpg",
 "caption":"본문...","publish_at":"2026-11-10T19:00:00+09:00","status":"approved"}
status: pending(대기, 게시 안 함) → approved(승인) → posted(완료) / error
영상·커버는 Supabase Storage 공개 버킷(reels)에 올려 인스타가 가져갈 수 있는 주소를 만든다.
로그에는 개수와 결과 링크만 남긴다(공개 저장소).
"""
import json, os, pathlib, time, datetime, urllib.request, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
Q = ROOT / "publish/queue"
SB = os.environ["SUPABASE_URL"].strip().rstrip("/")
SBKEY = "".join(os.environ["SUPABASE_SERVICE_KEY"].split())
TOKEN = "".join(os.environ["IG_TOKEN"].split())
IGID = os.environ["IG_USER_ID"].strip()
TG_T = os.environ.get("TELEGRAM_TOKEN", "").strip(); TG_C = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
G = "https://graph.facebook.com/v23.0"
BUCKET = "reels"


def req(url, data=None, headers=None, method=None, raw=None):
    h = headers or {}
    body = raw if raw is not None else (urllib.parse.urlencode(data).encode() if data is not None else None)
    r = urllib.request.Request(url, data=body, headers=h, method=method or ("POST" if body is not None else "GET"))
    try:
        with urllib.request.urlopen(r, timeout=300) as res:
            t = res.read().decode() or "{}"
            return json.loads(t) if t.strip().startswith(("{", "[")) else {"text": t}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:400]}")


def ensure_bucket():
    try:
        req(f"{SB}/storage/v1/bucket", raw=json.dumps({"id": BUCKET, "name": BUCKET, "public": True}).encode(),
            headers={"Authorization": f"Bearer {SBKEY}", "apikey": SBKEY, "Content-Type": "application/json"})
    except RuntimeError as e:
        if "already exists" not in str(e) and "409" not in str(e) and "Duplicate" not in str(e):
            raise


def upload(path, ctype):
    name = f"{int(time.time())}_{pathlib.Path(path).name}"
    req(f"{SB}/storage/v1/object/{BUCKET}/{name}", raw=(ROOT / path).read_bytes(),
        headers={"Authorization": f"Bearer {SBKEY}", "apikey": SBKEY, "Content-Type": ctype, "x-upsert": "true"})
    return f"{SB}/storage/v1/object/public/{BUCKET}/{name}"


def tg(msg):
    if TG_T and TG_C:
        try: req(f"https://api.telegram.org/bot{TG_T}/sendMessage", {"chat_id": TG_C, "text": msg})
        except Exception: pass


def wait(cid):
    for _ in range(60):  # 최대 10분 대기
        st = req(f"{G}/{cid}?" + urllib.parse.urlencode({"fields": "status_code,status", "access_token": TOKEN}))
        if st.get("status_code") == "FINISHED": return
        if st.get("status_code") == "ERROR": raise RuntimeError("인스타 처리 실패: " + str(st.get("status"))[:200])
        time.sleep(10)
    raise RuntimeError("인스타 처리 시간 초과")


def carousel(item):
    """캐러셀: item["media"] = ["publish/media/x-01.mp4", "publish/media/x-02.jpg", ...] (2~10장, 사진은 JPEG)"""
    paths = item["media"]
    if not 2 <= len(paths) <= 10: raise RuntimeError(f"캐러셀은 2~10장이어야 함 (지금 {len(paths)}장)")
    kids = []
    for p in paths:
        if p.lower().endswith(".mp4"):
            c = {"media_type": "VIDEO", "video_url": upload(p, "video/mp4")}
        else:
            c = {"image_url": upload(p, "image/jpeg")}
        c.update(is_carousel_item="true", access_token=TOKEN)
        kids.append(req(f"{G}/{IGID}/media", c)["id"])
    for k in kids: wait(k)
    cid = req(f"{G}/{IGID}/media", {"media_type": "CAROUSEL", "children": ",".join(kids),
                                    "caption": item.get("caption", ""), "access_token": TOKEN})["id"]
    wait(cid)
    return cid


def publish(item):
    ensure_bucket()
    if item.get("type") == "carousel":
        cid = carousel(item)
    else:
        vurl = upload(item["video"], "video/mp4")
        p = {"media_type": "REELS", "video_url": vurl, "caption": item.get("caption", ""), "share_to_feed": "true", "access_token": TOKEN}
        if item.get("cover"): p["cover_url"] = upload(item["cover"], "image/jpeg")
        cid = req(f"{G}/{IGID}/media", p)["id"]
        wait(cid)
    mid = req(f"{G}/{IGID}/media_publish", {"creation_id": cid, "access_token": TOKEN})["id"]
    link = req(f"{G}/{mid}?" + urllib.parse.urlencode({"fields": "permalink", "access_token": TOKEN})).get("permalink", "")
    return mid, link


def main():
    now = datetime.datetime.now(datetime.timezone.utc); done = 0
    if os.environ.get("IG_CHECK"):  # 연결 확인만
        def q(path, fields=None):
            prm = {"access_token": TOKEN}
            if fields: prm["fields"] = fields
            try: return req(f"{G}/{path}?" + urllib.parse.urlencode(prm))
            except Exception as e: return {"error": str(e)[:300]}
        print("ig account:", q(IGID, "username,media_count"))
        recent = q(f"{IGID}/media", "timestamp,caption")
        print("recent:", [(m.get("timestamp"), (m.get("caption") or "")[:20]) for m in recent.get("data", [])[:3]] or recent)
        print("token owner:", q("me", "name"))
        print("pages & linked ig:", q("me/accounts", "name,instagram_business_account{id,username}"))
        perms = q("me/permissions")
        print("permissions:", [f"{x.get('permission')}={x.get('status')}" for x in perms.get("data", [])] or perms)
        return
    for f in sorted(Q.glob("*.json")):
        item = json.loads(f.read_text())
        if item.get("status") != "approved": continue
        at = datetime.datetime.fromisoformat(item.get("publish_at", "2000-01-01T00:00:00+09:00"))
        if at > now: continue
        try:
            mid, link = publish(item)
            item.update(status="posted", media_id=mid, permalink=link, posted_at=now.isoformat())
            kind = "캐러셀" if item.get("type") == "carousel" else "릴스"
            tg(f"✅ 인스타 {kind} 게시 완료: {item['id']}\n{link}"); done += 1
        except Exception as e:
            item.update(status="error", error=str(e)[:300]); tg(f"⚠️ 인스타 게시 실패: {item['id']}\n{str(e)[:200]}")
        f.write_text(json.dumps(item, ensure_ascii=False, indent=1))
    print("posted:", done)


if __name__ == "__main__":
    main()
