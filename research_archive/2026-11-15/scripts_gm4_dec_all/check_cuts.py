"""Sanity check of the corner-cut theorem on the full cand block system G_1024^o.
For every main-diagonal Hilbert block P of side 2m (m = 1..512) of the 1024 curve, the unique
cell of O4(P) with |T| = 1 should be a cut: no cand triple (r, u) with r < rank(cell) <= u or
r <= rank(cell) < u.  Also lists which |T| = 1 cells are cuts in general.
Usage: py -B check_cuts.py orient"""
import sys, time
import numpy as np
from common import hilbert_array, legs, window_triples

o = sys.argv[1]
B = 1024
t0 = time.time()
xy = hilbert_array(B).astype(np.int64)
if o == "swap":
    xy = xy[:, ::-1].copy()
odd = 2 * xy[:, 0] + 1; even = 2 * xy[:, 1] + 2
E = window_triples(odd, even, 0, B * B, legs(2 * B - 1))
print(f"{o}: cand G_{B} triples {len(E)}  ({time.time()-t0:.1f}s)")
n = B * B
# coverage of position p by triples with r < p < u, and incidence of p
cov = np.zeros(n + 1, dtype=np.int64)
np.add.at(cov, E[:, 0] + 1, 1); np.add.at(cov, E[:, 1], -1)
cov = np.cumsum(cov)[:n]
inc = np.bincount(E[:, 0], minlength=n) + np.bincount(E[:, 1], minlength=n)
rank = np.empty((B, B), dtype=np.int64); rank[xy[:, 0], xy[:, 1]] = np.arange(n)
T = xy[:, 1] - xy[:, 0]
# enumerate diagonal blocks P = [a, a+2m)^2 aligned; O4(P) = block of P's last quarter
bad, tot = 0, 0
m = 1
while 2 * m <= B:
    for a in range(0, B, 2 * m):
        r0 = rank[a, a]                      # a diagonal block starts at its corner cell (a,a)
        assert r0 % (4 * m * m) == 0
        last = xy[r0 + 3 * m * m: r0 + 4 * m * m]   # O4(P): last quarter
        cells = [(x, y) for (x, y) in [(a + m, a + m - 1), (a + m - 1, a + m)]]
        c = [rank[x, y] for x, y in cells if r0 + 3 * m * m <= rank[x, y] < r0 + 4 * m * m]
        assert len(c) == 1
        p = c[0]; tot += 1
        if cov[p] != 0 or inc[p] != 0:
            bad += 1
    m *= 2
print(f"O4 corner cells checked {tot}; not a cut: {bad}")
t1 = np.abs(T) == 1
print(f"|T|=1 cells {int(t1.sum())}; of them cuts with no incidence {int((t1 & (cov == 0) & (inc == 0)).sum())}")
print(f"all rank positions that are cuts (cov 0): {int((cov == 0).sum())}; |T| of the cut cells with |T|>1: "
      f"{np.unique(np.abs(T[(cov == 0) & ~t1 & (T != 0)]))[:20]}")
print(f"done ({time.time()-t0:.1f}s)")
