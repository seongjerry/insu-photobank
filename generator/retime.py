#!/usr/bin/env python3
"""나레이션 mp3 길이에 맞춰 릴스 장면 타이밍 재계산. 사용: python3 retime.py content/x.json"""
import json, sys, subprocess, pathlib
p=pathlib.Path(sys.argv[1]); d=json.loads(p.read_text())
a=d["audio"]; lead=a.get("lead",0.25); tail=a.get("tail",0.55); t=0.0
for i,s in enumerate(d["scenes"],1):
    f=pathlib.Path(a["narration_dir"])/f"{i:02d}.mp3"
    dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).decode())
    s["t"]=[round(t,2), round(t+lead+dur+tail,2)]; t=s["t"][1]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)); print("total", round(t,2), [s["t"] for s in d["scenes"]])
