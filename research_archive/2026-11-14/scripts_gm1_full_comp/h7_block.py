"""H7 analog of G_B: one main-diagonal Hilbert block of side B in index space, rows a = 17 + 28 x,
b = BRES + 28 y (local), S = 6272, all local P candidates (no owner filter, no strip test).
Reports full components and distinct gaps.  Usage: py -B h7_block.py B BRES M"""
import sys, math
from collections import defaultdict, Counter
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from gb_components import hilbert_array

def factor(n):
    f = {}; p = 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def main():
    B, BRES, M = map(int, sys.argv[1:4]); S = 6272; D = 28; c = BRES - 17
    xy = hilbert_array(B); x, y = xy[:, 0], xy[:, 1]
    A = 17 + D * x; Bv = BRES + D * y
    Ymax = abs(c) + D * B
    legs = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        if (Y - c) % D and (-Y - c) % D: continue      # need c + D U = +-Y
        ds = [1]
        for p, e in factor(Y).items(): ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
        Y2 = Y * Y
        for u in ds:
            if u >= Y: continue
            w = Y2 // u; X = (w - u) // 2
            if X > 0 and X % S == 0: legs[X][Y] = (w + u) // 2
    N = B * B; trip = {}
    for X, ys in legs.items():
        q = X // S; hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, L in ys.items(): hyp[Y] = L
        for d in {q // M, -(-q // M)} - {0}:
            dl = q - M * d
            if abs(dl) > M - 1 or d >= N: continue
            for r1, r2 in ((A[:-d], Bv[d:]), (Bv[:-d], A[d:])):
                yy = np.abs(r2 - r1); ok = yy <= Ymax; yc = np.where(ok, yy, 0)
                idx = np.nonzero(np.where(ok, hyp[yc], 0) > 0)[0]
                for rr in idx.tolist(): trip[(rr, rr + d, dl)] = q
    print(f"H7 block B={B} BRES={BRES} c={c} M={M}: vectors {len(legs)}, constraints {len(trip)}, "
          f"max L {max((L for ys in legs.values() for L in ys.values()), default=0)}")
    if not trip: return
    keys = list(trip); a = np.array([k[0] for k in keys]); b = np.array([k[1] for k in keys])
    nc, comp = connected_components(coo_matrix((np.ones(len(keys)), (a, b)), shape=(N, N)), directed=False)
    cg = defaultdict(set); cv = defaultdict(set)
    for k, q in trip.items(): cg[comp[k[0]]].add(q); cv[comp[k[0]]].update((k[0], k[1]))
    inc = len(set(a.tolist()) | set(b.tolist()))
    print("  incident labels", inc, "mean weighted incidence", round(2 * len(trip) / N, 5))
    print("  distinct gaps per component:", sorted(Counter(len(v) for v in cg.values()).items()))
    big = max(cg, key=lambda z: len(cg[z])); print("  max:", len(cg[big]), "gaps on", len(cv[big]), "labels")
main()
