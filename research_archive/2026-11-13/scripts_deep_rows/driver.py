import numpy as np
from collections import Counter, defaultdict
from board import shapes, tilted_scan, mixed_scan, rival_scan

ROLE = {0: '.', 1: 'S', 2: 'F', 3: 'o', 4: 'e'}

def build(h, Wd, labels, filler_row):
    """labels: list of (x, odd_row, even_row) with x%4==0. filler_row(n) -> row (or None)."""
    kind = np.zeros((Wd, h + 2), dtype=np.int64)
    labcols = set()
    for (x, ro, re) in labels:
        kind[x, ro] = 3; kind[x, re] = 4; labcols.add(x)
    for x in range(Wd):
        if x % 4:
            kind[x, 1] = 1
        elif x not in labcols:
            r = filler_row(x // 4)
            if r is not None:
                kind[x, r] = 2
    return kind

def analyse(h, kind, S=None, verbose=False, only_filler=True):
    Wd = kind.shape[0]
    blk = (kind > 0).astype(np.int64)
    if S is None:
        S = shapes(h)
    W = (h * h) // 4 + 1
    pts = np.argwhere(kind > 0)
    ptsx = pts[:, 0].astype(np.int64); ptsy = pts[:, 1].astype(np.int64)
    colblack = defaultdict(list)
    for x, y in zip(ptsx, ptsy):
        colblack[int(x)].append(int(y))
    res = Counter(); ex = defaultdict(list)
    # tilted
    T = tilted_scan(blk, h, Wd, S)
    parked_at = defaultdict(list)
    for (x, r, k, nb, w) in T:
        a, b, c, d = S[k]
        Q = [(x, r), (x + a, r - b), (x + c, r + d), (x + a + c, r - b + d)]
        roles = [ROLE[kind[q]] for q in Q]
        blackroles = ''.join(sorted(roles[i] for i in range(4) if i != w)) if w >= 0 else ''.join(sorted(roles))
        hasF = 'F' in roles
        if nb == 4:
            key = 'V1:' + blackroles
        else:
            Wp = Q[w]
            par = Wp[1] % 2
            parked = all((yy % 2) == par for yy in colblack[Wp[0]])
            if not parked:
                key = 'V2:' + blackroles
            else:
                parked_at[Wp].append((tuple(Q), hasF, blackroles))
                key = None
        if key and (hasF or not only_filler):
            res[key] += 1
            if len(ex[key]) < 3: ex[key].append(Q)
    for Wp, L in parked_at.items():
        if len(L) >= 2 and (any(f for _, f, _ in L) or not only_filler):
            key = 'V3:' + '|'.join(sorted(br for _, _, br in L))
            res[key] += 1
            if len(ex[key]) < 3: ex[key].append((Wp, [q for q, _, _ in L]))
    # mixed
    M = mixed_scan(blk, h, Wd, S, ptsx, ptsy, W)
    seen = set()
    for (ax, ay, bx, by, cx, cy, dx, dy) in M:
        sup = frozenset([(ax, ay), (bx, by), (cx, cy), (dx, dy)])
        if sup in seen: continue
        seen.add(sup)
        rAB = ''.join(sorted([ROLE[kind[ax, ay]], ROLE[kind[bx, by]]]))
        rCD = ''.join(sorted([ROLE[kind[cx, cy]], ROLE[kind[dx, dy]]]))
        hasF = 'F' in rAB + rCD
        if hasF or not only_filler:
            key = 'V4:' + rAB + '/' + rCD
            res[key] += 1
            if len(ex[key]) < 3: ex[key].append(((ax, ay), (bx, by), (cx, cy), (dx, dy)))
    R = rival_scan(h, ptsx, ptsy, 2 * W)
    for (cx, cy, dx, dy, jj) in R:
        rr = ''.join(sorted([ROLE[kind[cx, cy]], ROLE[kind[dx, dy]]]))
        if 'F' in rr or not only_filler:
            key = 'V5:' + rr
            res[key] += 1
            if len(ex[key]) < 3: ex[key].append(((cx, cy), (dx, dy), jj))
    return res, ex
