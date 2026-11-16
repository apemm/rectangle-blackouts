"""Exact small certificates for the period-four sea obstructions."""
from pathlib import Path
import json
from check_four_block_obstruction import rectangle


def check_mixed(S, z, H, L=3, F=2):
    b = H-8*z
    assert 0 < b < H and S % 4 == 0
    center = 10*S
    sea_x = [center-4, center+4*(z*z-1), center+4*z*z]
    assert all(x % 4 == 0 and x % S for x in sea_x)
    E = (center, b)
    A, C, B = [(x, H) for x in sea_x]
    P, Q = (A[0], H-4*z), (B[0], H-4*z)
    tilted, axis = (E, P, C, Q), (A, P, Q, B)
    assert rectangle(tilted) and rectangle(axis)
    black = {E, A, B, C}
    assert set(tilted)-black == set(axis)-black == {P, Q}
    assert 1 <= P[1] < H and 1 <= Q[1] < H
    assert (4*(z*z-1))**2+(8*z)**2 == (4*(z*z+1))**2
    return dict(S=S, z=z, H=H, b=b, label=E, sea=[A,C,B],
                common=[P,Q], tilted=tilted, axis=axis)


def check_sea():
    L, F, H = 1, 2, 8
    W = (9, 7)
    triples = [[(2,2),(3,1),(8,8)],[(14,2),(11,1),(12,8)]]
    for B,A,C in triples:
        assert rectangle((B,A,W,C))
        for x,y in (A,B,C):
            assert y == (L if x%2 else F if x%4==2 else H)
    assert set(triples[0]) != set(triples[1])
    return dict(sea=[L,F,H], white=W, triples=triples)


def check_low_side(S,z,H,L=3,F=2):
    assert S%32 == 0 and z%8 in (3,5)
    b=H-4*z
    assert F < b < H
    center=10*S
    E=(center,b)
    C=(center+2*(z*z-1),H)
    P,Q=(center-2,H-2*z),(center+2*z*z,H-2*z)
    A,B=(P[0],F),(Q[0],F)
    assert C[0]%4 == 0 and C[0]%S
    assert A[0]%4 == B[0]%4 == 2
    assert A[0]%S and B[0]%S
    assert rectangle((E,P,C,Q)) and rectangle((A,P,Q,B))
    black={E,C,A,B}
    assert set((E,P,C,Q))-black == set((A,P,Q,B))-black == {P,Q}
    return dict(S=S,z=z,H=H,b=b,label=E,sea=[A,C,B],common=[P,Q])


if __name__ == '__main__':
    cases = [check_mixed(64,10,200),check_mixed(64,18,320),
             check_mixed(128,34,600),check_mixed(6272,1570,20000)]
    low_cases=[check_low_side(64,3,200),check_low_side(128,13,200),
               check_low_side(6272,101,2000)]
    result = dict(status='PASS',mixed=cases,low_side=low_cases,sea_only=check_sea(),
                  scope='Explicit period-four sea collisions; no general threshold claim.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',mixed_cases=len(cases)+len(low_cases),sea_only_cases=1)))
