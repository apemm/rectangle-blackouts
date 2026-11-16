"""Sparse, exact checks of the genuine Hilbert R2s domino obstruction.

No board-sized array or external research module is used. The forward
Hilbert decoder and recursive inverse are independent implementations.
"""
from itertools import product
from pathlib import Path
import json


def point(n, d):
    x = y = 0
    side = 1
    while side < n:
        rx = (d // 2) & 1
        ry = (d ^ rx) & 1
        if not ry:
            if rx:
                x, y = side - 1 - x, side - 1 - y
            x, y = y, x
        x += side * rx
        y += side * ry
        d //= 4
        side *= 2
    assert d == 0
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
            and tuple(a[i]+c[i] for i in (0, 1))
            == tuple(b[i]+d[i] for i in (0, 1))
            and sum((a[i]-c[i])**2 for i in (0, 1))
            == sum((b[i]-d[i])**2 for i in (0, 1)))


def check(n, S):
    depth = n.bit_length()-1
    assert n == 1 << depth and depth >= 3 and depth % 2 == 1
    assert S % 4 == 0
    R = n*n//4+6
    local = [(0, 0), (0, 1), (1, n//2+3), (1, n//2+2)]
    rr = [0, 1, R, R+1]
    assert [point(n, r) for r in rr] == local
    assert R % 2 == 0
    q = S*R//4
    y = q**3+q*q-1
    U = q*q+2*q+2
    h = 2*y-8
    k = (y-3)//4
    n0, n1 = k-1, 2*k
    assert y == 4*k+3 and y % 4 == 3 and q % 2 == 0
    assert n0 >= n and k >= n
    assert 2*y > h+1 and 2*(y-4) <= h+1
    assert y+4*(n0-1) <= h < y+4*n0
    assert 2+4*(n1-1) == h

    N = 4*n
    zeros = 0
    while N < 16*h:
        N *= 4
        zeros += 2
    I, J = N//4, 3*N//4
    start = 3*N*N//8
    U0, U1 = I, J-k
    assert point(N, start) == (I, J)
    assert rank(N, I, J) == start
    assert 0 <= U0 < U0+n0 < N and 0 <= U1 < U1+n1 < N
    for r, (i, j) in zip(rr, local):
        cell = (I+i, J+j)
        assert point(N, start+r) == cell
        assert rank(N, *cell) == start+r
        assert U0 <= cell[0] < U0+n0 and U1 <= cell[1] < U1+n1

    x0 = S*start
    A, B = (x0, y), (x0+U, 1)
    C, D = (x0+4*q, y+4), (x0+U-4, 1)
    P, Q = (x0+2*q-2, y+2), (x0+q*q+4*q, 3)
    assert rectangle((A, B, Q, P)) and rectangle((C, P, D, Q))
    assert len({A, B, C, D, P, Q}) == 6
    assert all(0 <= p[0] < S*N*N and 1 <= p[1] <= h
               for p in (A, B, C, D, P, Q))
    assert B[0] % 4 == D[0] % 4 == P[0] % 4 == 2
    assert Q[0] % 4 == 0 and Q[1] < y
    assert 16 <= 2*(C[0]-A[0])
    assert (q-1)*U == y-1
    T, delta, V, m = 4*(q-1), 4, U-4*q-4, 1-y
    assert T*U == -m*delta
    assert V*V-U*U == delta*(2*m-delta)

    swap_checks = color_checks = 0
    for swap0, swap1 in product((0, 1), repeat=2):
        labels = []
        for z, swap in ((0, swap0), (2, swap1)):
            for e in (0, 1):
                i, j = local[z+(e ^ swap)]
                labels.append((y+4*i, y-1+4*j))
        assert len(set(labels)) == 4
        assert A[1] in labels[0] and C[1] in labels[2]
        assert all(1 <= a <= h and 1 <= b <= h for a, b in labels)
        assert all(a % 4 == 3 and b % 4 == 2 for a, b in labels)
        swap_checks += 1
        # Symmetric-difference black support is robust even if either
        # common corner later becomes black. The stated board has both white.
        for mask in range(4):
            black = {A, B, C, D}
            if mask & 1:
                black.add(P)
            if mask & 2:
                black.add(Q)
            assert set((A, B, Q, P))-black == set((C, P, D, Q))-black
            color_checks += 1

    return dict(n=n, stride=S, q=q, y=y, height=h, padded_side=N,
                profile_labels=n0*n1, global_start=start,
                address_zero_digits=zeros, swap_checks=swap_checks,
                common_color_checks=color_checks)


def main():
    cases = [check(n, S) for n in (8, 32, 128, 512, 2048)
             for S in (6272, 12544, 25088)]
    result = dict(status="PASS", cases=cases,
                  swap_checks=sum(c["swap_checks"] for c in cases),
                  common_color_checks=sum(c["common_color_checks"] for c in cases),
                  scope="Sparse exact identities, profile embedding, all protected swaps; no full-board validity claim.")
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "cases"}))


if __name__ == "__main__":
    main()
