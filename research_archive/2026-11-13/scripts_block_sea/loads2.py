import sys
from fam import *
from math import isqrt
def v2(n):
    k=0
    while n%2==0: n//=2; k+=1
    return k
def S_T(h,T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
h=int(sys.argv[1]); A=(h+1)//2; K=h//2
fams=['X1','X2','M2c']
tot={k:0 for k in fams}; same3=0; deg={}
for T in range(-(2*A-1),2*K,2):
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K]
    DT=S_T(h,T)
    od=lambda i:(4*i,2*i+1); ev=lambda i:(4*i,2*i+2+2*s)
    for i in I: deg[(T,i)]={k:0 for k in fams}
    for a in I:
        for b in I:
            if a>=b or (b-a) in DT: continue
            c={k:0 for k in fams}
            for (P,Q) in ((a,b),(b,a)):
                c['X1']+=X1(ev(P),od(Q),h)>0
                x2=X2(od(P),ev(Q),h)>0
                c['X2']+=x2
                if x2 and a>0 and b>0 and v2(a)%3==v2(b)%3: same3+=1
                c['M2c']+=(M2c(od(P),od(Q),h)>0)+(M2c(ev(P),ev(Q),h)>0)
            for k in c:
                if c[k]:
                    deg[(T,a)][k]+=1; deg[(T,b)][k]+=1; tot[k]+=1
nl=len(deg)
print('h',h,'avg degree',{k:round(2*v/nl,3) for k,v in tot.items()},'max',{k:max(d[k] for d in deg.values()) for k in fams},'X2 pairs with equal v2 mod 3:',same3)
