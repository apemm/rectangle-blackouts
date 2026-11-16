"""In-class three-label one-filler mixed quadruples in SAW*: which label triples admit a fourth
point F (solved exactly from Lemma mixedeq) that sits in a deep column with the SAW* filler row of
its slot offset?  Class: slots x = 0 mod 32 (iota = 0, rho0 = 0), odd point (4x, 2x+1),
even point (4x, 2x+1+T).  SAW* rows relative to y_P = 1 (mod 64): offset o -> c_T + 8o with
c_T = 8 if T = 3 (mod 4) and 24 if T = 1 (mod 4).  (Rows are compared mod 64 only: a superset.)
Prints counts by label-type pattern."""
import math, itertools, sys
from collections import Counter

def solve_D(A, B, C):
    # D = A + B - C + 2n, n = k w, w primitive perpendicular to U = B - A, |D - C| = |U|
    ux, uy = B[0] - A[0], B[1] - A[1]
    if ux == 0: return []          # AB vertical: not a mixed quadruple (rival pair instead)
    g = math.gcd(ux, uy); wx, wy = -uy // g, ux // g
    zx, zy = A[0] + B[0] - 2 * C[0], A[1] + B[1] - 2 * C[1]
    # 4|w|^2 k^2 + 4 (z.w) k + |z|^2 - |U|^2 = 0
    a2 = 4 * (wx * wx + wy * wy); a1 = 4 * (zx * wx + zy * wy); a0 = zx * zx + zy * zy - ux * ux - uy * uy
    disc = a1 * a1 - 4 * a2 * a0
    out = []
    if disc < 0: return out
    s = math.isqrt(disc)
    if s * s != disc: return out
    for num in {-a1 + s, -a1 - s}:
        if num % (2 * a2): continue
        k = num // (2 * a2)
        if k == 0: continue
        D = (A[0] + B[0] - C[0] + 2 * k * wx, A[1] + B[1] - C[1] + 2 * k * wy)
        if (D[0] - C[0], D[1] - C[1]) in ((ux, uy), (-ux, -uy)): continue
        out.append(D)
    return out

def solve_A(B, C, D):
    # A = F = P1 - 2n, P1 = C + D - B, W = B - P1, n.W = -2|n|^2, |n|^2 = (|W|^2 - |D-C|^2)/4
    P1 = (C[0] + D[0] - B[0], C[1] + D[1] - B[1]); W = (B[0] - P1[0], B[1] - P1[1])
    L2 = (D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2; W2 = W[0] ** 2 + W[1] ** 2
    if (W2 - L2) % 4: return []
    N2 = (W2 - L2) // 4
    if N2 <= 0: return []
    out = []
    r = math.isqrt(N2)
    for nx in range(-r, r + 1):
        rem = N2 - nx * nx; t = math.isqrt(rem)
        if t * t != rem: continue
        for ny in {t, -t}:
            if nx * W[0] + ny * W[1] != -2 * N2: continue
            A = (P1[0] - 2 * nx, P1[1] - 2 * ny)
            if A[0] == B[0]: continue
            if (D[0] - C[0], D[1] - C[1]) in ((B[0] - A[0], B[1] - A[1]), (A[0] - B[0], A[1] - B[1])): continue
            out.append(A)
    return out

def run(T, nslots, rmax):
    cT = 8 if T % 4 == 3 else 24
    pts = []
    for k in range(nslots):
        x = 32 * k
        pts.append(('o', (4 * x, 2 * x + 1)))
        pts.append(('e', (4 * x, 2 * x + 1 + T)))
    match = Counter(); tot = Counter()
    for (t1, P), (t2, Q), (t3, R) in itertools.permutations(pts, 3):
        for role, Fs in (('diag', solve_D(P, Q, R)), ('side', solve_A(P, Q, R) if rmax else [])):
            for F in Fs:
                if F[0] % 4: continue
                o = (F[0] // 4) % 4
                key = (role, ''.join(sorted(t1 + t2 + t3)))
                tot[key] += 1
                if (F[1] - 1 - cT - 8 * o) % 64 == 0: match[key] += 1
    return tot, match

for T in (3, 35, 67, 99, 1, 33, 65, 97, 13, 45, 29, 61):
    tot, match = run(T, 14, 1)
    print("T", T, "deep-column solutions", dict(tot), "matching a SAW* filler row mod 64:", dict(match))
    sys.stdout.flush()
