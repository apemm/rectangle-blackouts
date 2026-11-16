# sanity exploration: two-per-column sets on parallel lines of slope 1/2; look for corner-triple-free ones with k > h
import sys
def violations(pts, k, h, first_only=True):
    S=set(pts)
    P=sorted(S)
    bycol={}
    out=[]
    for X in P:
        for Y in P:
            if Y==X: continue
            ux=Y[0]-X[0]; uy=Y[1]-X[1]
            if ux==0 or uy==0: continue
            for Z in P:
                if Z<=Y or Z==X: continue
                vx=Z[0]-X[0]; vy=Z[1]-X[1]
                if ux*vx+uy*vy!=0: continue
                F=(Y[0]+Z[0]-X[0],Y[1]+Z[1]-X[1])
                if 1<=F[0]<=k and 1<=F[1]<=h:
                    out.append((X,Y,Z,F))
                    if first_only: return out
    return out
best=None
for c in range(1,40):
    for k in range(4,80):
        pts=[]
        for x in range(1,k+1):
            pts.append((x,(x+1)//2)); pts.append((x,(x+2)//2+c))
        h=max(p[1] for p in pts)
        v=violations(pts,k,h)
        if v:
            # first failing k for this c
            print('c',c,'max ok k',k-1,'h at that k',((k-1)+2)//2+c,'first violation at k',k,v[0])
            break
    else:
        print('c',c,'ok up to k=79, h=',(79+2)//2+c)
