"""Independent checks for the round 3 audit.

Usage:  py audit_round3.py [part ...]     parts: enum tail good seas const four partial four9
With no argument all parts run.

Nothing here imports the scripts of the repository. Two rectangle enumerators are used.

  rects_naive(h, lo, hi)  lists every rectangle from the definition: for each pair of grid
      points p < q, taken as a side, it moves the side along the primitive normal as long
      as it stays in the grid.
  the fast validity test lists tilted rectangles by the side in the open first quadrant,
      and lists only those axis-aligned rectangles that have 2 or more black corners.
      Two rectangles with the same presentation show at most 2 corners each, so
      rectangles with 3 or 4 white corners can be skipped.

Part "enum" compares the two enumerators and the two validity tests.
"""
import random
import sys
import time
from itertools import combinations
from math import gcd, isqrt


def W(h):
    return 1 + (h - 1) ** 2 // 4


def q(h):
    return h * h // 4


# ---------------------------------------------------------------- enumerators

def rects_naive(h, lo, hi):
    """All rectangles with corners in columns lo..hi and rows 1..h, as frozensets."""
    pts = [(x, y) for x in range(lo, hi + 1) for y in range(1, h + 1)]
    out = set()
    for i, p in enumerate(pts):
        for k in range(i + 1, len(pts)):
            qq = pts[k]
            dx, dy = qq[0] - p[0], qq[1] - p[1]
            g = gcd(abs(dx), abs(dy))
            nx, ny = -dy // g, dx // g
            for sg in (1, -1):
                t = 1
                while True:
                    a = (p[0] + sg * t * nx, p[1] + sg * t * ny)
                    b = (qq[0] + sg * t * nx, qq[1] + sg * t * ny)
                    if not (lo <= a[0] <= hi and lo <= b[0] <= hi
                            and 1 <= a[1] <= h and 1 <= b[1] <= h):
                        break
                    out.add(frozenset((p, qq, a, b)))
                    t += 1
    return out


def is_axis(rect):
    return len({p[0] for p in rect}) == 2 and len({p[1] for p in rect}) == 2


def valid_naive(cols, h, rects=None, lo=1):
    """cols[i] is the set of black rows of column lo+i. Returns (valid, witness)."""
    m = len(cols)
    if rects is None:
        rects = rects_naive(h, lo, lo + m - 1)
    seen = {}
    for r in rects:
        pres = frozenset(p for p in r if p[1] not in cols[p[0] - lo])
        if pres in seen:
            return False, (sorted(seen[pres]), sorted(r))
        seen[pres] = r
    return True, None


_shape_cache = {}


def tilted_shapes(h):
    """Pairs of sides u = (u1, u2), v = (-v1, v2) with all four numbers positive."""
    if h in _shape_cache:
        return _shape_cache[h]
    out = []
    for u2 in range(1, h):
        for u1 in range(1, (h - 1) ** 2 + 1):
            g = gcd(u1, u2)
            s = 1
            while u2 + s * u1 // g <= h - 1:
                out.append((u1, u2, s * u2 // g, s * u1 // g))
                s += 1
    _shape_cache[h] = out
    return out


def tilted_rects(h, lo, hi):
    out = []
    for u1, u2, v1, v2 in tilted_shapes(h):
        for x in range(lo + v1, hi - u1 + 1):
            for y in range(1, h - u2 - v2 + 1):
                out.append(((x, y), (x + u1, y + u2), (x + u1 - v1, y + u2 + v2),
                            (x - v1, y + v2)))
    return out


def valid_fast(cols, h, lo=1):
    m = len(cols)
    hi = lo + m - 1
    black = {(lo + i, r) for i in range(m) for r in cols[i]}
    seen = {}

    def add(rect):
        white = tuple(sorted(p for p in rect if p not in black))
        if len(white) > 2:
            return None
        fr = frozenset(rect)
        old = seen.get(white)
        if old is not None and old != fr:
            return sorted(old), sorted(fr)
        seen[white] = fr
        return None

    for rect in tilted_rects(h, lo, hi):
        bad = add(rect)
        if bad:
            return False, bad
    bl = sorted(black)
    for i, p in enumerate(bl):
        for k in range(i + 1, len(bl)):
            c = bl[k]
            if p[0] == c[0]:
                for z in range(lo, hi + 1):
                    if z != p[0]:
                        bad = add((p, c, (z, p[1]), (z, c[1])))
                        if bad:
                            return False, bad
            elif p[1] == c[1]:
                for s in range(1, h + 1):
                    if s != p[1]:
                        bad = add((p, c, (p[0], s), (c[0], s)))
                        if bad:
                            return False, bad
            else:
                bad = add((p, c, (p[0], c[1]), (c[0], p[1])))
                if bad:
                    return False, bad
    return True, None


def part_enum():
    print('== enum: the two enumerators and the two validity tests agree')
    for h, m in ((3, 7), (4, 9), (5, 12), (6, 14), (7, 16)):
        a = rects_naive(h, 1, m)
        tilt_a = {r for r in a if not is_axis(r)}
        tilt_b = {frozenset(r) for r in tilted_rects(h, 1, m)}
        assert tilt_a == tilt_b and len(tilt_b) == len(tilted_rects(h, 1, m))
        span = max(max(p[0] for p in r) - min(p[0] for p in r) for r in tilt_a)
        axis = len(a) - len(tilt_a)
        assert axis == (h * (h - 1) // 2) * (m * (m - 1) // 2)
        assert span <= W(h)
        print('  %dx%d: %d rectangles, %d tilted, largest span %d, W_h = %d'
              % (h, m, len(a), len(tilt_a), span, W(h)))
    rng = random.Random(7)
    agree = [0, 0]
    for trial in range(4000):
        h = rng.randint(3, 6)
        m = rng.randint(3, 9)
        cols = []
        for _ in range(m):
            k = rng.choice((0, 1, 1, 1, 1, 2, 2, 3))
            cols.append(set(rng.sample(range(1, h + 1), min(k, h))))
        a = valid_naive(cols, h)[0]
        b = valid_fast(cols, h)[0]
        assert a == b, (h, cols)
        agree[a] += 1
    print('  4000 random blackouts: %d not valid, %d valid, both tests agree' % tuple(agree))


# ---------------------------------------------------------------- item 2

TAIL = ('16,36,5,25,2,2,14,7,12,27,2,7,67,7,47,7,7,56,45,34,23,1,1,1' + ',2' * 21)


def part_tail():
    print('== tail: the 7 row board T of the supplement')
    cols = [set(int(c) for c in w) for w in TAIL.split(',')]
    assert len(cols) == 45
    doubles = [frozenset(c) for c in cols if len(c) == 2]
    odd_even = {frozenset((r, s)) for r in (1, 3, 5, 7) for s in (2, 4, 6)}
    assert len(doubles) == 12 and set(doubles) == odd_even
    assert all(len(c) == 2 for c in cols[:21] if len(c) != 1) and all(len(c) == 1 for c in cols[21:])
    top = 70
    t0 = time.time()
    rects = rects_naive(7, 1, top)
    print('  %d rectangles on the 7x%d grid (%.0f s)' % (len(rects), top, time.time() - t0))
    by_width = {}
    for r in rects:
        by_width.setdefault(max(p[0] for p in r), []).append(r)
    ext = cols + [{2}] * (top - 45)
    cur = []
    ok_naive = []
    for m in range(1, top + 1):
        cur.extend(by_width.get(m, []))
        if m >= 21:
            v = valid_naive(ext[:m], 7, cur)[0]
            assert sum(len(c) for c in ext[:m]) == m + 12
            ok_naive.append((m, v))
    assert all(v for _, v in ok_naive)
    print('  definition test, every rectangle listed: T_m valid with m+12 points for m = 21..%d' % top)
    for m in (21, 22, 23, 24, 25, 33, 44, 45, 46, 60, 100, 150):
        c = (cols + [{2}] * 200)[:m]
        assert valid_fast(c, 7)[0]
    print('  second test: T_m valid for m = 21..25, 33, 44, 45, 46, 60, 100, 150')
    # the tail really needs the three columns black in row 1: without them the board fails
    c = cols[:21] + [{2}] * 24
    print('  control, row 2 directly after column 21, width 45: valid =', valid_fast(c, 7)[0])


# ---------------------------------------------------------------- item 1: goodness

def good(h, g, e):
    r = [x for x in e if x % 2 == 1][0]
    s = [x for x in e if x % 2 == 0][0]
    if r > g or s > g:
        return False
    for j in range(1, min(r - 1, h - g) + 1):
        v = j * (g - r + j)
        if isqrt(v) ** 2 == v:
            return False
    return True


def parity_edges(h):
    return [(r, s) for r in range(1, h + 1, 2) for s in range(2, h + 1, 2)]


def rho(h, e):
    return tuple(sorted((h + 1 - e[0], h + 1 - e[1]), key=lambda x: x % 2 == 0))


def part_good():
    print('== good: counting claims on good edges')
    worst = None
    for h in range(9, 1202, 2):
        es = parity_edges(h)
        assert len(es) == q(h)
        n_good = sum(good(h, h - 1, e) for e in es)
        assert 2 * n_good >= q(h), h
        ratio = n_good / q(h)
        if worst is None or ratio < worst[0]:
            worst = (ratio, h, n_good)
        if h <= 401:
            for e in es:
                f = rho(h, e)
                assert (good(h, h - 1, e) or good(h, h - 3, e)
                        or good(h, h - 1, f) or good(h, h - 3, f)), (h, e)
    print('  odd h = 9..1201: at least q_h/2 edges are good for h-1; smallest share %.4f at h = %d'
          % (worst[0], worst[1]))
    print('  odd h = 9..401: for every parity edge e, one of e, rho(e) is good for h-1 or h-3')
    for h in range(4, 41, 2):
        assert all(good(h, h, e) for e in parity_edges(h))
    print('  even h = 4..40: every parity edge is good for g = h')
    for h in (5, 7):
        es = parity_edges(h)
        print('  h = %d: %d of %d edges good for h-1' % (h, sum(good(h, h - 1, e) for e in es), len(es)))


# ---------------------------------------------------------------- item 1: gadgets

class Window:
    """Rectangles of the strip in the columns -2W..2W, with sides and diagonals."""

    def __init__(self, h):
        self.h = h
        w = 2 * W(h)
        rects = [tuple(sorted(r)) for r in rects_naive(h, -w, w)]
        self.rects = rects
        self.diag = []
        self.by_diag = {}
        for idx, r in enumerate(rects):
            a, b, c, d = r
            pairs = None
            for x, y in ((b, (c, d)), (c, (b, d)), (d, (b, c))):
                if a[0] + x[0] == y[0][0] + y[1][0] and a[1] + x[1] == y[0][1] + y[1][1]:
                    pairs = ((a, x), y)
            assert pairs is not None
            self.diag.append(pairs)
            for pr in pairs:
                self.by_diag.setdefault(frozenset(pr), []).append(idx)

    def A(self, g, e):
        """The set A_e of the definition of a good edge, by listing private obstructions."""
        def allowed(p):
            return (p[1] in e) if p[0] == 0 else (p[1] == 1 or p[1] == g)
        out = set()
        for idx, r in enumerate(self.rects):
            if not is_axis(r):
                for tri in combinations(r, 3):
                    if all(allowed(p) for p in tri) and any(p[0] == 0 for p in tri):
                        out.update(p[0] for p in tri)
            d1, d2 = self.diag[idx]
            sides = [(d1[0], d2[0]), (d1[0], d2[1]), (d1[1], d2[0]), (d1[1], d2[1])]
            for side in sides:
                a, b = [p for p in r if p not in side]
                if a[0] == b[0] or not (allowed(a) and allowed(b)):
                    continue
                for jdx in self.by_diag.get(frozenset(side), ()):
                    e1, e2 = self.diag[jdx]
                    cd = e2 if frozenset(e1) == frozenset(side) else e1
                    if allowed(cd[0]) and allowed(cd[1]):
                        quad = (a, b, cd[0], cd[1])
                        if any(p[0] == 0 for p in quad):
                            out.update(p[0] for p in quad)
        out.discard(0)
        return out


_windows = {}
_gadgets = {}


def gadget(h, g, e):
    key = (h, g, tuple(sorted(e)))
    if key not in _gadgets:
        if h not in _windows:
            _windows[h] = Window(h)
        _gadgets[key] = _windows[h].A(g, e)
    return _gadgets[key]


def board_ab(h, g, edges, m, rng, free='one'):
    """Cases (a), (b): doubles 4W+1 apart, so that no set of columns is bad."""
    step = 4 * W(h) + 1
    cols = [None] * (m + 1)
    for i, e in enumerate(edges):
        x = 1 + i * step
        cols[x] = set(e)
        for a in gadget(h, g, e):
            assert abs(a) <= 2 * W(h)
            if 1 <= x + a <= m:
                assert cols[x + a] is None
                cols[x + a] = {1} if a < 0 else {g}
    for x in range(1, m + 1):
        if cols[x] is None:
            cols[x] = {1} if free == 'one' else {rng.choice((1, g))}
    return cols[1:]


def part_partial():
    print('== partial: boards of the proposition on partial edge sets, doubles 4W_h+1 apart')
    rng = random.Random(11)
    t0 = time.time()
    # cases (a) and (b)
    for h in (4, 5, 6, 7, 8, 9, 10):
        g = h if h % 2 == 0 else h - 1
        pool = [e for e in parity_edges(h) if good(h, g, e)]
        sizes = {4: (1, 2, 3, 4), 5: (1, 2, 4), 6: (1, 3, 5), 7: (1, 3, 5), 8: (1, 4), 9: (1, 3),
                 10: (1, 3)}[h]
        count = 0
        for n in sizes:
            for rep in range(2):
                edges = rng.sample(pool, n)
                last = 1 + (n - 1) * (4 * W(h) + 1)
                for m in (last, last + rng.randint(1, 3 * W(h)), last + 4 * W(h) + 2):
                    for free in ('one', 'random'):
                        cols = board_ab(h, g, edges, m, rng, free)
                        assert sum(len(c) for c in cols) == m + n
                        ok, wit = valid_fast(cols, h)
                        assert ok, (h, edges, m, free, wit)
                        count += 1
        print('  h = %2d, g = %2d: %d boards valid, |A_e| at most %d  (%.0f s)'
              % (h, g, count, max(len(v) for k, v in _gadgets.items() if k[0] == h), time.time() - t0))
    # case (c) at h = 9
    h = 9
    Wh = W(h)
    step = 4 * Wh + 1
    cls = {1: [], 2: [], 3: [], 4: []}
    for e in parity_edges(h):
        f = rho(h, e)
        if good(h, h - 1, e):
            cls[1].append(e)
        elif good(h, h - 3, e):
            cls[2].append(e)
        elif good(h, h - 1, f):
            cls[3].append(e)
        elif good(h, h - 3, f):
            cls[4].append(e)
        else:
            raise AssertionError(e)
    print('  h = 9: classes of sizes', [len(cls[k]) for k in (1, 2, 3, 4)],
          ' class 2:', cls[2], ' class 4:', cls[4])
    gk = {1: h - 1, 2: h - 3, 3: h - 1, 4: h - 3}
    count = 0
    plans = [(1, 1, 1, 1), (2, 1, 2, 1), (0, 2, 0, 1), (3, 0, 0, 0), (0, 0, 3, 0), (1, 0, 0, 1),
             (0, 1, 1, 0)]
    for plan in plans:
        parts = {k: rng.sample(cls[k], plan[k - 1]) for k in (1, 2, 3, 4)}
        N = {k: 1 + (max(len(parts[k]), 1) - 1) * step for k in parts}
        s = {1: 1}
        for k in (1, 2, 3):
            s[k + 1] = s[k] + N[k] + 8 * Wh
        z = s[3] - 4 * Wh
        last = s[4] + N[4] - 1
        n = sum(plan)
        for m in (last, last + 2 * Wh + 5):
            cols = [None] * (m + 1)
            for k in (1, 2, 3, 4):
                for i, e in enumerate(parts[k]):
                    x = s[k] + i * step
                    cols[x] = set(e)
                    src = e if k <= 2 else rho(h, e)
                    for a in gadget(h, gk[k], src):
                        if 1 <= x + a <= m:
                            assert cols[x + a] is None
                            if k <= 2:
                                cols[x + a] = {1} if a < 0 else {gk[k]}
                            else:
                                cols[x + a] = {h} if a < 0 else {h + 1 - gk[k]}
            for x in range(1, m + 1):
                if cols[x] is None:
                    cols[x] = {1} if x < z else {h}
            cols = cols[1:]
            assert sum(len(c) for c in cols) == m + n
            ok, wit = valid_fast(cols, h)
            assert ok, (plan, parts, m, wit)
            count += 1
    print('  h = 9, case (c): %d boards valid, with 1 to 6 doubles in 1 to 4 blocks  (%.0f s)'
          % (count, time.time() - t0))
    # controls
    cols = [{5, 2}] + [{8}] * 30 + [{9, 4}] + [{8}] * 5
    print('  control h = 9, edge {5,2} (not good for 8) with sea row 8 and a double {4,9}: valid =',
          valid_fast(cols, 9)[0])
    cols = [{1}] * 20 + [{9}] * 20
    print('  control h = 9, sea rows 1 then 9, no double: valid =', valid_fast(cols, 9)[0])
    cols = [{1}] * 3 + [{9}] * 3 + [{1}] * 30
    print('  control h = 9, sea rows 1, 9, 1 mixed: valid =', valid_fast(cols, 9)[0])


def part_seas():
    print('== seas: the explicit construction for 3 <= h <= 8 (used by the corollary for h <= 8)')
    for h in range(3, 9):
        half = h // 2
        edges = [(a, b) for a in range(1, half + 1) for b in range(half + 1, h + 1)]
        assert len(edges) == q(h)
        Mh = q(h) + (q(h) - 1) * W(h)
        for m in (Mh, Mh + 1, Mh + W(h) + 3):
            cols = []
            row = 1
            pos = {1 + j * (W(h) + 1): e for j, e in enumerate(edges)}
            for x in range(1, m + 1):
                if x in pos:
                    cols.append(set(pos[x]))
                    row = h + 1 - row
                else:
                    cols.append({row})
            assert max(pos) == Mh and sum(len(c) for c in cols) == m + q(h)
            assert valid_fast(cols, h)[0], (h, m)
        print('  h = %d: valid with m + q_h points at m = M_h = %d, M_h + 1, M_h + W_h + 3' % (h, Mh))
    for h in range(3, 9):
        for m in range(1, 8):
            cols = [set(range(1, h + 1))] + [{1}] * (m - 1)
            assert valid_naive(cols, h)[0]
    print('  boundary cross (first row and first column) valid for 3 <= h <= 8, 1 <= m <= 7')


# ---------------------------------------------------------------- item 1: constants

def hcn(limit):
    """Record holders of the divisor function up to limit: list of (n, tau(n))."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
              73, 79, 83, 89, 97]
    cand = []

    def rec(i, n, d, emax):
        cand.append((n, d))
        p = primes[i]
        e = 1
        n *= p
        while n <= limit and e <= emax:
            rec(i + 1, n, d * (e + 1), e)
            n *= p
            e += 1

    rec(0, 1, 1, 200)
    cand.sort()
    out = []
    best = 0
    for n, d in cand:
        if d > best:
            out.append((n, d))
            best = d
    return out


def part_const():
    print('== const: the constant c_0 and the crossover with M_h')
    c1 = 2 ** 31
    c0 = 48 * c1
    assert c0 == 3 * 2 ** 35
    print('  c_0 = 48 * 2^31 = 3 * 2^35 = %d = %.4g' % (c0, c0))
    assert (2 ** 14 + 1) ** 2 <= 2 ** 30 and 768 + 12288 <= 2 ** 14
    assert 2 ** 30 + 8 + 4 * (10 ** 3 + 10 ** 4) <= c1
    for h in range(3, 9):
        assert q(h) + (q(h) - 1) * W(h) <= 2 * c0
    for h in range(9, 4000, 2):
        assert c0 * (q(h) // 2 - 4) >= 6 * h * h + 4 and 2 * (q(h) // 2) == q(h)
    rec = hcn(10 ** 27)

    def tmax(h):
        lo, hi = 0, len(rec) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if rec[mid][0] <= h * h:
                lo = mid
            else:
                hi = mid - 1
        return rec[lo][1]

    def below(h):
        return c0 * (q(h) + 4) * tmax(h) ** 2 + 6 * h * h + 5 < q(h) + (q(h) - 1) * W(h)

    # tmax is constant between consecutive record holders; there the comparison is
    # monotone in h, which the bisection assumes and the two asserts below test at the ends
    first = None
    last_fail = None
    for i in range(len(rec) - 1):
        hs = max(3, isqrt(rec[i][0] - 1) + 1)
        he = isqrt(rec[i + 1][0] - 1)
        if hs > he or hs > 10 ** 13:
            continue
        if not below(he):
            assert not below(hs)
            last_fail = he
            continue
        lo, hi = hs, he
        while lo < hi:
            mid = (lo + hi) // 2
            if below(mid):
                hi = mid
            else:
                lo = mid + 1
        if lo > hs:
            assert not below(lo - 1) and not below(hs)
            last_fail = lo - 1
        if first is None:
            first = lo
    lo, hi = first, last_fail
    print('  first h with bound of the theorem < M_h: %d  (tmax = %d)' % (lo, tmax(lo)))
    print('  last  h with bound of the theorem >= M_h: %d  (tmax = %d)' % (hi, tmax(hi)))
    for h in (10 ** 11, 5 * 10 ** 11, 6 * 10 ** 11, 7 * 10 ** 11, 8 * 10 ** 11, 10 ** 12):
        print('    h = %.0e: tmax = %d, bound < M_h: %s' % (h, tmax(h), below(h)))


# ---------------------------------------------------------------- item 4

def read_gf(path):
    P, Q = {}, {}
    with open(path) as fh:
        for line in fh:
            t = line.split()
            if len(t) == 3 and t[0] in 'PQ' and len(t[0]) == 1:
                (P if t[0] == 'P' else Q)[int(t[1])] = int(t[2])
    return ([P.get(k, 0) for k in range(max(P) + 1)], [Q.get(k, 0) for k in range(max(Q) + 1)])


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return out


def count_four(m):
    """Number of valid blackouts among the candidates of the 4 x m grid (4 doubles on a
    4-cycle of rows, singletons elsewhere), each tested against the definition."""
    rects = rects_naive(4, 1, m)
    bit = {(x, y): 1 << (4 * (x - 1) + y - 1) for x in range(1, m + 1) for y in range(1, 5)}
    masks = [sum(bit[p] for p in r) for r in rects]
    cycles = [[(1, 3), (1, 4), (2, 3), (2, 4)], [(1, 2), (1, 4), (3, 2), (3, 4)],
              [(1, 2), (1, 3), (4, 2), (4, 3)]]
    from itertools import permutations, product
    res = []
    for cyc in cycles:
        total = 0
        for places in permutations(range(m), 4):
            base = 0
            for (r, s), x in zip(cyc, places):
                base |= (1 << (4 * x + r - 1)) | (1 << (4 * x + s - 1))
            rest = [x for x in range(m) if x not in places]
            for rows in product(range(4), repeat=m - 4):
                S = base
                for x, r in zip(rest, rows):
                    S |= 1 << (4 * x + r)
                seen = set()
                ok = True
                for mk in masks:
                    pr = mk & ~S
                    if pr in seen:
                        ok = False
                        break
                    seen.add(pr)
                total += ok
        res.append(total)
    return res


def part_four(gf_path, top=7):
    print('== four: the file four_row_gf.txt and the size of the modulus')
    P, Q = read_gf(gf_path)
    assert len(P) == 445 and len(Q) == 421 and Q[0] == 1 and P[444] != 0 and Q[420] != 0
    print('  deg P = 444, deg Q = 420, Q(0) = 1, P_444 = %d, P_6 = %d, P_7 = %d' % (P[444], P[6], P[7]))
    a = [0] * 40
    for n in range(40):
        a[n] = (P[n] if n < len(P) else 0) - sum(Q[j] * a[n - j] for j in range(1, min(n, 420) + 1))
    table = [26, 292, 2118, 13332, 75398, 402656, 2037848, 9894016]
    assert a[:6] == [0] * 6 and a[6:14] == table
    print('  series of P/Q: a_4(6..13) =', a[6:14], '(equal to the table of the paper)')
    A = sum(abs(x) for x in Q)
    primes = []
    n = 2 ** 31
    while len(primes) < 48:
        n -= 1
        if n % 2 and all(n % d for d in range(3, isqrt(n) + 1, 2)):
            primes.append(n)
    prod = 1
    for p in primes:
        prod *= p
    prod47 = prod // primes[-1]
    need = 2 * A * 8 ** 445
    print('  sum |q_j| has %d bits; 2 * 8^445 * sum|q_j| has %d bits; product of the 48 largest'
          ' primes below 2^31 has %d bits' % (A.bit_length(), need.bit_length(), prod.bit_length()))
    assert prod > need
    print('  48 primes suffice for the vector identity: True; 47 primes suffice: %s;'
          ' enough for the stricter bound of the script (factor 6): %s'
          % (prod47 > need, prod > 3 * need))
    assert prod > 2 * (3 * A * 8 ** 444 + max(abs(c) for c in P))
    print('  48 primes also decide the comparison with P (|coefficient| <= 3*8^444*sum|q_j| + max|P_n|)')
    # factors stated in the theorem
    g5 = [1, 0, 3, -2, 2, -1]
    h5 = [1, 0, 1, 0, 0, -1]
    g6 = [1, 0, -1, 0, 0, -1, -2]
    g20 = [1, -4, 2, 1, -3, 5, 1, -3, 7, 2, 30, -7, 10, 12, 2, 17, 26, 19, -26, -4, 8]
    try:
        import sympy as sp
        z = sp.symbols('z')
        Qs = sp.Poly(sum(c * z ** k for k, c in enumerate(Q)), z)
        Ps = sp.Poly(sum(c * z ** k for k, c in enumerate(P)), z)
        t0 = time.time()
        _, fl = sp.factor_list(Qs)
        shape = sorted((f.degree(), mult) for f, mult in fl)
        print('  factorization of Q over Z, (degree, multiplicity):', shape, '(%.0f s)' % (time.time() - t0))
        assert shape == [(1, 2), (1, 2), (5, 3), (5, 3), (6, 3), (11, 5), (17, 3), (19, 3), (20, 5), (21, 5)]
        have = {tuple(int(c) * (1 if f.all_coeffs()[-1] > 0 else -1) for c in reversed(f.all_coeffs()))
                for f, _ in fl}
        for name, poly in (('g5', g5), ('g5 tilde', h5), ('g6', g6), ('g20', g20)):
            assert tuple(poly) in have, name
        print('  g_5, g~_5, g_6, g_20 of the theorem are among the factors, with constant term 1')
        gg = sp.gcd(Ps, Qs)
        print('  gcd(P, Q) has degree', gg.degree())
        assert gg.degree() == 0
    except ImportError:
        print('  sympy not available, factorization not checked')
    for m in range(6, top + 1):
        t0 = time.time()
        res = count_four(m)
        print('  m = %d: valid candidates for the pair sets of 12|34, 13|24, 14|23 = %s,'
              ' total %d  (%.0f s)' % (m, res, sum(res), time.time() - t0))
        assert sum(res) == table[m - 6]


def main():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    gf = os.path.join(here, 'enumeration', 'anc', 'four_row_gf.txt')
    parts = sys.argv[1:] or ['enum', 'tail', 'good', 'seas', 'const', 'four', 'partial']
    t0 = time.time()
    for p in parts:
        if p == 'four9':
            part_four(gf, 9)
        elif p == 'four':
            part_four(gf, 8)
        else:
            globals()['part_' + p]()
        print('  [%.0f s]' % (time.time() - t0), flush=True)


if __name__ == '__main__':
    main()
