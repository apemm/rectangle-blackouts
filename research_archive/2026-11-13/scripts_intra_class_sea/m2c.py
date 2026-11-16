# intra-class M2c via the note's predicate; check (alpha,beta) parametrization and 2-adic families
import sys
from math import gcd
from collections import Counter
def v2(n):
    n=abs(n); c=0
    while n%2==0: n//=2; c+=1
    return c
def divisors(n):
    n=abs(n); out=[]
    d=1
    while d*d<=n:
        if n%d==0: out+= [d, n//d]
        d+=1
    return set(out)
h=int(sys.argv[1])
A=(h+1)//2; K=h//2
fam=Counter(); bad=0; tot=0; maxdeg=Counter(); ok_param=0
for T in range(-(h-1),h,2):
    s=(T-1)//2
    L=[i for i in range(A) if 0<=i+s<K]
    pts=[]
    for i in L:
        pts.append((i,2*i+1)); pts.append((i,2*(i+s)+2))
    for (iB,yB) in pts:
        u2=yB-1
        if u2==0: continue
        for (iD,yD) in pts:
            t=iD-iB
            if t<=0 or (yD-yB)!=2*t: continue
            if yB+t>h: continue
            e=t; D=4*t
            for d in divisors(e*u2):
                for n1 in (d,-d):
                    if n1*((D-n1)**2+e*e)!=e*u2*(D-2*n1): continue
                    if (e*u2)%n1: continue
                    z=-e*u2//n1
                    if z%4==0 or (2*n1-z)%4==0: continue
                    tot+=1; maxdeg[(T,iB)]+=1
                    g=gcd(n1,t); a=n1//g; b=t//g
                    if b<0: a,b=-a,-b
                    F=(a-4*b)**2+b*b
                    if (10*u2)%F==0 and (u2 % abs(a))==0: ok_param+=1
                    key=('a%2' if a%2 else 'a2' if v2(a)==1 else 'a4+', 'b%2' if b%2 else 'b'+str(min(v2(b),3)))
                    fam[(key, v2(t))]+=1
print('total M2c intra (directed B->D):',tot,'param ok:',ok_param)
for k,v in sorted(fam.items()): print(k,v)
print('max B forward degree',max(maxdeg.values()) if maxdeg else 0)
