"""Driver for the label-centric checker.
usage: py lcd.py h iota8 s_list off_list [excl_rows|-] [r0] [verbose]
Region with odd iota8 (row-1 sea, r0=1) or row-3 sea (r0=3).  Labels i = iota8 mod 8, 1 <= i < A,
0 <= i+s < K, at n = i + M (one block), odd row 2i+1, even row 2(i+s)+2.
Filler row at slot n: R0 + 8*off[(n - base) % P], base = iota8 + M, R0 = max{y<=h: y = 2*iota8+1 mod 16}."""
import sys, time, os
LM = int(os.environ.get('LM', '8'))
KEEP = float(os.environ.get('KEEP', '1'))
import random as _r
_rng = _r.Random(int(os.environ.get('SEED', '1')))
import numpy as np
from collections import Counter, defaultdict
from lc import rects_at, mixed_cd, mixed_ab, rivals_at

ROLE = {0: '.', 1: 'S', 2: 'F', 3: 'o', 4: 'e'}

def build(h, iota8, s, off, excl, r0=1, Mx=None, rowfun=None):
    A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota8 + 1) % 16
    R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
    W = h * h // 4 + 4 * h
    M = (((W + 16) // 4) // 16) * 16 + 16 if Mx is None else Mx
    base = iota8 + M; P = len(off)
    Wd = 4 * (M + A) + W + 16
    kind = np.zeros((Wd, h + 2), dtype=np.int64)
    labs = []
    for i in range(1, A):
        thr = excl[0] if (len(excl) == 1 and excl[0] < 0) else None
        bad = ((2 * i + 1) >= -thr or 2 * (i + s) + 2 >= -thr) if thr is not None else ((2 * i + 1) in excl)
        if r0 == 3 and (i == 2 or i + s in (0, 1)):
            bad = True
        if i % LM == iota8 and 0 <= i + s < K and not bad and _rng.random() < KEEP:
            labs.append((4 * (i + M), 2 * i + 1, 2 * (i + s) + 2))
    labcols = set(x for x, _, _ in labs)
    for (x, ro, re) in labs:
        kind[x, ro] = 3; kind[x, re] = 4
    for x in range(Wd):
        if x % 4:
            kind[x, r0] = 1
        elif x not in labcols:
            n = x // 4
            y = rowfun(n - base) if rowfun else R0 + 8 * off[(n - base) % P]
            kind[x, y] = 2
    cb = np.full((Wd, 3), -1, dtype=np.int64); cn = np.zeros(Wd, dtype=np.int64)
    for x in range(Wd):
        ys = np.nonzero(kind[x] > 0)[0]
        cn[x] = len(ys); cb[x, :len(ys)] = ys
    return kind, cb, cn, labs, (R0, M, base, Wd)

def analyse(h, kind, cb, cn, labs, verbose=False):
    Wd = kind.shape[0]
    res = Counter(); ex = defaultdict(list)
    def tag(Q): return ROLE[kind[Q[0], Q[1]]]
    labcols = set(x for x, _, _ in labs)
    def parked(W):
        return all((cb[W[0], i] % 2) == (W[1] % 2) for i in range(cn[W[0]]))
    seen = set(); parkedW = defaultdict(set)
    reachT = h * h
    for (x, _, _) in labs:
        for y in range(1, h + 1):
            for r in rects_at(kind, cb, cn, h, Wd, x, y, reachT, False):
                Q = [(r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7])]
                key = frozenset(Q)
                if key in seen: continue
                seen.add(key)
                wh = [q for q in Q if kind[q[0], q[1]] == 0]
                if not wh:
                    k = 'V1:' + ''.join(sorted(tag(q) for q in Q))
                else:
                    Wp = wh[0]
                    br = ''.join(sorted(tag(q) for q in Q if q != Wp))
                    if parked(Wp):
                        parkedW[Wp].add(key); continue
                    k = 'V2:' + br + ('|Wlab' if Wp[0] in labcols else '')
                res[k] += 1
                if len(ex[k]) < 3: ex[k].append(Q)
    for Wp, S in parkedW.items():
        allr = set(S)
        for r in rects_at(kind, cb, cn, h, Wd, Wp[0], Wp[1], reachT, False):
            allr.add(frozenset([(r[0], r[1]), (r[2], r[3]), (r[4], r[5]), (r[6], r[7])]))
        if len(allr) >= 2:
            k = 'V3:' + '|'.join(sorted(''.join(sorted(tag(q) for q in R if q != Wp)) for R in allr))
            res[k] += 1
            if len(ex[k]) < 3: ex[k].append((Wp, [sorted(R) for R in allr]))
    reachM = h * h // 4 + 4 * h
    seenM = set()
    for (x, ro, re) in labs:
        for y in (ro, re):
            for fn in (mixed_cd, mixed_ab):
                for m in fn(kind, cb, cn, h, Wd, x, y, reachM):
                    A, B, C, D = (m[0], m[1]), (m[2], m[3]), (m[4], m[5]), (m[6], m[7])
                    sup = frozenset([A, B, C, D])
                    if len(sup) < 4 or sup in seenM: continue
                    seenM.add(sup)
                    k = 'V4:' + ''.join(sorted([tag(A), tag(B)])) + '/' + ''.join(sorted([tag(C), tag(D)]))
                    res[k] += 1
                    if len(ex[k]) < 3: ex[k].append((A, B, C, D, (m[8], m[9]), (m[10], m[11])))
            for rv in rivals_at(kind, cb, cn, h, Wd, x, y, 2 * h):
                k = 'V5:' + ''.join(sorted([tag((rv[0], rv[1])), tag((rv[2], rv[3]))]))
                res[k] += 1
                if len(ex[k]) < 3: ex[k].append(rv)
    return res, ex

if __name__ == '__main__':
    h = int(sys.argv[1]); iota8 = int(sys.argv[2])
    ss = [int(a) for a in sys.argv[3].split(',')]
    off = [int(a) for a in sys.argv[4].split(',')]
    excl = [int(a) for a in sys.argv[5].split(',')] if len(sys.argv) > 5 and sys.argv[5] != '-' else []
    r0 = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    verbose = len(sys.argv) > 7
    t = time.time(); tot = Counter(); nl = 0
    for s in ss:
        kind, cb, cn, labs, info = build(h, iota8, s, off, excl, r0)
        res, ex = analyse(h, kind, cb, cn, labs)
        nl += len(labs); tot.update(res)
        print('s', s, 'labels', [(l[1], l[2]) for l in labs], info[:3], dict(sorted(res.items())), 'time %.1f' % (time.time() - t), flush=True)
        if verbose:
            for k in sorted(res):
                for e in ex[k]: print('      ', k, e)
    print('h', h, 'off', off, 'labels', nl, 'total', sum(tot.values()), dict(sorted(tot.items())), 'time %.1f' % (time.time() - t))
