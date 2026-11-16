"""Explicit blocked-label witnesses: W labels whose crossing triples, under the fixed old
values, forbid all three residues (so no certified extension exists, by hand).
Usage: py -B witness.py seg.npz cert.npz key src_lo B orient"""
import sys
import numpy as np
from blk import hilbert_array
z = np.load(sys.argv[1]); E, lo, J = z["E"], int(z["lo"]), int(z["J"])
y = np.load(sys.argv[2])[sys.argv[3]].astype(np.int64); src = int(sys.argv[4])
B, o = int(sys.argv[5]), sys.argv[6]
xy = hilbert_array(B)
if o == "swap": xy = xy[:, ::-1]
X = E[(E[:, 0] < J) & (E[:, 1] >= J)]
res = {}
for r, u, d, q in X.tolist():
    res.setdefault(u, []).append((r, d, q, (y[src + r - lo] + d) % 3))
blk = [u for u, L in res.items() if len({t[3] for t in L}) == 3]
print(f"{len(blk)} blocked W labels")
for u in blk[:2]:
    print(f" W label rank {u} cell {tuple(xy[u])}:")
    for r, d, q, f in res[u]:
        print(f"   old rank {r} cell {tuple(xy[r])} y={y[src + r - lo]} delta={d} gap q={q} -> forbids y_u = {f} (mod 3)")
