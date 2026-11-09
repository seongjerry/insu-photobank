#!/usr/bin/env python3
"""publish/queue/*.json 중 yt_status=approved 이고 게시 시각이 지난 항목을 유튜브 쇼츠로 올린다.
큐 항목에 추가하는 필드: "yt_status":"approved", "yt_title":"제목 #Shorts"(없으면 본문 첫 줄)
API 심사 전 프로젝트는 유튜브가 영상을 비공개로 고정한다(스튜디오에서 공개로 바꿔야 함).
"""
import json, os, pathlib, datetime, urllib.request, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]; Q = ROOT / "publish/queue"
CID = "".join(os.environ["YT_CLIENT_ID"].split()); CSEC = "".join(os.environ["YT_CLIENT_SECRET"].split())
RT = "".join(os.environ["YT_REFRESH_TOKEN"].split())
TG_T = os.environ.get("TELEGRAM_TOKEN", "").strip(); TG_C = os.environ.get("TELEGRAM_CHAT_ID", "").strip()


def http(url, data=None, headers=None, method=None):
    r = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(r, timeout=600) as res:
            return res.status, dict(res.headers), res.read().decode() or "{}"
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.read().decode()[:400]}")


def access_token():
    _, _, b = http("https://oauth2.googleapis.com/token", urllib.parse.urlencode(
        {"client_id": CID, "client_secret": CSEC, "refresh_token": RT, "grant_type": "refresh_token"}).encode(),
        {"Content-Type": "application/x-www-form-urlencoded"}, "POST")
    d = json.loads(b); return d["access_token"], d.get("scope", "")


def tg(msg):
    if TG_T and TG_C:
        try: http(f"https://api.telegram.org/bot{TG_T}/sendMessage", urllib.parse.urlencode({"chat_id": TG_C, "text": msg}).encode(), method="POST")
        except Exception: pass


def upload(tok, item):
    cap = item.get("caption", "")
    title = item.get("yt_title") or (cap.splitlines()[0] if cap else item["id"])
    if "#shorts" not in title.lower(): title = (title[:90] + " #Shorts")
    meta = {"snippet": {"title": title[:100], "description": cap[:4900], "categoryId": "27", "defaultLanguage": "ko",
                        "tags": [t.lstrip("#") for t in cap.split() if t.startswith("#")][:15]},
            "status": {"privacyStatus": item.get("yt_privacy", "public"), "selfDeclaredMadeForKids": False}}
    data = (ROOT / item["video"]).read_bytes()
    _, h, _ = http("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
                   json.dumps(meta).encode(), {"Authorization": f"Bearer {tok}", "Content-Type": "application/json; charset=UTF-8",
                   "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(len(data))}, "POST")
    loc = h.get("Location") or h.get("location")
    _, _, b = http(loc, data, {"Content-Type": "video/mp4"}, "PUT")
    vid = json.loads(b)["id"]
    if item.get("cover"):
        try: http(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}", (ROOT / item["cover"]).read_bytes(),
                  {"Authorization": f"Bearer {tok}", "Content-Type": "image/jpeg"}, "POST")
        except Exception as e: print("thumbnail skipped:", str(e)[:80])
    return vid


def main():
    tok, scope = access_token()
    if os.environ.get("YT_CHECK"): print("youtube token ok, scope:", scope); return
    now = datetime.datetime.now(datetime.timezone.utc); n = 0
    for f in sorted(Q.glob("*.json")):
        item = json.loads(f.read_text())
        if item.get("yt_status") != "approved": continue
        if datetime.datetime.fromisoformat(item.get("publish_at", "2000-01-01T00:00:00+09:00")) > now: continue
        try:
            vid = upload(tok, item); link = f"https://youtube.com/shorts/{vid}"
            item.update(yt_status="posted", yt_id=vid, yt_link=link); n += 1
            tg(f"✅ 유튜브 쇼츠 업로드 완료: {item['id']}\n{link}\n(API 심사 전에는 비공개로 올라가요. 스튜디오에서 공개로 바꿔주세요)")
        except Exception as e:
            item.update(yt_status="error", yt_error=str(e)[:300]); tg(f"⚠️ 유튜브 업로드 실패: {item['id']}\n{str(e)[:200]}")
        f.write_text(json.dumps(item, ensure_ascii=False, indent=1))
    print("youtube posted:", n)


if __name__ == "__main__":
    main()
