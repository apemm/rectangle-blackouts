# Sanity checks of stride-4u forms used via my notes (menu {3,5,7,13}).
from math import gcd
def v2(n):
    n=abs(n); c=0
    while n%2==0: n//=2; c+=1
    return c
for u in (1,3,5,7,13):
    D=4*u*u+1
    bad=0; mnq=10**9; mnp=10**9; mxp=0; gs=set(); n=0
    for be in range(1,161,2):
        for al in range(1,u*be,2):
            if gcd(al,be)!=1 or v2(u*be-al)<3: continue
            F=4*(al-2*u*be)**2+be*be
            g=gcd(F,u*be-al)
            if D%g: bad+=1
            q=al*F//g; p=(al*F+4*(u*be-al)*be*be)//g
            if (al*F)%g or (al*F+4*(u*be-al)*be*be)%g: bad+=1
            mnq=min(mnq,q/(al*be*be)); mnp=min(mnp,p*D/(4*u*be**3)); mxp=max(mxp,p/be**3)
            if (p-q)%32: bad+=1
            gs.add(g); n+=1
    # FF content gcd(U,V) | 8 u D
    badff=0
    for a in range(-400,401):
        for b in range(1,120):
            if gcd(a,b)!=1: continue
            U=(a-4*u*b)*(a*a+b*b); V=a**3-4*u*a*a*b-3*a*b*b+4*u*b**3
            if U==0: continue
            if (8*u*D)%gcd(U,V): badff+=1
    # Theorem F identity at r=4u: (P-8ut)(P^2+4t^2) = 8tY1(P-4ut) with Y1 = t(m-4u)(m^2+1)/(2(m-2u)), P=2tm
    from fractions import Fraction as Fr
    badF=0
    for t in (-64,-32,32):
        for m in (Fr(1,3),Fr(7,2),Fr(2*u+1,1),Fr(4*u-1,2)):
            if m==2*u: continue
            P=2*t*m; Y1=t*(m-4*u)*(m*m+1)/(2*(m-2*u))
            if (P-8*u*t)*(P*P+4*t*t)!=8*t*Y1*(P-4*u*t): badF+=1
    print(f"u={u} D={D} pairs={n} bad={bad} min q/(al be^2)={mnq:.3f} min p*D/(4u be^3)={mnp:.3f} max p/be^3={mxp:.2f} (bound {128*u**3/27+4*u:.1f}) g-set={sorted(gs)} FFbad={badff} Fbad={badF}")
