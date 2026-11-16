"""Iterative edge-stack decomposition of the saved zero-gain graph."""
from collections import Counter
from pathlib import Path
import json
import time
import numpy as np


def audit():
    started=time.monotonic()
    events=np.load(Path(__file__).with_name('aligned_private_side1024_minus2048_events.npy'))
    edges=events[events[:,2]==0,:2]
    n=1024**2;m=len(edges)
    endpoints=np.r_[edges[:,0],edges[:,1]]
    perm=np.argsort(endpoints,kind='stable')
    adjacent=(perm % m).astype(np.int32)
    degree=np.bincount(endpoints,minlength=n)
    start=np.r_[0,np.cumsum(degree)]
    del events,endpoints,perm
    disc=np.full(n,-1,dtype=np.int32);low=np.zeros(n,dtype=np.int32)
    parent=np.full(n,-1,dtype=np.int32);parent_edge=np.full(n,-1,dtype=np.int32)
    cursor=start[:-1].copy();marked=np.zeros(n,dtype=np.int32)
    clock=0;edge_stack=[];blocks=[];hist=Counter();component_counts=[]
    for root in np.flatnonzero(degree):
        root=int(root)
        if disc[root]>=0:continue
        first_clock=clock;disc[root]=low[root]=clock;clock+=1;dfs=[root]
        component_edges=0
        while dfs:
            u=dfs[-1]
            if cursor[u]<start[u+1]:
                edge=int(adjacent[cursor[u]]);cursor[u]+=1
                if edge==parent_edge[u]:continue
                a,b=map(int,edges[edge]);v=b if a==u else a
                if disc[v]<0:
                    edge_stack.append(edge);component_edges+=1
                    parent[v]=u;parent_edge[v]=edge;disc[v]=low[v]=clock;clock+=1
                    dfs.append(v)
                elif disc[v]<disc[u]:
                    edge_stack.append(edge);component_edges+=1
                    low[u]=min(low[u],disc[v])
                continue
            dfs.pop();p=int(parent[u])
            if p<0:continue
            low[p]=min(low[p],low[u])
            if low[u]>=disc[p]:
                block_id=len(blocks)+1;count_e=count_v=0
                while True:
                    edge=edge_stack.pop();count_e+=1
                    for v in edges[edge]:
                        if marked[v]!=block_id:marked[v]=block_id;count_v+=1
                    if edge==parent_edge[u]:break
                blocks.append((count_v,count_e));hist[count_v]+=1
        assert not edge_stack
        component_counts.append((clock-first_clock,component_edges))
    assert sum(e for v,e in blocks)==m
    assert sum(e for v,e in component_counts)==m
    result=dict(status='PASS: edge-stack accounting',vertices=n,zero_edges=m,
                nontrivial_components=len(component_counts),blocks=len(blocks),
                bridges=sum(v==2 and e==1 for v,e in blocks),
                cyclic_blocks=sum(e>=v for v,e in blocks),
                noncycle_blocks=sum(e>v for v,e in blocks),
                largest_blocks=[dict(vertices=v,edges=e,cycle_rank=e-v+1)
                                for v,e in sorted(blocks,reverse=True)[:20]],
                largest_components=sorted(component_counts,reverse=True)[:5],
                block_size_histogram={str(v):c for v,c in sorted(hist.items())},
                seconds=round(time.monotonic()-started,3))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='block_size_histogram'},indent=2))
    return result


if __name__=='__main__':audit()
