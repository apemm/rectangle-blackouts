"""Finite checks for the sawtooth layer SAW in Euclidean coordinates (n, Y), Y = (y - r1)/4.
Filler height Y(n) = H[n mod 4] with H = (-2, 0, 2, 4) (offset 0 = label residue).
Labels: (8k, 4k) (odd points).  All checks are exact integer enumerations."""
from math import isqrt
H = (-2, 0, 2, 4)
Y = lambda n: H[n % 4]
bad = 0
# (a) no right angle with three filler points (vertex V, legs to P, Q), legs not axis-parallel.
for v in range(4):
    for a1 in range(-80, 81):
        e1 = Y(v + a1) - Y(v)
        if a1 == 0 or e1 == 0: continue
        for a2 in range(-80, 81):
            e2 = Y(v + a2) - Y(v)
            if a2 == 0 or e2 == 0: continue
            if a1 * a2 + e1 * e2 == 0: bad += 1
print('(a) filler right angles:', bad)
# (b) filler-only mixed quadruples: A=(a,Y(a)), B=(a+U,..), C=(c,..), D=(c+dl,..)
# |AB|=|CD|, (C+D-A-B).(B-A)=0, U != 0, D-C != +-(B-A), {C,D} != {A,B}.  Bounds from the text: |U|,|dl| <= 80, |c-a| <= 200.
cnt = 0
for a in range(4):
    for U in range(-80, 81):
        if U == 0: continue
        eAB = Y(a + U) - Y(a)
        LAB = U * U + eAB * eAB
        dls = set()
        for e in (0, 2, 4, 6):
            r = LAB - e * e
            if r > 0 and isqrt(r) ** 2 == r: dls.update((isqrt(r), -isqrt(r)))
        for c in range(a - 300, a + 301):
            for dl in dls:
                eCD = Y(c + dl) - Y(c)
                if dl * dl + eCD * eCD != LAB: continue
                if (dl, eCD) in ((U, eAB), (-U, -eAB)): continue
                if {c, c + dl} == {a, a + U}: continue
                Sn = c + (c + dl) - a - (a + U)
                SY = Y(c) + Y(c + dl) - Y(a) - Y(a + U)
                if Sn * U + SY * eAB == 0: cnt += 1
print('(b) filler-only mixed quadruples:', cnt)
# (c) label-filler deep M2a (A2): label C=(0, Yc) with Yc = 0 mod 4; filler D at offset dl.
# Pythagorean: dl^2 + (YD-Yc)^2 = L^2; witnesses at (dl -+ L)/2 must have different heights
# (witness columns that are label columns, i.e. offsets = 0 mod 8 with label height equal, are reported separately).
fails = 0; tot = 0
for Yc in range(-400, 1, 4):          # label heights well below the band
    for dl in range(-6000, 6001):
        if dl == 0: continue
        dY = Y(dl) - Yc
        L2 = dl * dl + dY * dY
        L = isqrt(L2)
        if L * L != L2: continue
        if (dl - L) % 2: continue      # A2 needs integer witness slots
        w1 = (dl - L) // 2; w2 = (dl + L) // 2
        tot += 1
        if Y(w1) == Y(w2):
            mid2 = Yc + Y(dl)          # 2 * midpoint height
            if 2 * Y(w1) != mid2: fails += 1
print('(c) label-filler Pythagorean pairs:', tot, 'with equal witness heights:', fails)
# (d) 2-adic table: for filler pairs at slot distance g with row difference dy=4*dY:
# need v2(dy) <= 3 + v2(g) [no (E;F,F) family] and v2(dy) not in {v2(g)+1, v2(g)+2} [no Pc]
def v2(x):
    x = abs(x); k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k
viol = 0
for n in range(4):
    for g in range(1, 200):
        dy = 4 * (Y(n + g) - Y(n))
        if dy == 0: continue
        if v2(dy) > 3 + v2(g) or v2(dy) in (v2(g) + 1, v2(g) + 2): viol += 1
print('(d) 2-adic violations:', viol)
