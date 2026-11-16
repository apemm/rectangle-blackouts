"""Verify the saved M=2 odd cycle without a generator or SAT solver."""
from pathlib import Path
from math import isqrt
import hashlib
import json


HERE=Path(__file__).resolve().parent


def rank_to_cell(side,rank):
    x=y=0
    work=rank
    scale=1
    while scale<side:
        rx=(work//2)&1
        ry=(work^rx)&1
        if ry==0:
            if rx==1:
                x,y=scale-1-x,scale-1-y
            x,y=y,x
        x+=scale*rx
        y+=scale*ry
        work//=4
        scale*=2
    return x,y


def cell_to_rank(side,x,y):
    rank=0
    scale=side//2
    while scale:
        rx=int(bool(x&scale))
        ry=int(bool(y&scale))
        rank+=scale*scale*((3*rx)^ry)
        if ry==0:
            if rx==1:
                x,y=scale-1-x,scale-1-y
            x,y=y,x
        scale//=2
    return rank


def audit():
    file=HERE/'aligned_m2_side256_minus512_odd_cycle.json'
    data=json.loads(file.read_text())
    side,offset=data['side'],data['offset']
    assert (side,offset,data['choices'],data['outer'])==(256,-512,2,0)
    assert offset%side==0
    cycle=data['cycle']
    assert len(cycle)==51 and len(set(cycle))==51
    assert len(data['witnesses'])==51
    assert all(0<=r<side*side for r in cycle)
    decoded={r:rank_to_cell(side,r) for r in cycle}
    for rank,cell in decoded.items():
        assert cell_to_rank(side,*cell)==rank
    checked=0
    for u,v,record in zip(cycle,cycle[1:]+cycle[:1],data['witnesses']):
        r,s=sorted((u,v))
        assert (r,s)==(record['r'],record['s'])
        a,b=decoded[r],decoded[s]
        assert list(a)==record['cell_r'] and list(b)==record['cell_s']
        horizontal=64*(s-r)
        signed=(2*offset+1+2*(b[1]-a[0]),
                2*offset+1+2*(a[1]-b[0]))
        expected=[]
        for role,vertical in enumerate(signed):
            length=isqrt(horizontal*horizontal+vertical*vertical)
            if length*length==horizontal*horizontal+vertical*vertical:
                expected.append(dict(role=role,X=horizontal,Y=vertical,L=length))
        assert expected and expected==record['norms']
        for choice in (0,1):
            xr,xs=32*(2*r+choice),32*(2*s+choice)
            assert xs-xr==horizontal
            assert any((xs-xr)**2+signed[n['role']]**2==n['L']**2 for n in expected)
            checked+=1
    # Avoiding each zero-difference norm requires alternating binary choices.
    for first in (0,1):
        values=[first^(i&1) for i in range(len(cycle))]
        assert all(values[i]!=values[i+1] for i in range(len(cycle)-1))
        assert values[-1]==values[0]
    return dict(status='PASS: exact binary candidate-system contradiction',
                side=side,offset=offset,choices=2,outer=0,
                distinct_vertices=51,cycle_edges=51,
                equal_choice_norm_tests=checked,
                source_sha256=hashlib.sha256(file.read_bytes()).hexdigest(),
                scope='Candidate private P norm system only. No in-strip '
                      'common-corner or full-board owner assertion.')


if __name__=='__main__':
    result=audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
