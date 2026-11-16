"""Mixed quadruples with two row-1 sea points, one on the side and one on the diagonal:
A=(x0,1), C=(x0',1) sea (s does not divide x0, x0'), B, D label points of the stride-s scaffold
(full diagonals in blocks c=0..nb-1).  Method: (u-w)(u+w) = N := (yD-yB)(yB+yD-2),
u(2 dx + u - w) = -(yB-1)(yD-yB), u = xB-x0, w = xD-x0'.  Every hit is checked from the
definition.  Also: brute force over ALL pairs of sea points for the side-side and diag-diag roles
is replaced by the proof in the write-up (integer-length argument).
usage: py sea2.py h s nb seed [offsets...]
"""
import sys, random
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

def divisors(n):
    n = abs(n); out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
        d += 1
    return out

def is_mixed(Ap, Bp, Cp, Dp):
    ux, uy = Bp[0] - Ap[0], Bp[1] - Ap[1]; vx, vy = Dp[0] - Cp[0], Dp[1] - Cp[1]
    if ux == 0 or ux * ux + uy * uy != vx * vx + vy * vy: return False
    nx2 = Cp[0] + Dp[0] - Ap[0] - Bp[0]; ny2 = Cp[1] + Dp[1] - Ap[1] - Bp[1]
    if nx2 % 2 or ny2 % 2: return False
    nx, ny = nx2 // 2, ny2 // 2
    if (nx, ny) == (0, 0) or nx * ux + ny * uy != 0: return False
    if (vx, vy) in ((ux, uy), (-ux, -uy)) or len({Ap, Bp, Cp, Dp}) < 4: return False
    return 1 <= Ap[1] + ny <= h and 1 <= Bp[1] + ny <= h

divcache = {}
res = Counter(); ex = []
for (xB, yB), infoB in lab.items():
    for yD in range(1, h + 1):
        if (yD - yB) % 2 or yD == yB: continue
        N = (yD - yB) * (yB + yD - 2)
        if N == 0: continue
        if abs(N) not in divcache: divcache[abs(N)] = divisors(N)
        for d0 in divcache[abs(N)]:
            for d in (d0, -d0):
                e = N // d
                if (d + e) % 2: continue
                u = (d + e) // 2; w = (e - d) // 2
                if u == 0: continue
                r = -(yB - 1) * (yD - yB)
                if r % u: continue
                t = r // u - d
                if t % 2: continue
                dx = t // 2
                xD = xB + dx
                if (xD, yD) not in lab: continue
                x0 = xB - u; x0p = xD - w
                if x0 % s == 0 or x0p % s == 0: continue
                Ap, Bp, Cp, Dp = (x0, 1), (xB, yB), (x0p, 1), (xD, yD)
                ok = is_mixed(Ap, Bp, Cp, Dp)
                infoD = lab[(xD, yD)]
                key = (ok, "same block" if infoB[0] == infoD[0] else "two blocks", "B,D parity", infoB[2], infoD[2])
                res[key] += 1
                if ok and len(ex) < 6: ex.append((Ap, Bp, infoB, Cp, Dp, infoD))
print("h", h, "s", s, "P", P, "offsets", Ts, "label points", len(lab))
for k, v in sorted(res.items()): print(v, k)
for e in ex: print("  ", e)
