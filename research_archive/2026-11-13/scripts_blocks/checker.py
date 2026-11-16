"""Driver: anchored census of (V1)-(V5) on a window board.
A board is given by h, Wd, R1, R2 (local columns 0..Wd-1), and a tag function tag(x, y)."""
import numpy as np
from core import rects_anchor, rects_W, rects_Wcol, mixed_anchor, rivals_anchor, divisor_table

_DIV = {}


def divs(NMAX):
    if NMAX not in _DIV:
        _DIV.clear()
        _DIV[NMAX] = divisor_table(NMAX)
    return _DIV[NMAX]


class Board:
    def __init__(self, h, Wd):
        self.h = h; self.Wd = Wd
        self.R1 = np.full(Wd, -1, dtype=np.int64)
        self.R2 = np.full(Wd, -1, dtype=np.int64)
        self.tags = {}  # (x, y) -> tag string

    def put(self, x, y, tag):
        if self.R1[x] == -1:
            self.R1[x] = y
        elif self.R1[x] != y and self.R2[x] == -1:
            self.R2[x] = y
        elif self.R1[x] != y and self.R2[x] != y:
            raise ValueError('three black points in column %d' % x)
        self.tags[(x, y)] = tag

    def black(self, x, y):
        if x < 0 or x >= self.Wd:
            return None
        return self.R1[x] == y or self.R2[x] == y

    def colrows(self, x):
        return [r for r in (self.R1[x], self.R2[x]) if r != -1]

    def rows(self):
        s = set(self.R1[self.R1 > 0].tolist()) | set(self.R2[self.R2 > 0].tolist())
        return np.array(sorted(s), dtype=np.int64)

    def tag(self, x, y):
        return self.tags.get((x, y), '?')


def parked(board, W):
    """W white; parked iff every black point of W's column has the parity of row(W)."""
    return all((r - W[1]) % 2 == 0 for r in board.colrows(W[0]))


def census(board, black_anchors, white_anchors=(), grid=False, want=('R', 'M', 'V'), req=-1):
    """black_anchors: list of black points; white_anchors: white points W (V2 with W there).
    Returns dict with keys V1, V2, V3, V4, V5 (dicts key -> record), oob count, parked map."""
    h = board.h
    ds, dl = divs(h * h)
    rows = board.rows()
    oob = np.zeros(1, dtype=np.int64)
    rects = {}
    def addrect(r):
        Q = ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))
        key = frozenset(Q)
        if key in rects:
            return
        if grid and any(q[0] < 0 or q[0] >= board.Wd for q in Q):
            return
        rects[key] = Q
    if 'R' in want:
        for (x, y) in black_anchors:
            for r in rects_anchor(board.R1, board.R2, board.Wd, h, rows, ds, dl, x, y, oob, req):
                addrect(r)
        bycol = {}
        for (x, y) in white_anchors:
            bycol.setdefault(x, []).append(y)
        for x, ys in bycol.items():
            for r in rects_Wcol(board.R1, board.R2, board.Wd, h, rows, ds, dl, x, np.array(ys, dtype=np.int64), oob):
                addrect(r)
    V1 = {}; V2 = {}; parkedW = {}
    for key, Q in rects.items():
        wh = [q for q in Q if not board.black(*q)]
        if any(board.black(*q) is None for q in Q):
            oob[0] += 1
            continue
        if not wh:
            V1[key] = Q
        else:
            W = wh[0]
            if parked(board, W):
                parkedW.setdefault(W, set()).add(key)
            else:
                V2[key] = (Q, W)
    V3 = {}
    for W, S in parkedW.items():
        allr = set(S)
        for r in rects_W(board.R1, board.R2, board.Wd, h, rows, ds, dl, W[0], W[1], oob):
            Q = ((r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7]))
            if grid and any(q[0] < 0 or q[0] >= board.Wd for q in Q):
                continue
            allr.add(frozenset(Q))
        if len(allr) >= 2:
            V3[W] = allr
    V4 = {}
    if 'M' in want:
        for (x, y) in black_anchors:
            for role in (0, 1):
                for m in mixed_anchor(board.R1, board.R2, board.Wd, h, rows, ds, dl, x, y, role, oob, req):
                    A, B, C, D, p, q = (m[0], m[1]), (m[2], m[3]), (m[4], m[5]), (m[6], m[7]), (m[8], m[9]), (m[10], m[11])
                    if grid and any(z[0] < 0 or z[0] >= board.Wd for z in (p, q)):
                        continue
                    key = frozenset((A, B, C, D))
                    if key not in V4:
                        V4[key] = (A, B, C, D, p, q)
    V5 = {}
    if 'V' in want:
        for (x, y) in black_anchors:
            for rv in rivals_anchor(board.R1, board.R2, board.Wd, h, rows, x, y, oob):
                key = frozenset(((rv[0], rv[1]), (rv[2], rv[3])))
                if key not in V5:
                    V5[key] = rv
    return dict(V1=V1, V2=V2, V3=V3, V4=V4, V5=V5, parked=parkedW, oob=int(oob[0]))
