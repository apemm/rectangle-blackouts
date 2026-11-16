"""Complete finite-period right-triangle tests for the lowbit sea."""
from math import isqrt
from collections import defaultdict
from pathlib import Path
import json
from check_four_block_obstruction import rectangle


def signed_divisors(n):
    n=abs(n)
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            yield d;yield -d
            if d*d!=n:
                yield n//d;yield -n//d


def search(e):
    S=1<<e
    rows=[1<<r for r in range(e)]
    def sea(x):
        return None if x%S==0 else x&-x
    completions=defaultdict(set)
    for x0 in range(1,S):
      y0=sea(x0)
      for y1 in rows:
       for y2 in rows:
        N=-(y1-y0)*(y2-y0)
        if not N:
            continue
        for u in signed_divisors(N):
         v=N//u
         if sea(x0+u)!=y1 or sea(x0+v)!=y2:
             continue
         W=(x0+u+v,y1+y2-y0)
         if W[1]<1:
             continue
         assert sea(W[0])!=W[1]
         triple=tuple(sorted(((x0-W[0],y0),(x0+u-W[0],y1),
                              (x0+v-W[0],y2))))
         completions[(W[0]%S,W[1])].add(triple)
    assert all(len(v)==1 for v in completions.values())
    return dict(e=e,white_patterns=len(completions),status='PASS')


def check_bitflip_counterexample(k=0,extra=0):
    scale=1<<k
    S=1<<(k+5)
    b0=6*scale+extra*(1<<(k+4))
    rows=[((b0+(1<<r))%(1<<(r+1))) or (1<<(r+1)) for r in range(k+5)]
    def sea(x):
        return None if x%S==0 else rows[(x&-x).bit_length()-1]
    W=(39*scale,11*scale)
    base=[[(70,4),(40,14),(69,1)],[(22,4),(24,14),(37,1)]]
    triangles=[[(scale*x,scale*y) for x,y in t] for t in base]
    for R,A,B in triangles:
        assert all(sea(x)==y for x,y in (R,A,B))
        assert rectangle((R,A,W,B))
    assert sea(W[0])!=W[1]
    return dict(S=S,reference_even_residue=b0,rows=rows,white=W,
                black_triples=triangles,status='PASS')


if __name__=='__main__':
    result=dict(unshifted=[search(e) for e in range(2,8)],
                bitflip_obstruction=[check_bitflip_counterexample(k,t)
                                     for k in range(5) for t in (0,1)])
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
