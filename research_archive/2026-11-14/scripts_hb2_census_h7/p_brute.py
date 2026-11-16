"""Brute-force check of p_h7.py: every pair (e, e+d), d <= dmax, every choice
gap, both cross-parity roles, exact isqrt test.  usage: py p_brute.py h M lo"""
import sys, math
import numpy as np
from numba import njit
from h7common import S, d2xy, xy2d, block
import p_h7


@njit(cache=True)
def isq(n):
    r = int(math.sqrt(n))
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r


@njit(cache=True)
def brute(Q, h, M, ares, bres, iA0, iA1, jK0, jK1, Smul, out):
    n = 0
    dmax = ((h - 1) // Smul + M - 1) // M + 1
    for i in range(iA0, iA1 + 1):
        for j in range(jK0, jK1 + 1):
            r = xy2d(Q, i, j)
            for d in range(1, dmax + 1):
                s = r + d
                if s >= Q * Q:
                    continue
                fi, fj = d2xy(Q, s)
                if fi < iA0 or fi > iA1 or fj < jK0 or fj > jK1:
                    continue
                for delta in range(1 - M, M):
                    qq = M * d + delta
                    if qq <= 0:
                        continue
                    X = Smul * qq
                    if X >= h:
                        continue
                    hit = False
                    for role in range(2):
                        if role == 0:
                            y1 = ares + 28 * i; y2 = bres + 28 * fj
                        else:
                            y1 = bres + 28 * j; y2 = ares + 28 * fi
                        Y = y2 - y1
                        L2 = X * X + Y * Y
                        L = isq(L2)
                        if L * L == L2 and L <= h - 1 and y1 + y2 - L >= 2 and y1 + y2 + L <= 2 * h:
                            hit = True
                    if hit:
                        out[n, 0] = r; out[n, 1] = s; out[n, 2] = delta
                        n += 1
    return n


if __name__ == "__main__":
    h, M, lo = map(int, sys.argv[1:4])
    bres = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    Sm = int(sys.argv[5]) if len(sys.argv) > 5 else S
    B = block(h, lo, bres=bres)
    out = np.zeros((1 << 20, 3), np.int64)
    n = brute(B["Q"], h, M, 17, bres, B["iA0"], B["iA1"], B["jK0"], B["jK1"], Sm, out)
    bk = np.unique(out[:n], axis=0)
    _, key, _ = p_h7.build(h, M, lo, bres, Sm)
    same = len(bk) == len(key) and (len(bk) == 0 or (bk == key).all())
    print("h", h, "M", M, "lo", lo, "bres", bres, "S", Sm, "brute", len(bk), "band", len(key), "identical", same)
