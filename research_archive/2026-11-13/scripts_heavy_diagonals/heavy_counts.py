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
h=int(sys.argv[1]); menu=[int(a) for a in sys.argv[2:]]
tr=triples(h); A=(h+1)//2; K=h//2
Ds={s:dsets(h,s,tr) for s in menu}
rows=[]
for T in range(-h+1,h,2):
    sd=(T-1)//2; lo=max(0,-sd); hi=min(A,K-sd); n=hi-lo
    if n<1: continue
    ks=[len(Ds[s].get(T,())) for s in menu]
    cs=[greedy(n,sorted(Ds[s].get(T,()))) for s in menu]
    rows.append((T,n,min(ks),min(cs),ks[menu.index(4)] if 4 in menu else None, cs[menu.index(4)] if 4 in menu else None))
q=A*K
print("h",h,"menu",menu,"diagonals",len(rows),"labels",sum(r[1] for r in rows),"q_h",q)
print("max min_k",max(r[2] for r in rows),"max min_chi",max(r[3] for r in rows))
for B in [1,2,3,4,5,6,8,10,15,20]:
    hk=[r for r in rows if r[2]>=B]; hc=[r for r in rows if r[3]>B]
    print(f"B={B:3d} min_k>=B: diag {len(hk):6d} labels/q {sum(r[1] for r in hk)/q:.4f} | min_chi>B: diag {len(hc):6d} labels/q {sum(r[1] for r in hc)/q:.4f}")
print("sum min chi /h", sum(r[3] for r in rows)/h, " sum min k /h", sum(r[2] for r in rows)/h)
if 4 in menu:
    print("stride4 only: sum chi/h",sum(r[5] for r in rows)/h,"max chi",max(r[5] for r in rows))
    for B in [1,2,3,4,6,8]:
        hc=[r for r in rows if r[5]>B]
        print(f"  stride4 chi>B={B}: diag {len(hc)} labels/q {sum(r[1] for r in hc)/q:.4f}")
