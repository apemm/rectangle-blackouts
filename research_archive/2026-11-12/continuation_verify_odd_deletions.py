"""Independent signed-coefficient recurrence for the retained certificates."""
import argparse
import itertools
import json
import math
from functools import reduce
from pathlib import Path

from continuation_odd_relation_deletions import (
    all_gaps, degree, odd_relation, verify_result)


def signed_dp_has_odd(ds, m):
    if not ds:
        return False
    g = reduce(math.gcd, ds)
    ds = [d//g for d in ds]
    radius = m*sum(ds)
    mask = (1 << (2*radius+1))-1
    even, odd = 1 << radius, 0
    for d in ds:
        new_even = new_odd = 0
        for coefficient in range(-m, m+1):
            shift = coefficient*d
            e, o = (odd, even) if coefficient % 2 else (even, odd)
            if shift < 0:
                new_even |= e >> -shift
                new_odd |= o >> -shift
            else:
                new_even |= e << shift
                new_odd |= o << shift
        even, odd = new_even & mask, new_odd & mask
    return bool((odd >> radius) & 1)


def small_checks():
    tested = 0
    for k in range(1, 5):
        for ds in itertools.combinations(range(1, 9), k):
            for m in (1, 2, 3):
                direct = any(sum(c) % 2 and sum(a*b for a, b in zip(c, ds)) == 0
                             for c in itertools.product(range(-m, m+1), repeat=k))
                assert direct == signed_dp_has_odd(ds, m)
                assert direct == (odd_relation(ds, m) is not None)
                tested += 1
    for h in range(4, 81):
        A, K = (h+1)//2, h//2
        generated = all_gaps(h)
        for T, ds in generated.items():
            s = (T-1)//2
            n = min(A, K-s)-max(0, -s)
            brute = set()
            for d in range(1-n, n):
                if not d:
                    continue
                norm = 20*d*d+4*T*d+T*T
                hyp = math.isqrt(norm)
                if hyp < h and hyp*hyp == norm:
                    brute.add(abs(d))
            assert list(ds) == sorted(brute)
    return tested


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificates", nargs="+")
    args = parser.parse_args()
    direct_cases = small_checks()
    results = []
    for name in args.certificates:
        data = json.loads(Path(name).read_text(encoding="utf-8"))
        verify_result(data)
        for row in data["diagonals"]:
            assert row["m"] == degree(len(row["retained"]))
            assert not signed_dp_has_odd(row["retained"], row["m"])
        results.append(dict(h=data["h"], certificate=Path(name).name,
                            checked_diagonals=len(data["diagonals"]),
                            deleted=data["total_deleted"], status="PASS"))
        print(json.dumps(results[-1]), flush=True)
    result = dict(brute_force_dp_cases=direct_cases,
                  brute_force_gap_heights=[4,80],
                  independent_signed_dp_results=results)
    Path("odd_relation_deletion_independent_check.json").write_text(
        json.dumps(result, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
