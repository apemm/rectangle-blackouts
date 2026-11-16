"""Cross-checks: curve identity with the archive recursion, and a brute
full-scan constraint count (archive method) against the band method."""
import sys
import time
import numpy as np
from pgraph import d2xy, xy2d, build, pythagorean_rows


def hilbert_array(q):  # verbatim from archive hilbert_finite_choice_search.py
    xy = np.zeros((1, 2), dtype=np.int64)
    n = 1
    while n < q:
        block = n * n
        nxt = np.empty((4 * block, 2), dtype=np.int64)
        nxt[:block] = xy[:, ::-1]
        nxt[block:2 * block] = xy + (0, n)
        nxt[2 * block:3 * block] = xy + (n, n)
        nxt[3 * block:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * block:, 1] = n - 1 - xy[:, 0]
        xy = nxt
        n *= 2
    return xy


def brute(h, S, M):  # archive constraint loop, plus factor witnesses
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    out = set()
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            trip = pythagorean_rows(X, h)
            if not trip:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            fac = np.zeros(2 * h + 2, dtype=np.int64)
            for Y, L, a in trip:
                hyp[Y] = L; fac[Y] = a
            for row1, row2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                Y = np.abs(row2 - row1)
                L = hyp[Y]
                tot = row1 + row2
                hit = (L > 0) & (tot - L >= 2) & (tot + L <= 2 * h) & active[:-d] & active[d:]
                for r in np.nonzero(hit)[0]:
                    out.add((int(r), int(r) + d, delta, int(fac[Y[r]])))
    return out


if __name__ == "__main__":
    for q in (1, 2, 4, 8, 16, 64, 256, 1024):
        xy = hilbert_array(q)
        t = np.arange(q * q)
        x, y = d2xy(q, t)
        assert (x == xy[:, 0]).all() and (y == xy[:, 1]).all(), q
        assert (xy2d(q, x, y) == t).all(), q
    print("curve identity PASS through q=1024")
    for h, S, M in [(300, 32, 1), (513, 32, 2), (777, 32, 3), (1024, 32, 1),
                    (1024, 32, 3), (1500, 32, 2), (2048, 32, 3), (2048, 64, 2), (1100, 64, 3)]:
        t0 = time.time()
        b = brute(h, S, M)
        w = build(h, S, M)["witness"]
        mine = {tuple(map(int, row)) for row in w}
        assert mine == b, (h, S, M, len(mine), len(b))
        cons = {k[:3] for k in b}
        print(h, S, M, "witnesses", len(b), "constraints", len(cons), "PASS",
              round(time.time() - t0, 1), flush=True)
