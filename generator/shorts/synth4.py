from lib import *
# Track 4: 경쾌한 업템포 (124bpm, C-G-Am-F, 16분 플럭 + 4온더플로어) 빠른 편집 정보성 영상용
def track4(L=64):
    bpm=124; beat=60/bpm; bar=4*beat; buf=np.zeros(int((L+2)*SR)); drums=np.zeros_like(buf); bass=np.zeros_like(buf)
    prog=[[48,52,55,60],[43,47,50,55],[45,48,52,57],[41,45,48,53]]; roots=[36,31,33,29]
    pat=[0,1,2,3,2,1,2,3]
    for b in range(int(L/bar)):
        t0=b*bar; ch=prog[b%4]
        for k in range(16):
            p=pat[k%8]; add(buf,pluck(midi(ch[p]+12+(12 if k%8==3 else 0)),beat*0.22,0.22 if k%4==0 else 0.15),t0+k*beat/4)
        for n in ch[1:]: add(buf,pad(midi(n),bar,0.04),t0)
        for k in range(4):
            n=int(beat*0.45*SR); tt=np.arange(n)/SR
            add(bass,np.tanh(2*np.sin(2*np.pi*midi(roots[b%4])*tt))*np.exp(-tt*6)*0.28,t0+k*beat+beat/2)
        if b>=1:
            for k in range(4):
                add(drums,kick(0.42),t0+k*beat)
                add(drums,hat(0.05),t0+k*beat+beat/2)
                if k%2: add(drums,snare(0.11),t0+k*beat)
            for k in range(16):
                if k%2: add(drums,hat(0.018),t0+k*beat/4)
    x=lp(reverb(buf,1.0,0.18),6500)+lp(bass,900)+lp(drums,9000)
    return x[:int(L*SR)]
master(track4(),'bgm_04_upbeat_pluck.wav')
print('ok')
