# Count layout-free cross-block M2c shapes: (u2,e,z) with z | e*u2, n1=-e*u2/z,
# X^2 = z^2 - 4e(u2+e), w=(-(z+2n1)+-X)/2, Delta=-z-w, |Delta|>=78h,
# shallowness z!=0 mod 4, 2n1-z != 0 mod 4, u2+2e <= h (rows), then re-check the
# block_sea M2c equation n1((Delta-n1)^2+e^2) = e*u2*(Delta-2n1) directly.
import sys, math
import numpy as np
from math import gcd
THR=int(sys.argv[1])
def count(h):
    tot=0; bad=0
    for e in range(1,h):
        cmax = (e*(h-1))//(int(0.8*THR)*h)+2
        for c in range(1,cmax+1):
            st = c//gcd(c,e)
            u2 = np.arange(st, h-2*e+1, st, dtype=np.int64)
            if u2.size==0: continue
            for sgn in (1,-1):
                n1 = -sgn*c
                z = (e*u2)//(-n1)  # z = -e u2/n1
                D = z*z - 4*e*(u2+e)
                ok = D>=0
                X = np.zeros_like(D); X[ok]=np.round(np.sqrt(D[ok].astype(np.float64))).astype(np.int64)
                ok &= (X*X==D)
                for s2 in (1,-1):
                    num = -(z+2*n1)+s2*X
                    ok2 = ok & (num%2==0)
                    w = num//2
                    Dl = -z-w
                    ok2 &= (np.abs(Dl)>=THR*h) & (z%4!=0) & ((2*n1-z)%4!=0)
                    idx=np.nonzero(ok2)[0]
                    for i in idx:
                        U=int(u2[i]); Dd=int(Dl[i])
                        if n1*((Dd-n1)**2+e*e)!=e*U*(Dd-2*n1): bad+=1
                        else: tot+=1
    return tot,bad
for h in map(int,sys.argv[2:]):
    print(h, count(h)); sys.stdout.flush()
