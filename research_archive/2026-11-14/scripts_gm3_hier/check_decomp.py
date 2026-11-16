"""Sanity check of the decomposition theorem on one fixed block system.
Usage: py -B check_decomp.py B orient version M
Checks, for every distinct constraint (r, u, delta):
  (SS) T_r and T_u are nonzero and of the same sign (T = y - x);
  (CUT) no main-diagonal cell has rank in (r, u]  (equivalently seg[r] == seg[u]).
Then reports the weighted M-core (integer and certified) split by segment.
"""
import sys, time
import numpy as np
from blk import build, segments, weighted_core

B, orient, version, M = int(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4])
S = 32
t0 = time.time()
xy, E = build(B, S, M, orient, version)
n = B * B
T = xy[:, 1] - xy[:, 0]
seg = segments(xy)
print(f"B={B} {orient} {version} M={M}: distinct triples {len(E)}  ({time.time()-t0:.1f}s)")
Tr, Tu = T[E[:, 0]], T[E[:, 1]]
print("  SS violations (opposite sign or zero):", int(((Tr * Tu) <= 0).sum()),
      "  min |T| at an endpoint:", int(min(np.abs(Tr).min(), np.abs(Tu).min())))
print("  CUT violations (seg differs):", int((seg[E[:, 0]] != seg[E[:, 1]]).sum()))
# rank-distance bound d <= U(U+1)/48 + 2/3 style check: d vs min |T|^2
d = E[:, 1] - E[:, 0]
tmin = np.minimum(np.abs(Tr), np.abs(Tu))
print("  max d / (tmin+4.5)^2:", float((d / (tmin + 4.5) ** 2).max()))
for mode in ("int", "mod"):
    C = weighted_core(n, E, M, mod=(M if mode == "mod" else None))
    labs = np.unique(C[:, :2]) if len(C) else np.array([], dtype=np.int64)
    segs, cnt = np.unique(seg[labs], return_counts=True) if len(labs) else ([], [])
    print(f"  {mode} {M}-core: labels {len(labs)}, triples {len(C)}, segments touched {len(segs)}")
    for s_, c_ in zip(segs, cnt):
        rk = np.flatnonzero(seg == s_)
        lo, hi = rk[0], rk[-1] + 1
        tl = T[labs[seg[labs] == s_]]
        print(f"    segment {s_}: ranks [{lo},{hi}) size {hi-lo}, core labels {c_}, T in [{tl.min()},{tl.max()}]")
print(f"  done ({time.time()-t0:.1f}s)")
