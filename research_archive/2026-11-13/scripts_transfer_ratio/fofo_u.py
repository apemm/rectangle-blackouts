# In-class Fo/Fo at stride 4u: definition-level search (Lemma mixedeq) vs Theorem F / F2 predictions
import sys
from math import gcd
from fractions import Fraction as Fr
def divisors(n):
    n=abs(n); ds=[]; i=1
    while i*i<=n:
        if n%i==0:
            ds.append(i)
            if i*i!=n: ds.append(n//i)
        i+=1
    return ds
def v2(x):
    x=abs(x); c=0
    while x and x%2==0: x//=2; c+=1
    return c
def run(u,H,iota,mod,Y):
    labs=[i for i in range(iota,H//2,mod) if 2*i+1<Y]
    labslots=set(u*i for i in labs)          # slot of label = u*i (class offset 0)
    def filler_col(x):                        # deep column, slot = 0 mod 4 relative to labels, not a label slot
        if x%4: return False
        n=x//4
        return n%4==(u*iota)%4 and n not in labslots
    hits=[]
    for i1 in labs:
        L1=(4*u*i1,2*i1+1); Y1=Y-L1[1]
        for i2 in labs:
            if i2==i1: continue
            L2=(4*u*i2,2*i2+1); t=i2-i1
            for d in divisors(t*Y1):
                for X in (d,-d):
                    if (t*Y1)%X: continue
                    F1=(L1[0]+X,Y)
                    if not filler_col(F1[0]): continue
                    n=(-t*Y1//X,t)
                    C=(L1[0]+F1[0]+2*n[0]-L2[0], L1[1]+F1[1]+2*n[1]-L2[1])
                    assert C[1]==Y
                    if not filler_col(C[0]): continue
                    DC=(L2[0]-C[0],L2[1]-C[1]); BA=(X,Y1)
                    if DC[0]**2+DC[1]**2!=X*X+Y1*Y1: continue
                    if DC in (BA,(-X,-Y1)): continue
                    p=(L1[0]+n[0],L1[1]+n[1]); q=(F1[0]+n[0],F1[1]+n[1])
                    if not(1<=p[1]<=H and 1<=q[1]<=H): continue
                    P=X-(C[0]-L2[0])      # alpha1 - alpha2
                    m=Fr(P,2*t); a,b=m.numerator,m.denominator
                    U=(a-4*u*b)*(a*a+b*b); V=a**3-4*u*a*a*b-3*a*b*b+4*u*b**3
                    Y2=Y-L2[1]
                    ok = Fr(Y2,Y1)==Fr(V,U)
                    hits.append((Y1,Y2,t,a,b,ok,a%2==1 and b%2==0, 2*u<m<4*u, v2(X//4)-v2(b)))
    return hits
for (u,H,iota,Y) in []:
    # choose Y with Y - (2 iota+1) = 8 mod 64 (hole row, c=1)
    while (Y-(2*iota+1))%64!=8: Y-=1
    hs=run(u,H,iota,32,Y)
    print("u",u,"H",H,"Y",Y,"hits",len(hs),"all ratio ok",all(h[5] for h in hs),"all a odd b even",all(h[6] for h in hs),"all 2u<m<4u",all(h[7] for h in hs),"v2(A)-beta set",sorted(set(h[8] for h in hs)))
    print("  sample",hs[:4])
