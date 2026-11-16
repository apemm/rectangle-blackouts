# Brute-force obstruction finder from the definitions (criterion V1-V5).
# Board: columns 0..W-1, rows 1..h, black set given as list of (x,y).
# Tilted corner triples (V1 / fatal / parked), V3 collisions, mixed quadruples
# (side AB not vertical), rival pairs.  numba for speed.
import numpy as np
from numba import njit
from math import gcd

@njit(cache=True)
def _gcd(a, b):
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

@njit(cache=True)
def triples_nb(X, Y, grid, colpar, h, W, reach, out):
    # out: rows of (Vx,Vy,P1x,P1y,P2x,P2y,Wx,Wy,kind) kind 0=V1,1=fatal,2=parked
    n = X.shape[0]; m = 0
    for a in range(n):
        vx = X[a]; vy = Y[a]
        for b in range(n):
            if b == a: continue
            dx = X[b] - vx; dy = Y[b] - vy
            if dx == 0 or dy == 0 or abs(dx) > reach: continue
            g = _gcd(dx, dy)
            wx = -dy // g; wy = dx // g
            for k in range(-h, h + 1):
                if k == 0: continue
                p2x = vx + k * wx; p2y = vy + k * wy
                if p2y < 1 or p2y > h or p2x < 0 or p2x >= W: continue
                if grid[p2x, p2y] == 0: continue
                # canonical: P1 index < P2 index (lexicographic on (x,y))
                if (X[b], Y[b]) > (p2x, p2y): continue
                qx = X[b] + p2x - vx; qy = Y[b] + p2y - vy
                if qy < 1 or qy > h or qx < 0 or qx >= W: continue
                if grid[qx, qy] == 1:
                    kind = 0
                else:
                    # parked iff all black points in column qx have parity of qy
                    cp = colpar[qx]  # bit0: has odd black, bit1: has even black
                    if qy % 2 == 1:
                        kind = 1 if (cp & 2) else 2
                    else:
                        kind = 1 if (cp & 1) else 2
                if m < out.shape[0]:
                    out[m, 0] = vx; out[m, 1] = vy; out[m, 2] = X[b]; out[m, 3] = Y[b]
                    out[m, 4] = p2x; out[m, 5] = p2y; out[m, 6] = qx; out[m, 7] = qy; out[m, 8] = kind
                m += 1
    return m

@njit(cache=True)
def pairs_nb(X, Y, reach):
    n = X.shape[0]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(X[j] - X[i]) <= reach: cnt += 1
    keys = np.empty(cnt, np.int64); I = np.empty(cnt, np.int32); J = np.empty(cnt, np.int32)
    c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(X[j] - X[i]) <= reach:
                dx = X[j] - X[i]; dy = Y[j] - Y[i]
                L = dx * dx + dy * dy
                keys[c] = (np.int64(L) * 65536 + (X[i] + X[j])) * 1024 + (Y[i] + Y[j])
                I[c] = i; J[c] = j; c += 1
    return keys, I, J

@njit(cache=True)
def mixed_nb(X, Y, keys, I, J, h, out):
    # keys sorted with I,J permuted accordingly
    m = 0
    npairs = keys.shape[0]
    for t in range(npairs):
        a = I[t]; b = J[t]
        ux = X[b] - X[a]; uy = Y[b] - Y[a]
        if ux == 0: continue
        g = _gcd(ux, uy)
        wx = -uy // g; wy = ux // g
        L = ux * ux + uy * uy
        for k in range(-2 * h, 2 * h + 1):
            if k == 0: continue
            nx = k * wx; ny = k * wy
            py = Y[a] + ny; qy = Y[b] + ny
            if py < 1 or py > h or qy < 1 or qy > h: continue
            px = X[a] + nx; qx = X[b] + nx
            sx = X[a] + X[b] + 2 * nx; sy = Y[a] + Y[b] + 2 * ny
            if sx < 0 or sy < 0 or sy >= 1024 or sx >= 65536: continue
            key = (np.int64(L) * 65536 + sx) * 1024 + sy
            lo = np.searchsorted(keys, key)
            while lo < npairs and keys[lo] == key:
                c = I[lo]; d = J[lo]; lo += 1
                if c == a or c == b or d == a or d == b: continue
                vx = X[d] - X[c]; vy = Y[d] - Y[c]
                if (vx == ux and vy == uy) or (vx == -ux and vy == -uy): continue
                if (X[c] == px and Y[c] == py) or (X[c] == qx and Y[c] == qy): continue
                if (X[d] == px and Y[d] == py) or (X[d] == qx and Y[d] == qy): continue
                if m < out.shape[0]:
                    out[m, 0] = a; out[m, 1] = b; out[m, 2] = c; out[m, 3] = d
                    out[m, 4] = px; out[m, 5] = py; out[m, 6] = qx; out[m, 7] = qy
                m += 1
    return m

@njit(cache=True)
def rivals_nb(X, Y, h, out):
    n = X.shape[0]; m = 0
    for a in range(n):
        for b in range(a + 1, n):
            ya = Y[a]; yb = Y[b]
            if (yb - ya) % 2 == 0: continue
            t = X[a] - X[b]
            if t == 0 or t % 2 != 0: continue
            if abs(t) > 2 * h * h: continue
            c = min(ya, yb); cp = max(ya, yb); d = cp - c
            for j in range(1, h):
                if c - j < 1 or cp + j > h: break
                if 4 * j * (d + j) == t * t:
                    if m < out.shape[0]:
                        out[m, 0] = a; out[m, 1] = b; out[m, 2] = j
                    m += 1
    return m

def analyse(S, h, W, reach=None):
    if reach is None: reach = h * h // 4 + 2
    pts = sorted(S)
    X = np.array([p[0] for p in pts], np.int64); Y = np.array([p[1] for p in pts], np.int64)
    grid = np.zeros((W, h + 2), np.int8)
    colpar = np.zeros(W, np.int8)
    for (x, y) in pts:
        grid[x, y] = 1
        colpar[x] |= (1 if y % 2 else 2)
    out = np.zeros((200000, 9), np.int64)
    m = triples_nb(X, Y, grid, colpar, h, W, reach, out)
    assert m <= out.shape[0], m
    tr = out[:m].copy()
    keys, I, J = pairs_nb(X, Y, reach)
    o = np.argsort(keys, kind='stable'); keys = keys[o]; I = I[o]; J = J[o]
    outm = np.zeros((200000, 8), np.int64)
    mm = mixed_nb(X, Y, keys, I, J, h, outm)
    assert mm <= outm.shape[0], mm
    mx = outm[:mm].copy()
    outr = np.zeros((100000, 3), np.int64)
    mr = rivals_nb(X, Y, h, outr)
    rv = outr[:mr].copy()
    return pts, tr, mx, rv
