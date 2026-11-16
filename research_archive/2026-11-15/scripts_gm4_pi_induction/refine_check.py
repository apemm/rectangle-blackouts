"""Sanity checks for the refinement statement (fixed small systems).
(1) coarsening: cells of W_{j+1} (O4 of the id block of side 2^{j+2}) with (x//2, y//2) and rank//4
    equal the cells of W_j (O4 of the id block of side 2^{j+1}), up to a diagonal translation.
(2) refinement does not carry cand: for each constrained pair of W_j, does some pair of their
    2x2 refinements in W_{j+1} carry a constraint, and how many refined constrained pairs have
    an unconstrained parent pair."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # local copy of the archive blk.py
import numpy as np
from blk import hilbert_array, legs, kernel

M, S = 3, 32


def cand(cells, Ymax):
    odd = np.ascontiguousarray(2 * cells[:, 0] + 1).astype(np.int64)
    even = np.ascontiguousarray(2 * cells[:, 1] + 2).astype(np.int64)
    P = legs(Ymax, S); qs, offs, Ys, Ls = [], [0], [], []
    for qq in sorted(P):
        qs.append(qq)
        for Y, L in P[qq]:
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((3_000_000, 4), dtype=np.int64)
    cnt = kernel(odd, even, (Ymax + 8) // 4 + 1, M, False, np.array(qs), np.array(offs),
                 np.array(Ys), np.array(Ls), out)
    return np.unique(out[:cnt], axis=0)


for j in (6, 7, 8):
    m = 2 ** j
    Wj = hilbert_array(2 * m)[3 * m * m:]
    Wn = hilbert_array(4 * m)[12 * m * m:]
    coarse = Wn[::4] // 2
    blocks_ok = all((Wn[4 * i:4 * i + 4] // 2 == coarse[i]).all() for i in range(0, len(coarse), 997))
    sh = coarse[0] - Wj[0]
    print(f"j={j}: coarsened W_(j+1) = W_j + {tuple(sh)}: {(coarse - sh == Wj).all()} (diagonal {sh[0] == sh[1]}), 4-rank groups are 2x2 blocks: {blocks_ok}")
    Ec = cand(Wj, 4 * m + 3); Ef = cand(Wn, 8 * m + 3)
    cp = set(map(tuple, Ec[:, :2].tolist()))
    fp = set((r // 4, u // 4) for r, u in Ef[:, :2].tolist() if r // 4 != u // 4)
    print(f"   coarse constrained pairs {len(cp)}; with a constrained refined pair {len(cp & fp)}; "
          f"refined-constrained parent pairs {len(fp)}, of which unconstrained at the coarse level {len(fp - cp)}")
