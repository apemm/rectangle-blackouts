# Divisor-driven shape-level search for a fatal Fee triple in L***(3).
# E1 even label vertex (class c0 at t0), E2 even label end (class c1 at t1 = t0 + 16),
# V the offset-0 hole at the slot of label i1 + 32 of c0 (alpha = 32u slots), and
# W = V + E2 - E1, which lands in the column of label i2 + 32 of c1.
# Right angle at E1:  eta (8 u alpha + d) = 8 alpha Dnu,  Dnu = u Ds - DM,  d = yV - y_E1.
# Only positions and rows are checked; which labels the colouring puts in class k = 0 is not modelled.
import sys, time

def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2; r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def legendre(a, q):
    return pow(a % q, (q - 1) // 2, q)

def factor(n):
    n = abs(n); f = {}
    q = 2
    while q * q <= n:
        while n % q == 0:
            f[q] = f.get(q, 0) + 1; n //= q
        q += 1 if q == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds

u = 3
h = 20_000_000
A, K = (h + 1) // 2, h // 2
kappa, b = 0, 0
alpha = 32 * u
start = time.time()

def tstar(iota, sigma):
    yP, T = 2 * iota + 1, 2 * sigma + 1
    off = 32 if T % 4 == 3 else 48
    return max(y for y in range(h - 70, h + 1) if (y - yP - off) % 64 == 0)

def rho(s, p, l, twisted):
    m = 16 * l
    return (pow(p, -1, m) * ((u * s if twisted else s) - kappa)) % m

def run(twisted, budget):
    hits, pairs = [], 0
    p = 80 * h + 1
    lstart = int(1.04 * h) + 1
    while time.time() - start < budget and p < 160 * h:
        p += 2
        if p % 4 != 3 or not is_prime(p) or legendre(37, p) != p - 1:
            continue
        cands = []
        for kk in range(p // (2 * h) + 1, p // lstart + 1):
            c = p // kk
            w = h // (16 * kk)
            for l in range(c - w, c + w):
                if l < lstart or l > 2.08 * h or not is_prime(l) or legendre(37, l) != l - 1:
                    continue
                mm = 16 * l
                Dres = (16 * p * (pow(u, -1, mm) if twisted else 1)) % mm
                Ds = Dres if Dres < mm // 2 else Dres - mm
                if abs(Ds) < h // 4 and Ds % 32 == 0:
                    cands.append((l, Ds))
            if len(cands) >= 3:
                break
        for l, Ds in cands:
            pairs += 1
            process(p, l, Ds, hits)
    return hits, pairs

def process(p, l, Ds, hits):
        DM = 16 * p
        Dnu = u * Ds - DM
        for den in divisors(factor(Dnu)):
            if den % 2 == 0:
                continue
            d = den - 8 * u * alpha
            if d <= 0:
                continue
            num = 8 * alpha * Dnu
            eta = num // den
            if num % den or eta == 0 or (eta - Ds) % 32:
                continue
            for iota in range(32):
                for sigma in range(16):
                    Ts = tstar(iota, sigma)
                    yV = Ts - 24
                    yE1 = yV - d
                    if yE1 % 2 or yE1 < 10002:
                        continue
                    j1 = (yE1 - 2) // 2
                    if (j1 - iota - sigma) % 16:
                        continue
                    hits.append((p, l, Ds, d, eta, iota, sigma, yV, j1))

def verify(hit, twisted):
    p, l, Ds, d, eta, iota, sigma, yV, j1 = hit
    for i1 in range(iota, A, 32):
        s0 = j1 - i1
        if s0 < -(A - 1):
            break
        if s0 % 16 != sigma or s0 > K - 1:
            continue
        s1, j2 = s0 + Ds, j1 + eta
        i2 = j2 - s1
        if not (0 <= i2 and i2 + 32 < A and 0 <= j2 and j2 + 32 < K and -(A - 1) <= s1 <= K - 1):
            continue
        # every label involved must be a kept label: rows in [5000, h - 5000] (outside R-a..R-d)
        rows = [2 * i1 + 1, 2 * j1 + 2, 2 * i2 + 1, 2 * j2 + 2, 2 * (i2 + 32) + 1, 2 * (j2 + 32) + 2]
        if min(rows) < 5000 or max(rows) > h - 5000:
            continue
        t0, t1 = rho(s0, p, l, twisted), rho(s1, p, l, twisted)
        if t1 - t0 != 16:
            continue
        M0, M1 = p * t0 + b, p * t1 + b
        E1 = (4 * (u * i1 + M0), 2 * j1 + 2)
        E2 = (4 * (u * i2 + M1), 2 * j2 + 2)
        V = (4 * (u * (i1 + 32) + M0), yV)
        W = (V[0] + E2[0] - E1[0], V[1] + E2[1] - E1[1])
        dotp = (V[0] - E1[0]) * (E2[0] - E1[0]) + (V[1] - E1[1]) * (E2[1] - E1[1])
        if dotp == 0 and W[0] == 4 * (u * (i2 + 32) + M1) and 1 <= W[1] <= h:
            return dict(i1=i1, j1=j1, s0=s0, i2=i2, j2=j2, s1=s1, t0=t0, t1=t1, E1=E1, E2=E2, V=V, W=W,
                        rows_in_W_column=(2 * (i2 + 32) + 1, 2 * (j2 + 32) + 2), span=abs(E2[0] - E1[0]))
    return None

for twisted, budget in ((False, 25), (True, 50)):
    hits, pairs = run(twisted, budget)
    print("twisted" if twisted else "untwisted", "| prime pairs:", pairs, "| shape hits:", len(hits))
    shown = 0
    for hit in hits:
        v = verify(hit, twisted)
        if v:
            print("  instance p=%d l=%d Ds=%d d=%d eta=%d iota=%d sigma=%d" % hit[:7])
            print("  ", v)
            shown += 1
            if shown >= 1:
                break
    sys.stdout.flush()
