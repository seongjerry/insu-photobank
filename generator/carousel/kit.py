#!/usr/bin/env python3
"""보험비밀노트 캐러셀 제작 도구 (다크노트 · 1080x1350)

에피소드 파일(generator/carousel/episodes/cNN.py)이 SLIDES·MOTION·CAPTION 을 정의하고
    python3 generator/carousel/kit.py cNN
을 실행하면 publish/media/cNN-01.(jpg|mp4) ... 와 미리보기 시트가 만들어진다.

- 글꼴: generator/kit/fonts (페이퍼로지 제목·본문, 깍두기 숫자 포인트, 나눔펜 손글씨)
- 비노: generator/kit/mascot/poses/bino-<포즈>.svg  (poses.json 에 포즈별 쓰임새)
- 움직이는 장: 5초 반복 무음 영상 (배경음악은 본부장님이 모바일 업로드 때 직접 넣음)
- 표지: 상단 시리즈 문구·쪽번호 없음. covers.py 의 틀 4종(A1·B1·A2·B2)을 에피소드 번호 순서로 쓴다
- 비노는 표지(B)·마지막 장 + 중간 1장 정도만. 모든 장에 넣지 않는다
- 결과물은 텔레그램 전송까지만 (자동 게시 안 함)
"""
import importlib.util, json, os, pathlib, shutil, subprocess, sys, tempfile

R = pathlib.Path(__file__).resolve().parents[2]
FONTS = (R / "generator/kit/fonts/fonts.css").as_uri()
POSES = R / "generator/kit/mascot/poses"
MEDIA = R / "publish/media"
CHROME = "/usr/bin/google-chrome" if os.path.exists("/usr/bin/google-chrome") else None


def bino(pose, w, style=""):
    svg = (POSES / f"bino-{pose}.svg").read_text(encoding="utf-8")
    return f'<div class="bino" style="width:{w}px;{style}">{svg}</div>'


CSS = """
@import url("%s");
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Paperlogy,sans-serif;font-weight:500;color:#F5F5F5;letter-spacing:-.025em;word-break:keep-all;
 background-color:#121212;background-image:linear-gradient(#202020 2px,transparent 2px),linear-gradient(90deg,#202020 2px,transparent 2px);background-size:60px 60px}
.s{position:relative;width:1080px;height:1350px;padding:64px 72px 0;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;height:56px;flex:none}
.pen{font-family:NanumPen,cursive;letter-spacing:0;font-weight:400}
.top .pen{font-size:44px;color:#7FB2FF;transform:rotate(-2deg)}
.top .pg{font-size:24px;font-weight:600;color:#8C8C8C;border:2px solid #3A3A3A;border-radius:999px;padding:6px 18px}
.bot{position:absolute;left:72px;right:72px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-size:25px;color:#8C8C8C;font-weight:600}
.bot b{color:#FFE45C;font-weight:700}
h1{font-size:94px;font-weight:900;line-height:1.16;letter-spacing:-.05em}
h2{font-size:62px;font-weight:900;line-height:1.22;letter-spacing:-.045em;margin-top:34px}
.y{color:#FFE45C}.r{color:#FF6B6B}.b{color:#7FB2FF}
p{font-size:35px;line-height:1.5;color:#D6D6D6}
.lead{font-size:37px;line-height:1.5;color:#D6D6D6;margin-top:22px}
.lead b{color:#fff;font-weight:700}
.box{background:#1C1C1C;border:2px solid #2E2E2E;border-radius:28px;padding:30px 34px}
.rows{display:flex;flex-direction:column;gap:20px;margin-top:34px}
.row{display:flex;gap:24px;align-items:flex-start}
.num{flex:none;width:64px;height:64px;border-radius:18px;background:#FFE45C;color:#121212;font-family:Kkakdugi,Paperlogy;font-weight:700;font-size:34px;display:flex;align-items:center;justify-content:center}
.row h3{font-size:37px;font-weight:800;line-height:1.3;color:#fff}
.row p{font-size:30px;line-height:1.45;margin-top:6px;color:#BDBDBD}
.note{background:#FFF27A;color:#222;padding:30px 36px;transform:rotate(-2deg);box-shadow:0 14px 34px rgba(0,0,0,.6);font-weight:800;font-size:42px;line-height:1.3;position:relative}
.note:before{content:"";position:absolute;top:-16px;left:50%%;width:120px;height:32px;margin-left:-60px;background:rgba(255,255,255,.55);transform:rotate(-3deg)}
.src{font-size:22px;color:#7A7A7A;margin-top:auto;padding-bottom:104px;line-height:1.4}
.bino svg{display:block;width:100%%;height:auto}
.mini{position:absolute;right:56px;top:118px}
.stat{display:flex;gap:20px;margin-top:30px}
.stat .box{flex:1;text-align:center;padding:28px 16px}
.stat .k{font-size:26px;color:#9E9E9E;font-weight:600}
.stat .v{font-family:Kkakdugi,Paperlogy;font-size:80px;font-weight:700;line-height:1.1;margin-top:6px;letter-spacing:-.02em}
.stat .d{font-size:25px;color:#BDBDBD;margin-top:6px;line-height:1.35}
table{width:100%%;border-collapse:separate;border-spacing:0;margin-top:20px;font-size:29px;line-height:1.36}
th,td{padding:14px 18px;text-align:left;vertical-align:top;border-bottom:2px solid #2E2E2E}
th{font-size:27px;color:#9E9E9E;font-weight:600}
thead th{font-size:33px;color:#fff;font-weight:900;border-bottom:3px solid #FFE45C}
thead th.new{color:#FFE45C}
td{color:#E0E0E0}
tbody th{width:180px}
.tag{display:inline-block;background:#FFE45C;color:#121212;font-size:22px;font-weight:900;border-radius:8px;padding:2px 10px;margin-left:8px;vertical-align:middle}
.qa{display:flex;flex-direction:column;gap:16px;margin-top:30px}
.qa .box{padding:22px 30px}
.qa .q{font-size:32px;font-weight:800;color:#fff;line-height:1.35}
.qa .q:before{content:"Q. ";color:#7FB2FF}
.qa .a{font-size:28px;color:#C8C8C8;line-height:1.45;margin-top:8px}
.ck{display:flex;flex-direction:column;gap:14px;margin-top:8px;font-family:NanumPen,cursive;font-size:54px;line-height:1.2;color:#222;font-weight:400}
.ck span:before{content:"☐ "}
.chip{display:inline-block;align-self:flex-start;background:#FFE45C;color:#121212;font-weight:800;font-size:30px;border-radius:999px;padding:10px 24px}
""" % FONTS

HELP = """<script>
const c=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-x,3);
const eb=x=>{const k=1.70158;return 1+(k+1)*Math.pow(x-1,3)+k*Math.pow(x-1,2)};
const $=s=>document.querySelector(s);
</script>"""


def page(ep, i, body, hint, motion_js=""):
    n = len(ep.SLIDES)
    top = "" if i == 1 else f'<div class="top"><span class="pen">{ep.SERIES}</span><span class="pg">{ep.LABEL} · {i}/{n}</span></div>'  # 표지는 상단 문구·쪽번호 없이
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{CSS}</style>{HELP}</head><body>
<div class="s">
 {top}
 {body}
 <div class="bot"><span>@insu_secretnote</span><b>{hint}</b></div>
</div>{"<script>" + motion_js + "</script>" if motion_js else ""}</body></html>"""


def load(ep_id):
    f = R / "generator/carousel/episodes" / f"{ep_id}.py"
    spec = importlib.util.spec_from_file_location(ep_id, f); m = importlib.util.module_from_spec(spec)
    sys.modules[ep_id] = m; spec.loader.exec_module(m)
    m.ID = ep_id
    return m


def build(ep_id, preview_only=False):
    from playwright.sync_api import sync_playwright
    ep = load(ep_id)
    n = len(ep.SLIDES); hints = ["넘겨서 보기 →"] * (n - 1) + ["저장 · 공유 ♥"]
    work = pathlib.Path(tempfile.mkdtemp(prefix=f"{ep_id}_")); MEDIA.mkdir(parents=True, exist_ok=True)
    outs = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"]) if CHROME else pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        jobs = [(1, k, v) for k, v in getattr(ep, "COVERS", {}).items()] + [(i, "", b) for i, b in enumerate(ep.SLIDES, 1) if not (i == 1 and getattr(ep, "COVERS", None))]
        for i, var, body in jobs:
            mo = getattr(ep, "MOTION", {}).get(f"{i}{var}")
            html = work / f"s{i:02d}{var}.html"
            html.write_text(page(ep, i, body, hints[i - 1], mo["js"] if mo else ""), encoding="utf-8")
            pg.goto(html.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
            if mo and not preview_only:
                out = MEDIA / f"{ep_id}-{i:02d}{var}.mp4"; motion(pg, mo, out, work); outs.append(out)
            else:
                if mo: pg.evaluate(f"window.setT({mo.get('still_t', mo['dur'] - 1)})")
                png = work / f"{i:02d}{var}.png"; pg.screenshot(path=str(png))
                out = MEDIA / f"{ep_id}-{i:02d}{var}.jpg"
                subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(png), "-q:v", "2", str(out)], check=True)
                outs.append(out)
        b.close()
    sheet(outs, work, R / f"publish/media/{ep_id}-sheet.jpg")
    shutil.rmtree(work)
    print("ok", ep_id, [o.name for o in outs])
    return ep, outs


def motion(pg, mo, out, work, fps=30):
    dur = mo["dur"]; frames = work / "fr"; frames.mkdir(exist_ok=True)
    for k in range(int(dur * fps)):
        pg.evaluate(f"window.setT({k / fps})")
        pg.screenshot(path=str(frames / f"{k:05d}.jpg"), type="jpeg", quality=92)
    silent = work / "silent.mp4"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-framerate", str(fps), "-i", str(frames / "%05d.jpg"),
                    "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", str(silent)], check=True)
    shutil.rmtree(frames)
    tmp = out.with_suffix(".tmp.mp4")
    if not mo.get("bgm"):
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(silent), "-c", "copy", "-movflags", "+faststart", str(tmp)], check=True)
        tmp.rename(out); return
    bgm = R / "bgm" / mo["bgm"]; ofs = mo.get("bgm_offset", 0)
    af = f"atrim=start={ofs}:duration={dur},asetpts=PTS-STARTPTS,afade=t=in:d=0.4,afade=t=out:st={dur - 0.7}:d=0.7,loudnorm=I=-20:TP=-2,aresample=44100"
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(silent), "-i", str(bgm), "-filter_complex", f"[1:a]{af}[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(tmp)], check=True)
    tmp.rename(out)


def sheet(outs, work, dst):
    from PIL import Image
    ims = []
    for o in outs:
        if o.suffix == ".mp4":
            f = work / (o.stem + "_f.jpg")
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-sseof", "-1.2", "-i", str(o), "-frames:v", "1", str(f)], check=True)
            ims.append(Image.open(f))
        else:
            ims.append(Image.open(o))
    w, h = 432, 540; cols = 5; rows = (len(ims) + cols - 1) // cols
    s = Image.new("RGB", (w * cols, h * rows), "#333")
    for i, im in enumerate(ims): s.paste(im.convert("RGB").resize((w, h)), ((i % cols) * w, (i // cols) * h))
    s.save(dst, quality=88)


if __name__ == "__main__":
    build(sys.argv[1], preview_only="--preview" in sys.argv)
