"""Second, independent count of N-windows of a fixed width K (written from the definition,
not from wn.py).  P = 2 points per column in the h x K grid, row pairs distinct edges of
K_{A,B}; valid iff no right-angle triple (O1, V, O2) of P with legs not axis-parallel has its
fourth corner O1 + O2 - V inside the h x K grid.  The condition is monotone in P, so the DFS
prunes as soon as a placed triple has its fourth corner anywhere in the h x K grid.

Usage: py wk.py h K lo hi    (A-sets lo..hi-1; A of size floor(h/2), for even h only A with 1)
Prints the number of windows of width K for each bipartition."""
import sys, itertools, time
from math import gcd

def count(h, K, A):
    B = [r for r in range(1, h + 1) if r not in A]
    edges = [(min(a, b), max(a, b)) for a in A for b in B]
    grid = [[False] * (h + 2) for _ in range(K + 2)]
    pts = []
    def inside(c, r):
        return 1 <= c <= K and 1 <= r <= h
    def bad_with(N):
        # some right-angle triple containing N, with the other two points in pts
        nc, nr = N
        for (oc, orow) in pts:
            if (oc, orow) == N:
                continue
            u1, u2 = oc - nc, orow - nr
            if u1 == 0 or u2 == 0:
                continue
            g = gcd(abs(u1), abs(u2))
            p1, p2 = -u2 // g, u1 // g
            # (i) N is the vertex: T = N + t p
            # (ii) O is the vertex: T = O + t p
            for (vc, vr, ec, er) in ((nc, nr, oc, orow), (oc, orow, nc, nr)):
                for sgn in (1, -1):
                    t = 1
                    while True:
                        tc, tr = vc + sgn * t * p1, vr + sgn * t * p2
                        if not inside(tc, tr):
                            break
                        if grid[tc][tr]:
                            fc, fr = ec + tc - vc, er + tr - vr
                            if inside(fc, fr):
                                return True
                        t += 1
        return False
    total = [0]
    used = [False] * len(edges)
    def dfs(x):
        if x > K:
            total[0] += 1
            return
        for j, (r1, r2) in enumerate(edges):
            if used[j]:
                continue
            N1, N2 = (x, r1), (x, r2)
            grid[x][r1] = True; pts.append(N1)
            ok = not bad_with(N1)
            if ok:
                grid[x][r2] = True; pts.append(N2)
                ok = not bad_with(N2)
                if ok:
                    used[j] = True
                    dfs(x + 1)
                    used[j] = False
                grid[x][r2] = False; pts.pop()
            grid[x][r1] = False; pts.pop()
    dfs(1)
    return total[0]

if __name__ == "__main__":
    h, K, lo, hi = map(int, sys.argv[1:5])
    parts = [A for A in itertools.combinations(range(1, h + 1), h // 2) if h % 2 == 1 or 1 in A]
    t0 = time.time()
    for A in parts[lo:hi]:
        print('A', A, 'K', K, 'windows', count(h, K, A), flush=True)
    print('total sec', round(time.time() - t0, 1), 'of', len(parts), 'A-sets')
