"""Search-free independent checks and full extensions of saved private choices.

No solver or producer geometry is imported.  Queue peeling, rotate/add
Hilbert decoding, and math.isqrt are used throughout the certificate audit.
"""
from collections import deque
from math import isqrt
from pathlib import Path
import ast
import hashlib
import json
import time
import numpy as np


HERE = Path(__file__).resolve().parent


def decode(side, outer=0):
    ranks = np.arange(side*side,dtype=np.int64)
    work = ranks.copy()
    x = np.zeros_like(ranks)
    y = np.zeros_like(ranks)
    scale = 1
    while scale < side:
        rx = (work//2)&1
        ry = (work^rx)&1
        reflected = (ry==0)&(rx==1)
        x = np.where(reflected,scale-1-x,x)
        y = np.where(reflected,scale-1-y,y)
        swapped = ry==0
        x,y = np.where(swapped,y,x),np.where(swapped,x,y)
        x += scale*rx
        y += scale*ry
        work //= 4
        scale *= 2
    if outer&1:
        x,y = y,x
    if outer&2:
        x,y = side-1-x,side-1-y
    return x,y


def queue_peel(size, events):
    """Delete vertices sequentially, counting each gain as one edge."""
    endpoints = np.concatenate((events[:,0],events[:,1]))
    permutation = np.argsort(endpoints,kind='stable')
    adjacency = (permutation % len(events)).astype(np.int32)
    degree = np.bincount(endpoints,minlength=size).astype(np.int32)
    start = np.empty(size+1,dtype=np.int64)
    start[0]=0
    np.cumsum(degree,out=start[1:])
    del endpoints,permutation
    live = np.ones(size,dtype=bool)
    live_edge = np.ones(len(events),dtype=bool)
    pending = deque(int(v) for v in np.flatnonzero(degree<3))
    order=[]
    while pending:
        vertex = pending.popleft()
        if not live[vertex]:
            continue
        assert degree[vertex] < 3
        live[vertex]=False
        order.append(vertex)
        for edge_index in adjacency[start[vertex]:start[vertex+1]]:
            if not live_edge[edge_index]:
                continue
            live_edge[edge_index]=False
            u,v,_ = events[edge_index]
            other = int(v) if int(u)==vertex else int(u)
            assert live[other]
            degree[other]-=1
            if degree[other]==2:
                pending.append(other)
    assert np.all(degree[live]>=3)
    assert np.all(live_edge == (live[events[:,0]] & live[events[:,1]]))
    return np.flatnonzero(live),order,live_edge,adjacency,start


def norm_hit(r,s,delta,x,y,offset):
    horizontal = 32*(3*(s-r)+delta)
    base = horizontal*horizontal
    first = 2*offset+1+2*(int(y[s])-int(x[r]))
    second = 2*offset+1+2*(int(y[r])-int(x[s]))
    return (isqrt(base+first*first)**2 == base+first*first or
            isqrt(base+second*second)**2 == base+second*second)


def verify(side,offset,model,stem):
    started=time.monotonic()
    events_file=HERE/f'aligned_private_side{side}_minus{-offset}_events.npy'
    events=np.load(events_file)
    assert events.ndim==2 and events.shape[1]==3
    size=side*side
    assert np.all((events[:,0]>=0)&(events[:,0]<events[:,1])&
                  (events[:,1]<size)&(events[:,2]>=0)&(events[:,2]<3))
    keys=3*(size*events[:,0].astype(np.int64)+events[:,1])+events[:,2]
    assert len(np.unique(keys))==len(events)
    del keys
    vertices,order,live_edge,adjacency,start=queue_peel(size,events)
    certificate=np.load(HERE/f'{stem}.npz')
    assert np.array_equal(vertices,certificate['vertices'])
    saved_colors=certificate['colors']
    assert len(saved_colors)==len(vertices) and np.all((saved_colors>=0)&(saved_colors<3))
    colors=np.full(size,-1,dtype=np.int8)
    colors[vertices]=saved_colors
    x,y=decode(side)
    print('independent peel',side,len(vertices),int(live_edge.sum()),flush=True)

    # Check that every original modular event has a real signed witness.
    # Also check the saved core assignment directly, without mask reuse.
    masks=np.zeros(len(events),dtype=np.uint8)
    modular_core_hits=0
    for index,(rr,ss,gg) in enumerate(events):
        r,s,g=int(rr),int(ss),int(gg)
        positive=norm_hit(r,s,g,x,y,offset)
        negative=norm_hit(r,s,g-3 if g else 0,x,y,offset)
        assert positive or negative,(side,'invalid supplied event',r,s,g)
        masks[index]=int(positive)+2*int(negative)
        if live_edge[index]:
            delta=int(colors[s])-int(colors[r])
            modular_hit=(delta-g)%3==0
            modular_core_hits+=int(modular_hit)
            if model=='modular':
                assert not modular_hit
            assert not norm_hit(r,s,delta,x,y,offset),(side,'invalid core color',r,s,delta)
    print('all supplied norms and core colors checked',side,flush=True)

    # Compare the producer's vector masks to the independent isqrt masks.
    # Extract this single function without importing any solver module.
    tree=ast.parse((HERE/'probe_aligned_private_sat.py').read_text())
    function=next(node for node in tree.body
                  if isinstance(node,ast.FunctionDef) and node.name=='actual_delta_masks')
    namespace={'np':np}
    exec(compile(ast.Module(body=[function],type_ignores=[]),
                 'extracted_actual_delta_masks','exec'),namespace)
    positive,negative=namespace['actual_delta_masks'](side,offset,0,events[live_edge])
    assert np.array_equal(positive,(masks[live_edge]&1)!=0)
    assert np.array_equal(negative,(masks[live_edge]&2)!=0)

    # At removal each vertex had at most two remaining gain edges.
    # In reverse order, each such edge forbids at most one of three colors.
    for vertex in reversed(order):
        forbidden=set()
        colored_edges=0
        for edge_index in adjacency[start[vertex]:start[vertex+1]]:
            rr,ss,gg=events[edge_index]
            r,s,g=int(rr),int(ss),int(gg)
            other=s if vertex==r else r
            if colors[other]<0:
                continue
            colored_edges+=1
            candidate=(int(colors[other])-g)%3 if vertex==r else (int(colors[other])+g)%3
            if model=='modular':
                forbidden.add(candidate)
            else:
                delta=int(colors[other])-candidate if vertex==r else candidate-int(colors[other])
                if norm_hit(r,s,delta,x,y,offset):
                    forbidden.add(candidate)
        assert colored_edges<=2 and len(forbidden)<=2
        colors[vertex]=next(c for c in range(3) if c not in forbidden)
    assert np.all((colors>=0)&(colors<3))

    final_modular_hits=0
    for rr,ss,gg in events:
        r,s,g=int(rr),int(ss),int(gg)
        delta=int(colors[s])-int(colors[r])
        final_modular_hits+=int((delta-g)%3==0)
        if model=='modular':
            assert (delta-g)%3!=0
        assert not norm_hit(r,s,delta,x,y,offset),(side,'invalid full color',r,s,delta)

    output=HERE/f'{stem}_independent_full.npz'
    np.savez_compressed(output,colors=colors)
    result=dict(side=side,offset=offset,outer=0,model=model,
                status='PASS: independently peeled, extended, and checked without search',
                events=len(events),core_vertices=len(vertices),core_events=int(live_edge.sum()),
                peeled_vertices=len(order),core_modular_hits=modular_core_hits,
                full_modular_hits=final_modular_hits,
                producer_masks_match_independent_isqrt=True,
                integer_mask_histogram={str(k):int(np.sum(masks==k)) for k in (1,2,3)},
                events_sha256=hashlib.sha256(events.astype('<i4',copy=False).tobytes()).hexdigest(),
                full_colors_sha256=hashlib.sha256(colors.tobytes()).hexdigest(),
                full_certificate=output.name,
                seconds=round(time.monotonic()-started,3))
    print(json.dumps(result),flush=True)
    return result


def audit():
    cases=[verify(512,-1024,'modular','aligned_private_side512_minus1024_sat'),
           verify(1024,-2048,'integer','aligned_private_side1024_minus2048_integer_sat')]
    result=dict(status='PASS',cases=cases,
                scope='Every supplied event is checked against exact norms. '
                      'Completeness of the supplied event universe uses the separately '
                      'audited complete rank-lag generator. No finite-strip owner claim.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    return result


if __name__=='__main__':
    audit()
