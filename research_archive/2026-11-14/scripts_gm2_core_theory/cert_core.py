"""Mod-M certified solvability of the weighted M-core of the block system G_B^o.

G_B^o: hilbert_p_height_independent_cores.md, Corollary A1 (owner outside the block).
A mod-M certified assignment y satisfies y_u - y_r != delta (mod M) on every constraint
(r, u, delta), r < u.  By Theorem R (this route) the shift-quotient theorem II.1, in any
form, produces only certified assignments, so certified UNSAT of a subsystem kills it.

Usage: py -B cert_core.py B S M orient(id|swap)
Exact finite certificate on one fixed system; not a census.
"""
import sys
from collections import defaultdict
import numpy as np
from pysat.solvers import Cadical153


def hilbert_array(q):
    # recursion (2): quadrants (y,x), (x,y+n), (x+n,y+n), (2n-1-y, n-1-x)
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


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1].copy()
    x, y = xy[:, 0], xy[:, 1]
    odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1
    legs = defaultdict(dict)  # X -> {Y: L}
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u:
                continue
            w = Y2 // u
            X, L = (w - u) // 2, (w + u) // 2
            if X > 0 and X % S == 0:
                legs[X][Y] = L
    trip = {}  # (r, u, delta) -> q
    N = B * B
    for X, ys in legs.items():
        q = X // S
        hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, L in ys.items():
            hyp[Y] = L
        for d in {q // M, -(-q // M)} - {0}:
            delta = q - M * d
            if abs(delta) > M - 1 or d >= N:
                continue
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                yy = np.abs(r2 - r1)
                ok = yy <= Ymax
                yc = np.where(ok, yy, 0)
                L = np.where(ok, hyp[yc], 0)
                idx = np.nonzero(L > 0)[0]
                if not len(idx):
                    continue
                Lh = L[idx]
                s1 = r1[idx] + r2[idx]
                c1, c2 = (s1 - Lh) // 2, (s1 + Lh) // 2
                co = np.where(c1 % 2 == 1, c1, c2)
                ce = np.where(c1 % 2 == 1, c2, c1)
                ins = (co >= 1) & (ce >= 2) & ((co - 1) // 2 < B) & ((ce - 2) // 2 < B)
                for rr in idx[~ins].tolist():
                    trip[(rr, rr + d, delta)] = q
    return trip, x, y


def peel(keys, M, weight_key):
    """Peel labels with fewer than M distinct weight_key-classes to alive labels."""
    inc = defaultdict(set)
    for (r, u, dl) in keys:
        inc[r].add(weight_key(r, u, dl, side=0))
        inc[u].add(weight_key(r, u, dl, side=1))
    # class -> other endpoint, for decrementing
    alive = set(inc)
    cls_nb = {}
    for (r, u, dl) in keys:
        cls_nb.setdefault((r, weight_key(r, u, dl, side=0)), u)
        cls_nb.setdefault((u, weight_key(r, u, dl, side=1)), r)
    nbr_classes = defaultdict(lambda: defaultdict(set))  # v -> w -> set of classes at v pointing to w
    for (r, u, dl) in keys:
        nbr_classes[r][u].add(weight_key(r, u, dl, side=0))
        nbr_classes[u][r].add(weight_key(r, u, dl, side=1))
    deg = {v: len(inc[v]) for v in alive}
    stack = [v for v in alive if deg[v] < M]
    removed = set()
    while stack:
        v = stack.pop()
        if v in removed:
            continue
        removed.add(v)
        for w, cl in nbr_classes[v].items():
            if w in removed:
                continue
            deg[w] -= len(nbr_classes[w][v])
            if deg[w] < M:
                stack.append(w)
    return alive - removed


def solve(keys, M, certified):
    verts = sorted({r for (r, u, d) in keys} | {u for (r, u, d) in keys})
    idx = {v: k for k, v in enumerate(verts)}
    var = lambda v, c: idx[v] * M + c + 1
    s = Cadical153()
    for v in verts:
        s.add_clause([var(v, c) for c in range(M)])
        for c in range(M):
            for c2 in range(c + 1, M):
                s.add_clause([-var(v, c), -var(v, c2)])
    for (r, u, d) in keys:
        for c in range(M):
            if certified:
                s.add_clause([-var(r, c), -var(u, (c + d) % M)])
            elif 0 <= c + d < M:
                s.add_clause([-var(r, c), -var(u, c + d)])
    ok = s.solve()
    if not ok:
        return False, None
    model = set(z for z in s.get_model() if z > 0)
    val = {v: next(c for c in range(M) if var(v, c) in model) for v in verts}
    for (r, u, d) in keys:
        if certified:
            assert (val[u] - val[r] - d) % M != 0
        else:
            assert val[u] - val[r] != d
    return True, val


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    trip, x, y = build(B, S, M, orient)
    keys = list(trip)
    print(f"B={B} S={S} M={M} {orient}: constraints {len(keys)}")
    # integer weighted M-core: classes are distinct triples
    K = peel(keys, M, lambda r, u, dl, side: (u, dl) if side == 0 else (r, dl))
    EK = [k for k in keys if k[0] in K and k[1] in K]
    print(f" integer {M}-core: labels {len(K)}, constraints {len(EK)}")
    # certified core inside K: classes are (neighbour, residue of y_other - y_self forbidden)
    Kc = peel(EK, M, lambda r, u, dl, side: (u, dl % M) if side == 0 else (r, (-dl) % M))
    EKc = [k for k in EK if k[0] in Kc and k[1] in Kc]
    print(f" certified {M}-core of K: labels {len(Kc)}, constraints {len(EKc)}")
    if EK:
        ok, _ = solve(EK, M, certified=False)
        print("  integer problem on K:", "SAT (model verified)" if ok else "UNSAT")
        ok, _ = solve(EK, M, certified=True)
        print("  certified problem on K:", "SAT (model verified)" if ok else "UNSAT")
    if EKc:
        ok, _ = solve(EKc, M, certified=True)
        print("  certified problem on Kc:", "SAT (model verified)" if ok else "UNSAT")
        res = defaultdict(int)
        for (r, u, d) in EKc:
            res[d] += 1
        print("  delta distribution on Kc:", dict(sorted(res.items())))


if __name__ == "__main__":
    main()
