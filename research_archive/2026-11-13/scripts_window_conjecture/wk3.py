"""Count N-windows of fixed width K with forward checking and most-constrained-column order.
Third program. M[{a,b}] = cells c with {a,b,c} a right-angle triple (vertex any of the three),
legs not axis-parallel, fourth corner inside the h x K grid.  A point set is valid iff no such
triple lies in it.  F = union of M over pairs of placed points = cells that may no longer be used.
Usage: py wk3.py h K lo hi [orbits]"""
import sys, itertools, time

def build(h, K):
    cells = [(c, r) for c in range(1, K + 1) for r in range(1, h + 1)]
    n = len(cells)
    inside = lambda p: 1 <= p[0] <= K and 1 <= p[1] <= h
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        a = cells[i]
        for j in range(i + 1, n):
            b = cells[j]
            m = 0
            for k in range(n):
                if k == i or k == j: continue
                c = cells[k]
                for (V, X, Y) in ((a, b, c), (b, a, c), (c, a, b)):
                    u = (X[0] - V[0], X[1] - V[1]); v = (Y[0] - V[0], Y[1] - V[1])
                    if u[0] * v[0] + u[1] * v[1] != 0: continue
                    if u[0] == 0 or u[1] == 0: continue
                    if inside((X[0] + Y[0] - V[0], X[1] + Y[1] - V[1])):
                        m |= 1 << k; break
            M[i][j] = M[j][i] = m
    return cells, M

def count(h, K, A, cells, M, witness_out=None):
    B = [r for r in range(1, h + 1) if r not in A]
    edges = [(min(a, b), max(a, b)) for a in A for b in B]
    cid = {p: i for i, p in enumerate(cells)}
    ecell = [[(cid[(x, r1)], cid[(x, r2)]) for (r1, r2) in edges] for x in range(K + 1) if x >= 1]
    ecell.insert(0, None)
    total = [0]
    pts = []
    assign = {}
    def dfs(F, used, free):
        if not free:
            total[0] += 1
            if witness_out is not None and len(witness_out) < 50:
                witness_out.append([edges[assign[x]] for x in range(1, K + 1)])
            return
        # most constrained free column
        best = None
        for x in free:
            opts = [j for j in range(len(edges)) if not used >> j & 1
                    and not (F >> ecell[x][j][0]) & 1 and not (F >> ecell[x][j][1]) & 1]
            if not opts: return
            if best is None or len(opts) < len(best[1]):
                best = (x, opts)
                if len(opts) == 1: break
        x, opts = best
        nfree = [y for y in free if y != x]
        for j in opts:
            n1, n2 = ecell[x][j]
            F1 = F
            for o in pts: F1 |= M[n1][o]
            if (F1 >> n2) & 1: continue
            F2 = F1 | M[n1][n2]
            for o in pts: F2 |= M[n2][o]
            pts.append(n1); pts.append(n2); assign[x] = j
            dfs(F2, used | (1 << j), nfree)
            pts.pop(); pts.pop(); del assign[x]
    dfs(0, 0, list(range(1, K + 1)))
    return total[0]

def parts_list(h, orbits):
    parts = [A for A in itertools.combinations(range(1, h + 1), h // 2) if h % 2 == 1 or 1 in A]
    if not orbits: return parts
    Es = lambda S: frozenset(frozenset((a, b)) for a in S for b in range(1, h + 1) if b not in S)
    seen = set(); reps = []
    for A in parts:
        Ar = tuple(sorted(h + 1 - a for a in A))
        if Es(A) in seen or Es(Ar) in seen: continue
        seen.add(Es(A)); reps.append(A)
    return reps

if __name__ == "__main__":
    h, K, lo, hi = map(int, sys.argv[1:5])
    parts = parts_list(h, len(sys.argv) > 5)
    t0 = time.time()
    cells, M = build(h, K)
    print('build', round(time.time() - t0, 1), 'A-sets', len(parts), flush=True)
    for A in parts[lo:hi]:
        print('A', A, 'K', K, 'windows', count(h, K, A, cells, M), flush=True)
    print('total sec', round(time.time() - t0, 1))
