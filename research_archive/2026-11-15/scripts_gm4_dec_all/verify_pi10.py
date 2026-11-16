"""Second-builder check of the archived Pi_10 certificates (certificates_pi10_M3.npz) and of the
corner cuts inside Pi_10 = W_9 + W_10 (2048 curve), all four types.
For each type: rebuild every cand triple of the window with common.py (independent code),
count certified violations (y_u - y_r = delta mod 3) of the archived assignment, and count
triples crossing the corner cell of W_9 and, for attach O4, of W_10.
Usage: py -B verify_pi10.py path/to/certificates_pi10_M3.npz"""
import sys, time
import numpy as np
from common import hilbert_array, legs, window_triples, certified_classes, core

z = np.load(sys.argv[1])
N = 1024
R = lambda m: (m * m - 1) // 3
P = legs(4 * N - 1)
t0 = time.time()
for g in ("id", "swap"):
    for attach in ("O4", "O2"):
        h = g if attach == "O4" else ("swap" if g == "id" else "id")
        xy = hilbert_array(2 * N).astype(np.int64)
        if h == "swap":
            xy = xy[:, ::-1].copy()
        J = 3 * N * N if attach == "O4" else N * N
        lo, hi = J - (N // 2) ** 2, J + N * N
        odd = 2 * xy[lo:hi, 0] + 1; even = 2 * xy[lo:hi, 1] + 2
        T = xy[lo:hi, 1] - xy[lo:hi, 0]
        E = window_triples(odd, even, 0, hi - lo, P)
        y = z[f"pi_{g}_{attach}_sol"].astype(np.int64)
        viol = int(((y[E[:, 1]] - y[E[:, 0]] - E[:, 2]) % 3 == 0).sum())
        cuts = [(N // 2) ** 2 * 0 + R(N // 2)]               # corner of W_9 (local rank in window)
        if attach == "O4":
            cuts.append((N // 2) ** 2 + R(N))                # corner of W_10
        res = []
        for p in cuts:
            cross = int(((E[:, 0] < p) & (E[:, 1] > p)).sum()) + int(((E[:, 0] == p) | (E[:, 1] == p)).sum())
            res.append(f"p={p} |T|={abs(int(T[p]))} crossing/incident {cross}")
        K = core(hi - lo, certified_classes(E))
        kl = np.unique(K[:, :2])
        seg = (kl >= cuts[0]) & (kl < (cuts[1] if len(cuts) > 1 else hi - lo))
        print(f"{g} {attach}: triples {len(E)}, certified violations {viol}; " + "; ".join(res)
              + f"; core labels {len(kl)} (inside [c*(W_9), next cut): {int(seg.sum())})  ({time.time()-t0:.1f}s)", flush=True)
