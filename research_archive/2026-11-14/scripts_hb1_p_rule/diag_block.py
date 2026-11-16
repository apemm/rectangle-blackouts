"""Candidate P system inside one main-diagonal Hilbert block of side B.

Main-diagonal aligned blocks have orientation id or swap, and their
row differences are local.  Constraints (r, r+d, delta) forbid
xi_{r+d} - xi_r = delta.  Only constraints whose completion owner lies
outside the block are kept (so the owner is never at the midpoint).
Reports average weighted degree and weighted degeneracy.  Sanity tool.
"""
import sys
from collections import defaultdict
import numpy as np


def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64)
    n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt
        n *= 2
    return xy


def legs_by_X(Ymax, S):
    """X -> {Y: L} for odd Y<=Ymax, S|X, X^2+Y^2=L^2."""
    out = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                if X % S == 0:
                    out[X][Y] = (w + u) // 2
    return out


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1]
    i, j = xy[:, 0], xy[:, 1]
    odd, even = 2 * i + 1, 2 * j + 2
    n = B * B
    legs = legs_by_X(2 * B + 1, S)
    cons = set()
    for X, ys in legs.items():
        q = X // S
        for d in {q // M, -(-q // M)}:
            delta = q - M * d
            if d < 1 or d >= n or abs(delta) > M - 1:
                continue
            look = np.zeros(4 * B + 4, dtype=np.int64)
            for Y, L in ys.items():
                look[Y] = L
            for a_rows, b_rows in ((odd[d:], even[:-d]), (odd[:-d], even[d:])):
                # a_rows: odd row used, b_rows: even row used
                y = np.abs(b_rows - a_rows)
                L = look[y]
                s = a_rows + b_rows
                lo, hi = (s - L) // 2, (s + L) // 2
                # owner rows: one odd one even
                oddr = np.where(lo % 2 == 1, lo, hi)
                evr = np.where(lo % 2 == 1, hi, lo)
                oi, oj = (oddr - 1) // 2, (evr - 2) // 2
                inside = (oi >= 0) & (oi < B) & (oj >= 0) & (oj < B)
                ok = (L > 0) & ~inside
                for r in np.nonzero(ok)[0]:
                    cons.add((int(r), int(r) + d, delta))
    return n, cons


def degeneracy(n, cons):
    adj = defaultdict(list)
    for k, (a, b, _) in enumerate(cons):
        adj[a].append(k)
        adj[b].append(k)
    deg = {v: len(adj[v]) for v in adj}
    alive = set(cons)
    import heapq
    heap = [(dv, v) for v, dv in deg.items()]
    heapq.heapify(heap)
    removed = set()
    best = 0
    order = []
    cl = list(cons)
    while heap:
        dv, v = heapq.heappop(heap)
        if v in removed or dv != deg[v]:
            continue
        best = max(best, dv)
        removed.add(v)
        order.append((v, dv))
        for k in adj[v]:
            a, b, _ = cl[k]
            if cl[k] in alive:
                alive.discard(cl[k])
                w = b if a == v else a
                deg[w] -= 1
                heapq.heappush(heap, (deg[w], w))
    return best, order


if __name__ == "__main__":
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    n, cons = build(B, S, M, orient)
    inc = len({a for a, _, _ in cons} | {b for _, b, _ in cons})
    best, order = degeneracy(n, cons)
    print(f"B={B} S={S} M={M} {orient}: labels={n} constraints={len(cons)} "
          f"avgdeg={2*len(cons)/n:.4f} incident={inc} weighted_degeneracy={best}")
