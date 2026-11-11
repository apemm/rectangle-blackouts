"""Rectangle kernels for the square-grid experiments (10 November 2026).

Cells are indexed r * m + c with 0 <= r < h (row) and 0 <= c < m (column).

Three separate pieces of code live here.

1. rects_by_sides(h, m): every lattice rectangle once, from a corner and two
   perpendicular side vectors. Used by the SAT encoder and by the small
   brute-force cross-check of the counters.

2. verify_board(h, m, black): the independent validity check. It enumerates
   rectangles as pairs of equal-length segments with a common midpoint (the two
   diagonals) and tests injectivity of the presentation map directly. It shares
   no code with (1) or (3).

3. Collision counters (process_cell and helpers): incremental tallies of
     n_P  = number of rectangles R containing the pair P with R minus P black,
     t_p  = number of rectangles R containing the point p with R minus p black,
   and the totals
     M4 = sum over pairs P of C(n_P, 2)     (four-cell collisions),
     M6 = sum over points p of C(t_p, 2)    (six-cell collisions),
     RA = number of black right angles, RAin = those whose fourth corner lies
          in the grid.
   A set is valid exactly when M4 = M6 = 0 and at most one rectangle is fully
   black: two distinct rectangles share at most two corners, and the three
   cases (two, one, none) give a pair with n_P >= 2, a point with t_p >= 2, or
   two fully black rectangles.
"""
from math import gcd

import numpy as np
from numba import njit


# --------------------------------------------------------------------------
# 1. side-vector enumeration (pure Python)

def rects_by_sides(h, m):
    out = []
    for dx in range(1, max(h, m)):
        for dy in range(0, max(h, m)):
            if gcd(dx, dy) != 1:
                continue
            # direction d = (dx, dy) in (column, row); perpendicular e = (-dy, dx)
            s = 1
            while s * dx < m and s * dy < h:
                t = 1
                while t * dy < m and t * dx < h:
                    ax, ay = s * dx, s * dy
                    bx, by = -t * dy, t * dx
                    xs = (0, ax, ax + bx, bx)
                    ys = (0, ay, ay + by, by)
                    x0, x1 = -min(xs), m - 1 - max(xs)
                    y0, y1 = -min(ys), h - 1 - max(ys)
                    for px in range(x0, x1 + 1):
                        for py in range(y0, y1 + 1):
                            out.append(tuple(sorted((py + ys[i]) * m + px + xs[i] for i in range(4))))
                    t += 1
                s += 1
    return out


# --------------------------------------------------------------------------
# 2. independent verifier: diagonals with a common midpoint

@njit(cache=True)
def _verify(h, m, black, full):
    NN = h * m
    base = NN + 1
    keys = [np.int64(-1)]
    nrect = 0
    seg_a = np.empty(NN, np.int64)
    seg_b = np.empty(NN, np.int64)
    seg_l = np.empty(NN, np.int64)
    vis = np.empty(4, np.int64)
    for sx in range(0, 2 * (m - 1) + 1):
        for sy in range(0, 2 * (h - 1) + 1):
            k = 0
            for y in range(max(0, sy - (h - 1)), min(h - 1, sy) + 1):
                y2 = sy - y
                for x in range(max(0, sx - (m - 1)), min(m - 1, sx) + 1):
                    x2 = sx - x
                    if y < y2 or (y == y2 and x < x2):
                        seg_a[k] = y * m + x
                        seg_b[k] = y2 * m + x2
                        seg_l[k] = (x - x2) * (x - x2) + (y - y2) * (y - y2)
                        k += 1
            if k < 2:
                continue
            order = np.argsort(seg_l[:k])
            i = 0
            while i < k:
                j = i
                while j < k and seg_l[order[j]] == seg_l[order[i]]:
                    j += 1
                for u in range(i, j):
                    a1 = seg_a[order[u]]
                    b1 = seg_b[order[u]]
                    for v in range(u + 1, j):
                        a2 = seg_a[order[v]]
                        b2 = seg_b[order[v]]
                        nrect += 1
                        nb = black[a1] + black[b1] + black[a2] + black[b2]
                        if nb < 2 and not full:
                            continue
                        nv = 0
                        if not black[a1]:
                            vis[nv] = a1 + 1
                            nv += 1
                        if not black[b1]:
                            vis[nv] = b1 + 1
                            nv += 1
                        if not black[a2]:
                            vis[nv] = a2 + 1
                            nv += 1
                        if not black[b2]:
                            vis[nv] = b2 + 1
                            nv += 1
                        # sort the visible corners (at most four values)
                        for p in range(1, nv):
                            q = p
                            while q > 0 and vis[q - 1] > vis[q]:
                                tmp = vis[q]
                                vis[q] = vis[q - 1]
                                vis[q - 1] = tmp
                                q -= 1
                        key = np.int64(0)
                        for p in range(nv):
                            key = key * base + vis[p]
                        # separate presentations of different sizes
                        key = key * 5 + nv
                        keys.append(key)
                i = j
    arr = np.array(keys[1:], dtype=np.int64)
    arr.sort()
    coll = 0
    for i in range(1, arr.size):
        if arr[i] == arr[i - 1]:
            coll += 1
    return nrect, arr.size, coll


def verify_board(h, m, cells, full=None):
    """Return (valid, rectangles, presentations compared, collisions).

    full=True compares the presentations of all rectangles. full=False keeps
    only rectangles with two or more black corners; this loses nothing, since
    two rectangles with the same presentation share at most two corners, so
    each has at least two black corners. Default: full when the grid has at
    most 4096 cells.
    """
    black = np.zeros(h * m, np.uint8)
    for v in cells:
        black[v] = 1
    if full is None:
        full = h * m <= 4096
    nrect, nkeys, coll = _verify(h, m, black, full)
    return coll == 0, int(nrect), int(nkeys), int(coll)


def verify_plain(h, m, cells):
    """Plain Python version of the same check, all rectangles, for small grids."""
    S = set(cells)
    seen = set()
    groups = {}
    for a in range(h * m):
        ya, xa = divmod(a, m)
        for b in range(a + 1, h * m):
            yb, xb = divmod(b, m)
            groups.setdefault((xa + xb, ya + yb, (xa - xb) ** 2 + (ya - yb) ** 2), []).append((a, b))
    n = 0
    ok = True
    for segs in groups.values():
        for i in range(len(segs)):
            for j in range(i + 1, len(segs)):
                n += 1
                pres = frozenset(segs[i] + segs[j]) - S
                if pres in seen:
                    ok = False
                seen.add(pres)
    return ok, n


# --------------------------------------------------------------------------
# 3. incremental collision counters

@njit(cache=True)
def _isqrt(n):
    s = np.int64(np.sqrt(np.float64(n)))
    while s * s > n:
        s -= 1
    while (s + 1) * (s + 1) <= n:
        s += 1
    return s


@njit(cache=True)
def _gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


@njit(cache=True)
def _bump_pair(nP, tot, NN, c, e, sign):
    if c < e:
        key = c * NN + e
    else:
        key = e * NN + c
    if sign > 0:
        tot[0] += nP[key]
        nP[key] += 1
    else:
        nP[key] -= 1
        tot[0] -= nP[key]


@njit(cache=True)
def _bump_point(tp, tot, p, sign):
    if sign > 0:
        tot[1] += tp[p]
        tp[p] += 1
    else:
        tp[p] -= 1
        tot[1] -= tp[p]


@njit(cache=True)
def process_cell(h, m, black, blist, nb, nP, tp, tot, x, sign):
    """Add (sign=+1) or subtract (sign=-1) every tally that involves cell x and
    the black cells listed in blist[:nb]; x itself must not be in the list."""
    NN = h * m
    xr = x // m
    xc = x % m
    for ib in range(nb):
        b = blist[ib]
        br = b // m
        bc = b % m
        dr = br - xr
        dc = bc - xc
        g = _gcd(dr, dc)
        ur = -dc // g
        uc = dr // g
        # rectangles with side {x, b}
        for sg in (1, -1):
            t = 1
            while True:
                cr = xr + sg * t * ur
                cc = xc + sg * t * uc
                er = br + sg * t * ur
                ec = bc + sg * t * uc
                if cr < 0 or cr >= h or cc < 0 or cc >= m or er < 0 or er >= h or ec < 0 or ec >= m:
                    break
                _bump_pair(nP, tot, NN, cr * m + cc, er * m + ec, sign)
                t += 1
        # rectangles with diagonal {x, b}: v . (d - v) = 0
        L2 = dr * dr + dc * dc
        L = _isqrt(L2)
        lo = (dr - L - 2) // 2
        hi = (dr + L + 2) // 2 + 1
        for vr in range(lo, hi + 1):
            disc = dc * dc - 4 * (vr * vr - dr * vr)
            if disc < 0:
                continue
            s = _isqrt(disc)
            if s * s != disc or ((dc + s) & 1):
                continue
            for k in range(2):
                if k == 1 and s == 0:
                    break
                vc = (dc + s) // 2 if k == 0 else (dc - s) // 2
                if (vr == 0 and vc == 0) or (vr == dr and vc == dc):
                    continue
                cr = xr + vr
                cc = xc + vc
                er = br - vr
                ec = bc - vc
                if cr < 0 or cr >= h or cc < 0 or cc >= m or er < 0 or er >= h or ec < 0 or ec >= m:
                    continue
                c = cr * m + cc
                e = er * m + ec
                if c < e:
                    _bump_pair(nP, tot, NN, c, e, sign)
        # right angles with vertex x, arms b and c, c counterclockwise from b
        t = 1
        while True:
            cr = xr + t * ur
            cc = xc + t * uc
            if cr < 0 or cr >= h or cc < 0 or cc >= m:
                break
            if black[cr * m + cc]:
                pr = br + cr - xr
                pc = bc + cc - xc
                tot[2] += sign
                if 0 <= pr < h and 0 <= pc < m:
                    tot[3] += sign
                    _bump_point(tp, tot, pr * m + pc, sign)
            t += 1
        # right angles with vertex b, arms x and c
        for sg in (1, -1):
            t = 1
            while True:
                cr = br + sg * t * ur
                cc = bc + sg * t * uc
                if cr < 0 or cr >= h or cc < 0 or cc >= m:
                    break
                if black[cr * m + cc]:
                    pr = xr + cr - br
                    pc = xc + cc - bc
                    tot[2] += sign
                    if 0 <= pr < h and 0 <= pc < m:
                        tot[3] += sign
                        _bump_point(tp, tot, pr * m + pc, sign)
                t += 1


@njit(cache=True)
def add_cell(h, m, black, blist, nb, pos, nP, tp, tot, x):
    process_cell(h, m, black, blist, nb, nP, tp, tot, x, 1)
    black[x] = 1
    blist[nb] = x
    pos[x] = nb
    return nb + 1


@njit(cache=True)
def remove_cell(h, m, black, blist, nb, pos, nP, tp, tot, x):
    i = pos[x]
    last = blist[nb - 1]
    blist[i] = last
    pos[last] = i
    pos[x] = -1
    nb -= 1
    black[x] = 0
    process_cell(h, m, black, blist, nb, nP, tp, tot, x, -1)
    return nb


class State:
    """Black set with its collision tallies."""

    def __init__(self, h, m, cells=()):
        self.h, self.m = h, m
        NN = h * m
        self.black = np.zeros(NN, np.uint8)
        self.blist = np.zeros(NN, np.int64)
        self.pos = -np.ones(NN, np.int64)
        self.nb = 0
        self.nP = np.zeros(NN * NN, np.uint8 if NN > 5000 else np.uint16)
        self.tp = np.zeros(NN, np.int32)
        self.tot = np.zeros(4, np.int64)
        for x in cells:
            self.add(int(x))

    def add(self, x):
        assert not self.black[x]
        self.nb = add_cell(self.h, self.m, self.black, self.blist, self.nb, self.pos, self.nP, self.tp, self.tot, x)

    def remove(self, x):
        assert self.black[x]
        self.nb = remove_cell(self.h, self.m, self.black, self.blist, self.nb, self.pos, self.nP, self.tp, self.tot, x)

    def cells(self):
        return sorted(int(v) for v in self.blist[:self.nb])

    def full_black(self):
        """Number of fully black rectangles (each is seen from its four corners)."""
        return int(self.tp[self.black == 1].sum()) // 4

    def summary(self):
        M4, M6, RA, RAin = (int(v) for v in self.tot)
        return {'cells': int(self.nb), 'M4': M4, 'M6': M6, 'full_black': self.full_black(),
                'right_angles': RA, 'right_angles_completing_inside': RAin}


def brute_counts(h, m, cells):
    """Slow reference for the counters, from the side-vector rectangle list."""
    from itertools import combinations
    S = set(cells)
    rects = rects_by_sides(h, m)
    nP, tp = {}, {}
    full = RAin = 0
    for R in rects:
        k = sum(v in S for v in R)
        if k == 4:
            full += 1
        for p in R:
            if all(v in S for v in R if v != p):
                tp[p] = tp.get(p, 0) + 1
                RAin += 1
        for P in combinations(R, 2):
            if all(v in S for v in R if v not in P):
                nP[P] = nP.get(P, 0) + 1
    M4 = sum(v * (v - 1) // 2 for v in nP.values())
    M6 = sum(v * (v - 1) // 2 for v in tp.values())
    bad = 0
    for i in range(len(rects)):
        Ri = set(rects[i])
        if len(Ri & S) < 2:
            continue
        for j in range(i + 1, len(rects)):
            if (Ri ^ set(rects[j])) <= S:
                bad += 1
    return {'M4': M4, 'M6': M6, 'full_black': full, 'right_angles_completing_inside': RAin, 'bad_pairs': bad}
