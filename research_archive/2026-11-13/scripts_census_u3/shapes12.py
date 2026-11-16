"""Homogeneous two-label two-filler quadruples (side {L1,F1}, diagonal {L2,F2}, F1, F2 in one row Y)
inside a class of stride s: L2 - L1 = (s t, 2t).  Unknowns: a = x(F1) - x(L1), c = x(F2) - x(L2) - ... (see notes),
delta = a - c.  Derived equations (my derivation, checked against additive_class_split Lemma 1 at s = 4):
   a = (delta^2 + 4 t^2) / (4 (delta - s t)),   Y1 = a (delta - 2 s t) / (2 t),   Y2 = Y1 - 2t,
   n = ((2 s t - delta)/2, t).
Constraints used: t = 0 mod 32, t != 0; a integer, a = 0 mod 4 (F1 in a deep column); delta = 0 mod 16
(F1, F2 same filler offset); 1 <= Y1, Y2 <= H; for t > 0 also t <= 210 (row of q = Y + t <= h).
Each solution is also re-checked against the definition (Lemma mixedeq equations) with explicit points.
usage: py shapes12.py s H"""
import sys
from fractions import Fraction
s = int(sys.argv[1]); H = int(sys.argv[2])
sols = []
for t in range(-H // 2 // 32 * 32, H // 2 + 1, 32):
    if t == 0:
        continue
    if t > 210:
        continue
    R = 40 * H * s
    for delta in range(-R - (-R % 16), R + 1, 16):
        den = 4 * (delta - s * t)
        if den == 0:
            continue
        num = delta * delta + 4 * t * t
        if num % den:
            continue
        a = num // den
        if a % 4:
            continue
        y1n = a * (delta - 2 * s * t)
        if y1n % (2 * t):
            continue
        Y1 = y1n // (2 * t); Y2 = Y1 - 2 * t
        if not (1 <= Y1 <= H and 1 <= Y2 <= H):
            continue
        c = a - delta
        # explicit check: L1 = (0, 0), F1 = (a, Y1), L2 = (s t, 2t), F2 = (s t + c, Y1)
        A = (0, 0); B = (a, Y1); C = (s * t, 2 * t); D = (s * t + c, Y1)
        u = (B[0] - A[0], B[1] - A[1]); w = (D[0] - C[0], D[1] - C[1])
        n2 = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
        ok = (u[0] ** 2 + u[1] ** 2 == w[0] ** 2 + w[1] ** 2 and n2[0] % 2 == 0 and n2[1] % 2 == 0
              and n2[0] * u[0] + n2[1] * u[1] == 0 and n2 != (0, 0) and w != u and w != (-u[0], -u[1]) and u[0] != 0)
        sols.append((t, delta, a, c, Y1, Y2, ok))
print('s', s, 'H', H, 'solutions', len(sols), 'all pass definition check', all(x[-1] for x in sols))
for x in sorted(sols, key=lambda x: (x[4], x[0]))[:40]:
    t, delta, a, c, Y1, Y2, ok = x
    print('  t %5d delta %7d a %7d c %7d Y1 %5d Y2 %5d parity %s offset(a/4 mod 4) %d' % (
        t, delta, a, c, Y1, Y2, 'Fo' if Y1 % 2 == 0 else 'Fe', (a // 4) % 4))
