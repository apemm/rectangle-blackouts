"""Sanity check of the stride-4u placement L***(u): positions, U1, and the
re-derived identities.  Synthetic region, true primes.  Not a board census."""
import random, sys

def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def leg(a, q):  # Euler criterion, q odd prime not dividing a
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r

def run(h, u, seed):
    rnd = random.Random(seed)
    D = 4 * u * u + 1
    P = 8 * u * u + 4
    A, K = (h + 1) // 2, h // 2
    def pick(lo, hi, cond):
        while True:
            q = rnd.randrange(lo, hi + 1)
            if is_prime(q) and cond(q): return q
    l = pick(int(1.04 * h) + 1, int(2.08 * h), lambda q: q > 2 and leg(D, q) == -1)
    p = pick(P * h + 1, 2 * P * h, lambda q: q % 4 == 3 and leg(D, q) == -1)
    m = 16 * l
    pinv = pow(p, -1, m)
    kappa, b = rnd.randrange(-50, 50), rnd.randrange(-50, 50)
    iota, sigma = rnd.randrange(32), rnd.randrange(16)
    B = 4
    labels = []  # (i, j, s, t, n_new, n_old)
    for s in range(-A + 1, K):
        if (s - sigma) % 16: continue
        for i in range(iota, A, 32):
            j = i + s
            if not (0 <= j < K): continue
            k = rnd.randrange(B)
            t_new = (pinv * (u * s - kappa)) % m + m * k
            t_old = (pinv * (s - kappa)) % m + m * k
            labels.append((i, j, s, t_new, u * i + p * t_new + b, u * i + p * t_old + b))
    res = {}
    res['n_mod16_new'] = sorted({L[4] % 16 for L in labels})
    res['n_mod16_old'] = sorted({L[5] % 16 for L in labels})
    res['inj_new'] = len({L[4] for L in labels}) == len(labels)
    res['nuj_mod_16l_new'] = len({(L[4] - u * L[1]) % m for L in labels})
    res['nuj_mod_l_old'] = len({(L[5] - u * L[1]) % l for L in labels})
    res['nj_mod_l_old'] = len({(L[5] - L[1]) % l for L in labels})
    bad = 0
    ncl = lambda L: u * L[2] - p * L[3]          # class constant n(c) = u s - M_c
    odd = lambda L: (4 * L[4], 2 * L[0] + 1)
    even = lambda L: (4 * L[4], 2 * L[1] + 2)
    dot = lambda X, Y: X[0] * Y[0] + X[1] * Y[1]
    sub = lambda X, Y: (X[0] - Y[0], X[1] - Y[1])
    for _ in range(20000):
        L1, L2 = rnd.choice(labels), rnd.choice(labels)
        Dt, Ds, Di, Dj = L2[3] - L1[3], L2[2] - L1[2], L2[0] - L1[0], L2[1] - L1[1]
        Dn = u * Ds - p * Dt
        if Dn % m: bad += 1
        if (Dt == 0) != (Dn == 0): bad += 1
        dxo, dyo = sub(odd(L2), odd(L1)); dxe, dye = sub(even(L2), even(L1))
        if dxo // 4 - u * dyo // 2 != p * Dt: bad += 1
        if dxe // 4 - u * dye // 2 != -Dn: bad += 1
    # identities with true coordinates
    bycls = {}
    for L in labels: bycls.setdefault((L[2], L[3]), []).append(L)
    multi = [c for c in bycls if len(bycls[c]) >= 2]
    for _ in range(20000):
        c0 = rnd.choice(multi); c1 = rnd.choice(list(bycls))
        if c1 == c0: continue
        Lv, Lp = rnd.sample(bycls[c0], 2); Lq = rnd.choice(bycls[c1])
        V, Pp, Q = even(Lv), odd(Lp), even(Lq)
        t1, T0, c2 = Lp[0] - Lv[0], 2 * Lv[2] + 1, Lq[1] - Lv[1]
        N = ncl(Lq) - ncl(Lv)
        if dot(sub(Pp, V), sub(Q, V)) != 2 * (c2 * (2 * D * t1 - T0) - 8 * u * t1 * N): bad += 1
        # B1: A, C in c0 (A even, C odd); B, D in c1 (B even, D odd)
        La, Lc = Lv, Lp; Lb = Lq; Ld = rnd.choice(bycls[c1])
        Aa, Bb, Cc, Dd = even(La), even(Lb), odd(Lc), odd(Ld)
        U = sub(Bb, Aa); twon = (Cc[0] + Dd[0] - Aa[0] - Bb[0], Cc[1] + Dd[1] - Aa[1] - Bb[1])
        Sig = (Lc[0] - La[0]) + (Ld[0] - Lb[0]); S = La[2] + Lb[2] + 1; DjB = Lb[1] - La[1]
        Dn = ncl(Lb) - ncl(La)
        if dot(U, twon) != 4 * (DjB * (D * Sig - S) - 4 * u * Sig * Dn): bad += 1
        # L-adic (i): G - V for two even points equals (4(u Dj - Dn), 2 Dj)
        if sub(even(Lq), even(Lv)) != (4 * (u * c2 - N), 2 * c2): bad += 1
    res['bad'] = bad
    res['l'], res['p'], res['labels'] = l, p, len(labels)
    return res

if __name__ == '__main__':
    for (h, u, seed) in [(1001, 3, 1), (1500, 3, 2), (1201, 5, 3), (2003, 9, 4)]:
        print(h, u, run(h, u, seed)); sys.stdout.flush()
