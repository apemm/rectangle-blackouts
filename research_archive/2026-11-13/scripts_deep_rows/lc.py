"""Label-centric obstruction finder (criterion V1-V5), numba.
kind[x, y]: 0 white, 1 sea (row r0, x%4!=0), 2 filler, 3 label odd, 4 label even.  y in 1..h.
Finds every obstruction that contains a label point, or a tilted rectangle whose white corner
lies in a label column, plus V3 collisions involving such triples (with any other parked triple)."""
import numpy as np
from numba import njit
from math import isqrt

@njit(cache=True)
def gcd(a, b):
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

@njit(cache=True)
def isq(n):
    if n < 0:
        return -1
    r = int(np.sqrt(n))
    while r * r > n: r -= 1
    while (r + 1) * (r + 1) <= n: r += 1
    return r if r * r == n else -1

@njit(cache=True)
def rects_at(kind, cb, cn, h, Wd, zx, zy, reach, need_black_anchor):
    """All tilted rectangles with >= 3 black corners having corner Z=(zx,zy).
    Returns (x0,y0,x1,y1,x2,y2,x3,y3) with corners Z, P, R, Q in cyclic order (Z,P,R,Q)."""
    out = []
    zb = kind[zx, zy] > 0
    for px in range(max(0, zx - reach), min(Wd, zx + reach + 1)):
        vx = px - zx
        if vx == 0:
            continue
        for ii in range(cn[px]):
            py = cb[px, ii]
            vy = py - zy
            if vy == 0:
                continue
            g = gcd(vx, vy)
            if abs(vx) > h * g:
                continue
            wx = -vy // g; wy = vx // g
            for sgn in (1, -1):
                k = sgn
                while True:
                    qx = zx + k * wx; qy = zy + k * wy
                    rx = px + k * wx; ry = py + k * wy
                    if qy < 1 or qy > h or ry < 1 or ry > h:
                        # rows move monotonically in k; once both out we stop
                        if (qy < 1 or qy > h) and (ry < 1 or ry > h):
                            break
                        k += sgn
                        continue
                    if qx < 0 or qx >= Wd or rx < 0 or rx >= Wd:
                        break
                    nb = (1 if zb else 0) + 1 + (1 if kind[qx, qy] > 0 else 0) + (1 if kind[rx, ry] > 0 else 0)
                    if nb >= 3:
                        out.append((zx, zy, px, py, rx, ry, qx, qy))
                    k += sgn
    return out

@njit(cache=True)
def mixed_cd(kind, cb, cn, h, Wd, cx, cy, reach):
    """Mixed quadruples with C = (cx,cy) black (label point) and D any black point. Output A,B,C,D,p,q."""
    out = []
    for dx in range(max(0, cx - reach), min(Wd, cx + reach + 1)):
        for ii in range(cn[dx]):
            dy = cb[dx, ii]
            if dx == cx and dy == cy:
                continue
            # p on Thales circle of CD: (px-cx)(px-dx) + (py-cy)(py-dy) = 0
            sx = cx + dx; Dx = dx - cx
            for py in range(1, h + 1):
                qy = cy + dy - py
                if qy < 1 or qy > h:
                    continue
                disc = Dx * Dx - 4 * (py - cy) * (py - dy)
                s = isq(disc)
                if s < 0:
                    continue
                if (sx + s) % 2:
                    continue
                for sg in (1, -1):
                    if s == 0 and sg == -1:
                        continue
                    px = (sx + sg * s) // 2
                    qx = sx - px
                    if (px == cx and py == cy) or (px == dx and py == dy):
                        continue
                    ux = qx - px; uy = qy - py
                    if ux == 0:
                        continue
                    g = gcd(ux, uy)
                    nx0 = -uy // g; ny0 = ux // g
                    for sgn in (1, -1):
                        t = sgn
                        while True:
                            nx = t * nx0; ny = t * ny0
                            ax = px - nx; ay = py - ny; bx = qx - nx; by = qy - ny
                            if (ay < 1 or ay > h) and (by < 1 or by > h):
                                break
                            if ay >= 1 and ay <= h and by >= 1 and by <= h and ax >= 0 and ax < Wd and bx >= 0 and bx < Wd:
                                if kind[ax, ay] > 0 and kind[bx, by] > 0:
                                    # exclude D-C = +-(B-A)
                                    if not ((dx - cx == bx - ax and dy - cy == by - ay) or (dx - cx == ax - bx and dy - cy == ay - by)):
                                        out.append((ax, ay, bx, by, cx, cy, dx, dy, px, py, qx, qy))
                            t += sgn
                            if abs(t) > 4 * h:
                                break
    return out

@njit(cache=True)
def mixed_ab(kind, cb, cn, h, Wd, ax, ay, reach):
    """Mixed quadruples with A = (ax,ay) black (label point), B any black point, AB not vertical."""
    out = []
    for bx in range(max(0, ax - reach), min(Wd, ax + reach + 1)):
        ux = bx - ax
        if ux == 0:
            continue
        for ii in range(cn[bx]):
            by = cb[bx, ii]
            uy = by - ay
            g = gcd(ux, uy)
            nx0 = -uy // g; ny0 = ux // g
            for sgn in (1, -1):
                t = sgn
                while True:
                    nx = t * nx0; ny = t * ny0
                    px = ax + nx; py = ay + ny; qx = bx + nx; qy = by + ny
                    if (py < 1 or py > h) and (qy < 1 or qy > h):
                        break
                    if abs(t) > 4 * h:
                        break
                    t += sgn
                    if py < 1 or py > h or qy < 1 or qy > h:
                        continue
                    # C on Thales circle of pq
                    sx = px + qx; Dx = qx - px
                    for cy in range(1, h + 1):
                        dy = py + qy - cy
                        if dy < 1 or dy > h:
                            continue
                        disc = Dx * Dx - 4 * (cy - py) * (cy - qy)
                        s = isq(disc)
                        if s < 0 or (sx + s) % 2:
                            continue
                        for sg in (1, -1):
                            if s == 0 and sg == -1:
                                continue
                            cx = (sx + sg * s) // 2
                            dx = sx - cx
                            if cx < 0 or cx >= Wd or dx < 0 or dx >= Wd:
                                continue
                            if (cx == px and cy == py) or (cx == qx and cy == qy):
                                continue
                            if kind[cx, cy] > 0 and kind[dx, dy] > 0:
                                if not ((dx - cx == ux and dy - cy == uy) or (dx - cx == -ux and dy - cy == -uy)):
                                    if not ((cx == ax and cy == ay) or (cx == bx and cy == by) or (dx == ax and dy == ay) or (dx == bx and dy == by)):
                                        out.append((ax, ay, bx, by, cx, cy, dx, dy, px, py, qx, qy))
    return out

@njit(cache=True)
def rivals_at(kind, cb, cn, h, Wd, cx, cy, reach):
    out = []
    for dx in range(max(0, cx - reach), min(Wd, cx + reach + 1)):
        t = dx - cx
        if t == 0 or t % 2:
            continue
        for ii in range(cn[dx]):
            dy = cb[dx, ii]
            d = abs(dy - cy)
            if d % 2 == 0:
                continue
            lo = min(cy, dy); hi = max(cy, dy)
            L = isq(d * d + t * t)
            if L < 0:
                continue
            jj = (L - d) // 2
            if jj >= 1 and lo - jj >= 1 and hi + jj <= h:
                out.append((cx, cy, dx, dy, jj))
    return out
