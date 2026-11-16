import sys
from fam import *
h=int(sys.argv[1]); A=(h+1)//2; K=h//2
for T in map(int,sys.argv[2].split(',')):
    s=(T-1)//2; I=[i for i in range(A) if 0<=i+s<K]
    od=lambda i:(4*i,2*i+1); ev=lambda i:(4*i,2*i+2+2*s)
    res={'X1':[],'X2':[],'M2c':[],'M1C':[]}
    for a in I:
        for b in I:
            if a>=b: continue
            for (P,Q) in ((a,b),(b,a)):
                if X1(ev(P),od(Q),h): res['X1'].append((a,b))
                if X2(od(P),ev(Q),h): res['X2'].append((a,b))
                if M2c(od(P),od(Q),h) or M2c(ev(P),ev(Q),h): res['M2c'].append((a,b))
                for Dd in (od(a),od(b)):
                    if M1C(ev(P),ev(Q),Dd,h): res['M1C'].append((a,b))
    print(T,{k:sorted(set(v)) for k,v in res.items()})
