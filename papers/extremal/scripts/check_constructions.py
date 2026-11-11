"""Check the constructions of the extremal paper from the definition of a valid blackout.

Points are (column, row), one-based, with (1,1) the top left point. A blackout is a set of
points. It is valid if no 2 distinct rectangles (axis-aligned or tilted) show the same white
corners.

The script checks
  1. the explicit blackouts and test boards of the section on small heights,
  2. the alternating boundary seas with spacing W_h + 1 for 3 <= h <= 8, and spacing W_h
     for the lexicographic order (valid for h = 3, 5, 7, not valid for h = 4, 6, 8),
  3. blackouts built as in the section on the nearly quadratic threshold for 4 <= h <= 14
     and h = 16: each double gets the smallest column that is not bad, with (B1), (B2), (B3)
     tested as defined, the prescribed singletons are set next to each double, and the
     blackout is checked from the definition. At h = 16 a control with only (B1) tested
     gives blackouts that are not valid.

It uses only the standard library and runs in about 2 minutes. Run: py check_constructions.py
"""
import itertools
import math
import os
import random
from collections import defaultdict


def span_bound(h):
    return 1 + (h - 1) ** 2 // 4


def tilted_shapes(h):
    """Tilted rectangles on h rows with leftmost corner in column 0, as 4 corners in cyclic order.

    The leftmost corner is (0, r) and the sides from it are (a, -b) and (c, d) with ac = bd.
    """
    out = []
    for b in range(1, h):
        for d in range(1, h - b):
            n = b * d
            for a in range(1, n + 1):
                if n % a:
                    continue
                c = n // a
                for r in range(1 + b, h - d + 1):
                    out.append(((0, r), (a, r - b), (a + c, r - b + d), (c, r + d)))
    return out


def is_valid(h, m, black):
    """True if the blackout is valid on the h x m grid (m >= 3)."""
    cols = defaultdict(set)
    rows = defaultdict(set)
    for (x, y) in black:
        cols[x].add(y)
        rows[y].add(x)
    # Axis-aligned against axis-aligned: no 4-cycle and no 6-cycle in the row-column graph.
    pair_col = {}
    for x, ys in cols.items():
        for p in itertools.combinations(sorted(ys), 2):
            if p in pair_col:
                return False
            pair_col[p] = x
    adj = defaultdict(set)
    for (a, b) in pair_col:
        adj[a].add(b)
        adj[b].add(a)
    for (a, b) in pair_col:
        for c in adj[a] & adj[b]:
            xs = {pair_col[tuple(sorted(p))] for p in ((a, b), (b, c), (a, c))}
            if len(xs) == 3:
                return False
    # Tilted rectangles: compare presentations with at most 2 points, and look for an
    # axis-aligned rectangle with the same presentation.
    seen = {}
    for shape in tilted_shapes(h):
        span = max(p[0] for p in shape)
        for x0 in range(1, m - span + 1):
            corners = [(x0 + px, py) for (px, py) in shape]
            pres = frozenset(p for p in corners if p not in black)
            if len(pres) >= 3:
                continue
            corners = frozenset(corners)
            if seen.setdefault(pres, corners) != corners:
                return False
            if len(pres) == 1:
                (px, py), = pres
                if any((x, y) in black for y in cols[px] for x in rows[py]):
                    return False
            elif len(pres) == 2:
                p, q = tuple(pres)
                if p[0] == q[0]:
                    if rows[p[1]] & rows[q[1]]:
                        return False
                elif p[1] == q[1]:
                    if cols[p[0]] & cols[q[0]]:
                        return False
                elif (p[0], q[1]) in black and (q[0], p[1]) in black:
                    return False
    return True


def board(word, left=None, right=None):
    """A blackout from its column word, with optional padding (count, row) on each side."""
    columns = []
    if left:
        columns += [str(left[1])] * left[0]
    columns += word.split(',')
    if right:
        columns += [str(right[1])] * right[0]
    black = {(i, int(ch)) for i, w in enumerate(columns, 1) for ch in w}
    return len(columns), black


def check_small_heights():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, '..', 'data', 'seven_row_blackouts.txt')) as fh:
        seven = [line.strip() for line in fh if line.strip() and not line.startswith('#')]
    assert [len(w.split(',')) for w in seven] == [24, 25, 26, 27, 28]
    tail = '16,36,5,25,2,2,14,7,12,27,2,7,67,7,47,7,7,56,45,34,23,1,1,1' + ',2' * 21
    s16 = '36,14,25,6,6,16,6,6,56,45,4,4,4,34,23,12'
    cases = [
        ('S_8', 5, '14,45,25,5,5,34,23,12', 6, None, None),
        ('5x13 test board', 5, '14,45,25,5,5,34,23,12', 6, None, (5, 1)),
        ('S_0', 5, '45,34,123,1,15', 5, None, None),
        ('5x6', 5, '15,12,23,3,34,45', 5, None, None),
        ('5x7', 5, '1,12,23,3,34,45,15', 5, None, None),
        ('6x6', 6, '14,1,12,2,23,3456', 6, None, None),
        ('6x7', 6, '16,1,1,12,2,23,3456', 6, None, None),
        ('6x8', 6, '15,1,123,34,4,4,456,26', 7, None, None),
        ('6x9', 6, '12,23,34,45,6,6,36,56,25', 7, None, None),
        ('6x9 test board', 6, '12,23,34,45,6,6,36,56,25', 7, (7, 1), (7, 1)),
        ('6x15', 6, '56,45,34,23,1,1,14,1,1,12,36,1,25,6,16', 9, None, None),
        ('S_16', 6, s16, 9, None, None),
        ('6x23 test board', 6, s16, 9, None, (7, 1)),
        ('7x7', 7, '17,1,12,2,23,3456,67', 7, None, None),
        ('7x8', 7, '27,367,46,2,6,24,125,16', 8, None, None),
        ('7x38 test board', 7, seven[-1], 12, (10, 7), None),
        ('T (7x45)', 7, tail, 12, None, None),
    ]
    for m in (12, 13, 14):
        word = '16,36,25,12,' + ','.join(['1'] * (m - 8)) + ',23,34,45,56'
        cases.append(('6x%d' % m, 6, word, 8, None, None))
    for word in seven:
        cases.append(('7x%d' % len(word.split(',')), 7, word, 12, None, None))
    for m in range(21, 45):
        cases.append(('T_%d' % m, 7, ','.join(tail.split(',')[:m]), 12, None, None))
    for name, h, word, excess, left, right in cases:
        m, black = board(word, left, right)
        assert len(black) - m == excess, name
        assert is_valid(h, m, black), name
    for m in range(6, 14):
        black = {(i, 1) for i in range(2, m)}
        black |= {(m - 1, 2), (m, 2), (1, 3), (2, 3), (1, 4), (m, 4)}
        assert len(black) == m + 4 and is_valid(4, m, black)
    for h in range(2, 8):
        for m in range(3, 10):
            cross = {(i, 1) for i in range(1, m + 1)} | {(1, j) for j in range(1, h + 1)}
            assert is_valid(h, m, cross)
    print('small heights: %d blackouts, the four-row family for 6 <= m <= 13, and the '
          'boundary cross are valid' % len(cases))


def alternating_seas(h, gap, extra, edges):
    positions = [1 + j * gap for j in range(len(edges))]
    m = positions[-1] + extra
    black = set()
    row, j = 1, 0
    for x in range(1, m + 1):
        if j < len(edges) and x == positions[j]:
            black |= {(x, edges[j][0]), (x, edges[j][1])}
            row = h + 1 - row
            j += 1
        else:
            black.add((x, row))
    return m, black


def check_alternating_seas():
    rng = random.Random(1)
    for h in range(3, 9):
        k = h // 2
        edges = [(a, b) for a in range(1, k + 1) for b in range(k + 1, h + 1)]
        for extra in (0, 3):
            m, black = alternating_seas(h, span_bound(h) + 1, extra, edges)
            assert len(black) == m + h * h // 4 and is_valid(h, m, black)
        m, black = alternating_seas(h, span_bound(h), 0, edges)
        assert is_valid(h, m, black) == (h % 2 == 1)
        if h <= 7:
            for _ in range(5):
                rows = list(range(1, h + 1))
                rng.shuffle(rows)
                shuffled = [tuple(sorted((a, b))) for a in rows[:k] for b in rows[k:]]
                rng.shuffle(shuffled)
                m, black = alternating_seas(h, span_bound(h) + 1, 2, shuffled)
                assert is_valid(h, m, black)
    print('alternating seas: valid with spacing W_h + 1 for 3 <= h <= 8, '
          'with spacing W_h valid for h = 3, 5, 7 and not valid for h = 4, 6, 8')


def normalize(points):
    x0 = min(p[0] for p in points)
    return tuple(sorted((p[0] - x0, p[1]) for p in points))


def obstructions(h):
    """Corner triples and mixed quadruples of the strip, up to horizontal translation."""
    out = set()
    shapes = tilted_shapes(h)
    for shape in shapes:
        for i in range(4):
            out.add(normalize([shape[j] for j in range(4) if j != i]))
        # R_2 tilted with diagonal pq, R_1 any rectangle with the non-vertical side pq.
        for (i, j) in ((0, 2), (1, 3)):
            p, q = shape[i], shape[j]
            c, d = [shape[k] for k in range(4) if k not in (i, j)]
            ux, uy = q[0] - p[0], q[1] - p[1]
            if ux == 0:
                continue
            g = math.gcd(abs(ux), abs(uy))
            nx, ny = -uy // g, ux // g
            for t in range(-h, h + 1):
                a = (p[0] + t * nx, p[1] + t * ny)
                b = (q[0] + t * nx, q[1] + t * ny)
                if t != 0 and 1 <= a[1] <= h and 1 <= b[1] <= h:
                    out.add(normalize([a, b, c, d]))
        # R_1 tilted with side pq, R_2 axis-aligned with diagonal pq.
        for i in range(4):
            p, q = shape[i], shape[(i + 1) % 4]
            a, b = shape[(i + 3) % 4], shape[(i + 2) % 4]
            out.add(normalize([a, b, (p[0], q[1]), (q[0], p[1])]))
    return out


def rival_pairs(h):
    """Triples (dx, c, c') such that {(0, c), (dx, c')} is a rival pair."""
    out = set()
    for shape in tilted_shapes(h):
        for (i, j) in ((0, 2), (1, 3)):
            p, q = shape[i], shape[j]
            if p[0] == q[0] and (p[1] - q[1]) % 2 == 1:
                c, d = [shape[k] for k in range(4) if k not in (i, j)]
                out.add((d[0] - c[0], c[1], d[1]))
                out.add((c[0] - d[0], d[1], c[1]))
    return out


class Tools:
    """Obstructions of the strip on h rows, indexed by pairs of their points."""

    def __init__(self, h):
        self.h = h
        self.obs = obstructions(h)
        self.rivals = rival_pairs(h)
        self.index = defaultdict(list)
        for s in self.obs:
            for (x1, y1) in s:
                for (x2, y2) in s:
                    if x1 != x2:
                        self.index[(x2 - x1, y1, y2)].append((s, x1))


class Block:
    """A set of parity edges with the sea rows alpha (row 1 or h) and gamma.

    The columns are bad as in the paper: (B1) the translates of the sets A_e and of 0
    intersect, (B2) 2 double points form a rival pair, (B3) a corner triple or a mixed
    quadruple has points in 2 or more doubles, in rows of their edges, and all its other
    points in the sea rows. With full=False only (B1) is tested.
    """

    def __init__(self, alpha, gamma, edges, tools, full=True):
        self.alpha, self.gamma, self.edges = alpha, gamma, list(edges)
        self.sea = {alpha, gamma}
        self.tools, self.full = tools, full
        self.influence = {}
        for e in self.edges:
            offsets = set()
            for s in tools.obs:
                columns = defaultdict(list)
                for (x, y) in s:
                    columns[x].append(y)
                for x0, ys in columns.items():
                    if all(y in e for y in ys) and all(
                            y in self.sea for x, v in columns.items() if x != x0 for y in v):
                        offsets |= {x - x0 for x in columns if x != x0}
            self.influence[e] = offsets

    def prescribed_row(self, offset):
        return self.alpha if offset < 0 else self.gamma

    def bad(self, pos, by_col, taken, new, x):
        """True if column x for the edge new is bad together with the columns in pos."""
        if x in taken or any(x + a in taken for a in self.influence[new]):
            return True
        if not self.full:
            return False
        tools = self.tools
        for f, xf in pos.items():
            dx = xf - x
            for c in new:
                for c2 in f:
                    if (dx, c, c2) in tools.rivals:
                        return True
                    for (s, shift) in tools.index.get((dx, c, c2), ()):
                        columns = defaultdict(list)
                        for (px, py) in s:
                            columns[px + x - shift].append(py)
                        ok = True
                        for col, rows in columns.items():
                            if col == x:
                                ok = all(r in new for r in rows)
                            elif col == xf:
                                ok = all(r in f for r in rows)
                            elif col in by_col:
                                t = by_col[col]
                                ok = all(r in t for r in rows) or all(r in self.sea for r in rows)
                            else:
                                ok = all(r in self.sea for r in rows)
                            if not ok:
                                break
                        if ok:
                            return True
        return False

    def first_fit(self, order):
        """Give each edge, in the given order, the smallest column that is not bad."""
        pos, by_col, taken = {}, {}, set()
        for e in order:
            x = 1
            while self.bad(pos, by_col, taken, e, x):
                x += 1
            pos[e] = x
            by_col[x] = e
            taken |= {x} | {x + a for a in self.influence[e]}
        return pos


def good(h, e, g):
    r = [y for y in e if y % 2][0]
    if max(e) > g:
        return False
    return all(math.isqrt(j * (g - r + j)) ** 2 != j * (g - r + j)
               for j in range(1, min(h - g, r - 1) + 1))


def parity_edges(h):
    return [tuple(sorted((r, s))) for r in range(1, h + 1, 2) for s in range(2, h + 1, 2)]


def split_edges(h):
    """The sea rows and the 4 sets of edges of the proof (1 set for even h)."""
    edges = parity_edges(h)
    if h % 2 == 0:
        return [(1, h)], [edges]
    groups = [[], [], [], []]
    for e in edges:
        mirror = tuple(sorted((h + 1 - e[0], h + 1 - e[1])))
        if good(h, e, h - 1):
            groups[0].append(e)
        elif h >= 9 and good(h, e, h - 3):
            groups[1].append(e)
        elif good(h, mirror, h - 1):
            groups[2].append(e)
        elif h >= 9 and good(h, mirror, h - 3):
            groups[3].append(e)
        else:
            raise RuntimeError('edge %s is not covered' % (e,))
    return [(1, h - 1), (1, h - 3), (h, 2), (h, 4)], groups


def threshold_board(h, tools, rng, full=True, random_sea=False):
    """A blackout as in the proof of the threshold theorem, cut after its last double.

    Even h: 1 block with the sea rows 1 and h. Odd h: up to 4 blocks, 8 W_h columns apart,
    with the free singletons in row 1 before column z and in row h from column z on.
    Returns the width, the blackout, and the number of doubles in each block.
    """
    seas, groups = split_edges(h)
    wide = span_bound(h)
    layout = []
    start = 1
    for k, group in enumerate(groups):
        width = 1
        pos = {}
        block = None
        if group:
            block = Block(seas[k][0], seas[k][1], group, tools, full)
            order = list(group)
            rng.shuffle(order)
            pos = block.first_fit(order)
            width = max(pos.values())
        layout.append((block, pos, start, width))
        start += width + 8 * wide
    m = layout[-1][2] + layout[-1][3] - 1
    while layout and layout[-1][0] is None:
        layout.pop()
        m = layout[-1][2] + layout[-1][3] - 1
    z = layout[2][2] - 4 * wide if len(layout) > 2 else m + 1
    doubles, fixed = {}, {}
    for block, pos, first, width in layout:
        if block is None:
            continue
        for e in block.edges:
            doubles[first - 1 + pos[e]] = e
            for a in block.influence[e]:
                fixed[first - 1 + pos[e] + a] = block.prescribed_row(a)
    assert not set(doubles) & set(fixed)
    black = set()
    for x in range(1, m + 1):
        if x in doubles:
            black |= {(x, y) for y in doubles[x]}
        elif x in fixed:
            black.add((x, fixed[x]))
        elif h % 2 == 0:
            black.add((x, rng.choice((1, h)) if random_sea else 1))
        else:
            black.add((x, 1 if x < z else h))
    assert len(black) == m + h * h // 4
    return m, black, [len(g) for g in groups]


def check_threshold_construction():
    """Blackouts of the threshold theorem with (B1), (B2), (B3) enforced, checked from the
    definition. Also a control with only (B1) enforced at height 16."""
    rng = random.Random(7)
    for h in (4, 5, 6, 7, 8, 9, 10, 11):
        tools = Tools(h)
        for trial in range(2):
            m, black, sizes = threshold_board(h, tools, rng, random_sea=(trial == 1))
            assert is_valid(h, m, black)
        print('threshold construction: h = %d valid (last width %d, blocks %s)' % (h, m, sizes))
    for h in (12, 13, 14, 16):
        tools = Tools(h)
        best = None
        for trial in range(3):
            m, black, sizes = threshold_board(h, tools, rng)
            assert is_valid(h, m, black)
            if best is None or m < best:
                best = m
        q = h * h // 4
        print('threshold construction: h = %d, 3 blackouts valid, smallest width %d, blocks %s, '
              'explicit construction %d' % (h, best, sizes, q + (q - 1) * span_bound(h)))
        if h == 16:
            invalid = 0
            for trial in range(5):
                m, black, sizes = threshold_board(h, tools, rng, full=False)
                invalid += not is_valid(h, m, black)
            print('control at h = 16 with only (B1) enforced: %d of 5 blackouts are not valid'
                  % invalid)


if __name__ == '__main__':
    check_small_heights()
    check_alternating_seas()
    check_threshold_construction()
