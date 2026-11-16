"""Exact enumeration of the Hilbert-feasible R2s solutions of a label,
using the regime lemma (proved in the write-up):
 every R2s solution with |X| >= S and |X| > sigma*delta^2/2 is in
 (c)/(s): |X| < 2.04 h/sqrt(sigma), hence |delta| < 2.02 sqrt(h) sigma^(-3/4), or
 (n): 1 <= |U| < 4|m|/(sigma |delta|).
(c)/(s): full factorization enumeration for the few small delta.
(n): loop over U and over delta in lcm(28, U/gcd(U,m)) Z; test U^2+N square.
Keeps S | X, sea types of B and D, strip rows of p and q, and the weak
Hilbert bound |X| > sigma delta^2/2; then looks for actual partners f.
Rows, sea and Hilbert curve as in r2s_census.py; bulk rows [lo, h-lo].
usage: py r2s_pruned.py h M sigma nsample seed lo
"""
import sys, math, random
h, M, sigma, ns, seed, lo = map(int, sys.argv[1:7]); random.seed(seed)
S = 6272 * sigma
L, F = 3, 2015
H = max(x for x in range(h - 800, h + 1) if x % 28 == 18)
hi = h - lo
a0 = lo + (17 - lo) % 28; b0 = lo + (8 - lo) % 28
A = len(range(a0, hi, 28)); K = len(range(b0, hi, 28))
Q = 1
while Q < max(A, K): Q *= 2
QR = {1, 2, 4}
def stype(x):
    r = x % 7
    return F if r == 0 else (H if r in QR else L)
def xy2d(n, x, y):
    d = 0; s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0; ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        s //= 2
    return d
def d2xy(n, d):
    x = y = 0; s = 1; t = d
    while s < n:
        rx = 1 & (t // 2); ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        x += s * rx; y += s * ry
        t //= 4; s *= 2
    return x, y
def fac(n, fd):
    n = abs(n); p = 2
    while p * p <= n:
        while n % p == 0: fd[p] = fd.get(p, 0) + 1; n //= p
        p += 1 if p == 2 else 2
    if n > 1: fd[n] = fd.get(n, 0) + 1
def divisors2(a, b):
    fd = {}; fac(a, fd); fac(b, fd); ds = [1]
    for p, c in fd.items():
        ds = [d * p**k for d in ds for k in range(c + 1)]
    return ds
def accept(y, s, m, delta, U, V):
    """common tests; returns X or None."""
    if U == 0 or V == 0: return None
    md = m * delta
    if md % U: return None
    T = -md // U
    if T & 1: return None
    x2 = U + T - V
    if x2 & 1: return None
    X = x2 // 2
    if X == 0 or X % S: return None
    if 2 * abs(X) <= sigma * delta * delta: return None
    if stype(U) != s or stype(V) != s: return None
    e1 = U - X
    if e1 == 0 or e1 + T == 0: return None
    if not (1 <= y + delta // 2 <= h and 1 <= s + delta // 2 <= h): return None
    assert 4 * e1 * (X - T) == T * T + delta * delta
    return X
dcs = int(2.02 * math.sqrt(h) * sigma ** (-0.75)) + 28
tot = 0; feas = {'cs': 0, 'n': 0}; hits = 0; per_feas = []
sample = [(random.randrange(A), random.randrange(K)) for _ in range(ns)]
for (i, j) in sample:
    re = xy2d(Q, i, j); found = set()
    for role in (0, 1):
        y = (a0 + 28 * i) if role == 0 else (b0 + 28 * j)
        coord = i if role == 0 else j; ncoord = A if role == 0 else K
        for s in (L, F, H):
            m = s - y
            # (c)/(s): small delta, full factorization
            for Dl in range(-min(coord, dcs // 28), min(ncoord - coord, dcs // 28 + 1)):
                if Dl == 0: continue
                delta = 28 * Dl; w = 2 * m - delta
                if w == 0: continue
                N = delta * w
                for g in divisors2(delta, w):
                    for g1 in (g, -g):
                        g2 = N // g1
                        if (g1 - g2) & 1: continue
                        U = (g2 - g1) // 2; V = (g1 + g2) // 2
                        X = accept(y, s, m, delta, U, V)
                        if X is not None: found.add((role, s, delta, U, V, X))
            # (n): small U
            Umax = 4 * abs(m) // (sigma * 28) + 1
            for Ua in range(1, Umax + 1):
                step = 28 * (Ua // math.gcd(Ua, m)) // math.gcd(28, Ua // math.gcd(Ua, m))
                dlim = 4 * abs(m) // (sigma * Ua) + 1
                kmax = dlim // step
                for k in range(-kmax, kmax + 1):
                    delta = k * step
                    if delta == 0 or delta % 28: continue
                    Dl = delta // 28
                    if not (0 <= coord + Dl < ncoord): continue
                    N = delta * (2 * m - delta)
                    for U in (Ua, -Ua):
                        R = U * U + N
                        if R <= 0: continue
                        Vr = math.isqrt(R)
                        if Vr * Vr != R: continue
                        for V in (Vr, -Vr):
                            X = accept(y, s, m, delta, U, V)
                            if X is not None: found.add((role, s, delta, U, V, X))
    per_feas.append(len(found))
    for z in found: print('FEAS label', (i, j), 'rank', re, z)
    for (role, s, delta, U, V, X) in found:
        rg = 'cs' if 2 * abs(U) > abs(X) or 2 * abs(U - X) <= abs(X) else 'n'
        feas[rg] += 1
        q = X // S; sg = 1 if q > 0 else -1; aq = abs(q)
        for d in {aq // M, -(-aq // M)}:
            if d < 1 or abs(aq - M * d) > M - 1: continue
            rf = re + sg * d
            if not (0 <= rf < Q * Q): continue
            fi, fj = d2xy(Q, rf)
            if fi >= A or fj >= K: continue
            if (fi - i if role == 0 else fj - j) == delta // 28:
                hits += 1; print('HIT', role, s, delta, U, V, X, rg, d)
print('h', h, 'M', M, 'sigma', sigma, 'S', S, 'bulk from', lo, 'side', A, 'Q', Q, 'labels', ns)
print('Hilbert-feasible arithmetic solutions per label', sum(per_feas) / ns, 'max', max(per_feas), feas)
print('actual R2s hits per label (side-owner role)', hits / ns)
