import itertools
from math import isqrt
def v2(x):
    x = abs(x); k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k
P = 8
holes = [y for y in range(-18, 19) if y % 4 == 2]
bases = [y for y in range(-18, 19) if y % 4 == 0]
res = []
for h2, h4, h6 in itertools.product(holes, repeat=3):
    for b1, b3, b5, b7 in itertools.product(bases, repeat=4):
        H = [-2, b1, h2, b3, h4, b5, h6, b7]
        if max(H) - min(H) > 16: continue
        if b1 == b7 or b3 == b5: continue
        Y = lambda n: H[n % P]
        ok = True
        for n in range(P):
            for g in range(1, 9):
                dy = 4 * (Y(n + g) - Y(n))
                if dy and (v2(dy) > 3 + v2(g) or v2(dy) in (v2(g) + 1, v2(g) + 2)): ok = False; break
            if not ok: break
        if not ok: continue
        # T2 quick
        t2 = 0
        for Yc in range(-400, -40, 4):
            for t in range(1, 60):
                Hh = Yc + 10 * t
                for sg in (1, -1):
                    if Y(-sg * 10 * t) == Hh and Y(-sg * 6 * t) == Hh: t2 += 1
        if t2: continue
        # right angles quick
        bad = 0
        for v in range(P):
            for a1 in range(-40, 41):
                e1 = Y(v + a1) - Y(v)
                if a1 == 0 or e1 == 0: continue
                for a2 in range(-40, 41):
                    e2 = Y(v + a2) - Y(v)
                    if a2 and e2 and a1 * a2 + e1 * e2 == 0: bad += 1
        if bad: continue
        hs = sorted(set(H)); diffs = sorted(set(abs(x - y) for x in hs for y in hs if x != y))
        t1 = 0
        for Yc in range(-400, -40, 4):
            for e in diffs + [-d for d in diffs]:
                for delta in (e, -e):
                    YD = Y(delta); dY = YD - Yc
                    for U, k in ((-dY, e), (dY, -e)):
                        if (delta - U + k) % 2: continue
                        a = (delta - U + k) // 2
                        if Y(a + U) - Y(a) == e and Y(a) + Y(a + U) == 2 * YD: t1 += 1
        if t1: continue
        res.append((max(H) - min(H), len(set(H)), H))
res.sort()
print(len(res))
for r in res[:40]: print(r)
