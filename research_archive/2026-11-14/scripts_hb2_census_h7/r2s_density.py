"""Row-stage-only R2s candidate density per sampled row, with the |Delta|, |u| and
|X|/S of each candidate.  usage: py r2s_density.py h lo bres nrows seed"""
import sys, time, json
import numpy as np
from h7common import block
import r2s_h7, r2s_par
h, lo, bres, nrows, seed = map(int, sys.argv[1:6])
t0 = time.time()
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
sv = np.array((B["L"], B["F"], B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
rng = np.random.default_rng(seed)
out = {"h": h, "lo": lo, "bres": bres}
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    rows = np.sort(rng.choice(np.arange(lo_i, hi_i + 1), size=min(nrows, hi_i - lo_i + 1), replace=False))
    cnt, o = r2s_par.row_stage_list(h, lo_i, hi_i, rows.astype(np.int64), rr, sv, sc, 6272, 1, spf, r2s_h7.QR7, 1)
    cl = [o[j, :cnt[j]] for j in np.nonzero(cnt)[0]]
    cand = np.concatenate(cl) if cl else np.zeros((0, 6), np.int64)
    nm = "O" if odd_role else "E"
    out[nm + "_rows"] = int(len(rows)); out[nm + "_cands"] = int(len(cand))
    out[nm + "_per_row"] = len(cand) / len(rows)
    out[nm + "_list(sea,|Delta|,|u|,|X|/S)"] = [("LFH"[int(c[0])], int(abs(c[2])), int(abs(c[4])), int(abs(c[3]) // 6272)) for c in cand[::2]][:12]
out["sec"] = round(time.time() - t0, 1)
print(json.dumps(out))
