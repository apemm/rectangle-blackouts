"""Exact finite checks on the weighted M-core of the block system G_B^o (owner outside block).
Builder re-implemented from the definition in hilbert_p_height_independent_cores.md / gap_mixing_full_components.md.
For each core component C:
  (1) slot set Gamma_C = {(d, delta)} and the exact set A(Gamma_C) of tau in [0,1) with
      ||tau d - delta/M|| >= 1/M for all slots (Lemma C, phase free), by exact Fraction intersection;
  (2) SAT: plain solvability (xi_u - xi_r != delta as integers);
  (3) SAT: mod-M certified solvability (xi_u - xi_r != q mod M).
Usage: py -B core_cert.py B S M orient [maxcomp]"""
import sys
from fractions import Fraction as Fr
from collections import defaultdict
import numpy as np
from pysat.solvers import Cadical153


def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64); n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt; n *= 2
    return xy


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap": xy = xy[:, ::-1].copy()
    x, y = xy[:, 0], xy[:, 1]; odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1; legs = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u: continue
            w = Y2 // u; X = (w - u) // 2; L = (w + u) // 2
            if X % S == 0 and X > 0: legs[X][Y] = L
    trip = {}
    N = B * B
    for X, ys in legs.items():
        q = X // S
        hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, L in ys.items(): hyp[Y] = L
        for d in {q // M, -(-q // M)} - {0}:
            delta = q - M * d
            if abs(delta) > M - 1 or d >= N: continue
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                yy = np.abs(r2 - r1); ok = yy <= Ymax
                yc = np.where(ok, yy, 0); L = np.where(ok, hyp[yc], 0)
                idx = np.nonzero(L > 0)[0]
                if not len(idx): continue
                Lh = L[idx]; s1 = r1[idx] + r2[idx]
                c1 = (s1 - Lh) // 2; c2 = (s1 + Lh) // 2
                co = np.where(c1 % 2 == 1, c1, c2); ce = np.where(c1 % 2 == 1, c2, c1)
                ins = (co >= 1) & (ce >= 2) & ((co - 1) // 2 < B) & ((ce - 2) // 2 < B)
                for rr in idx[~ins].tolist():
                    trip[(rr, rr + d, delta)] = q
    return trip


def core(trip, M):
    adj = defaultdict(list)
    for (r, s, dl), q in trip.items():
        adj[r].append(s); adj[s].append(r)
    deg = {v: len(l) for v, l in adj.items()}
    removed = set(); stack = [v for v in adj if deg[v] < M]
    while stack:
        v = stack.pop()
        if v in removed: continue
        removed.add(v)
        for w in adj[v]:
            if w not in removed:
                deg[w] -= 1
                if deg[w] < M: stack.append(w)
    K = set(adj) - removed
    comps = []; seen = set()
    for v in K:
        if v in seen: continue
        comp = [v]; seen.add(v); k = 0
        while k < len(comp):
            u = comp[k]; k += 1
            for w in adj[u]:
                if w in K and w not in seen: seen.add(w); comp.append(w)
        comps.append(comp)
    return K, comps


def admissible(slots, M):
    """Exact set of tau in [0,1] with ||d tau - delta/M|| >= 1/M for all (d, delta): list of closed intervals."""
    cur = [(Fr(0), Fr(1))]
    for d, dl in sorted(slots):
        # allowed for this slot: d tau in [n + (dl+1)/M, n + 1 + (dl-1)/M]
        new = []
        for a, b in cur:
            lo = int((a * d - Fr(dl + 1, M)) // 1) - 1
            hi = int((b * d - Fr(dl + 1, M)) // 1) + 1
            for n in range(lo, hi + 1):
                L = (n + Fr(dl + 1, M)) / d; R = (n + 1 + Fr(dl - 1, M)) / d
                l2, r2 = max(a, L), min(b, R)
                if l2 <= r2: new.append((l2, r2))
        cur = new
        if not cur: return []
    return cur


def sat(cons, verts, M, certified):
    idx = {v: i for i, v in enumerate(verts)}
    var = lambda v, k: idx[v] * M + k + 1
    s = Cadical153()
    for v in verts:
        s.add_clause([var(v, k) for k in range(M)])
        for k in range(M):
            for l in range(k + 1, M): s.add_clause([-var(v, k), -var(v, l)])
    for (r, u, dl, q) in cons:
        for k in range(M):
            if certified:
                s.add_clause([-var(r, k), -var(u, (k + q) % M)])
            elif 0 <= k + dl < M:
                s.add_clause([-var(r, k), -var(u, k + dl)])
    res = s.solve(); model = s.get_model() if res else None; s.delete()
    return res, model


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    maxc = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    trip = build(B, S, M, orient)
    K, comps = core(trip, M)
    ncons = sum(1 for (r, u, dl) in trip if r in K and u in K)
    print(f"B={B} S={S} M={M} {orient}: constraints {len(trip)}, core labels {len(K)}, core constraints {ncons}, comps {len(comps)}")
    comps.sort(key=len, reverse=True)
    for comp in comps[:maxc]:
        cs = set(comp)
        cons = [(r, u, dl, q) for (r, u, dl), q in trip.items() if r in cs and u in cs]
        slots = {(u - r, dl) for (r, u, dl, q) in cons}
        gaps = {q for *_, q in cons}
        A = admissible(slots, M)
        meas = sum(b - a for a, b in A)
        p, _ = sat(cons, comp, M, False)
        c, _ = sat(cons, comp, M, True)
        print(f" comp labels {len(comp)} cons {len(cons)} gaps {len(gaps)} slots {len(slots)} "
              f"| A(Gamma): {len(A)} pieces, measure {float(meas):.3g} | plain SAT {p} | certified SAT {c}")
        if A: print("   first admissible pieces:", [(str(a), str(b)) for a, b in A[:3]])


if __name__ == "__main__":
    main()
