import numpy as np
S5=5**0.5; PHI=(1+S5)/2; PHIc=(1-S5)/2
def d1(x): f=x-np.floor(x); return np.minimum(f,1-f)
u=np.linspace(-14,14,3_000_001); a=np.exp(u)
for m in range(1,9):
  for delta in [0.2,0.4]:
    best=1
    for sg in (1,-1):
        s=sg*a
        bad=((s>1-delta)&(s<1+delta)) | ((s< -PHI**-2*(1-delta))&(s> -PHI**-2*(1+delta)))
        ss=s[~bad]; v=np.maximum(d1(m*(2*PHIc/ss-1)/S5), d1(m*(2*PHI*ss-1)/S5))
        i=np.argmin(v)
        if v[i]<best: best=v[i]; arg=ss[i]
    print("m",m,"delta",delta,"c=%.4f at s=%.4f  ||m/sqrt5||=%.4f"%(best,arg,d1(m/S5)))
