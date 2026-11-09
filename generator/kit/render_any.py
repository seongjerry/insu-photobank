import sys, subprocess, os, json
from playwright.sync_api import sync_playwright
html, durf, outdir, mode = sys.argv[1:5]; FPS=30
durs=json.load(open(durf))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file://"+os.path.abspath(html)); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1000)
    os.makedirs(outdir,exist_ok=True)
    if mode=="preview":
        for i,d in enumerate(durs):
            pg.evaluate(f"render({i},{d-0.05})"); pg.screenshot(path=f"{outdir}/p{i:02d}.jpg",type="jpeg",quality=80)
    else:
        for i,d in enumerate(durs):
            tmp,out=f"{outdir}/s{i:02d}.tmp.mp4",f"{outdir}/s{i:02d}.mp4"
            ff=subprocess.Popen(["ffmpeg","-y","-v","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-","-c:v","libx264","-crf","18","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS),tmp],stdin=subprocess.PIPE)
            for f in range(round(d*FPS)):
                pg.evaluate(f"render({i},{f/FPS})"); ff.stdin.write(pg.screenshot(type="jpeg",quality=92))
            ff.stdin.close()
            if ff.wait()==0: os.replace(tmp,out)
    b.close()
