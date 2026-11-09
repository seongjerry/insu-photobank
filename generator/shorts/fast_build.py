# 사용: python3 fast_build.py <html> <tts_out_dir> <prefix> <out.mp4> [bgm] [thumb.jpg]
# 공백 제거 빠른 편집: 문장 안 쉼 축소 + 1.2배속 + 장면 = 음성+0.2초(마지막 +0.9), 애니메이션은 음성 길이 안으로 압축
import sys,os,re,json,glob,subprocess,shutil,numpy as np,scipy.io.wavfile as wf
from playwright.sync_api import sync_playwright
html,ttsdir,pf,out=sys.argv[1:5]; bgm=sys.argv[5] if len(sys.argv)>5 else '/home/claude/bgm/bgm_04_upbeat_pluck.wav'
thumb=sys.argv[6] if len(sys.argv)>6 else None
os.chdir('/home/claude/build'); base=html.replace('.html','_base.html')
if not os.path.exists(base): shutil.copy(html,base)
mp3=sorted(glob.glob(f'{ttsdir}/*.mp3')); N=len(mp3)
AF="silenceremove=start_periods=1:start_threshold=-45dB:stop_periods=-1:stop_duration=0.15:stop_threshold=-42dB:stop_silence=0.12,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo=1.2"
for i,f in enumerate(mp3,1): subprocess.run(['ffmpeg','-y','-v','error','-i',f,'-af',AF,'-ar','44100','-ac','2',f'{pf}a_{i:02d}.wav'],check=True)
vd=[len(wf.read(f'{pf}a_{i:02d}.wav')[1])/44100 for i in range(1,N+1)]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(); pg.goto('file://'+os.path.abspath(base))
    last=pg.evaluate("()=>[...document.querySelectorAll('.scene')].map(s=>Math.max(0,...[...s.querySelectorAll('.a')].map(e=>(+e.dataset.in||0)+(+(e.dataset.d||0.35)))))"); b.close()
assert len(last)==N,(len(last),N)
s=open(base).read(); parts=re.split(r'(<div class="scene")',s); o=parts[0]; durs=[]
for si,k in enumerate(range(1,len(parts),2)):
    body=parts[k]+parts[k+1]; v=vd[si]; L=last[si]; f=min(1.0,(v-0.15)/L) if L>0 else 1
    body=re.sub(r'data-in="([\d.]+)"',lambda m:f'data-in="{float(m.group(1))*f:.2f}"',body)
    body=re.sub(r'data-d="([\d.]+)"',lambda m:f'data-d="{max(0.2,float(m.group(1))*f):.2f}"',body)
    d=round((v+0.2+(0.9 if si==N-1 else 0))*30)/30; durs.append(d)
    body=re.sub(r'data-dur="[\d.]+"',f'data-dur="{d:.3f}"',body,count=1); o+=body
open(html,'w').write(o); json.dump(durs,open(f'{pf}durs.json','w'))
segs=[]
for i in range(1,N+1):
    sr,v=wf.read(f'{pf}a_{i:02d}.wav'); v=v.astype(np.float32)/32767
    seg=np.zeros((int(round(durs[i-1]*sr)),2),np.float32); s0=int(0.05*sr); seg[s0:s0+len(v)]=v[:len(seg)-s0]; segs.append(seg)
wf.write(f'{pf}voice.wav',44100,(np.concatenate(segs)*32767).astype(np.int16))
shutil.rmtree(f'{pf}scenes',ignore_errors=True)
R=lambda *a:subprocess.run(list(a),check=True)
R('python3','render_any.py',html,f'{pf}durs.json',f'{pf}scenes','full')
R('python3','sfx_mix.py',html,f'{pf}durs.json',f'{pf}voice.wav',f'{pf}_vs.wav')
R('bash','bgm_mix.sh',f'{pf}_vs.wav',bgm,f'{pf}_final.wav','-34','-1.5')
open(f'{pf}list.txt','w').write(''.join(f"file '{pf}scenes/s{i:02d}.mp4'\n" for i in range(N)))
R('ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',f'{pf}list.txt','-c','copy',f'{pf}joined.mp4')
R('ffmpeg','-y','-v','error','-i',f'{pf}joined.mp4','-i',f'{pf}_final.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out)
if thumb:
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920}); pg.goto('file://'+os.path.abspath(html))
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1000); pg.evaluate(f"render(0,{durs[0]-0.05})")
        pg.screenshot(path=thumb,type='jpeg',quality=95); b.close()
print('durs',[round(x,2) for x in durs],'total',round(sum(durs),1))
