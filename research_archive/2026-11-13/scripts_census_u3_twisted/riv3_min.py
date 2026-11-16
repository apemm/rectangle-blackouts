"""Smallest R_IV(3) edges (stride_transfer_ratio Theorem R4) for the mod-2^k split, k = 3, 5.
Edge (q m, p m), m odd; (al, be) odd coprime, 0 < al < 3 be, v2(3 be - al) >= k - 2."""
from math import gcd
u = 3
for k in (3, 5):
    E = []
    for be in range(1, 61, 2):
        for al in range(1, u * be, 2):
            if gcd(al, be) != 1: continue
            d = u * be - al; v = (d & -d).bit_length() - 1
            if v < k - 2: continue
            F = 4 * (al - 2 * u * be) ** 2 + be * be
            g1 = gcd(F, d); g2 = gcd(al * F, 4 * be * be * d)
            q = al * F // g1; p = (al * F + 4 * d * be * be) // g1
            assert (al * F + 4 * d * be * be) % g1 == 0 and q % 2 == 1
            E.append((p, q, al, be, g1, g2))
    E.sort()
    print('k', k, 'edges', len(E), 'least p:', E[:4], ' max g', max(e[4] for e in E))
