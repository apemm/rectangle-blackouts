from math import isqrt
from collections import Counter
from chk import analyse

def GT_adj(T, h):
    D = set()
    for d in range(1, h):
        for sg in (1, -1):
            L2 = 20 * d * d + sg * 4 * T * d + T * T
            L = isqrt(L2)
            if L * L == L2 and 0 < L < h:
                D.add(d)
    return D

def greedy_class(h, s, iota8, excl_rows=(), mod=8):
    A = (h + 1) // 2; K = h // 2; T = 2 * s + 1
    Dset = GT_adj(T, h); cls = []
    for i in range(1, A):
        if i % mod == iota8 % mod and 0 <= i + s < K and 2 * i + 1 not in excl_rows \
                and not any(abs(i - k) in Dset for k in cls):
            cls.append(i)
    return cls

def build(h, W, r0, blocks, rowfun):
    """blocks: list of (M, s, slots). rowfun(n) -> row of filler in deep column 4n (or None)."""
    S = set(); lab = {}; kinds = {}
    labcols = {}
    for (M, s, slots) in blocks:
        for i in slots:
            labcols[i + M] = (i, s)
    for x in range(W):
        if x % 4:
            S.add((x, r0)); kinds[(x, r0)] = 'S'; continue
        n = x // 4
        if n in labcols:
            i, s = labcols[n]
            S.add((x, 2 * i + 1)); kinds[(x, 2 * i + 1)] = 'Lo'
            S.add((x, 2 * (i + s) + 2)); kinds[(x, 2 * (i + s) + 2)] = 'Le'
            continue
        y = rowfun(n)
        S.add((x, y)); kinds[(x, y)] = 'F'
    return S, kinds

def report(S, kinds, h, W, verbose=0):
    pts, tr, mx, rv = analyse(S, h, W)
    C = Counter(); ex = {}
    tag = lambda q: kinds.get(q, '?')
    seen = set()
    parkedW = {}
    for r in tr:
        V = (r[0], r[1]); P1 = (r[2], r[3]); P2 = (r[4], r[5]); Wc = (r[6], r[7]); kind = r[8]
        key = frozenset([V, P1, P2, Wc])
        if kind == 0:
            if key in seen: continue
            seen.add(key)
        lab = 'T' + ['V1', 'fatal', 'parked'][kind] + ':' + tag(V) + ';' + ','.join(sorted([tag(P1), tag(P2)]))
        if kind == 2:
            parkedW.setdefault(Wc, []).append(lab)
            C[lab] += 1
            continue
        C[lab] += 1; ex.setdefault(lab, (V, P1, P2, Wc))
    for Wc, v in parkedW.items():
        if len(v) >= 2:
            lab = 'V3:' + '|'.join(sorted(v)); C[lab] += 1; ex.setdefault(lab, Wc)
    for r in mx:
        A, B, Cc, D = (pts[r[0]], pts[r[1]], pts[r[2]], pts[r[3]])
        horiz = 'h' if A[1] == B[1] else 't'
        lab = 'M' + horiz + ':' + ''.join(sorted([tag(A), tag(B)])) + '/' + ''.join(sorted([tag(Cc), tag(D)]))
        C[lab] += 1; ex.setdefault(lab, (A, B, Cc, D, (r[4], r[5]), (r[6], r[7])))
    for r in rv:
        a, b = pts[r[0]], pts[r[1]]
        lab = 'R:' + ''.join(sorted([tag(a), tag(b)]))
        C[lab] += 1; ex.setdefault(lab, (a, b, r[2]))
    return C, ex
