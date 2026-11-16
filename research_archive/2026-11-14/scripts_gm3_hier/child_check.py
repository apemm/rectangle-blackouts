"""Check that restrictions of the B1024 cand certificates to diagonal children are
certified solutions of the cand child systems (nesting), as used for the counterexample.
Usage: py -B child_check.py cert.npz"""
import sys
import numpy as np
from blk import build
z = np.load(sys.argv[1])
for o in ("id", "swap"):
    _, E = build(512, 32, 3, o, "cand")
    for key, start in (("full_swap_cand_B1024_M3_cert", 0) if o == "id" else ("full_id_cand_B1024_M3_cert", 0),
                       ("full_id_cand_B1024_M3_cert", 2 * 512 * 512) if o == "id" else ("full_swap_cand_B1024_M3_cert", 2 * 512 * 512)):
        y = z[key].astype(np.int64)[start:start + 512 * 512]
        bad = int(((y[E[:, 1]] - y[E[:, 0]] - E[:, 2]) % 3 == 0).sum())
        print(f"cand G_512^{o} ({len(E)} triples) vs {key}[{start}:+512^2]: certified violations {bad}")
