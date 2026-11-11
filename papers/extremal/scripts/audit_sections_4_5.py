"""Independent checks for the audit of Sections 4 and 5. Points are (column, row), rows 1..h."""
import sys, math, random, itertools
from math import gcd, isqrt
import numpy as np

def W(h): return 1 + (h - 1) ** 2 // 4
def q(h): return h * h // 4
def tau(n): return sum(1 for d in range(1, n + 1) if n % d == 0)
def tmax(h): return max(tau(n) for n in range(1, h * h + 1))

def norm(pts):
    mn = min(p[0] for p in pts)
    return tuple(sorted((p[0] - mn, p[1]) for p in pts))

# ---------- rectangles of the strip, tilted, up to horizontal translation ----------
def tilted_shapes(h):
    """All tilted rectangles with rows in 1..h, up to horizontal translation.
    Side u=(u1,u2), other side v=k*(-u2,u1)/g. Both sides have all coordinates nonzero.
    |u1| <= (h-1)^2 follows from |k*u1/g| <= h-1 and g <= |u2| <= h-1 (no use of the span lemma)."""
    out = set()
    B = (h - 1) ** 2
    for y in range(1, h + 1):
        for u2 in range(-(h - 1), h):
            if u2 == 0 or not (1 <= y + u2 <= h): continue
            for u1 in range(-B, B + 1):
                if u1 == 0: continue
                g = gcd(abs(u1), abs(u2))
                b1, b2 = -u2 // g, u1 // g
                for sgn in (1, -1):
                    k = 1
                    while True:
                        v1, v2 = sgn * k * b1, sgn * k * b2
                        if not (1 <= y + v2 <= h): break
                        if 1 <= y + u2 + v2 <= h:
                            out.add(norm([(0, y), (u1, y + u2), (v1, y + v2), (u1 + v1, y + u2 + v2)]))
                        k += 1
    return out

def corner_triples(tsh):
    out = set()
    for s in tsh:
        for i in range(4):
            out.add(norm([s[j] for j in range(4) if j != i]))
    return out

def mixed_and_rivals(h, maxspan):
    """From Definition (mixed pair): pq side of R1 and diagonal of R2.
    Returns set of ordered tuples (A,B,C,D) translated so A is in column 0 (pq not vertical),
    and set of rival pairs ((0,c),(t,c')) (pq vertical, rows of p,q of different parity)."""
    quads = set(); rivals = set()
    for py in range(1, h + 1):
        for qy in range(1, h + 1):
            for qx in range(-maxspan, maxspan + 1):
                dx, dy = qx, qy - py
                if dx == 0 and dy == 0: continue
                L2 = dx * dx + dy * dy
                sx, sy = qx, py + qy
                CD = []
                for e2 in range(-(h - 1), h):
                    r2 = L2 - e2 * e2
                    if r2 < 0: continue
                    e1 = isqrt(r2)
                    if e1 * e1 != r2: continue
                    for e1s in {e1, -e1}:
                        if (e1s, e2) in ((dx, dy), (-dx, -dy)): continue
                        if (sx + e1s) % 2 or (sy + e2) % 2: continue
                        C = ((sx + e1s) // 2, (sy + e2) // 2); D = ((sx - e1s) // 2, (sy - e2) // 2)
                        if 1 <= C[1] <= h and 1 <= D[1] <= h: CD.append((C, D))
                if not CD: continue
                if dx == 0:
                    if dy % 2:
                        for C, D in CD:
                            rivals.add(((0, C[1]), (D[0] - C[0], D[1])))
                    continue
                g = gcd(abs(dx), abs(dy))
                b1, b2 = -dy // g, dx // g
                for sgn in (1, -1):
                    k = 1
                    while True:
                        n1, n2 = sgn * k * b1, sgn * k * b2
                        A = (n1, py + n2); Bp = (qx + n1, qy + n2)
                        if not (1 <= A[1] <= h) or not (1 <= Bp[1] <= h):
                            # rows are affine in k, so once out, stays out
                            break
                        for C, D in CD:
                            a0 = A[0]
                            quads.add(((0, A[1]), (Bp[0] - a0, Bp[1]), (C[0] - a0, C[1]), (D[0] - a0, D[1])))
                        k += 1
    return quads, rivals

# ---------- validity checkers ----------
def all_rects_naive(h, m):
    """Every 4-subset of grid points that is a rectangle (pure geometry). Tiny grids only."""
    pts = [(x, y) for x in range(m) for y in range(1, h + 1)]
    out = set()
    for a, b, c, d in itertools.combinations(pts, 4):
        for (p, r), (s, t) in (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))):
            # p,r and s,t diagonals: same midpoint, same length, nondegenerate
            if p[0] + r[0] == s[0] + t[0] and p[1] + r[1] == s[1] + t[1]:
                if (p[0] - r[0]) ** 2 + (p[1] - r[1]) ** 2 == (s[0] - t[0]) ** 2 + (s[1] - t[1]) ** 2:
                    out.add(frozenset((a, b, c, d)))
    return out

def rects_from_shapes(h, m, tsh):
    out = set()
    for y1 in range(1, h + 1):
        for y2 in range(y1 + 1, h + 1):
            for x1 in range(m):
                for x2 in range(x1 + 1, m):
                    out.add(frozenset(((x1, y1), (x2, y1), (x1, y2), (x2, y2))))
    for s in tsh:
        w = max(p[0] for p in s)
        for x in range(m - w):
            out.add(frozenset((p[0] + x, p[1]) for p in s))
    return out

def valid_naive(black, rects):
    seen = {}
    for R in rects:
        pres = frozenset(R - black)
        if pres in seen: return False
        seen[pres] = R
    return True

def valid_fast(blk, h, m, tsh):
    """blk[y][x] bool, y in 1..h, x in 0..m-1. Distinct rectangles with equal presentation
    must each show <= 2 corners (3 points determine a rectangle), so only rectangles with
    >= 2 black corners are encoded and compared. Returns number of colliding presentations."""
    P = (h + 1) * m
    codes = []
    def proc(pts, width):
        n = m - width
        if n <= 0: return
        x = np.arange(n)
        bs = [blk[y, dx:dx + n] for dx, y in pts]
        cnt = bs[0].astype(np.int8) + bs[1] + bs[2] + bs[3]
        sel = np.nonzero(cnt >= 2)[0]
        if sel.size == 0: return
        arr = np.empty((4, sel.size), dtype=np.int64)
        for i, (dx, y) in enumerate(pts):
            arr[i] = np.where(bs[i][sel], P, y * m + dx + sel)
        arr.sort(axis=0)
        codes.append(arr[0] * (P + 1) + arr[1])
    for y1 in range(1, h + 1):
        for y2 in range(y1 + 1, h + 1):
            for w in range(1, m):
                proc([(0, y1), (w, y1), (0, y2), (w, y2)], w)
    for s in tsh:
        proc(list(s), max(p[0] for p in s))
    if not codes: return 0
    allc = np.concatenate(codes)
    u, c = np.unique(allc, return_counts=True)
    return int((c > 1).sum())

def blk_from(cols, h):
    m = len(cols)
    blk = np.zeros((h + 1, m), dtype=bool)
    for x, rows in enumerate(cols):
        for y in rows: blk[y, x] = True
    return blk

# ---------- tests ----------
def test_enumerator():
    for h, m in ((3, 5), (4, 6), (5, 5)):
        tsh = tilted_shapes(h)
        a = all_rects_naive(h, m); b = rects_from_shapes(h, m, tsh)
        print("enumerator", h, m, len(a), len(b), a == b)
        rng = random.Random(1)
        agree = 0; nvalid = 0
        for t in range(300):
            k = rng.randint(1, m + q(h) + 1)
            black = frozenset(rng.sample([(x, y) for x in range(m) for y in range(1, h + 1)], k))
            v1 = valid_naive(black, a)
            cols = [[y for y in range(1, h + 1) if (x, y) in black] for x in range(m)]
            v2 = valid_fast(blk_from(cols, h), h, m, tsh) == 0
            agree += (v1 == v2); nvalid += v1
        print("  fast vs naive agree", agree, "/300, valid among them", nvalid)
    for h in range(3, 12):
        tsh = tilted_shapes(h)
        print("max span h=%d: %d, W_h=%d" % (h, max(max(p[0] for p in s) for s in tsh), W(h)))

def seas_cols(h, m, edges, pos):
    cols = []; row = 1; d = dict(zip(pos, edges))
    for x in range(m):
        if x in d:
            cols.append(list(d[x])); row = h + 1 - row
        else: cols.append([row])
    return cols

def tri_free(edges):
    E = set(map(frozenset, edges))
    vs = sorted(set(v for e in edges for v in e))
    for a, b, c in itertools.combinations(vs, 3):
        if frozenset((a, b)) in E and frozenset((b, c)) in E and frozenset((a, c)) in E: return False
    return True

def test_seas(hmax=8, seed=0):
    rng = random.Random(seed)
    for h in range(3, hmax + 1):
        tsh = tilted_shapes(h); w = W(h); tot = 0; bad = 0
        rows = list(range(1, h + 1))
        # complete balanced bipartite graphs, spacing exactly W+1, first double in column 1
        parts = [set(c) for c in itertools.combinations(rows, h // 2)]
        if len(parts) > 12: parts = rng.sample(parts, 10) + [set(range(1, h // 2 + 1)), set(range(2, h + 1, 2))]
        for A in parts:
            edges = [(a, b) for a in sorted(A) for b in rows if b not in A]
            for rep in range(3 if h <= 6 else 1):
                e = edges[:] if rep == 0 else rng.sample(edges, len(edges))
                pos = [j * (w + 1) for j in range(len(e))]
                Mh = q(h) + (q(h) - 1) * w
                assert pos[-1] + 1 == Mh
                for m in (Mh, Mh + 1, Mh + w + 2):
                    nb = valid_fast(blk_from(seas_cols(h, m, e, pos), h), h, m, tsh)
                    tot += 1; bad += nb > 0
                    assert sum(len(c) for c in seas_cols(h, m, e, pos)) == m + q(h)
        # random triangle-free graphs (not nec. bipartite), random spacings >= W+1, random margins
        for rep in range(60 if h <= 6 else 8):
            alle = list(itertools.combinations(rows, 2)); rng.shuffle(alle)
            edges = []
            for e in alle:
                if rng.random() < 0.7 and tri_free(edges + [e]): edges.append(e)
            if not edges: continue
            x = rng.randint(0, w + 2); pos = []
            for _ in edges:
                pos.append(x); x += w + 1 + rng.choice((0, 0, 1, 2, w))
            m = pos[-1] + 1 + rng.randint(0, w + 2)
            nb = valid_fast(blk_from(seas_cols(h, m, edges, pos), h), h, m, tsh)
            tot += 1; bad += nb > 0
        print("seas h=%d: %d configurations, %d invalid" % (h, tot, bad), flush=True)

def test_spacing_W():
    for h in (3, 4, 5, 6, 7):
        tsh = tilted_shapes(h); w = W(h); rows = range(1, h + 1)
        A = set(range(1, h // 2 + 1))
        edges = [(a, b) for a in sorted(A) for b in rows if b not in A]  # lexicographic
        pos = [j * w for j in range(len(edges))]; m = pos[-1] + 1 + w
        nb = valid_fast(blk_from(seas_cols(h, m, edges, pos), h), h, m, tsh)
        print("spacing W_h, lexicographic, rows 1..h/2 vs rest, h=%d: collisions=%d" % (h, nb))
        rng = random.Random(5); cnt = 0; T = 40
        for t in range(T):
            e = rng.sample(edges, len(edges))
            cnt += valid_fast(blk_from(seas_cols(h, m, e, pos), h), h, m, tsh) > 0
        print("   random orders with spacing W_h: %d of %d invalid" % (cnt, T), flush=True)

def is_chain(pts):
    return all((a[0] <= b[0] and a[1] <= b[1]) or (b[0] <= a[0] and b[1] <= a[1]) for a, b in itertools.combinations(pts, 2))

def test_lemmas(hmax=11):
    for h in range(3, hmax + 1):
        tsh = tilted_shapes(h); ms = max(max(p[0] for p in s) for s in tsh)
        trip = corner_triples(tsh); quads, riv = mixed_and_rivals(h, ms)
        tm = tmax(h)
        qsets = set(norm(t) for t in quads)
        width = max([max(p[0] for p in s) for s in qsets] + [0])
        # sea lemma
        sea_fail = 0
        for g in range(2, h + 1, 2):
            if 2 * g - 1 <= h: continue
            for s in list(trip) + list(qsets):
                if all(p[1] in (1, g) for p in s): sea_fail += 1
            for C, D in riv:
                if C[1] in (1, g) and D[1] in (1, g): sea_fail += 1
        # does the hypothesis 2g-1>h matter? count failures for the other even g
        other = 0
        for g in range(2, h + 1, 2):
            if 2 * g - 1 > h: continue
            other += sum(1 for s in list(trip) + list(qsets) if all(p[1] in (1, g) for p in s))
        chain_fail = sum(1 for s in list(trip) + list(qsets) if is_chain(s))
        # rival lemma
        riv_fail = 0
        for C, D in riv:
            c, c2 = sorted((C[1], D[1])); t = D[0]
            ok = (c2 - c) % 2 == 1 and c >= 2 and c2 <= h - 1 and any(
                c - j >= 1 and c2 + j <= h and 4 * j * (c2 - c + j) == t * t for j in range(1, h))
            riv_fail += not ok
        # counting lemma
        from collections import Counter
        ca = Counter()
        for s in tsh:
            for i in range(4):
                # right angle at s[i]; the two neighbours are the corners not opposite
                P0 = s[i]; others = [s[j] for j in range(4) if j != i]
                # opposite corner = the one with P0+opp = sum of the other two
                for o in others:
                    nb = [p for p in others if p != o]
                    if (P0[0] + o[0], P0[1] + o[1]) == (nb[0][0] + nb[1][0], nb[0][1] + nb[1][1]):
                        for a, b in ((nb[0], nb[1]), (nb[1], nb[0])):
                            ca[(P0[1], a[1], b[1])] += 1
        cb = Counter((t[0][1], t[1][1], t[2][1], t[3][1]) for t in quads)
        cc = Counter((C[1], D[1]) for C, D in riv)
        print("h=%d tmax=%d | triples %d quads %d rivals %d | quad width max %d (2W=%d) | sea fails %d (bad-g hits %d) | chains %d | rival fails %d | count a: %d<=%d, b: %d<=%d, c: %d<=%d"
              % (h, tm, len(trip), len(qsets), len(riv), width, 2 * W(h), sea_fail, other, chain_fail, riv_fail,
                 max(ca.values()), 2 * tm, max(cb.values()) if cb else 0, 4 * tm, max(cc.values()) if cc else 0, 2 * tm), flush=True)

def good(e, g, h):
    r, s = (e if e[0] % 2 else (e[1], e[0]))
    if r > g or s > g: return False
    for j in range(1, min(r - 1, h - g) + 1):
        v = j * (g - r + j)
        if isqrt(v) ** 2 == v: return False
    return True

def rho(e, h): return tuple(sorted((h + 1 - e[0], h + 1 - e[1])))

def test_claim(hmax=401):
    worst = 0
    for h in range(9, hmax + 1, 2):
        for r in range(1, h + 1, 2):
            for s in range(2, h, 2):
                e = (r, s)
                ok = good(e, h - 1, h) or good(e, h - 3, h) or good(rho(e, h), h - 1, h) or good(rho(e, h), h - 3, h)
                if not ok: worst += 1; print("CLAIM FAILS", h, e)
    print("odd-height claim checked for odd h in 9..%d, failures %d" % (hmax, worst))
    for h in (5, 7):
        fails = [(r, s) for r in range(1, h + 1, 2) for s in range(2, h, 2)
                 if not (good((r, s), h - 1, h) or good(rho((r, s), h), h - 1, h))]
        print("h=%d: edges not good for g=h-1 even after reflection:" % h, fails)

# ---------- Section 5 construction ----------
class Block:
    def __init__(self, h, g, shapes, riv):
        self.h, self.g = h, g
        self.sea = (1, g)
        self.byrows = {}
        for s in shapes:
            self.byrows.setdefault(frozenset(p[1] for p in s), []).append(s)
        self.anch = {c: [] for c in range(1, h + 1)}
        for s in shapes:
            for i, p in enumerate(s):
                self.anch[p[1]].append(tuple((o[0] - p[0], o[1]) for j, o in enumerate(s) if j != i))
        self.riv = {}
        for C, D in riv:
            self.riv.setdefault(C[1], []).append((D[0], D[1]))
        self.rivset = riv

    def A(self, e):
        r, s = e; R4 = {1, self.g, r, s}; out = set(); in_gadget = 0
        for k in range(1, 5):
            for sub in itertools.combinations(sorted(R4), k):
                for sh in self.byrows.get(frozenset(sub), []):
                    for i in range(len(sh)):
                        pts = [(p[0] - sh[i][0], p[1]) for p in sh]
                        if all((p[1] in e) if p[0] == 0 else (p[1] in self.sea) for p in pts):
                            out.update(p[0] for p in pts if p[0] != 0)
                            if all(p[0] == 0 or (p[0] < 0 and p[1] == 1) or (p[0] > 0 and p[1] == self.g) for p in pts):
                                in_gadget += 1
        rivbad = sum(1 for c in e for (t, c2) in self.riv.get(c, []) if c2 in self.sea)
        return out, in_gadget, rivbad

    def place(self, edges, N, rng, tries=400, skipB3=False):
        Aof = {e: self.A(e)[0] for e in edges}
        placed = {}; reserved = set(); X = {}
        for e in edges:
            for t in range(tries):
                x = rng.randint(1, N)
                cols = {x + a for a in Aof[e]} | {x}
                if cols & reserved: continue                       # (B1)
                bad = False
                for c in e:                                        # (B2)
                    for (t2, c2) in self.riv.get(c, []):
                        f = placed.get(x + t2)
                        if f is not None and c2 in f: bad = True
                if bad: continue
                if not skipB3:
                    for c in e:                                    # (B3)
                        for rel in self.anch[c]:
                            ok = True; other = False
                            for dx, y in rel:
                                f = e if dx == 0 else placed.get(x + dx)
                                if f is not None and y in f:
                                    if f is not e: other = True
                                elif y not in self.sea:
                                    ok = False; break
                            if ok and other: bad = True; break
                        if bad: break
                if bad: continue
                placed[x] = e; reserved |= cols; X[e] = x
                break
            else:
                return None
        return X, Aof

def obstruction_shapes(h):
    tsh = tilted_shapes(h); ms = max(max(p[0] for p in s) for s in tsh)
    trip = corner_triples(tsh); quads, riv = mixed_and_rivals(h, ms)
    return tsh, list(trip | set(norm(t) for t in quads)), riv

def parity_edges(h): return [(r, s) for r in range(1, h + 1, 2) for s in range(2, h + 1, 2)]

def find_place(blk, edges, rng, skipB3=False):
    N = 8 * len(edges) + 8
    while True:
        for attempt in range(3):
            res = blk.place(rng.sample(edges, len(edges)), N, rng, skipB3=skipB3)
            if res: return N, res
        N = int(N * 1.4) + 1

def test_even(h, seed=0, variants=4, sabotage=False):
    rng = random.Random(seed); g = h
    tsh, shapes, riv = obstruction_shapes(h)
    blk = Block(h, g, shapes, riv); edges = parity_edges(h)
    assert all(good(e, g, h) for e in edges)
    stats = [blk.A(e) for e in edges]
    print("h=%d even: max|A_e|=%d (bound %d), max|a|=%d (2W=%d), private obstructions inside gadget=%d, rival with sea=%d"
          % (h, max(len(s[0]) for s in stats), 2 ** 14 * tmax(h), max(max(map(abs, s[0])) for s in stats if s[0]), 2 * W(h),
             sum(s[1] for s in stats), sum(s[2] for s in stats)), flush=True)
    N, (X, Aof) = find_place(blk, edges, rng, skipB3=(sabotage == "noB3"))
    res = []
    for v in range(variants):
        m = (N, max(X.values()), N + 2 * W(h) + 3, N + 7)[v % 4]
        if m < max(X.values()): m = max(X.values())
        cols = []
        for x in range(1, m + 1):
            mode = v % 3
            cols.append([1] if mode == 0 else [g] if mode == 1 and v < 2 else [rng.choice((1, g))])
        if sabotage != "noA":
            for e, x in X.items():
                for a in Aof[e]:
                    if 1 <= x + a <= m: cols[x + a - 1] = [1] if a < 0 else [g]
        for e, x in X.items(): cols[x - 1] = list(e)
        assert sum(map(len, cols)) == m + q(h)
        res.append((m, valid_fast(blk_from(cols, h), h, m, tsh)))
    print("   window N=%d, sabotage=%s, (m, collisions): %s" % (N, sabotage, res), flush=True)

def test_odd(h, seed=0, sabotage=False):
    rng = random.Random(seed)
    tsh, shapes, riv = obstruction_shapes(h)
    gs = [h - 1, h - 3, h - 1, h - 3]
    blks = {g: Block(h, g, shapes, riv) for g in set(gs)}
    E = [[], [], [], []]
    for e in parity_edges(h):
        if good(e, h - 1, h): E[0].append(e)
        elif good(e, h - 3, h): E[1].append(e)
        elif good(rho(e, h), h - 1, h): E[2].append(e)
        elif good(rho(e, h), h - 3, h): E[3].append(e)
        else: raise Exception("claim fails")
    print("h=%d odd: block sizes %s" % (h, [len(x) for x in E]))
    w = W(h); s = 1; cols = {}; starts = []; Ns = []; pres = {}; dbl = {}
    for k in range(4):
        edges = E[k] if k < 2 else [rho(e, h) for e in E[k]]
        if edges:
            N, (X, Aof) = find_place(blks[gs[k]], edges, rng)
        else: N, X, Aof = 1, {}, {}
        starts.append(s); Ns.append(N)
        for e, x in X.items():
            xe = s - 1 + x
            ee = e if k < 2 else rho(e, h)
            assert xe not in dbl; dbl[xe] = list(ee)
            for a in Aof[e]:
                assert abs(a) <= 2 * w
                row = (1 if a < 0 else gs[k]) if k < 2 else (h if a < 0 else h + 1 - gs[k])
                assert pres.get(xe + a, row) == row; pres[xe + a] = row
        s = s + N + 8 * w
    z = starts[2] - 4 * w
    M = starts[3] + Ns[3] - 1
    assert not (set(pres) & set(dbl))
    assert len(dbl) == q(h) and len(set(map(tuple, dbl.values()))) == q(h)
    out = []
    for m in (M, M + 3 * w):
        c = []
        for x in range(1, m + 1):
            if x in dbl: c.append(dbl[x])
            elif x in pres and sabotage != "noA": c.append([pres[x]])
            else: c.append([1] if x < z else [h])
        assert sum(map(len, c)) == m + q(h)
        out.append((m, valid_fast(blk_from(c, h), h, m, tsh)))
    print("   M=%d, sabotage=%s, (m, collisions): %s" % (M, sabotage, out), flush=True)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "enum": test_enumerator()
    elif cmd == "seas": test_seas(int(sys.argv[2]))
    elif cmd == "spacing": test_spacing_W()
    elif cmd == "lemmas": test_lemmas(int(sys.argv[2]))
    elif cmd == "claim": test_claim(int(sys.argv[2]))
    elif cmd == "even":
        test_even(int(sys.argv[2]), seed=int(sys.argv[3]), sabotage=(sys.argv[4] if len(sys.argv) > 4 else False))
    elif cmd == "odd":
        test_odd(int(sys.argv[2]), seed=int(sys.argv[3]), sabotage=(sys.argv[4] if len(sys.argv) > 4 else False))
