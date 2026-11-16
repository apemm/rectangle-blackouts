"""Sanity census: candidate parked triangles (PT) per label in one aligned
Hilbert period-seven block (mixed type), stride S = 6272 = 8*28^2.
PT: right angle at label point A (row y) of e, other end C = same-parity
point of f at (X, y+delta), third corner sea point (xi, s) with
X*xi = -delta*(s-y); sea type of xi must be s; W row s+delta in [1,h].
Candidates are counted over ALL choice gaps q in f's window
[M(d-1)+1, M(d+1)-1], d = |r_f - r_e| (as in the factor-choice notes).
usage: py pt_census.py h M nsample seed
"""
import sys, random, math
h, M, ns, seed = map(int, sys.argv[1:5]); random.seed(seed)
S = 6272
L, F = 3, 2015
H = max(x for x in range(h - 800, h + 1) if x % 28 == 18)
QR = {1, 2, 4}
def stype(x):
    r = x % 7
    return F if r == 0 else (H if r in QR else L)
lo, hi = 10000, h - 10000
a_rows = [a for a in range(lo, hi) if a % 28 == 17]
b_rows = [b for b in range(lo, hi) if b % 28 == 8]
A, K = len(a_rows), len(b_rows)
q = 1
while q < max(A, K): q *= 2
def xy2d(n, x, y):
    d = 0; s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0; ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1:
                x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        s //= 2
    return d
rank_of = {}; lab_at = {}
for i in range(A):
    for j in range(K):
        r = xy2d(q, i, j); rank_of[(i, j)] = r; lab_at[r] = (i, j)
def divisors(n):
    out = set()
    for dd in range(1, math.isqrt(n) + 1):
        if n % dd == 0: out |= {dd, n // dd}
    return out
labs = list(rank_of)
sample = random.sample(labs, min(ns, len(labs)))
tot = 0; per = []
for (i, j) in sample:
    re = rank_of[(i, j)]; c = 0
    for role in (0, 1):
        y = a_rows[i] if role == 0 else b_rows[j]
        for s in (L, F, H):
            m = s - y
            Dmax = abs(m) // (14 * M) + 8
            for Dl in range(-Dmax, Dmax + 1):
                if Dl == 0: continue
                delta = 28 * Dl
                if not (1 <= s + delta <= h): continue
                N = abs(delta * m)
                if N % S: continue
                for qq in divisors(N // S):
                    xi_abs = N // (S * qq)
                    if xi_abs < 1: continue
                    for side in (1, -1):
                        X = side * S * qq
                        xi = -delta * m // X
                        if stype(xi) != s or xi % S == 0 and s == F and False: pass
                        if stype(xi) != s: continue
                        for d in {qq // M, -(-qq // M)}:
                            if d < 1: continue
                            if not (M * (d - 1) + 1 <= qq <= M * (d + 1) - 1): continue
                            rf = re + side * d
                            if rf not in lab_at: continue
                            fi, fj = lab_at[rf]
                            if role == 0 and fi - i == Dl: c += 1
                            if role == 1 and fj - j == Dl: c += 1
    per.append(c); tot += c
per.sort()
print('h', h, 'M', M, 'labels in block', len(labs), 'side', q)
print('mean PT candidates per label', tot / len(sample), 'max', per[-1],
      'frac>0', sum(1 for x in per if x) / len(per))
