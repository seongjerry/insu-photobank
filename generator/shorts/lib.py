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
