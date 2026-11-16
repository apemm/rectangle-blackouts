# Lemma 1 check, version 2: generate genuine mixed supports with one sea point
# (two label columns 0 and X, one free sea column xi), then count ALL (X, xi)
# solutions for the same rows and role by brute force over a grid.
import numpy as np, math, random
random.seed(7)
R = 300
Xs = np.arange(-R, R + 1)
GX, GXI = np.meshgrid(Xs, Xs, indexing="ij")

def count(role, rows):
    a, b, c, d, s = rows
    Z = 0 * GX
    P = {"a": (Z, a + Z), "b": (Z, b + Z), "c": (GX, c + Z), "d": (GX, d + Z), "s": (GXI, s + Z)}
    A, B, C, D = (P[k] for k in role.replace("|", ""))
    u1, u2 = B[0] - A[0], B[1] - A[1]; w1, w2 = D[0] - C[0], D[1] - C[1]
    z1, z2 = C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1]
    ok = (u1 * u1 + u2 * u2 == w1 * w1 + w2 * w2) & (u1 * z1 + u2 * z2 == 0)
    ok &= (GX != 0) & (GXI != 0) & (GXI != GX) & (u1 != 0)
    ok &= ~((w1 == u1) & (w2 == u2)) & ~((w1 == -u1) & (w2 == -u2))
    return int(ok.sum())

def supports():
    # A=(0,ya); u=B-A; n = m*(-u2,u1)/g; w = D-C with |w|=|u|; C=(A+B+2n-w)/2
    for _ in range(200000):
        u1 = random.randint(-60, 60); u2 = random.randint(-40, 40)
        if u1 == 0: continue
        g = math.gcd(u1, u2); m = random.randint(-6, 6)
        n1, n2 = -m * u2 // g, m * u1 // g
        N = u1 * u1 + u2 * u2
        for w1 in range(-int(math.isqrt(N)), int(math.isqrt(N)) + 1):
            r = N - w1 * w1; w2 = math.isqrt(r)
            if w2 * w2 != r: continue
            for w2s in {w2, -w2}:
                if (w1, w2s) in {(u1, u2), (-u1, -u2)}: continue
                cx2, cy2 = u1 + 2 * n1 - w1, u2 + 2 * n2 - w2s
                if cx2 % 2 or cy2 % 2: continue
                yield (u1, u2), (cx2 // 2, cy2 // 2), (w1, w2s)

found = {"ac|bs": [], "as|bc": [], "ac|ds": [], "as|cd": []}
ya = 50
for (u1, u2), (cx, cy), (w1, w2) in supports():
    A = (0, ya); B = (u1, ya + u2); C = (cx, ya + cy); D = (cx + w1, ya + cy + w2)
    pts = [A, B, C, D]
    if len(set(pts)) < 4 or any(not (1 <= p[1] <= 200) for p in pts): continue
    rows_sets = []
    if C[0] == 0 and B[0] != 0 and D[0] not in (0, B[0]):   # ac|bs : a=A,c=B,b=C,s=D
        rows_sets.append(("ac|bs", (A[1], C[1], B[1], 999, D[1])))
    if C[0] == 0 and D[0] != 0 and B[0] not in (0, D[0]):   # as|bc : a=A,s=B,b=C,c=D
        rows_sets.append(("as|bc", (A[1], C[1], D[1], 999, B[1])))
    if C[0] == B[0] != 0 and D[0] not in (0, B[0]):         # ac|ds : a=A,c=B,d=C,s=D
        rows_sets.append(("ac|ds", (A[1], 999, B[1], C[1], D[1])))
    if C[0] == D[0] != 0 and B[0] not in (0, C[0]):         # as|cd : a=A,s=B,c=C,d=D
        rows_sets.append(("as|cd", (A[1], 999, C[1], D[1], B[1])))
    for role, rows in rows_sets:
        if len(found[role]) < 12 and abs(B[0]) <= R and abs(D[0]) <= R and abs(C[0]) <= R:
            found[role].append(rows)
    if all(len(v) >= 12 for v in found.values()): break
for role, lst in found.items():
    counts = [count(role, r) for r in lst]
    print(role, "instances", len(lst), "solution counts", counts)
