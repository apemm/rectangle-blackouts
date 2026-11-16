"""Exact checks for the ladder layer LAD (classes i mod 64; rows relative to T*, slot rel = n - rho).
(1) staircase property: every filler pair has dy = 0 or v2(dy) = 3 + v2(slot gap), and dy = 0 only for v2(gap) >= 2;
(2) Feo-relevant residues: holes have v2(row - T* + 24) >= 3 with row = T* - 24 (mod 16)... (bases unchanged);
(3) kill: for every homogeneous d<0 shape (alpha odd, beta even, coprime, 2 < alpha/beta < 4, beta <= Bmax),
    every lambda = 2 (mod 4) up to Lmax and every label alignment n1 = rho (mod 64) over one full period,
    the two filler slots are fillers with DIFFERENT LAD rows, unless the level is a class level beyond the ladder;
    and with the SAW* rows the same slots have EQUAL rows (sanity: the family is present in SAW*).
Usage: py ladder_check.py Eprime Bmax Lmax"""
import sys
from math import gcd

def v2(n):
    n = abs(n); c = 0
    if n == 0: return 99
    while n % 2 == 0: n //= 2; c += 1
    return c

Ep = int(sys.argv[1]); Bmax = int(sys.argv[2]); Lmax = int(sys.argv[3])
PER = 256 * max(1, 2 ** Ep) * 4      # a common period of the layer in slots (generous)

def row_lad(rel):
    """row offset relative to T* (T* = 0) for a non-label slot with rel = n - rho"""
    r = rel % 4
    if r == 1: return -16
    if r == 3: return 0
    if r == 2:
        t2 = (rel - 2) // 4
        return -8 - 32 * (t2 % 4)
    tau = rel // 4
    if tau % 2: phi = 1 + 2 * (((tau - 1) // 2) % 4)
    elif tau % 4 == 2: phi = 2 + 4 * (((tau - 2) // 4) % 4)
    elif tau % 8 == 4: phi = 4 + 8 * (((tau - 4) // 8) % 4)
    elif tau % 16 == 8: phi = 8 + 16 * (((tau - 8) // 16) % 4)
    else: phi = 16 * ((tau // 16) % (2 ** Ep)) if Ep > 0 else 0
    return -24 - 32 * phi

def row_saw(rel):
    return [-24, -16, -8, 0][rel % 4]

# (1) staircase property over pairs inside two periods
bad = 0; maxdepth = 0
rels = range(0, 2 * PER)
rows = {r: row_lad(r) for r in rels}
for a in rels:
    if a % 64 == 0: continue     # treat class slots as fillers too (empty); labels are excluded below anyway
for a in range(0, min(PER, 1024)):
    ra = rows[a]; maxdepth = min(maxdepth, ra)
    for b in range(a + 1, a + PER):
        g = b - a; dy = rows[b] - ra
        if dy == 0:
            if v2(g) < 2: bad += 1
        elif v2(dy) != 3 + v2(g): bad += 1
print('LAD E\'=%d: period %d slots, deepest filler row T*%d, staircase violations %d' % (Ep, PER, maxdepth, bad))

# (2) hole rows congruent to T* - 24 (mod 32) at offset 0 and T* - 8 (mod 32) at offset 2
h0 = all((row_lad(r) + 24) % 32 == 0 for r in range(0, PER, 4))
h2 = all((row_lad(r) + 8) % 32 == 0 for r in range(2, PER, 4))
print('offset-0 rows = T*-24 mod 32:', h0, ' offset-2 rows = T*-8 mod 32:', h2)

# (3) kill of the homogeneous family
stats = {}
for b in range(2, Bmax + 1, 2):
    for a in range(2 * b + 1, 4 * b):
        if a % 2 == 0 or gcd(a, b) != 1: continue
        w = [b * (a*a + b*b), (a - 4*b) * (a*a + b*b), b * (-3*a*a + 8*a*b + b*b),
             a**3 - 4*a*a*b - 3*a*b*b + 4*b**3, 4*b*b*(a - 2*b)]
        g = 0
        for c in w: g = gcd(g, abs(c))
        x1, u, x2, v, d = [-c // g for c in w]
        j = v2(b) + 1
        for lam in range(2, Lmax + 1, 4):
            X1, D2, X2 = lam * x1, 2 * lam * d, lam * x2
            s1 = X1; s2 = D2 + X2                # filler slots relative to n1
            for n1 in range(0, PER, 64):         # label alignments rho + 64 m
                r1 = n1 + s1; r2 = n1 + s2
                if r1 % 64 == 0 or r2 % 64 == 0: classF = True
                else: classF = False
                eqL = row_lad(r1 % PER) == row_lad(r2 % PER)
                eqS = row_saw(r1 % PER) == row_saw(r2 % PER)
                key = (j, classF)
                st = stats.setdefault(key, [0, 0, 0])
                st[0] += 1; st[1] += eqL; st[2] += eqS
for key in sorted(stats):
    n, eqL, eqS = stats[key]
    print('  level j=%d fillers on class slots=%s: placements %d, same row in LAD %d, same row in SAW* %d' % (key[0], key[1], n, eqL, eqS))
