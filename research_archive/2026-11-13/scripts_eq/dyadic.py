"""Sanity check for the 2-adic first moment of D_T (stride 4).
D_T = { |d| : 16 d^2 + (2d+T)^2 = L^2, 0 < L < h, d != 0, |d| < n_T }.
Built from triples (2gmn, g(m^2-n^2), g(m^2+n^2)), g odd, m>n>=1 coprime, opposite parity.
Also checked by brute force for small h.
"""
import sys, math
from math import gcd, isqrt

def nT(T, h):
    A = (h + 1) // 2; K = h // 2; s = (T - 1) // 2
    lo = max(0, -s); hi = min(A - 1, K - 1 - s)
    return max(0, hi - lo + 1)

def dsets(h):
    D = {}
    r = isqrt(h) + 1
    for m in range(2, r + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            F = m * m + n * n
            if F >= h:
                break
            g = 1
            while g * F < h:
                ad = g * m * n // 2  # |d|
                B = g * (m * m - n * n)
                for sd in (1, -1):
                    d = sd * ad
                    for sb in (1, -1):
                        T = sb * B - 2 * d
                        if ad < nT(T, h):
                            D.setdefault(T, set()).add(ad)
                g += 2
    return D

def brute(h):
    D = {}
    for T in range(-(h | 1), (h | 1) + 1, 2):
        n = nT(T, h)
        for d in range(-n + 1, n):
            if d == 0:
                continue
            v = 16 * d * d + (2 * d + T) ** 2
            L = isqrt(v)
            if L * L == v and L < h:
                D.setdefault(T, set()).add(abs(d))
    return D

def v2(x):
    c = 0
    while x % 2 == 0:
        x //= 2; c += 1
    return c

if __name__ == "__main__":
    for hb in (60, 201, 500):
        a = dsets(hb); b = brute(hb)
        a = {k: v for k, v in a.items() if v}; b = {k: v for k, v in b.items() if v}
        print("brute check h=%d:" % hb, a == b)
    for h in [int(x) for x in sys.argv[1:]]:
        D = dsets(h)
        tot = sum(len(v) for v in D.values())
        lnh = math.log(h)
        print("h=%d  total distances=%d  total/(h ln h)=%.4f" % (h, tot, tot / (h * lnh)))
        for a in range(0, 8):
            Q = 2 ** a
            w = {T: sum(1 for d in v if d % Q == 0) for T, v in D.items()}
            s = sum(w.values())
            bound = math.pi * h * (lnh + 2)
            # predicted truncation law: Q^-1 * ln(sqrt h/Q)/ln(sqrt h)
            pred = (1 / Q) * max(0.0, math.log(math.sqrt(h) / Q)) / math.log(math.sqrt(h))
            print("  a=%d Q=%3d frac=%.4f  2^-a=%.4f  trunc-law=%.4f  Q*sum/(pi h(lnh+2))=%.3f  maxw=%d" % (
                a, Q, s / tot, 1 / Q, pred, Q * s / bound, max(w.values())))
