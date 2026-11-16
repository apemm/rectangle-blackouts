"""Weighted M-core of G_B^o (owner outside block) and distinct gaps per core component.
Usage: py -B core_components.py B S M orient"""
import sys
from collections import defaultdict, Counter
import numpy as np
sys.argv_saved = list(sys.argv)
import gb_components as g

def build_rows(B, S, M, orient):
    xy = g.hilbert_array(B)
    if orient == "swap": xy = xy[:, ::-1].copy()
    x, y = xy[:, 0], xy[:, 1]; odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1; legs = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u: continue
            w = Y2 // u; X = (w - u) // 2; L = (w + u) // 2
            if X % S == 0 and X > 0: legs[X][Y] = (L, (L - Y) // 2)
    trip = {}
    N = B * B
    for X, ys in legs.items():
        q = X // S
        hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, (L, a) in ys.items(): hyp[Y] = L
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
    return trip, x, y

def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    trip, x, y = build_rows(B, S, M, orient)
    adj = defaultdict(list)
    for (r, s, dl), q in trip.items():
        adj[r].append((s, q)); adj[s].append((r, q))
    deg = {v: len(l) for v, l in adj.items()}
    alive = set(adj); stack = [v for v in alive if deg[v] < M]; removed = set()
    while stack:
        v = stack.pop()
        if v in removed: continue
        removed.add(v)
        for w, _ in adj[v]:
            if w not in removed:
                deg[w] -= 1
                if deg[w] < M: stack.append(w)
    core = alive - removed
    print(f"B={B} S={M and S} M={M} {orient}: constraints {len(trip)}, incident labels {len(alive)}, weighted {M}-core labels {len(core)}")
    if not core: return
    seen = set(); stats = []
    for v in core:
        if v in seen: continue
        comp = [v]; seen.add(v); gs = set(); k = 0; ne = 0
        while k < len(comp):
            u = comp[k]; k += 1
            for w, q in adj[u]:
                if w in core:
                    gs.add(q); ne += 1
                    if w not in seen: seen.add(w); comp.append(w)
        s = len(gs); k0 = sum(1 for q in gs if q % M == 0)
        stats.append((s, len(comp), ne // 2, k0, sorted(gs)))
    stats.sort(reverse=True)
    print(" core components", len(stats), "distinct-gap distribution", sorted(Counter(t[0] for t in stats).items()))
    for t in stats[:5]:
        print("  s", t[0], "labels", t[1], "edges", t[2], "k0", t[3], "gaps", t[4][:40], "..." if t[0] > 40 else "")
main()
