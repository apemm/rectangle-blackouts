"""R2-same solutions with the Hilbert inequality delta^2 < 2|X| and X = 0 mod Smod.
Parameters: m ranges over s - y for bulk rows y, delta over multiples of 28.
usage: py r2s_hilbert.py Smod mmax dmax
Sea-type rule by chi_7 of the sea columns; sea row parity/alignment ignored
except that delta = 0 mod 28 and m is the actual s - y with y from a 28-progression.
"""
import sys, math
Smod, mmax, dmax, HIL = map(int, sys.argv[1:5])
QR = {1, 2, 4}
def stype(x):
    r = x % 7
    return 'F' if r == 0 else ('H' if r in QR else 'L')
def divisors(n):
    n = abs(n); out = set()
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0: out |= {d, n // d}
    return out
cnt = 0; ex = []
# sea rows s: L (=3), F (=55 mod 28 class), H (big). Use m = s - y directly:
# odd label y = 17 mod 28; L = 3 -> m = 3 - y = -14 mod 28 ; F=55 -> m = 38 - .. etc
for sname, s in (('L', 3), ('F', 55)):
    for y in range(17 + 28 * 3, mmax, 28):
        m = s - y
        for delta in range(-(dmax // 28) * 28, dmax + 1, 28):
            if delta == 0: continue
            N = delta * (2 * m - delta)
            if N == 0: continue
            for P0 in divisors(N):
                for P in (P0, -P0):
                    if (P * P - N) % (2 * P): continue
                    u = (P * P - N) // (2 * P)
                    if u == 0 or (m * delta) % u: continue
                    t = -(m * delta) // u
                    if (P + t) % 2: continue
                    X = (P + t) // 2
                    if X == 0 or X % Smod: continue
                    if HIL and delta * delta >= 2 * abs(X): continue
                    v = u - P
                    if s + delta // 2 < 1 or s - m + delta // 2 < 1: continue
                    if u % 7 == 0 and sname != 'F': continue
                    if stype(u) != sname or stype(X + v) != sname: continue
                    cnt += 1
                    if len(ex) < 10: ex.append((sname, y, m, delta, X, u, v))
print('solutions', cnt)
for e in ex: print(e)
