# Sanity check of Theorem W for w = 2: slab elements with |k_p| <= m (p = small-exponent prime), |k_q| <= J.
# Assignment: k_q = 0 -> prime p (one character, N = 18); k_q != 0 -> prime q at level |k_q| (t chars, N = 2q).
# Checks: loads per level <= 4 (at p) and <= 4(2m+1) (at q); the greedy digit choice never gets stuck;
# every assigned element ends with ||{zeta r}_l|| >= 1/N for some character of its prime.
import sys, math, random
from fractions import Fraction as F
from adelic_copy import mul, pw, L, s1, find_pi, PHI
p, q, m, J = map(int, sys.argv[1:5])
random.seed(1)
def omega(l):
    x = find_pi(l); o = mul(x, x); return (o[0]/l, o[1]/l)
op, oq = omega(p), omega(q); eps = (F(-1), F(-1))
ap = math.log(abs(float(s1(op)))); aq = math.log(abs(float(s1(oq)))); g = 2*math.log((1+5**0.5)/2)
def vl(x, l):
    d = x.denominator; e = 0
    while d % l == 0: d //= l; e += 1
    return e
els = []  # (kp, kq, r)
Pp = {k: pw(op, k) for k in range(-m, m+1)}; Pq = {k: pw(oq, k) for k in range(-J, J+1)}
for kp in range(-m, m+1):
    for kq in range(-J, J+1):
        if kp == 0 and kq == 0: continue
        base = mul(Pp[kp], Pq[kq]); x = -(kp*ap + kq*aq)/g
        for n in range(math.floor(x)-1, math.floor(x)+3):
            for sg in (1, -1):
                be = mul(pw(eps, n), base); be = (sg*be[0], sg*be[1]); s = float(s1(be))
                for st in (1.0, -float(PHI)**-2):
                    if s/st > 0 and abs(s/st - 1) < 0.2:
                        r = L((be[0]-1, be[1]))
                        assert vl(r, p) == abs(kp) and vl(r, q) == abs(kq)
                        els.append((kp, kq, r))
def val(r, z, l, j):  # {z r}_l with z mod l^j, v_l(r) = -j
    M = l**j; num = r.numerator; den = r.denominator // M
    return ((z * num * pow(den, -1, M)) % M) / M
def nrm(x): return min(x, 1 - x)
def choose(levels, l, N, t, top):
    zs = [0]*t; maxload = 0
    for j in range(1, top+1):
        E = levels.get(j, []); maxload = max(maxload, len(E))
        found = None
        cands = [tuple(random.randrange(l) for _ in range(t)) for _ in range(4000)]
        for dv in cands:
            zt = [zs[s] + dv[s]*l**(j-1) for s in range(t)]
            if all(any(nrm(val(r, zt[s], l, j)) >= 1/N for s in range(t)) for r in E):
                found = zt; break
        if found is None: return None, maxload, j
        zs = found
    return zs, maxload, None
levp, levq = {}, {}
for kp, kq, r in els:
    if kq == 0: levp.setdefault(abs(kp), []).append(r)
    else: levq.setdefault(abs(kq), []).append(r)
Mq = 4*(2*m+1); t = 1
while q**t <= Mq: t += 1
zp, lp, failp = choose(levp, p, 18, 1, m)
zq, lq, failq = choose(levq, q, 2*q, t, J)
print("p,q,m,J =", p, q, m, J, "| slab elements", len(els))
print("prime p: max load", lp, "(bound 4); stuck at level", failp)
print("prime q: max load", lq, "(bound", Mq, "), t =", t, "; stuck at level", failq)
print("colours (excluding off-strip factor 160000):", 18 * (2*q)**t)
