#!/usr/bin/env python3
"""지난 N일(기본 8일) 게시물 성과 수집 → publish/insights/<날짜>.json
인스타: 좋아요·댓글(기본) + 조회·도달·저장·공유·평균시청(권한 있으면)
유튜브: 조회·좋아요·댓글(토큰 권한 있으면). 실패한 항목은 error 로 남겨 리포트에서 해결책을 안내한다.
"""
import json, os, pathlib, time, datetime, urllib.request, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parents[1]
DAYS = int(os.environ.get("DAYS", "8")); since = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=DAYS)
G = "https://graph.facebook.com/v23.0"; TOKEN = "".join(os.environ["IG_TOKEN"].split()); IGID = os.environ["IG_USER_ID"].strip()


def get(url):
    try:
        with urllib.request.urlopen(url, timeout=60) as r: return json.loads(r.read())
    except urllib.error.HTTPError as e: return {"error": e.read().decode()[:300]}


out = {"collected_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "days": DAYS, "instagram": [], "youtube": [], "errors": []}
q = urllib.parse.urlencode({"fields": "id,caption,timestamp,permalink,like_count,comments_count,media_product_type", "limit": 50, "access_token": TOKEN})
res = get(f"{G}/{IGID}/media?{q}")
if "error" in res: out["errors"].append({"instagram_media": res["error"]})
for m in res.get("data", []):
    if datetime.datetime.fromisoformat(m["timestamp"].replace("+0000", "+00:00")) < since: continue
    m["caption"] = (m.get("caption") or "")[:120]
    ins = get(f"{G}/{m['id']}/insights?" + urllib.parse.urlencode({"metric": "views,reach,saved,shares,total_interactions,ig_reels_avg_watch_time", "access_token": TOKEN}))
    if "error" in ins: m["insights_error"] = ins["error"][:200]
    else: m.update({d["name"]: (d.get("values") or [{}])[0].get("value") for d in ins.get("data", [])})
    out["instagram"].append(m)
# 유튜브: 큐에 기록된 영상 ID 기준
ids = []
for f in (ROOT / "publish/queue").glob("*.json"):
    d = json.loads(f.read_text())
    if d.get("yt_id"): ids.append((d["id"], d["yt_id"]))
if ids and os.environ.get("YT_REFRESH_TOKEN"):
    try:
        tok = json.loads(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
            "client_id": os.environ["YT_CLIENT_ID"].strip(), "client_secret": os.environ["YT_CLIENT_SECRET"].strip(),
            "refresh_token": "".join(os.environ["YT_REFRESH_TOKEN"].split()), "grant_type": "refresh_token"}).encode()), timeout=60).read())["access_token"]
        r = urllib.request.Request("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "statistics,status,snippet", "id": ",".join(i for _, i in ids)}), headers={"Authorization": f"Bearer {tok}"})
        for v in json.loads(urllib.request.urlopen(r, timeout=60).read()).get("items", []):
            out["youtube"].append({"yt_id": v["id"], "title": v["snippet"]["title"][:80], "privacy": v["status"]["privacyStatus"], **v.get("statistics", {})})
    except Exception as e:
        out["errors"].append({"youtube": str(getattr(e, "read", lambda: str(e).encode())().decode() if hasattr(e, "read") else e)[:300]})
p = ROOT / f"publish/insights/{datetime.date.today().isoformat()}.json"; p.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print("instagram:", len(out["instagram"]), "youtube:", len(out["youtube"]), "errors:", len(out["errors"]))
