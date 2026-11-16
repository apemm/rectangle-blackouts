"""DEC at the 512 -> 1024 junctions: no certified-core component of the segment holds a
label before J_8 (start of the last block of the old tail) and a label after J.
Usage: py -B dec9.py seg.npz [more seg.npz ...]"""
import sys
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from blk import weighted_core

for f in sys.argv[1:]:
    z = np.load(f)
    E, lo, J, hi = z["E"], int(z["lo"]), int(z["J"]), int(z["hi"])
    J8 = J - (256 * 256 if hi > 600000 else 128 * 128)
    K = weighted_core(hi, E, 3, mod=3)
    labs = np.unique(K[:, :2])
    a = np.searchsorted(labs, K[:, 0]); b = np.searchsorted(labs, K[:, 1])
    nc, lab = connected_components(coo_matrix((np.ones(len(K)), (a, b)), shape=(len(labs),) * 2), directed=False)
    rows = []
    bad = 0
    for c in range(nc):
        L = labs[lab == c]
        p, m, w = int((L < J8).sum()), int(((L >= J8) & (L < J)).sum()), int((L >= J).sum())
        bad += bool(p and w)
        rows.append(f"({len(L)}: {p}/{m}/{w})")
    print(f"{f}: core components (size: before J8 / in W_8 / in W_9): {' '.join(rows)}; spanning J8 and J: {bad}")
