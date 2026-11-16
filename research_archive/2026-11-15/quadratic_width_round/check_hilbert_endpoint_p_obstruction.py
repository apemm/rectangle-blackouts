"""Sparse exact checks for the orientation-independent endpoint P witness."""
from itertools import permutations
from pathlib import Path
import json


def point(n, d):
    x = y = 0
    s = 1
    while s < n:
        rx = (d // 2) & 1
        ry = (d ^ rx) & 1
        if ry == 0:
            if rx:
                x, y = s - 1 - x, s - 1 - y
            x, y = y, x
        x += s * rx
        y += s * ry
        d //= 4
        s *= 2
    return x, y


def rank(n, x, y):
    if n == 1:
        return 0
    s = n // 2
    if x < s and y < s:
        return rank(s, y, x)
    if x < s:
        return s*s + rank(s, x, y-s)
    if y >= s:
        return 2*s*s + rank(s, x-s, y-s)
    return 3*s*s + rank(s, s-1-y, 2*s-1-x)


def rectangle(v):
    a, b, c, d = v
    return (len(set(v)) == 4
            and a[0]+c[0] == b[0]+d[0]
            and a[1]+c[1] == b[1]+d[1]
            and sum((a[k]-c[k])**2 for k in (0, 1))
            == sum((b[k]-d[k])**2 for k in (0, 1)))


def check(n, S, D=4):
    assert n >= 2 and n & (n-1) == 0
    assert S >= 128 and S & (S-1) == 0
    assert D in (4, 8)
    assert D == 4 or n >= 4
    q = n*n-1
    Y0, L0 = S*S//4-1, S*S//4+1
    h = 8*L0*q
    A, B = 5*L0*q, (5*L0+Y0)*q
    side = 64*S*S*n*n
    I = J = 3*side//8
    odd_base, even_base = h//2+(3 if D == 4 else 7), 4
    n0, n1 = (h-odd_base)//D+1, (h-even_base)//D+1
    U0 = I-(A-odd_base)//D
    U1 = J-(B-even_base)//D
    assert (A-odd_base) % D == (B-even_base) % D == 0
    assert 2*n1 <= min(U0, U1)
    assert max(U0, U1) <= side-3*n1
    assert U0 <= I and I+n <= U0+n0
    assert U1 <= J and J+n <= U1+n1
    R = (rank(side, I, J)//(n*n))*(n*n)
    corners = [(0,0), (n-1,0), (n-1,n-1), (0,n-1)]
    for i,j in corners:
        rr = rank(side, I+i, J+j)
        assert R <= rr < R+n*n
        assert point(side, rr) == (I+i, J+j)
    first, last = point(side, R), point(side, R+q)
    assert abs(first[0]-last[0])+abs(first[1]-last[1]) == n-1
    tests = []
    for c0,c1 in permutations(corners, 2):
        if abs(c0[0]-c1[0])+abs(c0[1]-c1[1]) != n-1:
            continue
        if c0[0] == c1[1]:
            odd_at, even_at, c = 0, 1, c0[0]
        else:
            assert c1[0] == c0[1]
            odd_at, even_at, c = 1, 0, c1[0]
        C = (S*(R+odd_at*q), A+D*c)
        V = (S*(R+even_at*q), B+D*c)
        middle = S*(2*R+q)//2
        lo, hi = A-q+D*c, B+q+D*c
        assert middle % S == S//2
        assert 1 < lo < hi < h
        assert A+D*c > h//2
        assert C[1] % 4 == 3 and V[1] % 4 == 0
        assert (C[0]-V[0])**2+(C[1]-V[1])**2 == (L0*q)**2
        assert ((L0*q)-(Y0*q))//2 == q
        assert (Y0+1)*q % D == 0
        K = (Y0+1)*q//D
        owner = (I+K+c, J-K+c)
        assert U0 <= owner[0] < U0+n0
        assert U1 <= owner[1] < U1+n1
        assert not (I <= owner[0] < I+n and J <= owner[1] < J+n)
        assert odd_base+D*(owner[0]-U0) == hi
        assert even_base+D*(owner[1]-U1) == lo
        owner_rank = rank(side, *owner)
        assert point(side, owner_rank) == owner
        assert not R <= owner_rank < R+n*n
        P,Q = (middle,lo), (middle,hi)
        E,F = (S*owner_rank,lo), (S*owner_rank,hi)
        tilted, axis = (C,P,V,Q), (E,P,Q,F)
        assert rectangle(tilted) and rectangle(axis)
        assert set(tilted) != set(axis)
        fixed_black = {C,V,E,F}
        for mask in range(4):
            black = fixed_black | ({P} if mask&1 else set()) | ({Q} if mask&2 else set())
            assert set(tilted)-black == set(axis)-black
        tests.append({"entry": c0, "exit": c1, "common_index": c,
                      "owner": owner, "owner_rank": owner_rank,
                      "common_rows": [lo,hi]})
    assert len(tests) == 8
    return {"n":n, "S":S, "row_step":D, "h":h, "q":q, "half_factor":q,
            "padded_side":side, "origin":[I,J], "offsets":[U0,U1],
            "block_start":R, "corner_patterns":tests}


def main():
    for n in (1,2,4,8,16):
        for r in range(n*n):
            assert rank(n, *point(n,r)) == r
    cases = [check(n,S) for S in (128,256,1024)
             for n in (2,4,16,64)]
    cases += [check(n,S,8) for S in (16384,32768) for n in (4,16,64)]
    result = {"status":"PASS", "cases":cases,
              "corner_patterns_checked":8*len(cases),
              "common_corner_colorings_checked":32*len(cases),
              "scope":"Protected square with adjacent-corner endpoints; no row-filter survival claim."}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="cases"}))


if __name__ == "__main__":
    main()

