"""Sanity check: Lemma F incident weight per label, class P (Q=1) versus
congruence-restricted lists (x = s1 a mod p1, x = s2 b mod p2), m = 7.
Labels f_{T,i}: odd row a = 2i+1, even row b = 2i+T+1, T in Ts.
Weight of e = sum over partners f, parities, Pythagorean offsets X (X = 0 mod 7)
of P(x_f - x_e = X), exact for i.i.d. uniform slots on the lists.
u+- emptiness and block membership of u+- are ignored (all other slots empty)."""
import sys, math, random

def pyth_offsets(H, Xmax):
    # for each even y in 1..H, list of X>0 with X^2+y^2 square, X<=Xmax
    res = {}
    for y in range(2, H + 1, 2):
        y2 = y * y
        out = []
        d = 1
        while d * d < y2:
            if y2 % d == 0:
                e = y2 // d
                if (e - d) % 2 == 0:
                    X = (e - d) // 2
                    if X <= Xmax:
                        out.append(X)
            d += 1
        res[y] = out
    return res

def count_res(lo, hi, r, Q):
    # number of j in [lo,hi) with j = r mod Q
    if hi <= lo:
        return 0
    def upto(n):  # j in [0,n)
        if n <= 0:
            return 0
        return (n - 1 - r) // Q + 1 if n - 1 >= r else 0
    return upto(hi) - upto(lo) if lo >= 0 else None

def run(h, N, Ts, primes, svals, samples, seed=1):
    m = 7
    Q = 1
    for p in primes:
        Q *= p
    inv7 = {p: pow(7, -1, p) for p in primes}
    labels = []
    for T in Ts:
        for i in range(0, (h - T) // 2):
            labels.append((2 * i + 1, 2 * i + T + 1))
    def psi(lab):
        # slot index residue mod Q via CRT
        if Q == 1:
            return 0
        a, b = lab
        rs = []
        rows = [a, b]
        for k, p in enumerate(primes):
            rs.append((svals[k] * rows[k] * inv7[p]) % p)
        # CRT
        r = 0
        for k, p in enumerate(primes):
            Mk = Q // p
            r += rs[k] * Mk * pow(Mk, -1, p)
        return r % Q
    sizes = {}
    ps = {}
    for lab in labels:
        r = psi(lab)
        ps[lab] = r
        sizes[r] = sizes.get(r, 0) + 0
    Lsize = {}
    for r in set(ps.values()):
        Lsize[r] = count_res(0, N, r, Q)
    py = pyth_offsets(h, m * N)
    random.seed(seed)
    samp = random.sample(labels, samples)
    tot = 0.0
    for e in samp:
        re = ps[e]
        w = 0.0
        for f in labels:
            if f == e:
                continue
            rf = ps[f]
            for par in (0, 1):
                y = f[par] - e[par]
                if y == 0:
                    continue
                for X in py[abs(y)]:
                    if X % m:
                        continue
                    for sgn in (1, -1):
                        d = sgn * X // m
                        if (d - (rf - re)) % Q:
                            continue
                        lo = max(0, -d)
                        hi = min(N, N - d)
                        c = count_res(lo, hi, re, Q)
                        w += c / (Lsize[re] * Lsize[rf])
        tot += w
    return tot / samples

if __name__ == "__main__":
    h = int(sys.argv[1]); N = int(sys.argv[2])
    Ts = [2, 6, 10]
    for primes, svals in [((), ()), ((3, 5), (1, 1)), ((11, 13), (1, 1))]:
        w = run(h, N, Ts, list(primes), list(svals), 12)
        print(primes, "avg Lemma F weight per label:", round(w, 5))
