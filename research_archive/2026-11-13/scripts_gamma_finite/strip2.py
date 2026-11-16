# Two split primes: strip elements (real size near 1 or -phi^-2) per level, and a greedy test of the
# digit scheme with one l-adic character at each prime.  Usage: py strip2.py l1 l2 J delta cz_den
import sys, time, math
from fractions import Fraction as F
import mpmath as mp
from adelic import mul, pw, L, s1, find_pi, PHI
mp.mp.dps = 50
l1, l2, J = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); delta = float(sys.argv[4]); czd = int(sys.argv[5])
cz = F(1, czd)
def omega(l):
    p = find_pi(l); o = mul(p, p); return (o[0]/l, o[1]/l)
o1, o2 = omega(l1), omega(l2); eps = (F(-1), F(-1))
a1 = math.log(abs(float(s1(o1)))); a2 = math.log(abs(float(s1(o2)))); g = 2*math.log((1+5**0.5)/2)
t0 = time.time(); strip = []
for k1 in range(-J, J+1):
    for k2 in range(-J, J+1):
        base = mul(pw(o1, k1), pw(o2, k2))
        x = -(k1*a1 + k2*a2)/g
        for n in range(math.floor(x)-2, math.floor(x)+3):
            for sg in (1, -1):
                be = mul(pw(eps, n), base); be = (sg*be[0], sg*be[1])
                s = s1(be)
                if (1-delta < s < 1+delta) or (-PHI**-2*(1+delta) < s < -PHI**-2*(1-delta)):
                    r = L((be[0]-1, be[1]))
                    if r != 0: strip.append((k1, k2, r))
lev = {}
for (k1, k2, r) in strip: lev.setdefault(max(abs(k1), abs(k2)), []).append((k1, k2, r))
print("strip elements per level:", {j: len(v) for j, v in sorted(lev.items())}, "%.1fs" % (time.time()-t0))
def part(r, l):
    num, den = r.numerator, r.denominator; e = 0
    while den % l == 0: den //= l; e += 1
    if e == 0: return 0, 1
    m = l**e; return num*pow(den, -1, m) % m, m
def ok(ph): return min(ph, 1-ph) >= cz
z1 = z2 = 0
for j in range(1, J+1):
    best = None
    for d1 in range(l1):
        for d2 in range(l2):
            Z1 = z1 + d1*l1**(j-1); Z2 = z2 + d2*l2**(j-1); bad = 0
            for (k1, k2, r) in lev.get(j, []):
                u1, m1 = part(r, l1); u2, m2 = part(r, l2)
                p1 = F((Z1*u1) % m1, m1) if m1 > 1 else F(0); p2 = F((Z2*u2) % m2, m2) if m2 > 1 else F(0)
                if not (ok(p1) or ok(p2)): bad += 1
            if best is None or bad < best[0]: best = (bad, Z1, Z2)
            if bad == 0: break
        if best[0] == 0: break
    z1, z2 = best[1], best[2]
    print("level", j, "elements", len(lev.get(j, [])), "unavoidable bad", best[0], flush=True)
