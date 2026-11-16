"""Interface of a tail with the block attached after it, inside one segment.
Usage: py -B interface.py B orient version M lo J hi
  ranks [lo, J) = the old tail, [J, hi) = the attached off-diagonal block.
Reports: crossing triples (all, and inside the certified M-core), their gaps, the
touched labels, the T and rank-depth ranges, and whether the certified core of the
old tail alone is a union of components of the certified core of the whole segment.
Saves seg_<orient>_<version>_B<B>_<lo>.npz with the segment triples (global ranks).
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from blk import build, weighted_core

B, orient, version, M = int(sys.argv[1]), sys.argv[2], sys.argv[3], int(sys.argv[4])
lo, J, hi = int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])
t0 = time.time()
xy, E = build(B, 32, M, orient, version)
n = B * B
T = xy[:, 1] - xy[:, 0]
inseg = (E[:, 0] >= lo) & (E[:, 1] < hi)
assert not (((E[:, 0] >= lo) & (E[:, 0] < hi)) ^ ((E[:, 1] >= lo) & (E[:, 1] < hi))).any(), "segment not closed"
E = E[inseg]
np.savez_compressed(f"seg_{orient}_{version}_B{B}_{lo}.npz", E=E, xy=xy[lo:hi], lo=lo, J=J, hi=hi)
cross = (E[:, 0] < J) & (E[:, 1] >= J)
print(f"B={B} {orient} {version} M={M} segment [{lo},{hi}) junction {J}: triples {len(E)}, crossing {int(cross.sum())}")


def comps(C):
    labs = np.unique(C[:, :2]); idx = {v: k for k, v in enumerate(labs.tolist())}
    a = np.searchsorted(labs, C[:, 0]); b = np.searchsorted(labs, C[:, 1])
    g = coo_matrix((np.ones(len(C)), (a, b)), shape=(len(labs), len(labs)))
    nc, lab = connected_components(g, directed=False)
    return labs, nc, lab


Ccore = weighted_core(n, E, M, mod=M)          # certified core of the whole segment
labs, nc, lab = comps(Ccore)
cc = (Ccore[:, 0] < J) & (Ccore[:, 1] >= J)
print(f"  certified {M}-core: labels {len(labs)}, triples {len(Ccore)}, components {nc}, crossing triples in core {int(cc.sum())}")
for c in range(nc):
    L = labs[lab == c]
    print(f"    comp {c}: labels {len(L)} (old {int((L < J).sum())}, new {int((L >= J).sum())}), T in [{T[L].min()},{T[L].max()}]")
Eold = E[E[:, 1] < J]
Cold = weighted_core(n, Eold, M, mod=M)
if len(Cold):
    lo_labs, nco, labo = comps(Cold)
    print(f"  certified core of the old tail alone: labels {len(lo_labs)}, components {nco}")
    for c in range(nco):
        L = lo_labs[labo == c]
        # which new component holds it, and is it the whole component?
        pos = np.searchsorted(labs, L)
        ok = (pos < len(labs)) & (labs[np.minimum(pos, len(labs) - 1)] == L)
        hold = np.unique(lab[pos[ok]]) if ok.any() else []
        same = len(hold) == 1 and (lab == hold[0]).sum() == len(L)
        print(f"    old comp {c}: labels {len(L)}, T in [{T[L].min()},{T[L].max()}], inside new comps {list(hold)}, unchanged component: {same}")
else:
    print("  certified core of the old tail alone: empty")
X = E[cross]
q = X[:, 3]
print(f"  crossing triples: {len(X)}, distinct gaps {len(np.unique(q))}, gap range [{q.min()},{q.max()}]")
print(f"    old endpoints: {len(np.unique(X[:,0]))} labels, depth J-r in [{(J-X[:,0]).min()},{(J-X[:,0]).max()}], T in [{T[X[:,0]].min()},{T[X[:,0]].max()}]")
print(f"    new endpoints: {len(np.unique(X[:,1]))} labels, depth u-J in [{(X[:,1]-J).min()},{(X[:,1]-J).max()}], T in [{T[X[:,1]].min()},{T[X[:,1]].max()}]")
Xc = Ccore[cc]
if len(Xc):
    print(f"  crossing triples inside the certified core: {len(Xc)}, distinct gaps {len(np.unique(Xc[:,3]))}; old endpoints {len(np.unique(Xc[:,0]))}, new {len(np.unique(Xc[:,1]))}")
    if len(Cold):
        oldin = np.isin(Xc[:, 0], lo_labs)
        print(f"    of these, old endpoint lies in the old tail's own core: {int(oldin.sum())}")
print(f"  ({time.time()-t0:.1f}s)")
