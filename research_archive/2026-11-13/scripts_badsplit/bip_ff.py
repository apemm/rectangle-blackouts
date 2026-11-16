# Bipartiteness of ratio graphs on odd integers <= N, by union-find with parity.
# G_FF(r): shapes (a,b), gcd 1, a odd, v2(b) in BSET, r/2 < a/b < r;
#   U = (a - r b)(a^2+b^2), V = a^3 - r a^2 b - 3 a b^2 + r b^3, edge (k|U'|, k|V'|), k odd.
# R_IV^(k): (al,be) odd coprime, 0<al<be, v2(be-al) >= k-2; F = 4(al-2be)^2+be^2,
#   g = gcd(F, be-al), q = al F/g, p = (al F + 4(be-al) be^2)/g; edge (m q, m p), m odd.
import sys
from math import gcd

def v2(x):
    k = 0
    while x % 2 == 0: x //= 2; k += 1
    return k

def ff_shapes(r, N, BSET):
    out = []
    b = 1
    while True:
        if 2*b**3 > 40*N and b > 4: break   # |V| >= c b^3 roughly; crude stop
        if v2(b) in BSET:
            for a in range(r*b//2 + 1, r*b):
                if a % 2 == 0 or gcd(a, b) != 1: continue
                U = (a - r*b)*(a*a + b*b); V = a**3 - r*a*a*b - 3*a*b*b + r*b**3
                g = gcd(U, V); U1, V1 = abs(U//g), abs(V//g)
                if max(U1, V1) <= N: out.append((U1, V1, a, b))
        b += 1
    return out

def iv_shapes(k, N):
    out = []
    be = 3
    while be**3 // 5 <= N:
        for al in range(1, be, 2):
            if gcd(al, be) != 1 or v2(be - al) < k - 2: continue
            F = 4*(al - 2*be)**2 + be*be; g = gcd(F, be - al)
            q = al*F//g; p = (al*F + 4*(be - al)*be*be)//g
            if p <= N: out.append((q, p, al, be))
        be += 2
    return out

def bip(edges_gen, N):
    par = {}; rel = {}
    def find(x):
        path = []
        while par.get(x, x) != x:
            path.append(x); x = par[x]
        root = x
        # compress with parity
        acc = 0
        for y in reversed(path):
            acc ^= rel[y]; rel[y] = acc; par[y] = root
        return root
    def parity(x):
        find(x); return rel.get(x, 0) if par.get(x, x) != x else 0
    ne = 0
    for (u, v, s) in edges_gen:
        ne += 1
        ru, rv = find(u), find(v)
        pu, pv = parity(u), parity(v)
        if ru == rv:
            if pu == pv:
                return ne, (u, v, s)
        else:
            par[ru] = rv; rel[ru] = pu ^ pv ^ 1
    return ne, None

def gen(shapes, N):
    # edges ordered by largest endpoint, so the first conflict has small vertices
    ev = []
    for (x, y, *s) in shapes:
        lo, hi = min(x, y), max(x, y)
        for m in range(1, N//hi + 1, 2):
            ev.append((m*hi, m*lo, m*hi, tuple(s)))
    ev.sort()
    for (_, u, v, s) in ev:
        yield (u, v, s)

which = sys.argv[1]; N = int(float(sys.argv[2]))
if which == 'iv':
    sh = iv_shapes(int(sys.argv[3]), N)
else:
    r = int(sys.argv[3]); BSET = set(int(x) for x in sys.argv[4].split(','))
    sh = ff_shapes(r, N, BSET)
print(which, sys.argv[3:], "N =", N, "shapes:", len(sh), "smallest:", sorted(sh)[:6])
ne, conf = bip(gen(sh, N), N)
print("edges processed:", ne, "first odd-cycle-closing edge:", conf)
