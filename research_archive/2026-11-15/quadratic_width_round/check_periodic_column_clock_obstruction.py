"""Exact endpoint witnesses for fixed dyadic-period monotone clocks."""
from itertools import permutations
from pathlib import Path
import json
from check_hilbert_endpoint_p_obstruction import rank, point, rectangle


def valuation2(x):
    return (x & -x).bit_length()-1


def check(pattern, n):
    P = len(pattern)
    assert P and P & (P-1) == 0
    assert all(d >= 128 and d % 4 == 0 for d in pattern)
    assert n*n % P == 0
    total = sum(pattern)
    X = n*n//P*total-pattern[-1]
    v = valuation2(pattern[-1])
    assert valuation2(n*n//P*total) > v
    assert valuation2(X) == v
    X0 = 1 << v
    g = X//X0
    Y0, L0 = X0*X0//4-1, X0*X0//4+1
    assert g % 2 == 1
    h = 8*L0*g
    A = 5*L0*g
    A += (3-A) % 4
    B = A+Y0*g
    beta = 4 if B % 4 == 0 else 2
    N = 1 << (64*h-1).bit_length()
    I = J = 3*N//8
    odd_base = h//2+3
    n0, n1 = h//8, h//4
    U0, U1 = I-(A-odd_base)//4, J-(B-beta)//4
    assert (A-odd_base) % 4 == (B-beta) % 4 == 0
    assert 2*n1 <= min(U0,U1) <= max(U0,U1) <= N-3*n1
    R = rank(N,I,J)//(n*n)*(n*n)
    assert R % P == 0

    def clock(r):
        blocks, rem = divmod(r,P)
        return blocks*total+sum(pattern[:rem])

    assert clock(R+n*n-1)-clock(R) == X
    corners = [(0,0),(n-1,0),(n-1,n-1),(0,n-1)]
    K = (Y0+1)*g//4
    cases = []
    for c0,c1 in permutations(corners,2):
        if abs(c0[0]-c1[0])+abs(c0[1]-c1[1]) != n-1:
            continue
        if c0[0] == c1[1]:
            odd_at, even_at, c = 0, 1, c0[0]
        else:
            assert c1[0] == c0[1]
            odd_at, even_at, c = 1, 0, c1[0]
        for i,j in (c0,c1):
            assert U0 <= I+i < U0+n0 and U1 <= J+j < U1+n1
        C = (clock(R+odd_at*(n*n-1)),A+4*c)
        D = (clock(R+even_at*(n*n-1)),B+4*c)
        low, high = A-g+4*c,B+g+4*c
        assert 1 < low < high < h
        assert (C[0]-D[0])**2+(C[1]-D[1])**2 == (L0*g)**2
        middle = (clock(R)+clock(R+n*n-1))//2
        owner = I+K+c,J-K+c
        assert U0 <= owner[0] < U0+n0 and U1 <= owner[1] < U1+n1
        assert odd_base+4*(owner[0]-U0) == high
        assert beta+4*(owner[1]-U1) == low
        owner_rank = rank(N,*owner)
        assert point(N,owner_rank) == owner
        assert not R <= owner_rank < R+n*n
        Q0,Q1 = (middle,low),(middle,high)
        tilted = (C,Q0,D,Q1)
        assert rectangle(tilted)
        owner_col = clock(owner_rank)
        if owner_col == middle:
            kind = "hidden"
        else:
            kind = "mixed"
            E,F = (owner_col,low),(owner_col,high)
            axis = (E,Q0,Q1,F)
            assert rectangle(axis) and set(axis) != set(tilted)
            for mask in range(4):
                black = {C,D,E,F} | ({Q0} if mask&1 else set()) | ({Q1} if mask&2 else set())
                assert set(tilted)-black == set(axis)-black
        cases.append({"entry":c0,"exit":c1,"kind":kind})
    assert len(cases) == 8
    return {"pattern":pattern,"n":n,"horizontal_span":X,
            "v2_span":v,"half_factor":g,"h":h,"A":A,"B":B,
            "padded_side":N,"offsets":[U0,U1],"patterns":cases}


def main():
    patterns = [[128],[128,132],[128,256],
                [128,136,140,132],
                [128,132,136,140,144,148,152,156]]
    results = [check(p,n) for p in patterns for n in (16,32,64)]
    data = {"status":"PASS","cases":results,
            "endpoint_patterns_checked":sum(len(c["patterns"]) for c in results)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(data,indent=2)+"\n")
    print(json.dumps({"status":"PASS","cases":len(results),
                      "endpoint_patterns_checked":data["endpoint_patterns_checked"]}))


if __name__ == "__main__":
    main()

