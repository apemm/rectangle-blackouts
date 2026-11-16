"""Census of the 6PT subfamily with equal sea offsets (xi = xi') in one
aligned H7 block (mixed type), rows and sea as in r2s_census.py.
Hub f with odd point C=(x_f,a_f) and even point C'=(x_f,b_f). For a sea row
s and an even row offset delta: e has odd row a_f - delta, e' has even row
b_f - delta; m = s - a_f + delta, m' = s - b_f + delta. For every signed
divisor xi of gcd(delta m, delta m') with sea type s at offset xi:
X = -delta m/xi, X' = -delta m'/xi must be nonzero multiples of S, rows
s+delta of W in [1,h]. e must sit at x_f - X (slot gap -X/S from f) with
i_e = i_f - delta/28, and e' at x_f - X' with j_e' = j_f - delta/28.
Only delta = 0 mod 896 is scanned: 2^7 | delta is proved necessary (one of
m, m' is odd). The census checks the further claim 49 | delta for s in {L,H}.
usage: py sixpt_same_census.py h M sigma nsample seed
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
def divisors(n):
    n = abs(n); out = set()
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0: out |= {d, n // d}
    return out
def partner(rf, X):
    """labels whose column can be x_f - X: slot gap q = -X/S from f."""
    q = -X // S; sg = 1 if q > 0 else -1; aq = abs(q); out = []
    for d in {aq // M, -(-aq // M)}:
        if d < 1 or abs(aq - M * d) > M - 1: continue
        r = rf + sg * d
        if 0 <= r < Q * Q:
            x, y = d2xy(Q, r)
            if x < A and y < K: out.append((x, y))
    return out
labs = [(i, j) for i in range(A) for j in range(K)]
sample = random.sample(labs, min(ns, len(labs)))
arith = 0; half = 0; full = 0; viol49 = 0; per = []
for (i, j) in sample:
    rf = xy2d(Q, i, j); af, bf = a_rows[i], b_rows[j]; c = 0
    for s in (L, F, H):
        dmax = (2 * h // sigma) // 896 * 896
        for delta in range(-dmax, dmax + 1, 896):
            if delta == 0: continue
            if not (1 <= s + delta <= h): continue
            Di = delta // 28
            if not (0 <= i - Di < A and 0 <= j - Di < K): continue
            m = s - af + delta; mp = s - bf + delta
            g = math.gcd(delta * m, delta * mp)
            for x0 in divisors(g):
                for xi in (x0, -x0):
                    if stype(xi) != s: continue
                    X = -delta * m // xi; Xp = -delta * mp // xi
                    if X == 0 or Xp == 0 or X % S or Xp % S: continue
                    arith += 1
                    if s != F and delta % 49: viol49 += 1
                    he = [p for p in partner(rf, X) if p[0] == i - Di]
                    hp = [p for p in partner(rf, Xp) if p[1] == j - Di]
                    if he or hp: half += 1
                    if he and hp: full += 1; c += 1
    per.append(c)
print('h', h, 'M', M, 'sigma', sigma, 'S', S, 'sampled hubs', len(sample))
print('arith per hub', arith / len(sample), 'one-side hits per hub', half / len(sample),
      'full 6PT(xi=xi\') per hub', full / len(sample), 'max', max(per))
print('violations of 49 | delta (s in L,H):', viol49)
