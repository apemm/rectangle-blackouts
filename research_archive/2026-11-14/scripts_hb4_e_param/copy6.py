"""Translation-matched 6-cycle: find Y with three legs giving distinct valid gaps (S=32, M=3),
then for those slot sets compute over all T: sum N1N2N3 and sum (N1N2N3)^2 (windows width 8 sqrt(g))."""
import math, random
from collections import defaultdict
from bisect import bisect_left, bisect_right
from pair_corr import vectors
S, M, h = 32, 3, 2 ** 18
V = vectors(S, h)
legsq = defaultdict(list); legsY = defaultdict(list)
for q, Y in V:
    legsq[q].append(Y); legsY[Y].append(q)
def gap(q):
    g = round(q / M); return g if abs(q - M * g) <= M - 1 and g >= 1 else None
def slotlegs(g):
    ys = []
    for q in range(M * g - M + 1, M * g + M):
        ys += legsq.get(q, [])
    return sorted(ys)
found = 0
for Y in sorted(legsY):
    if Y < h // 8: continue
    qs = sorted(legsY[Y])
    if len(qs) < 3: continue
    gs = [gap(q) for q in qs[:3]]
    if None in gs: continue
    g, g1, g2 = gs
    ranks = [0, g, g - g2, g + g1 - g2, g1 - g2, g1]
    if len(set(ranks)) < 6: continue
    sets = [slotlegs(x) for x in (g, g1, g2)]
    ws = [int(8 * math.sqrt(x)) for x in (g, g1, g2)]
    s1 = s2 = 0; good = 0
    for T in range(0, h // 2):
        Y0 = 2 * T + 1
        n = [bisect_right(st, Y0 + w) - bisect_left(st, Y0 - w) for st, w in zip(sets, ws)]
        p = n[0] * n[1] * n[2]
        s1 += p; s2 += p * p
    nY = [bisect_right(st, Y + w) - bisect_left(st, Y - w) for st, w in zip(sets, ws)]
    print(f"Y={Y} legs q={qs[:3]} gaps={gs} ranks={ranks} windows={ws} N at T=(Y-1)/2: {nY}; sum_T N1N2N3={s1}, sum_T (N1N2N3)^2={s2}, range~{min(ws)}")
    found += 1
    if found >= 4: break
