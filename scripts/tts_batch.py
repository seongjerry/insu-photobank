#!/usr/bin/env python3
"""tts/requests/*.json → 나레이션 mp3 생성 → tts/out/<id>/NN.mp3 (+ done.json)

엔진 1) edge-tts (기본, engine 생략 가능)
  {"id": "2026-10-27_reel_walk_sleep", "voice": "ko-KR-SunHiNeural", "rate": "+8%", "pitch": "+0Hz",
   "segments": [{"n": 1, "text": "밤에 자꾸 깨세요?"}, ...]}
  추천 음성: ko-KR-SunHiNeural(여, 또렷) · ko-KR-InJoonNeural(남, 차분) · ko-KR-HyunsuMultilingualNeural(남, 자연스러움)

엔진 2) TTSMaker  (https://ttsmaker.com/developer-api-docs)
  {"id": "...", "engine": "ttsmaker", "voice_id": 1501, "speed": 1.1,
   "segments": [{"n": 1, "text": "..."}]}
  음성 전체 샘플: {"id": "...", "engine": "ttsmaker", "action": "sample_all", "language": "ko", "text": "샘플 문장"}
  토큰: 저장소 Secret TTSMAKER_TOKEN 이 있으면 사용, 없으면 공용 테스트 토큰(주 10만자, 공유)
"""
import json, os, pathlib, subprocess, time, urllib.request, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQ = ROOT / "tts/requests"; OUT = ROOT / "tts/out"
TM_TOKEN = os.environ.get("TTSMAKER_TOKEN") or "ttsmaker_demo_token"
TM_BASES = [os.environ.get("TTSMAKER_API") or "https://api.ttsmaker.com/v1", "https://api.ttsmaker.cn/v1",
            "https://ttsmaker.com/api/v1", "https://api.ttsmaker.com/v2"]
TM_API = None  # 첫 성공한 주소로 고정
TM_LOG = []


def http_json(url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json; charset=utf-8",
                                                          "User-Agent": "insu-photobank-tts"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def tm_voices(lang):
    global TM_API
    q = urllib.parse.urlencode({"token": TM_TOKEN, "language": lang})
    for base in TM_BASES:
        for method in ("GET", "POST"):
            try:
                res = http_json(f"{base}/get-voice-list?{q}") if method == "GET" else \
                      http_json(f"{base}/get-voice-list", {"token": TM_TOKEN, "language": lang})
                TM_LOG.append({"base": base, "method": method, "ok": True, "status": res.get("status")})
                if res.get("status") == "success" or res.get("voices_detailed_list"):
                    TM_API = base
                    return res
            except Exception as e:
                TM_LOG.append({"base": base, "method": method, "error": str(e)[:200]})
    raise RuntimeError("voice list failed: " + json.dumps(TM_LOG, ensure_ascii=False))


def tm_speak(text, voice_id, path, speed=1.0, volume=0):
    res = http_json(f"{TM_API or TM_BASES[0]}/create-tts-order", {
        "token": TM_TOKEN, "text": text, "voice_id": int(voice_id), "audio_format": "mp3",
        "audio_speed": float(speed), "audio_volume": volume, "text_paragraph_pause_time": 0})
    url = res.get("audio_file_url")
    if not url:
        raise RuntimeError(json.dumps(res, ensure_ascii=False))
    req = urllib.request.Request(url, headers={"User-Agent": "insu-photobank-tts"})
    with urllib.request.urlopen(req, timeout=120) as r:
        path.write_bytes(r.read())
    time.sleep(0.3)  # QPS 제한 여유


def run_edge(r, d):
    for seg in r["segments"]:
        mp3 = d / f"{seg['n']:02d}.mp3"
        cmd = ["edge-tts", "--voice", r.get("voice", "ko-KR-SunHiNeural"), "--rate", r.get("rate", "+5%"),
               "--pitch", r.get("pitch", "+0Hz"), "--text", seg["text"], "--write-media", str(mp3)]
        subprocess.run(cmd, check=True)
        print("ok", mp3)
    return {"segments": len(r["segments"])}


def run_ttsmaker(r, d):
    if r.get("action") == "sample_all":
        vl = tm_voices(r.get("language", "ko"))
        (d / "voices.json").write_text(json.dumps(vl, ensure_ascii=False, indent=1), encoding="utf-8")
        voices = vl.get("voices_detailed_list") or vl.get("voices") or []
        made, errors = [], []
        for v in voices:
            vid = v.get("id") if isinstance(v, dict) else v
            try:
                tm_speak(r["text"], vid, d / f"v{vid}.mp3", r.get("speed", 1.0))
                made.append(vid)
            except Exception as e:  # 한 음성 실패해도 계속
                errors.append({"voice_id": vid, "error": str(e)[:300]})
        return {"api": TM_API, "samples": made, "errors": errors[:10], "log": TM_LOG}
    for seg in r["segments"]:
        mp3 = d / f"{seg['n']:02d}.mp3"
        tm_speak(seg["text"], r["voice_id"], mp3, r.get("speed", 1.0))
        print("ok", mp3)
    return {"segments": len(r["segments"])}


for f in sorted(REQ.glob("*.json")):
    r = json.loads(f.read_text(encoding="utf-8"))
    d = OUT / r["id"]
    if (d / "done.json").exists():
        continue
    d.mkdir(parents=True, exist_ok=True)
    try:
        info = run_ttsmaker(r, d) if r.get("engine") == "ttsmaker" else run_edge(r, d)
        info["ok"] = True
    except Exception as e:
        info = {"ok": False, "error": str(e)[:1000]}
        print("FAIL", r["id"], e)
    (d / "done.json").write_text(json.dumps({"id": r["id"], **info}, ensure_ascii=False), encoding="utf-8")
    f.unlink()  # 처리된 요청은 제거 (실패 시 done.json 의 error 확인 후 다시 올리기)
print("done")
