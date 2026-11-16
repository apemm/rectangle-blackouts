"""Mixed quadruples with exactly ONE row-1 sea point (column not divisible by s) and three label
points, in a stride-s scaffold with full diagonals.  Roles: the sea point is A (side) or C (diag).
Enumerate pairs {P1,P2} of black points with at least one label point as the SIDE pair or as
the DIAGONAL pair, translate by n = t (-U2,U1)/g, and solve for the remaining two points on the
circle |D-C| = |U|.  Every hit is checked from the definition.
usage: py sea1.py h s nb seed [offsets...]
"""
import sys, random
from math import gcd, isqrt
from collections import Counter

def isprime(n):
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return n > 1

h, s, nb, seed = map(int, sys.argv[1:5])
rng = random.Random(seed)
A_ = (h + 1) // 2; K = h // 2
p = max(20 * h, (s * s // 2 + 4) * h) + 1
while not isprime(p): p += 1
P = p
Ts = [int(t) for t in sys.argv[5:]]
while len(Ts) < nb: Ts.append(rng.randrange(-h + 2, h, 2) | 1)
lab = {}
for c, T in enumerate(Ts):
    st = (T - 1) // 2
    for i in range(A_):
        if 0 <= i + st < K:
            x = s * (i + P * c)
            lab[(x, 2 * i + 1)] = (c, i, 0); lab[(x, 2 * i + 1 + T)] = (c, i, 1)
pts = list(lab)
def black(q):
    return q in lab or (q[1] == 1 and q[0] % s != 0)
def is_mixed(Ap, Bp, Cp, Dp):
    ux, uy = Bp[0] - Ap[0], Bp[1] - Ap[1]; vx, vy = Dp[0] - Cp[0], Dp[1] - Cp[1]
    if ux == 0 or ux * ux + uy * uy != vx * vx + vy * vy: return False
    nx2 = Cp[0] + Dp[0] - Ap[0] - Bp[0]; ny2 = Cp[1] + Dp[1] - Ap[1] - Bp[1]
    if nx2 % 2 or ny2 % 2: return False
    nx, ny = nx2 // 2, ny2 // 2
    if (nx, ny) == (0, 0) or nx * ux + ny * uy != 0: return False
    if (vx, vy) in ((ux, uy), (-ux, -uy)) or len({Ap, Bp, Cp, Dp}) < 4: return False
    return 1 <= Ap[1] + ny <= h and 1 <= Bp[1] + ny <= h
res = Counter(); ex = []
W2 = (h - 1) ** 2 // 2 + 2
# (a) side pair = two label points A,B ; diagonal = sea C + label D
for a in range(len(pts)):
    for b in range(len(pts)):
        if a == b: continue
        Ap, Bp = pts[a], pts[b]
        ux, uy = Bp[0] - Ap[0], Bp[1] - Ap[1]
        if ux == 0 or abs(ux) > W2: continue
        L2 = ux * ux + uy * uy
        g = gcd(ux, uy); px, py = -uy // g, ux // g
        tmax = (2 * h) // abs(py) + 1 if py else 0
        for t in range(-tmax, tmax + 1):
            if t == 0: continue
            nx, ny = t * px, t * py
            if not (1 <= Ap[1] + ny <= h and 1 <= Bp[1] + ny <= h): continue
            Sx, Sy = Ap[0] + Bp[0] + 2 * nx, Ap[1] + Bp[1] + 2 * ny
            r = L2 - (Sy - 2) ** 2
            if r < 0: continue
            q = isqrt(r)
            if q * q != r: continue
            for sg in ((q, -q) if q else (0,)):
                if (Sx - sg) % 2: continue
                x0 = (Sx - sg) // 2
                if x0 % s == 0: continue
                Cp = (x0, 1); Dp = (Sx - x0, Sy - 1)
                if Dp not in lab: continue
                ok = is_mixed(Ap, Bp, Cp, Dp)
                key = (ok, "sea on diagonal", tuple(lab[z][2] for z in (Ap, Bp, Dp)), len({lab[z][0] for z in (Ap, Bp, Dp)}), "x0 mod 4 = %d" % (x0 % 4))
                res[key] += 1
                if ok and len(ex) < 5: ex.append((Ap, Bp, Cp, Dp))
# (b) side pair = sea A + label B ; diagonal = two label points C,D   (search over diagonal pairs)
for c_ in range(len(pts)):
    for d_ in range(c_ + 1, len(pts)):
        Cp, Dp = pts[c_], pts[d_]
        vx, vy = Dp[0] - Cp[0], Dp[1] - Cp[1]
        if abs(vx) > W2: continue
        L2 = vx * vx + vy * vy
        for Bp in pts:
            if Bp in (Cp, Dp): continue
            # A = (x0,1): |B-A|^2 = L2 -> (xB-x0)^2 = L2-(yB-1)^2
            r = L2 - (Bp[1] - 1) ** 2
            if r <= 0: continue
            q = isqrt(r)
            if q * q != r: continue
            for sg in (q, -q):
                Ap = (Bp[0] - sg, 1)
                if Ap[0] % s == 0: continue
                ok = is_mixed(Ap, Bp, Cp, Dp)
                if ok:
                    key = (ok, "sea on side", tuple(lab[z][2] for z in (Bp, Cp, Dp)), len({lab[z][0] for z in (Bp, Cp, Dp)}), "x0 mod 4 = %d" % (Ap[0] % 4))
                    res[key] += 1
                    if len(ex) < 10: ex.append((Ap, Bp, Cp, Dp))
print("h", h, "s", s, "P", P, "offsets", Ts, "label points", len(lab))
for k, v in sorted(res.items()): print(v, k)
for e in ex: print("  ", e, [lab.get(z) for z in e])
