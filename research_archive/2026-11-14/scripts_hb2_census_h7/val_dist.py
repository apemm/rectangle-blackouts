"""Distribution of v2(Delta), v7(Delta) and |X| among R2s row-stage solutions.
usage: py val_dist.py h lo bres Smod hil"""
import sys
from collections import Counter
import numpy as np
from h7common import block
import r2s_h7
h, lo, bres, Smod, hil = map(int, sys.argv[1:6])
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
Fr = B["F"] if B["F"] < h else 55
sv = np.array((B["L"], Fr, B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
v2 = lambda x: (abs(x) & -abs(x)).bit_length() - 1
def v7(x):
    k = 0
    while x % 7 == 0: x //= 7; k += 1
    return k
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    o = np.zeros((1 << 21, 6), np.int64)
    n = r2s_h7.row_stage(h, lo_i, hi_i, rr, sv, sc, Smod, 0, spf, r2s_h7.QR7, o, hil)
    o = o[:n]
    for si, nm in enumerate("LFH"):
        sel = o[o[:, 0] == si]
        if len(sel) == 0: continue
        c2 = Counter(v2(int(d)) for d in sel[:, 2]); c7 = Counter(v7(int(d)) for d in sel[:, 2])
        rq = sel[:, 3] // Smod
        print("role", "O" if odd_role else "E", nm, "n", len(sel), "v2(Delta)", dict(sorted(c2.items())),
              "v7(Delta)", dict(sorted(c7.items())), "median |X|/Smod", int(np.median(np.abs(rq))),
              "max |Delta|", int(np.abs(sel[:, 2]).max()))
