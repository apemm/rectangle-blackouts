"""Model mean candidate degree mu = 16 W / h^2 at large h via the Euclid normal form.

W = sum over P vectors (k odd, e'>=1, O odd, gcd(e',O)=1, L = k*l < h,
l = S^2 e'^2/4 + O^2) of sigma * (h - L), with sigma = 2 slots per gap q
(the M >= 2 value away from multiples of M).  Also V = number of vectors.
"""
import math, sys, time
import numpy as np

def W_and_V(S, h):
    W = 0.0
    V = 0
    E2 = (S * S) // 4
    ep = 1
    while E2 * ep * ep + 1 < h:
        omax = math.isqrt(h - 1 - E2 * ep * ep)
        O = np.arange(1, omax + 1, 2, dtype=np.int64)
        O = O[np.gcd(O, ep) == 1]
        l = E2 * ep * ep + O * O
        l = l[l < h]
        kmax = (h - 1) // l
        n = (kmax + 1) // 2
        V += int(n.sum())
        W += float((n * h - l * n * n).astype(np.float64).sum())
        ep += 1
    return 2.0 * W, V

if __name__ == "__main__":
    t0 = time.time()
    for S in (32, 64, 128):
        for e in range(11, 31, 2):
            h = 1 << e
            if S * S // 4 + 1 >= h:
                continue
            W, V = W_and_V(S, h)
            mu = 16.0 * W / h / h
            K = 4 * h / S / S
            asym = 16.0 / (math.pi * S) * math.log(K)
            print(f"S={S} h=2^{e} V={V} V*S/h={V*S/h:.3f} mu={mu:.4f} "
                  f"16logK/(piS)={asym:.4f} diff*S={(mu-asym)*S:.3f}")
            sys.stdout.flush()
            if time.time() - t0 > 50:
                sys.exit(0)
