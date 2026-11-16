"""Exact R2s incidence of the labels on sampled rows (as the A label), at large h.
For each sampled bulk row (odd and even, uniform without replacement) the row
stage is complete for that row; the partner stage then scans every label on the
row.  Mean A-count per label is an unbiased estimate of half the mean R2s
incidence.  Also reports the A-count by sea role and by |m| bucket.
usage: py r2s_sample.py h lo bres nrows seed M"""
import sys, time, json
import numpy as np
from h7common import block
import r2s_h7, r2s_par

h, lo, bres, nrows, seed, M = map(int, sys.argv[1:7])
t0 = time.time()
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
sv = np.array((B["L"], B["F"], B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
rng = np.random.default_rng(seed)
res = {"h": h, "lo": lo, "bres": bres, "M": M, "nrows_each_parity": nrows}
per_label_max = 0
tot_w = 0; tot_lab = 0; rate = 0.0
by_role = {}
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    rows = np.sort(rng.choice(np.arange(lo_i, hi_i + 1), size=min(nrows, hi_i - lo_i + 1), replace=False))
    cnt, out = r2s_par.row_stage_list(h, lo_i, hi_i, rows.astype(np.int64), rr, sv, sc, 6272, 1, spf, r2s_h7.QR7, 1)
    assert cnt.max(initial=0) <= r2s_par.CAP
    cl = [out[j, :cnt[j]] for j in np.nonzero(cnt)[0]]
    cand = np.concatenate(cl) if cl else np.zeros((0, 6), np.int64)
    o0, o1 = (B["jK0"], B["jK1"]) if odd_role else (B["iA0"], B["iA1"])
    w = np.zeros((1 << 22, 4), np.int64)
    n = r2s_h7.partner_stage(B["Q"], M, 6272, odd_role, cand, o0, o1, B["iA0"], B["iA1"], B["jK0"], B["jK1"], w)
    w = w[:n]
    nl = len(rows) * (o1 - o0 + 1)
    tot_w += n; tot_lab += nl; rate += n / nl
    # A-label of each witness: the endpoint on the candidate's row
    if n:
        ci = w[:, 3]
        # per-label A-count: identify A as the endpoint whose rank equals xy2d of the row label;
        # count witnesses per (candidate row, partner-independent) A rank
        A_rank = np.where(cand[ci, 3] > 0, w[:, 0], w[:, 1])
        _, c = np.unique(A_rank, return_counts=True)
        per_label_max = max(per_label_max, int(c.max()))
        for si, nm in enumerate("LFH"):
            by_role[("O" if odd_role else "E") + nm] = int((cand[ci, 0] == si).sum())
    res[("O" if odd_role else "E") + "_row_candidates"] = int(len(cand))
res["witnesses"] = int(tot_w); res["labels_scanned"] = int(tot_lab)
res["est_mean_incidence"] = 2 * rate
res["max_A_count_on_label"] = per_label_max
res["witnesses_by_role"] = by_role
res["sec"] = round(time.time() - t0, 1)
print(json.dumps(res))
