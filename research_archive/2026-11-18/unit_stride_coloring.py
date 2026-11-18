"""Construct a four-color placement using only equal-offset norm events."""
from hashlib import sha256
import json
from pathlib import Path
import sys
import numpy as np
from numba import njit
from integer_star import HERE, enumerate_lag, odd_legs


def zero_edges(s, Q):
    n = s*s
    chunks = []
    for d,y in odd_legs(6*s-3, Q, n-1):
        k = (4*s-1-y)//2
        if abs(k) >= s:
            continue
        for role in (0,1):
            r = np.asarray(enumerate_lag(s,d,k,role,0),dtype=np.int64)
            if r.size:
                chunks.append(r*n+r+d)
    if not chunks:
        return np.empty((0,2),np.int32)
    keys = np.unique(np.concatenate(chunks))
    return np.column_stack((keys//n, keys%n)).astype(np.int32)


@njit(cache=False)
def peel(n, e):
    off=np.zeros(n+1,np.int32)
    for a,b in e:
        off[a+1]+=1
        off[b+1]+=1
    off=np.cumsum(off)
    ix=off[:-1].copy()
    adj=np.empty(2*len(e),np.int32)
    for a,b in e:
        adj[ix[a]]=b
        adj[ix[b]]=a
        ix[a]+=1
        ix[b]+=1
    deg=off[1:]-off[:-1]
    queue=np.empty(n,np.int32)
    head=tail=0
    for a in range(n):
        if deg[a]<4:
            queue[tail]=a
            tail+=1
    while head<tail:
        a=queue[head]
        head+=1
        for j in range(off[a],off[a+1]):
            b=adj[j]
            deg[b]-=1
            if deg[b]==3:
                queue[tail]=b
                tail+=1
    col=np.full(n,-1,np.int8)
    if tail==n:
        for a in queue[::-1]:
            avail=15
            for j in range(off[a],off[a+1]):
                c=col[adj[j]]
                if c>=0:
                    avail &= ~(1 << c)
            assert avail
            for c in range(4):
                if avail & (1<<c):
                    col[a]=c
                    break
        for a,b in e:
            assert col[a]!=col[b]
    return n-tail,col


def main():
    Q=int(sys.argv[1])
    assert Q>=4 and Q%4==0
    for s in map(int,sys.argv[2:]):
        assert s>0 and s&(s-1)==0
        e=zero_edges(s,Q)
        unresolved,col=peel(s*s,e)
        rec=dict(side=s,Q=Q,zero_edges=len(e),four_core_vertices=int(unresolved))
        if unresolved==0:
            rec['assignment_sha256']=sha256(col.tobytes()).hexdigest()
            rec['histogram']=np.bincount(col,minlength=4).tolist()
            np.savez_compressed(HERE/f'unit_stride_{s}_{Q}.npz',colors=col)
        (HERE/f'unit_stride_{s}_{Q}.json').write_text(json.dumps(rec,indent=2)+'\n')
        print(json.dumps(rec),flush=True)


if __name__=='__main__':
    main()
