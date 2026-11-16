"""Uniform finite-state exclusion of aligned S32/M3 dyadic quadratic K4s."""
from itertools import product
from collections import deque,Counter
from pathlib import Path
from functools import lru_cache
import json
from check_hilbert_quadratic_clique_exclusions import OPTIONS

BITS=tuple(product(range(2),repeat=4))
INITIAL=frozenset((*o,0,0,0) for o in product(range(4),repeat=4))

def strong_templates():
    pairs=tuple((i,j) for i in range(4) for j in range(i+1,4))
    count=Counter()
    templates=[]
    for mask in range(64):
        edges=tuple((j,i) if mask>>k&1 else (i,j) for k,(i,j) in enumerate(pairs))
        score=tuple(sorted(sum(i==u for i,j in edges) for u in range(4)))
        count[score]+=1
        if score!=(1,1,2,2):continue
        adj=[[] for _ in range(8)]
        for i,j in edges:
            w=-(j-i)**2
            adj[i].append((4+j,w));adj[4+j].append((i,-w))
        comp=[None]*8;pot=[None]*8;groups=[]
        for vertex in range(8):
            if pot[vertex] is not None:continue
            group=[];pot[vertex]=0;comp[vertex]=len(groups);todo=[vertex]
            while todo:
                u=todo.pop();group.append(u)
                for v,w in adj[u]:
                    if pot[v] is None:
                        pot[v]=pot[u]+w;comp[v]=comp[u];todo.append(v)
                    else:assert pot[v]==pot[u]+w
            groups.append(group)
        assert sorted(map(len,groups))==[2,6]
        big=max(range(2),key=lambda j:len(groups[j]));small=1-big
        for group in groups:
            minimum=min(pot[v] for v in group)
            for v in group:pot[v]-=minimum
        source=next(v for v in groups[small] if v<4)
        target=next(v-4 for v in groups[small] if v>=4)
        coeff=tuple(value for i in range(4) for value in (pot[i],pot[4+i]))
        base=tuple(value for i in range(4) for value in (0 if comp[i]==big else 2,1 if comp[4+i]==big else 3))
        templates.append(dict(mask=mask,edges=edges,positions=(source,target),coeff=coeff,base=base))
    assert count==Counter({(0,1,2,3):24,(1,1,1,3):8,(0,2,2,2):8,(1,1,2,2):24})
    return templates

@lru_cache(None)
def modular_step(state,positions,mode='any',equal=False):
    *orient,c0,c1,c2=state
    result=set()
    for a,b,z,w in BITS:
        if equal and a!=b:continue
        rel=a+w-b-z+c0
        if rel%2:continue
        xy=[(a,b)]*4
        xy[positions[0]]=(z,b);xy[positions[1]]=(a,w)
        pairs=[OPTIONS[orient[i],*xy[i]] for i in range(4)]
        parent=tuple(v[0] for v in pairs);q=tuple(v[1] for v in pairs)
        delta=(q[1]-q[0])%4
        if mode=='zero' and delta:continue
        if mode=='odd' and not delta%2:continue
        if mode=='two' and delta!=2:continue
        cfirst=q[0]-2*q[1]+q[2]+c1
        csecond=q[1]-2*q[2]+q[3]+c2
        if cfirst%4 or csecond%4:continue
        result.add((*parent,rel//2,cfirst//4,csecond//4))
    return frozenset(result)

def advance(states,positions,n=1,mode='any',equal=False):
    states=frozenset(states)
    for _ in range(n):
        states=frozenset(nxt for state in states for nxt in modular_step(state,positions,mode,equal))
    return states

def prefix_certificate(positions):
    union=set();small=[]
    for t in range(4):
        j=t//2;states=INITIAL
        for depth in range(1,8+2*t):
            mode='zero' if depth<j+1 else ('two' if t%2 else 'odd') if depth==j+1 else 'any'
            states=advance(states,positions,mode=mode,equal=depth<=2)
        small.append(sorted(states));union.update(states)
    invariant=advance(INITIAL,positions,n=2,mode='zero',equal=True)
    assert len(invariant)==32
    assert advance(invariant,positions,mode='zero')==invariant
    tails=[]
    for epsilon in (0,1):
        source=advance(invariant,positions,mode='two' if epsilon else 'odd')
        current=advance(source,positions,n=12+2*epsilon)
        orbit=[];seen={}
        while current not in seen:
            seen[current]=len(orbit);orbit.append(sorted(current));union.update(current)
            current=advance(current,positions,n=3)
        tails.append(dict(epsilon=epsilon,initial_exponent=12+2*epsilon,
                          preperiod=seen[current],period=len(orbit)-seen[current],
                          orbit_states=orbit,orbit_counts=[len(v) for v in orbit]))
    return dict(positions=positions,small_t_states=small,small_t_counts=[len(v) for v in small],
                zero_invariant=sorted(invariant),tail_orbits=tails,seed_states=sorted(union))

def exact_step(state,coeff,base):
    orient=state[:4];c0,c1,c2=state[4:7];carry=state[7:]
    result=set()
    for bits in BITS:
        a,b,z,w=bits;rel=a+w-b-z+c0
        if rel%2:continue
        values=[bits[base[i]]+carry[i] for i in range(8)]
        xy=[v%2 for v in values]
        pairs=[OPTIONS[orient[i],xy[2*i],xy[2*i+1]] for i in range(4)]
        parent=tuple(v[0] for v in pairs);q=tuple(v[1] for v in pairs)
        first=q[0]-2*q[1]+q[2]+c1
        second=q[1]-2*q[2]+q[3]+c2
        if first%4 or second%4:continue
        newcarry=tuple(v//2 for v in values)
        assert all(0<=newcarry[i]<=coeff[i] for i in range(8))
        result.add((*parent,rel//2,first//4,second//4,*newcarry))
    return result

def audit():
    prefixes={};results=[]
    for template in strong_templates():
        positions=template['positions'];coeff=template['coeff'];base=template['base']
        if positions not in prefixes:prefixes[positions]=prefix_certificate(positions)
        seed={(*state,*coeff) for state in prefixes[positions]['seed_states']}
        reached=set(seed);todo=deque(seed)
        while todo:
            state=todo.popleft()
            assert any(state),'An accepting aligned quadratic K4 state was found.'
            for nxt in exact_step(state,coeff,base):
                if nxt not in reached:reached.add(nxt);todo.append(nxt)
        results.append(dict(**template,seed_count=len(seed),reachable_count=len(reached),
                            reachable_states=sorted(reached)))
    assert len(results)==24
    return dict(status='PASS',prefix_certificates=list(prefixes.values()),templates=results,
                max_reachable=max(v['reachable_count'] for v in results),
                scope='All t>=0; S32/M3; c=2^(7+2t); aligned offset necessary condition C=0mod4.')

if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'strong_orientations':len(result['templates']),
                      'max_reachable':result['max_reachable'],
                      'seed_sizes':sorted(set(v['seed_count'] for v in result['templates']))}))
