"""Build the R2s system (parallel row stage + partner stage) of one block for
M = 1, 2, 3, analyze R2s alone and P u R2s.  usage: py run_r2s.py h lo bres [withP=1]"""
import sys, time, json
import numpy as np
from h7common import block
import r2s_h7, r2s_par, p_h7, analyze_h7
h, lo, bres = map(int, sys.argv[1:4]); withP = int(sys.argv[4]) if len(sys.argv) > 4 else 1
t0 = time.time()
B = block(h, lo, bres=bres)
spf = r2s_h7.spf_sieve(4 * h + 10)
sv = np.array((B["L"], B["F"], B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
cands = {}
for odd_role in (1, 0):
    lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
    cands[odd_role] = r2s_par.run(h, lo_i, hi_i, rr, sv, sc, 6272, 1, spf, 1)
t1 = time.time()
summ = {"h": h, "lo": lo, "bres": bres, "labels": B["labels"], "Q": B["Q"],
        "row_cands_O": len(cands[1]), "row_cands_E": len(cands[0]), "row_stage_sec": round(t1 - t0, 1)}
by = {}
for odd_role in (1, 0):
    for si, nm in enumerate("LFH"):
        by[("O" if odd_role else "E") + nm] = int((cands[odd_role][:, 0] == si).sum())
summ["row_cands_by_role"] = by
np.savez_compressed(f"out/r2s_cands_h{h}_lo{lo}_b{bres}.npz", O=cands[1], E=cands[0])
print(json.dumps(summ))
for M in (1, 2, 3):
    lst = []
    for odd_role in (1, 0):
        o0, o1 = (B["jK0"], B["jK1"]) if odd_role else (B["iA0"], B["iA1"])
        out = np.zeros((1 << 23, 4), np.int64)
        n = r2s_h7.partner_stage(B["Q"], M, 6272, odd_role, cands[odd_role], o0, o1,
                                 B["iA0"], B["iA1"], B["jK0"], B["jK1"], out)
        assert n <= out.shape[0]
        lst.append(out[:n, :3])
    w = np.concatenate(lst)
    cons = np.unique(w, axis=0) if len(w) else np.zeros((0, 3), np.int64)
    # witnesses per label (R2s alone)
    r = analyze_h7.analyze(M, B["labels"], cons); hist = r.pop("inc_hist", None)
    keep = ["constraints", "incident", "mean_inc", "max_inc", "degeneracy", "core_sizes", "greedy_stuck", "M_suffices", "method"]
    line = {"M": M, "R2s": {k: r.get(k) for k in keep}, "R2s_witnesses": int(len(w))}
    if withP:
        _, pk, _ = p_h7.build(h, M, lo, bres)
        u = np.unique(np.concatenate([pk, cons]), axis=0) if len(cons) else pk
        r2 = analyze_h7.analyze(M, B["labels"], u); r2.pop("inc_hist", None)
        line["P"] = len(pk)
        line["PuR2s"] = {k: r2.get(k) for k in keep + ["Mcore_vertices", "Mcore_largest", "exact_Mcore"]}
    print(json.dumps(line))
print("total sec", round(time.time() - t0, 1))
