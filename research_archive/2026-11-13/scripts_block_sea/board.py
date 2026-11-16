"""Brute-force obstruction finder for one stride-4 block plus a row-1 sea.

Board: columns 0..m-1, rows 1..h. cols[x] = list of (row, tag).
Tags: ('S',) row-1 sea point; ('F',) filler; ('O',k) odd point of label k;
('E',k) even point of label k.
Criterion (equality board, parity bipartition): see notes in the write-up.
 V1 fully black tilted rectangle
 V2 three black corners, white corner W fatal iff column of W has a black
    point of the other parity than row(W)
 V3 two parked triples at the same W
 V4 black support of a mixed pair with non-vertical side AB
 V5 rival pair
"""
from math import gcd, isqrt
from collections import defaultdict


def Wh(h):
    return (h - 1) ** 2 // 4 + 1


def build(h, T, slots, filler, margin, nslots=None):
    """One class of offset T at stride 4; slot i at column base+4i.
    slots: set of occupied slots i (label (i, i+s)).
    filler(i, x): row of the filler at slot i (empty slot) or None for
    no filler (white column; for experiments).
    Columns = 0 mod 4 outside the block: filler(None, x)."""
    s = (T - 1) // 2
    A = (h + 1) // 2
    if nslots is None:
        nslots = A
    base = margin - margin % 4
    m = base + 4 * nslots + margin
    cols = [[] for _ in range(m)]
    labels = {}
    for x in range(m):
        if x % 4:
            cols[x].append((1, ('S',)))
            continue
        i = (x - base) // 4
        if 0 <= i < nslots and i in slots:
            j = i + s
            assert 0 <= j < h // 2
            labels[i] = (i, j)
            cols[x].append((2 * i + 1, ('O', i)))
            cols[x].append((2 * j + 2, ('E', i)))
        else:
            r = filler(i if 0 <= i < nslots else None, x)
            if r is not None:
                cols[x].append((r, ('F',)))
    return cols, labels, base


def black_map(cols):
    bm = {}
    for x, c in enumerate(cols):
        for (r, t) in c:
            bm[(x, r)] = t
    return bm


def tilted_triples(cols, h):
    """All tilted rectangles with >= 3 black corners, as frozensets."""
    m = len(cols)
    bm = black_map(cols)
    W = Wh(h)
    pts = list(bm.keys())
    seen = set()
    out = []
    for V in pts:
        vx, vy = V
        for dx in range(-W, W + 1):
            if dx == 0:
                continue
            x = vx + dx
            if x < 0 or x >= m:
                continue
            for (r, t) in cols[x]:
                dy = r - vy
                if dy == 0:
                    continue
                g = gcd(abs(dx), abs(dy))
                wx, wy = -dy // g, dx // g
                for lam in range(-h, h + 1):
                    if lam == 0:
                        continue
                    Q = (vx + lam * wx, vy + lam * wy)
                    if not (1 <= Q[1] <= h and 0 <= Q[0] < m):
                        continue
                    R = (x + lam * wx, r + lam * wy)
                    if not (1 <= R[1] <= h and 0 <= R[0] < m):
                        continue
                    if Q not in bm:
                        continue
                    key = frozenset([V, (x, r), Q, R])
                    if key in seen:
                        continue
                    seen.add(key)
                    out.append(key)
    return out, bm


def classify_triples(cols, h):
    rects, bm = tilted_triples(cols, h)
    fatal = []
    parked = defaultdict(list)
    for key in rects:
        black = [P for P in key if P in bm]
        white = [P for P in key if P not in bm]
        if len(white) == 0:
            fatal.append(('V1', key, None))
            continue
        Wp = white[0]
        x, rho = Wp
        own = any((r - rho) % 2 for (r, t) in cols[x])
        if not cols[x]:
            own = (rho % 2 == 0)  # empty column stands for an odd filler
        if own:
            fatal.append(('V2', key, Wp))
        else:
            parked[Wp].append(key)
    return fatal, parked, bm


_REP = {}


def reps(L2):
    if L2 not in _REP:
        r = []
        a = isqrt(L2)
        for zx in range(-a, a + 1):
            rem = L2 - zx * zx
            zy = isqrt(rem)
            if zy * zy == rem:
                for zz in {zy, -zy}:
                    r.append((zx, zz))
        _REP[L2] = r
    return _REP[L2]


def mixed_quadruples(cols, h):
    """Supports {A,B,C,D} of mixed pairs, AB not vertical, all black."""
    m = len(cols)
    bm = black_map(cols)
    W = Wh(h)
    pts = list(bm.keys())
    out = set()
    for A in pts:
        ax, ay = A
        for dx in range(0, 2 * W + 2):
            x = ax + dx
            if x >= m:
                break
            for (r, t) in cols[x]:
                B = (x, r)
                if B == A or dx == 0:
                    continue  # AB not vertical; dx>0 orders the pair
                ux, uy = dx, r - ay
                g = gcd(abs(ux), abs(uy))
                nx0, ny0 = -uy // g, ux // g
                for lam in range(-h, h + 1):
                    if lam == 0:
                        continue
                    nx, ny = lam * nx0, lam * ny0
                    p = (ax + nx, ay + ny)
                    q = (x + nx, r + ny)
                    if not (1 <= p[1] <= h and 1 <= q[1] <= h):
                        continue
                    if not (0 <= p[0] < m and 0 <= q[0] < m):
                        continue
                    sx, sy = p[0] + q[0], p[1] + q[1]
                    L2 = ux * ux + uy * uy
                    # z = 2C - (p+q), |z|^2 = L2, z = (sx,sy) mod 2
                    for (zx, zyy) in reps(L2):
                        if True:
                            if True:
                                if (zx - sx) % 2 or (zyy - sy) % 2:
                                    continue
                                if (zx, zyy) in ((ux, uy), (-ux, -uy)):
                                    continue
                                C = ((sx + zx) // 2, (sy + zyy) // 2)
                                D = ((sx - zx) // 2, (sy - zyy) // 2)
                                if C in bm and D in bm:
                                    if not (1 <= C[1] <= h and 1 <= D[1] <= h):
                                        continue
                                    sup = frozenset([A, B, C, D])
                                    if len(sup) == 4:
                                        out.add((sup, (A, B, C, D)))
    return out, bm


def rival_pairs(cols, h):
    bm = black_map(cols)
    pts = list(bm.keys())
    out = []
    for C in pts:
        for D in pts:
            if C >= D:
                continue
            c, c2 = C[1], D[1]
            if c > c2:
                c, c2 = c2, c
            d = c2 - c
            if d % 2 == 0:
                continue
            t = C[0] - D[0]
            if t == 0:
                continue
            for j in range(1, h):
                if c - j < 1 or c2 + j > h:
                    break
                if 4 * j * (d + j) == t * t:
                    out.append((C, D, j))
    return out, bm


def tagset(points, bm):
    return tuple(sorted(str(bm[P]) for P in points if P in bm))
