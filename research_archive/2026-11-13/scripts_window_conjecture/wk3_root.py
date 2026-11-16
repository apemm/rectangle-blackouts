"""wk3 count with column 1 fixed to edge index j (root split).  Usage: py wk3_root.py h K A j1 j2"""
import sys, time
import wk3
h, K = int(sys.argv[1]), int(sys.argv[2])
A = tuple(int(t) for t in sys.argv[3].split(','))
j1, j2 = int(sys.argv[4]), int(sys.argv[5])
t0 = time.time(); cells, M = wk3.build(h, K)
B = [r for r in range(1, h + 1) if r not in A]
edges = [(min(a, b), max(a, b)) for a in A for b in B]
cid = {p: i for i, p in enumerate(cells)}
tot = 0
for j in range(j1, min(j2, len(edges))):
    # restrict: count windows whose column-1 pair is edges[j]
    r1, r2 = edges[j]
    n1, n2 = cid[(1, r1)], cid[(1, r2)]
    F = M[n1][n2]
    # run the wk3 DFS with column 1 pre-assigned
    total = [0]; pts = [n1, n2]
    ecell = [None] + [[(cid[(x, a)], cid[(x, b)]) for (a, b) in edges] for x in range(1, K + 1)]
    def dfs(F, used, free):
        if not free:
            total[0] += 1; return
        best = None
        for x in free:
            opts = [i for i in range(len(edges)) if not used >> i & 1
                    and not (F >> ecell[x][i][0]) & 1 and not (F >> ecell[x][i][1]) & 1]
            if not opts: return
            if best is None or len(opts) < len(best[1]):
                best = (x, opts)
                if len(opts) == 1: break
        x, opts = best
        nfree = [y for y in free if y != x]
        for i in opts:
            a, b = ecell[x][i]
            F1 = F
            for o in pts: F1 |= M[a][o]
            if (F1 >> b) & 1: continue
            F2 = F1 | M[a][b]
            for o in pts: F2 |= M[b][o]
            pts.append(a); pts.append(b)
            dfs(F2, used | (1 << i), nfree)
            pts.pop(); pts.pop()
    dfs(F, 1 << j, list(range(2, K + 1)))
    tot += total[0]
    print('j', j, edges[j], 'windows', total[0], round(time.time() - t0, 1), flush=True)
print('sum', tot)
