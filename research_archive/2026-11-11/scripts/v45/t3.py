import sys, time
from itertools import combinations
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from core import rects

def solve(h, m, tlimit):
    q = h*h//4; k = h//2
    n = 0
    def new():
        nonlocal n; n += 1; return n
    b = [[new() for y in range(h)] for c in range(m)]
    s = [new() for y in range(h)]
    cl = []
    for c in range(m):
        cl.append([b[c][y] for y in range(h)])
        for t in combinations(range(h),3): cl.append([-b[c][y] for y in t])
        for x,y in combinations(range(h),2):
            cl.append([-b[c][x],-b[c][y],-s[x],-s[y]])
            cl.append([-b[c][x],-b[c][y], s[x], s[y]])
    p = {}
    for c in range(m):
        for x,y in combinations(range(h),2):
            v = new(); p[c,x,y] = v
            cl += [[-v,b[c][x]],[-v,b[c][y]],[v,-b[c][x],-b[c][y]]]
    for x,y in combinations(range(h),2):
        ps = [p[c,x,y] for c in range(m)]
        cl.append([-s[x], s[y]] + ps)
        cl.append([s[x], -s[y]] + ps)
        for c1,c2 in combinations(range(m),2): cl.append([-p[c1,x,y],-p[c2,x,y]])
    card = CardEnc.equals(lits=s, bound=k, top_id=n, encoding=EncType.seqcounter)
    cl += card.clauses
    sol = Cadical153(bootstrap_with=cl)
    R = rects(h, m)
    it = 0; t0 = time.time()
    while True:
        if time.time()-t0 > tlimit: return "TIMEOUT", it, None
        if not sol.solve(): return "UNSAT", it, None
        model = set(l for l in sol.get_model() if l > 0)
        S = {(c+1,y+1) for c in range(m) for y in range(h) if b[c][y] in model}
        seen = {}; added = 0; ds = set()
        for r in R:
            key = frozenset(pt for pt in r if pt not in S)
            if key in seen:
                D = r ^ seen[key]
                if D not in ds:
                    ds.add(D)
            else: seen[key] = r
            if len(ds) >= 300: break
        if not ds:
            Xs = [y+1 for y in range(h) if s[y] in model]
            return "SAT", it, (S, Xs)
        for D in ds:
            sol.add_clause([-b[x-1][y-1] for (x,y) in D])
        it += 1

if __name__ == "__main__":
    h = int(sys.argv[1]); tl = float(sys.argv[2]); extra = int(sys.argv[3])
    q = h*h//4
    least = None; m = q
    while True:
        t = time.time()
        res, it, sol = solve(h, m, tl)
        print(f"h={h} m={m} {res} iters={it} time={time.time()-t:.1f}s" + (f" X={sol[1]} S={sorted(sol[0])}" if sol else ""), flush=True)
        if res == "SAT" and least is None: least = m
        if res == "TIMEOUT": break
        if least is not None and m >= least + extra: break
        m += 1
