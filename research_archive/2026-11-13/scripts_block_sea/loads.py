import sys
from fam import *
from math import isqrt
def S_T(h,T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if isqrt(L2)**2==L2 and isqrt(L2)<h: out.add(abs(d))
    return out
h=int(sys.argv[1]); A=(h+1)//2; K=h//2
tot={'X1':0,'X2':0,'M2c':0,'M1C':0}; mx=dict(tot); nl=0; deg={}
for T in range(-(2*A-1),2*K,2):
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K]
    DT=S_T(h,T)
    od=lambda i:(4*i,2*i+1); ev=lambda i:(4*i,2*i+2+2*s)
    for i in I: deg[(T,i)]={k:0 for k in tot}
    for a in I:
        for b in I:
            if a>=b or (b-a) in DT: continue
            c={'X1':0,'X2':0,'M2c':0,'M1C':0}
            for (P,Q) in ((a,b),(b,a)):
                c['X1']+=X1(ev(P),od(Q),h)>0
                c['X2']+=X2(od(P),ev(Q),h)>0
                c['M2c']+=(M2c(od(P),od(Q),h)>0)+(M2c(ev(P),ev(Q),h)>0)
                for Dd in (od(a),od(b)):
                    c['M1C']+=M1C(ev(P),ev(Q),Dd,h)>0
            for k in c:
                if c[k]:
                    deg[(T,a)][k]+=1; deg[(T,b)][k]+=1; tot[k]+=1
nl=len(deg)
print('h',h,'labels',nl,'pairs per label (2*edges/labels):',{k:round(2*v/nl,3) for k,v in tot.items()},
      'max degree:',{k:max(d[k] for d in deg.values()) for k in tot})
