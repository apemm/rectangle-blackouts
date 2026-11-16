"""Search type-A / type-B atoms that are actual factor-one conflicts under explicit rules."""
import itertools
import math
from atoms import build_A, build_B, check_conflict, digits_to_rank, point

S, M = 32, 3


def popc(r):
    return bin(r).count("1")


def dsum(r, b):
    s = 0
    while r:
        s += r % b
        r //= b
    return s


def gray(r):
    return r ^ (r >> 1)


RULES = {
    "popcount(r) mod M (= sum_k floor(r/2^k) mod 2, summed)": lambda r, i, j: popc(r) % M,
    "sum_k floor(r/2^k) mod M": lambda r, i, j: (2 * r - popc(r)) % M,
    "base-4 digit sum mod M": lambda r, i, j: dsum(r, 4) % M,
    "r mod M": lambda r, i, j: r % M,
    "floor(r/M) mod M": lambda r, i, j: (r // M) % M,
    "base-M digit sum mod M": lambda r, i, j: dsum(r, M) % M,
    "Gray(r) mod M": lambda r, i, j: gray(r) % M,
    "popcount(Gray(r)) mod M": lambda r, i, j: popc(gray(r)) % M,
    "(i + j + r) mod M": lambda r, i, j: (i + j + r) % M,
    "(T + popcount r) mod M": lambda r, i, j: (j - i + popc(r)) % M,
    "floor(r / w(T)) mod M, w = factor-one rank gap": None,  # filled below
}


def w_of_T(T):
    # factor-one candidate gap q ~ sqrt(8(|T|+1))/S ; rank gap q/M
    q = math.isqrt(max(1, 8 * (abs(T) + 1))) // S
    return max(1, q // M)


RULES["floor(r / w(T)) mod M, w = factor-one rank gap"] = lambda r, i, j: (r // w_of_T(j - i)) % M


def atoms():
    out = []
    for lo in (1, 2, 3):
        for hi in range(lo, lo + 6):
            for size in range(1, hi - lo + 2):
                for K in itertools.combinations(range(lo, hi + 1), size):
                    if K[0] != lo:
                        continue
                    D = sum(4 ** k for k in K)
                    N0 = S * S * M * M * D * D // 8
                    if ((N0 & -N0).bit_length() - 1) < hi + 2:
                        continue
                    n = N0.bit_length() + 5
                    if n > 60:
                        continue
                    out.append(("A", K, lo, hi, n))
    for kb in (1, 2, 3, 4):
        for kt in range(kb + 1, kb + 9, 2):
            out.append(("B", (kb, kt), None, None, None))
    return out


def main():
    cand = atoms()
    built = []
    for typ, K, lo, hi, n in cand:
        if typ == "A":
            dig, digf, D, N0 = build_A(S, M, list(K), lo, hi, n)
        else:
            kb, kt = K
            D = 2 * sum(4 ** k for k in range(kb, kt + 1))
            N0 = S * S * M * M * D * D // 8
            if ((N0 & -N0).bit_length() - 1) < kt + 2:
                continue
            n = N0.bit_length() + 5
            dig, digf, D, N0 = build_B(S, M, kb, kt, n)
        Q = 2 ** n
        re, rf = digits_to_rank(dig), digits_to_rank(digf)
        built.append((typ, K, n, dig, digf, re, rf, point(Q, re), point(Q, rf)))
    print("atoms built:", len(built))
    for name, rule in RULES.items():
        found = None
        for typ, K, n, dig, digf, re, rf, e, f in built:
            xe, xf = rule(re, *e), rule(rf, *f)
            if xe == xf:
                res = check_conflict(S, M, dig, digf, xe, xf, n, 2 ** (n + 1))
                assert res["witness"], (name, K)
                found = (typ, K, n + 1, xe)
                break
        print(f"{name:52s} -> {'CONFLICT at type %s K=%s h=2^%d xi=%d' % found if found else 'no atom conflict found'}")


if __name__ == "__main__":
    main()
