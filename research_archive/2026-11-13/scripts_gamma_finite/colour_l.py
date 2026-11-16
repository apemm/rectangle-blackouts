# Sanity check of the three-character colouring of Gamma_l (one split prime l).
# chi_+ , chi_- : x -> 2 sqrt5 x - { +-2 s5 x }_l ; chi_zeta : x -> -{ zeta x }_l, zeta built digit by digit.
# Claim: every r = L(beta-1), beta in +-<eps, omega>, r != 0, has
#   max(||chi_+(r)||, ||chi_-(r)||) >= C0 = 0.05  unless sigma1(beta) in a strip, and then
#   ||chi_zeta(r)|| >= cz  (cz = 1/l for l = 11, 1/16 for l >= 19).
import sys, time
from fractions import Fraction as F
import mpmath as mp
from adelic import mul, pw, L, s1, find_pi, hensel_phi, frac_l, dist1, S5, PHI
mp.mp.dps = 60
l = int(sys.argv[1]); NB = int(sys.argv[2]); KB = int(sys.argv[3]); delta = float(sys.argv[4])
cz = F(1, l) if l < 17 else F(1, 16)
K = KB + 6; mK = l**K
pi = find_pi(l); x, y = int(pi[0]), int(pi[1])
s5 = (2*hensel_phi(l, x, y, K) - 1) % mK
om = mul(pi, pi); om = (om[0]/l, om[1]/l); eps = (F(-1), F(-1))
t0 = time.time()
elems = []
for k in range(-KB, KB+1):
    wk = pw(om, k)
    for n in range(-NB, NB+1):
        en = pw(eps, n)
        for sg in (1, -1):
            be = mul(en, wk); be = (sg*be[0], sg*be[1])
            r = L((be[0]-1, be[1]))
            if r == 0: continue
            s = s1(be)
            instrip = (1-delta < s < 1+delta) or (-PHI**-2*(1+delta) < s < -PHI**-2*(1-delta))
            elems.append((k, n, sg, r, s, instrip))
# off-strip check
def chi(r, z):
    q = frac_l(r, z % mK, l, K)
    return 2*S5*mp.mpf(r.numerator)/r.denominator - mp.mpf(q.numerator)/q.denominator
minoff = 1; minstrip_pm = 1
for (k, n, sg, r, s, st) in elems:
    v = max(dist1(chi(r, 2*s5)), dist1(chi(r, -2*s5)))
    if st: minstrip_pm = min(minstrip_pm, v)
    else: minoff = min(minoff, v)
# greedy zeta
zeta = 0; perlevel = {}
for j in range(1, KB+1):
    S = [(k, n, sg, r) for (k, n, sg, r, s, st) in elems if st and abs(k) == j]
    perlevel[j] = len(S)
    m = l**j; units = []
    for (k, n, sg, r) in S:
        num, den = r.numerator, r.denominator
        e = 0
        while den % l == 0: den //= l; e += 1
        assert e == j, (k, e)
        units.append(num*pow(den, -1, m) % m)
    ok = None
    for dg in range(l):
        z = zeta + dg*l**(j-1)
        if all(min(F((z*u) % m, m), 1-F((z*u) % m, m)) >= cz for u in units): ok = z; break
    assert ok is not None, "no digit at level %d" % j
    zeta = ok
# final check on strip elements with zeta
minz = 1; nstrip = 0
for (k, n, sg, r, s, st) in elems:
    if st:
        nstrip += 1
        q = frac_l(r, zeta, l, K); minz = min(minz, min(q, 1-q))
print("l", l, "elements", len(elems), "strip elements", nstrip, "per level", max(perlevel.values()),
      "min off-strip max(||chi+||,||chi-||) = %.4f" % float(minoff),
      "min on strip (chi+-) = %.2e" % float(minstrip_pm), "min ||chi_zeta|| on strip = %.4f (target %.4f)" % (float(minz), float(cz)),
      "zeta mod l^%d digits" % KB, [ (zeta//l**i) % l for i in range(KB)], "%.1fs" % (time.time()-t0))
