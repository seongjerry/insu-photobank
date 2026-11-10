# 비노: 보험비밀노트 마스코트 (네이비 스프링노트 + 노란 포스트잇 머리 + 파란 펜)
NAVY="#22305C"; NAVY2="#1A2548"; PAGE="#FFFDF5"; YEL="#FFE45C"; BLUE="#3B6EF0"; PINK="#FF9DB1"; INK="#1A1A1A"; RED="#FF6B6B"
def body():
    s=[]
    # 그림자
    s.append(f'<ellipse cx="200" cy="372" rx="110" ry="14" fill="#000" opacity=".12"/>')
    # 다리
    s.append(f'<rect x="150" y="320" width="26" height="40" rx="13" fill="{NAVY2}"/><rect x="224" y="320" width="26" height="40" rx="13" fill="{NAVY2}"/>')
    s.append(f'<ellipse cx="160" cy="360" rx="22" ry="12" fill="{NAVY2}"/><ellipse cx="240" cy="360" rx="22" ry="12" fill="{NAVY2}"/>')
    # 포스트잇 머리(뒤)
    s.append(f'<g transform="rotate(-12 230 92)"><rect x="196" y="58" width="74" height="70" rx="6" fill="{YEL}"/><path d="M196 110 L214 128 L196 128Z" fill="#E8C93A"/></g>')
    # 표지(몸통)
    s.append(f'<rect x="92" y="88" width="216" height="246" rx="40" fill="{NAVY}"/>')
    # 속지(얼굴면)
    s.append(f'<rect x="112" y="104" width="182" height="214" rx="30" fill="{PAGE}"/>')
    # 줄
    for y in (250,276):
        s.append(f'<line x1="134" y1="{y}" x2="272" y2="{y}" stroke="#D8E1F2" stroke-width="5" stroke-linecap="round"/>')
    # 스프링
    for y in (128,168,208,248,288):
        s.append(f'<rect x="84" y="{y-7}" width="40" height="14" rx="7" fill="#C9CED9" stroke="#9AA2B3" stroke-width="3"/>')
    # 자물쇠 고리(비밀)
    s.append(f'<rect x="296" y="196" width="26" height="40" rx="8" fill="{YEL}" stroke="#E0BE2E" stroke-width="3"/><circle cx="309" cy="212" r="5" fill="{NAVY}"/><rect x="307" y="214" width="4" height="10" rx="2" fill="{NAVY}"/>')
    return "".join(s)
def eyes(kind):
    if kind=="smile":   # 웃는 눈
        return f'<path d="M150 186 Q164 170 178 186" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/><path d="M226 186 Q240 170 254 186" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    if kind=="wink":
        return f'<circle cx="164" cy="182" r="15" fill="{INK}"/><circle cx="169" cy="176" r="5" fill="#fff"/><path d="M226 184 Q240 172 254 184" fill="none" stroke="{INK}" stroke-width="8" stroke-linecap="round"/>'
    if kind=="wow":
        return f'<circle cx="164" cy="180" r="19" fill="{INK}"/><circle cx="171" cy="172" r="7" fill="#fff"/><circle cx="240" cy="180" r="19" fill="{INK}"/><circle cx="247" cy="172" r="7" fill="#fff"/>'
    return f'<circle cx="164" cy="182" r="15" fill="{INK}"/><circle cx="169" cy="176" r="5" fill="#fff"/><circle cx="240" cy="182" r="15" fill="{INK}"/><circle cx="245" cy="176" r="5" fill="#fff"/>'
def mouth(kind):
    m={"smile":f'<path d="M188 214 Q202 230 216 214" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
       "o":f'<ellipse cx="202" cy="222" rx="11" ry="14" fill="{INK}"/><ellipse cx="202" cy="228" rx="6" ry="5" fill="{RED}"/>',
       "shh":f'<path d="M192 220 L212 220" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
       "grin":f'<path d="M184 210 Q202 240 220 210 Z" fill="{INK}"/><path d="M192 224 Q202 232 212 224" fill="{RED}"/>'}
    return m[kind]
def blush(): return f'<ellipse cx="146" cy="212" rx="14" ry="8" fill="{PINK}" opacity=".8"/><ellipse cx="258" cy="212" rx="14" ry="8" fill="{PINK}" opacity=".8"/>'
def pen(x,y,rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><rect x="-7" y="-46" width="14" height="74" rx="5" fill="{BLUE}"/>'
            f'<rect x="-7" y="-46" width="14" height="14" rx="4" fill="#2450C8"/><path d="M-7 28 L7 28 L0 44Z" fill="#F2D3A8"/><path d="M-2.5 38 L2.5 38 L0 44Z" fill="{INK}"/></g>')
def arm(x1,y1,x2,y2): return f'<path d="M{x1} {y1} Q{(x1+x2)/2} {y1} {x2} {y2}" fill="none" stroke="{NAVY}" stroke-width="20" stroke-linecap="round"/><circle cx="{x2}" cy="{y2}" r="14" fill="{NAVY}"/>'
POSES={
 "basic": lambda: arm(100,250,62,212)+arm(304,250,340,262)+pen(352,236,20)+eyes("dot")+mouth("smile")+blush(),
 "shh":   lambda: arm(300,250,216,222)+arm(100,250,64,290)+eyes("wink")+mouth("shh")+blush()+'<g fill="#7FB2FF" font-family="Pretendard" font-weight="900"><text x="300" y="120" font-size="34">쉿!</text></g>',
 "wow":   lambda: arm(100,240,58,170)+arm(304,240,346,170)+eyes("wow")+mouth("o")+blush()+f'<g fill="{RED}"><rect x="186" y="18" width="16" height="44" rx="8"/><circle cx="194" cy="76" r="9"/></g>',
 "check": lambda: arm(100,250,64,290)+arm(304,250,338,190)+f'<circle cx="338" cy="168" r="30" fill="#fff" stroke="{BLUE}" stroke-width="6"/><path d="M324 168 L335 180 L354 156" fill="none" stroke="{BLUE}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'+eyes("smile")+mouth("grin")+blush(),
}
for k,f in POSES.items():
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">{body()}{f()}</svg>'
    open(f"bino_{k}.svg","w").write(svg)
print("ok")
