"""Brute force: right angles among the black points of one full stride diagonal
(all slots i = r + nu t of diagonal T, label at column mu t, odd row 2i+1, even row 2i+2s+2)."""
import itertools
def pts(h, mu, nu, T, r=0):
    A=(h+1)//2; K=h//2; s=(T-1)//2
    lo=max(0,-s); hi=min(A,K-s); P=[]
    t=0
    while lo+r+nu*t < hi:
        i=lo+r+nu*t; P.append((mu*t, 2*i+1)); P.append((mu*t, 2*(i+s)+2)); t+=1
    return P
def right_angles(P):
    S=set(P); n=0; ex=None
    for v in P:
        for a,b in itertools.combinations(P,2):
            if v in (a,b): continue
            x1,y1=a[0]-v[0],a[1]-v[1]; x2,y2=b[0]-v[0],b[1]-v[1]
            if x1*x2+y1*y2==0 and x1*y1!=0 or (x1*x2+y1*y2==0 and x2*y2!=0):
                n+=1; ex=ex or (v,a,b)
    return n, ex
for (h,mu,nu,T) in [(60,4,1,7),(60,8,1,9),(60,4,3,11),(60,4,2,13),(60,4,4,5),(80,4,8,17),(80,4,8,51),(80,4,8,15),(60,12,1,-9)]:
    n,ex=right_angles(pts(h,mu,nu,T))
    print((h,mu,nu,T),"tilted right angles:",n,ex)
