"""Baseline for the layout experiment: valid sets on the N x N grid built without
any incidence structure.

1. Random insertion: go through all N^2 cells in random order and keep a cell
   when the set stays valid.
2. The frame: row 1 and column 1 (2N - 1 cells), which is valid on every grid.

Usage: py baseline_insertion.py     (writes data/baseline_insertion.json)
"""
import json
import random
from pathlib import Path

import numpy as np

from rectcore import State, verify_board

HERE = Path(__file__).resolve().parent
rng = random.Random(7)
out = {}
for N, tries in ((8, 200), (15, 40), (27, 20), (40, 10), (64, 5), (125, 2)):
    sizes = []
    best = []
    for _ in range(tries):
        order = list(range(N * N))
        rng.shuffle(order)
        st = State(N, N)
        for x in order:
            st.add(x)
            if st.tot[0] + st.tot[1] > 0:
                st.remove(x)
        sizes.append(int(st.nb))
        if st.nb > len(best):
            best = st.cells()
    ok = verify_board(N, N, best)[0]
    frame = sorted(set(range(N)) | {r * N for r in range(N)})
    ok_frame = verify_board(N, N, frame)[0]
    assert ok and ok_frame
    out[N] = {'tries': tries, 'max': max(sizes), 'mean': float(np.mean(sizes)), 'best_cells': best,
              'best_verified': bool(ok), 'frame_size': len(frame), 'frame_verified': bool(ok_frame),
              'N^(6/5)': N ** 1.2, 'N^(4/3)': N ** (4 / 3)}
    print(N, 'random insertion max', max(sizes), 'mean', round(float(np.mean(sizes)), 1), '| frame', len(frame), flush=True)
(HERE / 'data' / 'baseline_insertion.json').write_text(json.dumps(out))
