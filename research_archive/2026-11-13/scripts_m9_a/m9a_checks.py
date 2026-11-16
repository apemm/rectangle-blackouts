"""Sanity checks for the (M9)(a),(b),(d),(e),(f) audit at stride 4u.
Only identities and row/residue facts; no definition-level census."""
import itertools, random, math
from sympy import isprime, jacobi_symbol, divisors

random.seed(7)

# ---------- (e) filler window from Table J1* ----------
def kshift(h, row3, D0):
    # Table J1* (v4 (B6)); returns k_tau
    if h % 2 == 0:
        return 0
    if h % 4 == 1:
        if not row3:
            return 0
        return {40: 1, 48: 1, 56: 2}.get(D0, 0)
    # h = 3 mod 4
    if not row3:
        return 1 if D0 in (24, 32, 40, 48) else 0
    return {42: 1, 50: 1, 58: 2}.get(D0, 0)

worst = 0
for h in range(10**6, 10**6 + 128):
    for iota in range(32):
        yP = 2 * iota + 1
        row3 = (iota % 2 == 0)
        for Tmod4 in (1, 3):
            add = 32 if Tmod4 == 3 else 48
            T0 = max(y for y in range(h - 63, h + 1) if (y - yP - add) % 64 == 0)
            D0 = h - T0
            assert 0 <= D0 <= 63
            k = kshift(h, row3, D0)
            Ts = T0 - 64 * k
            worst = max(worst, h - Ts)
            for w in range(4):
                row = Ts - 24 + 8 * w
                assert h - 210 <= row <= h
                c = 1 if Tmod4 == 3 else 3
                assert (row - yP - 8 * (w + c)) % 64 == 0  # (C4)
print("(e) max h - T* over all h mod 128, types:", worst, "(claim <= 186)")
# 6 neighbours: multiples of 32 in (0, 210]
print("(e) multiples of 32 in (0,210]:", [d for d in range(32, 211, 32)])

# ---------- (b),(a) residues of deep rows in a type at stride 4u ----------
def primes_in(lo, hi, cond, n=3):
    out = []
    x = lo + 1
    while x <= hi and len(out) < n:
        if isprime(x) and cond(x):
            out.append(x)
        x += 1
    return out

for (h, u) in [(2001, 3), (1503, 5), (3001, 7)]:
    Delta = 4 * u * u + 1
    P = max(40, 8 * u * u + 4)
    A, K = (h + 1) // 2, h // 2
    l = primes_in(int(1.04 * h), int(2.08 * h), lambda q: jacobi_symbol(Delta, q) == -1)[0]
    p = primes_in(P * h, 2 * P * h, lambda q: q % 4 == 3 and jacobi_symbol(Delta, q) == -1)[0]
    pinv = pow(p, -1, 16 * l)
    kappa = random.randrange(16 * l)
    bad = 0
    for iota in random.sample(range(32), 6):
        for sigma in random.sample(range(16), 4):
            b = random.randrange(64)
            kap_tau = kappa - b
            rho_tau = (u * (iota + sigma) - kap_tau) % 16
            rho0 = rho_tau % 4
            yP = 2 * iota + 1
            # stride-4 phase for the same type with b' realising the same rho_tau
            bprime = (rho_tau - (iota + sigma - kappa)) % 16
            assert (iota + sigma - kappa + bprime) % 16 == rho_tau
            slots, oddrows, evenrows = set(), set(), set()
            for s in range(-K + 1, K):
                if s % 16 != sigma:
                    continue
                rho_s = (pinv * (u * s - kappa)) % (16 * l)
                for kc in range(2):
                    t = rho_s + 16 * l * kc
                    for i in range(iota, A, 32):
                        j = i + s
                        if not (0 <= j <= K - 1):
                            continue
                        n = u * i + p * t + b
                        if n % 16 != rho_tau:
                            bad += 1
                        if (n - u * j + kap_tau) % (16 * l) != 0:
                            bad += 1
                        oddrows.add((2 * i + 1) % 64)
                        evenrows.add((2 * j + 2) % 32)
            filler_mod8 = {(yP + 8 * (w + 1)) % 8 for w in range(4)} | {(yP + 8 * (w + 3)) % 8 for w in range(4)}
            if len(oddrows) > 1 or len(evenrows) > 1:
                bad += 1
            # all odd deep rows congruent mod 8 (labels and fillers)
            odd8 = {r % 8 for r in oddrows} | filler_mod8
            if len(odd8) != 1:
                bad += 1
            # row-3 types: odd deep rows 1 mod 4; row-1 types: 3 mod 4
            want = 1 if iota % 2 == 0 else 3
            if any(r % 4 != want for r in odd8):
                bad += 1
    print(f"(a,b) h={h} u={u} l={l} p={p}: failures = {bad}")

# ---------- (d) Proposition 3(b) by exact enumeration ----------
def check_prop3(nv, B, edges, trials):
    adj = {v: set() for v in range(nv)}
    for a, c in edges:
        adj[a].add(c); adj[c].add(a)
    d = max(len(adj[v]) for v in adj)
    cols = [c for c in itertools.product(range(B), repeat=nv)
            if all(c[a] != c[b] for a, b in edges)]
    worst = 0.0
    for x, y in itertools.combinations(range(nv), 2):
        if y in adj[x]:
            continue
        pr = sum(1 for c in cols if c[x] == c[y]) / len(cols)
        worst = max(worst, pr * (B - d))
    return d, worst

for trial in range(4):
    nv, B = 7, 5
    # random graph with max degree 2 (< B/2)
    edges = []
    deg = [0] * nv
    for a, c in itertools.combinations(range(nv), 2):
        if deg[a] < 2 and deg[c] < 2 and random.random() < 0.5:
            edges.append((a, c)); deg[a] += 1; deg[c] += 1
    d, w = check_prop3(nv, B, edges, trial)
    print(f"(d) nv={nv} B={B} maxdeg={d}: max P(mono)*(B-d) = {w:.4f} (claim <= 1)")

# ---------- (f) type-II triple count, exact vs bound ----------
worstratio = 0
for h in (60, 97):
    for Sigma in range(1, 4):
        for u in (3, 5):
            N0 = 16 * u * Sigma
            exact = sum(1 for H in range(-2 * h + 1, 2 * h) for U2 in range(-h + 1, h)
                        if (H * U2) % N0 == 0)
            per_d = sum((2 * h / d + 1) * (4 * h * d / N0 + 1) for d in divisors(N0))
            bound = len(divisors(N0)) * (8 * h * h / N0 + 7 * h)
            assert exact <= per_d <= bound, (h, Sigma, u, exact, per_d, bound)
            worstratio = max(worstratio, exact / bound)
print("(f) type-II count: exact <= sum_d (2h/d+1)(4hd/N0+1) <= tau(N0)(8h^2/N0+7h); max exact/bound =", round(worstratio, 3))

# I.2 gcd sum: sum over odd T0, |T0|<h, of gcd(2 Delta a + T0, u a) <= 3h tau(ua)
for u in (3, 5):
    Delta = 4 * u * u + 1
    h = 4001
    for a in range(1, 12):
        s = sum(math.gcd(2 * Delta * a + T0, u * a) for T0 in range(-h + 2, h, 2))
        assert s <= 3 * h * len(divisors(u * a)), (u, a, s)
print("(f) I.2 gcd sum bound holds for u in {3,5}, a < 12, h = 4001")
