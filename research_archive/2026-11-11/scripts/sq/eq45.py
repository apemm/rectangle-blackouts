"""Eager SAT: is there a blackout with m+q black points that is valid for a family of rectangles?
family = 'axis', 'diag' (axis + 45 degrees) or 'all'. Independent of the scripts in ../v45."""
import sys, time, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType

def rects(h, m, family):
    R = set()
    pts = [(x, y) for x in range(1, m+1) for y in range(1, h+1)]
    inside = lambda p: 1 <= p[0] <= m and 1 <= p[1] <= h
    for x1 in range(1, m+1):
        for x2 in range(x1+1, m+1):
            for y1 in range(1, h+1):
                for y2 in range(y1+1, h+1):
                    R.add(frozenset([(x1,y1),(x1,y2),(x2,y1),(x2,y2)]))
    if family == 'diag':
        for (x, y) in pts:
            for s in range(1, h):
                for t in range(1, h):
                    c = [(x,y),(x+s,y+s),(x+t,y-t),(x+s+t,y+s-t)]
                    if all(inside(p) for p in c): R.add(frozenset(c))
    if family == 'all':
        for (x, y) in pts:
            for ux in range(1, m):
                for uy in range(1, h):
                    a = (x+ux, y+uy)
                    if not inside(a): continue
                    for vx in range(1, m):
                        for vy in range(-h+1, 0):
                            if ux*vx + uy*vy != 0: continue
                            b = (x+vx, y+vy); c = (x+ux+vx, y+uy+vy)
                            if inside(b) and inside(c): R.add(frozenset([(x,y),a,b,c]))
    return list(R)

def solve(h, m, family, limit):
    q = h*h//4
    R = rects(h, m, family)
    var = {(x,y): (x-1)*h + y for x in range(1,m+1) for y in range(1,h+1)}
    top = m*h
    clauses = set()
    by_pt = {}
    for i, r in enumerate(R):
        for p in r: by_pt.setdefault(p, []).append(i)
    # pairs sharing at least one corner
    seen = set()
    for p, lst in by_pt.items():
        for i, j in itertools.combinations(lst, 2):
            if (i, j) in seen: continue
            seen.add((i, j))
            d = R[i] ^ R[j]
            clauses.add(tuple(sorted(-var[c] for c in d)))
    # disjoint pairs: both fully black. Fully black axis rectangles are excluded outright (m >= 3).
    tilted = []
    for r in R:
        xs = {p[0] for p in r}
        if len(xs) == 2: clauses.add(tuple(sorted(-var[c] for c in r)))
        else: tilted.append(r)
    for a, b in itertools.combinations(tilted, 2):
        if not (a & b): clauses.add(tuple(sorted(-var[c] for c in a | b)))
    # redundant structure of equality boards (h >= 4): every column has 1 or 2 black points
    for x in range(1, m+1):
        col = [var[(x,y)] for y in range(1,h+1)]
        clauses.add(tuple(col))
        for t3 in itertools.combinations(col, 3): clauses.add(tuple(-v for v in t3))
    card = CardEnc.atleast(lits=list(var.values()), bound=m+q, top_id=top, encoding=EncType.seqcounter)
    s = Cadical153(bootstrap_with=[list(c) for c in clauses] + card.clauses)
    t0 = time.time()
    import threading
    timer = threading.Timer(limit, lambda: s.interrupt())
    timer.start()
    res = s.solve_limited(expect_interrupt=True)
    timer.cancel()
    out = {True: 'SAT', False: 'UNSAT', None: 'TIMEOUT'}[res]
    board = None
    if res:
        model = set(v for v in s.get_model() if v > 0)
        board = [[y for y in range(1,h+1) if var[(x,y)] in model] for x in range(1,m+1)]
    s.delete()
    return out, time.time()-t0, len(R), len(clauses), board

if __name__ == '__main__':
    family = sys.argv[1]; h = int(sys.argv[2]); m0 = int(sys.argv[3]); m1 = int(sys.argv[4]); limit = float(sys.argv[5])
    for m in range(m0, m1+1):
        out, dt, nr, nc, board = solve(h, m, family, limit)
        print(f"{family} h={h} m={m} q={h*h//4}: {out} in {dt:.1f}s (rectangles {nr}, clauses {nc})", flush=True)
        if board: print("   columns:", ' '.join(''.join(str(y) for y in col) for col in board), flush=True)
