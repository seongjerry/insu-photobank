#!/usr/bin/env python3
"""insu_magazine 렌더러 v2 — 검정 배경·흰 글씨·빨간 강조·하단 insu_magazine/출처·손글씨 멘트 한 줄.

캐러셀: JSON → 1080x1350 PNG + caption.txt
릴스  : JSON → 1080x1920 mp4(30fps) + cover.png + caption.txt
사용   : python3 render.py content/xxx.json [out_dir]
"""
import json, sys, re, html, pathlib, subprocess, shutil, tempfile
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
FONTS = (ROOT / "assets/fonts").as_uri()

BASE_CSS = f"""
@font-face{{font-family:'PT';src:url('{FONTS}/Pretendard-Black.otf');font-weight:900}}
@font-face{{font-family:'PT';src:url('{FONTS}/Pretendard-ExtraBold.otf');font-weight:800}}
@font-face{{font-family:'PT';src:url('{FONTS}/Pretendard-Bold.otf');font-weight:700}}
@font-face{{font-family:'PT';src:url('{FONTS}/Pretendard-SemiBold.otf');font-weight:600}}
@font-face{{font-family:'PT';src:url('{FONTS}/Pretendard-Medium.otf');font-weight:500}}
@font-face{{font-family:'MJ';src:url('{FONTS}/nanum-myeongjo-korean-400-normal.woff2');font-weight:400}}
@font-face{{font-family:'MJ';src:url('{FONTS}/nanum-myeongjo-korean-700-normal.woff2');font-weight:700}}
@font-face{{font-family:'PEN';src:url('{FONTS}/nanum-pen-script-korean-400-normal.woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:#000;color:#fff;font-family:'PT','Noto Sans CJK KR',sans-serif;letter-spacing:-0.02em;word-break:keep-all;-webkit-font-smoothing:antialiased;overflow:hidden}}
.red{{color:#FF2B2B}}
.head{{text-align:center;font-weight:900;line-height:1.22;text-shadow:0 3px 0 #000,0 0 18px rgba(0,0,0,.6)}}
.head .l1{{color:#FF2B2B}}
.head .l2{{color:#fff}}
.quote{{font-family:'MJ',serif;color:#EDEDED;text-align:center;font-weight:400;letter-spacing:0}}
.quote:before{{content:'– '}} .quote:after{{content:' –'}}
.logo{{font-family:'PT';font-weight:900;font-style:italic;text-align:center;letter-spacing:-0.03em;color:#fff}}
.src{{font-family:'PT';font-weight:700;text-align:center;color:#C8C8C8;letter-spacing:0}}
.src:before{{content:'– '}} .src:after{{content:' –'}}
.wm{{position:absolute;left:0;right:0;text-align:center;font-weight:900;font-style:italic;color:rgba(255,255,255,.22);pointer-events:none}}
.panel{{position:relative;width:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.p-text .ln{{font-weight:800;line-height:1.3}}
.p-num .v{{font-weight:900;color:#FF2B2B;line-height:1;letter-spacing:-0.04em;font-variant-numeric:tabular-nums}}
.p-num .v small{{color:#fff;letter-spacing:-0.02em}}
.p-num .lb{{font-weight:700;color:#DADADA}}
.p-num .ln{{font-weight:700;color:#F2F2F2;line-height:1.5}}
.p-compare{{gap:14px}}
.p-compare .lb{{font-weight:700;color:#C8C8C8}}
.p-compare .from{{font-weight:800;color:#8A8A8A;text-decoration:line-through;text-decoration-color:#FF2B2B;text-decoration-thickness:6px}}
.p-compare .arrow{{color:#FF2B2B;font-weight:900}}
.p-compare .to{{font-weight:900;color:#fff}}
.p-compare .tag{{display:inline-block;background:#FF2B2B;color:#fff;font-weight:800;border-radius:12px;padding:10px 26px;margin-top:10px}}
.bars{{width:100%;display:flex;flex-direction:column}}
.bar{{display:grid;grid-template-columns:170px 1fr 130px;align-items:center;gap:18px;font-weight:800}}
.bar .t{{height:34px;background:#2A2A2A;border-radius:6px;overflow:hidden}}
.bar .f{{height:100%;background:#fff}} .bar.hot .f{{background:#FF2B2B}}
.bar .n{{text-align:right;font-variant-numeric:tabular-nums}}
.unit{{color:#9A9A9A;font-weight:600}}
.list{{width:100%;display:flex;flex-direction:column}}
.list .it{{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #2A2A2A;font-weight:800}}
.list .it span:last-child{{color:#FF2B2B;font-weight:800}}
.note{{color:#DADADA;font-weight:700}}
.check{{width:100%;display:flex;flex-direction:column;align-items:flex-start}}
.check .it{{display:flex;align-items:center;gap:22px;font-weight:800}}
.check .it b{{color:#FF2B2B;font-weight:900}}
.cta .ln{{font-weight:800;line-height:1.5}}
.cta .srcs{{color:#B0B0B0;font-weight:600;line-height:1.55;letter-spacing:0}}
.cta .srcs b{{color:#fff;display:block;margin-bottom:6px}}
.cta .disc{{color:#8A8A8A;font-weight:500;line-height:1.5;letter-spacing:0}}
"""

def esc(s): return html.escape(s)
def mark(s):
    """[[텍스트]] → 빨간 강조"""
    return re.sub(r"\[\[(.+?)\]\]", lambda m: f'<span class="red">{m.group(1)}</span>', esc(s))

def panel_html(p, big):
    """big=True: 캐러셀(여유 큼), False: 릴스."""
    t = p["type"]
    if t == "text":
        k = len(p["lines"])
        fs = (72 if k <= 4 else 58 if k <= 6 else 50) if big else 86
        lines = "".join(f'<div class="ln" style="font-size:{fs}px">{mark(l) if l else "&nbsp;"}</div>' for l in p["lines"])
        cta = f'<div class="ln" style="font-size:40px;margin-top:40px;color:#DADADA">{mark(p["cta"])}</div>' if p.get("cta") else ""
        return f'<div class="panel p-text">{lines}{cta}</div>'
    if t == "photo":
        # 기존 게시물처럼 사진 패널 + 사진 위 캡션 한 줄. p["photo"]: 로컬 경로 / p["keywords"]: 포토뱅크 키워드
        src = pathlib.Path(p["photo"]).resolve().as_uri() if p.get("photo") else ""
        cap = f'<div style="position:absolute;left:0;right:0;bottom:0;padding:22px 30px;background:linear-gradient(transparent,rgba(0,0,0,.85));font-size:36px;font-weight:800;text-align:center">{mark(p["caption"])}</div>' if p.get("caption") else ""
        return f'<div class="panel" style="height:100%"><div style="position:relative;width:100%;height:100%;background:#111 url(\'{src}\') center/cover;border-radius:6px;overflow:hidden">{cap}</div></div>'
    if t == "number":
        if big:
            lines = "".join(f'<div class="ln" style="font-size:44px">{mark(l)}</div>' for l in p.get("lines", []))
            return f'<div class="panel p-num"><div class="v" style="font-size:200px">{esc(p["value"])}</div>' \
                   f'<div class="lb" style="font-size:34px;margin:14px 0 36px">{esc(p["label"])}</div>{lines}</div>'
        dec = 1 if isinstance(p["value"], float) else 0
        return f'<div class="panel p-num"><div class="lb" style="font-size:46px;margin-bottom:10px">{esc(p["label"])}</div>' \
               f'<div class="v" style="font-size:250px" data-count="{p["value"]}" data-dec="{dec}" data-prefix="{esc(p["prefix"])}"><span>{esc(p["prefix"])}0</span><small style="font-size:120px">{esc(p["unit"])}</small></div></div>'
    if t == "compare":
        return f'<div class="panel p-compare"><div class="lb" style="font-size:36px">{esc(p["label"])}</div>' \
               f'<div class="from" style="font-size:66px">{esc(p["from"])}</div><div class="arrow" style="font-size:60px">▼</div>' \
               f'<div class="to" style="font-size:96px">{esc(p["to"])}</div><div class="tag" style="font-size:38px">{esc(p["tag"])}</div></div>'
    if t == "bars":
        mx = max(v for _, v in p["bars"])
        bars = "".join(f'<div class="bar{" hot" if i == 0 else ""}" style="font-size:38px"><span>{esc(n)}</span><div class="t"><div class="f" style="width:{v/mx*100:.1f}%"></div></div><span class="n">{v}</span></div>' for i, (n, v) in enumerate(p["bars"]))
        lines = "".join(f'<div class="ln" style="font-size:44px;font-weight:700;line-height:1.5">{mark(l)}</div>' for l in p.get("lines", []))
        return f'<div class="panel"><div class="bars" style="gap:26px">{bars}</div><div class="unit" style="font-size:28px;margin:18px 0 40px">{esc(p["unit"])}</div>{lines}</div>'
    if t == "list":
        items = "".join(f'<div class="it" style="font-size:44px;padding:26px 6px"><span>{esc(a)}</span><span>{esc(b)}</span></div>' for a, b in p["items"])
        return f'<div class="panel"><div class="list">{items}</div><div class="note" style="font-size:34px;margin-top:40px">📍 {esc(p["note"])}</div></div>'
    if t == "check":
        items = "".join(f'<div class="it" style="font-size:46px"><b>{i+1}.</b><span>{esc(x)}</span></div>' for i, x in enumerate(p["items"]))
        return f'<div class="panel"><div class="check" style="gap:30px;padding-left:60px">{items}</div></div>'
    if t == "cta":
        lines = "".join(f'<div class="ln" style="font-size:52px">{mark(l)}</div>' for l in p["lines"])
        srcs = "".join(f'{esc(s)}<br>' for s in p.get("sources", []))
        return f'<div class="panel cta">{lines}<div class="srcs" style="font-size:26px;margin-top:70px"><b>출처</b>{srcs}</div>' \
               f'<div class="disc" style="font-size:22px;margin-top:22px;padding:0 20px">{esc(p.get("disclaimer",""))}</div></div>'
    raise ValueError(t)

# ───────────────── 캐러셀 ─────────────────
def carousel_slide(d, s, i, n):
    pin = '<div style="position:absolute;top:70px;right:80px;font-size:64px;transform:rotate(20deg)">📌</div>' if s.get("pin") else ""
    src = s.get("src") or d["source_short"]
    body = f"""
<div style="position:relative;width:1080px;height:1350px;padding:0 70px">
 {pin}
 <div class="head" style="font-size:78px;padding-top:112px"><div class="l1">{esc(s["head"][0])}</div><div class="l2">{esc(s["head"][1])}</div></div>
 <div style="position:absolute;top:430px;left:70px;right:70px;height:600px;display:flex;align-items:center;justify-content:center">{panel_html(s["panel"], True)}</div>
 <div class="wm" style="{'top:690px;font-size:72px;opacity:.6' if s["panel"]["type"]=="photo" else 'top:1000px;font-size:46px;opacity:.55'}">insu_magazine</div>
 <div class="quote" style="position:absolute;left:70px;right:70px;top:1070px;font-size:38px">{esc(s["quote"])}</div>
 <div class="logo" style="position:absolute;left:0;right:0;top:1150px;font-size:66px">insu_magazine</div>
 <div class="src" style="position:absolute;left:0;right:0;top:1245px;font-size:26px">{esc(src)}</div>
 <div style="position:absolute;right:80px;bottom:46px;font-size:26px;color:#777;font-weight:700">{i}/{n}</div>
</div>"""
    return f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{BASE_CSS}html,body{{width:1080px;height:1350px}}</style></head><body>{body}</body></html>'

def render_carousel(d, out):
    slides = d["slides"]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            f = out / f"_slide{i:02d}.html"; f.write_text(carousel_slide(d, s, i, len(slides)), encoding="utf-8")
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(150)
            pg.screenshot(path=str(out / f"{i:02d}.png")); f.unlink()
        b.close()
    (out / "caption.txt").write_text(d["caption"], encoding="utf-8")
    print(f"ok carousel {len(slides)} slides → {out}")

# ───────────────── 릴스 ─────────────────
REEL_CSS = """
html,body{width:1080px;height:1920px}
.stage{position:relative;width:1080px;height:1920px;overflow:hidden}
.bg{position:absolute;left:-60px;top:380px;width:1200px;height:1000px;background-size:cover;background-position:center;filter:brightness(.55) saturate(.85);transform-origin:center;animation:kb 28s linear both}
.bg:after{content:'';position:absolute;inset:0;background:linear-gradient(#000 0%,rgba(0,0,0,0) 18%,rgba(0,0,0,0) 82%,#000 100%)}
@keyframes kb{from{transform:scale(1.02)}to{transform:scale(1.14)}}
.head{position:absolute;left:60px;right:60px;top:300px;font-size:86px;animation:pop .6s cubic-bezier(.2,.9,.3,1.25) both}
.scene{position:absolute;left:60px;right:60px;top:640px;height:560px;display:none;align-items:center;justify-content:center}
.scene .panel{animation:up .5s cubic-bezier(.2,.8,.2,1) both}
.scene .ln:nth-child(2){animation:up .5s .14s both;opacity:0}
.scene .ln:nth-child(3){animation:up .5s .28s both;opacity:0}
.qwrap{position:absolute;left:60px;right:60px;top:1250px;height:120px;display:flex;align-items:center;justify-content:center}
.qwrap .quote{font-size:40px;display:none;animation:fade .45s .25s both;opacity:0}
.logo{position:absolute;left:0;right:0;top:1400px;font-size:74px}
.srcl{position:absolute;left:0;right:0;top:1500px;font-size:28px}
.prog{position:absolute;left:60px;right:60px;top:1590px;height:6px;background:#2A2A2A}
.prog i{display:block;height:100%;background:#FF2B2B;width:0}
@keyframes up{from{opacity:0;transform:translateY(50px)}to{opacity:1;transform:none}}
@keyframes pop{from{opacity:0;transform:scale(.7)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
"""

REEL_JS = """
window.__T=%f;
window.seek=(t)=>{
  document.querySelector('.prog i').style.width=(t/window.__T*100)+'%%';
  for(const a of document.querySelector('.bg').getAnimations()){a.pause();a.currentTime=t*1000;}
  for(const a of document.querySelector('.head').getAnimations()){a.pause();a.currentTime=t*1000;}
  document.querySelectorAll('.scene,.qwrap .quote').forEach(el=>{
    const s=+el.dataset.s,e=+el.dataset.e,on=t>=s&&t<e;
    el.style.display=on?(el.classList.contains('scene')?'flex':'block'):'none';
    if(!on)return;
    const lt=(t-s)*1000;
    for(const a of el.getAnimations({subtree:true})){a.pause();a.currentTime=lt;}
    const big=el.querySelector('[data-count]');
    if(big){const v=+big.dataset.count,dec=+big.dataset.dec;let p=Math.min(1,Math.max(0,(lt-200)/1500));p=1-Math.pow(1-p,3);
      big.firstElementChild.textContent=big.dataset.prefix+(v*p).toFixed(dec);}
  });
};
"""

def render_reel(d, out):
    fps = d.get("fps", 30); T = d["scenes"][-1]["t"][1]
    bg = (ROOT / d["bg_photo"]).as_uri() if d.get("bg_photo") else ""
    scenes = "".join(f'<div class="scene" data-s="{s["t"][0]}" data-e="{s["t"][1]}">{panel_html(s["panel"], False)}</div>' for s in d["scenes"])
    quotes = "".join(f'<div class="quote" data-s="{s["t"][0]}" data-e="{s["t"][1]}">{esc(s["quote"])}</div>' for s in d["scenes"])
    page = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{BASE_CSS}{REEL_CSS}</style></head><body>
<div class="stage">
 <div class="bg" style="background-image:url('{bg}')"></div>
 <div class="wm" style="top:1165px;font-size:54px;opacity:.6">insu_magazine</div>
 <div class="head"><div class="l1">{esc(d["head"][0])}</div><div class="l2">{esc(d["head"][1])}</div></div>
 {scenes}
 <div class="qwrap">{quotes}</div>
 <div class="logo">insu_magazine</div>
 <div class="src srcl">{esc(d["source_short"])}</div>
 <div class="prog"><i></i></div>
</div><script>{REEL_JS % T}</script></body></html>"""
    hf = out / "reel.html"; hf.write_text(page, encoding="utf-8")
    frames = pathlib.Path(tempfile.mkdtemp(prefix="frames_")); n = int(T * fps)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto(hf.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
        for i in range(n):
            pg.evaluate(f"seek({i/fps})"); pg.screenshot(path=str(frames / f"{i:05d}.jpg"), type="jpeg", quality=92)
        b.close()
    mp4 = out / f"{d['id']}.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(fps), "-i", str(frames / "%05d.jpg"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-preset", "medium", "-movflags", "+faststart", str(mp4)], check=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", "1.0", "-i", str(mp4), "-frames:v", "1", str(out / "cover.png")], check=True)
    shutil.rmtree(frames)
    if d.get("audio"):
        mix_audio(d, out, mp4, T)
    (out / "caption.txt").write_text(d["caption"], encoding="utf-8")
    print(f"ok reel {n} frames {T}s → {mp4}")

def mix_audio(d, out, mp4, T):
    """audio: {"narration_dir": "tts/out/<id>" (NN.mp3, 장면 순서), "bgm": "path.mp3", "bgm_db": -20, "sfx": true}
    나레이션은 각 장면 시작 시점에 배치, BGM은 길이에 맞춰 반복·페이드, 효과음은 장면 전환 휙 + 숫자 카운트 틱."""
    a = d["audio"]; inputs = []; filters = []; mix = []
    def add(path):
        inputs.extend(["-i", str(path)]); return len(inputs) // 2  # 0번은 영상
    # 나레이션
    nd = a.get("narration_dir")
    if nd:
        for i, s in enumerate(d["scenes"], 1):
            f = (ROOT / nd / f"{i:02d}.mp3")
            if f.exists():
                k = add(f); start = int((s["t"][0] + a.get("lead", 0.25)) * 1000)
                filters.append(f"[{k}:a]adelay={start}|{start},volume=1.0[n{i}]"); mix.append(f"[n{i}]")
    # BGM
    if a.get("bgm") and (ROOT / a["bgm"]).exists():
        k = add(ROOT / a["bgm"]); db = a.get("bgm_db", -20)
        filters.append(f"[{k}:a]aloop=loop=-1:size=2e9,atrim=0:{T},volume={db}dB,afade=t=in:d=1,afade=t=out:st={T-1.5}:d=1.5[bgm]"); mix.append("[bgm]")
    # 효과음(합성)
    if a.get("sfx", True):
        sfx = []
        for i, s in enumerate(d["scenes"]):
            st = s["t"][0]
            if i > 0:  # 장면 전환 휙
                filters.append(f"anoisesrc=d=0.3:c=pink:r=44100:a=0.5,lowpass=f=1200,afade=t=in:d=0.05,afade=t=out:st=0.08:d=0.22,volume=-16dB,adelay={int(st*1000)}|{int(st*1000)}[w{i}]"); sfx.append(f"[w{i}]")
            if s["panel"].get("type") == "number":  # 카운트업 틱 8회
                for j in range(8):
                    ms = int((st + 0.25 + j * 0.17) * 1000)
                    filters.append(f"sine=f=1700:d=0.025:r=44100,afade=t=out:d=0.02,volume=-22dB,adelay={ms}|{ms}[k{i}_{j}]"); sfx.append(f"[k{i}_{j}]")
        if sfx:
            filters.append("".join(sfx) + f"amix=inputs={len(sfx)}:normalize=0[sfx]"); mix.append("[sfx]")
    if not mix: return
    filters.append(f"anullsrc=r=44100:cl=stereo:d={T}[sil]"); mix.append("[sil]")
    filters.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=longest,apad=whole_dur={T},atrim=0:{T},aresample=44100[aout]")
    tmp = out / "_with_audio.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp4), *inputs, "-filter_complex", ";".join(filters),
                    "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", str(tmp)], check=True)
    tmp.replace(mp4)
    print("audio mixed:", [m.strip("[]") for m in mix])

def resolve_photos(d):
    """panel.type=photo 에 photo 경로가 없고 keywords만 있으면 포토뱅크에서 가져온다. 릴스 bg_photo도 동일."""
    try:
        import photobank
    except Exception:
        return
    used = set()
    def _pick(kws, orient=None, prefer=(), avoid=()):
        try:
            ph = photobank.pick(kws, orient, exclude=used, prefer=prefer, avoid=avoid)
            if ph: used.add(ph["id"]); return str(photobank.fetch(ph))
        except Exception as e:
            print("photobank skip:", e)
    for s in d.get("slides", []):
        p = s.get("panel", {})
        if p.get("type") == "photo" and not p.get("photo") and p.get("keywords"):
            p["photo"] = _pick(p["keywords"], None, p.get("prefer", ()), p.get("avoid", ()))
    if d.get("format") == "reel" and not d.get("bg_photo") and d.get("bg_keywords"):
        d["bg_photo"] = _pick(d["bg_keywords"], "portrait", d.get("bg_prefer", ()), d.get("bg_avoid", ()))

def main():
    src = pathlib.Path(sys.argv[1]); d = json.loads(src.read_text(encoding="utf-8"))
    resolve_photos(d)
    out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else ROOT / "out" / d["id"]).resolve(); out.mkdir(parents=True, exist_ok=True)
    (render_reel if d["format"] == "reel" else render_carousel)(d, out)

if __name__ == "__main__":
    main()
