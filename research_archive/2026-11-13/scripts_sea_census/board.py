# Board construction for the census: one region type of sea_row3_split.md Corollary B,
# rigid stride-4 layout (rigid_layout_cross_block.md), BH16 deep layer (deep_layer_bh16.md).
# Kinds: 0 white, 1 shallow S, 2 base filler F, 3 hole filler H, 4 label odd o, 5 label even e.
from math import isqrt
import numpy as np

def gt_edges(T, h):
    """d > 0 with 20 d^2 + 4 T d + T^2 = L^2, 0 < L < h."""
    out = set()
    for d in range(1, h):
        v = 20 * d * d + 4 * T * d + T * T
        if v <= 0:
            continue
        L = isqrt(v)
        if L * L == v and 0 < L < h:
            out.add(d)
    return out

def build(h, iota, mu, kappa, p, nu, extra_split=1, margin=None, keep_s1=False,
          drop=()):
    A = (h + 1) // 2
    K = h // 2
    r0 = 1 if iota % 2 == 1 else 3
    r1 = (2 * iota + 1) % 16
    R = max(y for y in range(1, h + 1) if y % 16 == r1)
    rho = R - 8
    nup = (iota + mu) % 2
    mod = 2 ** nu
    inv = pow(p, -1, mod) if mod > 1 else 0
    classes = []          # (s, list of slots)
    for s in range(-(A - 1), K):
        if (s - kappa - mu) % 2:
            continue
        T = 2 * s + 1
        slots = [i for i in range(A) if 0 <= i + s < K]
        E = gt_edges(T, h)
        col = {}
        for i in slots:
            used = {col[i - d] for d in E if (i - d) in col}
            c = 0
            while c in used:
                c += 1
            col[i] = c
        bycol = {}
        for i in slots:
            if i % 8 != iota:
                continue
            j = i + s
            if i == 0:
                continue
            if iota % 2 == 0 and (i == 2 or j in (0, 1)):
                continue
            if not keep_s1 and (2 * i + 1) in (R, R - 16):
                continue
            if (i, j) in drop:
                continue
            key = (col[i], (i // 8) % extra_split) if extra_split > 1 else col[i]
            bycol.setdefault(key, []).append(i)
        for c in sorted(bycol, key=str):
            classes.append((s, bycol[c]))
    cnt = {}
    blocks = []           # (s, slots, pos)
    for (s, sl) in classes:
        base = (inv * (s - kappa)) % mod
        k = cnt.get(base, 0)
        cnt[base] = k + 1
        pos = base + mod * k
        blocks.append((s, sl, pos))
    Xmax = (h - 1) ** 2 // 4 + h + 4
    if margin is None:
        margin = Xmax + 8
    labels = []           # (x, y_odd, y_even, block index, i, j)
    for b, (s, sl, pos) in enumerate(blocks):
        M = p * pos
        for i in sl:
            labels.append((4 * (i + M), 2 * i + 1, 2 * (i + s) + 2, b, i, i + s))
    xs = [L[0] for L in labels]
    x0 = min(xs) - margin
    x0 -= x0 % 4
    x1 = max(xs) + margin
    m = x1 - x0 + 1
    kind = np.zeros((m, h + 1), dtype=np.int8)
    blk = -np.ones((m, h + 1), dtype=np.int32)
    labcol = set()
    for (x, yo, ye, b, i, j) in labels:
        X = x - x0
        kind[X, yo] = 4
        kind[X, ye] = 5
        blk[X, yo] = b
        blk[X, ye] = b
        labcol.add(X)
    for X in range(m):
        if X % 4:
            kind[X, r0] = 1
        elif X not in labcol:
            n = (X + x0) // 4
            if n % 2 != nup:
                kind[X, R] = 2
            else:
                kind[X, rho] = 3
    info = dict(h=h, iota=iota, mu=mu, kappa=kappa, p=p, nu=nu, r0=r0, R=R, rho=rho,
                nblocks=len(blocks), nlabels=len(labels), width=m, x0=x0, Xmax=Xmax,
                maxpos=max(b[2] for b in blocks))
    return kind, blk, info, labels, blocks
