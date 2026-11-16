"""G_p(s): residue pairs (alpha,beta) mod p for which Z_p periodic solution exists."""
import sys, json, time
sys.path.insert(0, r".")
from tg import *
P = int(sys.argv[1])
out = {}
t0 = time.time()
for p in range(2, P + 1):
    for s in (1, 2):
        bad = []
        for al in range(1, p):
            for be in range(p):
                # periodic_cnf uses shifts mod p: a=al, b=be (b=0 means shift 0: rels skips b=0 C1; handle by p)
                bb = be if be > 0 else p
                sol = solve(periodic_cnf(al, bb, s, p), p)
                if sol is None: bad.append((al, be))
                else: assert check_periodic(al, bb, s, sol)
        out[f"{p},{s}"] = bad
        print(p, s, "bad", len(bad), "of", (p - 1) * p, bad if len(bad) < 30 else '', flush=True)
json.dump(out, open("gp.json", "w"))
print("time", time.time() - t0)
