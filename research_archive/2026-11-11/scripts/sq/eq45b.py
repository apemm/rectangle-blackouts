"""Same question as eq45.py for the 45-degree family, with extra clauses that hold for every
blackout with m+q points (h >= 4): the row classes of the complete bipartite structure, and a
symmetry break (the board is the lexicographic leader under the two reflections). Usage: py eq45b.py h m"""
import sys, time, itertools
from pysat.solvers import Cadical153
from pysat.card import CardEnc, EncType
from eq45 import rects

def lex_geq(a, b, new_var):
    """clauses forcing bit vector a >= b lexicographically (first position most significant)."""
    cl = []
    prev = None  # prev true means all earlier positions equal
    for i, (x, y) in enumerate(zip(a, b)):
        e = new_var()  # e_i: positions 0..i all equal
        if prev is None:
            cl += [[x, -y]]                      # not (x=0 and y=1)
            cl += [[-e, x, -y], [-e, -x, y]]     # e -> x == y
            cl += [[e, x, y], [e, -x, -y]]       # x == y -> e
        else:
            cl += [[-prev, x, -y]]
            cl += [[-e, prev], [-e, x, -y], [-e, -x, y]]
            cl += [[e, -prev, x, y], [e, -prev, -x, -y]]
        prev = e
    return cl

def solve(h, m):
    q = h*h//4
    R = rects(h, m, 'diag')
    var = {(x,y): (x-1)*h + y for x in range(1,m+1) for y in range(1,h+1)}
    counter = [m*h]
    def new_var():
        counter[0] += 1
        return counter[0]
    clauses = set()
    by_pt = {}
    for i, r in enumerate(R):
        for p in r: by_pt.setdefault(p, []).append(i)
    seen = set()
    for p, lst in by_pt.items():
        for i, j in itertools.combinations(lst, 2):
            if (i, j) in seen: continue
            seen.add((i, j))
            clauses.add(tuple(sorted(-var[c] for c in R[i] ^ R[j])))
    tilted = []
    for r in R:
        if len({p[0] for p in r}) == 2: clauses.add(tuple(sorted(-var[c] for c in r)))
        else: tilted.append(r)
    for a, b in itertools.combinations(tilted, 2):
        if not (a & b): clauses.add(tuple(sorted(-var[c] for c in a | b)))
    extra = []
    for x in range(1, m+1):
        col = [var[(x,y)] for y in range(1,h+1)]
        extra.append(col)
        for t3 in itertools.combinations(col, 3): extra.append([-v for v in t3])
    # row classes: cls[y] true for the class of size floor(h/2); doubles join different classes
    cls = {y: new_var() for y in range(1, h+1)}
    for x in range(1, m+1):
        for y1, y2 in itertools.combinations(range(1, h+1), 2):
            extra.append([-var[(x,y1)], -var[(x,y2)], cls[y1], cls[y2]])
            extra.append([-var[(x,y1)], -var[(x,y2)], -cls[y1], -cls[y2]])
    eqk = CardEnc.equals(lits=list(cls.values()), bound=h//2, top_id=counter[0], encoding=EncType.seqcounter)
    counter[0] = max(counter[0], eqk.nv)
    extra += eqk.clauses
    if h % 2 == 0: extra.append([cls[1]])   # even h: the two classes can be swapped
    # symmetry: the board is lexicographically largest in its orbit under the two reflections
    # (one fixed order of the points for all three group elements, so the conditions are compatible)
    order = [(x, y) for x in range(1, m+1) for y in range(1, h+1)]
    base = [var[p] for p in order]
    for g in (lambda p: (m+1-p[0], p[1]), lambda p: (p[0], h+1-p[1]), lambda p: (m+1-p[0], h+1-p[1])):
        extra += lex_geq(base, [var[g(p)] for p in order], new_var)
    card = CardEnc.atleast(lits=list(var.values()), bound=m+q, top_id=counter[0], encoding=EncType.seqcounter)
    s = Cadical153(bootstrap_with=[list(c) for c in clauses] + extra + card.clauses)
    t0 = time.time()
    res = s.solve()
    out = 'SAT' if res else 'UNSAT'
    board = None
    if res:
        model = set(v for v in s.get_model() if v > 0)
        board = [[y for y in range(1,h+1) if var[(x,y)] in model] for x in range(1,m+1)]
    s.delete()
    return out, time.time()-t0, board

if __name__ == '__main__':
    h, m = int(sys.argv[1]), int(sys.argv[2])
    out, dt, board = solve(h, m)
    print(f"diag+sym h={h} m={m} q={h*h//4}: {out} in {dt:.1f}s", flush=True)
    if board: print("   columns:", ' '.join(''.join(str(y) for y in col) for col in board), flush=True)
