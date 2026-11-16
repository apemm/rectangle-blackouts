"""In the M-core, compare earlier constraint counts b^- with distinct earlier factors F^-."""
import sys
import numpy as np
from degeneracy_vs_mu import hilbert_array, pyth
from core_probe import kcore

def edges_with_factor(h, S, M):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    E = {}
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h: continue
            ys = pyth(X, h)
            if not ys: continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ys.items(): hyp[y] = L
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                Y = np.abs(r2 - r1); L = hyp[Y]; sm = r1 + r2
                hit = (L > 0) & (sm - L >= 2) & (sm + L <= 2 * h) & active[:-d] & active[d:]
                for r in np.nonzero(hit)[0].tolist():
                    a = (int(L[r]) - int(Y[r])) // 2
                    E.setdefault((r, r + d, delta), set()).add(a)
    return E

h, S, M = map(int, sys.argv[1:4])
Ed = edges_with_factor(h, S, M)
E = list(Ed)
V, Ec = kcore(E, M)
b = {}; F = {}
for (r, s, dl) in Ec:
    b[s] = b.get(s, 0) + 1
    F.setdefault(s, set()).update(Ed[(r, s, dl)])
n = len(V)
sb = sum(b.values()); sF = sum(len(x) for x in F.values())
print(f"h={h} S={S} M={M} core vertices={n} sum b^-={sb} sum F^-={sF} "
      f"avg b^-={sb/max(n,1):.3f} avg F^-={sF/max(n,1):.3f} "
      f"max b^-={max(b.values(), default=0)} max F^-={max((len(x) for x in F.values()), default=0)}")
