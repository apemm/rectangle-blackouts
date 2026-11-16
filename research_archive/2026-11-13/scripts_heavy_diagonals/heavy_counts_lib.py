# Heavy-diagonal counts: for each odd T, k_T^(s) and greedy chi of G_T^(s) for strides s in menu.
# Reports #diagonals and #labels with min_s chi_greedy > B and with min_s k >= B, and Delta_S.
import sys, math
from collections import defaultdict
def triples(h):
    out=[]; u=2
    while u*u+1<h:
        for v in range(1,u):
            if (u-v)%2==1 and math.gcd(u,v)==1:
                a=u*u-v*v; b=2*u*v; c=u*u+v*v; g=1
                while g*c<h:
                    out.append((g*a,g*b)); out.append((g*b,g*a)); g+=1
        u+=1
    return out
def dsets(h,s,tr):
    A=(h+1)//2; K=h//2; D=defaultdict(set)
    for (x,y) in tr:
        if x%s or y%2==0: continue
        for sx in (1,-1):
            for sy in (1,-1):
                d=sx*x//s; Y=sy*y; T=Y-2*d
                if abs(T)>=h: continue
                sd=(T-1)//2; lo=max(0,-sd); hi=min(A,K-sd); n=hi-lo
                if n>=1 and abs(d)<n: D[T].add(abs(d))
    return D
def greedy(n,ds):
    if not ds: return 1
    col=[0]*n; best=0
    for i in range(n):
        used=set(col[i-d] for d in ds if d<=i)
        c=0
        while c in used: c+=1
        col[i]=c; best=max(best,c)
    return best+1
