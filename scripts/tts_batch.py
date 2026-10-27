#!/usr/bin/env python3
"""tts/requests/*.json → edge-tts 로 mp3 생성 → tts/out/<id>/NN.mp3 (+ done.json)
요청 형식: {"id": "2026-10-27_reel_walk_sleep", "voice": "ko-KR-SunHiNeural", "rate": "+8%", "pitch": "+0Hz",
            "segments": [{"n": 1, "text": "밤에 자꾸 깨세요?"}, ...]}
추천 음성: ko-KR-SunHiNeural(여, 또렷) · ko-KR-InJoonNeural(남, 차분) · ko-KR-HyunsuMultilingualNeural(남, 자연스러움)
"""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
REQ = ROOT / "tts/requests"; OUT = ROOT / "tts/out"
for f in sorted(REQ.glob("*.json")):
    r = json.loads(f.read_text(encoding="utf-8"))
    d = OUT / r["id"]
    if (d / "done.json").exists(): continue
    d.mkdir(parents=True, exist_ok=True)
    for seg in r["segments"]:
        mp3 = d / f"{seg['n']:02d}.mp3"
        cmd = ["edge-tts", "--voice", r.get("voice", "ko-KR-SunHiNeural"), "--rate", r.get("rate", "+5%"),
               "--pitch", r.get("pitch", "+0Hz"), "--text", seg["text"], "--write-media", str(mp3)]
        subprocess.run(cmd, check=True)
        print("ok", mp3)
    (d / "done.json").write_text(json.dumps({"id": r["id"], "segments": len(r["segments"])}), encoding="utf-8")
    f.unlink()  # 처리된 요청은 제거
print("done")
