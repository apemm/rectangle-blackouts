"""Window boards for L*** and the family classifier (table of consolidated_board.md section 4)."""
import numpy as np
from checker import census


class WinBoard:
    """Columns X0..X0+Wd-1 (global). deep(n) -> row, sea row r0, label slots dict n -> (i, j).
    Optional seam: deep slots n >= nseam (right buffer) or n < nseam (left buffer) take row g."""
    def __init__(self, h, X0, Wd, tp, rho0, labels=None, seam=None, g=None):
        self.h = h; self.X0 = X0; self.Wd = Wd; self.tp = tp; self.rho0 = rho0
        self.labels = labels or {}
        self.seam = seam; self.g = g
        X = X0 + np.arange(Wd, dtype=np.int64)
        n = X // 4
        R1 = np.where(X % 4 != 0, tp['r0'], tp['Ts'] - 24 + 8 * ((n - rho0) % 4)).astype(np.int64)
        if seam is not None:
            side, ns = seam
            buf = (X % 4 == 0) & ((n >= ns) if side == 'R' else (n < ns))
            R1[buf] = g
        R2 = np.full(Wd, -1, dtype=np.int64)
        for nn, (i, j) in self.labels.items():
            x = 4 * nn - X0
            assert 0 <= x < Wd
            R1[x] = 2 * i + 1; R2[x] = 2 * j + 2
        self.R1 = R1; self.R2 = R2

    def black(self, x, y):
        if x < 0 or x >= self.Wd:
            return None
        return self.R1[x] == y or self.R2[x] == y

    def colrows(self, x):
        return [r for r in (self.R1[x], self.R2[x]) if r != -1]

    def rows(self):
        return np.unique(np.concatenate([self.R1, self.R2[self.R2 > 0]])).astype(np.int64)

    def tag(self, x, y):
        X = x + self.X0
        if X % 4:
            return 'S'
        n = X // 4
        if n in self.labels:
            i, j = self.labels[n]
            return 'o' if y == 2 * i + 1 else ('e' if y == 2 * j + 2 else '?')
        if self.seam is not None:
            side, ns = self.seam
            if (n >= ns) if side == 'R' else (n < ns):
                return 'g'
        return 'F%d' % ((n - self.rho0) % 4)

    def islabelcol(self, x):
        X = x + self.X0
        return X % 4 == 0 and X // 4 in self.labels

    def label_of(self, x):
        return self.labels.get((x + self.X0) // 4)


def letter(t):
    return 'F' if t.startswith('F') else t


def comp(tags):
    return ''.join(sorted(letter(t) for t in tags))


def family_rect(bd, Q, W, kind):
    """Q: 4 corners; W: white corner or None. kind 'V1' or 'V2'."""
    blackc = [q for q in Q if q != W]
    tg = [bd.tag(*q) for q in blackc]
    c = comp(tg)
    nl = sum(1 for t in tg if t in 'oe')
    nS = c.count('S'); nF = c.count('F'); ng = c.count('g')
    Wlab = W is not None and bd.islabelcol(W[0])
    det = c + ('|Wlab' if Wlab else '')
    if W is not None:
        iw = Q.index(W); V = Q[(iw + 2) % 4]
        det += '|vert=' + letter(bd.tag(*V))
        if bd.tp['r0'] == 3 and W[1] <= 2 and nS == 0:
            det += '|W in rows 1-2'
    if ng:
        return 'E1(seam)', det
    if nl >= 3:
        return 'A1', det
    if nl == 0:
        return ('pure, W in label column' if Wlab else 'C2(pure)'), det
    if nS >= 1:
        if nl == 2:
            return 'B1(SLL fatal)', det
        return 'SLF fatal (D8/D9 parked types; Cor D)', det
    if nl == 1 and nF == 2:
        return ('D2/D7 (FFo)' if 'o' in c else 'D2/D6 (FFe, CE)'), det
    if nl == 2 and nF == 1:
        if 'o' in c and 'e' in c:
            return 'D5 (Feo)', det
        return 'D6 (Fee/Foo)', det
    return 'UNLISTED', det


def family_mixed(bd, A, B, C, D, p, q):
    ta, tb, tc, td = (bd.tag(*z) for z in (A, B, C, D))
    side = ''.join(sorted(letter(t) for t in (ta, tb))); diag = ''.join(sorted(letter(t) for t in (tc, td)))
    det = side + '/' + diag
    allt = side + diag
    nl = sum(allt.count(x) for x in 'oe'); nF = allt.count('F'); ng = allt.count('g')
    sh_side = sum(1 for t in (ta, tb) if t == 'S'); sh_diag = sum(1 for t in (tc, td) if t == 'S')
    low = min(p[1], q[1]) <= 2
    row3 = bd.tp['r0'] == 3
    extra = ''
    if row3 and low and sh_side + sh_diag == 0:
        extra = ' +D21(p/q in rows 1-2)'
    if ng:
        return 'E1(seam)' + extra, det
    if nl == 0:
        return 'C2(pure)' + extra, det
    if nl == 4:
        return 'A3' + extra, det
    if sh_side + sh_diag:
        if sh_side == 2 and sh_diag == 0:
            return 'B4 (M2a)', det
        if sh_side == 1 and sh_diag == 1:
            deep = [t for t in (ta, tb, tc, td) if t != 'S']
            dl = comp(deep)
            if dl == 'oo':
                return 'B6 (in-class oo M2c, R_IV)', det
            if dl == 'ee':
                return 'B5 (in-class ee M2c)', det
            if 'F' in dl and nl == 1:
                return 'D11 (M2c label+filler)', det
            return 'UNLISTED (M2c)', det
        if sh_side == 0 and sh_diag == 1:
            return 'B4 (M1C)', det
        return 'UNLISTED (shallow pattern not in Thm 2)', det
    if nl == 1 and nF == 3:
        if side == 'FF':
            return ('D1 (S2, horizontal FF side)' if A[1] == B[1] else 'D4 (Thm 1(6))') + extra, det
        return 'D4 (Thm 1(6), side LF)' + extra, det
    if nl == 2 and nF == 2:
        if side in ('oo', 'ee', 'eo') or diag in ('oo', 'ee', 'eo'):
            return 'D14 (ll/FF, FF/ll)' + extra, det
        fs = [z for z, t in zip((A, B, C, D), (ta, tb, tc, td)) if t.startswith('F')]
        Ls = [z for z, t in zip((A, B), (ta, tb)) if t in 'oe'][0]
        Ld = [z for z, t in zip((C, D), (tc, td)) if t in 'oe'][0]
        if fs[0][1] == fs[1][1]:
            dsign = 'd>0' if Ld[1] > Ls[1] else 'd<0'
            return ('D12 (homog., d>0)' if dsign == 'd>0' else 'D13 (homog., d<0)') + extra, det
        return 'D15 (inhomog. 2L2F, Q2)' + extra, det
    if nl == 3 and nF == 1:
        lab = comp([t for t in (ta, tb, tc, td) if t in 'oe'])
        if lab == 'ooo':
            return 'D19 (3L1F ooo)' + extra, det
        if lab == 'eeo':
            return 'D20 (3L1F oee, Q3)' + extra, det
        return 'UNLISTED (3L1F parity)' + extra, det
    return 'UNLISTED' + extra, det


def family_rival(bd, C, D):
    c = comp([bd.tag(*C), bd.tag(*D)])
    if 'g' in c:
        return 'E1(seam)', c
    if c == 'eo':
        return 'A2', c
    if c == 'Fe':
        return 'D10', c
    if c == 'Se':
        return 'B8', c
    if 'o' not in c and 'e' not in c:
        return 'C2(pure)', c
    return 'UNLISTED', c


def run(bd, black_anchors, white_anchors, req=-1):
    res = census(bd, black_anchors, white_anchors, req=req)
    out = []
    for key, Q in res['V1'].items():
        f, d = family_rect(bd, Q, None, 'V1')
        out.append(('V1', f, d, Q))
    for key, (Q, W) in res['V2'].items():
        f, d = family_rect(bd, Q, W, 'V2')
        out.append(('V2', f, d, (Q, W)))
    for W, S in res['V3'].items():
        cs = []
        for R in S:
            cs.append(comp([bd.tag(*z) for z in R if z != W]))
        cs = '|'.join(sorted(cs))
        if all(x == 'SLL' or (x.count('S') == 1 and sum(x.count(y) for y in 'oe') == 2) for x in cs.split('|')):
            f = 'B3 (V3 of SLL)'
        elif 'g' in cs:
            f = 'E1(seam)'
        elif all(sum(x.count(y) for y in 'oe') == 0 for x in cs.split('|')):
            f = 'C2(pure)'
        else:
            f = 'D8/D22 (V3 with label+filler)'
        out.append(('V3', f, cs, (W, sorted(sorted(R) for R in S))))
    for key, (A, B, C, D, p, q) in res['V4'].items():
        f, d = family_mixed(bd, A, B, C, D, p, q)
        out.append(('V4', f, d, (A, B, C, D, p, q)))
    for key, rv in res['V5'].items():
        C = (rv[0], rv[1]); D = (rv[2], rv[3])
        f, d = family_rival(bd, C, D)
        out.append(('V5', f, d, rv))
    return out, res['oob']
