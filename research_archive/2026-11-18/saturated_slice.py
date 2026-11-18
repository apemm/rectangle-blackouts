"""Check necessary local conditions for a saturated blackout inside the full grid."""
import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from math import isqrt
from pathlib import Path
import sys
import time
from pysat.solvers import Solver

def clauses_for(h,k,run_width=None):
    width=h*h//4 if run_width is None else run_width
    left=(width-k)//2
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'2026-11-15/scripts_window_sat'))
    import win
    vp,cl,P0,S0,nrect=win.build(h,k)
    P=lambda p:P0(p[0]-left+1,p[1]+1)
    S=lambda r:S0(r+1)
    pts=list(itertools.product(range(left,left+k),range(h)))
    inside=lambda pt:0<=pt[0]<width and 0<=pt[1]<h
    dots=0
    pairs=defaultdict(list)
    rivals=0
    for i,a in enumerate(pts):
        for b in pts[i+1:]:
            u,v=b[0]-a[0],b[1]-a[1]
            N=u*u+v*v
            pairs[N].append((a,b,u,v))
            if u==0 or (a[0]+b[0])%2: continue
            L=isqrt(N)
            sy=a[1]+b[1]
            if L*L!=N or (sy+L)%2 or sy<L or sy+L>2*(h-1):continue
            lo,hi=(sy-L)//2,(sy+L)//2
            prefix=[-P(a),-P(b)]
            cl.extend([prefix+[-S(lo),S(hi)],prefix+[S(lo),-S(hi)]])
            rivals+=1
    for a in pts:
        arms=[(b,b[0]-a[0],b[1]-a[1]) for b in pts if b[0]!=a[0] and b[1]!=a[1]]
        for i,(b,u,v) in enumerate(arms):
            for c,s,t in arms[i+1:]:
                if u*s+v*t==0 and inside((a[0]+u+s,a[1]+v+t)):
                    cl.append([-P(a),-P(b),-P(c)])
                    dots+=1
    mixed=set()
    for group in pairs.values():
        for a,b,u,v in group:
            for c,d,s,t in group:
                if (u,v)==(s,t) or a in (c,d) or b in (c,d):continue
                tx,ty=c[0]+d[0]-a[0]-b[0],c[1]+d[1]-a[1]-b[1]
                if tx%2 or ty%2 or u*tx+v*ty or (not tx and not ty):continue
                p,q=(a[0]+tx//2,a[1]+ty//2),(b[0]+tx//2,b[1]+ty//2)
                if not inside(p) or not inside(q) or p in (c,d) or q in (c,d):continue
                mixed.add(tuple(sorted((-P(a),-P(b),-P(c),-P(d)))))
    cl.extend(sorted(mixed))
    return vp,cl,P,S,dict(h=h,k=k,width=width,left=left,rectangles_local=nrect,triples=dots,mixed=len(mixed),rivals=rivals)
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('h',type=int)
    ap.add_argument('k',type=int)
    ap.add_argument('--solver',default='cadical195')
    ap.add_argument('--run-width',type=int,help='ambient run of doubles to test')
    ap.add_argument('--parity',action='store_true')
    ap.add_argument('--mask',type=lambda value:int(value,0))
    ap.add_argument('--dimacs',type=Path)
    args=ap.parse_args()
    h,k=args.h,args.k
    vp,cl,P,S,stats=clauses_for(h,k,args.run_width)
    mask=args.mask
    if args.parity:
        if mask is not None: ap.error('choose mask or parity')
        mask=sum(1<<r for r in range(0,h,2))
    if mask is not None:
        if mask < 0 or mask >> h or mask.bit_count() != (h+1)//2: ap.error('invalid balanced mask')
        cl.extend([[S(r) if (mask >> r)&1 else -S(r)] for r in range(h)])
    formula='p cnf %d %d\n'%(vp.top,len(cl))+''.join(' '.join(map(str,c))+' 0\n' for c in cl)
    print(json.dumps(dict(**stats,clauses=len(cl),variables=vp.top,sha256=hashlib.sha256(formula.encode()).hexdigest())),flush=True)
    if args.dimacs:
        with args.dimacs.open('xb') as out: out.write(formula.encode())
        raise SystemExit(0)
    with Solver(name=args.solver,bootstrap_with=cl) as solver:
        start=time.monotonic()
        ok=solver.solve()
        print('SAT' if ok else 'UNSAT',time.monotonic()-start,flush=True)
        if ok:
            model=set(solver.get_model())
            print([[r+1 for r in range(h) if P((x,r)) in model] for x in range(stats['left'],stats['left']+k)])

