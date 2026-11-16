"""Sanity test of the phase-quotient theorem on the weighted M-core of G_B^o.
1. Residue statistics per core component: number of rank differences d whose slot residues
   R_d = {delta mod M} have size 1, 2, 3.
2. Partition each core component into connected tau-admissible pieces (BFS growth, keep A(slots) != empty).
3. Each piece gets a rational tau_P in A(P).  Pieces are ordered by reverse quotient peeling; each piece
   gets a phase theta_P chosen from the exact free set (complement of the forbidden arcs
   I_f - tau_P p of Theorem 4(d)), all in exact rational arithmetic.
4. The resulting xi_r = floor(M {tau_P r + theta_P}) is checked against every constraint of the core.
Usage: py -B phase_greedy.py B S M orient"""
import sys
from fractions import Fraction as Fr
from collections import defaultdict, Counter
from core_cert import build, core, admissible


def digit(y, M):
    return int((y - (y // 1)) * M // 1)


def intersect(A, d, dl, M):
    new = []
    for a, b in A:
        lo = int((a * d - Fr(dl + 1, M)) // 1) - 1
        hi = int((b * d - Fr(dl + 1, M)) // 1) + 1
        for n in range(lo, hi + 1):
            L = (n + Fr(dl + 1, M)) / d; R = (n + 1 + Fr(dl - 1, M)) / d
            l2, r2 = max(a, L), min(b, R)
            if l2 <= r2: new.append((l2, r2))
    return new


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    trip = build(B, S, M, orient)
    K, comps = core(trip, M)
    cons = [(r, u, dl, q) for (r, u, dl), q in trip.items() if r in K and u in K]
    adj = defaultdict(list)
    for (r, u, dl, q) in cons:
        adj[r].append((u, dl)); adj[u].append((r, dl))
    # 1. residue statistics
    for comp in sorted(comps, key=len, reverse=True):
        cs = set(comp); Rd = defaultdict(set)
        for (r, u, dl, q) in cons:
            if r in cs: Rd[u - r].add(dl % M)
        h = Counter(len(v) for v in Rd.values())
        full = sorted(d for d, v in Rd.items() if len(v) == M)
        print(f"comp {len(comp)}: rank differences {len(Rd)}, |R_d| histogram {sorted(h.items())}, full-residue d (first 10) {full[:10]}")
    # 2. pieces
    piece = {}; pieces = []; taus = []
    for v0 in sorted(K):
        if v0 in piece: continue
        pid = len(pieces); P = [v0]; piece[v0] = pid; A = [(Fr(0), Fr(1))]
        frontier = [v0]
        while frontier:
            x = frontier.pop()
            for w, _ in adj[x]:
                if w in piece: continue
                A2 = A
                for z, dl in adj[w]:
                    if piece.get(z) == pid:
                        A2 = intersect(A2, abs(z - w), dl, M)
                        if not A2: break
                if A2:
                    A = A2; piece[w] = pid; P.append(w); frontier.append(w)
        a, b = max(A, key=lambda t: t[1] - t[0])
        pieces.append(P); taus.append((a + b) / 2)
    sz = Counter(len(P) for P in pieces)
    print(f"pieces {len(pieces)}; size histogram (largest 8) {sorted(sz.items())[-8:]}; singletons {sz.get(1, 0)}")
    # quotient: crossing edges between pieces
    cross = defaultdict(list)
    for (r, u, dl, q) in cons:
        if piece[r] != piece[u]:
            cross[piece[r]].append((r, u, dl)); cross[piece[u]].append((r, u, dl))
    deg = {p: len(cross[p]) for p in range(len(pieces))}
    nb = defaultdict(Counter)
    for p, es in cross.items():
        for (r, u, dl) in es:
            o = piece[u] if piece[r] == p else piece[r]; nb[p][o] += 1
    # reverse peeling order on the quotient (by remaining crossing-edge count)
    alive = set(range(len(pieces))); order = []; cnt = dict(deg)
    import heapq
    hp = [(cnt[p], p) for p in alive]; heapq.heapify(hp)
    while hp:
        c, p = heapq.heappop(hp)
        if p not in alive or c != cnt[p]: continue
        alive.discard(p); order.append(p)
        for o, m in nb[p].items():
            if o in alive:
                cnt[o] -= m; heapq.heappush(hp, (cnt[o], o))
    order.reverse()
    maxdeg = 0
    theta = {}; fails = 0; maxarcs = 0; over = 0
    for p in order:
        tP = taus[p]; lefts = set()
        for (r, u, dl) in cross[p]:
            if piece[r] == p:  # r in P (lower rank), u in earlier piece Q? only if assigned
                Q = piece[u]
                if Q not in theta: continue
                f = digit(taus[Q] * u + theta[Q], M) - dl; pp = r
            else:
                Q = piece[r]
                if Q not in theta: continue
                f = digit(taus[Q] * r + theta[Q], M) + dl; pp = u
            if 0 <= f < M:
                lefts.add((Fr(f, M) - tP * pp) % 1)
        maxarcs = max(maxarcs, len(lefts))
        if len(lefts) >= M: over += 1
        if not lefts:
            theta[p] = Fr(0); continue
        L = sorted(lefts); best = None
        for i, a in enumerate(L):
            nxt = L[(i + 1) % len(L)] + (1 if i + 1 == len(L) else 0)
            g = nxt - a
            if g > Fr(1, M) and (best is None or g > best[0]): best = (g, a)
        if best is None:
            fails += 1; theta[p] = Fr(0)
        else:
            g, a = best; theta[p] = (a + Fr(1, M) + (g - Fr(1, M)) / 2) % 1
    print(f"phase greedy: pieces with >= M distinct arcs {over}, max distinct arcs {maxarcs}, pieces with no free phase {fails}")
    xi = {}
    for v in K:
        p = piece[v]; xi[v] = digit(taus[p] * v + theta[p], M)
    bad = sum(1 for (r, u, dl, q) in cons if xi[u] - xi[r] == dl)
    badint = sum(1 for (r, u, dl, q) in cons if piece[r] == piece[u] and xi[u] - xi[r] == dl)
    print(f"final check: violated constraints {bad} of {len(cons)} (internal {badint})")


if __name__ == "__main__":
    main()
