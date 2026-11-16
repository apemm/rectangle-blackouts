"""k-gap systems at general M: find period <= PMAX else shortest unsat interval <= LMAX."""
import sys, time, itertools, json
from pysat.solvers import Glucose4
def rels_of(Q, M):
    out = set()
    for q in Q:
        d, s = divmod(q, M)
        if s == 0: out.add((d, 0))
        else:
            if d >= 1: out.add((d, s))
            out.add((d + 1, s - M))
    return sorted(out)
def cnf(R, n, M, periodic):
    V = lambda r, v: M * r + v + 1
    cl = []
    for r in range(n):
        cl.append([V(r, v) for v in range(M)])
        for u in range(M):
            for w in range(u + 1, M): cl.append([-V(r, u), -V(r, w)])
    for (k, d) in R:
        for r in (range(n) if periodic else range(n - k)):
            t = (r + k) % n if periodic else r + k
            for v in range(M):
                w = v + d
                if 0 <= w < M:
                    if r == t:
                        if d == 0: cl.append([-V(r, v)])
                    else: cl.append([-V(r, v), -V(t, w)])
    return cl
def sat(cl):
    with Glucose4(bootstrap_with=cl) as S: return S.solve()
def decide(Q, M, PMAX, LMAX):
    R = rels_of(Q, M)
    for p in range(1, PMAX + 1):
        if any(k % p == 0 and d == 0 for k, d in R): continue
        if sat(cnf(R, p, M, True)): return ("period", p)
    for L in range(max(k for k, _ in R) + 1, LMAX + 1):
        if not sat(cnf(R, L, M, False)): return ("unsat_interval", L)
    return ("undecided",)
if __name__ == "__main__":
    M, K, QMAX, PMAX, LMAX = map(int, sys.argv[1:6])
    t0 = time.time(); res = {}
    for Q in itertools.combinations(range(1, QMAX + 1), K):
        if all(q % M for q in Q): continue
        res[str(Q)] = decide(Q, M, PMAX, LMAX)
        if time.time() - t0 > 50: print("time stop at", Q); break
    from collections import Counter
    print(Counter(v[0] for v in res.values()))
    print([ (k,v) for k,v in res.items() if v[0] != "period"][:40])
    print("time", round(time.time() - t0, 1))
