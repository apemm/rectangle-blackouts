"""Brute force for the conservation lemma.

Leaves u in Z/2^D (rho = rho0 + 32u, so d(u,u') = 5 + v2(u - u')).
Each leaf gets a kappa-class K(u) and one lambda value f(u) in Z/2^F
(lambda = kappa0 + 16 f, F = E - 4). S5 between leaves with K(u) != K(u') is
killed by congruence iff, with d = 5 + v2(u-u') and v = 4 + v2(f(u)-f(u'))
(v = infinity if equal, meaning only v >= E is known):
   strict rule:   v >= d+1 visible (v < E, v >= d+1) or (f equal and E >= d+1)
   relaxed rule:  v in {d-2, d-1} with v < E, or the strict rule.
Maximise N = #distinct (K, f).  Compare with 2^F.
"""
import itertools, sys

def v2(x, cap):
    if x == 0: return cap
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c

def ok_pair(du, df, D, F, relaxed):
    E = F + 4
    d = 5 + v2(du % (2**D), 99)
    if df % (2**F) == 0:
        return E >= d + 1
    v = 4 + v2(df % (2**F), 99)
    if v >= d + 1: return True
    if relaxed and v in (d - 2, d - 1): return True
    return False

def best(D, F, relaxed):
    L = 2**D
    # greedy-free exhaustive over f assignments; K chosen optimally:
    # given f, build conflict graph: leaves u,u' must share K if pair not ok.
    # K-classes = connected components of the 'must share' graph.
    # N = sum over components of #distinct f in component.
    bestN = 0; arg = None
    for f in itertools.product(range(2**F), repeat=L):
        if f[0] != 0: continue
        parent = list(range(L))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        for a in range(L):
            for b in range(a+1, L):
                if not ok_pair(b - a, f[b] - f[a], D, F, relaxed):
                    ra, rb = find(a), find(b)
                    if ra != rb: parent[ra] = rb
        comps = {}
        for u in range(L):
            comps.setdefault(find(u), set()).add(f[u])
        N = sum(len(s) for s in comps.values())
        if N > bestN: bestN, arg = N, f
    return bestN, arg

if __name__ == '__main__':
    for D in range(1, 5):
        for F in range(1, 4):
            if (2**F)**(2**D) > 3_000_000: continue
            for relaxed in (False, True):
                N, arg = best(D, F, relaxed)
                print(f"D={D} F={F} relaxed={relaxed}: maxN={N} vs 2^F={2**F}  f={arg}")
