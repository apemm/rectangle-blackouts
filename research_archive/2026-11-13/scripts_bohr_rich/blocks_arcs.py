# For rich diagonals: (1) arc number M_T of D_T (grid search theta=a/Q), (2) block bound 4*ceil(n/B*) where
# B* = largest B (binary search) such that E_B = D_T cap [1,B) has a 4-arc theta (||theta d|| >= 1/4).
import sys, time, numpy as np
from math import log, ceil
from common import all_D, nT
t0 = time.time()
h = int(sys.argv[1]); top = int(sys.argv[2])
D = all_D(h)
Ts = [T for T in sorted(D, key=lambda T: -len(D[T])) if T > 0][:top]

def has_arc(ds, M):
    if len(ds) == 0: return True
    Q = int(64 * max(ds)) | 1
    a = np.arange(Q, dtype=np.int64)
    ok = np.ones(Q, dtype=bool)
    lo = Q / M; hi = Q - Q / M
    for d in ds:
        r = (a * d) % Q
        ok &= (r >= lo) & (r <= hi)
        if not ok.any(): return False
    return True

for T in Ts:
    d = D[T]; k = len(d); n = nT(h, T)
    M = 2
    while not has_arc(d, M): M += 1
    lo, hi = 0, k  # number of smallest distances kept
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if has_arc(d[:mid], 4): lo = mid
        else: hi = mid - 1
    B = d[lo] if lo < k else n   # E_B = d[:lo] has a 4-arc, B = next distance
    print("T %6d n %6d k %3d  M_T %2d  kept %3d  B* %6d  4ceil(n/B*) %3d  k/ln h %.1f  k/ln k %.1f  t=%.0fs" %
          (T, n, k, M, lo, B, 4 * ceil(n / B), k / log(h), k / log(k), time.time() - t0))
