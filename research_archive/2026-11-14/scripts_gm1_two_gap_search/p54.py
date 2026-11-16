import sys, time
sys.path.insert(0, '.')
from tg import *
p = int(sys.argv[1]); t0 = time.time(); bad = []
als = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else range(1, p)
for al in als:
    for be in range(p):
        for s in (1, 2):
            bb = be if be else p
            sol = solve(periodic_cnf(al, bb, s, p), p)
            if sol is None: bad.append((al, be, s))
            else: assert check_periodic(al, bb, s, sol)
print(p, "bad", len(bad), bad[:40], "time", round(time.time() - t0, 1))
