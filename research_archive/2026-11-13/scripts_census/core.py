"""Definition-level obstruction finder, criterion (V1)-(V5), row-set / divisor enumeration.

Board window: columns X0 .. X0+Wd-1 (local index x = 0..Wd-1), rows 1..h.
R1[x], R2[x]: black rows of column x (-1 if none); every column has <= 2 black points.
rows: sorted array of all distinct rows that hold a black point in the window.
dstart, dlist: CSR table of positive divisors of n, n = 1..NMAX.

Enumerations are anchored at one black point P (or one white point W) and are complete:
 - rects_anchor: every tilted rectangle of the grid (rows 1..h) with >= 3 black corners that
   has P as a black corner (P as the vertex adjacent to two black corners, or P adjacent to such
   a vertex).
 - rects_W: every tilted rectangle with corner W whose other three corners are black.
 - mixed_anchor: every black mixed quadruple (A,B,C,D) (AB side, CD diagonal, AB not vertical)
   with P = A (role 0) or P = C (role 1). By the symmetries A<->B, C<->D this covers every
   black mixed quadruple containing P.
 - rivals_anchor: every black rival pair containing P.
Points outside the window are counted in oob (must stay 0 when margins are right)."""
import numpy as np
from numba import njit


@njit(cache=True)
def _divfill(NMAX, dstart, dlist):
    pos = dstart.copy()
    for d in range(1, NMAX + 1):
        for m in range(d, NMAX + 1, d):
            dlist[pos[m]] = d
            pos[m] += 1


@njit(cache=True)
def _divcount(NMAX, cnt):
    for d in range(1, NMAX + 1):
        for m in range(d, NMAX + 1, d):
            cnt[m] += 1


def divisor_table(NMAX):
    cnt = np.zeros(NMAX + 1, dtype=np.int64)
    _divcount(NMAX, cnt)
    dstart = np.zeros(NMAX + 2, dtype=np.int64)
    dstart[1:] = np.cumsum(cnt)
    dlist = np.zeros(dstart[-1], dtype=np.int64)
    _divfill(NMAX, dstart, dlist)
    return dstart, dlist


@njit(cache=True)
def isblack(R1, R2, Wd, x, y, oob):
    if x < 0 or x >= Wd:
        oob[0] += 1
        return False
    return R1[x] == y or R2[x] == y


@njit(cache=True)
def isqrt_exact(n):
    if n < 0:
        return -1
    r = int(np.sqrt(n))
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    if r * r == n:
        return r
    return -1


@njit(cache=True)
def rects_anchor(R1, R2, Wd, h, rows, dstart, dlist, px, py, oob, req=-1):
    """Rectangles (as 8-tuples V,F,W,G in cyclic order V-F-W-G) with >=3 black corners, P black corner."""
    out = []
    nr = rows.shape[0]
    # role vertex: P = V, F and G black
    for i1 in range(nr):
        yF = rows[i1]
        bF = yF - py
        if bF == 0:
            continue
        for i2 in range(nr):
            yG = rows[i2]
            bG = yG - py
            if bG == 0:
                continue
            yW = yF + yG - py
            if yW < 1 or yW > h:
                continue
            if req >= 0 and yF != req and yG != req and py != req:
                continue
            N = -bF * bG
            aN = abs(N)
            for k in range(dstart[aN], dstart[aN + 1]):
                d = dlist[k]
                for sg in (1, -1):
                    a = sg * d
                    c = N // a
                    if isblack(R1, R2, Wd, px + a, yF, oob) and isblack(R1, R2, Wd, px + c, yG, oob):
                        out.append((px, py, px + a, yF, px + a + c, yW, px + c, yG))
    # role end: P adjacent to the black vertex V; G the other neighbour of V
    for i1 in range(nr):
        yV = rows[i1]
        bP = py - yV
        if bP == 0:
            continue
        for i2 in range(nr):
            yG = rows[i2]
            bG = yG - yV
            if bG == 0:
                continue
            yW = py + yG - yV
            if yW < 1 or yW > h:
                continue
            if req >= 0 and yV != req and yG != req and py != req:
                continue
            N = -bP * bG
            aN = abs(N)
            for k in range(dstart[aN], dstart[aN + 1]):
                d = dlist[k]
                for sg in (1, -1):
                    a = sg * d          # a = xP - xV
                    xV = px - a
                    xG = xV + N // a
                    if isblack(R1, R2, Wd, xV, yV, oob) and isblack(R1, R2, Wd, xG, yG, oob):
                        out.append((xV, yV, px, py, px + xG - xV, yW, xG, yG))
    return out


@njit(cache=True)
def rects_W(R1, R2, Wd, h, rows, dstart, dlist, wx, wy, oob):
    """Rectangles W,F,V,G with F, V, G black (V opposite W). Output as (V,F,W,G)."""
    out = []
    nr = rows.shape[0]
    for i1 in range(nr):
        yF = rows[i1]
        bF = yF - wy
        if bF == 0:
            continue
        for i2 in range(nr):
            yG = rows[i2]
            bG = yG - wy
            if bG == 0:
                continue
            yV = yF + yG - wy
            if yV < 1 or yV > h:
                continue
            N = -bF * bG
            aN = abs(N)
            for k in range(dstart[aN], dstart[aN + 1]):
                d = dlist[k]
                for sg in (1, -1):
                    a = sg * d
                    c = N // a
                    if isblack(R1, R2, Wd, wx + a, yF, oob) and isblack(R1, R2, Wd, wx + c, yG, oob) \
                            and isblack(R1, R2, Wd, wx + a + c, yV, oob):
                        out.append((wx + a + c, yV, wx + a, yF, wx, wy, wx + c, yG))
    return out


@njit(cache=True)
def _mixed_finish(R1, R2, Wd, h, ax, ay, ux, uy, nx, ny, wx, wy, out, oob, anchor_is_C, cx0):
    # given A (or C if anchor_is_C), u = B-A, n, w = D-C
    t2 = ux + 2 * nx - wx
    if t2 % 2 != 0:
        return
    if anchor_is_C:
        cx = cx0
        axx = cx - t2 // 2
    else:
        axx = ax
        cx = ax + t2 // 2
    bx = axx + ux; by = ay + uy
    cy = (ay + by + 2 * ny - wy) // 2
    dx = cx + wx; dy = cy + wy
    pyy = ay + ny; qyy = by + ny
    if pyy < 1 or pyy > h or qyy < 1 or qyy > h:
        return
    if cy < 1 or cy > h or dy < 1 or dy > h or by < 1 or by > h:
        return
    if (cx == axx and cy == ay) or (cx == bx and cy == by) or (dx == axx and dy == ay) or (dx == bx and dy == by):
        return
    if (wx == ux and wy == uy) or (wx == -ux and wy == -uy):
        return
    if not isblack(R1, R2, Wd, axx, ay, oob):
        return
    if not isblack(R1, R2, Wd, bx, by, oob):
        return
    if not isblack(R1, R2, Wd, cx, cy, oob):
        return
    if not isblack(R1, R2, Wd, dx, dy, oob):
        return
    # p, q columns must be in the window too (grid points); check bounds only
    if axx + nx < 0 or axx + nx >= Wd or bx + nx < 0 or bx + nx >= Wd:
        oob[0] += 1
    out.append((axx, ay, bx, by, cx, cy, dx, dy, axx + nx, pyy, bx + nx, qyy))


@njit(cache=True)
def mixed_anchor(R1, R2, Wd, h, rows, dstart, dlist, px, py, role, oob, req=-1):
    out = [(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)]
    nr = rows.shape[0]
    for i1 in range(nr):
        for i2 in range(nr):
            for i3 in range(nr):
                if role == 0:
                    yA = py; yB = rows[i1]; yC = rows[i2]; yD = rows[i3]
                else:
                    yC = py; yA = rows[i1]; yB = rows[i2]; yD = rows[i3]
                if req >= 0 and yA != req and yB != req and yC != req and yD != req:
                    continue
                s2 = yC + yD - yA - yB
                if s2 % 2 != 0:
                    continue
                ny = s2 // 2
                if ny == 0:
                    continue
                uy = yB - yA
                wy = yD - yC
                Q = wy * wy - uy * uy
                if Q != 0:
                    aQ = abs(Q)
                    for k in range(dstart[aQ], dstart[aQ + 1]):
                        d = dlist[k]
                        for sg in (1, -1):
                            e = sg * d
                            f = Q // e
                            if (e + f) % 2 != 0:
                                continue
                            ux = (e + f) // 2
                            wx = (f - e) // 2
                            if ux == 0:
                                continue
                            if (ny * uy) % ux != 0:
                                continue
                            nx = -(ny * uy) // ux
                            _mixed_finish(R1, R2, Wd, h, px, yA, ux, uy, nx, ny, wx, wy, out, oob, role == 1, px)
                else:
                    if uy == 0:
                        continue
                    M = abs(ny * uy)
                    for k in range(dstart[M], dstart[M + 1]):
                        d = dlist[k]
                        for sg in (1, -1):
                            ux = sg * d
                            nx = -(ny * uy) // ux
                            if wy == uy:
                                wx = -ux
                            else:
                                wx = ux
                            _mixed_finish(R1, R2, Wd, h, px, yA, ux, uy, nx, ny, wx, wy, out, oob, role == 1, px)
    return out[1:]


@njit(cache=True)
def rivals_anchor(R1, R2, Wd, h, rows, px, py, oob):
    out = []
    nr = rows.shape[0]
    for i1 in range(nr):
        yD = rows[i1]
        dd = abs(yD - py)
        if dd % 2 == 0:
            continue
        lo = min(yD, py); hi = max(yD, py)
        j = 1
        while lo - j >= 1 and hi + j <= h:
            v = j * (dd + j)
            r = isqrt_exact(v)
            if r > 0:
                t = 2 * r
                for sg in (1, -1):
                    xD = px + sg * t
                    if isblack(R1, R2, Wd, xD, yD, oob):
                        out.append((px, py, xD, yD, j))
            j += 1
    return out


@njit(cache=True)
def rects_Wcol(R1, R2, Wd, h, rows, dstart, dlist, wx, wys, oob):
    mask = np.zeros(h + 2, dtype=np.bool_)
    for r in rows:
        mask[r] = True
    """rects_W for every white point (wx, y), y in wys."""
    out = [(0, 0, 0, 0, 0, 0, 0, 0)]
    nr = rows.shape[0]
    for t in range(wys.shape[0]):
        wy = wys[t]
        for i1 in range(nr):
            yF = rows[i1]
            bF = yF - wy
            if bF == 0:
                continue
            for i2 in range(nr):
                yG = rows[i2]
                bG = yG - wy
                if bG == 0:
                    continue
                yV = yF + yG - wy
                if yV < 1 or yV > h or not mask[yV]:
                    continue
                N = -bF * bG
                aN = abs(N)
                for k in range(dstart[aN], dstart[aN + 1]):
                    d = dlist[k]
                    for sg in (1, -1):
                        a = sg * d
                        c = N // a
                        if isblack(R1, R2, Wd, wx + a, yF, oob) and isblack(R1, R2, Wd, wx + c, yG, oob) \
                                and isblack(R1, R2, Wd, wx + a + c, yV, oob):
                            out.append((wx + a + c, yV, wx + a, yF, wx, wy, wx + c, yG))
    return out[1:]
