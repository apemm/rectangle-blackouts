"""Census of R2s candidates per label in one aligned H7 block (mixed type).
Rows as in pt_census.py: odd label rows = 17 mod 28, even = 8 mod 28,
L = 3, F = 2015, H = largest x <= h with x = 18 mod 28 (g = 1, so the
physical sea rule is the normalized one). S = 6272*sigma. Standard Hilbert
curve on the padded Q-square; columns x_e = S(M r_e + xi_e).
For a sampled label e (side owner, point A), every role (odd/even), sea
row s, and row offset delta = 28*Delta to a same-parity point C of another
label, enumerate all signed factorizations g1*g2 = N = delta(2m - delta):
 U=(g2-g1)/2, V=(g1+g2)/2, T=-m delta/U (even), X=(U+T-V)/2 a nonzero multiple of S.
Keep: sea types of B (offset U) and D (offset X+V) equal to s, corners
p,q (rows y+delta/2, s+delta/2) in [1,h]. 'arith' counts these.
A hit is a label f at slot gap q=X/S (ranks d=floor,ceil(|q|/M) with
|q|-Md in [-(M-1),M-1]) whose role coordinate differs from e's by Delta.
usage: py r2s_census.py h M sigma nsample seed
"""
import sys, math, random
h, M, sigma, ns, seed = map(int, sys.argv[1:6]); random.seed(seed)
S = 6272 * sigma
L, F = 3, 2015
H = max(x for x in range(h - 800, h + 1) if x % 28 == 18)
lo, hi = 10000, h - 10000
a_rows = [a for a in range(lo, hi) if a % 28 == 17]
b_rows = [b for b in range(lo, hi) if b % 28 == 8]
A, K = len(a_rows), len(b_rows)
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
# spf sieve
LIM = 3 * h + 10
spf = list(range(LIM))
for p in range(2, math.isqrt(LIM) + 1):
    if spf[p] == p:
        for k in range(p * p, LIM, p):
            if spf[k] == k: spf[k] = p
def fac(n, out):
    n = abs(n)
    while n > 1:
        p = spf[n]; c = 0
        while n % p == 0: n //= p; c += 1
        out[p] = out.get(p, 0) + c
def divs(fd):
    ds = [1]
    for p, c in fd.items():
        ds = [d * p**k for d in ds for k in range(c + 1)]
    return ds
def v(p, n):
    n = abs(n); c = 0
    while n and n % p == 0: n //= p; c += 1
    return c
labs = [(i, j) for i in range(A) for j in range(K)]
sample = random.sample(labs, min(ns, len(labs)))
tot_hit = 0; tot_ar = 0; per = []; reg = {'c': 0, 's': 0, 'n': 0}
reg_ar = {'c': 0, 's': 0, 'n': 0}; arH = {'c': 0, 's': 0, 'n': 0}; band = {}; checks_bad = 0; slotflag = 0
seven_bad = 0; hits_detail = []
for (i, j) in sample:
    re = xy2d(Q, i, j); c = 0
    for role in (0, 1):
        y = a_rows[i] if role == 0 else b_rows[j]
        coord = i if role == 0 else j
        ncoord = A if role == 0 else K
        for s in (L, F, H):
            m = s - y
            for Dl in range(-coord, ncoord - coord):
                if Dl == 0: continue
                delta = 28 * Dl
                if not (1 <= y + delta // 2 <= h and 1 <= s + delta // 2 <= h): continue
                w = 2 * m - delta
                if w == 0: continue
                N = delta * w
                fd = {}; fac(delta, fd); fac(w, fd)
                md = m * delta
                for g in divs(fd):
                    for g1 in (g, -g):
                        g2 = N // g1
                        if (g1 - g2) & 1: continue
                        U = (g2 - g1) // 2
                        if U == 0 or md % U: continue
                        T = -md // U
                        if T & 1: continue
                        V = (g1 + g2) // 2
                        x2 = U + T - V
                        if x2 & 1: continue
                        X = x2 // 2
                        if X == 0 or X % S or V == 0: continue
                        if stype(U) != s or stype(V) != s: continue
                        e1 = U - X
                        if e1 == 0 or e1 + T == 0: continue
                        if 4 * e1 * (X - T) != T * T + delta * delta: checks_bad += 1
                        rg = 'c' if 2 * abs(e1) <= abs(X) else ('s' if 2 * abs(U) > abs(X) else 'n')
                        tot_ar += 1; reg_ar[rg] += 1
                        if 2 * abs(X) > M * sigma * delta * delta - 2 * (M - 1) * S: arH[rg] += 1
                        if len(sys.argv) > 6:
                            print('ar', role, s, 'y', y, 'm', m, 'delta', delta, 'U', U, 'V', V, 'T', T,
                                  'X/S', X // S, 'e1', e1, rg, 'g1', g1, 'g2', g2,
                                  'delta^2/(2|X|)', round(delta * delta / (2 * abs(X)), 3))
                        if s != F and m % 7 and v(7, delta) != v(7, X): seven_bad += 1
                        q = X // S; sg = 1 if q > 0 else -1; aq = abs(q)
                        for d in {aq // M, -(-aq // M)}:
                            if d < 1 or abs(aq - M * d) > M - 1: continue
                            rf = re + sg * d
                            if not (0 <= rf < Q * Q): continue
                            fi, fj = d2xy(Q, rf)
                            if fi >= A or fj >= K: continue
                            if (fi - i if role == 0 else fj - j) != Dl: continue
                            c += 1; reg[rg] += 1
                            if (U % S == 0) or (V % S == 0): slotflag += 1
                            hits_detail.append((role, s, delta, X, U, V, T, rg, d))
    per.append(c); tot_hit += c
    bk = min(abs(j - i) * 8 // max(A, 1), 7)
    band.setdefault(bk, []).append(c)
per.sort()
print('h', h, 'M', M, 'sigma', sigma, 'S', S, 'block', A, 'x', K, 'Q', Q, 'sampled', len(sample))
print('arith solutions per label (S|X, types, strip):', tot_ar / len(sample), reg_ar)
print('arith solutions also meeting |X| > M sigma delta^2/2 - (M-1)S (totals):', arH)
print('hits per label (side-owner role):', tot_hit / len(sample), 'max', per[-1], 'by regime', reg)
print('band (|j-i| in eighths of side): mean hits', {k: round(sum(x)/len(x), 4) for k, x in sorted(band.items())})
print('E4 failures', checks_bad, '7-adic rule failures', seven_bad, 'hits with B or D on a slot column', slotflag)
for z in hits_detail[:10]: print('hit', z)
