# BH16 S2 instances by formula: label slot i (odd row 2i+1 = r1 mod 16), e' = (rho - y)/8 odd,
# delta = +-(f2 - f1) for f1*f2 = e'^2, f1 < f2.  Count those with D inside the block slot range.
import sys
from math import isqrt
def divs(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0: out.append(d)
    return out
for h in (1000, 10000, 100000):
    A=(h+1)//2; r1=3; R=max(y for y in range(h-20,h+1) if y%16==r1); rho=R-8
    tot=0; inz=0; nl=0
    for i in range(1, A, 8):
        y=2*i+1; e=(rho-y)//8
        if e<=0 or (rho-y)%8: continue
        nl+=1; E=e*e
        for f1 in divs(E):
            f2=E//f1
            if f1>=f2: continue
            d=f2-f1
            for dd in (d,-d):
                tot+=1
                if 0<=i+dd<A: inz+=1
    print('h',h,'labels',nl,'S2 per label',round(tot/nl,2),'in-block share',round(inz/tot,3))
