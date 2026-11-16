"""Brute-force check of the (E;O,E) cross-block parametrization.

Stride 4. Class c: offset s_c (j = i + s_c), slots S_c subset of valid i,
block position M_c (columns 4(i + M_c)). Odd point (4(i+M_c), 2i+1), even point
(4(i+M_c), 2(i+s_c)+2).

Brute force: every right angle with vertex V = even point of class c0,
end P = odd point of class c0 (P != V's own odd point), end Q = even point
of a class c' != c0. Compare with the parametrization:
  g = gcd(t1, T0), t' = t1/g, T' = T0/g, b = 10t' - T',
  N = n(c') - n(c0), n(c) = s_c - M_c, q = N / b integer, c2 = 8 q t'.
Usage: py check_param.py h P nclasses seed
"""
import sys, random
from math import gcd

def main():
    h = int(sys.argv[1]); P = int(sys.argv[2]); nc = int(sys.argv[3]); seed = int(sys.argv[4])
    rnd = random.Random(seed)
    A = (h + 1) // 2; K = h // 2
    classes = []
    for c in range(nc):
        s = rnd.randint(-(A - 1), K - 1)
        slots = [i for i in range(A) if 0 <= i + s < K and rnd.random() < 0.7]
        classes.append((s, slots, P * c))
    # even points of other classes, by class
    found = set()
    for c0, (s0, sl0, M0) in enumerate(classes):
        T0 = 2 * s0 + 1
        set0 = set(sl0)
        for c1, (s1, sl1, M1) in enumerate(classes):
            if c1 == c0:
                continue
            for i0 in sl0:
                Vx, Vy = 4 * (i0 + M0), 2 * (i0 + s0) + 2
                for iq in sl1:
                    Qx, Qy = 4 * (iq + M1), 2 * (iq + s1) + 2
                    X, Y = Qx - Vx, Qy - Vy
                    for ip in sl0:
                        if ip == i0:
                            continue
                        Px, Py = 4 * (ip + M0), 2 * ip + 1
                        if (Px - Vx) * X + (Py - Vy) * Y == 0:
                            found.add((c0, i0, ip - i0, c1, iq))
    # parametrization
    pred = set()
    for c0, (s0, sl0, M0) in enumerate(classes):
        T0 = 2 * s0 + 1
        set0 = set(sl0)
        for c1, (s1, sl1, M1) in enumerate(classes):
            if c1 == c0:
                continue
            set1 = set(sl1)
            N = (s1 - M1) - (s0 - M0)
            for i0 in sl0:
                for t1 in range(-A, A):
                    if t1 == 0 or (i0 + t1) not in set0:
                        continue
                    g = gcd(abs(t1), abs(T0)); tp = t1 // g; Tp = T0 // g
                    b = 10 * tp - Tp
                    if N % b:
                        continue
                    q = N // b
                    c2 = 8 * q * tp
                    u = c2 - (s1 - s0)
                    if (i0 + u) in set1:
                        pred.add((c0, i0, t1, c1, i0 + u))
    print("h", h, "P", P, "classes", nc, "brute", len(found), "param", len(pred),
          "equal", found == pred)
    # check bound |T'| >= (8(P-h+2)/(K-1) - 10)|t'| and Delta s != 0 on found configs
    bad = 0; mins = None
    for (c0, i0, t1, c1, iq) in found:
        s0 = classes[c0][0]; s1 = classes[c1][0]; T0 = 2 * s0 + 1
        g = gcd(abs(t1), abs(T0)); tp = t1 // g; Tp = T0 // g
        ratio = abs(Tp) / abs(tp)
        mins = ratio if mins is None else min(mins, ratio)
        if s1 == s0 and P > 20 * h:
            bad += 1
    print("min |T'|/|t'| over found:", mins, " bound:", 8 * (P - h + 2) / (K - 1) - 10,
          " same-diagonal hits with P>20h:", bad)

main()
