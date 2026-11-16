# Definition-level census: distinct rectangles must have distinct presentations
# (paper Definition valid, Lemma diff). Every tilted rectangle with >= 2 black corners
# inside the board is enumerated from a black pair (side or diagonal). Axis-aligned
# rectangles are matched by rule, assuming the rest of the full board carries every
# parity edge {odd, even} as a double far away (this is the paper's situation; rows of
# the doubles are the only thing that matters for an axis rectangle).
import numpy as np
from numba import njit

@njit(cache=True)
def isq(v):
    if v < 0:
        return -1
    r = int(np.sqrt(v))
    while r * r > v:
        r -= 1
    while (r + 1) * (r + 1) <= v:
        r += 1
    if r * r == v:
        return r
    return -1

@njit(cache=True)
def gcd(a, b):
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

@njit(cache=True)
def enum(kind, h, Xmax, px, py, fill, out2, out3, out4):
    """fill=False: count only. Records:
    out2[r] = (id W1, id W2, id P, id Q, mode)   two black corners P,Q; mode 0 side, 1 diagonal
    out3[r] = (id W, id B1, id B2, id V)          V opposite W
    out4[r] = (id a, id b, id c, id d)            fully black tilted
    """
    m = kind.shape[0]
    H1 = h + 1
    n = px.shape[0]
    c2 = 0; c3 = 0; c4 = 0
    for a in range(n):
        xa = px[a]; ya = py[a]
        b = a + 1
        while b < n and px[b] - xa <= Xmax:
            xb = px[b]; yb = py[b]
            dx = xb - xa; dy = yb - ya
            # side mode
            if dx != 0 and dy != 0:
                g = gcd(dx, dy)
                wx = -dy // g; wy = dx // g      # wy > 0
                kmin = -100000; kmax = 100000
                for yy in (ya, yb):
                    lo = -((yy - 1) // wy)       # ceil((1-yy)/wy)
                    hi = (h - yy) // wy
                    if lo > kmin: kmin = lo
                    if hi < kmax: kmax = hi
                for k in range(kmin, kmax + 1):
                    if k == 0:
                        continue
                    x1 = xa + k * wx; y1 = ya + k * wy
                    x2 = xb + k * wx; y2 = yb + k * wy
                    if x1 < 0 or x1 >= m or x2 < 0 or x2 >= m:
                        continue
                    if kind[x1, y1] == 0 and kind[x2, y2] == 0:
                        if fill:
                            i1 = x1 * H1 + y1; i2 = x2 * H1 + y2
                            if i1 > i2:
                                i1, i2 = i2, i1
                            out2[c2, 0] = i1; out2[c2, 1] = i2
                            out2[c2, 2] = xa * H1 + ya; out2[c2, 3] = xb * H1 + yb
                            out2[c2, 4] = 0
                        c2 += 1
            # diagonal mode
            D2 = dx * dx + dy * dy
            sx = xa + xb; sy = ya + yb
            ymaxv = min(sy - 2, 2 * h - sy)
            for Y in range(0, ymaxv + 1):
                if (Y - sy) % 2 != 0:
                    continue
                r = isq(D2 - Y * Y)
                if r < 0:
                    continue
                for sgn in (1, -1):
                    X = sgn * r
                    if Y == 0 and X <= 0:
                        continue
                    if sgn == -1 and r == 0:
                        continue
                    if (X - sx) % 2 != 0:
                        continue
                    if (X == dx and Y == dy) or (X == -dx and Y == -dy):
                        continue
                    if (X == dx and Y == -dy) or (X == -dx and Y == dy):
                        continue   # axis-aligned
                    x1 = (sx + X) // 2; y1 = (sy + Y) // 2
                    x2 = (sx - X) // 2; y2 = (sy - Y) // 2
                    if x1 < 0 or x1 >= m or x2 < 0 or x2 >= m:
                        continue
                    if y1 < 1 or y1 > h or y2 < 1 or y2 > h:
                        continue
                    k1 = kind[x1, y1]; k2 = kind[x2, y2]
                    i1 = x1 * H1 + y1; i2 = x2 * H1 + y2
                    ia = xa * H1 + ya; ib = xb * H1 + yb
                    if k1 == 0 and k2 == 0:
                        if fill:
                            if i1 > i2:
                                i1, i2 = i2, i1
                            out2[c2, 0] = i1; out2[c2, 1] = i2
                            out2[c2, 2] = ia; out2[c2, 3] = ib
                            out2[c2, 4] = 1
                        c2 += 1
                    elif k1 == 0 or k2 == 0:
                        if fill:
                            if k1 == 0:
                                out3[c3, 0] = i1; out3[c3, 3] = i2
                            else:
                                out3[c3, 0] = i2; out3[c3, 3] = i1
                            out3[c3, 1] = ia; out3[c3, 2] = ib
                        c3 += 1
                    else:
                        if ia < i1 and ia < i2:
                            if fill:
                                out4[c4, 0] = ia; out4[c4, 1] = ib
                                out4[c4, 2] = i1; out4[c4, 3] = i2
                            c4 += 1
            b += 1
    return c2, c3, c4

@njit(cache=True)
def axis2(kind, h, rec):
    """1 if some axis-aligned rectangle presents the white pair rec[0], rec[1]."""
    H1 = h + 1
    x1 = rec[0] // H1; y1 = rec[0] % H1
    x2 = rec[1] // H1; y2 = rec[1] % H1
    if x1 == x2:
        return 1 if (y1 - y2) % 2 != 0 else 0
    if y1 == y2:
        for yy in range(1, h + 1):
            if yy != y1 and kind[x1, yy] != 0 and kind[x2, yy] != 0:
                return 1
        return 0
    if kind[x1, y2] != 0 and kind[x2, y1] != 0:
        return 1
    return 0

@njit(cache=True)
def axis3(kind, h, w):
    H1 = h + 1
    x = w // H1; y = w % H1
    for yy in range(1, h + 1):
        if kind[x, yy] != 0 and (yy - y) % 2 != 0:
            return 1
    return 0

@njit(cache=True)
def axis_all(kind, h, out2, n2, out3, n3, f2, f3):
    for r in range(n2):
        f2[r] = axis2(kind, h, out2[r])
    for r in range(n3):
        f3[r] = axis3(kind, h, out3[r, 0])

def run(kind, h, Xmax):
    xs, ys = np.nonzero(kind)
    order = np.lexsort((ys, xs))
    px = xs[order].astype(np.int64); py = ys[order].astype(np.int64)
    d2 = np.zeros((1, 5), np.int64); d3 = np.zeros((1, 4), np.int64); d4 = np.zeros((1, 4), np.int64)
    c2, c3, c4 = enum(kind, h, Xmax, px, py, False, d2, d3, d4)
    out2 = np.zeros((max(c2, 1), 5), np.int64)
    out3 = np.zeros((max(c3, 1), 4), np.int64)
    out4 = np.zeros((max(c4, 1), 4), np.int64)
    enum(kind, h, Xmax, px, py, True, out2, out3, out4)
    out2 = out2[:c2]; out3 = out3[:c3]; out4 = out4[:c4]
    f2 = np.zeros(c2, np.int8); f3 = np.zeros(c3, np.int8)
    axis_all(kind, h, out2, c2, out3, c3, f2, f3)
    viol = []
    H1 = h + 1
    # V1
    for r in out4:
        viol.append(('V1', tuple(int(v) for v in r), None))
    # 3-black: axis (fatal triple) and V3 (two tilted at the same W)
    for r in np.nonzero(f3)[0]:
        viol.append(('V2', tuple(int(v) for v in out3[r, 1:]), int(out3[r, 0])))
    if c3:
        key = out3[:, 0]
        o = np.argsort(key, kind='stable')
        ks = key[o]
        dup = np.nonzero(ks[1:] == ks[:-1])[0]
        seen = set()
        for d in dup:
            k = int(ks[d])
            if k in seen:
                continue
            seen.add(k)
            rows = o[np.nonzero(ks == k)[0]]
            blacks = []
            for rr in rows:
                blacks.append(tuple(int(v) for v in out3[rr, 1:]))
            viol.append(('V3', tuple(blacks), k))
    # 2-black: axis match and tilted-tilted
    for r in np.nonzero(f2)[0]:
        viol.append(('A2', (int(out2[r, 2]), int(out2[r, 3])), (int(out2[r, 0]), int(out2[r, 1]), int(out2[r, 4]))))
    if c2:
        key = out2[:, 0] * (np.int64(1) << 31) + out2[:, 1]
        o = np.argsort(key, kind='stable')
        ks = key[o]
        dup = np.nonzero(ks[1:] == ks[:-1])[0]
        seen = set()
        for d in dup:
            k = int(ks[d])
            if k in seen:
                continue
            seen.add(k)
            rows = o[np.nonzero(ks == k)[0]]
            recs = [(int(out2[rr, 2]), int(out2[rr, 3]), int(out2[rr, 4])) for rr in rows]
            viol.append(('T2', tuple(recs), (int(out2[rows[0], 0]), int(out2[rows[0], 1]))))
    stats = dict(rect2=c2, rect3=c3, rect4=c4, black=len(px))
    return viol, stats
