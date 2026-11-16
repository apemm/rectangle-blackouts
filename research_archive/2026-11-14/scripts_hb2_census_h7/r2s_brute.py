"""Independent check of the R2s row stage: for each (parity, s, row y, Delta)
loop over every u with |u| <= (|N|+1)/2, take v = +-isqrt(u^2 + N) when it is
a square, solve u(2X + v - u) = -m delta for X, and apply the same filters
(X = 0 mod Smod, Hilbert precondition, sea types, n integral, strip).
Then compare with r2s_h7.row_stage (prune7 = 0 and 1).
usage: py r2s_brute.py h lo bres Smod"""
import sys, math
import numpy as np
from numba import njit
from h7common import block
import r2s_h7


@njit(cache=True)
def isq(n):
    r = int(math.sqrt(n))
    while r * r > n:
        r -= 1
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r


@njit(cache=True)
def brute(h, lo_idx, hi_idx, res, svals, scodes, Smod, typ7, out, hil):
    n = 0
    for si in range(3):
        s = svals[si]; sc = scodes[si]
        for i in range(lo_idx, hi_idx + 1):
            y = res + 28 * i; m = s - y
            for Dl in range(lo_idx - i, hi_idx - i + 1):
                if Dl == 0:
                    continue
                dl = 28 * Dl
                if y + dl // 2 < 1 or y + dl // 2 > h or s + dl // 2 < 1 or s + dl // 2 > h:
                    continue
                N = dl * (2 * m - dl)
                if N == 0:
                    continue
                U = (abs(N) + 1) // 2
                for u in range(-U, U + 1):
                    if u == 0:
                        continue
                    w = u * u + N
                    if w < 0:
                        continue
                    r = isq(w)
                    if r * r != w:
                        continue
                    for sv in (1, -1):
                        if r == 0 and sv == -1:
                            continue
                        v = sv * r
                        # u (2X + v - u) = -m dl
                        num = -m * dl
                        if num % u != 0:
                            continue
                        tt = num // u          # = 2X + v - u
                        if (tt - v + u) % 2 != 0:
                            continue
                        X = (tt - v + u) // 2
                        if tt % 2 != 0:        # n_x = tt/2 integral
                            continue
                        if X == 0 or X % Smod != 0 or abs(X) // Smod < (1 + (Dl * Dl) // 16 if hil else 1):
                            continue
                        if typ7[u % 7] != sc or typ7[(X + v) % 7] != sc:
                            continue
                        # direct checks of the defining equations
                        if u * u + m * m != v * v + (m - dl) * (m - dl):
                            continue
                        if u * (2 * X + v - u) + m * dl != 0:
                            continue
                        out[n, 0] = si; out[n, 1] = i; out[n, 2] = Dl
                        out[n, 3] = X; out[n, 4] = u; out[n, 5] = v
                        n += 1
    return n


if __name__ == "__main__":
    h, lo, bres, Smod = map(int, sys.argv[1:5])
    hil = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    B = block(h, lo, bres=bres)
    spf = r2s_h7.spf_sieve(4 * h + 10)
    Fr = B["F"] if B["F"] < h else 55
    sv = np.array((B["L"], Fr, B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
    for odd_role in (1, 0):
        lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
        o = np.zeros((1 << 20, 6), np.int64)
        nb = brute(h, lo_i, hi_i, rr, sv, sc, Smod, r2s_h7.QR7, o, hil)
        bset = set(map(tuple, o[:nb].tolist()))
        res = []
        for pr in (0, 1):
            o2 = np.zeros((1 << 20, 6), np.int64)
            n2 = r2s_h7.row_stage(h, lo_i, hi_i, rr, sv, sc, Smod, pr, spf, r2s_h7.QR7, o2, hil)
            res.append(set(map(tuple, o2[:n2].tolist())))
        print("h", h, "lo", lo, "bres", bres, "Smod", Smod, "hil", hil, "role", "O" if odd_role else "E",
              "brute", len(bset), "fast", len(res[0]), "equal", bset == res[0],
              "pruned", len(res[1]), "pruned_equal", bset == res[1])
