"""Sanity data only: triples per label and certified 3-core size of the single block
W_j = O4(P_{j+1}) (id P), j = 6..10, cand, S = 32, M = 3 (fixed systems, no census)."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # local copy of the archive blk.py
import numpy as np
from blk import hilbert_array, weighted_core
exec(open("type_check.py").read().split("s = 256\nF = forms(s)")[0].split("CLS = ")[0])  # imports + forms
from blk import legs, kernel
M, S = 3, 32
def cand(cells, Ymax):
    odd = np.ascontiguousarray(2 * cells[:, 0] + 1).astype(np.int64)
    even = np.ascontiguousarray(2 * cells[:, 1] + 2).astype(np.int64)
    P = legs(Ymax, S); qs, offs, Ys, Ls = [], [0], [], []
    for qq in sorted(P):
        qs.append(qq)
        for Y, L in P[qq]: Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((6_000_000, 4), dtype=np.int64)
    cnt = kernel(odd, even, (Ymax + 8) // 4 + 1, M, False, np.array(qs), np.array(offs), np.array(Ys), np.array(Ls), out)
    assert cnt <= len(out)
    return np.unique(out[:cnt], axis=0)
for j in [int(a) for a in sys.argv[1:]] or range(6, 11):
    t0 = time.time(); m = 2 ** j
    W = hilbert_array(2 * m)[3 * m * m:]
    W = hilbert_array(2 * m)[3 * m * m:]
    E = cand(W, 4 * m + 3)
    K = weighted_core(m * m, E, 3, mod=3)
    lab = np.unique(K[:, :2]) if len(K) else []
    cdeg = 2 * len(K) / max(len(lab), 1)
    print(f"core mean certified degree {cdeg:.3f}")
    print(f"j={j}: labels {m*m}, triples {len(E)}, per label {len(E)/(m*m):.3f}, certified 3-core labels {len(lab)} ({len(lab)/(m*m):.3%}), {time.time()-t0:.1f}s")
