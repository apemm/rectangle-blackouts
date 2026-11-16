# checks the (kappa,mu,m') reduction on every witness of E(Q) (no congruences)
import sys
from math import gcd, isqrt
from eq_enum import spf_sieve, EQ
def fac(n,spf):
    d={}
    while n>1:
        p=spf[n]; d[p]=d.get(p,0)+1; n//=p
    return d
Qs=list(range(3001,3061))+[1000,1002,2002,4001,8191,9973,10080,20011,30030]
spf=spf_sieve(2*max(Qs)+5)
nw=0; bad=0; ratio=0
for Q in Qs:
    for (e,n1,X,Y) in EQ(Q,spf):
        nw+=1
        L=X+Y+2*n1; W=X-Y; m=Q-2*e
        ok = n1*L==e*m and W*W==L*L-4*e*(Q-e)
        g=gcd(e,n1); kap=e//g; mu=n1//g
        ok = ok and m%mu==0
        mp=m//mu
        ok = ok and (kap*kap+mu*mu)*mp*mp==Q*Q+W*W
        ok = ok and 4*n1*n1<=e*Q
        # kappa | G b^2 ; local lemma
        fe=fac(e,spf); fq=fac(2*Q,spf); fn=fac(n1,spf) if n1>1 else {}
        Gb2=1
        for p,a in fe.items():
            if p in fq: Gb2*=p**a
            else:
                Gb2*=p**(2*(a//2))
                if a%2==1: ok = ok and fn.get(p,0)>=(a+1)//2
        ok = ok and Gb2%kap==0
        if not ok: bad+=1; print('FAIL',Q,e,n1,X,Y)
        ratio=max(ratio, mu/(kap*(Q/e)**.5))
print('witnesses',nw,'failures',bad,'max mu/(kap sqrt(Q/e))',round(ratio,3))
