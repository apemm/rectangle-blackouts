import sys, time, json
sys.path.insert(0, r".")
from tg import *
A = int(sys.argv[1]); B = int(sys.argv[2]); PMAX = int(sys.argv[3])
t0 = time.time()
res = {}
for a in range(2, A + 1, 2):
    for b in range(1, B + 1):
        if not uncovered(a, b): continue
        for s in (1, 2):
            found = None
            for p in range(1, PMAX + 1):
                if a % p == 0: continue
                sol = solve(periodic_cnf(a, b, s, p), p)
                if sol is not None:
                    assert check_periodic(a, b, s, sol)
                    found = (p, ''.join(map(str, sol)))
                    break
            res[f"{a},{b},{s}"] = found
            if found is None: print("NOPERIOD", a, b, s, flush=True)
    if time.time() - t0 > 50: print("time stop at a", a); break
json.dump(res, open(sys.argv[4], 'w'))
for k, v in res.items(): print(k, v)
print("time", time.time() - t0)
