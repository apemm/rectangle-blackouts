"""Exact sparse checks of the translation-atom (type A) and diagonal-atom (type B)
factor-one P conflicts for choice rules x_e = S(M r_e + xi_e).

Hilbert order copied from the archive convention (quadrant maps
0:(y,x) 1:(x,y+q) 2:(x+q,y+q) 3:(2q-1-y,q-1-x)); nothing imported from the archive.
"""
import math
import sys

sys.setrecursionlimit(10000)


def point(n, r):
    x = y = 0
    s = 1
    # iterative version of the archive recursion, bottom-up
    digs = []
    m = n
    while m > 1:
        digs.append(r % 4)
        r //= 4
        m //= 2
    assert r == 0
    for d in digs:  # lowest level first; s = side of current sub-square
        q = s
        if d == 0:
            x, y = y, x
        elif d == 1:
            x, y = x, y + q
        elif d == 2:
            x, y = x + q, y + q
        else:
            x, y = 2 * q - 1 - y, q - 1 - x
        s *= 2
    return x, y


def rank(n, x, y):
    r = 0
    while n > 1:
        q = n // 2
        if x < q and y < q:
            r += 0
            x, y = y, x
        elif x < q:
            r += q * q
            y -= q
        elif y >= q:
            r += 2 * q * q
            x -= q
            y -= q
        else:
            r += 3 * q * q
            x, y = q - 1 - y, 2 * q - 1 - x
        n = q
    return r


# Klein orientation model: (s, n) bits; L_0 = swap, L_1 = L_2 = id, L_3 = -swap
LMAP = {0: (1, 0), 1: (0, 0), 2: (0, 0), 3: (1, 1)}
COFF = {0: (0, 0), 1: (0, 1), 2: (1, 1), 3: (1, 0)}


def comp(o, d):
    a = LMAP[d]
    return (o[0] ^ a[0], o[1] ^ a[1])


def off(o, c):
    x, y = c
    if o[0]:
        x, y = y, x
    if o[1]:
        x, y = 1 - x, 1 - y
    return x, y


def sigma(o):
    return 1 if (o[0] ^ o[1]) == 0 else -1


def tau(o, d):
    x, y = off(o, COFF[d])
    return y - x


def v2(z):
    return (z & -z).bit_length() - 1


def digits_to_rank(dig):
    return sum(d * 4 ** l for l, d in enumerate(dig))


def place_top(dig, o, n, l, want):
    """choose digit in {0,2} at level l whose offset is `want`."""
    for d in (0, 2):
        if off(o, COFF[d]) == want:
            dig[l] = d
            return comp(o, d)
    raise AssertionError


def build_A(S, M, K, lam_lo, lam_hi, n):
    """Type A atom: e has digit 1 on K, digit 2 on [lam_lo, lam_hi] \\ K; f has 2 on K."""
    K = sorted(K)
    assert K and lam_lo >= 1 and lam_lo <= K[0] and K[-1] <= lam_hi
    D = sum(4 ** k for k in K)
    assert (S * S * M * M * D * D) % 8 == 0
    N0 = S * S * M * M * D * D // 8
    assert v2(N0) >= lam_hi + 2, "N0 low bits overlap region"
    assert N0 < 2 ** (n - 4), "height too small"
    dig = [None] * n
    o = (0, 0)
    for l in range(n - 1, -1, -1):
        if l == n - 1:
            o = place_top(dig, o, n, l, (0, 0))
        elif l == n - 2:
            o = place_top(dig, o, n, l, (1, 1))
        elif l == n - 3:
            o = place_top(dig, o, n, l, (0, 0))
        elif l == lam_hi + 1:
            for d in (0, 2):
                if comp(o, d) in ((1, 0), (1, 1)):
                    dig[l] = d
            o = comp(o, dig[l])
        elif lam_lo <= l <= lam_hi:
            dig[l] = 1 if l in K else 2
            o = comp(o, dig[l])
        elif l == 0:
            dig[l] = 1 if sigma(o) == -1 else 3
            o = comp(o, dig[l])
        else:
            bit = (N0 >> l) & 1
            if bit:
                dig[l] = 1 if sigma(o) == 1 else 3
            else:
                dig[l] = 2
            o = comp(o, dig[l])
    digf = list(dig)
    for k in K:
        digf[k] = 2
    return dig, digf, D, N0


def build_B(S, M, kb, kt, n):
    """Type B atom: e has digit 0 on [kb,kt] (even length), f has 2 there."""
    assert (kt - kb + 1) % 2 == 0 and kb >= 1
    K = list(range(kb, kt + 1))
    D = 2 * sum(4 ** k for k in K)
    Dp = 2 ** (kt + 1) - 2 ** kb
    assert (S * S * M * M * D * D) % 8 == 0
    N0 = S * S * M * M * D * D // 8
    assert v2(N0) >= kt + 2
    assert N0 < 2 ** (n - 4)
    # target T_e = N0 - 1 - Dp = (N0 - 2^(kt+1)) + (2^kb - 1)
    dig = [None] * n
    o = (0, 0)
    for l in range(n - 1, -1, -1):
        if l == n - 1:
            o = place_top(dig, o, n, l, (0, 0))
        elif l == n - 2:
            o = place_top(dig, o, n, l, (1, 1))
        elif l == n - 3:
            o = place_top(dig, o, n, l, (0, 0))
        elif kb <= l <= kt:
            dig[l] = 0
            o = comp(o, 0)
        elif l < kb:
            want = 1
            dig[l] = 1 if sigma(o) == want else 3
            o = comp(o, dig[l])
        elif l == kt + 1:
            want = -1  # -2^(kt+1); N0 bit there is 0
            dig[l] = 1 if sigma(o) == want else 3
            o = comp(o, dig[l])
        else:
            bit = (N0 >> l) & 1
            dig[l] = (1 if sigma(o) == 1 else 3) if bit else 2
            o = comp(o, dig[l])
    digf = list(dig)
    for k in K:
        digf[k] = 2
    return dig, digf, D, N0


def check_conflict(S, M, dig, digf, xi_e, xi_f, n, h):
    """Verify an actual in-strip factor-one P conflict between e and f for the given choices."""
    Q = 2 ** n
    re, rf = digits_to_rank(dig), digits_to_rank(digf)
    e, f = point(Q, re), point(Q, rf)
    assert rank(Q, *e) == re and rank(Q, *f) == rf
    A, Kc = (h + 1) // 2, h // 2
    assert Q // 2 < max(A, Kc) <= Q
    for lab in (e, f):
        assert lab[0] < A and lab[1] < Kc
    xe, xf = S * (M * re + xi_e), S * (M * rf + xi_f)
    X = xf - xe
    out = []
    for (pa, pb) in (((xe, 2 * e[0] + 1), (xf, 2 * f[1] + 2)), ((xe, 2 * e[1] + 2), (xf, 2 * f[0] + 1))):
        y = pb[1] - pa[1]
        L2 = X * X + y * y
        L = math.isqrt(L2)
        if L * L != L2:
            continue
        s = pa[1] + pb[1]
        if (s - L) % 2:
            continue
        lo, hi = (s - L) // 2, (s + L) // 2
        if not (1 <= lo < hi <= h):
            continue
        xm2 = xe + xf
        assert xm2 % 2 == 0
        xm = xm2 // 2
        odd, even = (lo, hi) if lo % 2 else (hi, lo)
        g = ((odd - 1) // 2, (even - 2) // 2)
        assert 0 <= g[0] < A and 0 <= g[1] < Kc, "owner not a label"
        rg = rank(Q, *g)
        # owner column differs from midpoint column for every choice xi_g in [0, M)
        assert all(S * (M * rg + c) != xm for c in range(M))
        P, Z = (xm, lo), (xm, hi)
        tilted = {pa, pb, P, Z}
        assert len(tilted) == 4
        # rectangle: diagonals pa-pb and P-Z share midpoint and length
        assert pa[0] + pb[0] == P[0] + Z[0] and pa[1] + pb[1] == P[1] + Z[1]
        assert (pb[0] - pa[0]) ** 2 + (pb[1] - pa[1]) ** 2 == (Z[1] - P[1]) ** 2
        a_fac = (L - abs(y)) // 2
        out.append({"y": y, "X": X, "L": L, "rows": (lo, hi), "owner": g, "factor": a_fac})
    return {"re": re, "rf": rf, "e": e, "f": f, "witness": out}


if __name__ == "__main__":
    S, M = 32, 3
    # type A: K = {1}
    for (K, lo, hi) in [([1], 1, 1), ([2], 2, 5), ([2, 3, 5], 2, 5), ([3, 4], 3, 9)]:
        D = sum(4 ** k for k in K)
        N0 = S * S * M * M * D * D // 8
        n = N0.bit_length() + 5
        for extra in (0, 3):
            nn = n + extra
            h = 2 ** (nn + 1)
            dig, digf, D, N0 = build_A(S, M, K, lo, hi, nn)
            res = check_conflict(S, M, dig, digf, 0, 0, nn, h)
            e, f = res["e"], res["f"]
            print("A", K, "n", nn, "D", D, "e", e, "f", f, "di,dj", f[0] - e[0], f[1] - e[1],
                  "witness", [(w["factor"], w["y"]) for w in res["witness"]])
            assert res["witness"] and all(w["factor"] == 1 for w in res["witness"])
            # also a non-power-of-two height with the same padded side
            h2 = 2 ** (nn + 1) - 7
            res2 = check_conflict(S, M, dig, digf, 1, 1, nn, h2)
            assert res2["witness"]
    for (kb, kt) in [(1, 2), (2, 3), (2, 5), (3, 6)]:
        D = 2 * sum(4 ** k for k in range(kb, kt + 1))
        N0 = S * S * M * M * D * D // 8
        n = N0.bit_length() + 5
        dig, digf, D, N0 = build_B(S, M, kb, kt, n)
        h = 2 ** (n + 1)
        res = check_conflict(S, M, dig, digf, 2, 2, n, h)
        e, f = res["e"], res["f"]
        Te, Tf = e[1] - e[0], f[1] - f[0]
        print("B", (kb, kt), "n", n, "e", e, "f", f, "T", Te, Tf, "witness",
              [(w["factor"], w["y"]) for w in res["witness"]])
        assert Te == Tf and res["witness"]
    print("ALL PASS")
