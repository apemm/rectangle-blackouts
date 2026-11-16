"""Three-gap systems at M=3 with at least one gap divisible by 3.
For each gap set, find a period <= PMAX, else the shortest unsatisfiable interval <= LMAX."""
import sys, time, itertools, json
from pysat.solvers import Glucose4

def rels_of(Q):
    out = set()
    for q in Q:
        d, s = divmod(q, 3)
        if s == 0: out.add((d, 0))
        else:
            if d >= 1: out.add((d, s))
            out.add((d + 1, s - 3))
    return sorted(out)

def var(r, v): return 3 * r + v + 1

def cnf(R, n, periodic):
    cl = []
    for r in range(n):
        cl.append([var(r, 0), var(r, 1), var(r, 2)])
        for u in range(3):
            for w in range(u + 1, 3): cl.append([-var(r, u), -var(r, w)])
    for (k, d) in R:
        rng = range(n) if periodic else range(n - k)
        for r in rng:
            t = (r + k) % n if periodic else r + k
            for v in range(3):
                w = v + d
                if 0 <= w <= 2:
                    if r == t:
                        if d == 0: cl.append([-var(r, v)])
                    else: cl.append([-var(r, v), -var(t, w)])
    return cl

def sat(cl, n):
    with Glucose4(bootstrap_with=cl) as S:
        if S.solve():
            m = set(x for x in S.get_model() if x > 0)
            return [next(v for v in range(3) if var(r, v) in m) for r in range(n)]
    return None

def decide(Q, PMAX, LMAX):
    R = rels_of(Q)
    for p in range(1, PMAX + 1):
        if any(k % p == 0 and d == 0 for k, d in R): continue
        sol = sat(cnf(R, p, True), p)
        if sol: return ("period", p, ''.join(map(str, sol)))
    lo = max(k for k, _ in R) + 1
    for L in range(lo, LMAX + 1):
        if sat(cnf(R, L, False), L) is None: return ("unsat_interval", L)
    return ("undecided",)

if __name__ == "__main__":
    QMAX = int(sys.argv[1]); PMAX = int(sys.argv[2]); LMAX = int(sys.argv[3])
    t0 = time.time(); res = {}
    for Q in itertools.combinations(range(1, QMAX + 1), 3):
        if all(q % 3 for q in Q): continue
        res[str(Q)] = decide(Q, PMAX, LMAX)
        if time.time() - t0 > 50: print("time stop at", Q); break
    json.dump(res, open(sys.argv[4], "w"))
    from collections import Counter
    print(Counter(v[0] for v in res.values()))
    for k, v in res.items():
        if v[0] != "period": print(k, v)
    print("time", round(time.time() - t0, 1))
