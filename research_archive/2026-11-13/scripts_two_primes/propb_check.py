# Sanity check of Proposition B (column averaging).  l1 = small-exponent prime, rows i = k1 in [1, m],
# columns j = k2 in [1, J], window s in (0.8, 1.2).  For t random pure l1-characters zeta_s and N cells,
# count per column the present rows whose l1-values all lie in (-1/N, 1/N).  Compare the column average with
# the lower bound 0.4213 * (2 (1 - 1/l) m / N^t - 2/l) and report the maximum over columns.
import sys, math, random
from adelic_copy import find_pi, hensel_phi, s1, mul
from fractions import Fraction as F
l1, l2, m, J, t, N, seed = map(int, sys.argv[1:8])
random.seed(seed)
K = m + 3; Mod = l1**K
def pi_int(l): x = find_pi(l); return (int(x[0]), int(x[1]))
p1 = pi_int(l1); p2 = pi_int(l2)
def mm(x, y):
    a, b = x; c, d = y
    return ((a*c + b*d) % Mod, (a*d + b*c + b*d) % Mod)
def mpow(x, n):
    r = (1, 0)
    while n:
        if n & 1: r = mm(r, x)
        x = mm(x, x); n >>= 1
    return r
eps = (Mod - 1, Mod - 1); epsinv = mpow(eps, 0)  # placeholder
# eps^-1 = -phi^-2, phi^-1 = phi - 1
phinv = (Mod - 1, 1); epsinv = mm((Mod - 1, 0), mm(phinv, phinv))
assert mm(eps, epsinv) == (1, 0)
inv_l2 = pow(l2, -1, Mod)
om2 = mm(p2, p2); om2 = (om2[0]*inv_l2 % Mod, om2[1]*inv_l2 % Mod)
pi1sq = mm(p1, p1)
# real data
PHI = (1 + 5**0.5)/2
def s1f(x): return x[0] + x[1]*PHI
A1 = math.log(abs(s1f(p1)**2 / l1)); A2 = math.log(abs(s1f(p2)**2 / l2))
sg1 = 1 if s1f(p1)**2 / l1 > 0 else -1; sg2 = 1 if s1f(p2)**2/l2 > 0 else -1
g = 2*math.log(PHI); lo, hi = math.log(0.8), math.log(1.2)
inv10 = pow(10, -1, Mod)
zetas = [random.randrange(1, Mod) for _ in range(t)]
pw1 = [mpow(pi1sq, i) for i in range(m+1)]
counts = []
om2p = (1, 0)
for j in range(1, J+1):
    om2p = mm(om2p, om2)
    c = 0
    for i in range(1, m+1):
        base = i*A1 + j*A2
        n = math.ceil((lo - base)/g)
        if not (n*g + base < hi): continue
        sign = (-1)**n * sg1**i * sg2**j  # sign of sigma1(eps^n omega1^i omega2^j)
        e = mpow(eps, n) if n >= 0 else mpow(epsinv, -n)
        X = mm(mm(e, pw1[i]), om2p)        # = l1^i * beta / sign
        if sign < 0: X = ((-X[0]) % Mod, (-X[1]) % Mod)
        LX = (X[0] + 3*X[1]) * inv10 % Mod   # L(l1^i beta)
        y = (LX - l1**i * inv10) % Mod       # l1^i * r, an l1-unit
        assert y % l1 != 0
        M = l1**i
        bad = all(min(((z*y) % M)/M, 1 - ((z*y) % M)/M) < 1/N for z in zetas)
        c += bad
    counts.append(c)
avg = sum(counts)/len(counts)
lb = 0.4213*(2*(1 - 1/l1)*m/N**t - 2/l1)
hist = {}
for c in counts: hist[c] = hist.get(c, 0) + 1
print("l1,l2,m,J,t,N =", l1, l2, m, J, t, N, "| column average", round(avg, 4), "lower bound", round(lb, 4), "| max", max(counts), "| histogram", dict(sorted(hist.items())))
