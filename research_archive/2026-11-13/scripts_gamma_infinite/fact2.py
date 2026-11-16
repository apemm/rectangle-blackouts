from fractions import Fraction as F
from c1_lib import mul, conj, norm, inv, pw, L, r_of, is_sq, odd_den
from pairs import gen_pi
eps=(F(-1),F(-1))
def cong(beta,m,l):
    for q in (beta[0]-1, beta[1]):
        d=q.denominator
        while d%l==0: d//=l
        if d!=1 or q.numerator%m: return False
    return True
def find(l1,l2,amax=2000):
    pi=tuple(map(F,gen_pi(l1))); om=mul(pi,inv(conj(pi)))
    for k in (1,-1):
        wk=pw(om,k); e=(F(1),F(0))
        for a in range(amax):
            b=mul(e,wk)
            for s in (1,-1):
                bb=(s*b[0],s*b[1])
                if cong(bb,10*l2,l1): return (s,a,k,bb)
            e=mul(e,eps)
l1,l2=29,59
s1,a1,k1,B1=find(l1,l2); s2,a2,k2,B2=find(l2,l1)
print("beta1=%d*eps^%d*omega29^%d  beta2=%d*eps^%d*omega59^%d"%(s1,a1,k1,s2,a2,k2))
r1,r2,r12=r_of(B1),r_of(B2),r_of(mul(B1,B2))
for r in (r1,r2,r12): assert odd_den(r) and is_sq(20*r*r+4*r+1)
c=r12-r1-r2
print("cross term is integer:", c.denominator==1, " log10|cross| ~", len(str(abs(c.numerator))))
print("den(r1)=",r1.denominator," den(r2)=",r2.denominator," den(r12)=",r12.denominator)
# l-adic principal parts: r12 - r1 should be 29-integral, r12 - r2 59-integral
print("r12-r1 den:", (r12-r1).denominator, " r12-r2 den:", (r12-r2).denominator)
import math
print("log10|r1|,|r2|,|r12| ~", [round(math.log10(abs(float(x))) if abs(float(x))<1e300 else 999,1) for x in (r1,r2,r12)])
