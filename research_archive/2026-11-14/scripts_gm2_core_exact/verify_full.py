"""Independent checker (shares no code with build_core.py / extend.py / dpll.py).

Usage: py -B verify_full.py B S M orient version assignment.npy [count]
Places label of local rank r at column x_r = S (M r + xi_r).  For every pair of
labels r < u whose column difference X = x_u - x_r is a multiple of S that is
the leg of a Pythagorean triple with an odd leg Y <= 2B-1, and every cross
pair (odd row of one label, even row of the other) with |row difference| = Y,
it reports a violation (version 'gen': only when the owner of the two completion
rows lies outside the block).  Hilbert cells are computed digit by digit per rank;
Pythagorean legs by an isqrt scan over X.  With 'count' it also counts the
distinct constraint triples (r, u, delta) of the system, independently of xi.
"""
import sys, math, time
import numpy as np

B, S, M, orient, version = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
xi = np.load(sys.argv[6]).astype(np.int64)
do_count = len(sys.argv) > 7 and sys.argv[7] == "count"
part, nparts = (int(sys.argv[8]), int(sys.argv[9])) if len(sys.argv) > 9 else (0, 1)
t0 = time.time()
n = B * B
assert xi.shape == (n,) and xi.min() >= 0 and xi.max() < M

# Hilbert cells, digit recursion per rank
t = np.arange(n, dtype=np.int64)
x = np.zeros(n, dtype=np.int64); y = np.zeros(n, dtype=np.int64)
lev, w = 0, 1
while w < B:
    k = (t >> (2 * lev)) & 3
    nx = np.where(k == 0, y, np.where(k == 1, x, np.where(k == 2, x + w, 2 * w - 1 - y)))
    ny = np.where(k == 0, x, np.where(k == 1, y + w, np.where(k == 2, y + w, w - 1 - x)))
    x, y = nx, ny
    lev += 1; w *= 2
assert (np.abs(np.diff(x)) + np.abs(np.diff(y)) == 1).all(), "not a Hilbert path"
assert len(np.unique(x * B + y)) == n
if orient == "swap":
    x, y = y, x
odd = 2 * x + 1; even = 2 * y + 2

# Pythagorean table by isqrt scan: Lt[qi, Y] = L for X = S q
Ymax = 2 * B - 1
pairs = {}
for Y in range(1, Ymax + 1, 2):
    Xs = S * np.arange(1, (Y * Y - 1) // (2 * S) + 1, dtype=np.int64)   # X <= (Y^2-1)/2 for an integer L
    v = Xs * Xs + Y * Y
    rt = np.floor(np.sqrt(v.astype(np.float64))).astype(np.int64)
    for c in (-1, 0, 1):
        hit = (rt + c) * (rt + c) == v
        for X in Xs[hit].tolist():
            L = math.isqrt(X * X + Y * Y); assert L * L == X * X + Y * Y
            pairs.setdefault(X // S, {})[Y] = L
qs = sorted(pairs)
qmax = max(qs)
qidx = -np.ones(qmax + M + 2, dtype=np.int64)
Lt = np.zeros((len(qs), Ymax + 2), dtype=np.int64)
for i, q in enumerate(qs):
    qidx[q] = i
    for Y, L in pairs[q].items():
        Lt[i, Y] = L
ds = sorted({d for q in qs for d in range(max(1, (q - M + 1 + M - 1) // M), (q + M - 1) // M + 1)
             if abs(q - M * d) <= M - 1 and d < n})
W = Ymax + 2
Ltf = Lt.ravel()
ds = ds[part::nparts]
print(f"B={B} S={S} M={M} {orient} {version}: {len(qs)} gaps with legs, {len(ds)} rank distances (part {part}/{nparts})", flush=True)


def hits(r, d, q):
    """mask of r (array) where a cross pair at rank distance d, gap q is a constraint"""
    qi = qidx[q]
    ok = qi >= 0
    res = []
    for a, b in ((odd[r], even[r + d]), (odd[r + d], even[r])):
        Y = np.abs(b - a)
        L = np.where(ok & (Y <= Ymax), Ltf[np.maximum(qi, 0) * W + np.minimum(Y, Ymax)], 0)
        good = L > 0
        if version == "gen":
            s = a + b
            lo = (s - L) // 2; hi = (s + L) // 2
            oddrow = np.where(lo % 2 == 1, lo, hi); evrow = np.where(lo % 2 == 1, hi, lo)
            oi = (oddrow - 1) // 2; oj = (evrow - 2) // 2
            inside = (oi >= 0) & (oi < B) & (oj >= 0) & (oj < B)
            good &= ~inside
        res.append(good)
    return res[0] | res[1]


viol = 0; count = 0
for d in ds:
    r = np.arange(n - d, dtype=np.int64)
    q = M * d + xi[r + d] - xi[r]          # actual slot gap of the pair (r, r+d)
    sel = (q >= 1) & (q <= qmax) & (qidx[np.clip(q, 0, qmax)] >= 0)
    if sel.any():
        rr = r[sel]
        viol += int(hits(rr, d, q[sel]).sum())
    if do_count:
        for delta in range(-(M - 1), M):
            qq = M * d + delta
            if qq < 1 or qq > qmax or qidx[qq] < 0:
                continue
            count += int(hits(r, d, np.full(n - d, qq)).sum())
print(f"  violated pairs: {viol}" + (f"   distinct constraint triples: {count}" if do_count else "")
      + f"   ({time.time()-t0:.1f}s)")
