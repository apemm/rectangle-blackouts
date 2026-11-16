"""Check Lemma 7P on the unpruned fast enumerator: when 7 does not divide m = s - y,
every R2s solution with 49 | X has 7 | Delta.  usage: py check_prune7.py h lo bres Smod hil"""
import sys
import numpy as np
from h7common import block
import r2s_h7
h, lo, bres, Smod, hil = map(int, sys.argv[1:6])
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
Fr = B["F"] if B["F"] < h else 55
sv = np.array((B["L"], Fr, B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    o = np.zeros((1 << 21, 6), np.int64)
    n = r2s_h7.row_stage(h, lo_i, hi_i, rr, sv, sc, Smod, 0, spf, r2s_h7.QR7, o, hil)
    o = o[:n]
    m = sv[o[:, 0]] - (rr + 28 * o[:, 1])
    bad = ((m % 7 != 0) & (o[:, 2] % 7 != 0)).sum()
    print("h", h, "Smod", Smod, "hil", hil, "role", "O" if odd_role else "E", "solutions", n,
          "with 7|m", int((m % 7 == 0).sum()), "violating 7|Delta", int(bad))
