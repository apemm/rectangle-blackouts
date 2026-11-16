"""Modular core with CaDiCaL (compact binary clauses). Plain solve, no budget."""
import sys, json, time
from pathlib import Path
import numpy as np
F = Path(__file__).resolve().parent
sys.path.insert(0, str(F / 'local_sat_dependencies'))
from pysat.solvers import Solver
from probe_aligned_private_sat import core
events, side = sys.argv[1], int(sys.argv[2])
t = time.monotonic()
ev = np.load(events); n = side * side
vertices, ce, rounds = core(n, ev, 3)
index = np.full(n, -1, dtype=np.int32); index[vertices] = np.arange(len(vertices), dtype=np.int32)
a = 3 * index[ce[:, 0]].astype(np.int64) + 1; b = 3 * index[ce[:, 1]].astype(np.int64) + 1; g = ce[:, 2].astype(np.int64)
del ev
with Solver(name='cd19') as sat:
    for i in range(len(vertices)):
        x = 3 * i + 1
        sat.add_clause([x, x + 1, x + 2]); sat.add_clause([-x, -x - 1]); sat.add_clause([-x, -x - 2]); sat.add_clause([-x - 1, -x - 2])
    sat.add_clause([1])
    for c in range(3):
        la = (-(a + c)).tolist(); lb = (-(b + (c + g) % 3)).tolist()
        for p, q in zip(la, lb):
            sat.add_clause([p, q])
        del la, lb
    print('loaded', len(vertices), len(ce), round(time.monotonic() - t), flush=True)
    ans = sat.solve()
    res = dict(side=side, core_vertices=len(vertices), core_events=len(ce), solver='cd19', model='certified_modular',
               seconds=round(time.monotonic() - t))
    if ans:
        col = np.full(len(vertices), -1, dtype=np.int8)
        for lit in sat.get_model():
            if 0 < lit <= 3 * len(vertices):
                col[(lit - 1) // 3] = (lit - 1) % 3
        assert (col >= 0).all()
        assert not np.any((col[index[ce[:, 1]]] - col[index[ce[:, 0]]] - ce[:, 2]) % 3 == 0)
        out = events.replace('_events.npy', '_sat_cadical')
        np.savez_compressed(out + '.npz', vertices=vertices.astype(np.int32), colors=col)
        res['status'] = 'SAT_DIRECTLY_CHECKED_CORE'
    else:
        res['status'] = 'UNSAT_SOLVER_REPORT_NOT_INDEPENDENTLY_PROVED'
    json.dump(res, open(events.replace('_events.npy', '_sat_cadical.json'), 'w'), indent=2)
    print(json.dumps(res), flush=True)
