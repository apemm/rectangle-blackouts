# (1) Corner-chain lemma: if base-4 digits d_j = d_(j-1) in {0,3} (j = level, top digit = level n),
#     then bits j-1 and j-2 of both coordinates of H(r) coincide. Checked on sampled RQC curves.
# (2) Atom breaking: fraction of r with H(r+4^k) - H(r) = v (max over v), RQC vs deterministic Hilbert.
import random, numpy as np
from rqc import sample_curve, configs

def digits(r, n): return [(r >> (2*(j-1))) & 3 for j in range(1, n+1)]   # index j-1 -> level j

def hilbert(n):
    # deterministic Hilbert = RQC with the U order and Hilbert corner choices (standard d2xy)
    N = 1 << n; H = np.zeros((N*N, 2), dtype=np.int64)
    for d in range(N*N):
        x = y = 0; t = d; s = 1
        while s < N:
            rx = 1 & (t // 2); ry = 1 & (t ^ rx)
            if ry == 0:
                if rx == 1: x, y = s-1-x, s-1-y
                x, y = y, x
            x += s*rx; y += s*ry; t //= 4; s *= 2
        H[d] = (x, y)
    return H

rng = random.Random(5); n = 7
viol = 0; checked = 0
for trial in range(4):
    H = sample_curve(n, rng)
    for r in range(len(H)):
        dg = digits(r, n)
        for j in range(2, n+1):
            if dg[j-1] == dg[j-2] and dg[j-1] in (0, 3):
                checked += 1
                for c in (0, 1):
                    if ((H[r][c] >> (j-1)) & 1) != ((H[r][c] >> (j-2)) & 1): viol += 1
print("corner-chain pairs checked", checked, "violations", viol)

Hd = hilbert(n)
for k in range(1, 6):
    d = 4**k
    def maxfrac(H):
        D = H[d:] - H[:-d]
        _, cnt = np.unique(D[:,0]*4096 + D[:,1], return_counts=True)
        return cnt.max() / len(H)
    rq = np.mean([maxfrac(sample_curve(n, rng)) for _ in range(3)])
    print("k=%d  Hilbert max fraction %.4f   RQC max fraction %.4f   bound (3/4)^k %.4f" % (k, maxfrac(Hd), rq, 0.75**k))
