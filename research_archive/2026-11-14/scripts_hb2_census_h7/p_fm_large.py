"""First-moment P incidence of an H7 block at large h (sigma = 1, S = 6272), total and
by diagonal band |T| (heuristic: validated against the exact census at h <= 2e6).
Triples from the factorisation of (X/2)^2 = (3136 q')^2.  usage: py p_fm_large.py h M lo bres"""
import sys, math, json
from h7common import block
h, M, lo, bres = map(int, sys.argv[1:5]); S = 6272
B = block(h, lo, bres=bres); c = bres - 17
nq = (h - 1) // S
spf = list(range(nq + 1))
for p in range(2, math.isqrt(nq) + 1):
    if spf[p] == p:
        for k in range(p * p, nq + 1, p):
            if spf[k] == k: spf[k] = p
def fac(n):
    f = {}
    while n > 1:
        p = spf[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f
def count_rows(res, Ysg, L):
    lo_y = max(lo, lo - Ysg, -(-(L + 2 - Ysg) // 2)); hi_y = min(h - lo, h - lo - Ysg, (2 * h - L - Ysg) // 2)
    if lo_y > hi_y: return 0
    first = lo_y + ((res - lo_y) % 28)
    return 0 if first > hi_y else (hi_y - first) // 28 + 1
edges = [0, 64, 256, 1024, 4096, 16384, 65536, 262144, 10 ** 12]
Wb = [0] * (len(edges) - 1); W = 0; ntr = 0
for qq in range(1, nq + 1):
    f = fac(qq); f[2] = f.get(2, 0) + 6; f[7] = f.get(7, 0) + 2
    v = (3136 * qq) ** 2; half = 3136 * qq
    e2 = 2 * f[2]
    # odd part divisors of v: v = 2^e2 * odd^2 ; one of a, b carries 2^e2 entirely
    odd = [1]
    for p, e in f.items():
        if p == 2: continue
        odd = [d * p ** k for d in odd for k in range(2 * e + 1)]
    oddv = v >> e2
    nd = len({d for d in (qq // M, -(-qq // M)) if d >= 1})
    for o in odd:            # a = o (odd), b = v / o (even)  or  a = v/o even...
        a1, b1 = o, v // o   # opposite parity pair, unordered
        a, b = min(a1, b1), max(a1, b1)
        if a + b > h - 1 or a == b: continue
        Y, L = b - a, a + b
        ntr += 1
        for sg in (1, -1):
            for role, res, ok in ((1, 17, (sg * Y - c) % 28 == 0), (2, bres, (sg * Y + c) % 28 == 0)):
                if not ok: continue
                w = nd * count_rows(res, sg * Y, L)
                if w == 0: continue
                W += w
                T = abs((sg * Y - c) // 28) if role == 1 else abs((sg * Y + c) // 28)
                for k in range(len(edges) - 1):
                    if edges[k] <= T < edges[k + 1]: Wb[k] += w; break
# labels per |T| band in the bulk square (both coordinates have the same bulk range up to 1)
n = B["iA1"] - B["iA0"] + 1
def labs(t0, t1):  # number of (i,j) in n x n with t0 <= |j-i| < t1
    tot = 0
    for t in (t0, t1):
        pass
    f = lambda t: (n if t > 0 else 0) and 0
    s = 0
    t1 = min(t1, n)
    if t0 >= t1: return 0
    # sum_{t=t0}^{t1-1} m(t), m(0) = n, m(t) = 2(n - t)
    if t0 == 0: s += n; t0 = 1
    s += 2 * ((t1 - t0) * n - (t1 * (t1 - 1) // 2 - t0 * (t0 - 1) // 2))
    return s
prof = []
for k in range(len(edges) - 1):
    nl = labs(edges[k], edges[k + 1])
    if nl: prof.append([edges[k], min(edges[k + 1], n), round(2 * Wb[k] / nl, 5)])
print(json.dumps({"h": h, "M": M, "bres": bres, "rho=h/S^2": round(h / S ** 2, 4), "triples": ntr,
                  "pred_mean_inc": 2 * W / B["labels"], "pred_band_profile[T0,T1,mean]": prof}))
