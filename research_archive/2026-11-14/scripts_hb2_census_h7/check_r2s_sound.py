"""Soundness check of R2s witnesses: rebuild, then for every witness recompute the
four points from the ranks and the forbidden gap, and verify Lemma mixedeq, the
sea types, the strip and the Hilbert offset with exact integers.
usage: py check_r2s_sound.py h lo bres M"""
import sys
import numpy as np
from h7common import d2xy, block
import r2s_h7, r2s_par
h, lo, bres, M = map(int, sys.argv[1:5]); S = 6272
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
sv = (B["L"], B["F"], B["H"]); scode = ("L", "F", "H")
def typ(x):
    r = x % 7
    return "F" if r == 0 else ("H" if r in (1, 2, 4) else "L")
bad = 0; tot = 0
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    cand = r2s_par.run(h, lo_i, hi_i, rr, np.array(sv, np.int64), np.array([1, 0, 2], np.int64), S, 1, spf, 1)
    o0, o1 = (B["jK0"], B["jK1"]) if odd_role else (B["iA0"], B["iA1"])
    out = np.zeros((1 << 22, 4), np.int64)
    n = r2s_h7.partner_stage(B["Q"], M, S, odd_role, cand, o0, o1, B["iA0"], B["iA1"], B["jK0"], B["jK1"], out)
    for k in range(n):
        r1, r2, dlt, c = map(int, out[k]); si, i, Dl, X, u, v = map(int, cand[c])
        tot += 1
        x1 = S * (M * r1); x2 = S * (M * r2 + dlt)        # xi_earlier = 0, xi_later = dlt
        (i1, j1), (i2, j2) = d2xy(B["Q"], r1), d2xy(B["Q"], r2)
        # A is the label whose row index is i (odd role: i-coordinate; even: j)
        if X > 0:
            xe, xf, ce, cf = x1, x2, (i1, j1), (i2, j2)
        else:
            xe, xf, ce, cf = x2, x1, (i2, j2), (i1, j1)
        ye = 17 + 28 * ce[0] if odd_role else bres + 28 * ce[1]
        yf = 17 + 28 * cf[0] if odd_role else bres + 28 * cf[1]
        s = sv[si]
        A = (xe, ye); Bp = (xe + u, s); C = (xf, yf); D = (xf + v, s)
        ok = (C[0] - A[0] == X) and (ye == rr + 28 * i) and (yf - ye == 28 * Dl)
        BA = (Bp[0] - A[0], Bp[1] - A[1]); DC = (D[0] - C[0], D[1] - C[1])
        T2 = (C[0] + D[0] - A[0] - Bp[0], C[1] + D[1] - A[1] - Bp[1])
        ok &= BA[0] ** 2 + BA[1] ** 2 == DC[0] ** 2 + DC[1] ** 2
        ok &= BA[0] * T2[0] + BA[1] * T2[1] == 0
        ok &= T2[0] % 2 == 0 and T2[1] % 2 == 0 and DC != BA and DC != (-BA[0], -BA[1])
        p = (A[0] + T2[0] // 2, A[1] + T2[1] // 2); q = (Bp[0] + T2[0] // 2, Bp[1] + T2[1] // 2)
        ok &= 1 <= p[1] <= h and 1 <= q[1] <= h
        ok &= typ(Bp[0]) == scode[si] and typ(D[0]) == scode[si]
        ok &= Bp[0] % S != 0 and D[0] % S != 0
        ok &= (ce[0] - cf[0]) ** 2 < 16 * abs(r2 - r1) and (ce[1] - cf[1]) ** 2 < 16 * abs(r2 - r1)
        bad += not ok
print("h", h, "M", M, "bres", bres, "witnesses", tot, "failed", bad)
