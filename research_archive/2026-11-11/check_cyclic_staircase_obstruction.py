"""Check the cyclic staircase certificates without a solver."""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json

def board(h):
    return {(i,i) for i in range(1,h+1)} | {(i,i+1) for i in range(1,h)} | {(h,1)}

def is_rectangle(R):
    for a,b in combinations(R,2):
        q=list(set(R)-{a,b})
        if len(q)!=2: continue
        c,d=q
        if (a[0]+b[0],a[1]+b[1])==(c[0]+d[0],c[1]+d[1]):
            if sum((a[i]-b[i])**2 for i in (0,1))==sum((c[i]-d[i])**2 for i in (0,1)):
                return True
    return False

certificates=[]
for h in range(4,1025):
    S=board(h)
    s=(h+1)//2
    d=h//2
    a=s//2
    W,Z=(s,1),(h,d+1)
    R={W,Z,(h,1),(s,d+1)}
    T={W,Z,(s-a,1+a),(h-a,d+1+a)}
    assert len(R)==len(T)==4 and R!=T
    assert is_rectangle(R) and is_rectangle(T)
    assert all(1<=x<=h and 1<=y<=h for x,y in R|T)
    assert R-S==T-S=={W,Z}
    if h<=10:
        certificates.append({"h":h,"axis":sorted(R),"tilted":sorted(T),"shown":sorted(R-S)})
        for P,Q,C in combinations(S,3):
            for A,B,D in ((P,Q,C),(Q,P,C),(C,P,Q)):
                U=(B[0]-A[0],B[1]-A[1])
                V=(D[0]-A[0],D[1]-A[1])
                if U[0]*V[0]+U[1]*V[1]!=0: continue
                if 0 in U or 0 in V: continue
                E=(B[0]+D[0]-A[0],B[1]+D[1]-A[1])
                assert not (1<=E[0]<=h and 1<=E[1]<=h), (h,A,B,D,E)
out={"status":"PASS","symbolic_certificate_heights":[4,1024],
     "full_black_triple_checks":[4,10],"sample_certificates":certificates}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in out.items() if k!="sample_certificates"},indent=2))

