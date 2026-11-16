# Geometric sanity check of the 3L1F norm lemma on synthetic point sets that obey
# exactly the L*** congruences (label columns 4*rho0 mod 16, odd rows y_P mod 64,
# even rows E0 mod 32, filler at offset o in row T*-24+8o), with random geometry.
# Every hit is verified from Lemma mixedeq. Control: filler rows decoupled from offsets.
import random, sys
from collections import defaultdict
def run(h, iota, sigma, rho0, seed, coupled):
    rnd = random.Random(seed)
    yP = 2*iota + 1; T0 = 2*sigma + 1
    c = 1 if T0 % 4 == 3 else 3
    # T*: largest y <= h with y = yP + 8 + 8*... rule: f_o = yP + 8(o+c) mod 64
    Tst = max(y for y in range(h-80, h+1) if (y - 24 - yP - 8*c) % 64 == 0)
    W = 2400
    labels = []
    for n in range(0, W//4):
        if (n - rho0) % 4 == 0 and rnd.random() < 0.5:
            # random label: odd row and even row with the congruences, rows in [2, Tst-40]
            yo = rnd.choice([y for y in range(1, Tst-40) if (y - yP) % 64 == 0])
            ye = rnd.choice([y for y in range(2, Tst-40) if (y - yP - T0) % 32 == 0])
            labels.append((4*n, yo, 'o')); labels.append((4*n, ye, 'e'))
    lab_cols = {x for x, _, _ in labels}
    fillers = []
    for n in range(0, W//4):
        if 4*n in lab_cols: continue
        o = (n - rho0) % 4
        if not coupled: o = rnd.randrange(4)
        fillers.append((4*n, Tst - 24 + 8*o, 'F'))
    pts = labels + fillers
    black = {(x, y) for x, y, _ in pts}
    kind = {(x, y): k for x, y, k in pts}
    LL = defaultdict(list); LF = defaultdict(list)
    L = [(x, y) for x, y, _ in labels]; F = [(x, y) for x, y, _ in fillers]
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            a, b = L[i], L[j]
            LL[(a[0]-b[0])**2 + (a[1]-b[1])**2].append((a, b))
    for a in L:
        for b in F:
            if abs(a[0]-b[0]) > 600: continue
            LF[(a[0]-b[0])**2 + (a[1]-b[1])**2].append((a, b))
    common = set(LL) & set(LF)
    hits = 0
    for N in common:
        for P in LL[N]:
            for Q in LF[N]:
                for side, diag in ((P, Q), (Q, P)):
                    (A, B), (C, D) = side, diag
                    for (A, B) in (side, side[::-1]):
                        sx = C[0] + D[0] - A[0] - B[0]; sy = C[1] + D[1] - A[1] - B[1]
                        if sx % 2 or sy % 2: continue
                        nx, ny = sx//2, sy//2
                        if (nx, ny) == (0, 0): continue
                        ux, uy = B[0]-A[0], B[1]-A[1]
                        if ux == 0: continue
                        if nx*ux + ny*uy != 0: continue
                        vx, vy = D[0]-C[0], D[1]-C[1]
                        if (vx, vy) in ((ux, uy), (-ux, -uy)): continue
                        p = (A[0]+nx, A[1]+ny); q = (B[0]+nx, B[1]+ny)
                        if not (1 <= p[1] <= h and 1 <= q[1] <= h): continue
                        hits += 1
    return hits, len(labels)//2, len(fillers)
for coupled in (True, False):
    tot = 0
    for seed, (iota, sigma, rho0) in enumerate([(2,3,1),(6,8,2),(10,1,3),(4,13,0),(0,7,1),(14,10,2)]):
        hts, nl, nf = run(400, iota, sigma, rho0, seed, coupled)
        tot += hts
    print("coupled" if coupled else "control (decoupled)", "3L1F hits:", tot)
