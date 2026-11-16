"""Count fatal (E;O,E) cross-block configurations with the verified parametrization.

One full class per diagonal (all slots occupied), stride 4, M_c multiple of a prime p > 20h.
Layouts:
  random : diagonals in random order at M = p*k
  rule r : M = unique solution of M = 0 mod p, M = s - kappa mod 2^r in [0, p 2^r)
           (one period; one class per diagonal; requires 2^r >= number of residues used)
A configuration (c0, i0, t1, c') is counted when V, P, Q exist and the slot of R
(iQ + t1 in c') is occupied, and R's row 2(i0+t1+c2)+1 is in [1, h].
Usage: py count_fatal.py h layout [r] [seed]
"""
import sys, random
from math import gcd, log

def nextprime(n):
    def isp(m):
        if m < 2: return False
        i = 2
        while i * i <= m:
            if m % i == 0: return False
            i += 1
        return True
    while not isp(n): n += 1
    return n

def slots(s, A, K):
    lo = max(0, -s); hi = min(A, K - s)  # i in [lo, hi)
    return lo, hi

def main():
    h = int(sys.argv[1]); layout = sys.argv[2]
    r = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    A = (h + 1) // 2; K = h // 2
    p = nextprime(20 * h + 1)
    diags = list(range(-(A - 1), K))
    if layout == "random":
        rnd = random.Random(seed); rnd.shuffle(diags)
        pos = {s: p * k for k, s in enumerate(diags)}
    else:
        mod = 2 ** r
        pos = {}
        for s in diags:
            # M = p*k, p*k = s mod 2^r
            k = ((s % mod) * pow(p, -1, mod)) % mod
            # several diagonals share a residue when 2^r < #diagonals: stack periods
            while p * k in pos.values():
                k += mod
            pos[s] = p * k
    order = sorted(diags, key=lambda s: pos[s])
    width_M = max(pos.values()) + A
    total = 0; pairs = set(); same_diag = 0
    reach = (K - 1) * (h + 9) // 8 + h
    for a, s0 in enumerate(order):
        T0 = 2 * s0 + 1
        if abs(T0) < 294: continue
        lo0, hi0 = slots(s0, A, K)
        nb = []
        for bidx in range(a - 1, -1, -1):
            if pos[s0] - pos[order[bidx]] > reach + h: break
            nb.append(order[bidx])
        for bidx in range(a + 1, len(order)):
            if pos[order[bidx]] - pos[s0] > reach + h: break
            nb.append(order[bidx])
        for s1 in nb:
            if s1 == s0: continue
            N = (s1 - pos[s1]) - (s0 - pos[s0])
            if abs(N) > reach: continue
            lo1, hi1 = slots(s1, A, K)
            tmax = abs(T0) // 294 + 1
            for t1 in range(-tmax, tmax + 1):
                if t1 == 0: continue
                g = gcd(abs(t1), abs(T0)); tp = t1 // g; Tp = T0 // g
                b = 10 * tp - Tp
                if N % b: continue
                q = N // b; c2 = 8 * q * tp
                if abs(c2) >= K: continue
                u = c2 - (s1 - s0)
                # i0 with i0, i0+t1 in [lo0,hi0); i0+u, i0+u+t1 in [lo1,hi1); R row ok
                L = max(lo0, lo0 - t1, lo1 - u, lo1 - u - t1, -(t1 + c2))
                H = min(hi0, hi0 - t1, hi1 - u, hi1 - u - t1, A - t1 - c2)
                if H > L:
                    total += H - L; pairs.add((s0, s1))
    print("h", h, "p", p, "layout", layout, "r", r, "width/h^2 (columns)",
          round(4 * width_M / h ** 2, 2), "fatal configs", total, "bad class pairs", len(pairs))

main()
