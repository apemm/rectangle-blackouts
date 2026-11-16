"""SAT check of the M-core of the main-diagonal block system (sanity tool)."""
import sys
import numpy as np
from pysat.solvers import Cadical153
from diag_fast import build
from diag_core import core


def sat_core(Ec, M):
    verts = np.unique(Ec[:, :2])
    idx = {int(v): k for k, v in enumerate(verts)}
    var = lambda v, c: idx[v] * M + c + 1
    s = Cadical153()
    for v in idx:
        s.add_clause([var(v, c) for c in range(M)])
    for a, b, d in Ec:
        a, b, d = int(a), int(b), int(d)
        for c in range(M):
            if 0 <= c + d < M:
                s.add_clause([-var(a, c), -var(b, c + d)])
    ok = s.solve()
    if not ok:
        return False, None
    model = set(x for x in s.get_model() if x > 0)
    val = {v: next(c for c in range(M) if var(v, c) in model) for v in idx}
    for a, b, d in Ec:
        assert val[int(b)] - val[int(a)] != int(d)
    return True, val


if __name__ == "__main__":
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    n, E = build(B, S, M, orient)
    Ec = core(n, E, M)
    print(f"B={B} S={S} M={M} {orient}: constraints={len(E)} avgdeg={2*len(E)/n:.4f} "
          f"core_vertices={len(np.unique(Ec[:, :2])) if len(Ec) else 0} core_constraints={len(Ec)}")
    if len(Ec):
        ok, _ = sat_core(Ec, M)
        print("  core SAT (verified)" if ok else "  core UNSAT")
