"""Number theory only (no Hilbert geometry).  For odd Y <= YMAX list the legs X = 32 q
(X^2 + Y^2 = L^2) and report pairs of legs q2 < q1 of the SAME Y with q1 - q2 in {1, 2, 4}
(so they fit in one window [3d-2, 3d+2] and have distinct residues mod 3).
Also reports the smallest Y with three legs of distinct residue in one window.
Usage: py -I nt_double_legs.py YMAX
"""
import sys
import numpy as np

YMAX = int(sys.argv[1])
S = 32
spf = np.zeros(YMAX + 1, dtype=np.int64)
for p in range(2, YMAX + 1):
    if spf[p] == 0:
        spf[p::p][spf[p::p] == 0] = p


def divisors_of_square(Y):
    fac = {}
    n = Y
    while n > 1:
        p = int(spf[n]); fac[p] = fac.get(p, 0) + 1; n //= p
    ds = [1]
    for p, e in fac.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


def legs_q(Y):
    Y2 = Y * Y
    out = []
    for a in divisors_of_square(Y):
        if a < Y:
            X = (Y2 // a - a) // 2
            if X % S == 0:
                out.append(X // S)
    return sorted(out)


doubles = []
triples = []
for Y in range(3, YMAX + 1, 2):
    qs = legs_q(Y)
    st = set(qs)
    for q2 in qs:
        for k in (1, 2, 4):
            if q2 + k in st:
                doubles.append((Y, q2, q2 + k))
        # three distinct residues inside some 5-window [c, c+4] with c = 3d-2
    for c0 in set(q - i for q in qs for i in range(5)):
        if c0 % 3 != 1:
            continue
        win = [q for q in qs if c0 <= q <= c0 + 4]
        if len({q % 3 for q in win}) == 3:
            triples.append((Y, (c0 + 2) // 3, win))
print("double legs with distinct residues (Y, q2, q1):", len(doubles))
print("first 40:", doubles[:40])
print("count with 3 | Y:", sum(1 for t in doubles if t[0] % 3 == 0),
      " with 3 not dividing Y:", sum(1 for t in doubles if t[0] % 3))
print("single-Y blocked windows (Y, d, legs):", triples[:20], "total", len(triples))
