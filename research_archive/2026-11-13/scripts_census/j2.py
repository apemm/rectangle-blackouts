"""Buffer pieces and buffer-chain seams of (B9)/(P8), and the switch z (row-1 tail | row-h tail).
Pieces: tail1 (row 1 everywhere), Sea(1,g), allg (row g everywhere), Sea(3,g), tailh (row h).
Pieces are 4-periodic: anchor one period. Seams: anchor every black point within 2W_h+8 left of
the seam (any obstruction meeting both sides contains such a point).  usage: py j2.py h"""
import sys, time
import numpy as np
from collections import Counter
from lstar import params, g_of
from checker import census

h = int(sys.argv[1]); W = params(h)['W']; g = g_of(h)
def piece(name, X):
    if name == 'tail1': return np.ones_like(X)
    if name == 'tailh': return np.full_like(X, h)
    if name == 'allg': return np.full_like(X, g)
    r0 = 1 if name == 'sea1' else 3
    return np.where(X % 4 != 0, r0, g)
class B:
    pass
def board(left, right, Xs):
    marg = 4 * W + 64
    X = Xs - marg + np.arange(2 * marg)
    R1 = np.where(X < Xs, piece(left, X), piece(right, X)).astype(np.int64)
    b = B(); b.h = h; b.Wd = len(X); b.R1 = R1; b.R2 = np.full(len(X), -1, dtype=np.int64); b.X0 = Xs - marg
    b.black = lambda x, y: None if x < 0 or x >= b.Wd else (b.R1[x] == y)
    b.colrows = lambda x: [int(b.R1[x])]
    b.rows = lambda: np.array(sorted(set(b.R1.tolist())), dtype=np.int64)
    return b, marg
t0 = time.time()
seams = [('tail1', 'sea1'), ('sea1', 'allg'), ('allg', 'sea3'), ('sea3', 'allg'), ('allg', 'sea1'), ('sea1', 'tail1'), ('tail1', 'tailh')]
for name in ('tail1', 'sea1', 'allg', 'sea3', 'tailh'):
    b, marg = board(name, name, 4 * 10 ** 6)
    res = census(b, [(x, int(b.R1[x])) for x in range(marg, marg + 4)])
    n = sum(len(res[k]) for k in ('V1', 'V2', 'V3', 'V4', 'V5'))
    print('piece', name, 'violations', n, {k: len(res[k]) for k in ('V1', 'V2', 'V3', 'V4', 'V5')}, 'parked', sum(len(s) for s in res['parked'].values()), 'oob', res['oob'], flush=True)
for (L, R) in seams:
    for ph in range(4):
        Xs = 4 * 10 ** 6 + ph
        b, marg = board(L, R, Xs)
        anc = [(x, int(b.R1[x])) for x in range(marg - 2 * W - 8, marg)]
        res = census(b, anc)
        # keep only obstructions meeting both sides
        def both(pts): return min(p[0] for p in pts) < marg <= max(p[0] for p in pts)
        cnt = {}
        cnt['V1'] = sum(1 for k in res['V1'] if both(k)); cnt['V2'] = sum(1 for k in res['V2'] if both(k))
        cnt['V3'] = sum(1 for W_, S in res['V3'].items() if both([z for R_ in S for z in R_]))
        cnt['V4'] = sum(1 for k in res['V4'] if both(k)); cnt['V5'] = sum(1 for k in res['V5'] if both(k))
        print('seam', L, '|', R, 'seam column mod 4 =', ph, 'crossing violations', cnt, 'anchors', len(anc), 'oob', res['oob'], 'time %.1f' % (time.time() - t0), flush=True)
