# Check hypothesis (Hfull): <-1, eps, omega_{l2}> is dense in Z_{l1}^* under both embeddings of K into Q_{l1}.
# Dense iff the generated subgroup of (Z/l1^2)^* is everything (l1 odd).
from fractions import Fraction as F
from adelic_copy import find_pi, mul, hensel_phi
def omega(l):
    p = find_pi(l); o = mul(p, p); return (o[0]/l, o[1]/l)
def emb(x, t, m):  # a + b phi -> a + b t mod m
    a, b = x
    return (a.numerator * pow(a.denominator, -1, m) + b.numerator * pow(b.denominator, -1, m) * t) % m
def gen_order(gens, m):
    seen = {1}; frontier = [1]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                y = g * h % m
                if y not in seen: seen.add(y); nf.append(y)
        frontier = nf
    return len(seen)
for (l1, l2) in [(11, 19), (19, 11), (11, 29), (29, 11), (19, 29), (29, 19), (11, 31), (31, 41)]:
    m = l1 * l1
    p1 = find_pi(l1); t = hensel_phi(l1, int(p1[0]), int(p1[1]), 4) % m
    for tt, name in [(t, "P"), ((1 - t) % m, "P'")]:
        eps = emb((F(-1), F(-1)), tt, m); om2 = emb(omega(l2), tt, m)
        o = gen_order([m - 1, eps, om2], m)
        o_no_om = gen_order([m - 1, eps], m)
        print(l1, l2, name, "order", o, "of", l1 * (l1 - 1), "full" if o == l1 * (l1 - 1) else "NOT full", "| <-1,eps> alone:", o_no_om)
