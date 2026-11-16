"""Components of a saved weighted M-core: labels, constraints, distinct gaps,
gaps divisible by M, delta histogram.  Usage: py -B core_stats.py prefix M"""
import sys
from collections import Counter
import numpy as np


def components(C):
    verts = np.unique(C[:, :2])
    idx = {int(v): k for k, v in enumerate(verts)}
    par = list(range(len(verts)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for r, u, _ in C.tolist():
        a, b = find(idx[r]), find(idx[u])
        if a != b:
            par[a] = b
    lab = np.array([find(idx[int(r)]) for r in C[:, 0]])
    out = []
    for c in np.unique(lab):
        out.append(C[lab == c])
    out.sort(key=lambda e: -len(e))
    return out


if __name__ == "__main__":
    C = np.load(sys.argv[1] + "_core.npy").astype(np.int64)
    M = int(sys.argv[2])
    comps = components(C)
    print(f"{sys.argv[1]}: core constraints {len(C)}, labels {len(np.unique(C[:, :2]))}, components {len(comps)}")
    for E in comps:
        q = M * (E[:, 1] - E[:, 0]) + E[:, 2]
        gs = np.unique(q)
        pairs = len({(a, b) for a, b in E[:, :2].tolist()})
        print(f"  labels {len(np.unique(E[:, :2]))}, constraints {len(E)}, label pairs {pairs}, gaps {len(gs)}, "
              f"gaps div by M {int((gs % M == 0).sum())}, delta hist {sorted(Counter(E[:, 2].tolist()).items())}, "
              f"rank span {int(E[:, :2].min())}..{int(E[:, :2].max())}")
