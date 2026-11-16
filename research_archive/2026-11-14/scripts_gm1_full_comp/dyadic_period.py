"""Uncovered M=3 two-gap class reduced mod P = 2^(alpha+1): shift 2^alpha (!=), beta (!= s), beta+1 (!= s-3).
For each alpha, beta in 1..P-2, s in {1,2}: is there a solution on Z/P? Print failures and sample solutions."""
import sys
from pysat.solvers import Cadical153

def solve_mod(P, shifts):
    sol = Cadical153(); var = lambda k, c: 3 * k + c + 1
    for k in range(P):
        sol.add_clause([var(k, c) for c in range(3)])
        for c in range(3):
            for c2 in range(c + 1, 3): sol.add_clause([-var(k, c), -var(k, c2)])
    for sh, dl in shifts:
        for k in range(P):
            k2 = (k + sh) % P
            for c in range(3):
                c2 = c + dl
                if 0 <= c2 <= 2:
                    if k2 == k and c2 == c: return None
                    sol.add_clause([-var(k, c), -var(k2, c2)])
    if not sol.solve(): return None
    m = sol.get_model()
    return [next(c for c in range(3) if m[3 * k + c] > 0) for k in range(P)]

def check(seq, shifts):
    P = len(seq)
    return all(seq[(k + sh) % P] - seq[k] != dl for sh, dl in shifts for k in range(P))

if __name__ != "__main__": raise SystemExit
amax = int(sys.argv[1])
for al in range(1, amax + 1):
    P = 2 ** (al + 1); fails = []; ex = {}
    for beta in range(1, P - 1):
        for s in (1, 2):
            sh = [(2 ** al, 0), (beta, s), (beta + 1, s - 3)]
            seq = solve_mod(P, sh)
            if seq is None or not check(seq, sh): fails.append((beta, s))
            elif beta in (1, 2, P - 2) : ex[(beta, s)] = "".join(map(str, seq))
    print("alpha", al, "P", P, "failures (beta,s):", fails)
    if al <= 3: print("   samples", ex)
