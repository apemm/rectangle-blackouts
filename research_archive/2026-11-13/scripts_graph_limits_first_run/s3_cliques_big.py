# Cliques in Cay(Z, D_T) for T with many split prime factors, using arithmetic in Z[phi]. Under 60 s.
import sys, time, itertools
from math import gcd, isqrt

# element a + b*phi, phi^2 = phi + 1
def mul(u, v):
    a, b = u; c, d = v
    return (a*c + b*d, a*d + b*c + b*d)
def conj(u):
    a, b = u            # phi' = 1 - phi
    return (a + b, -b)
def norm(u):
    a, b = u
    return a*a + a*b - b*b
def tr(u):
    a, b = u
    return 2*a + b
PHI = (0, 1)
PHIINV = (-1, 1)        # phi^{-1} = phi - 1

def prime_elt(p):
    for b in range(0, 4*p):
        for a in range(-4*p, 4*p):
            if abs(a*a + a*b - b*b) == p:
                return (a, b)
    raise ValueError(p)

def power(u, n):
    r = (1, 0)
    for _ in range(n): r = mul(r, u)
    return r

def S_T(primes, exps, Lmax):
    """all d != 0 with 20d^2+4Td+T^2 = L^2, L <= Lmax, T = prod p^e (primes split or 5)."""
    T = 1
    for p, e in zip(primes, exps): T *= p**e
    gens = []
    for p, e in zip(primes, exps):
        if p == 5:
            gens.append([ (5**e, 0) ])           # only one ideal: (sqrt5)^{2e} = 5^e
        else:
            pi = prime_elt(p); pic = conj(pi)
            gens.append([ mul(power(pi, a), power(pic, 2*e - a)) for a in range(2*e + 1) ])
    out = set()
    for combo in itertools.product(*gens):
        xi = (1, 0)
        for c in combo: xi = mul(xi, c)
        # run over units +- phi^k
        cur = xi
        # go up
        ups = [cur]
        for _ in range(400):
            cur = mul(cur, PHI)
            if abs(cur[1]) > 5*Lmax and abs(tr(cur)) > 50*Lmax: break
            ups.append(cur)
        cur = xi
        for _ in range(400):
            cur = mul(cur, PHIINV)
            if abs(cur[1]) > 5*Lmax and abs(tr(cur)) > 50*Lmax: break
            ups.append(cur)
        for u in ups:
            for s in (1, -1):
                a, b = s*u[0], s*u[1]
                if a*a + a*b - b*b != -T*T: continue
                X = 2*a + b; L = abs(b)
                if L == 0 or L > Lmax: continue
                if (X - T) % 10 != 0: continue
                d = (X - T)//10
                if d != 0:
                    assert 20*d*d + 4*T*d + T*T == L*L
                    out.add(d)
    return T, out

def max_clique(D, tlimit):
    Ds = sorted(D)
    best = [1, [0]]
    t0 = time.time()
    def ext(cl, cands):
        if len(cl) > best[0]:
            best[0] = len(cl); best[1] = cl[:]
        if time.time() - t0 > tlimit: return
        for idx, v in enumerate(cands):
            if len(cl) + len(cands) - idx <= best[0]: return
            newc = [u for u in cands[idx+1:] if (u - v) in D]
            ext(cl + [v], newc)
    ext([0], Ds)
    return best

t0 = time.time()
tests = [
 ([5,11,19],[1,1,1]), ([5,11,19,29],[1,1,1,1]), ([5,11,19,29,31],[1,1,1,1,1]),
 ([11,19,29,31],[1,1,1,1]), ([5,11],[1,2]), ([5,11,19],[1,2,1]), ([5,11,19],[1,1,2]), ([5,11,19],[1,2,2]),
 ([5,11,19,29,31,41],[1,1,1,1,1,1]), ([5,11,19,31],[1,1,1,1]), ([5,11,19,41],[1,1,1,1]), ([5,11,29,31],[1,1,1,1]),
 ([5,11,19,29,31,41,59],[1,1,1,1,1,1,1]),
]
for primes, exps in tests:
    T = 1
    for p, e in zip(primes, exps): T *= p**e
    T, S = S_T(primes, exps, 200*T)
    D = set(abs(d) for d in S)
    k, cl = max_clique(D, 6.0)
    print(primes, exps, "T=", T, "|D|=", len(D), "clique>=", k, cl, "t=%.1f" % (time.time() - t0), flush=True)
    if time.time() - t0 > 50: break
