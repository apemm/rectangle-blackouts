# min of F(s)=max(||fA(s)||,||fC(s)||) over s in R* outside the two strips; grid in u = log|s|, both signs
import numpy as np
S5=5**0.5; PHI=(1+S5)/2; PHIc=(1-S5)/2
def d1(x): f=x-np.floor(x); return np.minimum(f,1-f)
def F(s): return np.maximum(d1((2*PHIc/s-1)/S5), d1((2*PHI*s-1)/S5))
u=np.linspace(-12,12,4_000_001); a=np.exp(u)
for delta in [0.1,0.2,0.3,0.35,0.4,0.44]:
    best=1
    for sg in (1,-1):
        s=sg*a
        bad=((s>1-delta)&(s<1+delta)) | ((s< -PHI**-2*(1-delta))&(s> -PHI**-2*(1+delta)))
        v=F(s[~bad]); i=np.argmin(v); best=min(best,v[i])
        if v[i]==best: arg=s[~bad][i]
    print("delta",delta,"c(delta) ~ %.4f at s=%.4f"%(best,arg), "tail value ||1/sqrt5||=%.4f"%d1(1/S5))
