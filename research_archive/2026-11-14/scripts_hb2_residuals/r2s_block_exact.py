"""Exact R2s candidate count for a whole aligned block at h = 40000,
sigma = 1, using the complete row census of r2s_rows.py: only three odd
rows carry Hilbert-feasible arithmetic solutions (all of the c-family,
s = F); the even role carries none. For every label of those rows and
each M, count the partners f at the two slot ranks with the right
i-displacement. Also verifies the c-family form of each solution:
delta = -c U^2, V = U w, m = (1 - w^2 - c^2 U^2)/(2c),
X = -U((w+1)^2 + c^2 U^2 - 4)/4.
"""
import math
h = 40000; S = 6272; lo = 10000; hi = h - lo
F = 2015
sols = [(13513, -196, -14, -2114, 13), (13513, -196, 14, 2114, -13),
        (19225, -196, 14, -2590, -19), (19225, -196, -14, 2590, 19),
        (24041, -392, 7, -4137, -98), (24041, -392, -7, 4137, 98)]
a0 = lo + (17 - lo) % 28; b0 = lo + (8 - lo) % 28
A = len(range(a0, hi, 28)); K = len(range(b0, hi, 28))
Q = 1
while Q < max(A, K): Q *= 2
def xy2d(n, x, y):
    d = 0; s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0; ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        s //= 2
    return d
def d2xy(n, d):
    x = y = 0; s = 1; t = d
    while s < n:
        rx = 1 & (t // 2); ry = 1 & (t ^ rx)
        if ry == 0:
            if rx == 1: x = s - 1 - x; y = s - 1 - y
            x, y = y, x
        x += s * rx; y += s * ry
        t //= 4; s *= 2
    return x, y
for (y, delta, U, V, q) in sols:
    m = F - y; c = -delta // (U * U); w = V // U
    assert delta == -c * U * U and V == U * w
    assert 2 * c * m == 1 - w * w - c * c * U * U
    assert q * S == -U * ((w + 1) ** 2 + c * c * U * U - 4) // 4
print('all six solutions are c-family members')
for M in (1, 2, 3, 4):
    tot = 0; labs = 0
    for (y, delta, U, V, q) in sols:
        i = (y - a0) // 28; Dl = delta // 28
        for j in range(K):
            re = xy2d(Q, i, j); labs += 1
            sg = 1 if q > 0 else -1; aq = abs(q)
            for d in {aq // M, -(-aq // M)}:
                if d < 1 or abs(aq - M * d) > M - 1: continue
                rf = re + sg * d
                if not (0 <= rf < Q * Q): continue
                fi, fj = d2xy(Q, rf)
                if fi < A and fj < K and fi - i == Dl: tot += 1
    print('M', M, 'R2s candidates in the whole block (odd role, side owner):', tot,
          'labels in block', A * K, 'per label', round(tot / (A * K), 6),
          'per label of the 3 special rows', round(tot / (3 * K), 4))
