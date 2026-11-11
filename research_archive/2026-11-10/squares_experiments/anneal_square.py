"""Lower bounds on f(n, n) by annealing: k black cells, move one cell at a time,
minimise the number of collisions M4 + M6 (rectcore). A board with no collision
is checked by the diagonal enumeration before it is written.

Usage: py anneal_square.py N K SECONDS [SEED]    (writes data/anneal_nN_kK_sSEED.json)
"""
import json
import sys
import time
from pathlib import Path

import numpy as np
from numba import njit

from rectcore import State, add_cell, remove_cell, verify_board, verify_plain

HERE = Path(__file__).resolve().parent


@njit(cache=True)
def run(h, m, black, blist, nb, pos, nP, tp, tot, nmoves, T, seed):
    np.random.seed(seed)
    NN = h * m
    E = tot[0] + tot[1]
    for it in range(nmoves):
        if E == 0:
            break
        x = blist[np.random.randint(0, nb)]
        y = np.random.randint(0, NN)
        if black[y]:
            continue
        nb = remove_cell(h, m, black, blist, nb, pos, nP, tp, tot, x)
        nb = add_cell(h, m, black, blist, nb, pos, nP, tp, tot, y)
        E2 = tot[0] + tot[1]
        d = E2 - E
        if d <= 0 or np.random.random() < np.exp(-d / T):
            E = E2
        else:
            nb = remove_cell(h, m, black, blist, nb, pos, nP, tp, tot, y)
            nb = add_cell(h, m, black, blist, nb, pos, nP, tp, tot, x)
    return nb


if __name__ == '__main__':
    n, k, seconds = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    rng = np.random.default_rng(seed)
    t0 = time.monotonic()
    found = []
    restarts = 0
    best_E = None
    while time.monotonic() - t0 < seconds and len(found) < 50:
        restarts += 1
        st = State(n, n, [int(v) for v in rng.choice(n * n, k, replace=False)])
        for T in np.geomspace(1.2, 0.15, 40):
            st.nb = run(n, n, st.black, st.blist, st.nb, st.pos, st.nP, st.tp, st.tot, 20000, T, int(rng.integers(1 << 30)))
            if st.tot[0] + st.tot[1] == 0 or time.monotonic() - t0 > seconds:
                break
        E = int(st.tot[0] + st.tot[1])
        best_E = E if best_E is None else min(best_E, E)
        if E == 0:
            cells = st.cells()
            if verify_board(n, n, cells, full=True)[0] and verify_plain(n, n, cells)[0] and cells not in found:
                found.append(cells)
    out = {'n': n, 'k': k, 'seed': seed, 'seconds': round(time.monotonic() - t0, 1), 'restarts': restarts,
           'least_collisions_at_end_of_a_run': best_E, 'valid_boards_found': len(found), 'boards': found}
    (HERE / 'data' / f'anneal_n{n}_k{k}_s{seed}.json').write_text(json.dumps(out))
    print({key: val for key, val in out.items() if key != 'boards'}, flush=True)
