#!/usr/bin/env python3
"""텔레그램(@Jerryblogbot) 보고·승인 도구 (GitHub Actions에서 실행, 토큰은 Secrets)
MODE=send  : publish/outbox/*.json 중 sent 아닌 것 전송 → {"text":"...", "video":"경로(선택)", "photo":"경로(선택)", "album":["경로",..](선택, 최대 10장)}
MODE=poll  : 본부장님 채팅의 최근 메시지를 publish/inbox/latest.json 에 기록 (getUpdates, offset 확정 안 함)
"""
import json, os, pathlib, time, uuid, urllib.request, urllib.parse
ROOT = pathlib.Path(__file__).resolve().parents[1]
T = os.environ["TELEGRAM_TOKEN"].strip(); C = os.environ["TELEGRAM_CHAT_ID"].strip(); API = f"https://api.telegram.org/bot{T}"


def call(method, data=None, files=None):
    if files:
        b = uuid.uuid4().hex; body = b""
        for k, v in (data or {}).items():
            body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode()
        for k, p in files.items():
            body += f'--{b}\r\nContent-Disposition: form-data; name="{k}"; filename="{pathlib.Path(p).name}"\r\nContent-Type: application/octet-stream\r\n\r\n'.encode() + (ROOT / p).read_bytes() + b"\r\n"
        body += f"--{b}--\r\n".encode(); h = {"Content-Type": f"multipart/form-data; boundary={b}"}
    else:
        body = urllib.parse.urlencode(data or {}).encode(); h = {}
    r = urllib.request.Request(f"{API}/{method}", data=body, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=300) as res: return json.loads(res.read())
    except urllib.error.HTTPError as e: return {"ok": False, "status": e.code, "error": e.read().decode()[:300]}


def send():
    n = 0
    for f in sorted((ROOT / "publish/outbox").glob("*.json")):
        m = json.loads(f.read_text())
        if m.get("sent"): continue
        text = m.get("text", "")
        if m.get("album"):  # 캐러셀 미리보기: 사진·영상 여러 장을 개별 파일로 (압축 없음, 최대 10장)
            paths = m["album"][:10]; media = []; files = {}
            for i, p in enumerate(paths):
                k = f"f{i}"; files[k] = p
                it = {"type": "video" if p.lower().endswith(".mp4") else "photo", "media": f"attach://{k}"}
                if i == 0 and len(text) <= 1000: it["caption"] = text
                media.append(it)
            r = call("sendMediaGroup", {"chat_id": C, "media": json.dumps(media, ensure_ascii=False)}, files)
        elif m.get("video"): r = call("sendVideo", {"chat_id": C, "caption": text[:1000], "supports_streaming": "true"}, {"video": m["video"]})
        elif m.get("photo"): r = call("sendPhoto", {"chat_id": C, "caption": text[:1000]}, {"photo": m["photo"]})
        else: r = None
        if not (m.get("video") or m.get("photo") or m.get("album")) or (text and len(text) > 1000):
            for i in range(0, len(text), 3900): r = call("sendMessage", {"chat_id": C, "text": text[i:i + 3900]})
        m["sent"] = bool(r and r.get("ok")); m["sent_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
        if not m["sent"]: m["error"] = str(r)[:300]
        f.write_text(json.dumps(m, ensure_ascii=False, indent=1)); n += 1
    print("sent:", n)


def poll():
    r = call("getUpdates", {"timeout": 0, "allowed_updates": json.dumps(["message"])})
    out = {"checked_at": int(time.time()), "ok": r.get("ok", False), "messages": []}
    if not r.get("ok"): out["error"] = r.get("error", str(r))[:300]  # 409이면 웹훅이 걸린 봇
    for u in r.get("result", []):
        msg = u.get("message") or {}
        if str((msg.get("chat") or {}).get("id")) != C: continue
        out["messages"].append({"date": msg.get("date"), "text": msg.get("text", ""),
                                "reply_to": ((msg.get("reply_to_message") or {}).get("text") or "")[:80]})
    (ROOT / "publish/inbox/latest.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print("poll ok:", out["ok"], "messages:", len(out["messages"]))


{"send": send, "poll": poll}[os.environ.get("MODE", "send")]()
