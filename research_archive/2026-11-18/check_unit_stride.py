"""Independently certify the four-offset result by Euclidean triples and direct rank scans."""
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json
import sys
import numpy as np
from numba import njit

HERE=Path(__file__).resolve().parent


@njit(cache=False)
def coords(s):
    xs=np.empty(s*s,np.int32)
    ys=np.empty(s*s,np.int32)
    for r in range(s*s):
        x=y=0
        t=r
        b=1
        while b<s:
            rx=(t//2)&1
            ry=(t^rx)&1
            if ry==0:
                if rx==1:
                    x,y=b-1-x,b-1-y
                x,y=y,x
            x+=b*rx
            y+=b*ry
            t//=4
            b*=2
        xs[r]=x
        ys[r]=y
    return xs,ys


def triples(s,Q):
    ymax=6*s-3
    out={}
    for u in range(2,(ymax+1)//2+1):
        for v in range(max(1,isqrt(max(0,u*u-ymax))),u):
            if (u-v)%2==0 or gcd(u,v)!=1:
                continue
            X,Y=2*u*v,u*u-v*v
            start=max(1,(2*s+1+Y-1)//Y)
            for a in range(start+(1-start)%2,ymax//Y+1,2):
                xx=a*X
                if xx%Q==0 and 0<xx//Q<s*s:
                    assert xx*xx+(a*Y)**2==(a*(u*u+v*v))**2
                    out.setdefault(xx//Q,set()).add(a*Y)
    return out


@njit(cache=False)
def count(d,lookup,x,y,col,s):
    total=bad=0
    base=4*s-1
    for r in range(len(col)-d):
        v=r+d
        if (lookup[base+2*(x[r]-y[v])] or lookup[base+2*(x[v]-y[r])]):
            total+=1
            if col[r]==col[v]:
                bad+=1
    return total,bad


def main():
    Q=int(sys.argv[1])
    for s in map(int,sys.argv[2:]):
        colors=np.load(HERE/f'unit_stride_{s}_{Q}.npz')['colors']
        assert len(colors)==s*s and colors.min()>=0 and colors.max()<=3
        assert Q%4==0 and Q>=4
        x,y=coords(s)
        assert len(np.unique(x*s+y))==s*s
        legs=triples(s,Q)
        total=bad=0
        table=np.zeros(6*s,np.bool_)
        for d,ys in legs.items():
            indices=list(ys)
            table[indices]=True
            t,b=count(d,table,x,y,colors,s)
            total+=t
            bad+=b
            table[indices]=False
        gen=json.loads((HERE/f'unit_stride_{s}_{Q}.json').read_text())
        assert total==gen['zero_edges'] and bad==0
        h=sha256(colors.tobytes()).hexdigest()
        assert h==gen['assignment_sha256']
        rec=dict(side=s,Q=Q,distinct_rank_lags=len(legs),zero_edges=total,
                 monochromatic_pairs=bad,assignment_sha256=h,status='PASS')
        print(json.dumps(rec),flush=True)
        (HERE/f'unit_stride_check_{s}_{Q}.json').write_text(json.dumps(rec,indent=2)+'\n')


if __name__=='__main__':
    main()
