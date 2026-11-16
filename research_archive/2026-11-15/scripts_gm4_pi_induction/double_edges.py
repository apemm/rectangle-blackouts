"""Exact sanity count on fixed systems: pairs (r,u) of cand G_B^o (M = 3) that carry two or
three distinct certified residues (q mod 3).  Also tests the mod-3 lemma: every constraint
with q not divisible by 3 has a cross pair with 3 | Y.
Usage: py -I double_edges.py B orient"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # local copy of the archive blk.py
import numpy as np
from blk import build
B, o = int(sys.argv[1]), sys.argv[2]
t0 = time.time()
xy, E = build(B, 32, 3, o, "cand")
print("triples", len(E), "time", round(time.time() - t0, 1))
key = E[:, 0] * (B * B) + E[:, 1]
res = E[:, 3] % 3
order = np.lexsort((res, key))
k2, r2 = key[order], res[order]
newpair = np.r_[True, k2[1:] != k2[:-1]]
pid = np.cumsum(newpair) - 1
newres = newpair | np.r_[True, r2[1:] != r2[:-1]]
nres = np.bincount(pid, weights=newres.astype(float)).astype(int)
print("pairs", len(nres), "with 1/2/3 distinct residues:", [(nres == k).sum() for k in (1, 2, 3)])
# mod-3 lemma check: for q % 3 != 0, recompute both cross Y and confirm one of them is 3 | Y with a leg
odd = 2 * xy[:, 0] + 1; even = 2 * xy[:, 1] + 2
bad = 0
sel = E[E[:, 3] % 3 != 0]
for r, u, dl, q in sel[:200000].tolist():
    ok = False
    for Y in (abs(int(even[u]) - int(odd[r])), abs(int(even[r]) - int(odd[u]))):
        X = 32 * q; L2 = X * X + Y * Y; L = int(round(L2 ** 0.5))
        while L * L > L2: L -= 1
        while (L + 1) ** 2 <= L2: L += 1
        if L * L == L2:
            ok = ok or (Y % 3 == 0)
    bad += (not ok)
print("nonzero-residue triples checked", min(len(sel), 200000), "violating mod-3 lemma:", bad)
# where are the double pairs: |T| of endpoints, d
dbl = np.unique(k2[newpair][nres >= 2])
r_ = dbl // (B * B); u_ = dbl % (B * B)
T = xy[:, 1] - xy[:, 0]
print("double pairs: |T_r| range", np.abs(T[r_]).min() if len(r_) else None, np.abs(T[r_]).max() if len(r_) else None,
      " d range", (u_ - r_).min() if len(r_) else None, (u_ - r_).max() if len(r_) else None)
print("labels in >= 1 double pair:", len(np.unique(np.r_[r_, u_])), "of", B * B)
