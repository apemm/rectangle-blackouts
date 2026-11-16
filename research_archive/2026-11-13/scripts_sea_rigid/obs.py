# Obstruction finder from the definitions (criterion V1-V5), for small boards.
# Points are (x, y), y in 1..h. Black set given as a set of tuples.
from math import gcd, isqrt
from collections import defaultdict

def colmap(S):
    c = defaultdict(list)
    for (x, y) in S:
        c[x].append(y)
    return c

def triples(S, h):
    """All tilted rectangles with >= 3 black corners.
    Returns list of (kind, V, P1, P2, W) with kind in {'V1','fatal','parked'}."""
    cols = colmap(S)
    pts = sorted(S)
    seen = set()
    out = []
    for V in pts:
        for P1 in pts:
            dx, dy = P1[0] - V[0], P1[1] - V[1]
            if dx == 0 or dy == 0:
                continue
            g = gcd(abs(dx), abs(dy))
            wx, wy = -dy // g, dx // g   # perpendicular primitive
            for k in range(-h, h + 1):
                if k == 0:
                    continue
                P2 = (V[0] + k * wx, V[1] + k * wy)
                if not (1 <= P2[1] <= h):
                    continue
                if P2 not in S:
                    continue
                W = (P1[0] + P2[0] - V[0], P1[1] + P2[1] - V[1])
                if not (1 <= W[1] <= h):
                    continue
                key = frozenset([V, P1, P2, W])
                if key in seen:
                    continue
                seen.add(key)
                if W in S:
                    out.append(('V1', V, P1, P2, W))
                    continue
                # W white: V is the corner opposite W
                par = W[1] % 2
                bad = any((y % 2) != par for y in cols.get(W[0], []))
                out.append(('fatal' if bad else 'parked', V, P1, P2, W))
    return out

def mixed(S, h):
    """Mixed quadruples (A,B,C,D): AB side (not vertical), CD diagonal."""
    pts = sorted(S)
    idx = defaultdict(list)
    n = len(pts)
    for a in range(n):
        for b in range(a + 1, n):
            C, D = pts[a], pts[b]
            s = (C[0] + D[0], C[1] + D[1])
            L = (D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2
            idx[(s, L)].append((C, D))
    out = []
    seen = set()
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            A, B = pts[a], pts[b]
            ux, uy = B[0] - A[0], B[1] - A[1]
            if ux == 0:
                continue
            if (ux, uy) < (0, 0) and False:
                pass
            g = gcd(abs(ux), abs(uy))
            wx, wy = -uy // g, ux // g
            L = ux * ux + uy * uy
            for k in range(-2 * h, 2 * h + 1):
                if k == 0:
                    continue
                nx, ny = k * wx, k * wy
                p = (A[0] + nx, A[1] + ny)
                q = (B[0] + nx, B[1] + ny)
                if not (1 <= p[1] <= h and 1 <= q[1] <= h):
                    continue
                s = (A[0] + B[0] + 2 * nx, A[1] + B[1] + 2 * ny)
                for (C, D) in idx.get((s, L), []):
                    if len({A, B, C, D}) < 4:
                        continue
                    if (D[0] - C[0], D[1] - C[1]) in ((ux, uy), (-ux, -uy)):
                        continue
                    if C in (p, q) or D in (p, q):
                        continue
                    key = (frozenset([A, B]), frozenset([C, D]), frozenset([p, q]))
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append((A, B, C, D, p, q))
    return out

def rivals(S, h):
    pts = sorted(S)
    out = []
    for a in range(len(pts)):
        for b in range(a + 1, len(pts)):
            C, D = pts[a], pts[b]
            if C[1] > D[1]:
                C, D = D, C
            c, cp = C[1], D[1]
            d = cp - c
            if d % 2 == 0:
                continue
            t = C[0] - D[0]
            if t == 0 or t % 2:
                continue
            for j in range(1, h):
                if c - j < 1 or cp + j > h:
                    break
                if 4 * j * (d + j) == t * t:
                    out.append((C, D, j))
    return out

def v3(tr):
    cnt = defaultdict(list)
    for t in tr:
        if t[0] == 'parked':
            cnt[t[4]].append(t)
    return {W: v for W, v in cnt.items() if len(v) >= 2}
