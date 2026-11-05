import numpy as np, scipy.signal as sg, scipy.io.wavfile as wf
SR=44100
def midi(n): return 440*2**((n-69)/12)
def env_adsr(n,a,d,s,r):
    e=np.full(n,s,float); A=int(a*SR); D=int(d*SR); R=int(r*SR)
    e[:A]=np.linspace(0,1,A); e[A:A+D]=np.linspace(1,s,D)
    e[-R:]*=np.linspace(1,0,R); return e
def epiano(f,dur,vel=0.5):
    n=int(dur*SR); t=np.arange(n)/SR
    x=(np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*3)+0.12*np.sin(2*np.pi*3.01*f*t)*np.exp(-t*6))
    x*=np.exp(-t*1.6)*(1+0.08*np.sin(2*np.pi*4.5*t)); x*=env_adsr(n,0.005,0.05,1,0.08)
    return x*vel
def pianoish(f,dur,vel=0.5):
    n=int(dur*SR); t=np.arange(n)/SR
    x=sum(a*np.sin(2*np.pi*f*h*(1+0.0004*h*h)*t)*np.exp(-t*(1.2+h*0.8)) for h,a in [(1,1),(2,.5),(3,.25),(4,.12),(5,.06)])
    return x*env_adsr(n,0.003,0.02,1,0.1)*vel
def pad(f,dur,vel=0.2):
    n=int(dur*SR); t=np.arange(n)/SR
    x=sum(np.sin(2*np.pi*f*(1+d)*t+np.sin(2*np.pi*0.3*t)) for d in (-0.003,0,0.004))/3
    return x*env_adsr(n,0.8,0.3,0.8,0.9)*vel
def pluck(f,dur,vel=0.4):
    n=int(dur*SR); N=int(SR/f); buf=np.random.default_rng(int(f)).uniform(-1,1,N); out=np.zeros(n)
    for i in range(n):
        out[i]=buf[i%N]; buf[i%N]=0.497*(buf[i%N]+buf[(i+1)%N])
    return out*vel*env_adsr(n,0.002,0.01,1,0.05)
def kick(vel=0.8):
    n=int(0.35*SR); t=np.arange(n)/SR
    return np.sin(2*np.pi*(45+90*np.exp(-t*30))*t)*np.exp(-t*9)*vel
def hat(vel=0.1,rng=np.random.default_rng(5)):
    n=int(0.05*SR); t=np.arange(n)/SR
    b,a=sg.butter(2,7000/(SR/2),'high'); return sg.lfilter(b,a,rng.normal(size=n))*np.exp(-t*80)*vel
def snare(vel=0.25,rng=np.random.default_rng(9)):
    n=int(0.2*SR); t=np.arange(n)/SR
    b,a=sg.butter(2,[1500/(SR/2),6000/(SR/2)],'band')
    return (sg.lfilter(b,a,rng.normal(size=n))*np.exp(-t*25)+0.4*np.sin(2*np.pi*190*t)*np.exp(-t*30))*vel
def add(buf,x,t):
    s=int(t*SR); e=min(len(buf),s+len(x)); buf[s:e]+=x[:e-s]
def reverb(x,size=1.6,mix=0.25):
    n=int(size*SR); t=np.arange(n)/SR; ir=np.random.default_rng(1).normal(size=n)*np.exp(-t*4.5); ir/=np.sum(np.abs(ir))/8
    wet=sg.fftconvolve(x,ir)[:len(x)]; return x*(1-mix)+wet*mix
def lp(x,f): b,a=sg.butter(2,f/(SR/2)); return sg.lfilter(b,a,x)
def master(x,name,peak=0.7):
    x=x/np.max(np.abs(x))*peak
    fade=int(1.5*SR); x[:int(0.05*SR)]*=np.linspace(0,1,int(0.05*SR)); x[-fade:]*=np.linspace(1,0,fade)
    st=np.stack([x,np.roll(x,int(0.012*SR))*0.96],1)
    wf.write(name,SR,(st*32767).astype(np.int16))

# Track 1: 잔잔한 로파이 (82bpm, Cmaj7-Am7-Fmaj7-G6)
def track1(L=64):
    bpm=82; beat=60/bpm; bar=4*beat; buf=np.zeros(int((L+2)*SR)); drums=np.zeros_like(buf)
    prog=[[48,55,59,64,67],[45,52,55,60,64],[41,48,52,57,60],[43,50,55,59,64]]
    roots=[36,33,29,31]; nb=int(L/bar)
    for b in range(nb):
        t0=b*bar; ch=prog[b%4]
        for i,n in enumerate(ch[1:]): add(buf,epiano(midi(n),bar*0.98,0.22),t0+i*0.012)
        add(buf,epiano(midi(ch[-1]+12 if b%2 else ch[-2]+12),beat*1.5,0.12),t0+beat*2.5)
        add(buf,np.sin(2*np.pi*midi(roots[b%4])*np.arange(int(bar*SR))/SR)*np.exp(-np.arange(int(bar*SR))/SR*1.2)*0.35,t0)
        if b>=2:
            for k in range(4):
                if k in (0,2): add(drums,kick(0.5),t0+k*beat+(0.02 if k==2 else 0))
                if k in (1,3): add(drums,snare(0.12),t0+k*beat)
            for k in range(8): add(drums,hat(0.05 if k%2 else 0.08),t0+k*beat/2+(0.03 if k%2 else 0))
    x=lp(reverb(buf,1.8,0.3),5000)+lp(drums,6000)
    x+=lp(np.random.default_rng(2).normal(size=len(x)),3000)*0.0007  # 바이닐 노이즈
    return x[:int(L*SR)]
master(track1(),'bgm_01_lofi_calm.wav')

# Track 2: 밝은 플럭 (100bpm, F-C-G-Am 아르페지오)
def track2(L=64):
    bpm=100; beat=60/bpm; bar=4*beat; buf=np.zeros(int((L+2)*SR)); drums=np.zeros_like(buf)
    prog=[[53,57,60,65],[48,52,55,60],[43,50,55,59],[45,52,57,60]]; roots=[29,36,31,33]
    pat=[0,2,1,3,2,1,3,2]
    for b in range(int(L/bar)):
        t0=b*bar; ch=prog[b%4]
        for k,p in enumerate(pat): add(buf,pluck(midi(ch[p]+12),beat*0.9,0.28),t0+k*beat/2)
        for n in ch[:3]: add(buf,pad(midi(n),bar,0.06),t0)
        for k in (0,1.5,2,3.5): add(buf,np.sin(2*np.pi*midi(roots[b%4])*np.arange(int(beat*0.9*SR))/SR)*np.exp(-np.arange(int(beat*0.9*SR))/SR*4)*0.3,t0+k*beat)
        if b>=1:
            for k in range(4):
                add(drums,kick(0.35 if k%2==0 else 0.0),t0+k*beat)
                if k%2: add(drums,snare(0.08),t0+k*beat)
            for k in range(8): add(drums,hat(0.025),t0+k*beat/2)
    x=lp(reverb(buf,1.2,0.22),5000)+lp(drums,8000)
    return x[:int(L*SR)]
master(track2(),'bgm_02_bright_pluck.wav')

# Track 3: 따뜻한 피아노 (70bpm, Am-F-C-G, 드럼 없음)
def track3(L=64):
    bpm=70; beat=60/bpm; bar=4*beat; buf=np.zeros(int((L+2)*SR))
    prog=[[45,52,57,60,64],[41,48,53,57,60],[48,52,55,60,64],[43,50,55,59,62]]
    mel=[[76,74,72,74],[72,72,69,72],[72,74,76,79],[74,72,71,74]]
    for b in range(int(L/bar)):
        t0=b*bar; ch=prog[b%4]
        add(buf,pianoish(midi(ch[0]-12),bar,0.3),t0)
        for i,n in enumerate(ch[1:]): add(buf,pianoish(midi(n),bar*0.95,0.16),t0+beat*(i*0.5)+beat*0.05)
        for n in ch[1:4]: add(buf,pad(midi(n),bar,0.05),t0)
        if b>=2:
            for k,n in enumerate(mel[b%4]): add(buf,pianoish(midi(n),beat*1.2,0.16 if k!=0 else 0.2),t0+k*beat)
    return lp(reverb(buf,2.4,0.35),6000)[:int(L*SR)]
master(track3(),'bgm_03_warm_piano.wav')
print('ok')
