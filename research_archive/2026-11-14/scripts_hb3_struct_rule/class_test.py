"""Random members of the rule classes of Theorems A, B and Corollary A3, with K chosen
by the zero-sum arguments of the proofs (not by search); each must give an actual conflict."""
import random
import hashlib
from atoms import build_A, build_B, check_conflict, digits_to_rank, point

S, M = 32, 3
rnd = random.Random(2026)


def hsh(*a):
    return int(hashlib.sha256(repr(a).encode()).hexdigest(), 16)


def prefix_zero_block(incs, mod_tuple, step=1):
    """indices t<t' with equal prefix sums (over blocks of `step` consecutive elements)."""
    seen = {}
    s = tuple(0 for _ in mod_tuple)
    seen[s] = 0
    t = 0
    for start in range(0, len(incs) - step + 1, step):
        for g in incs[start:start + step]:
            s = tuple((a + b) % m for a, b, m in zip(s, g, mod_tuple))
        t += 1
        if s in seen:
            return seen[s] * step, t * step
        seen[s] = t
    return None


def theorem_A_trial(m, P, trial):
    # rule: xi = F(1/2-merged digits outside, sum gamma_l(d_l) mod m, r mod P, j mod P)
    gam = {}
    def gamma(l, d):
        if (l, d) not in gam:
            gam[(l, d)] = rnd.randrange(m)
        return gam[(l, d)]
    seed = rnd.randrange(10 ** 9)
    def rule(dig, r, i, j):
        merged = tuple('*' if d in (1, 2) else d for d in dig)
        stat = sum(gamma(l, d) for l, d in enumerate(dig)) % m
        return hsh(seed, merged, stat, r % P, j % P) % M
    N = m * P * P
    lam = max(1, -(-(N + 2) // 3))
    Lam = list(range(lam, lam + N))
    incs = [((gamma(k, 1) - gamma(k, 2)) % m, (4 ** k) % P, (2 ** k) % P) for k in Lam]
    blk = prefix_zero_block(incs, (m, P, P))
    assert blk is not None
    K = Lam[blk[0]:blk[1]]
    lo, hi = K[0], K[-1]
    D = sum(4 ** k for k in K)
    N0 = S * S * M * M * D * D // 8
    n = N0.bit_length() + 5
    dig, digf, D, N0 = build_A(S, M, K, lo, hi, n)
    Q = 2 ** n
    re, rf = digits_to_rank(dig), digits_to_rank(digf)
    e, f = point(Q, re), point(Q, rf)
    xe, xf = rule(dig, re, *e), rule(digf, rf, *f)
    assert xe == xf, "rule distinguishes atom"
    res = check_conflict(S, M, dig, digf, xe, xf, n, 2 ** (n + 1))
    assert res["witness"]
    return K, n + 1


def theorem_B_trial(m, P, trial):
    # rule: xi = F(T exactly, 0/2-merged digits, sum gamma_l(d_l) mod m, r mod P, i mod P, j mod P)
    gam = {}
    def gamma(l, d):
        if (l, d) not in gam:
            gam[(l, d)] = rnd.randrange(m)
        return gam[(l, d)]
    seed = rnd.randrange(10 ** 9)
    def rule(dig, r, i, j):
        merged = tuple(0 if d in (0, 2) else d for d in dig)
        stat = sum(gamma(l, d) for l, d in enumerate(dig)) % m
        return hsh(seed, j - i, merged, stat, r % P, i % P, j % P) % M
    N = m * P * P
    lam = max(1, -(-(2 * N) // 3))
    Lam = list(range(lam, lam + 2 * N))
    incs = [((gamma(k, 2) - gamma(k, 0)) % m, (2 * 4 ** k) % P, (2 ** k) % P) for k in Lam]
    blk = prefix_zero_block(incs, (m, P, P), step=2)
    assert blk is not None
    kb, kt = Lam[blk[0]], Lam[blk[1] - 1]
    D = 2 * sum(4 ** k for k in range(kb, kt + 1))
    N0 = S * S * M * M * D * D // 8
    n = N0.bit_length() + 5
    dig, digf, D, N0 = build_B(S, M, kb, kt, n)
    Q = 2 ** n
    re, rf = digits_to_rank(dig), digits_to_rank(digf)
    e, f = point(Q, re), point(Q, rf)
    xe, xf = rule(dig, re, *e), rule(digf, rf, *f)
    assert xe == xf, "rule distinguishes atom"
    res = check_conflict(S, M, dig, digf, xe, xf, n, 2 ** (n + 1))
    assert res["witness"]
    return (kb, kt), n + 1


# nonabelian level-independent automaton over S_3 (permutations of 3 points)
def compose(p, q):
    return tuple(p[q[x]] for x in range(3))


def corollary_A3_trial(trial):
    perms = [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 1, 0), (1, 2, 0), (2, 0, 1)]
    gam = {d: rnd.choice(perms) for d in range(4)}
    seed = rnd.randrange(10 ** 9)
    def rule(dig, r, i, j):
        p = (0, 1, 2)
        for d in reversed(dig):  # top-down product
            p = compose(p, gam[d])
        merged = tuple('*' if d in (1, 2) else d for d in dig)
        return hsh(seed, p, merged) % M
    m = 6  # exponent of S_3
    k0 = -(-(2 * m + 1) // 3)
    K = [k0 + 2 * t for t in range(m)]
    lo, hi = K[0], K[-1]
    D = sum(4 ** k for k in K)
    N0 = S * S * M * M * D * D // 8
    n = N0.bit_length() + 5
    dig, digf, D, N0 = build_A(S, M, K, lo, hi, n)
    Q = 2 ** n
    re, rf = digits_to_rank(dig), digits_to_rank(digf)
    e, f = point(Q, re), point(Q, rf)
    xe, xf = rule(dig, re, *e), rule(digf, rf, *f)
    assert xe == xf
    res = check_conflict(S, M, dig, digf, xe, xf, n, 2 ** (n + 1))
    assert res["witness"]
    return K, n + 1


if __name__ == "__main__":
    for m, P in ((1, 1), (2, 1), (3, 1), (5, 1), (3, 2), (2, 3)):
        for t in range(3):
            K, hb = theorem_A_trial(m, P, t)
        print("Theorem A class, |G| =", m, "P =", P, ": 3 random rules all conflict; last K", K, "h=2^%d" % hb)
    for m, P in ((1, 1), (2, 1), (3, 1), (2, 2)):
        for t in range(3):
            K, hb = theorem_B_trial(m, P, t)
        print("Theorem B class, |G| =", m, "P =", P, ": 3 random T-aware rules all conflict; last K", K, "h=2^%d" % hb)
    for t in range(5):
        K, hb = corollary_A3_trial(t)
    print("S_3 automaton rules: 5 random rules all conflict; K", K, "h=2^%d" % hb)
    print("ALL PASS")
