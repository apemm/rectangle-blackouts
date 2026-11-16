"""Vectorized enumeration of type II label-only mixed quadruples (A,C in block c, B,D in block c+dc),
then a definition-level check of every hit (same scaffold as enum_types.py, full diagonals).
Equations used:  E*:  4 U2 (tau T d2 - tau2 T2 d) = (d+d2) G,   G = |g'-g|^2
                 E2:  s^2 (d+d2)(P dc + k) + U2 (eta+eta2) = 0          (d+d2 != 0)
                 E1:  2 s (d2-d) U1 + G = 0 with U2 = 0                 (d+d2 == 0)
usage: py enum_II.py h s [Pmult]
"""
import sys
import numpy as np
from collections import Counter

def isprime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return n > 1

h, s = int(sys.argv[1]), int(sys.argv[2])
A = (h + 1) // 2; K = h // 2
p = max(20 * h, (s * s // 2 + 4) * h) + 1
want = int(sys.argv[3]) if len(sys.argv) > 3 else -1
while not isprime(p) or (want >= 0 and p % 4 != want): p += 1
P = p
def slots(T):
    st = (T - 1) // 2
    return [i for i in range(A) if 0 <= i + st < K]
offs = np.array([T for T in range(-h + 1, h) if T % 2 and slots(T)], dtype=np.int64)
SL = {int(T): set(slots(int(T))) for T in offs}
Tg, T2g = np.meshgrid(offs, offs, indexing='ij')
smax = int(2 * (h - 1) ** 2 / (19 * s * s * h)) + 1
lmax = int(8 * h / (38 * s * s)) + 3
dmax = (smax, lmax)

def point(c, T, i, e):
    return (s * (i + P * c), 2 * i + 1 + (T if e else 0))

def is_mixed(Ap, Bp, Cp, Dp):
    ux, uy = Bp[0] - Ap[0], Bp[1] - Ap[1]; vx, vy = Dp[0] - Cp[0], Dp[1] - Cp[1]
    if ux == 0 or ux * ux + uy * uy != vx * vx + vy * vy: return False
    nx2 = Cp[0] + Dp[0] - Ap[0] - Bp[0]; ny2 = Cp[1] + Dp[1] - Ap[1] - Bp[1]
    if nx2 % 2 or ny2 % 2: return False
    nx, ny = nx2 // 2, ny2 // 2
    if (nx, ny) == (0, 0) or nx * ux + ny * uy != 0: return False
    if (vx, vy) in ((ux, uy), (-ux, -uy)) or len({Ap, Bp, Cp, Dp}) < 4: return False
    return 1 <= Ap[1] + ny <= h and 1 <= Bp[1] + ny <= h

stage = Counter(); hits = Counter(); ex = []
for tau in (1, -1):
    eA = (1 - tau) // 2
    for tau2 in (1, -1):
        eB = (1 - tau2) // 2
        for Sg0 in range(-smax, smax + 1):
          for Dl in range(-lmax, lmax + 1):
                if (Sg0 + Dl) % 2: continue
                d2 = (Sg0 + Dl) // 2; d = (Sg0 - Dl) // 2
                if d == 0 and d2 == 0: continue
                Sg = d + d2
                eta = 2 * d + tau * Tg; eta2 = 2 * d2 + tau2 * T2g
                N1 = tau * Tg * d2 - tau2 * T2g * d
                G = (s * (d2 - d)) ** 2 + (eta2 - eta) ** 2
                base = eB * T2g - eA * Tg
                if Sg != 0:
                    rhs = Sg * G
                    ok = (N1 != 0) & (G != 0)
                    N1s = np.where(ok, N1, 1)
                    ok &= (rhs % (4 * N1s) == 0)
                    U2 = np.where(ok, rhs // (4 * N1s), 0)
                    ok &= (np.abs(U2) < h)
                    ok &= ((U2 - base) % 2 == 0)
                    k = (U2 - base) // 2
                    num = -(s * s * Sg * k + U2 * (eta + eta2))
                    den = s * s * Sg * P
                    ok &= (num % den == 0) & (num != 0)
                    dc = num // den
                else:
                    U2 = np.zeros_like(Tg)
                    ok = (N1 != 0) & (G != 0) & (base % 2 == 0)
                    k = (0 - base) // 2
                    num = -G - 2 * s * s * (d2 - d) * k
                    den = 2 * s * s * (d2 - d) * P
                    ok &= (num % den == 0) & (num != 0)
                    dc = num // den
                stage[(tau, tau2, Sg == 0)] += int(ok.sum())
                for (ii, jj) in zip(*np.nonzero(ok)):
                    T = int(Tg[ii, jj]); T2 = int(T2g[ii, jj]); kk = int(k[ii, jj]); dcc = int(dc[ii, jj])
                    sl, sl2 = SL[T], SL[T2]
                    for iA in sl:
                        iC, iB = iA + d, iA + kk; iD = iB + d2
                        if iC in sl and iB in sl2 and iD in sl2:
                            Ap = point(0, T, iA, eA); Cp = point(0, T, iC, 1 - eA)
                            Bp = point(dcc, T2, iB, eB); Dp = point(dcc, T2, iD, 1 - eB)
                            okm = is_mixed(Ap, Bp, Cp, Dp)
                            hits[(tau, tau2, Sg == 0, d == 0 or d2 == 0, okm)] += 1
                            if okm and len(ex) < 8: ex.append((tau, tau2, T, T2, d, d2, kk, dcc, iA, Ap, Bp, Cp, Dp))
print("h", h, "s", s, "P", P, "P mod 4", P % 4, "dmax", dmax)
print("equation solutions before slots, by (tau,tau2):", dict(stage))
print("slot-feasible (tau,tau2,horizontal,three-label,definition-ok):", dict(hits))
for e in ex: print("  ", e)
