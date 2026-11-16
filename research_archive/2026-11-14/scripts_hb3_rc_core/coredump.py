"""Dump the weighted k-core of the P candidate multigraph with witnesses."""
import sys, math
import numpy as np
import randcurve as R
from bandcore import core_numbers

def build_w(xy, h, S, M):
    A, K = (h + 1) // 2, h // 2
    n = len(xy)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    rows = []
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            ysd = R.pyth(X, h)
            if not ysd:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ysd.items():
                hyp[y] = L
            for role, (r1, r2) in enumerate(((odd[:-d], even[d:]), (even[:-d], odd[d:]))):
                L = hyp[np.abs(r2 - r1)]
                sm = r1 + r2
                hit = (L > 0) & (sm - L >= 2) & (sm + L <= 2 * h) & active[:-d] & active[d:]
                for i in np.nonzero(hit)[0]:
                    Y = abs(int(r2[i] - r1[i])); Lv = int(L[i])
                    rows.append((int(i), int(i + d), d, delta, role, Y, Lv, (Lv - Y) // 2))
    return rows

if __name__ == "__main__":
    mode, h, S, M, k = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    seed = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    q = 1 << (max((h + 1) // 2, h // 2) - 1).bit_length()
    xy = R.hilbert_array(q) if mode == "hil" else R.random_curve(q, seed)
    rows = build_w(xy, h, S, M)
    # dedupe identical (r,s,delta) triples as the archive does
    seen = {}
    for row in rows:
        seen.setdefault((row[0], row[1], row[3]), row)
    rows = list(seen.values())
    r = np.array([x[0] for x in rows]); s = np.array([x[1] for x in rows])
    deg, cn = core_numbers(r, s, q * q)
    core = set(np.nonzero(cn >= k)[0].tolist())
    print(f"{mode} seed={seed} h={h} S={S} M={M}: {len(rows)} constraints, {k}-core size {len(core)}")
    for v in sorted(core):
        i, j = xy[v]
        print(f"  rank {v} cell (i={i}, j={j}) T={j-i}")
    for row in rows:
        if row[0] in core and row[1] in core:
            print("  edge r={} s={} d={} delta={} role={} Y={} L={} a={}".format(*row))
