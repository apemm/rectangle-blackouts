"""Check the archived B = 1024, M = 3 certificates against my own constraint builder.

Usage: py -I check_certs.py path/to/certificates_B1024_M3.npz
For every array in the file whose name says id or swap, rebuild cand (and gen) G_1024^o
and count violated constraints xi_s - xi_r == delta, and mod-3 violations.
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from excursions import hilbert, vectors, scan

B = 1024; M = 3


def build(orient, gen):
    xs, ys = hilbert(B)
    if orient == 'swap':
        xs, ys = ys, xs
    ii = xs.astype(np.int64); jj = ys.astype(np.int64)
    N = B * B
    buf = np.zeros(N, dtype=np.int64)
    R = []; K = []
    for (q, Y, L) in vectors(2 * B - 1):
        for d in sorted({q // M, -(-q // M)}):
            if d < 1 or abs(q - M * d) > M - 1:
                continue
            c = scan(ii, jj, d, Y, L, B, gen, buf)
            if c:
                R.append(buf[:c].copy()); K.append(np.full(c, d * 16 + (q - M * d) + 8))
    key = np.unique(np.concatenate(R) * (1 << 24) + np.concatenate(K))
    r = key >> 24; d = (key & ((1 << 24) - 1)) >> 4; dl = (key & 15) - 8
    return r, r + d, dl


def main():
    z = np.load(sys.argv[1])
    print("arrays:", {k: (z[k].shape, str(z[k].dtype)) for k in z.files})
    cache = {}
    for k in z.files:
        orient = 'swap' if 'swap' in k else 'id'
        xi = z[k].astype(np.int64)
        assert xi.shape == (B * B,) and xi.min() >= 0 and xi.max() <= M - 1
        for gen in (0, 1):
            if (orient, gen) not in cache:
                cache[(orient, gen)] = build(orient, gen)
            r, s, dl = cache[(orient, gen)]
            diff = xi[s] - xi[r]
            bad = int(np.count_nonzero(diff == dl))
            badmod = int(np.count_nonzero((diff - dl) % M == 0))
            print(f"{k}: vs {'gen' if gen else 'cand'} {orient} ({len(r)} constraints): violations {bad}, mod-3 violations {badmod}")
            if len(cache) > 2:
                cache.pop(next(iter(cache)))


if __name__ == '__main__':
    main()
