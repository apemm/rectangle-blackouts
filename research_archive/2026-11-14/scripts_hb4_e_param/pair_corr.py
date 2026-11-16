"""Sanity check: pair correlation of Pythagorean legs at equal Y (pairing) vs shifted Y.

For S = 2^s, enumerate all (q, Y) with Y odd, (Sq)^2 + Y^2 = L^2, L < h, via T1:
q = k e' O, Y = k|E^2 - O^2|, L = k(E^2 + O^2), E = S e'/2, k,O odd, gcd(e',O)=1.
P(tau; D1, D2) = #{(Y, q, q'): Y in A_q, Y + 2 tau in A_q', D1 <= |q - q'| <= D2}.
kappa = P(0) / mean_{tau != 0} P(tau).
"""
import sys, math
from bisect import bisect_left, bisect_right
from collections import defaultdict

def vectors(S, h):
    out = []
    Emin = S // 2
    k = 1
    while k * (Emin * Emin + 1) < h:
        e = 1
        while k * ((S * e // 2) ** 2 + 1) < h:
            E = S * e // 2
            O = 1
            while k * (E * E + O * O) < h:
                if math.gcd(e, O) == 1:
                    out.append((k * e * O, k * abs(E * E - O * O)))
                O += 2
            e += 1
        k += 2
    return out

def main(S, h, bands, taus):
    V = vectors(S, h)
    byY = defaultdict(list)
    for q, Y in V:
        byY[Y].append(q)
    for Y in byY:
        byY[Y].sort()
    print(f"S={S} h={h} vectors={len(V)} distinct Y={len(byY)}")
    for (D1, D2) in bands:
        res = {}
        for tau in taus:
            tot = 0
            for Y, qs in byY.items():
                qs2 = byY.get(Y + 2 * tau)
                if not qs2:
                    continue
                for q in qs:
                    # q' in [q-D2, q-D1] u [q+D1, q+D2]
                    tot += bisect_right(qs2, q + D2) - bisect_left(qs2, q + D1)
                    tot += bisect_right(qs2, q - D1) - bisect_left(qs2, q - D2)
            res[tau] = tot
        base = [res[t] for t in taus if t != 0]
        mean = sum(base) / len(base)
        print(f" band |dq| in [{D1},{D2}]: P(0)={res[0]}  mean P(tau!=0)={mean:.1f}  kappa={res[0]/mean if mean else float('nan'):.3f}  min/max shift={min(base)}/{max(base)}")

if __name__ == "__main__":
    S = int(sys.argv[1]); h = int(sys.argv[2])
    bands = [(1, 4), (1, 16), (17, 256), (257, 10**9)]
    taus = [0] + list(range(1, 25)) + list(range(-24, 0))
    main(S, h, bands, taus)
