# Check 1: b-reduction. For beta = +-eps^n w1^k1 w2^k2 (S={11,19}), gamma = phi*beta = a + b phi,
# r = L(beta-1). Claim: {zeta r}_l = {-sig_l * zeta * s5_l * b / 10}_l for every zeta in Z_l (sig_l = sign k_l).
import random
from fractions import Fraction as F
from adelic_copy import mul, pw, L, find_pi, hensel_phi, frac_l
Ls=[11,19]; K=16; data=[]
for l in Ls:
    p=find_pi(l); o=mul(p,p); o=(o[0]/l,o[1]/l)
    s5=(2*hensel_phi(l,int(p[0]),int(p[1]),K)-1)%l**K
    data.append((l,o,s5))
eps=(F(-1),F(-1)); phi=(F(0),F(1)); random.seed(2); bad=0; cnt=0
for _ in range(600):
    n=random.randint(-20,20); ks=[random.randint(-6,6) for _ in Ls]; sg=random.choice((1,-1))
    be=pw(eps,n)
    for (l,o,s5),k in zip(data,ks): be=mul(be,pw(o,k))
    be=(sg*be[0],sg*be[1]); r=L((be[0]-1,be[1]))
    if r==0: continue
    g=mul(phi,be); b=g[1]
    for (l,o,s5),k in zip(data,ks):
        if k==0: continue
        sig=1 if k>0 else -1
        for _ in range(3):
            z=random.randrange(l**K)
            lhs=frac_l(r,z,l,K)
            # -sig*z*s5/10 * b : multiplier in Z_l mod l^K
            mlt=(-sig*z*s5*pow(10,-1,l**K))%l**K
            rhs=frac_l(b,mlt,l,K)
            cnt+=1; bad+= (lhs!=rhs)
        # valuation check of b
        den=b.denominator; e=0
        while den%l==0: den//=l; e+=1
        bad += (e!=abs(k))
print("checks",cnt,"failures",bad)
