"""Rigid 2-adic layout at realistic h (P > 20h): cost (positions used vs classes) and a
formula-based count of fatal cross-block (E;O,E) configurations, rigid vs one random layout.
Usage: py check4_rigid_cost.py h lam"""
import sys, math, random
from collections import defaultdict
from common import *
h = int(sys.argv[1]); lam = float(sys.argv[2]); random.seed(7)
A, K = params(h); P = next_prime(int(lam*h)+1)
cls = all_classes(h); C = len(cls)
r = 0
while 2**(r+3) < K: r += 1
Mr = 2**r; Pinv = pow(P, -1, Mr)
Mcount = defaultdict(int)
for s, _ in cls: Mcount[s] += 1
Nrho = defaultdict(int)
for s, c in Mcount.items(): Nrho[s % Mr] += c
FULL = (1 << A) - 1
def bits(sl):
    b = 0
    for i in sl: b |= 1 << i
    return b
def sh(b, t): return (b >> t) if t >= 0 else ((b << (-t)) & FULL)
def rng(lo, hi):
    lo = max(lo, 0); hi = min(hi, A)
    return 0 if hi <= lo else ((1 << hi) - 1) ^ ((1 << lo) - 1)
def rigid():
    nxt = defaultdict(int); out = []
    for (s, sl) in cls:
        rho = (Pinv*s) % Mr; k = nxt[rho]; nxt[rho] += 1
        out.append((s, bits(sl), rho + Mr*k))
    return out
def rand():
    o = cls[:]; random.shuffle(o)
    return [(s, bits(sl), c) for c, (s, sl) in enumerate(o)]
t1max = int(h*K/(8*(P-h) - 10*K)) + 1
def fatal(lay):
    at = {pos: (s, B) for (s, B, pos) in lay}
    tot = 0
    for (s0, B0, p0) in lay:
        T0 = 2*s0+1
        for t1 in list(range(1, t1max+1)) + list(range(-t1max, 0)):
            Pm = B0 & sh(B0, t1)
            if not Pm: continue
            g = math.gcd(abs(t1), abs(T0)); t1p = t1//g; ep = (10*t1 - T0)//g
            nmax = (K-1)//(8*abs(t1p)); nmin = max(1, -(-(P-h)//abs(ep)))
            for n in list(range(nmin, nmax+1)) + list(range(-nmax, -nmin+1)):
                N = ep*n; c2 = 8*t1p*n
                q = (N + P//2)//P; ds = N - P*q; dc = -q
                if dc == 0: continue
                blk = at.get(p0 + dc)
                if blk is None or blk[0] != s0 + ds: continue
                u = c2 - ds; B1 = blk[1]
                tot += bin(Pm & sh(B1, u) & sh(B1, u+t1) & rng(-t1-c2, A-t1-c2)).count("1")
    return tot
lr = rigid(); span = max(p for _, _, p in lr) + 1
print(f"h={h} P={P} classes C={C} maxM_T={max(Mcount.values())} 2^r={Mr} max_rho N_rho={max(Nrho.values())} mean N_rho={C/Mr:.1f}")
print(f"  rigid positions={span}  ratio positions/C={span/C:.2f}  positions/h={span/h:.2f}  bound 2^r*maxN={Mr*max(Nrho.values())}")
pass
