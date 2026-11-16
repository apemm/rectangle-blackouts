# Variant: the group actually swept by columns is <phi^2, s2*omega2> with s2 = sign sigma1(omega2) (no free -1).
from fractions import Fraction as F
from adelic_copy import find_pi, mul, hensel_phi, s1
from hfull import omega, emb, gen_order
for (l1, l2) in [(11, 19), (19, 11), (11, 29), (29, 11), (19, 29), (29, 19)]:
    m = l1 * l1
    p1 = find_pi(l1); t = hensel_phi(l1, int(p1[0]), int(p1[1]), 4) % m
    o2 = omega(l2); s2 = 1 if s1(o2) > 0 else -1
    for tt, name in [(t, "P"), ((1 - t) % m, "P'")]:
        g1 = emb((F(1), F(1)), tt, m)  # phi^2 = 1 + phi
        g2 = (s2 * emb(o2, tt, m)) % m
        o = gen_order([g1, g2], m)
        print(l1, l2, name, "s2", s2, "order <phi^2, s2*om2>", o, "of", l1*(l1-1))
