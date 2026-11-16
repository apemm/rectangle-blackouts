# Check of the low-p classification: random deep point sets with the L*** row ranges
# (odd labels in [301, T*-321], even labels in [2, T*-321], fillers in [T*-24, T*]),
# NO congruences. Enumerate every mixed quadruple (Lemma mixedeq, p,q in [1,h], AB not
# vertical) with p or q in row <= 2 and record its composition (side | diagonal).
import random
from collections import defaultdict, Counter
def run(h, seed, W=1400):
    rnd = random.Random(seed)
    Ts = h - rnd.randrange(0, 187)
    lo_odd, hi_lab = 301, Ts - 321
    pts = []
    for n in range(W//4):
        if rnd.random() < 0.45:
            yo = rnd.randrange(lo_odd, hi_lab+1) | 1
            if yo > hi_lab: yo -= 2
            ye = 2*rnd.randrange(1, hi_lab//2) if rnd.random() < 0.6 else 2*rnd.randrange(1, 14)
            pts.append((4*n, yo, 'L')); pts.append((4*n, ye, 'L'))
        else:
            pts.append((4*n, Ts - 24 + 8*rnd.randrange(4), 'F'))
    byN = defaultdict(list)
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            a, b = pts[i], pts[j]
            dx = a[0]-b[0]
            if abs(dx) > 1500: continue
            byN[dx*dx + (a[1]-b[1])**2].append((a, b))
    comp = Counter()
    for N, lst in byN.items():
        if len(lst) < 2: continue
        for s in range(len(lst)):
            for d in range(len(lst)):
                if s == d: continue
                A, B = lst[s]; C, D = lst[d]
                if len({A[:2], B[:2], C[:2], D[:2]}) < 4: continue
                for (A, B) in ((lst[s][0], lst[s][1]), (lst[s][1], lst[s][0])):
                    sx = C[0]+D[0]-A[0]-B[0]; sy = C[1]+D[1]-A[1]-B[1]
                    if sx % 2 or sy % 2: continue
                    nx, ny = sx//2, sy//2
                    ux, uy = B[0]-A[0], B[1]-A[1]
                    if (nx, ny) == (0, 0) or ux == 0 or nx*ux + ny*uy: continue
                    if (D[0]-C[0], D[1]-C[1]) in ((ux, uy), (-ux, -uy)): continue
                    py, qy = A[1]+ny, B[1]+ny
                    if not (1 <= py <= h and 1 <= qy <= h): continue
                    if min(py, qy) > 2: continue
                    lowend = A if py <= qy else B
                    other = B if lowend is A else A
                    key = (lowend[2] + other[2] + '|' + ''.join(sorted(C[2]+D[2])),
                           'evenlow' if (lowend[2]=='L' and lowend[1]%2==0) else '')
                    comp[key] += 1; comp[('rows', tuple(sorted((A[1],B[1],C[1],D[1]))))] += 1
                    break
    return comp
tot = Counter()
for seed in range(10):
    tot += run(900, seed)
print(dict(tot))
