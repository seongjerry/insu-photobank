import sys, json, os, numpy as np, scipy.io.wavfile as wf
from playwright.sync_api import sync_playwright
html, durs_f, voice_f, out_f = sys.argv[1:5]
durs=json.load(open(durs_f)); SR=44100
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto("file://"+os.path.abspath(html)); pg.wait_for_timeout(500)
    ev=pg.evaluate("""()=>[...document.querySelectorAll('.scene')].map(s=>[...s.querySelectorAll('.a')].map(e=>({fx:e.dataset.fx,t:+(e.dataset.in||0),
      circ:e.classList.contains('circ'),rough:e.classList.contains('rough'),chk:!!e.closest('.chk')&&e.tagName==='path',d:+(e.dataset.d||0.35)})))""")
    b.close()
sfx={k:wf.read(f'/home/claude/sfx/{k}.wav')[1].astype(np.float32)/32767 for k in ['pen','marker','note','tick','circle','pop','whoosh']}
gain={'pen':0.1,'marker':0.12,'note':0.16,'tick':0.14,'circle':0.11,'pop':0.08,'whoosh':0.07}
sr,v=wf.read(voice_f); v=v.astype(np.float32)/32767
if v.ndim==1: v=np.stack([v,v],1)
mix=np.zeros((len(v),),np.float32); last={}
start=0.0
for si,(evs,d) in enumerate(zip(ev,durs)):
    hits=[]
    if si>0: hits.append(('whoosh',-0.05))
    got=set()
    for e in evs:
        fx=e['fx']; t=e['t']
        if fx=='mark' and 'marker' not in got: hits.append(('marker',t)); got.add('marker')
        elif fx=='drop' and 'note' not in got: hits.append(('note',t+0.18)); got.add('note')
        elif fx=='draw' and e['chk']: hits.append(('tick',t))
        elif fx=='draw' and e['circ'] and 'circle' not in got: hits.append(('circle',t)); got.add('circle')
    for k,t in hits:
        T=start+max(0,t)
        if T-last.get(k,-9)<0.18: continue
        last[k]=T; s=int(T*SR); x=sfx[k]*gain[k]; e_=min(len(mix),s+len(x))
        mix[s:e_]+=x[:e_-s]
    start+=d
out=v+mix[:,None]
out=out/max(1.0,np.max(np.abs(out))/0.98)
wf.write(out_f,SR,(out*32767).astype(np.int16))
print("events ok")
