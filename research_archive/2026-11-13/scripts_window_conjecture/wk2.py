"""wk.py with the triple scan precomputed as bitmasks (same semantics as wk.py).
L[N][O] = cells T such that {N, O, T} is a right-angle triple with vertex N or vertex O,
legs not axis-parallel, fourth corner inside the h x K grid.
Usage: py wk2.py h K lo hi [orbits]   with 'orbits': only one A per row-reflection orbit"""
import sys, itertools, time
from math import gcd

def build(h, K):
    cells = [(c, r) for c in range(1, K + 1) for r in range(1, h + 1)]
    cid = {p: i for i, p in enumerate(cells)}
    inside = lambda c, r: 1 <= c <= K and 1 <= r <= h
    L = {}
    for N in cells:
        for O in cells:
            if O == N: continue
            u1, u2 = O[0] - N[0], O[1] - N[1]
            if u1 == 0 or u2 == 0: continue
            g = gcd(abs(u1), abs(u2)); p1, p2 = -u2 // g, u1 // g
            m = 0
            for (V, E) in ((N, O), (O, N)):
                for t in range(-(h + K), h + K + 1):
                    if t == 0: continue
                    T = (V[0] + t * p1, V[1] + t * p2)
                    if not inside(*T): continue
                    F = (E[0] + T[0] - V[0], E[1] + T[1] - V[1])
                    if inside(*F):
                        m |= 1 << cid[T]
            L[(cid[N], cid[O])] = m
    return cells, cid, L

def count(h, K, A, cells, cid, L):
    B = [r for r in range(1, h + 1) if r not in A]
    edges = [(min(a, b), max(a, b)) for a in A for b in B]
    total = [0]
    used = [False] * len(edges)
    pts = []
    def bad(n, P):
        for o in pts:
            if P & L.get((n, o), 0):
                return True
        return False
    def dfs(x, P):
        if x > K:
            total[0] += 1; return
        for j, (r1, r2) in enumerate(edges):
            if used[j]: continue
            n1, n2 = cid[(x, r1)], cid[(x, r2)]
            if bad(n1, P): continue
            P1 = P | (1 << n1); pts.append(n1)
            if not bad(n2, P1):
                used[j] = True; pts.append(n2)
                dfs(x + 1, P1 | (1 << n2))
                pts.pop(); used[j] = False
            pts.pop()
    dfs(1, 0)
    return total[0]

if __name__ == "__main__":
    h, K, lo, hi = map(int, sys.argv[1:5])
    parts = [A for A in itertools.combinations(range(1, h + 1), h // 2) if h % 2 == 1 or 1 in A]
    if len(sys.argv) > 5:
        def canon(A):
            Es = lambda S: frozenset(frozenset((a, b)) for a in S for b in range(1, h + 1) if b not in S)
            return Es(A)
        seen = set(); reps = []
        for A in parts:
            Ar = tuple(sorted(h + 1 - a for a in A))
            k1, k2 = canon(A), canon(Ar)
            if k1 in seen or k2 in seen: continue
            seen.add(k1); reps.append(A)
        parts = reps
    t0 = time.time()
    cells, cid, L = build(h, K)
    print('build', round(time.time() - t0, 1), 'A-sets', len(parts), flush=True)
    for A in parts[lo:hi]:
        print('A', A, 'K', K, 'windows', count(h, K, A, cells, cid, L), flush=True)
    print('total sec', round(time.time() - t0, 1))
