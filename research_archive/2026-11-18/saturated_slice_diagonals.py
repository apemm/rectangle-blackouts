"""Independent saturation check via pairing diagonals in the full physical grid."""
from collections import defaultdict
from itertools import combinations,product
from math import isqrt
import argparse, hashlib, json
from pathlib import Path
from pysat.solvers import Solver

def geometry(h,k,run_width=None):
    m=h*h//4 if run_width is None else run_width
    x0=(m-k)//2
    pts=list(product(range(m), range(h)))
    name=lambda a:1+(a[0]-x0)*h+a[1]
    def local(a): return x0 <= a[0] < x0+k
    def key(a,b): return (a[0]+b[0],a[1]+b[1],(a[0]-b[0])**2+(a[1]-b[1])**2)
    diagonals=defaultdict(list)
    for a,b in combinations(pts,2): diagonals[key(a,b)].append((a,b))
    geo=set()
    rivals=[]
    for x in range(k):
        for y,z in combinations(range(h),2):
            for xx in range(x+1,k):
                geo.add(tuple(sorted((-name((x+x0,y)),-name((x+x0,z)),-name((xx+x0,y)),-name((xx+x0,z))))))
    # Within each rectangle the complement of a possible common black-free pair
    # has two known black points in the tested slice.
    complements=defaultdict(set)
    for group in diagonals.values():
        if len(group)<2: continue
        for d1,d2 in combinations(group,2):
            corners=tuple(sorted((*d1,*d2)))
            if len({a[0] for a in corners})>2 or len({a[1] for a in corners})>2:
                for tri in combinations(corners,3):
                    if all(local(a) for a in tri): geo.add(tuple(sorted(-name(a) for a in tri)))
            for ij in combinations(range(4),2):
                a,b=(corners[j] for j in range(4) if j not in ij)
                if local(a) and local(b):complements[(corners[ij[0]],corners[ij[1]])].add((a,b))
        vertical=[(a[1],b[1]) for a,b in group if a[0]==b[0]]
        for lo,hi in vertical:
            for a,b in group:
                if a[0]!=b[0] and local(a) and local(b): rivals.append((lo,hi,-name(a),-name(b)))
    for choices in complements.values():
        for ab,cd in combinations(choices,2):
            # The compared rectangles share the two key corners; a third
            # common vertex would determine the fourth and hence the rectangle.
            support=set(ab).symmetric_difference(cd)
            if len(support)==4: geo.add(tuple(sorted(-name(a) for a in support)))
    return m,x0,sorted(geo),rivals

def fixed(h,k,mask,base,rivals):
    clauses=list(base)
    for a,b,u,v in rivals:
        if (mask>>a ^ mask>>b)&1: clauses.append((u,v))
    for x in range(k):
        for color in (0,1):
            pts=[1+h*x+r for r in range(h) if mask>>r&1==color]
            clauses.append(tuple(pts))
            clauses.extend((-a,-b) for a,b in combinations(pts,2))
    return clauses

def to_dimacs(num_vars,cls):
    return ('p cnf %d %d\n'%(num_vars,len(cls))+''.join(' '.join(map(str,c))+' 0\n' for c in cls)).encode()

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('h',type=int)
    parser.add_argument('k',type=int)
    parser.add_argument('--mask',type=lambda x:int(x,0))
    parser.add_argument('--dimacs',type=Path)
    parser.add_argument('--solver',default='cadical195')
    cfg=parser.parse_args()
    h,k=cfg.h,cfg.k
    mask=cfg.mask if cfg.mask is not None else sum(1<<r for r in range(0,h,2))
    if mask<0 or mask>>h or mask.bit_count()!=(h+1)//2: parser.error('invalid row mask')
    m,x0,base,rivals=geometry(h,k)
    cls=fixed(h,k,mask,base,rivals)
    frm=to_dimacs(h*k,cls)
    print(json.dumps(dict(h=h,k=k,mask=mask,variables=h*k,clauses=len(cls),sha256=hashlib.sha256(frm).hexdigest())),flush=True)
    if cfg.dimacs:
        with cfg.dimacs.open('xb') as out:out.write(frm)
    else:
        with Solver(name=cfg.solver,bootstrap_with=cls) as solver:
            print('SAT' if solver.solve() else 'UNSAT',flush=True)

