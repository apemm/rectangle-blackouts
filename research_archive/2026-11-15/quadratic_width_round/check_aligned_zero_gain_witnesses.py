"""Replay the saved aligned odd cycles and the abstract integer obstruction.

The finite P witnesses are candidate constraints. No strip or filler
claim is made. This checker imports neither their generator nor a solver.
"""
from itertools import product
from pathlib import Path
import json


def rank(n,x,y):
    if n==1:return 0
    s=n//2
    if x<s and y<s:return rank(s,y,x)
    if x<s:return s*s+rank(s,x,y-s)
    if y>=s:return 2*s*s+rank(s,x-s,y-s)
    return 3*s*s+rank(s,s-1-y,2*s-1-x)


def check_file(name):
    data=json.loads(Path(__file__).with_name(name).read_text())
    side,T,g=data['side'],data['offset'],data['outer']
    assert T%side==0
    points={int(r):tuple(p) for r,p in data['points'].items()}
    for r,(x,y) in points.items():
        assert 0<=x<side and 0<=y<side
        if g&2:x,y=side-1-x,side-1-y
        if g&1:x,y=y,x
        assert rank(side,x,y)==r
    cycle=data['cycle']
    assert len(cycle)%2==1 and len(set(cycle))==len(cycle)
    expected={tuple(sorted((u,v))) for u,v in zip(cycle,cycle[1:]+cycle[:1])}
    supplied=set()
    for witness in data['witnesses']:
        r,s=witness['r'],witness['s'];supplied.add((r,s))
        assert witness['roles']
        for norm in witness['roles']:
            o,e=norm['odd_rank'],norm['even_rank']
            assert {o,e}=={r,s}
            X=96*(s-r)
            Y=2*T+1+2*(points[e][1]-points[o][0])
            assert (X,Y)==(norm['X'],norm['Y'])
            assert X*X+Y*Y==norm['L']**2
    assert supplied==expected
    return dict(file=name,cycle_length=len(cycle),side=side,offset=T,outer=g)


def audit():
    cases=[check_file('aligned_zero_gain_triangle.json'),
           check_file('aligned_zero_gain_odd_cycle.json')]
    three_colors=sum(all(c[i]!=c[j] for i,j in ((0,1),(1,2),(0,2)))
                     for c in product(range(3),repeat=3))
    two_colors=sum(all(c[i]!=c[j] for i,j in ((0,1),(1,2),(0,2)))
                   for c in product(range(2),repeat=3))
    assert (three_colors,two_colors)==(6,0)
    gadget_solutions=[]
    for c in product(range(3),repeat=4):
        if any(c[i]==c[j] for i,j in ((0,1),(1,2),(0,2))):continue
        if any(c[3]-c[i] in (-1,1) for i in range(3)):continue
        gadget_solutions.append(c)
    assert not gadget_solutions
    return dict(status='PASS',cases=cases,triangle_three_colorings=three_colors,
                abstract_gadget_solutions=0)


if __name__=='__main__':
    print(json.dumps(audit(),indent=2))
