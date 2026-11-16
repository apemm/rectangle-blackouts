"""Sanity check: k_T^(mu,nu) for a few strides and the menu minimum.
k_T = #{ |m| : 1<=|m|<ceil(|I_T|/nu), (mu m)^2+(T-2 nu m)^2 = L^2, 0<L<h }.
Also checks the bound k <= tau(mu^2) g_f(T) (1+2.08 log(4h^2 D/(mu^2 T^2)))."""
import sys, math
import numpy as np

def isqrt_arr(v):
    r = np.floor(np.sqrt(v.astype(np.float64))).astype(np.int64)
    r[r*r > v] -= 1
    r[(r+1)*(r+1) <= v] += 1
    return r

def kvals(h, mu, nu):
    A = (h+1)//2; K = h//2
    out = {}
    for jm in range(-(A-1), K):
        T = 2*jm+1; s = jm
        lo = max(0, -s); hi = min(A, K-s)
        n = hi-lo
        if n <= 0: continue
        M = -(-n//nu)
        if M <= 1: out[T] = 0; continue
        m = np.arange(1, M, dtype=np.int64)
        cnt = 0
        for sg in (1, -1):
            v = (mu*m)**2 + (T-2*nu*sg*m)**2
            r = isqrt_arr(v)
            ok = (r*r == v) & (r < h)
            if sg == 1: okp = ok
            else: okm = ok
        out[T] = int(np.count_nonzero(okp | okm))
    return out

def sqfree(n):
    d = 1; p = 2; x = n
    while p*p <= x:
        while x % (p*p) == 0: x //= p*p
        if x % p == 0: d *= p; x //= p
        p += 1
    return d*x

def kron(D0, p):  # Legendre-type split test for odd p not dividing disc
    return pow(D0 % p, (p-1)//2, p)

def g(T, D0):
    T = abs(T); res = 1; p = 3; x = T
    while p*p <= x:
        if x % p == 0:
            v = 0
            while x % p == 0: x //= p; v += 1
            if D0 % p != 0 and kron(D0, p) == 1: res *= 2*v+1
        p += 2
    if x > 1 and D0 % x != 0 and kron(D0, x) == 1: res *= 3
    return res

def tau(n):
    return sum(1 for d in range(1, n+1) if n % d == 0)

h = int(sys.argv[1])
menu = [(4,1),(8,1),(12,1),(4,3)]
K = {}
for f in menu:
    K[f] = kvals(h, *f)
    mu, nu = f; D = mu*mu+4*nu*nu; D0 = sqfree(D)
    viol = 0
    for T, k in K[f].items():
        b = tau(mu*mu)*g(T, D0)*(1+2.08*max(0.0, math.log(4*h*h*D/(mu*mu*T*T))))
        if k > b: viol += 1
    print(f, "D0", D0, "sum(k+1)", sum(k+1 for k in K[f].values()), "maxk", max(K[f].values()), "bound violations", viol)
Ts = list(K[menu[0]].keys())
for sub in [menu[:2], menu[:3], menu]:
    tot = sum(min(K[f][T] for f in sub)+1 for T in Ts)
    print("menu", sub, "sum min(k+1)", tot, "per h", round(tot/h, 3), "max min k", max(min(K[f][T] for f in sub) for T in Ts))
