"""Reproduce the archived Pi_10 counts (p_cross_scale_chains.md, table in section 10):
triples and certified-core labels of W_9 + W_10 on the 2048 curve.
Usage: py -B repro_pi10.py g attach"""
import sys, time
import numpy as np
from common import hilbert_array, legs, window_triples, certified_classes, core, M

g, attach = sys.argv[1], sys.argv[2]
N = 1024
t0 = time.time()
h = g if attach == "O4" else ("swap" if g == "id" else "id")
xy = hilbert_array(2 * N)
if h == "swap":
    xy = xy[:, ::-1].copy()
odd = (2 * xy[:, 0] + 1).astype(np.int64); even = (2 * xy[:, 1] + 2).astype(np.int64)
J = 3 * N * N if attach == "O4" else N * N
lo, hi = J - (N // 2) ** 2, J + N * N
P = legs(4 * N - 1)
print(f"legs: {len(P)} gaps  ({time.time()-t0:.1f}s)", flush=True)
E = window_triples(odd, even, lo, hi, P)
print(f"triples {len(E)}  ({time.time()-t0:.1f}s)", flush=True)
C = certified_classes(E)
K = core(4 * N * N, C)
print(f"certified core labels {len(np.unique(K[:, :2]))}, classes {len(K)}  ({time.time()-t0:.1f}s)")
