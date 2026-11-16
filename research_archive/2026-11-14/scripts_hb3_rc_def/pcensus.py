"""Small P-candidate census: Hilbert vs random CGK curves, full-grid placement x = S(M r + xi).
Candidate (r, r+d, delta, role): X = S(M d + delta) > 0, Y = odd cross-parity row gap, X^2+Y^2 = L^2,
completion rows (y1+y2 -+ L)/2 in [1, h].  Weighted degeneracy: pair weight = number of distinct delta."""
import sys, random, time, heapq
import numpy as np
from curve import build

def census(H, h, S, M):
    q = int(np.sqrt(len(H)))
    A = (h + 1) // 2; K = h // 2
    i = H[:, 0]; j = H[:, 1]
    valid = (i < A) & (j < K)
    N = len(H)
    pairs = {}
    dmax = (h - 2) // (S * M) + 2
    for d in range(1, dmax + 1):
        e = np.arange(N - d); f = e + d
        ok = valid[e] & valid[f]
        e = e[ok]; f = f[ok]
        for role in (0, 1):
            if role == 0:
                y1 = 2 * i[e] + 1; y2 = 2 * j[f] + 2
            else:
                y1 = 2 * j[e] + 2; y2 = 2 * i[f] + 1
            Y = np.abs(y2 - y1)
            for delta in range(-(M - 1), M):
                x = S * (M * d + delta)
                if x <= 0 or x >= h: continue
                L2 = x * x + Y * Y
                L = np.rint(np.sqrt(L2)).astype(np.int64)
                hit = (L * L == L2) & (L <= h - 1)
                sm = y1 + y2
                lo = (sm - L) // 2; hi = (sm + L) // 2
                hit &= (lo >= 1) & (hi <= h)
                for a, b in zip(e[hit].tolist(), f[hit].tolist()):
                    pairs.setdefault((a, b), set()).add(delta)
    # weighted degeneracy
    adj = {}
    for (a, b), ds in pairs.items():
        w = len(ds)
        adj.setdefault(a, {})[b] = w; adj.setdefault(b, {})[a] = w
    deg = {v: sum(nb.values()) for v, nb in adj.items()}
    heap = [(dv, v) for v, dv in deg.items()]; heapq.heapify(heap)
    removed = set(); best = 0
    while heap:
        dv, v = heapq.heappop(heap)
        if v in removed or dv != deg[v]: continue
        best = max(best, dv); removed.add(v)
        for u, w in adj[v].items():
            if u not in removed:
                deg[u] -= w; heapq.heappush(heap, (deg[u], u))
    nlab = int(valid.sum())
    tot = sum(len(s) for s in pairs.values())
    maxdeg = max((sum(nb.values()) for nb in adj.values()), default=0)
    return len(pairs), 2 * tot / nlab, maxdeg, best

if __name__ == '__main__':
    h = int(sys.argv[1]); S = int(sys.argv[2]); M = int(sys.argv[3]); nrand = int(sys.argv[4])
    n = max(1, int(np.ceil(np.log2((h + 1) // 2))))
    rng = random.Random(2026)
    t0 = time.time()
    H = build(n, (0, 1), rng, hilbert=True)
    print('h', h, 'S', S, 'M', M, 'hilbert: pairs, mean weighted deg, max deg, weighted degeneracy =', census(H, h, S, M), round(time.time() - t0, 1), 's')
    for k in range(nrand):
        H = build(n, (0, 1), rng)
        print('   random%d:' % k, census(H, h, S, M), round(time.time() - t0, 1), 's')
