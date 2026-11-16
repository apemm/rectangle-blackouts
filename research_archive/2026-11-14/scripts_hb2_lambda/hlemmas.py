"""Sanity checks of Lemmas H1, H3, H4 on the recursion (2) Hilbert order."""
import json, math
import numpy as np
from angles import hilbert

q = 256
n = int(math.log2(q))
xy = np.array(hilbert(q), dtype=np.int64)
I, J = xy[:, 0], xy[:, 1]
N = q * q
res = {}
# H1: max over intervals of length L of #{s : I[s] = i0}  vs 4 sqrt(L)
h1 = []
for L in (1, 3, 10, 50, 200, 1000, 5000):
    worst = 0
    for i0 in range(0, q, 7):
        ind = (I == i0).astype(np.int64)
        c = np.concatenate([[0], np.cumsum(ind)])
        worst = max(worst, int((c[L:] - c[:-L]).max()))
    h1.append((L, worst, round(4 * math.sqrt(L), 1)))
res['H1_L_worst_bound'] = h1
# H3: fraction of r with H(r+4^k) - H(r) = +-(2^k,0) exactly (and (0,+-2^k))
h3 = []
for k in range(0, n - 1):
    t = 4 ** k
    dI = I[t:] - I[:-t]; dJ = J[t:] - J[:-t]
    fi = np.mean((np.abs(dI) == 2 ** k) & (dJ == 0))
    fj = np.mean((np.abs(dJ) == 2 ** k) & (dI == 0))
    h3.append((k, round(float(fi), 4), round(float(fj), 4), round(4 / 2 ** k, 4)))
res['H3_k_fracI_fracJ_vs_4_over_sqrt_t'] = h3
# H4: P(c | Y2(r,d)), Y2 = 2 J[r+d] + 1 - 2 I[r], vs 5/c + 8 sqrt(d c)/q
h4 = []
for d in (1, 4, 30):
    Y2 = 2 * J[d:] + 1 - 2 * I[:-d]
    for c in (3, 9, 27, 81):
        p = float(np.mean(Y2 % c == 0))
        h4.append((d, c, round(p, 4), round(5 / c + 8 * math.sqrt(d * c) / q, 4), round(1 / c, 4)))
res['H4_d_c_freq_bound_1overc'] = h4
print(json.dumps(res))
