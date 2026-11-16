"""Row-stage solution counts by (parity, sea) for several strides. usage: py combo_counts.py h lo bres hil S1 S2 ..."""
import sys
import numpy as np
from h7common import block
import r2s_h7, r2s_par
h, lo, bres, hil = map(int, sys.argv[1:5]); Ss = list(map(int, sys.argv[5:]))
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
Fr = B["F"] if B["F"] < h else 55
sv = np.array((B["L"], Fr, B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
for Sm in Ss:
    pr = 1 if Sm % 49 == 0 else 0
    row = {}
    for odd_role in (1, 0):
        lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
        a = r2s_par.run(h, lo_i, hi_i, rr, sv, sc, Sm, pr, spf, hil)
        for si, nm in enumerate("LFH"):
            row[("O" if odd_role else "E") + nm] = int((a[:, 0] == si).sum())
    print("h", h, "lo", lo, "bres", bres, "hil", hil, "Smod", Sm, row)
