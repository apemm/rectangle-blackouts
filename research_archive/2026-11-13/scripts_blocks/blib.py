"""Definition-level T1 (filled mod-7 profile) blocks for Theorem E / Theorem D, and a windowed
(V1)-(V5) check with the validated census checker (copied core.py / checker.py)."""
import random
from math import isqrt
import numpy as np
from checker import Board, census


def issq(n):
    return n >= 0 and isqrt(n) ** 2 == n


def chi7(x):
    x %= 7
    if x == 0:
        return 0
    return 1 if x in (1, 2, 4) else -1


def profile_ok(h, L, F, H, g):
    if not (1 <= L < F < H <= h):
        return False
    if (F - L) % 2 or (H - L) % 2 == 0:
        return False
    if (H - L - g) % 7 or (F - L - 3 * g) % 7:
        return False
    if any(issq(j * (H - L + j)) for j in range(1, L)):          # (7)
        return False
    if any(issq(j * (H - F + j)) for j in range(1, h - H + 1)):  # (8)
        return False
    m = 2 * max(L - 1, h - H)
    return F - L > m and H - F > m                                # (9)


def row_ok(h, prof, r, exact=True):
    """T1 conditions on one inserted row: residue (4), margins (6), and the vertical-rival filters
    (10).  exact=True uses (10) only where Lemma rival can apply: opposite parity, and
    1 <= j <= min(lower-1, h-upper).  exact=False is T1's literal (10)."""
    L, F, H, g = prof
    if (r - L) % 7 not in (0, (5 * g) % 7):
        return False
    if not (r > F + 2 * (h - H) and r + F < H - L + 2):
        return False
    for s in (L, F, H):
        if exact:
            if (r - s) % 2 == 0:
                continue
            lo, hi = min(r, s), max(r, s)
            J = min(lo - 1, h - hi)
        else:
            J = {L: L - 1, F: F - 1, H: h - H}[s]
        for j in range(1, J + 1):
            if issq(j * (abs(r - s) + j)):
                return False
    return True


def sea(prof, x):
    L, F, H, g = prof
    c = chi7(x)
    return F if c == 0 else (L if c == -1 else H)


def Wh(h):
    return (h - 1) ** 2 // 4 + 1


class Layout:
    """A list of column contents: col[x] = tuple of rows, tag[x] = segment name."""
    def __init__(self, h):
        self.h = h
        self.col = []
        self.tag = []
        self.labels = {}   # x -> label (a, b)

    def x(self):
        return len(self.col)

    def pad7(self, fn, name):
        while len(self.col) % 7:
            self.col.append((fn(len(self.col)),)); self.tag.append(name)

    def seg(self, n, fn, name):
        for _ in range(n):
            self.col.append((fn(len(self.col)),)); self.tag.append(name)


def collar_fns(h, prof):
    """Right-collar stages, in order away from the core (T1 Section 6)."""
    L, F, H, g = prof
    st = [('periodic', lambda x: sea(prof, x)),
          ('fillerH', lambda x: H if chi7(x) == 0 else sea(prof, x)),
          ]
    for y in range(H, h):
        st.append(('const%d' % y, (lambda yy: (lambda x: yy))(y)))
    return st


def build_block(lay, prof, classes, seglen, tail=True):
    """Append one T1 block: [row-h tail] left collar (mirror) | classes separated by periodic sea |
    right collar [row-h tail]. classes: list of (N, {label: slot}). Returns label columns."""
    h = lay.h
    L, F, H, g = prof
    st = collar_fns(h, prof)
    if tail:
        lay.seg(seglen, lambda x: h, 'tail_h')
    for name, fn in reversed(st[1:]):          # left collar: h-1, ..., H, fillerH
        lay.seg(seglen, fn, 'L_' + name)
    lay.seg(seglen, st[0][1], 'L_periodic')
    for ci, (N, place) in enumerate(classes):
        if ci > 0:
            lay.seg(seglen, lambda x: sea(prof, x), 'sep')
        lay.pad7(lambda x: sea(prof, x), 'pad')
        x0 = lay.x()
        inv = {s: e for e, s in place.items()}
        assert len(inv) == len(place), 'slot collision'
        for k in range(N):
            for t in range(7):
                x = lay.x()
                if t == 0 and k in inv:
                    a, b = inv[k]
                    lay.col.append((a, b)); lay.tag.append('label%d' % ci); lay.labels[x] = inv[k]
                else:
                    lay.col.append((sea(prof, x),)); lay.tag.append('core%d' % ci)
    for name, fn in st:
        lay.seg(seglen, fn, 'R_' + name)
    if tail:
        lay.seg(seglen, lambda x: h, 'tail_h')


def to_board(lay, x0, x1):
    b = Board(lay.h, x1 - x0)
    for x in range(x0, x1):
        for y in lay.col[x]:
            b.put(x - x0, y, lay.tag[x])
    return b


def _merge(found, r, x0, skipW=None):
    for k in found:
        for key, val in r[k].items():
            if k == 'V3':
                W = key
                if skipW is not None and W[0] + x0 in skipW:
                    continue
                found[k].add((W[0] + x0, W[1]))
            else:
                if k == 'V2' and skipW is not None and val[1][0] + x0 in skipW:
                    continue
                found[k].add(frozenset((q[0] + x0, q[1]) for q in key))


def check_windows(lay, D, verbose=False):
    """Every obstruction (and V3 pair) lies in D = 2W_h+1 consecutive columns, so the windows
    [a, a+2D), a = 0, D, 2D, ..., cover all of them.  Label-free windows: anchor every black point.
    Windows with label columns: (1) the real board, anchored at every label point, plus white
    anchors on every white cell of every label column; (2) the board with the label columns
    emptied, anchored at every black point, discarding records whose W lies in a label column.
    (1) finds every record with a black point or W in a label column; (2) every other one."""
    h = lay.h
    n = len(lay.col)
    found = {'V1': set(), 'V2': set(), 'V3': set(), 'V4': set(), 'V5': set()}
    stats = []
    a = 0
    while True:
        x0 = a; x1 = min(n, a + 2 * D)
        b = to_board(lay, x0, x1)
        labcols = [x - x0 for x in lay.labels if x0 <= x < x1]
        if not labcols:
            anchors = [(x, y) for x in range(x1 - x0) for y in b.colrows(x)]
            r = census(b, anchors)
            _merge(found, r, x0)
            cnt = {k: len(r[k]) for k in found}
            mode = 'all'
        else:
            anchors = [(x, y) for x in labcols for y in b.colrows(x)]
            whites = [(x, y) for x in labcols for y in range(1, h + 1) if not b.black(x, y)]
            r = census(b, anchors, whites)
            _merge(found, r, x0)
            b2 = to_board(lay, x0, x1)
            for x in labcols:
                b2.R1[x] = -1; b2.R2[x] = -1
            anchors2 = [(x, y) for x in range(x1 - x0) for y in b2.colrows(x)]
            r2 = census(b2, anchors2)
            _merge(found, r2, x0, skipW=set(x + x0 for x in labcols))
            cnt = {k: (len(r[k]), len(r2[k])) for k in found}
            mode = 'label'
        stats.append((x0, x1, mode, cnt))
        if verbose:
            print(x0, x1, mode, cnt, flush=True)
        if x1 >= n:
            break
        a += D
    return found, stats


def vweight(prof, e):
    from sympy import divisor_count
    return 1 + sum(int(divisor_count(abs(r - s))) for r in e for s in prof[:3])


def class_violations(h, prof, D, N, place, strict=False):
    """Census of one class core in the periodic sea (margins D), anchored at label points and at the
    white cells of label columns.  Returns the set of labels involved in some record."""
    lay = Layout(h)
    lay.seg(D, lambda x: sea(prof, x), 'sea'); lay.pad7(lambda x: sea(prof, x), 'pad')
    x0 = lay.x(); inv = {s: e for e, s in place.items()}
    for k in range(N):
        for t in range(7):
            x = lay.x()
            if t == 0 and k in inv:
                lay.col.append(inv[k]); lay.tag.append('label'); lay.labels[x] = inv[k]
            else:
                lay.col.append((sea(prof, x),)); lay.tag.append('core')
    lay.seg(D, lambda x: sea(prof, x), 'sea')
    b = to_board(lay, 0, len(lay.col))
    lc = list(lay.labels)
    anchors = [(x, y) for x in lc for y in lay.col[x]]
    whites = [(x, y) for x in lc for y in range(1, h + 1) if y not in lay.col[x]]
    r = census(b, anchors, whites)
    inv_x = lay.labels
    hit = set(); nrec = 0
    for k in ('V1', 'V2', 'V4', 'V5'):
        for key in r[k]:
            nrec += 1
            for q in key:
                if q[0] in inv_x:
                    hit.add(inv_x[q[0]])
            if k == 'V2':
                W = r[k][key][1]
                if W[0] in inv_x:
                    hit.add(inv_x[W[0]])
    for W, S in r['V3'].items():
        nrec += 1
        if W[0] in inv_x:
            hit.add(inv_x[W[0]])
        for key in S:
            for q in key:
                if q[0] in inv_x:
                    hit.add(inv_x[q[0]])
    npk = 0
    for W, S in r['parked'].items():
        for key in S:
            ls = set(inv_x[q[0]] for q in key if q[0] in inv_x and q != W)
            if len(ls) >= 1:
                npk += 1
                if strict:
                    nrec += 1; hit |= ls
    cnt = {k: len(r[k]) for k in ('V1', 'V2', 'V3', 'V4', 'V5')}
    cnt['parked_with_label'] = npk
    return hit, nrec, cnt


def place_class(h, prof, D, labs, N, rng, maxit=200, log=None, strict=False):
    """Random injective centres in {0..N-1}; resample the labels of every record (Moser-Tardos
    style) until the class has no record.  This is the existence step of the local lemma."""
    slots = rng.sample(range(N), len(labs))
    place = dict(zip(labs, slots))
    hist = []
    for it in range(maxit):
        hit, nrec, cnt = class_violations(h, prof, D, N, place, strict)
        hist.append((nrec, len(hit), cnt))
        if nrec == 0:
            return place, hist
        free = sorted(set(range(N)) - set(place.values()))
        for e in hit:
            s = rng.choice(free); free.remove(s); free.append(place[e]); place[e] = s
    return None, hist
