"""Exact positive-offset row-one R2s graph through a finite row bound.

Vertices are row-minus-one n. Enumeration uses 4ab=T^2+delta^2,
not a search through column pairs. Only actual sea residue conditions
and the strong same-parity norm gap are retained.
"""
from array import array
from collections import deque, Counter
from math import isqrt
from pathlib import Path
import argparse
import json
import time


def factor_sieve(limit):
    spf=array('I',range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for m in range(p*p,limit+1,p):
                if spf[m]==m:spf[m]=p
    return spf


def divisors(n,spf):
    out=[1]
    while n>1:
        p=spf[n];power=1;old=list(out)
        while n%p==0:
            n//=p;power*=p
            out.extend(v*power for v in old)
    return out


def enumerate_graph(H):
    bounds=[(d,isqrt(H*d)//2) for d in range(2,isqrt(2*H)//2+1,2)]
    limit=max(t*t+d*d for d,t in bounds)
    spf=factor_sieve(limit)
    witnesses={};support_count=0
    for d,tmax in bounds:
        for t in range(d,tmax+1):
            value=t*t+d*d
            for a in divisors(value,spf):
                b=value//a;X=2*t+a;U=X+b
                if X%4 or U%4==0 or (2*t+b)%4==0:continue
                if 2*d*d>X:continue
                if t*U%d:continue
                n=t*U//d
                if n+2*d>H:continue
                assert U<=n and 2*t>=2*d
                assert 4*a*b==(2*t)**2+(2*d)**2
                assert U*(2*t)==n*(2*d)
                assert (b-a)**2==U*U-2*n*(2*d)-(2*d)**2
                key=(n,n+2*d)
                witnesses.setdefault(key,(X,U,2*t,b-a))
                support_count+=1
    return witnesses,support_count,limit


def analyze(witnesses):
    adj={}
    for u,v in witnesses:
        adj.setdefault(u,set()).add(v);adj.setdefault(v,set()).add(u)
    alive=set(adj);degree={u:len(v) for u,v in adj.items()}
    buckets=[set() for _ in range(max(degree.values(),default=0)+1)]
    for u,d in degree.items():buckets[d].add(u)
    degeneracy=0;order=[]
    while alive:
        d=next(i for i,b in enumerate(buckets) if b)
        u=buckets[d].pop();alive.remove(u);degeneracy=max(degeneracy,d);order.append(u)
        for v in adj[u]&alive:
            buckets[degree[v]].remove(v);degree[v]-=1;buckets[degree[v]].add(v)
    color={}
    for u in reversed(order):
        used={color[v] for v in adj[u] if v in color};c=0
        while c in used:c+=1
        color[u]=c
    components=[];seen=set();odd_cycle=None
    for root in sorted(adj):
        if root in seen:continue
        queue=deque([root]);seen.add(root);part={root:0};parent={root:None};verts=[]
        while queue:
            u=queue.popleft();verts.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v);part[v]=part[u]^1;parent[v]=u;queue.append(v)
                elif part.get(v)==part[u] and odd_cycle is None:
                    pu=[];pv=[];x=u
                    while x is not None:pu.append(x);x=parent[x]
                    x=v
                    while x is not None:pv.append(x);x=parent[x]
                    common=next(x for x in pu if x in set(pv))
                    odd_cycle=pu[:pu.index(common)+1]+list(reversed(pv[:pv.index(common)]))
        components.append(len(verts))
    triangles=[]
    for u in sorted(adj):
        for v in adj[u]:
            if v>u:
                for w in adj[u]&adj[v]:
                    if w>v:triangles.append((u,v,w))
    # Tarjan edge blocks distinguish a cactus from a merely2-degenerate graph.
    entry={};low={};edge_stack=[];blocks=[]
    def visit(u,parent):
        entry[u]=low[u]=len(entry)+1
        for v in adj[u]:
            if v==parent:continue
            if v not in entry:
                edge_stack.append((u,v));visit(v,u);low[u]=min(low[u],low[v])
                if low[v]>=entry[u]:
                    block=[]
                    while True:
                        e=edge_stack.pop();block.append(e)
                        if e==(u,v):break
                    blocks.append(block)
            elif entry[v]<entry[u]:
                edge_stack.append((u,v));low[u]=min(low[u],entry[v])
    for u in sorted(adj):
        if u not in entry:visit(u,None)
    histogram=Counter();noncactus=[];cycle_blocks=[]
    for block in blocks:
        vertices=sorted({x for e in block for x in e})
        histogram[len(vertices),len(block)]+=1
        record=dict(n=vertices,edges=[dict(n=[min(u,v),max(u,v)],XUTV=witnesses[min(u,v),max(u,v)]) for u,v in sorted(block)])
        if len(block)>1:
            if len(block)==len(vertices):cycle_blocks.append(record)
            else:noncactus.append(record)
    noncactus.sort(key=lambda z:(len(z['n']),len(z['edges']),z['n']))
    cycle_blocks.sort(key=lambda z:(len(z['n']),z['n']))
    return dict(vertices=len(adj),edges=len(witnesses),degeneracy=degeneracy,
                greedy_colors=1+max(color.values(),default=-1),max_degree=max(map(len,adj.values()),default=0),
                components=len(components),largest_component=max(components,default=0),
                degree_histogram=dict(sorted(Counter(map(len,adj.values())).items())),
                odd_cycle=odd_cycle,triangles=triangles[:20],triangle_count=len(triangles),
                cactus=not noncactus,
                biconnected_histogram=[dict(vertices=v,edges=e,count=c) for (v,e),c in sorted(histogram.items())],
                cycle_blocks=cycle_blocks,noncactus_blocks=noncactus,
                first_edges=[dict(rows=[u+1,v+1],n=[u,v],witness=list(witnesses[u,v]))
                             for u,v in sorted(witnesses)[:20]])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--height',type=int,default=65536)
    args=parser.parse_args();start=time.time()
    witnesses,supports,limit=enumerate_graph(args.height)
    result=dict(n_bound=args.height,supports=supports,sieve_limit=limit,**analyze(witnesses))
    result['seconds']=round(time.time()-start,3)
    target=Path(__file__).with_name('r2s_row_pair_graph_'+str(args.height)+'.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('first_edges','triangles','degree_histogram','cycle_blocks','noncactus_blocks')}))


if __name__=='__main__':main()
