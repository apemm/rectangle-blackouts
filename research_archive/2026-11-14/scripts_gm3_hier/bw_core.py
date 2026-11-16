"""Backward relative core of the old tail A = [lo, J) with the attached block W = [J, hi)
held fixed: peel A labels whose distinct certified classes to alive A labels plus to W
number fewer than M.  If the result has no constraint to W, then every certified
solution of W combines with every certified solution of the result (Lemma RC).
Usage: py -B bw_core.py seg.npz
"""
import sys
import numpy as np
from blk import weighted_core

M = 3
z = np.load(sys.argv[1])
E, lo, J, hi = z["E"], int(z["lo"]), int(z["J"]), int(z["hi"])
key3 = np.stack([E[:, 0], E[:, 1], E[:, 2] % M], axis=1)
_, first = np.unique(key3, axis=0, return_index=True)
Ec = E[np.sort(first)][:, :3]
EA = Ec[Ec[:, 1] < J]
EX = Ec[(Ec[:, 0] < J) & (Ec[:, 1] >= J)]
n = J - lo
cW = np.bincount(EX[:, 0] - lo, minlength=n)
alive = np.ones(len(EA), dtype=bool)
while True:
    deg = cW + np.bincount(EA[alive, 0] - lo, minlength=n) + np.bincount(EA[alive, 1] - lo, minlength=n)
    bad = deg < M
    kill = alive & (bad[EA[:, 0] - lo] | bad[EA[:, 1] - lo])
    if not kill.any():
        break
    alive &= ~kill
R = np.flatnonzero(deg >= M) + lo
KA = weighted_core(hi, E[E[:, 1] < J], M, mod=M)
KAl = np.unique(KA[:, :2]) if len(KA) else np.array([], dtype=np.int64)
adjW = np.isin(R, EX[:, 0])
print(f"{sys.argv[1]}: A has {n} labels; certified core K_A {len(KAl)}; backward relative core {len(R)} labels, "
      f"{int(adjW.sum())} adjacent to W; equals K_A: {set(R.tolist()) == set(KAl.tolist())}")
