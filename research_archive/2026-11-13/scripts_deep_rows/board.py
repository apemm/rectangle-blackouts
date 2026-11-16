"""Brute-force obstruction finder for a strip board (columns 0..Wd-1, rows 1..h).
kind[x,y]: 0 white, 1 shallow (row 1, x%4!=0), 2 filler, 3 label odd, 4 label even.
Finds: tilted rectangles with >=3 black corners (fully black, fatal triple, parked triple),
V3 collisions, mixed quadruples (side AB not vertical), rival pairs.
"""
import numpy as np
from numba import njit

def shapes(h):
    L = []
    for b in range(1, h):
        for d in range(1, h - b):
            n = b * d
            for a in range(1, n + 1):
                if n % a == 0:
                    L.append((a, b, n // a, d))
    return np.array(L, dtype=np.int64)

@njit(cache=True)
def tilted_scan(blk, h, Wd, S):
    # returns rows: x, r, shape index, nblack, white corner index
    out = []
    for x in range(Wd):
        for r in range(1, h + 1):
            for k in range(S.shape[0]):
                a, b, c, d = S[k, 0], S[k, 1], S[k, 2], S[k, 3]
                if r - b < 1 or r + d > h or x + a + c >= Wd:
                    continue
                q0 = blk[x, r]; q1 = blk[x + a, r - b]; q2 = blk[x + c, r + d]; q3 = blk[x + a + c, r - b + d]
                nb = q0 + q1 + q2 + q3
                if nb >= 3:
                    w = -1
                    if q0 == 0: w = 0
                    elif q1 == 0: w = 1
                    elif q2 == 0: w = 2
                    elif q3 == 0: w = 3
                    out.append((x, r, k, nb, w))
    return out

@njit(cache=True)
def gcd(a, b):
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

@njit(cache=True)
def mixed_from_diag(blk, h, Wd, px, py, qx, qy, cx, cy, dx, dy, out):
    sx = qx - px; sy = qy - py
    if sx == 0:
        return
    g = gcd(sx, sy)
    ux = -sy // g; uy = sx // g
    for t in range(-2 * h, 2 * h + 1):
        if t == 0:
            continue
        nx = t * ux; ny = t * uy
        ax = px - nx; ay = py - ny; bx = qx - nx; by = qy - ny
        if ay < 1 or ay > h or by < 1 or by > h:
            continue
        if ax < 0 or ax >= Wd or bx < 0 or bx >= Wd:
            continue
        if blk[ax, ay] and blk[bx, by]:
            out.append((ax, ay, bx, by, cx, cy, dx, dy))

@njit(cache=True)
def mixed_scan(blk, h, Wd, S, ptsx, ptsy, maxdx):
    out = [(0, 0, 0, 0, 0, 0, 0, 0)]
    out.pop()
    # tilted R2
    for x in range(Wd):
        for r in range(1, h + 1):
            for k in range(S.shape[0]):
                a, b, c, d = S[k, 0], S[k, 1], S[k, 2], S[k, 3]
                if r - b < 1 or r + d > h or x + a + c >= Wd:
                    continue
                Q0x, Q0y = x, r
                Q1x, Q1y = x + a, r - b
                Q2x, Q2y = x + c, r + d
                Q3x, Q3y = x + a + c, r - b + d
                # diag pq = Q0Q3, CD = Q1Q2
                if blk[Q1x, Q1y] and blk[Q2x, Q2y]:
                    mixed_from_diag(blk, h, Wd, Q0x, Q0y, Q3x, Q3y, Q1x, Q1y, Q2x, Q2y, out)
                if blk[Q0x, Q0y] and blk[Q3x, Q3y]:
                    mixed_from_diag(blk, h, Wd, Q1x, Q1y, Q2x, Q2y, Q0x, Q0y, Q3x, Q3y, out)
    # axis-aligned R2: C, D black opposite corners, different rows and columns
    n = ptsx.shape[0]
    for i in range(n):
        for j in range(n):
            cx, cy, dx, dy = ptsx[i], ptsy[i], ptsx[j], ptsy[j]
            if dx <= cx or dx - cx > maxdx or dy == cy:
                continue
            # p=(cx,dy), q=(dx,cy)
            mixed_from_diag(blk, h, Wd, cx, dy, dx, cy, cx, cy, dx, dy, out)
    return out

@njit(cache=True)
def rival_scan(h, ptsx, ptsy, maxdx):
    out = []
    n = ptsx.shape[0]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            cx, cy, dx, dy = ptsx[i], ptsy[i], ptsx[j], ptsy[j]
            if dy <= cy or dx == cx or abs(dx - cx) > maxdx:
                continue
            d = dy - cy
            if d % 2 == 0:
                continue
            t = dx - cx
            L2 = d * d + t * t
            L = int(np.sqrt(L2))
            while L * L < L2: L += 1
            while L * L > L2: L -= 1
            if L * L != L2:
                continue
            jj = (L - d) // 2
            if jj >= 1 and cy - jj >= 1 and dy + jj <= h:
                out.append((cx, cy, dx, dy, jj))
    return out
