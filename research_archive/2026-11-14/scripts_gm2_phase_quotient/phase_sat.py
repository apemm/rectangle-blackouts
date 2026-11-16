"""Exact phase-quotient decision for a fixed partition of the weighted M-core of G_B^o.
Pieces: connected tau-admissible pieces grown by BFS (size capped at CAP), tau_P rational in A(P).
For each piece the phase circle is cut at the breakpoints k/M - tau_P p (p a crossing rank), so the
phase problem is a finite CSP; it is decided by SAT. Variant 'shift' allows only theta_P in {0,1/M,...}.
Any SAT model is turned into xi and re-checked against every core constraint.
Usage: py -B phase_sat.py B S M orient CAP"""
import sys
from fractions import Fraction as Fr
from collections import defaultdict
from pysat.solvers import Cadical153
from core_cert import build, core
from phase_greedy import intersect, digit


def main():
    B, S, M, orient, CAP = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], int(sys.argv[5])
    import os, json
    cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"core_{B}_{M}_{orient}.json")
    if os.path.exists(cache):
        cons = [(r, u, dl) for r, u, dl, q in json.load(open(cache))]
        K = {v for c in cons for v in c[:2]}
    else:
        trip = build(B, S, M, orient)
        K, comps = core(trip, M)
        cons = [(r, u, dl) for (r, u, dl), q in trip.items() if r in K and u in K]
    adj = defaultdict(list)
    for (r, u, dl) in cons:
        adj[r].append((u, dl)); adj[u].append((r, dl))
    piece = {}; pieces = []; taus = []
    for v0 in sorted(K):
        if v0 in piece: continue
        pid = len(pieces); P = [v0]; piece[v0] = pid; A = [(Fr(0), Fr(1))]; frontier = [v0]
        while frontier and len(P) < CAP:
            x = frontier.pop(0)
            for w, _ in adj[x]:
                if w in piece or len(P) >= CAP: continue
                A2 = A
                for z, dl in adj[w]:
                    if piece.get(z) == pid:
                        A2 = intersect(A2, abs(z - w), dl, M)
                        if not A2: break
                if A2:
                    A = A2; piece[w] = pid; P.append(w); frontier.append(w)
        a, b = max(A, key=lambda t: t[1] - t[0])
        pieces.append(P); taus.append((a + b) / 2)
    crossing = [(r, u, dl) for (r, u, dl) in cons if piece[r] != piece[u]]
    cr = defaultdict(set)
    for (r, u, dl) in crossing: cr[piece[r]].add(r); cr[piece[u]].add(u)
    print(f"CAP={CAP}: pieces {len(pieces)}, crossing constraints {len(crossing)} of {len(cons)}")
    for mode in ("shift", "phase"):
        cells = {}
        for p in range(len(pieces)):
            if mode == "shift":
                cells[p] = [Fr(j, M) for j in range(M)]
            else:
                bp = sorted({(Fr(k, M) - taus[p] * v) % 1 for v in cr[p] for k in range(M)}) or [Fr(0)]
                cells[p] = bp
        s = Cadical153(); nv = [0]
        def new():
            nv[0] += 1; return nv[0]
        xv = {v: [new() for _ in range(M)] for v in cr_all(cr)}
        for v, xs in xv.items():
            for i in range(M):
                for j in range(i + 1, M): s.add_clause([-xs[i], -xs[j]])
        cv = {}
        ncl = 0
        for p, cl in cells.items():
            vs = [new() for _ in cl]; cv[p] = vs; s.add_clause(vs)
            for c, th in zip(vs, cl):
                for v in cr[p]:
                    s.add_clause([-c, xv[v][digit(taus[p] * v + th, M)]]); ncl += 1
        for (r, u, dl) in crossing:
            for k in range(M):
                if 0 <= k + dl < M: s.add_clause([-xv[r][k], -xv[u][k + dl]])
        res = s.solve()
        msg = f"  {mode}: cells total {sum(len(c) for c in cells.values())}, SAT {res}"
        if res:
            mdl = set(l for l in s.get_model() if l > 0)
            theta = {p: next(th for c, th in zip(cv[p], cells[p]) if c in mdl) for p in cells}
            xi = {v: digit(taus[piece[v]] * v + theta[piece[v]], M) for v in K}
            bad = sum(1 for (r, u, dl) in cons if xi[u] - xi[r] == dl)
            msg += f", re-check violations {bad}"
        print(msg); s.delete()


def cr_all(cr):
    out = set()
    for v in cr.values(): out |= v
    return out


if __name__ == "__main__":
    main()
