"""Tests of analyze_h7 exact solvers on small random systems against brute force."""
import itertools, random
import numpy as np
import analyze_h7 as A
random.seed(1)
bad = 0
for trial in range(300):
    M = random.choice([2, 3]); n = random.randint(2, 7); E = random.randint(1, 3 * n)
    cons = set()
    for _ in range(E):
        a, b = sorted(random.sample(range(n), 2)); cons.add((a, b, random.randint(1 - M, M - 1)))
    cl = list(cons)
    brute = any(all(x[b] - x[a] != d for a, b, d in cl) for x in itertools.product(range(M), repeat=n))
    sol = A.two_sat(list(range(n)), cl) if M == 2 else A.backtrack(list(range(n)), cl, M)
    got = sol is not None
    if got and not all(sol[b] - sol[a] != d for a, b, d in cl): bad += 1
    if got != brute: bad += 1
    r = A.analyze(M, n, np.array(sorted(cl), np.int64))
    if r["M_suffices"] != brute: bad += 1
print("mismatches", bad)
