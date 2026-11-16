"""Re-run gapM periodic searches but extract and independently verify each periodic solution
against the raw slot rule: for ranks r<u (u-r>=1) with choices x_r,x_u, slot gap M(u-r)+x_u-x_r must not lie in Q.
Periodic solution of period p is checked on ranks 0..(p + maxshift) with all pairs at distance <= maxshift."""
import sys, itertools, time
from pysat.solvers import Glucose4
import gapM
def model(R, p, M):
    V = lambda r, v: M * r + v + 1
    with Glucose4(bootstrap_with=gapM.cnf(R, p, M, True)) as S:
        if not S.solve(): return None
        m = set(x for x in S.get_model() if x > 0)
        return [next(v for v in range(M) if V(r, v) in m) for r in range(p)]
def raw_ok(Q, M, sol):
    p = len(sol); Qs = set(Q); K = max(Q) // M + 2
    for r in range(p):
        for dd in range(1, K + 1):
            if M * dd + sol[(r + dd) % p] - sol[r] in Qs: return False
    return True
M, K, QMAX, PMAX = map(int, sys.argv[1:5])
t0 = time.time(); n = bad = 0
for Q in itertools.combinations(range(1, QMAX + 1), K):
    if all(q % M for q in Q): continue
    R = gapM.rels_of(Q, M)
    for p in range(1, PMAX + 1):
        if any(k % p == 0 and d == 0 for k, d in R): continue
        sol = model(R, p, M)
        if sol is not None:
            n += 1
            if not raw_ok(Q, M, sol): bad += 1; print("BAD", Q, sol)
            break
    if time.time() - t0 > 55: print("stop", Q); break
print("verified", n, "bad", bad, "time", round(time.time() - t0, 1))
