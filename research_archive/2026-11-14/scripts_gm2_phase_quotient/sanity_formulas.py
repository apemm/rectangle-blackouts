"""Exact sanity checks of the small formulas (not proofs):
(1) Prop 2: measure of V(t, delta) = (M-|delta|)(1/M - ||t - delta/M||)_+ ;
(2) Theorem 6(c'): exact independence of {d1 tau in G(R1)} and {d2 tau in G(R2)} when M | d2/g or M | d1/g,
    and the error bound J1 J2 g^2/(3 d1 d2) otherwise;
(3) Prop 8: an irrational-like tau gives M*p distinct assignments on p ranks as theta varies.
Everything with Fractions; measures computed from exact interval lists."""
import random
from fractions import Fraction as Fr
from math import gcd

random.seed(1)

def dist(x):
    x = x % 1
    return min(x, 1 - x)

def meas_V(t, dl, M):
    # V = {y in [0,1): D(y + t) - D(y) = dl}; breakpoints k/M and k/M - t
    pts = sorted({Fr(k, M) for k in range(M)} | {(Fr(k, M) - t) % 1 for k in range(M)} | {Fr(1)})
    tot = Fr(0)
    for a, b in zip(pts, pts[1:]):
        y = (a + b) / 2
        if int(((y + t) % 1) * M) - int(y * M) == dl: tot += b - a
    return tot

bad = 0
for _ in range(3000):
    M = random.randint(2, 7); dl = random.randint(-(M - 1), M - 1)
    t = Fr(random.randint(0, 10 ** 6), 10 ** 6)
    pred = (M - abs(dl)) * max(Fr(0), Fr(1, M) - dist(t - Fr(dl, M)))
    if meas_V(t, dl, M) != pred: bad += 1
print("(1) Prop 2 measure formula: failures", bad, "of 3000")

def Gcells(R, M):
    return [j for j in range(M) if j % M not in R and (j + 1) % M not in R]

def meas_pair(d1, R1, d2, R2, M):
    L = d1 * d2 * M
    tot = Fr(0)
    pts = sorted({Fr(k, M * d1) for k in range(M * d1 + 1)} | {Fr(k, M * d2) for k in range(M * d2 + 1)})
    C1, C2 = set(Gcells(R1, M)), set(Gcells(R2, M))
    for a, b in zip(pts, pts[1:]):
        y = (a + b) / 2
        if int((d1 * y % 1) * M) in C1 and int((d2 * y % 1) * M) in C2: tot += b - a
    return tot

bad = 0; badb = 0; cnt = 0
for _ in range(1500):
    M = random.randint(2, 5); d1 = random.randint(1, 30); d2 = random.randint(1, 30)
    if d1 == d2: continue
    R1 = set(random.sample(range(M), random.randint(1, M - 1))); R2 = set(random.sample(range(M), random.randint(1, M - 1)))
    g = gcd(d1, d2)
    m1 = Fr(len(Gcells(R1, M)), M); m2 = Fr(len(Gcells(R2, M)), M)
    mp = meas_pair(d1, R1, d2, R2, M)
    J1 = len(Gcells(R1, M)); J2 = len(Gcells(R2, M))
    cnt += 1
    if (d2 // g) % M == 0 or (d1 // g) % M == 0:
        if mp != m1 * m2: bad += 1
    if abs(mp - m1 * m2) > Fr(J1 * J2 * g * g, 3 * d1 * d2): badb += 1
print("(2) pair independence failures", bad, "; error-bound failures", badb, "of", cnt)

M = 3; tau = Fr(141421356, 10 ** 9) ; p = 40
bps = sorted({(Fr(k, M) - tau * r) % 1 for r in range(p) for k in range(M)})
assign = set()
for a, b in zip(bps, bps[1:] + [bps[0] + 1]):
    th = (a + b) / 2
    assign.add(tuple(int(((tau * r + th) % 1) * M) for r in range(p)))
print("(3) distinct assignments over all phases:", len(assign), "expected M*p =", M * p)
