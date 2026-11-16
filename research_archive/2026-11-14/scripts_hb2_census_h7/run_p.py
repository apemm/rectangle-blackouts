"""Build the P system of one block and analyze it in one run (< 60 s).
usage: py run_p.py h M lo bres"""
import sys, time, json
import numpy as np
import p_h7, analyze_h7
h, M, lo, bres = map(int, sys.argv[1:5])
t = time.time()
B, key, ntrip = p_h7.build(h, M, lo, bres)
if len(key) < 300000:
    np.savez_compressed(f"out/p_h{h}_M{M}_lo{lo}_b{bres}.npz", cons=key, meta=np.array([h, M, lo, B["Q"], B["labels"], bres]))
r = analyze_h7.analyze(M, B["labels"], key)
hist = r.pop("inc_hist", None)
r.update({"h": h, "lo": lo, "bres": bres, "Q": B["Q"], "triples": ntrip, "sec": round(time.time() - t, 1)})
print(json.dumps(r)); print("hist", hist)
