"""DSATUR upper bound for chi of Cay([0,n), D_T^inf ∩ [1,n)) (a finite piece; not chi_inf)."""
import sys
from dset import dset

def dsatur(n, E):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for d in E:
            if i + d < n: adj[i].append(i + d); adj[i + d].append(i)
    col = [-1] * n; sat = [set() for _ in range(n)]
    deg = [len(a) for a in adj]
    import heapq
    for _ in range(n):
        v = max((u for u in range(n) if col[u] < 0), key=lambda u: (len(sat[u]), deg[u]))
        c = 0
        while c in sat[v]: c += 1
        col[v] = c
        for u in adj[v]: sat[u].add(c)
    return max(col) + 1

if __name__ == "__main__":
    n = int(sys.argv[2])
    for T in [int(t) for t in sys.argv[1].split(",")]:
        E = sorted(d for d in dset(T, n) if d < n)
        print(T, len(E), dsatur(n, E), flush=True)
