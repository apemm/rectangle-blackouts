"""Check that inside one excursion, constraints join only the same or consecutive links.

Link of a label = side of the off-diagonal Hilbert block (the O2 or O4 child) that contains it.
Usage: py -I check_links.py Bside orient M
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from excursions import hilbert, vectors, scan


def main():
    Bs = int(sys.argv[1]); orient = sys.argv[2]; M = int(sys.argv[3])
    xs, ys = hilbert(Bs)
    if orient == 'swap':
        xs, ys = ys, xs
    half = Bs // 2
    diag = np.nonzero(xs == ys)[0]
    lo = int(diag[(xs[diag] == half - 1)][0]); hi = 2 * half * half
    ii = xs[lo:hi].astype(np.int64); jj = ys[lo:hi].astype(np.int64)
    N = hi - lo
    # link side: smallest k with ii//k == jj//k, halved
    link = np.ones(N, dtype=np.int64)
    k = np.ones(N, dtype=np.int64)
    while True:
        m = (ii // k) != (jj // k)
        if not m.any():
            break
        k[m] *= 2
    link = k // 2  # 0 for the diagonal cell
    vecs = vectors(2 * Bs - 1)
    buf = np.zeros(N, dtype=np.int64)
    worst = 0; tot = 0; same = 0
    for (q, Y, L) in vecs:
        for d in sorted({q // M, -(-q // M)}):
            if d < 1 or d >= N or abs(q - M * d) > M - 1:
                continue
            c = scan(ii, jj, d, Y, L, Bs, 0, buf)
            if c:
                r = buf[:c]; s = r + d
                a = link[r]; b = link[s]
                assert (a > 0).all() and (b > 0).all()
                ratio = np.maximum(a, b) // np.minimum(a, b)
                worst = max(worst, int(ratio.max())); tot += c; same += int(np.count_nonzero(ratio == 1))
                # Lemma A': rank length at most (min link side)^2 ... for an endpoint with |T| <= 2s-1
                Tm = np.minimum(np.abs(jj[r] - ii[r]), np.abs(jj[s] - ii[s]))
                sreq = (Tm + 2) // 2  # least s with |T| <= 2s - 1
                assert (d <= np.maximum(sreq, 1) ** 2).all(), "Lemma A' violated"
    print(f"side {Bs} {orient} M={M}: pair incidences {tot}, same link {same}, max link-side ratio {worst}")


if __name__ == '__main__':
    main()
