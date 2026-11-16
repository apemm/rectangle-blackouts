# Exact checks of the stride-4u identities used in the transfer table.
# Layout L***(u): label (i, j), s = j - i, T = 2s+1, slot n = u*i + M (M = p*t + b),
# odd point (4n, 2i+1), even point (4n, 2j+2).
import random
from fractions import Fraction as Fr
from math import gcd

random.seed(1)
U_LIST = [1, 3, 5, 7]

def odd(u, i, s, M):
    return (4 * (u * i + M), 2 * i + 1)

def even(u, i, s, M):
    return (4 * (u * i + M), 2 * (i + s) + 2)

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

bad = 0
for u in U_LIST:
    for _ in range(20000):
        s0, s1 = random.randint(-500, 500), random.randint(-500, 500)
        M0, M1 = random.randint(-10**6, 10**6), random.randint(-10**6, 10**6)
        i0, iQ, t1 = random.randint(0, 500), random.randint(0, 500), random.randint(-50, 50)
        T0 = 2 * s0 + 1
        Ds, DM = s1 - s0, M1 - M0
        Nu = u * Ds - DM
        # (E;O,E): V even (i0,c0), P odd (i0+t1,c0), Q even (iQ,c1)
        V, P, Q = even(u, i0, s0, M0), odd(u, i0 + t1, s0, M0), even(u, iQ, s1, M1)
        c2 = (iQ + s1) - (i0 + s0)
        lhs = dot(sub(P, V), sub(Q, V))
        rhs = 2 * (c2 * ((8 * u * u + 2) * t1 - T0) - 8 * u * t1 * Nu)
        bad += lhs != rhs
        # I.2: A odd (i0,c0), B even (i0+a,c0), C odd (iC,c1), D even (iC+b,c1)
        a, b, iC = random.randint(-30, 30), random.randint(-30, 30), random.randint(0, 500)
        A, B = odd(u, i0, s0, M0), even(u, i0 + a, s0, M0)
        C, D = odd(u, iC, s1, M1), even(u, iC + b, s1, M1)
        Uv = sub(B, A)
        two_n = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
        m = (iC + iC + b) - (i0 + i0 + a)
        n2 = m + Ds
        val = ((8 * u * u + 2) * a + T0) * n2 - 8 * u * a * (2 * Nu - u * Ds)
        bad += dot(Uv, two_n) != 2 * val
        # type II (-1,-1): A even (iA,c0), C odd (iA+d,c0), B even (iB,c1), D odd (iB+d',c1)
        iA, iB, d, dd = random.randint(0, 500), random.randint(0, 500), random.randint(-30, 30), random.randint(-30, 30)
        A, C = even(u, iA, s0, M0), odd(u, iA + d, s0, M0)
        B, D = even(u, iB, s1, M1), odd(u, iB + dd, s1, M1)
        Uv = sub(B, A)
        two_n = (C[0] + D[0] - A[0] - B[0], C[1] + D[1] - A[1] - B[1])
        Sig, S = d + dd, s0 + s1 + 1
        Dj = (iB + s1) - (iA + s0)
        bad += dot(Uv, two_n) != 4 * (Dj * ((4 * u * u + 1) * Sig - S) - 4 * u * Sig * Nu)
        # L-adic (i): V even (i0,c0), G even (iQ,c1), E = V + (a,-f): dot = 2[Dj(2ua - f) - 2a Nu]
        f = random.randint(-1000, 1000)
        G = even(u, iQ, s1, M1)
        Dj = (iQ + s1) - (i0 + s0)
        lhs = dot((a, -f), sub(G, V))
        bad += lhs != 2 * (Dj * (2 * u * a - f) - 2 * a * Nu)
    # type II algebraic identity: X^2+Y^2 - U2^2(H^2+16u^2 Sig^2) = 16u^2 Sig * [2U2(De Sig - Dd H) + Sig(16u^2 Dd^2 + De^2)]
    for _ in range(20000):
        Sig, U2, H, Dd, De = [random.randint(-10**4, 10**4) for _ in range(5)]
        X = 16 * u * u * Sig * Dd - U2 * H
        Y = 4 * u * Sig * (De + U2)
        lhs = X * X + Y * Y - U2 * U2 * (H * H + 16 * u * u * Sig * Sig)
        rhs = 16 * u * u * Sig * (2 * U2 * (De * Sig - Dd * H) + Sig * (16 * u * u * Dd * Dd + De * De))
        bad += lhs != rhs
print("geometric/algebraic identity failures:", bad)

# R_IV^(u): in-class odd-odd M2c with Delta = 4 u e; check (I1),(I2) and shallowness of z
def riv_check(u, al, be, mult=1):
    lam = Fr(2 * al, be)
    mu = (1 + lam * lam) / (4 * u - 2 * lam)
    Fu = 4 * (al - 2 * u * be) ** 2 + be * be
    ratio = Fr(4 * be * be * (u * be - al), al * Fu)  # e / nu_B
    g = gcd(al * Fu, 4 * be * be * (u * be - al))
    q, p = al * Fu // g, (al * Fu + 4 * be * be * (u * be - al)) // g
    nuB = q * mult
    e = ratio * nuB
    nuD = nuB + e
    assert nuD == p * mult
    n1, w, Delta = lam * e, mu * e, 4 * u * e
    u2 = 2 * nuB
    I1 = e * u2 == n1 * (Delta + w)
    I2 = (Delta - 2 * n1) * w == e * e + n1 * n1
    return I1 and I2, (q, p, g, e, n1, w)

bad = 0
cnt = 0
gs = {}
for u in [1, 3]:
    for be in range(1, 60, 2):
        for al in range(1, u * be, 2):
            if gcd(al, be) != 1:
                continue
            ok, (q, p, g, e, n1, w) = riv_check(u, al, be)
            bad += not ok
            cnt += 1
            gs.setdefault(u, set()).add(g)
print("R_IV^(u) parametrization checks:", cnt, "failures:", bad, "gcd values:", {k: sorted(v) for k, v in gs.items()})
print("u=1 first generator (al,be)=(1,5)?", riv_check(1, 1, 5)[1][:3])

# R_FF^(u): same-row two-filler, two-label (in-class) quadruple; side {L1,F1}, diagonal {L2,F2}
def rff_check(u, a, b, t):
    lam = Fr(2 * a, b)
    if lam == 4 * u:
        return None
    P = lam * t
    Y1 = t * (lam - 8 * u) * (lam * lam + 4) / (8 * (lam - 4 * u))
    Y2 = Y1 - 2 * t
    if P == 0:
        return None
    Qs = (Y2 * Y2 - Y1 * Y1) / P
    X1, X2 = (P + Qs) / 2, (Qs - P) / 2
    L1 = (Fr(0), Fr(0)); L2 = (Fr(4 * u * t), Fr(2 * t))
    F1 = (X1, Y1); F2 = (L2[0] + X2, L2[1] + Y2)
    n = ((L2[0] + F2[0] - L1[0] - F1[0]) / 2, (L2[1] + F2[1] - L1[1] - F1[1]) / 2)
    Uv = (F1[0] - L1[0], F1[1] - L1[1]); Vv = (F2[0] - L2[0], F2[1] - L2[1])
    ok = (dot(n, Uv) == 0) and (dot(Uv, Uv) == dot(Vv, Vv)) and (F1[1] == F2[1])
    Uu = (a - 4 * u * b) * (a * a + b * b)
    Vu = a ** 3 - 4 * u * a * a * b - 3 * a * b * b + 4 * u * b ** 3
    ratio_ok = (Y1 == 0) or (Y2 / Y1 == Fr(Vu, Uu))
    return ok and ratio_ok

bad = 0; cnt = 0
for u in [1, 3, 5]:
    for b in range(1, 25):
        for a in range(-60, 61):
            if gcd(a, b) != 1 or a == 0:
                continue
            for t in [-7, 3, 10]:
                r = rff_check(u, a, b, t)
                if r is None:
                    continue
                cnt += 1
                bad += not r
print("R_FF^(u) cubic checks:", cnt, "failures:", bad)

# content gcd(U_u, V_u) for u = 3
for u in [1, 3]:
    vals = set()
    for b in range(1, 300):
        for a in range(-1500, 1501):
            if gcd(a, b) != 1:
                continue
            Uu = (a - 4 * u * b) * (a * a + b * b)
            Vu = a ** 3 - 4 * u * a * a * b - 3 * a * b * b + 4 * u * b ** 3
            if Uu == 0:
                continue
            vals.add(gcd(Uu, Vu))
    print("u =", u, "gcd(U_u,V_u) values:", sorted(vals))
