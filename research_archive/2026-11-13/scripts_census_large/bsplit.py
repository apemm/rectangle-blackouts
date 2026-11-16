"""(B8) Bad_split and (B7) R-e by definition, inside one final subclass (all its labels, before R-a..R-c,
as the priority rule puts rule 2 before rule 3).
 - R_FF^+: every pair with 0 < |i - i'| <= 210: the shallow end (larger i) goes to Theorem D.
 - R_IV: odd-odd pairs whose u-values (u = (2i+1-r0)/2) are (q m, p m), m odd, lambda = (al, be) odd coprime,
   0 < al < be (sea_census_rigid B4). max(p, q) > h^(1/2)/32 always here, so R-e: both labels to WP.
 - R_FF^oo / R_FF^ee: in each filler row Y_o, depths Y1 = Y_o - y(L1), Y2 = Y_o - y(L2) > 0 with
   (Y1, Y2) = mu (|U'|, |V'|), U V > 0 (additive_class_split Lemma 1). |U'| <= h^(1/2)/32: the L1 end to
   Theorem D; otherwise R-e: both labels to WP."""
from math import gcd, isqrt


def U_(a, b): return (a - 4 * b) * (a * a + b * b)
def V_(a, b): return a ** 3 - 4 * a * a * b - 3 * a * b * b + 4 * b ** 3

_SH = {}
def shapes(h):
    if h not in _SH:
        S = set(); R = isqrt(40 * h) + 1
        for b in range(1, R + 1):
            for a in range(-R, R + 1):
                if a * a + b * b > 40 * h or gcd(abs(a), b) != 1:
                    continue
                U = U_(a, b); V = V_(a, b)
                if U == 0 or U * V <= 0:
                    continue
                g = gcd(abs(U), abs(V)); Up, Vp = abs(U) // g, abs(V) // g
                if Up <= h and Vp <= h:
                    S.add((Up, Vp))
        _SH[h] = S
    return _SH[h]

_RIV = {}
def riv(h):
    if h not in _RIV:
        E = []
        for be in range(3, 400, 2):
            for al in range(1, be, 2):
                if gcd(al, be) != 1: continue
                F = 4 * (al - 2 * be) ** 2 + be ** 2; g = gcd(F, be - al)
                q = al * F // g; p = (al * F + 4 * (be - al) * be * be) // g
                if q <= h: E.append((q, p))
        _RIV[h] = E
    return _RIV[h]


def graph_reloc(h, tp, labs):
    """labs: list of (i, j) of one final subclass. Returns dict (i, j) -> list of reasons."""
    cut = h ** 0.5 / 32
    S = shapes(h); E = riv(h); r0 = tp['r0']
    Ys = [tp['Ts'] - 24 + 8 * o for o in range(4)]
    out = {}
    def add(L, why): out.setdefault(L, []).append(why)
    for x in range(len(labs)):
        for y in range(x + 1, len(labs)):
            L1, L2 = labs[x], labs[y]
            if abs(L1[0] - L2[0]) <= 210:
                add(max(L1, L2), 'B8 R_FF^+ (WD)')
            u1, u2 = sorted(((2 * L1[0] + 1 - r0) // 2, (2 * L2[0] + 1 - r0) // 2))
            for (q, p) in E:
                if u1 * p == u2 * q and u1 % q == 0 and (u1 // q) % 2 == 1:
                    add(L1, 'R-e R_IV'); add(L2, 'R-e R_IV')
            for par in ('o', 'e'):
                ya = 2 * L1[0] + 1 if par == 'o' else 2 * L1[1] + 2
                yb = 2 * L2[0] + 1 if par == 'o' else 2 * L2[1] + 2
                for Y in Ys:
                    da, db = Y - ya, Y - yb
                    if da <= 0 or db <= 0: continue
                    g = gcd(da, db)
                    for (A, dA, B, dB) in ((L1, da, L2, db), (L2, db, L1, da)):
                        if (dA // g, dB // g) in S:
                            Up = dA // g
                            if Up <= cut:
                                add(A, 'B8 R_FF^%s%s |U\'|=%d (WD)' % (par, par, Up))
                            else:
                                add(A, 'R-e R_FF^%s%s' % (par, par)); add(B, 'R-e R_FF^%s%s' % (par, par))
    return out
