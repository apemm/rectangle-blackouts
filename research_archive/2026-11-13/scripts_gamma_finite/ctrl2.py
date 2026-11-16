# Direct check: the explicit colouring c(x) = (floor(20{chi+}), floor(20{chi-}), floor(N2{chi_zeta})) on x = i/T,
# T = 5 l^e, i in [0,n), against all edges |i-i'| in D_T (brute force squares).
import sys, subprocess, re
from math import isqrt
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 40
l, e, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
T = 5*l**e
out = subprocess.run(["py", "colour_l.py", str(l), "40", str(e), "0.2"], capture_output=True, text=True).stdout
digits = eval(re.search(r"digits \[(.*?)\]", out.replace("zeta mod l^%d digits " % e, "digits ")).group(0)[7:])
zeta = sum(d*l**i for i, d in enumerate(digits))
from adelic import find_pi, hensel_phi
K = e+4; mK = l**K
pi = find_pi(l); s5 = (2*hensel_phi(l, int(pi[0]), int(pi[1]), K) - 1) % mK
N2 = l if l < 17 else 16
S5 = mp.sqrt(5)
def fl(i, z):  # { z * i/T }_l
    m = l**e; v = (z*i*pow(5, -1, m)) % m; return F(v, m)
def col(i):
    x = mp.mpf(i)/T; re_ = 2*S5*x
    a = re_ - mp.mpf(fl(i, 2*s5).numerator)/fl(i, 2*s5).denominator
    b = re_ - mp.mpf(fl(i, -2*s5).numerator)/fl(i, -2*s5).denominator
    c = -fl(i, zeta)
    fa = a - mp.floor(a); fb = b - mp.floor(b); fc = c - (c.numerator//c.denominator)
    return (int(mp.floor(20*fa)), int(fc*N2))
C = [col(i) for i in range(n)]
D = [d for d in range(1, n) if any(isqrt(20*d*d+s*4*T*d+T*T)**2 == 20*d*d+s*4*T*d+T*T for s in (1, -1))]
bad = sum(1 for i in range(n) for d in D if i+d < n and C[i] == C[i+d])
print("T", T, "n", n, "|D|", len(D), "colours used", len(set(C)), "monochromatic edges", bad)
