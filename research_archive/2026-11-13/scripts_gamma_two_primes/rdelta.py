# Residual after the algebraic characters: R(delta) = slab elements with |s - s*| < delta*|s*| and ||{b}_{l1}|| < delta.
# Counts per level, split into (both k_i != 0) and (one k_i = 0). S = {11, 19}. Sanity check of the delta^2 * (linear) heuristic.
import sys, math
from fractions import Fraction as F
import mpmath as mp
from adelic_copy import mul, pw, L, s1, find_pi, PHI
mp.mp.dps=40
l1,l2,J=11,19,int(sys.argv[1])
def omega(l):
    p=find_pi(l); o=mul(p,p); return (o[0]/l,o[1]/l)
o1,o2=omega(l1),omega(l2); eps=(F(-1),F(-1)); phi=(F(0),F(1))
a1=math.log(abs(float(s1(o1)))); a2=math.log(abs(float(s1(o2)))); g=2*math.log((1+5**0.5)/2)
def fracl(q,l):
    num,den=q.numerator,q.denominator; e=0
    while den%l==0: den//=l; e+=1
    if e==0: return F(0)
    m=l**e; return F(num*pow(den,-1,m)%m,m)
dels=[0.2,0.1,0.05]; cnt={d:{} for d in dels}; tot={}
P1=[pw(o1,k) for k in range(-J,J+1)]; P2=[pw(o2,k) for k in range(-J,J+1)]
for k1 in range(-J,J+1):
    for k2 in range(-J,J+1):
        if k1==0 and k2==0: continue
        base=mul(P1[k1+J],P2[k2+J]); x=-(k1*a1+k2*a2)/g
        for n in range(math.floor(x)-1,math.floor(x)+3):
            for sg in (1,-1):
                be=mul(pw(eps,n),base); be=(sg*be[0],sg*be[1]); s=float(s1(be))
                for st in (1.0,-float(PHI)**-2):
                    dev=abs(s/st-1)
                    if s/st>0 and dev<0.2:
                        b=mul(phi,be)[1]; f1=float(fracl(b,l1)); nb=min(f1,1-f1)
                        lev=max(abs(k1),abs(k2)); both=(k1!=0 and k2!=0)
                        tot[lev]=tot.get(lev,0)+1
                        for d in dels:
                            if dev<d and nb<d:
                                cnt[d].setdefault(lev,[0,0]); cnt[d][lev][0 if both else 1]+=1
for d in dels:
    print("delta",d,"[both, single] per level:",{j:cnt[d].get(j,[0,0]) for j in range(1,J+1)})
print("slab per level:",[tot.get(j,0) for j in range(1,J+1)])
for d in dels:
    B=sum(cnt[d].get(j,[0,0])[0] for j in range(1,J+1)); T=sum(tot.values())
    print("delta",d,"both-nonzero residual total",B,"slab total",T,"ratio",B/T,"vs (delta/0.2)*2*delta",(d/0.2)*2*d)
