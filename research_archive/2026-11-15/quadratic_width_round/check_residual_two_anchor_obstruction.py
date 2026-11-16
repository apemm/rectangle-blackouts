"""Exact residual integer boundary obstruction, with full-board owners.

This verifies a three-variable subsystem and two prescribed anchor choices.
It does not assert that the unconstrained three-variable system is UNSAT.
"""

import json
from itertools import product
from math import isqrt
from pathlib import Path


def point(n, rank):
    if n == 1:
        return 0, 0
    m = n // 2
    quadrant, rem = divmod(rank, m*m)
    x, y = point(m, rem)
    return ((y,x), (x,y+m), (x+m,y+m),
            (2*m-1-y,m-1-x))[quadrant]


def rank(n, x, y):
    if n == 1:
        return 0
    m = n // 2
    if x < m and y < m:
        return rank(m,y,x)
    if x < m:
        return m*m+rank(m,x,y-m)
    if y >= m:
        return 2*m*m+rank(m,x-m,y-m)
    return 3*m*m+rank(m,m-1-y,2*m-1-x)


def square_divisors(n):
    factors=[]
    p=2
    while p*p <= n:
        e=0
        while n%p == 0:
            n//=p
            e+=1
        if e:
            factors.append((p,2*e))
        p=3 if p==2 else p+2
    if n>1:
        factors.append((n,2))
    out=[1]
    for p,e in factors:
        out=[d*p**j for d in out for j in range(e+1)]
    return out


def exceptional_y(height):
    result=[]
    for y in range(1,height,2):
        slots=sorted((y*y//a-a)//64 for a in square_divisors(y)
                     if a<y and (y*y//a-a)%64==0)
        if any(b-a<=4 for a,b in zip(slots,slots[1:])):
            result.append(y)
    return result


def in_band(t,y):
    # Exact comparison with |t +/- y/2| <= 4 sqrt(2y+1)+1.
    for signed_y in (y,-y):
        lhs=abs(2*t-signed_y)-2
        if lhs<=0 or lhs*lhs<=64*(2*y+1):
            return True
    return False


def main():
    height=65536
    q=32768
    base=895295488
    local=(192,210,597)
    cells={r:point(q,base+r) for r in local}
    assert cells=={192:(16967,15695),210:(16966,15690),
                   597:(16976,15711)}
    for r,p in cells.items():
        assert rank(q,*p)==base+r

    pair_sets={}
    for r,s in ((192,210),(192,597),(210,597)):
        a,b=cells[r],cells[s]
        ys=(abs(2*b[1]+2-(2*a[0]+1)),
            abs(2*b[0]+1-(2*a[1]+2)))
        bad=[]
        for delta in range(-2,3):
            x=32*(3*(s-r)+delta)
            if any(isqrt(x*x+y*y)**2==x*x+y*y for y in ys):
                bad.append(delta)
        pair_sets[(r,s)]=bad
    assert pair_sets[(192,210)]==[-1,1]
    assert pair_sets[(192,597)]==[0]
    assert pair_sets[(210,597)]==[]

    allowed=[]
    for choices in product(range(3),repeat=3):
        assignment=dict(zip(local,choices))
        if all(assignment[s]-assignment[r] not in bad
               for (r,s),bad in pair_sets.items()):
            allowed.append(choices)
    assert allowed
    assert not any(a==b==1 for c,a,b in allowed)
    relation=sum(1<<(3*a+b) for a,b in product(range(3),repeat=2)
                 if any(aa==a and bb==b for c,aa,bb in allowed))
    assert relation==495  # All nine anchor pairs except (1,1).

    records=[]
    all_cells=set(cells.values())
    for leaf_choice in range(3):
        assignment={192:leaf_choice,210:1,597:1}
        r,s=192,(597 if leaf_choice==1 else 210)
        a,b=cells[r],cells[s]
        xa=32*(3*(base+r)+assignment[r])
        xb=32*(3*(base+s)+assignment[s])
        for ya,yb in ((2*a[0]+1,2*b[1]+2),
                      (2*a[1]+2,2*b[0]+1)):
            x=xb-xa
            y=abs(yb-ya)
            ell=isqrt(x*x+y*y)
            if ell*ell!=x*x+y*y:
                continue
            lo,hi=(ya+yb-ell)//2,(ya+yb+ell)//2
            assert 1<=lo<hi<=height
            assert (xa+xb)%2==0
            xm=(xa+xb)//2
            odd,even=(lo,hi) if lo%2 else (hi,lo)
            owner=((odd-1)//2,(even-2)//2)
            owner_rank=rank(q,*owner)
            all_cells.add(owner)
            presentations=[]
            for owner_choice in range(3):
                xo=32*(3*owner_rank+owner_choice)
                assert xo!=xm
                tilted={(xa,ya),(xb,yb),(xm,lo),(xm,hi)}
                axis={(xm,lo),(xm,hi),(xo,lo),(xo,hi)}
                black={(xa,ya),(xb,yb),(xo,lo),(xo,hi)}
                assert len(tilted)==len(axis)==4 and tilted!=axis
                assert tilted.symmetric_difference(axis)<=black
                assert tilted-black==axis-black
                presentations.append(sorted(tilted-black))
            records.append({"leaf_choice":leaf_choice,
                "pair_ranks":[base+r,base+s],"rows":[ya,yb],
                "horizontal_leg":x,"vertical_leg":y,"hypotenuse":ell,
                "white_rows":[lo,hi],"owner_cell":owner,
                "owner_rank":owner_rank,
                "all_three_owner_choices_pass":True})
    assert len(records)==3
    exceptions=exceptional_y(height)
    diagonals=sorted({j-i for i,j in all_cells})
    assert not any(in_band(t,y) for t in diagonals for y in exceptions)
    result={"height":height,"side":q,"stride":32,"choices":3,
        "block_start":base,"local_ranks":local,"cells":cells,
        "pair_forbidden_differences":[[r,s,bad] for (r,s),bad in pair_sets.items()],
        "integer_solutions":allowed,"anchor_relation_mask":relation,
        "norm_and_presentation_certificates":records,
        "exceptional_vertical_legs_below_height":exceptions,
        "retained_source_and_owner_diagonals":diagonals,
        "all_source_and_owner_labels_outside_deleted_bands":True,
        "status":"PASS"}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
