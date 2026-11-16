"""Sanity check of Lemma U1 (position facts of rule (B5)) for random class data Xi.

For random h, random admissible (l, p), random kappa, b, random partition of the
labels of one type tau = (iota, sigma) into subclasses with arbitrary distinct
indices k, check:
 (a) Dn = Ds - p Dt = 0 (mod 16 l) for any two labels; Dt = 0 iff same subclass iff Dn = 0;
 (b) slot -> label is injective (a slot holds at most one label);
 (c) odd-odd: Dx/4 - Dy/2 = p Dt; even-even: Dx/4 - Dy/2 = -Dn.
"""
import random, sys

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def run(h, rng):
    A, K = (h + 1) // 2, h // 2
    Ls = [l for l in range(int(1.04 * h) + 1, int(2.08 * h) + 1) if isprime(l) and l % 5 in (2, 3)]
    Ps = [p for p in range(40 * h + 1, 80 * h + 1) if isprime(p) and p % 20 in (3, 7)]
    l, p = rng.choice(Ls), rng.choice(Ps)
    kappa, b = rng.randrange(-1000, 1000), rng.randrange(0, 1000)
    iota, sigma = rng.randrange(32), rng.randrange(16)
    M = 16 * l
    pinv = pow(p, -1, M)
    labels = [(i, j) for i in range(A) for j in range(K) if i % 32 == iota and (j - i) % 16 == sigma]
    # random partition into subclasses per diagonal, arbitrary distinct indices k
    sub = {}
    bydiag = {}
    for (i, j) in labels:
        bydiag.setdefault(j - i, []).append((i, j))
    for s, labs in bydiag.items():
        nsub = rng.randint(1, max(1, len(labs)))
        ks = rng.sample(range(0, 3 * nsub + 5), nsub)
        for lab in labs:
            sub[lab] = (s, rng.choice(ks))
    pos = {}
    slots = {}
    for lab in labels:
        s, k = sub[lab]
        rho = (pinv * (s - kappa)) % M
        t = rho + M * k
        n = lab[0] + p * t + b
        assert n not in slots, "slot collision"
        slots[n] = lab
        pos[lab] = (t, n)
    labs = list(labels)
    bad = 0
    for _ in range(20000):
        L1, L2 = rng.choice(labs), rng.choice(labs)
        (s1, k1), (s2, k2) = sub[L1], sub[L2]
        t1, n1 = pos[L1]; t2, n2 = pos[L2]
        Dt, Ds = t2 - t1, s2 - s1
        Dn = Ds - p * Dt
        same = (s1, k1) == (s2, k2)
        if Dn % M != 0: bad += 1
        if (Dt == 0) != same or (Dn == 0) != same: bad += 1
        Dx = 4 * (n2 - n1)
        Dyo = 2 * (L2[0] - L1[0])
        Dye = 2 * (L2[1] - L1[1])
        if Dx // 4 - Dyo // 2 != p * Dt: bad += 1
        if Dx // 4 - Dye // 2 != -Dn: bad += 1
    return len(labels), len(Ls), len(Ps), bad

rng = random.Random(1)
tot = 0
for h in [101, 160, 257, 400]:
    for rep in range(3):
        nl, nL, nP, bad = run(h, rng)
        tot += bad
        print(h, rep, "labels", nl, "#L", nL, "#P", nP, "failures", bad)
print("total failures", tot)
