# The odd-odd intra-class M2c graph R_IV (cross_class_sea.md A2, family IV) in shifted
# coordinates u = (y_B - r0)/2 (odd). Edge (q m, p m), m odd, for lambda = (a, b) = (alpha'', beta)
# odd, coprime, 0 < a < b, with t = 4 m (b - a) b^2 / g, v2(t) = 2 + v2(b - a) >= k.
# Checks: each edge is a genuine M2c from the definition; edge density; degeneracy; greedy colours.
import sys
from math import gcd, isqrt
import numpy as np

def lambdas(X, k):
    out = []
    b = 3
    while 5 * b * b <= X:
        for a in range(1, b, 2):
            if gcd(a, b) != 1:
                continue
            d = b - a
            v = 0
            while d % 2 == 0:
                d //= 2; v += 1
            if 2 + v < k:
                continue
            F = 4 * (a - 2 * b) ** 2 + b * b
            g = gcd(F, b - a)
            q = a * F // g
            if q > X:
                continue
            p = (a * F + 4 * (b - a) * b * b) // g
            out.append((a, b, q, p))
        b += 2
    return out

def check_def(u, up, r0=1):
    # B = (0, 2u + r0), D = (4(up - u), 2up + r0); search shallow A, C as in M2c
    yB = 2 * u + r0; yD = 2 * up + r0; e = up - u; u2 = yB - r0; Dl = 4 * e
    found = False
    for n1 in range(-4 * h_cap, 4 * h_cap + 1):
        if n1 == 0 or (e * u2) % n1:
            continue
        if n1 * ((Dl - n1) ** 2 + e * e) != e * u2 * (Dl - 2 * n1):
            continue
        z = -e * u2 // n1
        xA = -z; xC = 2 * n1 - z - Dl
        if xA % 4 == 0 or xC % 4 == 0:
            continue
        A = (xA, r0); B = (0, yB); C = (xC, r0); D = (Dl, yD)
        U = (B[0] - A[0], B[1] - A[1]); V = (D[0] - C[0], D[1] - C[1])
        s = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
        nn = (s[0] // 2, s[1] // 2)
        ok = (U[0] ** 2 + U[1] ** 2 == V[0] ** 2 + V[1] ** 2 and s[0] % 2 == 0 and s[1] % 2 == 0
              and nn[0] * U[0] + nn[1] * U[1] == 0 and nn != (0, 0) and V != U and V != (-U[0], -U[1]))
        if ok:
            found = True
    return found

if __name__ == '__main__':
    X = int(sys.argv[1]); k = int(sys.argv[2])
    L = lambdas(X, k)
    print('lambdas with q <= X:', len(L), 'first', sorted(L, key=lambda t: t[3])[:6])
    h_cap = 2000
    # definition check of the smallest edges
    for (a, b, q, p) in sorted(L, key=lambda t: t[3])[:5]:
        print('  edge', (q, p), 'genuine M2c:', check_def(q, p))
    # edges among odd u <= X
    adj = {}
    E = 0
    for (a, b, q, p) in L:
        m = 1
        while p * m <= X:
            u, v = q * m, p * m
            adj.setdefault(u, set()).add(v); adj.setdefault(v, set()).add(u)
            E += 1
            m += 2
    V = len(adj)
    print('X=%d k=%d: edges %d (edges/X = %.5f), vertices touched %d (fraction of odd u: %.4f)' % (X, k, E, E / X, V, V / (X / 2)))
    # degeneracy (smallest-last)
    deg = {v: len(s) for v, s in adj.items()}
    import heapq
    heap = [(d, v) for v, d in deg.items()]
    heapq.heapify(heap)
    removed = set(); degen = 0; order = []
    while heap:
        d, v = heapq.heappop(heap)
        if v in removed or d != deg[v]:
            continue
        degen = max(degen, d)
        removed.add(v); order.append(v)
        for w in adj[v]:
            if w not in removed:
                deg[w] -= 1
                heapq.heappush(heap, (deg[w], w))
    col = {}
    for v in reversed(order):
        used = {col[w] for w in adj[v] if w in col}
        c = 0
        while c in used:
            c += 1
        col[v] = c
    print('degeneracy', degen, 'smallest-last colours', max(col.values()) + 1, 'max degree', max(len(s) for s in adj.values()))
    # odd cycles? bipartite test
    side = {}; bip = True
    for s0 in adj:
        if s0 in side: continue
        side[s0] = 0; st = [s0]
        while st:
            v = st.pop()
            for w in adj[v]:
                if w not in side:
                    side[w] = 1 - side[v]; st.append(w)
                elif side[w] == side[v]:
                    bip = False
    print('bipartite:', bip)
