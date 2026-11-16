"""Weighted M-core of one excursion system P_B^o (S = 32, candidate version, no owner test).

Usage: py -I one_excursion.py Bside orient M [M ...]
The excursion of scale Bside/2 inside a main-diagonal block of side Bside and orientation
orient is the rank interval from the diagonal cell (Bside/2 - 1, Bside/2 - 1) up to the start
of the third child. By the excursion theorem it is closed, so only pairs inside it are scanned.
"""
import sys, time
import os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from excursions import hilbert, vectors, scan, weighted_core


def main():
    Bs = int(sys.argv[1]); orient = sys.argv[2]; Ms = [int(a) for a in sys.argv[3:]]
    t0 = time.time()
    xs, ys = hilbert(Bs)
    if orient == 'swap':
        xs, ys = ys, xs
    half = Bs // 2
    diag = np.nonzero(xs == ys)[0]
    lo = int(diag[(xs[diag] == half - 1)][0]); hi = 2 * half * half
    assert hi - lo == (4 * half * half + 2) // 3
    ii = xs[lo:hi].astype(np.int64); jj = ys[lo:hi].astype(np.int64)
    assert np.count_nonzero(ii == jj) == 1
    N = hi - lo
    vecs = vectors(2 * Bs - 1)
    buf = np.zeros(N, dtype=np.int64)
    for M in Ms:
        R = []; D = []
        for (q, Y, L) in vecs:
            for d in sorted({q // M, -(-q // M)}):
                if d < 1 or d >= N or abs(q - M * d) > M - 1:
                    continue
                c = scan(ii, jj, d, Y, L, Bs, 0, buf)
                if c:
                    R.append(buf[:c].copy()); D.append(np.full(c, d * 16 + (q - M * d) + 8))
        r = np.concatenate(R); dk = np.concatenate(D)
        key = r * (1 << 24) + dk
        key = np.unique(key)
        r = key >> 24; d = (key & ((1 << 24) - 1)) >> 4
        s = r + d
        alive = weighted_core(N, r, s, M)
        nc = int(alive.sum())
        msg = f"side {Bs} {orient} excursion scale {half}: labels {N}, M={M}: constraints {len(r)}, weighted core {nc}"
        if nc:
            T = (jj - ii)[alive]
            a = ii[alive]; b = jj[alive]
            lev = {}
            for v in range(nc):
                kk = 1
                while (a[v] // kk) != (b[v] // kk):
                    kk *= 2
                lev[kk // 2] = lev.get(kk // 2, 0) + 1
            msg += f", T in [{T.min()},{T.max()}], by off-diagonal block side {dict(sorted(lev.items()))}"
        print(msg, f"({time.time()-t0:.1f}s)", flush=True)


if __name__ == '__main__':
    main()
