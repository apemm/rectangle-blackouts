"""Census of family (d): cross-block V3 between two SLF-Pc triples
(V odd label, E shallow, G hole filler) with the same odd row.
Shape = (u, hole row, gamma1, gamma2); realized at prime p iff
phi(g1) - phi(g2) = 4 p dm, dm != 0, with phi(g) = 4g + u*g_/(2g).
Definition-level: also re-checks the right angle at V and W's row/column.
"""
import sys
from sympy import primerange

def divisors_signed(n):
    n = abs(n); ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds += [i, -i]
            if i * i != n:
                ds += [n // i, -(n // i)]
        i += 1
    return ds

def census(h, yP_res, Tmod4, r0=1, mod_s=8):
    # T* = largest y <= h with y = yP + 32 (T=3 mod 4) or yP + 48 (T=1) mod 64
    off = 32 if Tmod4 == 3 else 48
    Ts = max(y for y in range(h - 70, h + 1) if (y - yP_res - off) % 64 == 0)
    holes = [Ts - 24, Ts - 8]
    primes = [p for p in primerange(20 * h + 1, 40 * h + 1) if p % 20 in (3, 7)]
    pset = set(primes)
    shapes = []  # (u, yG, g1, g2, diff)
    ntrip = 0
    for yV in range(yP_res % 64, Ts - 128, 64):
        if yV <= 177:
            continue
        u = (yV - r0) // 2
        for yG in holes:
            g = yG - yV
            o = 0 if yG == Ts - 24 else 2
            gam = []
            for d in divisors_signed(u * g // 2):
                # need 2*a*gamma = u*g, a integer, gamma = o mod 4, a != 0 mod 4
                if (u * g) % (2 * d):
                    continue
                a = u * g // (2 * d)
                if d % 4 != o or a % 4 == 0:
                    continue
                # definition check: E = V + (a, -(yV - r0)), G = V + (4d, g)
                assert a * 4 * d - (yV - r0) * g == 0
                gam.append((d, a))
            ntrip += len(gam)
            for i in range(len(gam)):
                for j in range(len(gam)):
                    if i == j:
                        continue
                    (d1, a1), (d2, a2) = gam[i], gam[j]
                    diff = (4 * d1 + a1) - (4 * d2 + a2)
                    assert diff != 0
                    if diff % (4 * mod_s) or abs(diff) > h * h // 2:
                        continue
                    shapes.append((u, yG, d1, d2, diff))
    real = {}
    for s in shapes:
        q = abs(s[4]) // 4
        for p in pset:
            if q % p == 0:
                real.setdefault(p, []).append(s)
    return ntrip, len(shapes), len(primes), real

if __name__ == "__main__":
    for h in [int(x) for x in sys.argv[1:]]:
        tot_tr = tot_sh = 0; realized = 0; nprim = 0
        for yP in range(1, 64, 2):
            if yP % 4 != 3:
                continue
            for Tm in (1, 3):
                nt, ns, npr, real = census(h, yP, Tm)
                tot_tr += nt; tot_sh += ns; nprim = npr
                realized += sum(len(v) for v in real.values())
        print(f"h={h}: SLF-Pc triple shapes {tot_tr}, ordered shape pairs (2-adic ok, span ok) {tot_sh}, "
              f"#primes {nprim}, realized (pair,p) total {realized}, mean per p {realized/max(nprim,1):.3f}")
