"""Corner cuts of W_9 and W_10 in the saved J_11 window (dec11.py build). Usage: py -B check_win_cuts.py win.npz"""
import sys
import numpy as np
z = np.load(sys.argv[1]); E = z["E"].astype(np.int64); T = z["T"]
lo, J9, J10 = int(z["lo"]), int(z["J9"]), int(z["J10"])
R = lambda m: (m * m - 1) // 3
for name, p in [("c*(W_9)", J9 - lo + R(512)), ("c*(W_10)", J10 - lo + R(1024))]:
    cr = int(((E[:, 0] < p) & (E[:, 1] > p)).sum()); inc = int(((E[:, 0] == p) | (E[:, 1] == p)).sum())
    print(f"{name}: window rank {p}, T = {int(T[p])}, crossing triples {cr}, incident {inc}")
