# Check 2 (exact identity behind Proposition Q): for beta = eps^(15x) w19^(15y) (so beta = 1 mod 10 in O[1/19]),
# r = L(beta-1), gamma = phi beta = a + b phi, sigma = sign(k_19):
#   {(al + bt*s5) r}_19 + {(al' + bt' s5_11) r}_11  ==  al*r - sigma*bt*(b-1)/2   (mod 1, exactly, as rationals)
# with integers al, bt (the 11-part vanishes since r is 11-integral).
from fractions import Fraction as F
from adelic_copy import mul, pw, L, find_pi, hensel_phi, frac_l
K=200; eps=(F(-1),F(-1)); phi=(F(0),F(1))
p=find_pi(19); o=mul(p,p); o=(o[0]/19,o[1]/19)
s5={}
for l in (11,19):
    pp=find_pi(l); s5[l]=(2*hensel_phi(l,int(pp[0]),int(pp[1]),K)-1)%l**K
fails=0; cnt=0
for x in range(-4,5):
    for y in range(-4,5):
        if y==0: continue
        be=mul(pw(eps,15*x),pw(o,15*y)); r=L((be[0]-1,be[1])); b=mul(phi,be)[1]
        d=((b-1)/10).denominator
        while d%19==0: d//=19
        assert d==1, "b-1 not in 10 Z[1/19]"
        sig=1 if y>0 else -1
        for al in (0,1,3,-2):
            for bt in (1,2,7,-3):
                z=(al+bt*s5[19])%19**K
                lhs=frac_l(r,z,19,K)+frac_l(r,(5+4*s5[11])%11**K,11,K)
                rhs=al*r-sig*bt*(b-1)/2
                diff=lhs-rhs
                cnt+=1; fails+= (diff.denominator!=1)
print("cases",cnt,"failures",fails)
