# Rigorous (Lipschitz) lower bound for F(s) = max(||fA||,||fC||) off the strips, delta = 0.2.
# u = phi*s : fC = (2u-1)/sqrt5, fA = (-2/u-1)/sqrt5.  |u| >= 20 or |u| <= 1/20: F >= ||1/sqrt5|| - 2/(20 sqrt5) > 0.40.
# On t = log|u| in [-log20, log20]: d/dt of fA, fC bounded by 2*20/sqrt5 < 18; ||.|| is 1-Lipschitz.
import numpy as np
S5=5**0.5; PHI=(1+S5)/2; delta=0.2
def d1(x): f=x-np.floor(x); return np.minimum(f,1-f)
T=np.log(20.0); h=2e-6; best=1.0
t=np.arange(-T,T+h,h)
for sg in (1,-1):
    for c0 in range(0,len(t),2_000_000):
        u=sg*np.exp(t[c0:c0+2_000_000]); s=u/PHI
        bad=((s>1-delta)&(s<1+delta)) | ((s< -PHI**-2*(1-delta))&(s> -PHI**-2*(1+delta)))
        uu=u[~bad]
        if len(uu): best=min(best,float(np.min(np.maximum(d1((-2/uu-1)/S5),d1((2*uu-1)/S5)))))
err=18*h/2
print("grid min %.6f, Lipschitz error %.1e, certified c >= %.5f; outer bound %.4f"%(best,err,best-err,d1(1/S5)-2/(20*S5)))
# strip edges are excluded as open sets; the closed complement endpoints are on the grid up to h, covered by the same error term.
