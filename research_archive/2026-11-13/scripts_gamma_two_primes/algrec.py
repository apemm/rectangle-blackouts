# Check 2: algebraic characters are recurrent on the slab, via elements with k_11 = 0.
# beta in <eps^(2a), w19^(2b)>, beta = 1 mod 10M, sigma1(beta) -> 1. Then every character
# x -> theta x + {(al+be*s5_l) x}_l (l=11,19) + {g x}_5, al,be rational l-integral, should be small.
from fractions import Fraction as F
import mpmath as mp
from adelic_copy import mul, pw, L, s1, find_pi, hensel_phi, frac_l, dist1, S5
mp.mp.dps=3000
M=1; mod=10*M
def red(x):  # reduce a+b phi with denominators prime to mod
    a,b=x; return (a.numerator*pow(a.denominator,-1,mod)%mod, b.numerator*pow(b.denominator,-1,mod)%mod)
def order(x):
    one=(1,0); y=red(x); k=1; cur=y
    while cur!=one:
        cur=red(mul((F(cur[0]),F(cur[1])),x)); k+=1
    return k
eps=(F(-1),F(-1)); p=find_pi(19); o=mul(p,p); o=(o[0]/19,o[1]/19)
a=order(eps); b=order(o); print("orders",a,b)
E1=pw(eps,2*a); E2=pw(o,2*b)
l1,l2=mp.log(abs(s1(E1))),mp.log(abs(s1(E2)))
K=4900; data={}
for l in (11,19):
    pp=find_pi(l); data[l]=(2*hensel_phi(l,int(pp[0]),int(pp[1]),K)-1)%l**K
best=[]
for y in range(-160,161):
    if y==0: continue
    x=int(mp.nint(-y*l2/l1))
    for xx in (x-1,x,x+1):
        t=xx*l1+y*l2
        best.append((abs(t),xx,y))
best.sort()
for t,x,y in best[:6]:
    be=mul(pw(E1,x),pw(E2,y)); r=L((be[0]-1,be[1]))
    rr=mp.mpf(r.numerator)/r.denominator
    vals=[]
    for (l,al,bt) in ((19,F(0),1),(19,F(3),7),(19,F(1,3),2),(11,F(2),5)):
        s5=data[l]; z=(al.numerator*pow(al.denominator,-1,l**K)+bt*s5)%l**K
        q=frac_l(r,z,l,K); vals.append(float(dist1(mp.mpf(q.numerator)/q.denominator)))
    print("logs1=%.2e r=%.2e k19=%d"%(float(t),float(rr),2*b*y), "char dists",["%.1e"%v for v in vals], "rho", "%.1e"%float(dist1(2*S5*rr)))
