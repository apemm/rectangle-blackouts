# Check of the adelic Pisot identities for Gamma_l and of the three-character colouring.
# K = Q(sqrt5), elements a + b*phi with rational a, b.  eps = -phi^2, omega = pi^2 / l.
# chi_pm(x) = 2 sqrt5 x - { +-2 s5 x }_l,   s5 = iota_pi(sqrt5) in Z_l, iota_pi(pi) = 0 mod l.
# Claimed: k >= 0: chi_-(r) = fA(s), chi_+(r) = fC(s);  k <= 0: chi_+(r) = fA(s), chi_-(r) = fC(s),
# with s = sigma1(beta), fA(s) = (2 phi'/s - 1)/sqrt5, fC(s) = (2 phi s - 1)/sqrt5   (mod 1).
import sys
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 80
S5 = mp.sqrt(5); PHI = (1+S5)/2; PHIc = (1-S5)/2

def mul(x, y):  # (a+b phi)(c+d phi), phi^2 = phi+1
    a, b = x; c, d = y
    return (a*c + b*d, a*d + b*c + b*d)
def pw(x, n):
    r = (F(1), F(0))
    if n < 0:
        x = inv(x); n = -n
    while n:
        if n & 1: r = mul(r, x)
        x = mul(x, x); n >>= 1
    return r
def conjg(x): a, b = x; return (a + b, -b)          # phi -> 1 - phi
def norm(x): a, b = x; return a*a + a*b - b*b
def inv(x):
    c = conjg(x); n = norm(x); return (c[0]/n, c[1]/n)
def L(x): a, b = x; return (a + 3*b)/10
def s1(x): a, b = x; return mp.mpf(a.numerator)/a.denominator + mp.mpf(b.numerator)/b.denominator*PHI

def find_pi(l):
    for y in range(1, 200):
        for x in range(-200, 201):
            if x*x + x*y - y*y == l: return (F(x), F(y))
def hensel_phi(l, x, y, K):
    # root of t^2 - t - 1 with x + y t = 0 mod l
    m = l**K
    t0 = next(t for t in range(l) if (t*t - t - 1) % l == 0 and (x + y*t) % l == 0)
    t = t0
    for _ in range(K+2):
        f = t*t - t - 1; fp = 2*t - 1
        t = (t - f*pow(fp, -1, m)) % m
    assert (t*t - t - 1) % m == 0
    return t
def frac_l(q, z, l, K):
    """{ z * q }_l as a Fraction in [0,1), q rational, z in Z_l given mod l^K."""
    num, den = q.numerator, q.denominator
    e = 0
    while den % l == 0: den //= l; e += 1
    if e == 0: return F(0)
    assert e <= K - 2
    m = l**e
    v = (z * num * pow(den, -1, m)) % m
    return F(v, m)
def dist1(x):  # ||x|| for mpf
    f = x - mp.floor(x); return min(f, 1 - f)

if __name__ == "__main__":
    l = int(sys.argv[1]); NB = int(sys.argv[2]); KB = int(sys.argv[3])
    K = KB + 6
    pi = find_pi(l); x, y = int(pi[0]), int(pi[1])
    phl = hensel_phi(l, x, y, K); m = l**K
    s5 = (2*phl - 1) % m
    om = (pi[0]*pi[0]/l + 0, 0)  # placeholder
    om = mul(pi, pi); om = (om[0]/l, om[1]/l)
    eps = (F(-1), F(-1))
    worst = 0; cnt = 0
    for k in range(-KB, KB+1):
        wk = pw(om, k)
        for n in range(-NB, NB+1):
            for sg in (1, -1):
                be = mul(pw(eps, n), wk); be = (sg*be[0], sg*be[1])
                if be == (F(1), F(0)): continue
                r = L((be[0]-1, be[1]))
                if r == 0: continue
                s = s1(be)
                fA = (2*PHIc/s - 1)/S5; fC = (2*PHI*s - 1)/S5
                re = 2*S5*(mp.mpf(r.numerator)/r.denominator)
                cp = re - mp.mpf(frac_l(r, 2*s5, l, K).numerator)/frac_l(r, 2*s5, l, K).denominator
                q = frac_l(r, (-2*s5) % m, l, K)
                cm = re - mp.mpf(q.numerator)/q.denominator
                if k >= 0: e1 = dist1(cm - fA); e2 = dist1(cp - fC)
                if k < 0: e1 = dist1(cp - fA); e2 = dist1(cm - fC)
                worst = max(worst, e1, e2); cnt += 1
    print("l", l, "pi", (x, y), "checked", cnt, "max identity error", mp.nstr(worst, 5))
