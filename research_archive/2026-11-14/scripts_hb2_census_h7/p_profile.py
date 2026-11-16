"""Mean and max P incidence by diagonal band |T| = |j - i| (row gap ~ 28|T|).
usage: py p_profile.py h M lo bres"""
import sys, json
import numpy as np
from numba import njit
from h7common import d2xy, block
import p_h7

@njit(cache=True)
def decode(Q, r):
    I = np.empty(len(r), np.int64); J = np.empty(len(r), np.int64)
    for k in range(len(r)):
        I[k], J[k] = d2xy(Q, r[k])
    return I, J

h, M, lo, bres = map(int, sys.argv[1:5])
B, key, _ = p_h7.build(h, M, lo, bres)
verts, inv = np.unique(np.concatenate([key[:, 0], key[:, 1]]), return_inverse=True)
deg = np.bincount(inv)
I, J = decode(B["Q"], verts)
T = np.abs(J - I)
nA = B["iA1"] - B["iA0"] + 1; nK = B["jK1"] - B["jK0"] + 1
off = B["jK0"] - B["iA0"]
# labels per |T|: count pairs (i, j) in the bulk rectangle with |j - i| = t
tt = np.arange(0, max(nA, nK) + abs(off) + 2)
cnt = np.zeros(len(tt), np.int64)
ii = np.arange(B["iA0"], B["iA1"] + 1)
for s in (1, -1):
    # j = i + s t within [jK0, jK1]
    pass
# direct: for each i, j ranges over the bulk; |j-i| histogram via convolution of two interval indicators
a = np.zeros(B["iA1"] + 2, np.int64); a[B["iA0"]:B["iA1"] + 1] = 1
b = np.zeros(B["jK1"] + 2, np.int64); b[B["jK0"]:B["jK1"] + 1] = 1
# number of (i,j) with j - i = d : correlation
c = np.correlate(b, a, mode="full")   # index k -> d = k - (len(a) - 1)
dvals = np.arange(len(c)) - (len(a) - 1)
for dv, cv in zip(dvals, c):
    if cv:
        cnt[abs(dv)] += cv
edges = [0, 16, 64, 256, 1024, 4096, 8192, 16384, 32768, 10 ** 9]
rows = []
for lo_e, hi_e in zip(edges[:-1], edges[1:]):
    sel = (T >= lo_e) & (T < hi_e)
    nl = int(cnt[lo_e:min(hi_e, len(cnt))].sum())
    if nl == 0:
        continue
    rows.append({"T": [lo_e, hi_e], "labels": nl, "mean_deg": float(deg[sel].sum() / nl),
                 "max_deg": int(deg[sel].max()) if sel.any() else 0})
print(json.dumps({"h": h, "M": M, "bres": bres, "profile": rows}))
