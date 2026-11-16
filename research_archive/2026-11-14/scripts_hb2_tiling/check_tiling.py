"""Sanity checks for the multilevel tiling assembly (C4).
1. Recursion (2) of continuation_hilbert_placement.md: every aligned dyadic square of
   side 2^m is visited by one aligned rank block [beta*4^m, (beta+1)*4^m).
2. Level/tile partition: each (i,j) in the Q-square lies in exactly one tile
   (level k by |j-i|, square (p,q) of side Q/2^k with |p-q|<=1); count tiles.
3. Rank totals per level and the constant sums used in the width bound.
"""
import math

def hilbert(q):
    lst = [(0, 0)]
    s = 1
    while s < q:
        new = []
        new += [(y, x) for (x, y) in lst]
        new += [(x, y + s) for (x, y) in lst]
        new += [(x + s, y + s) for (x, y) in lst]
        new += [(2 * s - 1 - y, s - 1 - x) for (x, y) in lst]
        lst = new
        s *= 2
    return lst

for q in [2, 4, 8, 16, 32, 64]:
    lst = hilbert(q)
    assert len(set(lst)) == q * q
    rank = {c: r for r, c in enumerate(lst)}
    m = 1
    while m <= q:
        for P in range(0, q, m):
            for R in range(0, q, m):
                rs = sorted(rank[(P + a, R + b)] for a in range(m) for b in range(m))
                assert rs[0] % (m * m) == 0 and rs[-1] == rs[0] + m * m - 1, (q, m, P, R)
        m *= 2
    # locality (1)
    for r in range(q * q):
        for s2 in range(r + 1, min(q * q, r + 300)):
            (a, b), (c, d) = lst[r], lst[s2]
            assert max((a - c) ** 2, (b - d) ** 2) < 16 * (s2 - r)
print("aligned squares = aligned rank blocks, locality (1): OK up to q=64")

def tiles(Q, K):
    """Return dict tile -> list of labels; level k<K: Q2^-k-1 <= |j-i| < Q2^-k;
    level K: |j-i| < Q 2^-K. Tile side Q 2^-k."""
    T = {}
    for i in range(Q):
        for j in range(Q):
            d = abs(j - i)
            k = K
            for kk in range(K):
                if Q >> (kk + 1) <= d < Q >> kk:
                    k = kk
                    break
            l = Q >> k
            p, qq = i // l, j // l
            assert abs(p - qq) <= 1
            T.setdefault((k, p, qq), []).append((i, j))
    return T

for Q, K in [(64, 3), (128, 4), (256, 5), (512, 5)]:
    T = tiles(Q, K)
    assert sum(len(v) for v in T.values()) == Q * Q
    ntiles = len(T)
    bound = sum(3 * 2 ** k - 2 for k in range(K + 1))
    ranks = {}
    used = {}
    for (k, p, qq), v in T.items():
        ranks[k] = ranks.get(k, 0) + (Q >> k) ** 2
        used[k] = used.get(k, 0) + len(v)
    print(Q, K, "tiles", ntiles, "<= 3*2^(K+1)-3-2(K+1) =", bound,
          "rank/used per level", {k: round(ranks[k] / used[k], 2) for k in sorted(ranks)})
    assert ntiles <= bound

s18 = sum(3 * 2 ** -k * 2 ** math.ceil(math.log2(k + 1)) for k in range(200))
s24 = sum(3 * 2 ** -k * 2 * (k + 1) for k in range(200))
s4 = sum((k + 1) * 2 ** -k for k in range(200))
print("sum 3*2^-k*2^ceil(log2(k+1)) =", round(s18, 4), "(<=18);  sum 3*2^-k*2(k+1) =", round(s24, 4),
      "; sum (k+1)2^-k =", s4)
