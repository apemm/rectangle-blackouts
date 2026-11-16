"""Local checks for a periodic filler pattern H (Y units, offset 0 = label residue, period P = len(H)).
Prints counts of: (a) filler right angles, (b) filler-only mixed quadruples, (c) label-filler A2 pairs
with equal witness heights, (d) 2-adic violations, (e) T1 instances, (f) T2 (45-degree) instances,
(g) filler-filler Pythagorean pairs with equal witness heights (A2 among fillers)."""
import sys
from math import isqrt
H = [int(a) for a in sys.argv[1].split(',')]; P = len(H)
Y = lambda n: H[n % P]
def v2(x):
    x = abs(x); k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k
out = {}
# (a)
bad = 0
for v in range(P):
    for a1 in range(-120, 121):
        e1 = Y(v + a1) - Y(v)
        if a1 == 0 or e1 == 0: continue
        for a2 in range(-120, 121):
            e2 = Y(v + a2) - Y(v)
            if a2 and e2 and a1 * a2 + e1 * e2 == 0: bad += 1
out['a_rightangles'] = bad
# (b)
hs = sorted(set(H)); diffs = sorted(set(abs(x - y) for x in hs for y in hs))
cnt = 0
for a in range(P):
    for U in range(-200, 201):
        if U == 0: continue
        eAB = Y(a + U) - Y(a); LAB = U * U + eAB * eAB
        dls = set()
        for e in diffs:
            r = LAB - e * e
            if r > 0 and isqrt(r) ** 2 == r: dls.update((isqrt(r), -isqrt(r)))
        for c in range(a - 600, a + 601):
            for dl in dls:
                eCD = Y(c + dl) - Y(c)
                if dl * dl + eCD * eCD != LAB or (dl, eCD) in ((U, eAB), (-U, -eAB)) or {c, c + dl} == {a, a + U}: continue
                if (2 * c + dl - 2 * a - U) * U + (Y(c) + Y(c + dl) - Y(a) - Y(a + U)) * eAB == 0: cnt += 1
out['b_fillerquads'] = cnt
# (c) label at offset 0 with Yc = 0 mod 4, far below; D filler at offset dl
fails = 0
for Yc in range(-600, -40, 4):
    for dl in range(-8000, 8001):
        if dl == 0: continue
        dY = Y(dl) - Yc; L2 = dl * dl + dY * dY; L = isqrt(L2)
        if L * L != L2 or (dl - L) % 2: continue
        w1 = (dl - L) // 2; w2 = (dl + L) // 2
        if Y(w1) == Y(w2) and 2 * Y(w1) != Yc + Y(dl): fails += 1
out['c_labelfillerA2'] = fails
# (d)
viol = 0
for n in range(P):
    for g in range(1, 400):
        dy = 4 * (Y(n + g) - Y(n))
        if dy and (v2(dy) > 3 + v2(g) or v2(dy) in (v2(g) + 1, v2(g) + 2)): viol += 1
out['d_2adic'] = viol
# (e) T1: label C at offset 0, D = C + delta with delta = +-e, e = Y_B - Y_A, 2Y_D = Y_A + Y_B,
# A at a, B at a + U, U = +-dY (dY = Y_D - Y_C), 2a = 2c + delta - U + k, k = -+e (U = -dY <-> k = e).
t1 = 0
for Yc in range(-600, -40, 4):
    for e in [d for d in diffs if d] + [-d for d in diffs if d]:
        for delta in (e, -e):
            YD = Y(delta); dY = YD - Yc
            for U, k in ((-dY, e), (dY, -e)):
                if (delta - U + k) % 2: continue
                a = (delta - U + k) // 2
                if Y(a + U) - Y(a) == e and Y(a) + Y(a + U) == 2 * YD: t1 += 1
out['e_T1'] = t1
# (f) T2 (45-degree family and its mirror): A label (offset 0), e1 = 10t, B at -+10t, D at -+6t, both height Ya + 10t.
t2 = 0
for Yc in range(-600, -40, 4):
    for t in range(-200, 201):
        if t == 0: continue
        Hh = Yc + 10 * t
        for sg in (1, -1):
            if Y(-sg * 10 * t) == Hh and Y(-sg * 6 * t) == Hh: t2 += 1
out['f_T2'] = t2
# (g) filler-filler A2
g = 0
for c in range(P):
    for dl in range(-3000, 3001):
        if dl == 0: continue
        dY = Y(c + dl) - Y(c)
        if dY == 0: continue
        L2 = dl * dl + dY * dY; L = isqrt(L2)
        if L * L != L2 or (dl - L) % 2: continue
        w1 = c + (dl - L) // 2; w2 = c + (dl + L) // 2
        if Y(w1) == Y(w2) and 2 * Y(w1) != Y(c) + Y(c + dl): g += 1
out['g_fillerA2'] = g
print(H, out)
