"""telegram/outbox/<id>/ 에 들어온 콘텐츠를 텔레그램으로 개별 파일로 보낸다.
폴더 구성(있는 것만): header.txt(맨 처음 보낼 요약), *.png/*.jpg(이름순, 10장씩 앨범), *.mp4(영상), caption.txt(인스타 캡션, 복사용 별도 메시지)
보낸 폴더에는 sent.json 을 남긴다. 토큰·대화방은 저장소 Secrets(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)."""
import json, os, sys, time
from pathlib import Path
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
CHAT = os.environ.get("TELEGRAM_CHAT_ID", "")
API = f"https://api.telegram.org/bot{TOKEN}/"
OUT = Path("telegram/outbox")


def call(method, data=None, files=None):
    for i in range(3):
        r = requests.post(API + method, data=data, files=files, timeout=120)
        j = r.json()
        if j.get("ok"):
            return j
        if j.get("error_code") == 429:
            time.sleep(j.get("parameters", {}).get("retry_after", 5) + 1)
            continue
        raise RuntimeError(f"{method}: {j}")
    raise RuntimeError(f"{method}: retry exceeded")


def text(t):
    t = t.strip()
    while t:
        call("sendMessage", {"chat_id": CHAT, "text": t[:4000], "disable_web_page_preview": "true"})
        t = t[4000:]


def album(paths):
    for k in range(0, len(paths), 10):
        chunk = paths[k:k + 10]
        if len(chunk) == 1:
            with open(chunk[0], "rb") as f:
                call("sendPhoto", {"chat_id": CHAT}, {"photo": f})
            continue
        fhs = [open(p, "rb") for p in chunk]
        try:
            media = [{"type": "photo", "media": f"attach://f{i}"} for i in range(len(chunk))]
            call("sendMediaGroup", {"chat_id": CHAT, "media": json.dumps(media)},
                 {f"f{i}": fh for i, fh in enumerate(fhs)})
        finally:
            for fh in fhs:
                fh.close()
        time.sleep(1)


def main():
    if not (TOKEN and CHAT):
        print("TELEGRAM_TOKEN / TELEGRAM_CHAT_ID secrets missing"); return 1
    done = 0
    for d in sorted(p for p in OUT.glob("*") if p.is_dir()):
        if (d / "sent.json").exists():
            continue
        if (d / "header.txt").exists():
            text((d / "header.txt").read_text(encoding="utf-8"))
        imgs = sorted([p for p in d.iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg")])
        vids = sorted([p for p in d.iterdir() if p.suffix.lower() == ".mp4"])
        for v in vids:
            with open(v, "rb") as f:
                call("sendVideo", {"chat_id": CHAT, "supports_streaming": "true"}, {"video": f})
        if imgs:
            album(imgs)
        if (d / "caption.txt").exists():
            text((d / "caption.txt").read_text(encoding="utf-8"))
        (d / "sent.json").write_text(json.dumps({"sent_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                                                 "images": len(imgs), "videos": len(vids)}), encoding="utf-8")
        print(f"sent {d.name}: {len(imgs)} images, {len(vids)} videos")
        done += 1
    print(f"done {done}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
