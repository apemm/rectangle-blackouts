"""Full candidate components of the height-independent diagonal-block system G_B^o
(hilbert_p_height_independent_cores.md, Corollary A1), with distinct-gap statistics.
Usage: py -B gb_components.py B S M orient(id|swap)
Sanity / exact finite certificate tool only."""
import sys, math
from collections import defaultdict, Counter
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

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

def v2(n):
    if n == 0: return 10 ** 9
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c

def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    xy = hilbert_array(B)
    if orient == "swap": xy = xy[:, ::-1].copy()
    x, y = xy[:, 0], xy[:, 1]
    odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1
    # all P vectors with odd Y <= Ymax and S | X
    legs = defaultdict(dict)  # X -> {Y: (L, a)}
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u: continue
            w = Y2 // u
            X = (w - u) // 2; L = (w + u) // 2
            if X % S == 0 and X > 0:
                legs[X][Y] = (L, (L - Y) // 2)
    rows = []  # r, s, delta, q, a, Y, role, owner_inside
    N = B * B
    for X, ys in legs.items():
        q = X // S
        ds = {q // M, -(-q // M)} - {0}
        hyp = np.zeros(Ymax + 2, dtype=np.int64); fac = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, (L, a) in ys.items(): hyp[Y] = L; fac[Y] = a
        for d in ds:
            delta = q - M * d
            if abs(delta) > M - 1 or d >= N: continue
            for role, (r1, r2) in enumerate(((odd[:-d], even[d:]), (even[:-d], odd[d:]))):
                yy = np.abs(r2 - r1)
                ok = yy <= Ymax
                yc = np.where(ok, yy, 0)
                L = np.where(ok, hyp[yc], 0)
                idx = np.nonzero(L > 0)[0]
                if len(idx) == 0: continue
                Lh = L[idx]; s1 = r1[idx] + r2[idx]
                c1 = (s1 - Lh) // 2; c2 = (s1 + Lh) // 2   # completion rows (local)
                co = np.where(c1 % 2 == 1, c1, c2); ce = np.where(c1 % 2 == 1, c2, c1)
                ii = (co - 1) // 2; jj = (ce - 2) // 2
                inside = (co >= 1) & (ce >= 2) & (ii < B) & (jj < B)
                for k, rr in enumerate(idx.tolist()):
                    rows.append((rr, rr + d, delta, q, int(fac[yc[rr]]), int(yc[rr]), role, bool(inside[k])))
    print(f"B={B} S={S} M={M} orient={orient}: vectors(X) {len(legs)}, rows {len(rows)}")
    for label, keep in (("all (archive candidate def.)", lambda t: True), ("owner outside block (G_B^o)", lambda t: not t[7])):
        R = [t for t in rows if keep(t)]
        trip = {}
        for t in R: trip.setdefault((t[0], t[1], t[2]), t)
        E = list(trip.values())
        if not E:
            print(label, "empty"); continue
        a_ = np.array([t[0] for t in E]); b_ = np.array([t[1] for t in E])
        G = coo_matrix((np.ones(len(E)), (a_, b_)), shape=(N, N))
        nc, comp = connected_components(G, directed=False)
        cg = defaultdict(set); cf = defaultdict(set); cv = defaultdict(set); cT = defaultdict(list)
        for t in E:
            c = comp[t[0]]; cg[c].add(t[3]); cf[c].add(t[4]); cv[c].add(t[0]); cv[c].add(t[1])
        T = (y - x)
        gl = Counter(); cover = Counter(); mx = (0, None)
        ex = []
        for c, gs in cg.items():
            s = len(gs); k0 = sum(1 for g in gs if g % M == 0)
            gl[s] += 1
            t1 = (s == 1) or (k0 == 0) or (M > 2 * s - k0)
            # dyadic two-value rule (Theorem 2'): exists t with all D-rank-differences of one valuation alpha
            # and all t-binding N-slot rank differences of valuation > alpha
            t2 = False
            Dd = [g // M for g in gs if g % M == 0]
            if Dd and len({v2(d) for d in Dd}) == 1:
                al = v2(Dd[0])
                for tt in range(1, M):
                    E_t = []
                    for g in gs:
                        if g % M == 0: continue
                        d0, rho = divmod(g, M)
                        if rho == tt and d0 > 0: E_t.append(d0)
                        if rho == M - tt: E_t.append(d0 + 1)
                    if all(v2(e) > al for e in E_t): t2 = True; break
            if not Dd: t2 = True
            key = "T1" if t1 else ("T2'" if t2 else "uncovered")
            cover[key] += 1
            if not t1 and not t2: ex.append((s, len(cv[c]), sorted(gs)))
            if s > mx[0]: mx = (s, c)
        print(" ", label, ": constraints", len(E), "components", len(cg))
        print("    distinct gaps per component:", sorted(gl.items()))
        print("    coverage at this M:", dict(cover))
        c = mx[1]; Ts = [int(T[v]) for v in cv[c]]
        print("    max-gap component: gaps", sorted(cg[c]), "labels", len(cv[c]), "factors", sorted(cf[c]),
              "T-range", (min(Ts), max(Ts)))
        ex.sort(reverse=True)
        print("    uncovered examples (s, labels, gaps):", ex[:6])

if __name__ == "__main__":
    main()
