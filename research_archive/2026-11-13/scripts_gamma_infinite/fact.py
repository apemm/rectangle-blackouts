# Sanity check of the factorization lemma and the archimedean obstruction lemma.
from fractions import Fraction as F
from c1_lib import mul, conj, norm, inv, pw, L, r_of, is_sq, odd_den
def cong1(beta, m, l):
    # beta - 1 in m * O[1/l]  (l coprime to m)
    x, y = beta[0]-1, beta[1]
    for q in (x, y):
        d = q.denominator
        while d % l == 0: d //= l
        assert d == 1, q
        if (q.numerator) % m: return False
    return True
def omega(pi):
    return mul(pi, inv(conj(pi)))
eps = (F(-1), F(-1))
P = {11: (F(3), F(1)), 19: (F(4), F(3))}
for l, pi in P.items(): assert norm(pi) == l
def find(l, m, kmax=2, amax=300):
    w = omega(P[l]); out = []
    for k in [1, -1, 2, -2][:2*kmax]:
        wk = pw(w, k)
        e = (F(1), F(0))
        for a in range(0, amax):
            b = mul(e, wk)
            for s in (1, -1):
                bb = (s*b[0], s*b[1])
                if cong1(bb, m, l): out.append((s, a, k, bb))
            e = mul(e, eps)
        if out: break
    return out
b1 = find(11, 190)
b2 = find(19, 110)
print("found", len(b1), len(b2))
s1, a1, k1, B1 = b1[0]; s2, a2, k2, B2 = b2[0]
print("beta1 = %d eps^%d omega11^%d ; beta2 = %d eps^%d omega19^%d" % (s1, a1, k1, s2, a2, k2))
r1, r2, r12 = r_of(B1), r_of(B2), r_of(mul(B1, B2))
for r in (r1, r2, r12):
    assert odd_den(r) and is_sq(20*r*r+4*r+1)
c = r12 - r1 - r2
print("cross term", c, "integer:", c.denominator == 1)
print("|r1|,|r2|,|r12| ~", float(abs(r1)), float(abs(r2)), float(abs(r12)))
print("den r1, r2, r12:", r1.denominator, r2.denominator, r12.denominator)
