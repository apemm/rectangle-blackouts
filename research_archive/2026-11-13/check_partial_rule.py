"""Brute-force test of the partial power-of-two rule.

Labels (i, j), 0 <= i < A, 0 <= j < K, odd point (4n, 2i+1), even point (4n, 2j+2).
Placement: distinct integers n(i, j) with n - j = 0 mod 2^r, otherwise random.
For every right angle with an even vertex V it tests
  (E;O,E): a = n_P - n_V, b = row(P) - row(V), e = j_Q - j_V.
           Either the angle is axis-aligned, or 2^(r+3) |a| / gcd(a, b) divides-bounds |e|:
           |e| >= 2^(r+3) |a| / gcd(a, b)  and  2^(r+3) | e.
  (E;E,E): some leg has |e_k| >= 2^(r+1).
Usage: py check_partial_rule.py h trials
"""
import sys, random
from math import gcd

def run(h, r, rng):
    A, K = (h + 1) // 2, h // 2
    mod = 1 << r
    used = set()
    pos = {}
    span = max((3 * A * K) // 2, 2 * A * mod)
    for i in range(A):
        for j in range(K):
            while True:
                n = rng.randrange(0, span)
                n -= (n - j) % mod
                if n >= 0 and n not in used:
                    used.add(n); pos[(i, j)] = n; break
    labels = list(pos.items())
    eoe = eee = bad = 0
    for (i0, j0), n0 in labels:
        # even vertex V = (n0, 2 j0 + 2)
        for (i1, j1), n1 in labels:
            a = n1 - n0
            b = (2 * i1 + 1) - (2 * j0 + 2)
            if a == 0:
                continue
            g = gcd(abs(a), abs(b))
            for (i2, j2), n2 in labels:
                if n2 == n0:
                    continue
                f = n2 - n0
                e = j2 - j0
                # (E;O,E): P odd point of label 1, Q even point of label 2
                if 16 * a * f + 2 * b * e == 0 and e != 0:
                    eoe += 1
                    if abs(e) * g < (1 << (r + 3)) * abs(a) or e % (1 << (r + 3)):
                        bad += 1
                # (E;E,E): P even point of label 1, Q even point of label 2
                if n1 < n2:
                    e1 = j1 - j0
                    if 16 * a * f + 4 * e1 * e == 0:
                        eee += 1
                        if max(abs(e1), abs(e)) < (1 << (r + 1)):
                            bad += 1
    return eoe, eee, bad

if __name__ == "__main__":
    h = int(sys.argv[1]); trials = int(sys.argv[2])
    rng = random.Random(1)
    for r in range(0, 6):
        tot = [0, 0, 0]
        for _ in range(trials):
            res = run(h, r, rng)
            for k in range(3):
                tot[k] += res[k]
        print("h=%d r=%d  (E;O,E) angles=%d  (E;E,E) angles=%d  violations=%d" % (h, r, *tot))
