# Build the stride-menu partition (greedy colouring of G_T^{(s)} for the best stride) and
# check every class from the definitions: rival pairs (Lemma rival, exact j-constraints) and right angles.
import sys, math
from stride_sets import triples, dsets
h=int(sys.argv[1]); strides=[2,4,8,12,20]
A=(h+1)//2; K=h//2; tr=triples(h)
Ds={s:dsets(h,s,tr) for s in strides}
def is_rival(P,Q):
    (x1,y1),(x2,y2)=P,Q
    if x1==x2 or (y1-y2)%2==0: return False
    c,cp=min(y1,y2),max(y1,y2); t2=(x1-x2)**2
    for j in range(1,h):
        if c-j<1 or cp+j>h: break
        if 4*j*(cp-c+j)==t2: return True
    return False
ncls=0; bad=0
for T in [t for t in range(-h+1,h) if t%2]:
    sd=(T-1)//2; lo=max(0,-sd); hi=min(A,K-sd)
    if hi<=lo: continue
    s=min(strides,key=lambda s:len(Ds[s].get(T,())))
    D=Ds[s].get(T,set()); col={}
    for i in range(lo,hi):
        used={col[i-d] for d in D if i-d in col}
        c=0
        while c in used: c+=1
        col[i]=c
    for c in set(col.values()):
        ncls+=1
        pts=[]
        for i in [i for i in col if col[i]==c]:
            pts.append((s*i,2*i+1)); pts.append((s*i,2*(i+sd)+2))
        for a in range(len(pts)):
            for b in range(a+1,len(pts)):
                if is_rival(pts[a],pts[b]): bad+=1
            V=pts[a]; vs=[(P[0]-V[0],P[1]-V[1]) for P in pts if P!=V]
            for u in vs:
                for w in vs:
                    if u[0]*w[0]+u[1]*w[1]==0: bad+=1
print("h",h,"classes",ncls,"violations",bad)
