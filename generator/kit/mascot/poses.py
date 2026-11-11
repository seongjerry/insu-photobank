#!/usr/bin/env python3
"""비노 포즈 라이브러리 12종: python3 poses.py 로 poses/*.svg, poses.json, poses_sheet.png 생성"""
import os, subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "poses")

NAVY = "#22305C"
def arm(d, x, y):
    return f'<path d="{d}" fill="none" stroke="{NAVY}" stroke-width="20" stroke-linecap="round"/><circle cx="{x}" cy="{y}" r="14" fill="{NAVY}"/>'
def eye(x, y, r=15, dx=5, dy=-6, hr=5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#1A1A1A"/><circle cx="{x+dx}" cy="{y+dy}" r="{hr}" fill="#fff"/>'
def line(d, w=8, c="#1A1A1A"):
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def star(x, y, s=14, c="#FFE45C"):
    k = s * 0.3
    return f'<path d="M{x} {y-s} L{x+k} {y-k} L{x+s} {y} L{x+k} {y+k} L{x} {y+s} L{x-k} {y+k} L{x-s} {y} L{x-k} {y-k}Z" fill="{c}"/>'

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><defs><filter id="st" x="-10%" y="-10%" width="120%" height="120%">'
        '<feMorphology in="SourceAlpha" operator="dilate" radius="6" result="d"/><feFlood flood-color="#fff"/><feComposite in2="d" operator="in" result="o"/>'
        '<feMerge><feMergeNode in="o"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
        '<ellipse cx="200" cy="372" rx="110" ry="14" fill="#000" opacity=".2"/><g filter="url(#st)">'
        '<rect x="150" y="320" width="26" height="40" rx="13" fill="#1A2548"/><rect x="224" y="320" width="26" height="40" rx="13" fill="#1A2548"/>'
        '<ellipse cx="160" cy="360" rx="22" ry="12" fill="#1A2548"/><ellipse cx="240" cy="360" rx="22" ry="12" fill="#1A2548"/>'
        '<g transform="rotate(-12 230 92)"><rect x="196" y="58" width="74" height="70" rx="6" fill="#FFE45C"/><path d="M196 110 L214 128 L196 128Z" fill="#E8C93A"/></g>'
        '<rect x="92" y="88" width="216" height="246" rx="40" fill="#22305C"/><rect x="112" y="104" width="182" height="214" rx="30" fill="#FFFDF5"/>'
        '<line x1="134" y1="262" x2="272" y2="262" stroke="#D8E1F2" stroke-width="5" stroke-linecap="round"/>'
        '<line x1="134" y1="286" x2="272" y2="286" stroke="#D8E1F2" stroke-width="5" stroke-linecap="round"/>'
        + "".join(f'<rect x="84" y="{y}" width="40" height="14" rx="7" fill="#C9CED9" stroke="#9AA2B3" stroke-width="3"/>' for y in (121, 161, 201, 241, 281))
        + '<rect x="296" y="196" width="26" height="40" rx="8" fill="#FFE45C" stroke="#E0BE2E" stroke-width="3"/><circle cx="309" cy="212" r="5" fill="#22305C"/><rect x="307" y="214" width="4" height="10" rx="2" fill="#22305C"/>')
CHEEK = '<ellipse cx="146" cy="212" rx="14" ry="8" fill="#FF9DB1" opacity=".8"/><ellipse cx="258" cy="212" rx="14" ry="8" fill="#FF9DB1" opacity=".8"/>'
TAIL = '</g></svg>'

L_DOWN = arm("M100 250 Q82 250 64 290", 64, 290)
R_DOWN = arm("M304 250 Q322 250 340 290", 340, 290)
L_HIP = arm("M100 240 Q62 262 92 296", 92, 296)
R_HIP = arm("M304 240 Q342 262 312 296", 312, 296)
L_UP = arm("M100 240 Q79 240 58 170", 58, 170)
R_UP = arm("M304 240 Q325 240 346 170", 346, 170)
R_HOLD = arm("M304 250 Q321 250 338 196", 338, 196)
EYES = eye(164, 182) + eye(240, 182)
HAPPY_EYES = line("M150 186 Q164 170 178 186") + line("M226 186 Q240 170 254 186")
SMILE = line("M188 214 Q202 230 216 214", 7)
BIG_SMILE = '<path d="M184 210 Q202 240 220 210 Z" fill="#1A1A1A"/><path d="M192 224 Q202 232 212 224" fill="#FF6B6B"/>'
PEN = ('<g transform="translate(352 236) rotate(20)"><rect x="-7" y="-46" width="14" height="74" rx="5" fill="#3B6EF0"/><rect x="-7" y="-46" width="14" height="14" rx="4" fill="#2450C8"/>'
       '<path d="M-7 28 L7 28 L0 44Z" fill="#F2D3A8"/><path d="M-2.5 38 L2.5 38 L0 44Z" fill="#1A1A1A"/></g>')

# 이름: (한글 이름, 쓰는 상황, SVG 조각)
POSES = {
    "base":  ("기본", "소개·일반 설명", arm("M100 250 Q81 250 62 212", 62, 212) + arm("M304 250 Q322 250 340 262", 340, 262) + PEN + EYES + SMILE),
    "shh":   ("쉿", "비밀 공개 직전·표지", arm("M300 250 Q258 250 216 222", 216, 222) + L_DOWN + eye(164, 182) + line("M226 184 Q240 172 254 184") + line("M192 220 L212 220", 7)
              + '<text x="300" y="120" font-size="34" fill="#7FB2FF" font-family="Paperlogy,sans-serif" font-weight="900">쉿!</text>'),
    "wow":   ("헉", "손해 보는 순간·경고", L_UP + R_UP + eye(164, 180, 19, 7, -8, 7) + eye(240, 180, 19, 7, -8, 7)
              + '<ellipse cx="202" cy="222" rx="11" ry="14" fill="#1A1A1A"/><ellipse cx="202" cy="228" rx="6" ry="5" fill="#FF6B6B"/>'
              + '<g fill="#FF6B6B"><rect x="186" y="18" width="16" height="44" rx="8"/><circle cx="194" cy="76" r="9"/></g>'),
    "check": ("체크", "마무리·저장 유도", L_DOWN + arm("M304 250 Q321 250 338 190", 338, 190)
              + '<circle cx="338" cy="168" r="30" fill="#fff" stroke="#3B6EF0" stroke-width="6"/>' + line("M324 168 L335 180 L354 156", 8, "#3B6EF0") + HAPPY_EYES + BIG_SMILE),
    "think": ("고민", "질문 던지기·헷갈리는 내용", L_DOWN + arm("M304 252 Q290 262 244 240", 244, 240)
              + eye(164, 180, 15, 6, -8, 5) + eye(240, 180, 15, 6, -8, 5) + line("M150 156 Q164 148 178 156", 6) + line("M190 220 Q198 214 208 220", 7)
              + '<text x="296" y="128" font-size="72" fill="#7FB2FF" font-family="Paperlogy,sans-serif" font-weight="900">?</text>'),
    "angry": ("버럭", "팩폭·하면 안 되는 행동", L_HIP + R_HIP + EYES + line("M146 158 L180 170") + line("M258 158 L224 170") + line("M186 226 Q202 212 218 226", 7)
              + '<g transform="translate(318 104)">' + line("M-14 -22 Q-2 -14 -10 -2", 8, "#FF6B6B") + line("M14 -22 Q2 -14 10 -2", 8, "#FF6B6B") + line("M-10 6 Q-2 18 -14 26", 8, "#FF6B6B") + line("M10 6 Q2 18 14 26", 8, "#FF6B6B") + '</g>'),
    "sad":   ("시무룩", "못 받은 사례·손해", L_DOWN + R_DOWN + eye(164, 184, 15, 4, -6, 5) + eye(240, 184, 15, 4, -6, 5)
              + line("M148 166 Q160 156 176 160", 6) + line("M256 166 Q244 156 228 160", 6) + line("M188 228 Q202 214 216 228", 7)
              + '<path d="M264 198 Q276 218 264 226 Q252 218 264 198Z" fill="#7FB2FF"/>'),
    "cheer": ("만세", "돌려받음·해결·좋은 소식", L_UP + R_UP + HAPPY_EYES + BIG_SMILE + star(52, 120) + star(350, 116, 18) + star(92, 60, 10) + star(318, 56, 12, "#7FB2FF") + star(70, 196, 8, "#7FB2FF")),
    "search": ("돋보기", "점검·조회·확인 방법", L_DOWN + arm("M304 250 Q326 246 336 218", 336, 218)
               + line("M338 214 L346 196", 12, "#2450C8") + '<circle cx="356" cy="164" r="34" fill="#BFD7FF" fill-opacity=".55" stroke="#3B6EF0" stroke-width="8"/>' + line("M340 152 Q348 140 362 140", 5, "#fff")
               + eye(164, 182) + eye(240, 180, 20, 7, -8, 7) + '<ellipse cx="202" cy="222" rx="7" ry="8" fill="#1A1A1A"/>'),
    "money": ("돈", "환급·보험금·금액 이야기", L_DOWN + R_HOLD + '<circle cx="338" cy="162" r="34" fill="#FFE45C" stroke="#E0BE2E" stroke-width="6"/>'
              + '<text x="338" y="175" font-size="38" fill="#8A6B00" font-family="Paperlogy,sans-serif" font-weight="900" text-anchor="middle">₩</text>' + HAPPY_EYES + BIG_SMILE),
    "point": ("콕", "핵심 짚기·순서 설명", L_HIP + arm("M304 246 Q330 238 350 210", 350, 210) + line("M352 206 L370 180", 13, NAVY) + EYES + SMILE
              + '<circle cx="72" cy="104" r="24" fill="#FFE45C" stroke="#E0BE2E" stroke-width="4"/><rect x="61" y="126" width="22" height="13" rx="4" fill="#9AA2B3"/>'
              + line("M72 62 L72 50", 6, "#FFE45C") + line("M36 84 L26 78", 6, "#FFE45C") + line("M108 84 L118 78", 6, "#FFE45C")),
    "stop":  ("멈춰", "서명 금지·해지 금지 같은 경고", L_HIP + R_HOLD + '<circle cx="338" cy="160" r="36" fill="#FF6B6B" stroke="#C93B3B" stroke-width="5"/>'
              + line("M324 146 L352 174", 10, "#fff") + line("M352 146 L324 174", 10, "#fff") + EYES + line("M148 162 L178 166", 7) + line("M256 162 L226 166", 7) + line("M190 222 L214 222", 7)),
}

def svg(name):
    return HEAD + POSES[name][2] + CHEEK + TAIL

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k in POSES:
        with open(os.path.join(OUT, f"bino-{k}.svg"), "w", encoding="utf-8") as f:
            f.write(svg(k))
    cells = "".join(f'<div class="c"><div class="i">{svg(k)}</div><b>{v[0]}</b><span>{v[1]}</span><i>{k}</i></div>' for k, v in POSES.items())
    html = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@import url("../fonts/fonts.css");
*{{box-sizing:border-box;margin:0}}body{{width:1600px;background:#121212;background-image:linear-gradient(#202020 2px,transparent 2px),linear-gradient(90deg,#202020 2px,transparent 2px);background-size:60px 60px;font-family:Paperlogy,sans-serif;color:#F5F5F5;padding:56px}}
h1{{font-size:56px;font-weight:900;letter-spacing:-.04em}}p{{font-size:26px;color:#AAA;margin:8px 0 32px}}
.g{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}}
.c{{background:#1C1C1C;border:2px solid #2E2E2E;border-radius:24px;padding:16px 16px 20px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.i{{width:250px}}.i svg{{display:block;width:100%}}
.c b{{font-size:32px;font-weight:900;margin-top:2px}}.c span{{font-size:21px;color:#AAA;margin-top:4px;line-height:1.35}}.c i{{font-style:normal;font-size:17px;color:#666;margin-top:8px}}
</style></head><body><h1>비노 포즈 12종</h1><p>보험비밀노트 마스코트 · 내용과 상황에 맞춰 골라 씁니다</p><div class="g">{cells}</div></body></html>"""
    p = os.path.join(ROOT, "_sheet.html")
    open(p, "w", encoding="utf-8").write(html)
    png = os.path.join(ROOT, "poses_sheet.png")
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--window-size=1600,1420", "--virtual-time-budget=3000", f"--screenshot={png}", "file://" + p], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    os.remove(p)
    import json
    json.dump({k: {"name": v[0], "use": v[1], "file": f"poses/bino-{k}.svg"} for k, v in POSES.items()},
              open(os.path.join(ROOT, "poses.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("ok", png)
