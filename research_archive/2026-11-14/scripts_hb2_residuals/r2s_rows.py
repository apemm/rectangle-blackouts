"""Hilbert-free R2s row counts for ALL rows of one role in the aligned
mixed block of r2s_census.py. For a label row y (point A) and sea row s,
A(y,s) = number of Hilbert-feasible arithmetic solutions (delta,U,V,X)
(S | X, |X| > sigma delta^2/2, sea types, strip, delta = 28*Delta with the
partner row y+delta a label row). B(y,s) = number of such solutions of
other rows y' with y' + delta = y (y is then the diagonal owner's row).
Every label e with this row has R2s degree <= 2*sum_s (A + B) in this role.
Enumeration as in r2s_pruned.py (regime lemma).
usage: py r2s_rows.py h sigma role lo
"""
import sys, math
h, sigma, role, lo = map(int, sys.argv[1:5])
t0, t1 = (int(sys.argv[5]), int(sys.argv[6])) if len(sys.argv) > 6 else (0, 10**9)
S = 6272 * sigma
L, F = 3, 2015
H = max(x for x in range(h - 800, h + 1) if x % 28 == 18)
hi = h - lo
r0 = lo + ((17 if role == 0 else 8) - lo) % 28
rows = list(range(r0, hi, 28)); nr = len(rows)
QR = {1, 2, 4}
def stype(x):
    r = x % 7
    return F if r == 0 else (H if r in QR else L)
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
    return X
dcs = int(2.02 * math.sqrt(h) * sigma ** (-0.75)) + 28
Acnt = [0] * nr; Bcnt = [0] * nr; ex = []
for t, y in enumerate(rows):
    if not (t0 <= t < t1): continue
    for s in (L, F, H):
        m = s - y; found = set()
        for Dl in range(-min(t, dcs // 28), min(nr - t, dcs // 28 + 1)):
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
                    if X is not None: found.add((delta, U, V, X))
        Umax = 4 * abs(m) // (sigma * 28) + 1
        for Ua in range(1, Umax + 1):
            u2 = Ua // math.gcd(Ua, m)
            step = 28 * u2 // math.gcd(28, u2)
            kmax = (4 * abs(m) // (sigma * Ua) + 1) // step
            for k in range(-kmax, kmax + 1):
                delta = k * step
                if delta == 0: continue
                Dl = delta // 28
                if not (0 <= t + Dl < nr): continue
                N = delta * (2 * m - delta)
                for U in (Ua, -Ua):
                    R = U * U + N
                    if R <= 0: continue
                    Vr = math.isqrt(R)
                    if Vr * Vr != R: continue
                    for V in (Vr, -Vr):
                        X = accept(y, s, m, delta, U, V)
                        if X is not None: found.add((delta, U, V, X))
        Acnt[t] += len(found)
        for (delta, U, V, X) in found:
            Bcnt[t + delta // 28] += 1
            if len(ex) < 6: ex.append((y, s, delta, U, V, X // S))
tot = [Acnt[t] + Bcnt[t] for t in range(nr)]
from collections import Counter
print('h', h, 'sigma', sigma, 'role', 'odd' if role == 0 else 'even', 'rows', nr, 'bulk from', lo)
print('A computed for row indices', t0, 'to', min(t1, nr))
print('rows with A>0:', sum(1 for a in Acnt if a), 'sum A', sum(Acnt), 'max A', max(Acnt), 'max A+B', max(tot))
print('histogram of A+B over rows:', sorted(Counter(tot).items()))
print('examples (y, s, delta, U, V, X/S):', ex)
