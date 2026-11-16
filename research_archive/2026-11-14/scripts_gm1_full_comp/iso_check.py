"""(1) Window-graph adjacency of the near-isosceles chain Y = S n +- 1 (pure arithmetic).
(2) Near-isosceles gaps inside the max-gap genuine component of G_B^o; 2-gap components with
one gap divisible by M (Theorem 2 setting) and their coverage.  Usage: py -B iso_check.py B S M"""
import sys, math
from collections import defaultdict, Counter
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from gb_components import hilbert_array, v2

def isqrt_lt(d):  # windows |T-U| < 4 sqrt(d): largest integer k with k^2 < 16 d
    k = math.isqrt(16 * d - 1)
    return k

def arithmetic_chain(S, M, nmax):
    bad = []
    seq = []
    for n in range(1, nmax + 1):
        for sg in (-1, 1):
            Y = S * n + sg; q = n * (S * n // 2 + sg); U = (Y - 1) // 2
            assert (S * q) ** 2 + Y * Y == ((Y * Y + 1) // 2) ** 2
            ds = sorted({q // M, -(-q // M)} - {0})
            seq.append((U, max(isqrt_lt(d) for d in ds), q))
    for (U1, w1, q1), (U2, w2, q2) in zip(seq, seq[1:]):
        # common integer T with |T-U1|<=w1 and |T-U2|<=w2 (w = largest integer offset allowed)
        if U2 - U1 > w1 + w2: bad.append((q1, q2))
    return seq, bad

def build(B, S, M):
    xy = hilbert_array(B); x, y = xy[:, 0], xy[:, 1]; odd, even = 2 * x + 1, 2 * y + 2
    Ymax = 2 * B - 1; legs = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u: continue
            w = Y2 // u; X = (w - u) // 2; L = (w + u) // 2
            if X % S == 0 and X > 0: legs[X][Y] = L
    trip = {}; N = B * B
    for X, ys in legs.items():
        q = X // S; hyp = np.zeros(Ymax + 2, dtype=np.int64)
        for Y, L in ys.items(): hyp[Y] = L
        for d in {q // M, -(-q // M)} - {0}:
            delta = q - M * d
            if abs(delta) > M - 1 or d >= N: continue
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                yy = np.abs(r2 - r1); ok = yy <= Ymax; yc = np.where(ok, yy, 0); L = np.where(ok, hyp[yc], 0)
                idx = np.nonzero(L > 0)[0]
                if not len(idx): continue
                Lh = L[idx]; s1 = r1[idx] + r2[idx]; c1 = (s1 - Lh) // 2; c2 = (s1 + Lh) // 2
                co = np.where(c1 % 2 == 1, c1, c2); ce = np.where(c1 % 2 == 1, c2, c1)
                ins = (co >= 1) & (ce >= 2) & ((co - 1) // 2 < B) & ((ce - 2) // 2 < B)
                for rr in idx[~ins].tolist(): trip[(rr, rr + d, delta)] = q
    return trip, N

def main():
    B, S, M = map(int, sys.argv[1:4])
    seq, bad = arithmetic_chain(S, M, 400)
    print("arithmetic chain n<=400: non-adjacent consecutive pairs:", bad[:10], "count", len(bad))
    trip, N = build(B, S, M)
    keys = list(trip)
    a = np.array([k[0] for k in keys]); b = np.array([k[1] for k in keys])
    nc, comp = connected_components(coo_matrix((np.ones(len(keys)), (a, b)), shape=(N, N)), directed=False)
    cg = defaultdict(set)
    for k, q in trip.items(): cg[comp[k[0]]].add(q)
    big = max(cg, key=lambda c: len(cg[c]))
    iso = [q for (U, w, q) in seq if 2 * U + 1 <= 2 * B - 1]
    allq = set(trip.values())
    print(f"B={B}: near-isosceles gaps with Y<2B: {len(iso)}; present in system: {sum(q in allq for q in iso)};"
          f" in max-gap component: {sum(q in cg[big] for q in iso)}; max comp gaps {len(cg[big])} of {len(allq)} gaps in system")
    missing = [q for q in iso if q not in cg[big]]
    print("  near-isosceles gaps not in max component:", missing[:20])
    # two-gap components with exactly one gap divisible by M (M = 3 setting of Theorem 2)
    cnt = Counter(); ex = []
    for c, gs in cg.items():
        if len(gs) != 2: continue
        k0 = sum(1 for q in gs if q % M == 0)
        if M != 3 or k0 != 1: cnt["2 gaps, k0=%d" % k0] += 1; continue
        q0 = [q for q in gs if q % 3 == 0][0]; q1 = [q for q in gs if q % 3][0]
        aa, bb = q0 // 3, q1 // 3
        cov = v2(bb) > v2(aa) or v2(bb + 1) > v2(aa)
        cnt["2 gaps, k0=1, Thm2 " + ("covered" if cov else "UNCOVERED")] += 1
        if not cov: ex.append((q0, q1))
    print("  two-gap full components:", dict(cnt))
    print("  uncovered (q0=3a, q1) pairs:", sorted(Counter(ex).items())[:30])
main()
