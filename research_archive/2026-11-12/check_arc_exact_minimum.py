"""Find the exact minimum arc count for specified finite gap sets.

An infeasible M is certified by an overlapping chain of open rational
intervals that covers [0, 1/2]. Reflection covers the other half-circle.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path


def feasible_rotation(gaps, M):
    if not gaps:
        return Fraction(0), []
    intervals = []
    for d in gaps:
        for k in range(d // 2 + 1):
            intervals.append((Fraction(k * M - 1, M * d),
                              Fraction(k * M + 1, M * d), d, k))
    intervals.sort()
    right = Fraction(0)
    chain = []
    for left, endpoint, d, k in intervals:
        if left >= right:
            assert all(min((right * a) % 1, (-right * a) % 1) >= Fraction(1, M)
                       for a in gaps)
            return right, []
        if endpoint > right:
            right = endpoint
            chain.append([d, k])
        if right > Fraction(1, 2):
            # Independently replay the covering certificate.
            bound = Fraction(0)
            for dd, kk in chain:
                ll = Fraction(kk * M - 1, M * dd)
                rr = Fraction(kk * M + 1, M * dd)
                assert ll < bound < rr
                bound = rr
            assert bound > Fraction(1, 2)
            return None, chain
    assert all(min((right * a) % 1, (-right * a) % 1) >= Fraction(1, M)
               for a in gaps)
    return right, []


def main():
    p = argparse.ArgumentParser()
    p.add_argument("certificate", type=Path)
    p.add_argument("--at-least", type=int, default=10)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    cert = json.loads(args.certificate.read_text())
    results = []
    cache = {}
    for row in cert["classes"]:
        if row["M"] < args.at_least:
            continue
        gaps = tuple(row["blocked"])
        if gaps not in cache:
            for M in range(2, row["M"] + 1):
                theta, chain = feasible_rotation(gaps, M)
                if theta is not None:
                    # Infeasibility is monotone: failure at M-1 implies failure below it.
                    previous_chain = feasible_rotation(gaps, M - 1)[1] if M > 2 else []
                    cache[gaps] = {"least_M": M, "a": theta.numerator, "q": theta.denominator,
                                   "infeasible_previous_M": M - 1,
                                   "covering_chain_for_previous_M": previous_chain}
                    break
            assert gaps in cache
        result = {"s": row["s"], "T": 2 * row["s"] + 1, "producer_M": row["M"],
                  "blocked": list(gaps), **cache[gaps]}
        results.append(result)
        print(json.dumps({k: result[k] for k in ("T", "producer_M", "least_M", "a", "q")}), flush=True)
    args.out.write_text(json.dumps({"h": cert["h"], "results": results}, indent=2) + "\n")


if __name__ == "__main__":
    main()
