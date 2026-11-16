"""Local P system of one main-diagonal block of side B (local rows odd 2x+1, even 2y+2),
for the Hilbert order and for Model K random orders of each start type.  A constraint
(r, r+d, delta) is kept when a cross-parity pair has X = S(Md+delta), X^2+Y^2 = L^2, and the
owner of the completion rows lies outside the block (Corollary A1 of
hilbert_p_height_independent_cores.md).  Vectors are enumerated with the T1 normal form."""
import sys, math, time, random
import numpy as np
import randcurve as R
from bandcore import core_numbers

def vectors(S, Ymax):
    out = {}  # X -> {Y: L}
    emax = 2 * Ymax // S + 2
    for ep in range(1, emax + 1):
        E = S * ep // 2
        for O in range(1, E + Ymax + 2, 2):
            if math.gcd(ep, O) != 1:
                continue
            base = abs(E * E - O * O)
            if base == 0 or base > Ymax:
                continue
            k = 1
            while k * base <= Ymax:
                X = S * k * ep * O; Y = k * base; L = k * (E * E + O * O)
                out.setdefault(X, {})[Y] = L
                k += 2
    return out

def block_system(xy, S, M):
    B = int(xy[:, 0].max()) + 1
    n = len(xy)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    V = vectors(S, 2 * B)
    rs, ss = [], []
    for X, ys in V.items():
        q = X // S
        for d in sorted({q // M, -(-q // M)}):
            if d <= 0 or d >= n:
                continue
            hyp = np.zeros(2 * B + 2, dtype=np.int64)
            for y, L in ys.items():
                hyp[y] = L
            hit = np.zeros(n - d, dtype=bool)
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                y = np.abs(r2 - r1)
                L = hyp[y]
                sm = r1 + r2
                c1 = (sm - L) // 2; c2 = (sm + L) // 2
                co = np.where(c1 % 2 == 1, c1, c2); ce = np.where(c1 % 2 == 1, c2, c1)
                oi = (co - 1) // 2; oj = (ce - 2) // 2
                inside = (oi >= 0) & (oi < B) & (oj >= 0) & (oj < B)
                hit |= (L > 0) & ~inside
            idx = np.nonzero(hit)[0]
            rs.append(idx); ss.append(idx + d)
    if not rs:
        return np.zeros(0, int), np.zeros(0, int)
    return np.concatenate(rs), np.concatenate(ss)

def rand_block(B, seed, en, ex):
    rng = random.Random(seed)
    P = {1: R.plans_for(1), 2: R.plans_for(2), 4: R.plans_for(4)}
    xs = np.empty(B * B, dtype=np.int64); ys = np.empty(B * B, dtype=np.int64)
    p = 0
    stack = [(0, 0, B, en, ex)]
    while stack:
        x0, y0, s, a, b = stack.pop()
        if s == 1:
            xs[p] = x0; ys[p] = y0; p += 1; continue
        half = s // 2
        order, cs = rng.choice(P[min(half, 4)][(a, b)])
        for t in (3, 2, 1, 0):
            c = order[t]
            stack.append((x0 + c[0] * half, y0 + c[1] * half, half, cs[t][0], cs[t][1]))
    return np.stack([xs, ys], axis=1)

if __name__ == "__main__":
    B, S, M, nsamp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    t0 = time.time()
    xy = R.hilbert_array(B)
    r, s = block_system(xy, S, M)
    deg, cn = core_numbers(r, s, B * B)
    print(f"hilbert B={B} S={S} M={M} E={len(r)} avgdeg={2*len(r)/B/B:.3f} degen={cn.max()} 3core={(cn>=3).sum()} t={time.time()-t0:.1f}")
    for t in range(nsamp):
        en, ex = [(0, 1), (0, 2), (0, 3), (1, 2)][t % 4]
        xy = rand_block(B, 1000 + t, en, ex)
        r, s = block_system(xy, S, M)
        deg, cn = core_numbers(r, s, B * B)
        print(f"random#{t} type=({en},{ex}) E={len(r)} avgdeg={2*len(r)/B/B:.3f} degen={cn.max()} 3core={(cn>=3).sum()} 4core={(cn>=4).sum()} t={time.time()-t0:.1f}")
        sys.stdout.flush()
