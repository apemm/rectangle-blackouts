"""Uniform geometric reduction for even t>=4, without a solvability claim."""
from itertools import product
from collections import deque
from pathlib import Path
import json
from check_aligned_dyadic_quadratic_k4 import strong_templates,advance
from check_hilbert_odd_valuation_alignment import step,terminal

FIRST={13,19,44,50}
SECOND={17,29,34,46}


def audit():
    cases=[]
    for p in strong_templates():
        for generator in (1,3):
            initial=frozenset((*o,0,0,0) for g in range(4)
                              for o in product((g,g^generator),repeat=4))
            current=advance(advance(initial,p['positions'],mode='odd'),p['positions'],n=12)
            orbit=[];seen={}
            while current not in seen:
                seen[current]=len(orbit)
                if p['mask'] not in FIRST|SECOND:
                    assert not current
                    orbit.append(dict(seed=[]))
                elif p['mask'] in SECOND:
                    spreads=[max(c for c,b in zip(p['coeff'],p['base']) if b==i)
                             -min(c for c,b in zip(p['coeff'],p['base']) if b==i)
                             for i in range(4)]
                    assert max(spreads)>=8
                    cbits=(1,0,0) if generator==1 else (1,1,1)
                    states=frozenset((*s,*([0]*8)) for s in current)
                    for cb in cbits:
                        states=frozenset(n for s in states for n in step(s,p['coeff'],p['base'],cb))
                    reached=set(states);todo=deque(states)
                    while todo:
                        s=todo.popleft()
                        assert not terminal(s,p['base'])
                        for cb in (0,1):
                            for n in step(s,p['coeff'],p['base'],cb):
                                if n not in reached:reached.add(n);todo.append(n)
                    orbit.append(dict(seed=sorted(current),bits=cbits,after_bits=sorted(states),suffix=sorted(reached)))
                else:
                    orbit.append(dict(seed=sorted(current),status='not excluded'))
                current=advance(current,p['positions'],n=3)
            cases.append(dict(mask=p['mask'],generator=generator,preperiod=seen[current],
                              period=len(orbit)-seen[current],orbit=orbit))
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    symmetries=[]
    for p in strong_templates():
        if p['mask'] not in FIRST|SECOND:continue
        reversed_edges={(3-u,3-v) for u,v in p['edges']}
        reverse=sum(1<<i for i,(u,v) in enumerate(pairs) if (v,u) in reversed_edges)
        complement=63-p['mask']
        group=FIRST if p['mask'] in FIRST else SECOND
        assert reverse in group and complement in group
        symmetries.append(dict(mask=p['mask'],reverse=reverse,complement=complement))
    return dict(status='PASS: even-t family reduced to two symmetry classes',cases=cases,symmetries=symmetries)


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'])
