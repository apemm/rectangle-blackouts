# Check of the multi-prime aligned identity: chi_z(x) = 2 sqrt5 x - sum_i {2 z_i s5_i x}_{l_i};
# for beta = +-eps^n w1^k1 w2^k2 with sign vector sig: chi_{-sig}(r) = fA(s), chi_{sig}(r) = fC(s) mod 1.
import itertools, random
from fractions import Fraction as F
import mpmath as mp
from adelic import mul, pw, L, s1, find_pi, hensel_phi, frac_l, dist1, S5, PHI, PHIc
mp.mp.dps = 80
Ls = [11, 19]; K = 14
data = []
for l in Ls:
    p = find_pi(l); o = mul(p, p); o = (o[0]/l, o[1]/l)
    s5 = (2*hensel_phi(l, int(p[0]), int(p[1]), K) - 1) % l**K
    data.append((l, o, s5))
eps = (F(-1), F(-1)); worst = 0; cnt = 0
random.seed(1)
for _ in range(400):
    n = random.randint(-25, 25); ks = [random.randint(-8, 8) for _ in Ls]; sg = random.choice((1, -1))
    be = pw(eps, n)
    for (l, o, s5), k in zip(data, ks): be = mul(be, pw(o, k))
    be = (sg*be[0], sg*be[1]); r = L((be[0]-1, be[1]))
    if r == 0: continue
    s = s1(be); fA = (2*PHIc/s - 1)/S5; fC = (2*PHI*s - 1)/S5
    sig = [1 if k > 0 else -1 for k in ks]   # zeros: any choice
    def chi(z):
        v = 2*S5*mp.mpf(r.numerator)/r.denominator
        for (l, o, s5), zi in zip(data, z):
            q = frac_l(r, (2*zi*s5) % l**K, l, K); v -= mp.mpf(q.numerator)/q.denominator
        return v
    e1 = dist1(chi([-x for x in sig]) - fA); e2 = dist1(chi(sig) - fC)
    worst = max(worst, e1, e2); cnt += 1
print("checked", cnt, "max error", mp.nstr(worst, 5))
