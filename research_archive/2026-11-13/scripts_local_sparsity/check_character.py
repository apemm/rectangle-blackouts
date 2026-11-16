# Sanity check of Proposition 5 (a rotation that is nearly constant on the distances prime to p).
# T = p*t with p prime, split, p >= C h^(2/3).  For a real z0 the proof constructs theta with
#   || theta d - t z0 || <= 10.1 h / p^(3/2)   for d in S_T(h), p !| d,
#   theta * (p d') = -10 z0 d'  (mod 1).
# Here S_T(h) is enumerated from the definition through the orbits of Z[phi]; exact rationals are used.
import sys
from math import isqrt, gcd
from fractions import Fraction

SQ5 = 5 ** 0.5; PHI = (1 + SQ5) / 2

def mul(x, y):
    a, b = x; c, d = y
    return (a * c + b * d, a * d + b * c + b * d)
def conj(x): return (x[0] + x[1], -x[1])
def norm(x): return x[0] * x[0] + x[0] * x[1] - x[1] * x[1]
def tr(x): return 2 * x[0] + x[1]
def val(x): return x[0] + x[1] * PHI          # real embedding (float, only for sizes)
def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
def find_norm(n):
    out = []
    for b in range(0, 3 * isqrt(n) + 3):
        for sgn in (1, -1):
            D = 5 * b * b + 4 * sgn * n
            if D < 0: continue
            s = isqrt(D)
            if s * s == D and (s - b) % 2 == 0:
                a = (s - b) // 2
                if abs(norm((a, b))) == n: return (a, b)
    return None

def S_bruteforce_orbits(T, h, gens):
    # gens: list of elements x of norm +-T^2 (one per ideal class of norm T^2 that matters)
    phi = (0, 1); phinv = (-1, 1)
    out = set()
    for base in gens:
        for unit in (phi, phinv):
            x = base
            for _ in range(400):
                for sg in (1, -1):
                    y = (sg * x[0], sg * x[1])
                    if norm(y) == -T * T and (tr(y) - T) % 10 == 0:
                        d = (tr(y) - T) // 10
                        L2 = 20 * d * d + 4 * T * d + T * T
                        L = isqrt(L2)
                        if L * L == L2 and 0 < L < h and d != 0: out.add(d)
                x = mul(x, unit)
                if abs(x[0]) > 10 ** 60: break
    return sorted(out)

def dist1(fr):      # distance of a Fraction to the nearest integer
    f = fr - (fr.numerator // fr.denominator)
    return min(f, 1 - f)

def main():
    h = 10 ** 8
    worst = Fraction(0); worst_ratio = 0.0; tested = 0; total_d = 0
    p = 4 * 10 ** 6
    cases = []
    while tested < 25:
        p += 1
        if p % 5 not in (1, 4) or not is_prime(p): continue
        for t in (1, 11, 19, 3, 7):          # t = 11, 19 have split structure; 3, 7 are inert
            T = p * t
            if T >= h: continue
            pi = find_norm(p)
            # balance pi: 1 <= |pi/pi'| < phi^2
            for _ in range(200):
                r = abs(val(pi) / val(conj(pi)))
                if r < 1: pi = mul(pi, (0, 1))
                elif r >= PHI * PHI: pi = mul(pi, (-1, 1))
                else: break
            pic = conj(pi)
            # generators of the ideals of norm T^2 = p^2 t^2 : (pi^2 or pi'^2 or p) x (ideals of norm t^2)
            tg = [(t, 0)]
            if t in (11, 19):
                et = find_norm(t)
                tg += [mul(et, et), mul(conj(et), conj(et))]
            gens = [mul(a, b) for a in (mul(pi, pi), mul(pic, pic), (p, 0)) for b in tg]
            ds = S_bruteforce_orbits(T, h, gens)
            prim = [d for d in ds if d % p != 0]
            if not prim: continue
            eta = 10.1 * h / p ** 1.5
            # root r of x^2-x-1 mod p with pi = 0
            a, b = pi
            rr = (-a * pow(b, -1, p)) % p
            assert (rr * rr - rr - 1) % p == 0
            for z0 in (Fraction(1, 2), Fraction(1, 3), Fraction(137, 1000), Fraction(0)):
                # nearest element mu1 of O to z0*pi' (both embeddings)
                s1 = float(z0) * val(pic); s2 = float(z0) * val(pi)
                bb = round((s1 - s2) / SQ5); aa = round((s1 + s2 - bb) / 2)
                mu1 = (aa, bb)
                assert abs(val(mu1) - s1) <= 1.07 and abs(val(conj(mu1)) - s2) <= 1.07
                # integer n with mu1 = n*pi' mod the prime ideal (pi)
                img = lambda x: (x[0] + x[1] * rr) % p
                n = (img(mu1) * pow(img(pic), -1, p)) % p
                theta = 10 * (Fraction(n) - z0) / p          # theta = 10*vartheta, vartheta = (n - z0)/p
                for d in prim:
                    dev = dist1(theta * d - t * z0)
                    assert dev <= eta, (p, t, z0, d, float(dev), eta)
                    if dev > worst: worst = dev
                    worst_ratio = max(worst_ratio, float(dev) / eta)
                for dp in (1, 2, 3, 20, 52, 357):
                    assert dist1(theta * p * dp + 10 * z0 * dp) == 0
            tested += 1; total_d += len(prim)
            cases.append((p, t, len(ds), len(prim)))
    print(f"h={h}: {tested} offsets T = p*t tested, {total_d} distances prime to p; all deviations within "
          f"10.1 h/p^1.5; largest deviation {float(worst):.4f}, largest deviation/bound {worst_ratio:.3f}")
    print("  first cases (p, t, |S_T|, #prime to p):", cases[:6])

main()
