# Faster variant: min over menu of greedy chi, computing greedy only where needed.
import sys, math
from heavy_counts_lib import triples, dsets, greedy
h=int(sys.argv[1]); menu=[int(a) for a in sys.argv[2:]]
tr=triples(h); A=(h+1)//2; K=h//2
Ds={s:dsets(h,s,tr) for s in menu}
rows=[]
for T in range(-h+1,h,2):
    sd=(T-1)//2; lo=max(0,-sd); hi=min(A,K-sd); n=hi-lo
    if n<1: continue
    ks={s:len(Ds[s].get(T,())) for s in menu}
    order=sorted(menu,key=lambda s:ks[s]); s0=order[0]
    best=greedy(n,sorted(Ds[s0].get(T,())))
    if best>2:
        for s in order[1:]:
            best=min(best,greedy(n,sorted(Ds[s].get(T,()))))
    rows.append((T,n,ks[s0],best))
q=A*K
print("h",h,"menu",menu,"max min_k",max(r[2] for r in rows),"max min_chi",max(r[3] for r in rows))
for B in [1,2,3,4,5,6]:
    hk=[r for r in rows if r[2]>=B]; hc=[r for r in rows if r[3]>B]
    print(f"B={B} min_k>=B: diag {len(hk)} labels/q {sum(r[1] for r in hk)/q:.4f} | min_chi>B: diag {len(hc)} labels/q {sum(r[1] for r in hc)/q:.4f}")
print("sum min chi /h", sum(r[3] for r in rows)/h, " sum min k /h", sum(r[2] for r in rows)/h)
