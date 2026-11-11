"""Rectangle geometry, a brute-force validity check, and two CNF encodings.

Everything here is written from the definitions. Nothing is imported from the
2026-11-09 folders.

Grid: h rows, m columns. Cell (r, c), 0 <= r < h, 0 <= c < m, has index r*m + c
and SAT variable r*m + c + 1. A rectangle is a set of four cells that are the
corners of a nondegenerate rectangle in the plane (axis-aligned or tilted).
A black set S is valid when no two distinct rectangles R1, R2 have their
symmetric difference inside S. Equivalently, the white corner sets R minus S
are pairwise distinct.
"""
from itertools import combinations
from math import gcd


# ---------------------------------------------------------------- geometry

def rectangles_by_sides(h, m):
    """All rectangles, from a corner and two perpendicular side vectors."""
    out = set()
    for r in range(h):
        for c in range(m):
            for a in range(-(h - 1), h):
                for b in range(-(m - 1), m):
                    if (a, b) == (0, 0):
                        continue
                    r1, c1 = r + a, c + b
                    if not (0 <= r1 < h and 0 <= c1 < m):
                        continue
                    g = gcd(abs(a), abs(b))
                    pa, pb = -b // g, a // g          # primitive perpendicular
                    for sign in (1, -1):
                        k = 1
                        while True:
                            da, db = sign * k * pa, sign * k * pb
                            r2, c2 = r + da, c + db
                            r3, c3 = r1 + da, c1 + db
                            if not (0 <= r2 < h and 0 <= c2 < m
                                    and 0 <= r3 < h and 0 <= c3 < m):
                                break
                            out.add(frozenset((r * m + c, r1 * m + c1,
                                               r2 * m + c2, r3 * m + c3)))
                            k += 1
    assert all(len(R) == 4 for R in out)
    return out


def rectangles_by_diagonals(h, m):
    """All rectangles, as two distinct equal diagonals with a common midpoint."""
    groups = {}
    pts = [(r, c) for r in range(h) for c in range(m)]
    for (p, q) in combinations(pts, 2):
        key = (p[0] + q[0], p[1] + q[1],
               (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
        groups.setdefault(key, []).append((p[0] * m + p[1], q[0] * m + q[1]))
    out = set()
    for diags in groups.values():
        for d1, d2 in combinations(diags, 2):
            out.add(frozenset(d1 + d2))
    assert all(len(R) == 4 for R in out)
    return out


def find_collision(rects, black):
    """Return None if black (a set of cell indices) is valid, else a witness."""
    seen = {}
    for R in rects:
        key = R - black
        if key in seen:
            return (sorted(seen[key]), sorted(R))
        seen[key] = R
    return None


def word_to_black(word, m):
    """'16,36,5' style word (rows numbered from 1) to a set of cell indices."""
    cols = word.split(',') if isinstance(word, str) else list(word)
    assert len(cols) == m
    return frozenset((int(ch) - 1) * m + c for c, col in enumerate(cols) for ch in col)


def black_to_word(black, h, m):
    return ','.join(''.join(str(r + 1) for r in range(h) if r * m + c in black)
                    for c in range(m))


def balanced_partitions(h):
    """All balanced row bipartitions (A, B) with |A| = floor(h/2), unordered."""
    out = []
    for A in combinations(range(h), h // 2):
        B = tuple(r for r in range(h) if r not in A)
        if h % 2 == 0 and A > B:
            continue
        out.append((A, B))
    return out


def reflect_partition(part, h):
    A, B = (tuple(sorted(h - 1 - r for r in side)) for side in part)
    if h % 2 == 0 and A > B:
        A, B = B, A
    return (A, B)


# ---------------------------------------------------------------- encoding

class CNF:
    def __init__(self, nvars):
        self.nv = nvars
        self.clauses = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, clause):
        self.clauses.append(list(clause))

    def at_most_one(self, lits):
        lits = list(lits)
        if len(lits) <= 5:
            for a, b in combinations(lits, 2):
                self.add((-a, -b))
            return
        # ladder: s_i is forced true once one of lits[0..i] is true
        prev = None
        for i, l in enumerate(lits):
            if prev is not None:
                self.add((-l, -prev))
            if i == len(lits) - 1:
                break
            s = self.new()
            self.add((-l, s))
            if prev is not None:
                self.add((-prev, s))
            prev = s

    def at_least_k(self, lits, k):
        """Counter: s[i][j] true forces at least j true among lits[:i]."""
        lits = list(lits)
        n = len(lits)
        if k <= 0:
            return
        if k > n:
            self.add(())
            return
        prev = {0: None}            # j -> var; None means constant true
        for i in range(1, n + 1):
            cur = {0: None}
            x = lits[i - 1]
            for j in range(1, min(i, k) + 1):
                if j < k - (n - i):          # not needed for the final target
                    continue
                s = self.new()
                cur[j] = s
                below = prev.get(j)          # s[i-1][j], absent means false
                diag = prev.get(j - 1, 0) if j - 1 in prev else 0
                # s -> below or x
                self.add([-s, x] + ([below] if below else []))
                # s -> below or diag
                if j - 1 == 0:
                    pass                      # diag is constant true
                elif diag:
                    self.add([-s, diag] + ([below] if below else []))
                else:
                    self.add([-s] + ([below] if below else []))
            prev = cur
        self.add((prev[k],))


def validity_clauses(cnf, h, m, rects):
    """Clauses that hold exactly when the black set x is valid.

    Two distinct rectangles share 0, 1 or 2 corners (three corners fix the
    fourth). The symmetric difference lies in S exactly when all corners that
    are not shared are black. The three cases are encoded separately.
    """
    rects = [tuple(sorted(R)) for R in rects]
    rects.sort()
    # no shared corner: at most one rectangle is entirely black
    full = []
    for R in rects:
        b = cnf.new()
        cnf.add([-(p + 1) for p in R] + [b])
        full.append(b)
    cnf.at_most_one(full)
    # one shared corner p (two shared corners are covered again, soundly)
    through = {}
    for R in rects:
        for p in R:
            through.setdefault(p, []).append(R)
    for p, group in sorted(through.items()):
        if len(group) < 2:
            continue
        lits = []
        for R in group:
            t = cnf.new()
            cnf.add([-(q + 1) for q in R if q != p] + [t])
            lits.append(t)
        cnf.at_most_one(lits)
    # two shared corners
    through2 = {}
    for R in rects:
        for pq in combinations(R, 2):
            through2.setdefault(pq, []).append(R)
    for pq, group in sorted(through2.items()):
        for R1, R2 in combinations(group, 2):
            cnf.add([-(q + 1) for q in R1 if q not in pq]
                    + [-(q + 1) for q in R2 if q not in pq])


def encode_direct(h, m, k, rects):
    """Is there a valid black set with at least k cells? No structure assumed."""
    cnf = CNF(h * m)
    validity_clauses(cnf, h, m, rects)
    cnf.at_least_k(range(1, h * m + 1), k)
    return cnf


def encode_structured(h, m, part, rects):
    """Is there a valid equality board for the row bipartition part = (A, B)?

    Equality board: every column has one or two black cells, the two-cell
    columns have their rows in different classes, and each of the |A||B|
    cross pairs is the row pair of exactly one column.
    """
    A, B = part
    cnf = CNF(h * m)
    validity_clauses(cnf, h, m, rects)
    x = lambda r, c: r * m + c + 1
    for c in range(m):
        cnf.add([x(r, c) for r in range(h)])
        for side in (A, B):
            for r1, r2 in combinations(side, 2):
                cnf.add((-x(r1, c), -x(r2, c)))
        for trip in combinations(range(h), 3):
            cnf.add([-x(r, c) for r in trip])
    for a in A:
        for b in B:
            ys = []
            for c in range(m):
                y = cnf.new()
                cnf.add((-y, x(a, c)))
                cnf.add((-y, x(b, c)))
                cnf.add((y, -x(a, c), -x(b, c)))
                ys.append(y)
            cnf.add(ys)
            for y1, y2 in combinations(ys, 2):
                cnf.add((-y1, -y2))
    return cnf


def is_equality_board(black, h, m, part=None):
    """Check the equality structure of a black set directly."""
    cols = [tuple(r for r in range(h) if r * m + c in black) for c in range(m)]
    if any(len(col) not in (1, 2) for col in cols):
        return False
    doubles = sorted(col for col in cols if len(col) == 2)
    for (A, B) in ([part] if part else balanced_partitions(h)):
        want = sorted(tuple(sorted((a, b))) for a in A for b in B)
        if doubles == want:
            return True
    return False


def write_dimacs(cnf, path):
    with open(path, 'w', newline='\n') as fh:
        fh.write(f'p cnf {cnf.nv} {len(cnf.clauses)}\n')
        for cl in cnf.clauses:
            fh.write(' '.join(map(str, cl)) + ' 0\n')


def reflection_classes(h):
    """One balanced partition from each orbit of the row reflection r -> h-1-r."""
    seen, out = set(), []
    for part in balanced_partitions(h):
        if part in seen:
            continue
        out.append(part)
        seen.add(part)
        seen.add(reflect_partition(part, h))
    return out


def encode_window(h, k, part, rects, doubles):
    """Is there a valid h by k board in which every column has one or two black
    cells, two-cell columns join the two classes of part, each cross pair is
    used by at most one column, and at least `doubles` columns have two cells?

    Any k consecutive columns of an equality board for part form such a board,
    because validity passes to sub-boards. UNSAT therefore proves that every
    k-window of an equality board has at most doubles - 1 two-cell columns.
    """
    A, B = part
    cnf = CNF(h * k)
    validity_clauses(cnf, h, k, rects)
    x = lambda r, c: r * k + c + 1
    dbl = []
    for c in range(k):
        cnf.add([x(r, c) for r in range(h)])
        for side in (A, B):
            for r1, r2 in combinations(side, 2):
                cnf.add((-x(r1, c), -x(r2, c)))
        for trip in combinations(range(h), 3):
            cnf.add([-x(r, c) for r in trip])
    ycol = [[] for _ in range(k)]
    for a in A:
        for b in B:
            ys = []
            for c in range(k):
                y = cnf.new()
                cnf.add((-y, x(a, c)))
                cnf.add((-y, x(b, c)))
                cnf.add((y, -x(a, c), -x(b, c)))
                ys.append(y)
                ycol[c].append(y)
            for y1, y2 in combinations(ys, 2):
                cnf.add((-y1, -y2))
    for c in range(k):
        d = cnf.new()
        cnf.add([-d] + ycol[c])
        dbl.append(d)
    cnf.at_least_k(dbl, doubles)
    return cnf


def encode_structured_caps(h, m, part, rects, caps, break_reflection=True):
    """encode_structured plus implied constraints.

    caps: dict window length k -> largest number of two-cell columns in any k
    consecutive columns (each entry must be a proved window bound for part).
    break_reflection: require the column of the first cross pair to lie in the
    left half (middle column included). Column reflection c -> m-1-c preserves
    validity and the equality structure, so no board class is lost.
    """
    A, B = part
    cnf = encode_structured(h, m, part, rects)
    x = lambda r, c: r * m + c + 1
    dbl = []
    for c in range(m):
        d = cnf.new()
        for a in A:
            for b in B:
                cnf.add((d, -x(a, c), -x(b, c)))
        dbl.append(d)
    for k, cap in sorted(caps.items()):
        k = int(k)
        if k > m or cap >= k:
            continue
        for s in range(m - k + 1):
            cnf.at_least_k([-d for d in dbl[s:s + k]], k - cap)
    if break_reflection:
        a, b = A[0], B[0]
        for c in range((m + 1) // 2, m):
            cnf.add((-x(a, c), -x(b, c)))
    return cnf
