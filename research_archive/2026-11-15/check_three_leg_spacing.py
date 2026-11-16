"""Two independent exact enumerations below the three-leg cutoff.

The theorem reduces three legs in a width-128 interval to odd Y<4096.
Divisors and primitive Euclid triples independently enumerate every leg
divisible by 32 in this finite range, without a hypotenuse cutoff.
"""
import json
import math
from pathlib import Path


def divisor_vectors(bound=4096, stride=32):
    vectors = set()
    for y in range(1, bound, 2):
        for a in range(1, y, 2):
            if y * y % a:
                continue
            x = (y * y // a - a) // 2
            if x % stride == 0:
                vectors.add((y, x // stride))
    return vectors


def euclid_vectors(bound=4096, stride=32):
    vectors = set()
    # y0=m^2-n^2>=2m-1, and the multiplier is a positive odd integer.
    for m in range(2, (bound + 1) // 2 + 1):
        for n in range(m - 1, 0, -1):
            y0 = m * m - n * n
            if y0 >= bound:
                break
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            x0 = 2 * m * n
            for k in range(1, (bound - 1) // y0 + 1, 2):
                x = k * x0
                if x % stride == 0:
                    vectors.add((k * y0, x // stride))
    return vectors


def main():
    first, second = divisor_vectors(), euclid_vectors()
    assert first == second, (first - second, second - first)
    grouped = {}
    for y, q in sorted(first):
        grouped.setdefault(y, []).append(q)
    pairs, triples = [], []
    for y, qs in grouped.items():
        pairs.extend((y, qs[k:k + 2]) for k in range(len(qs) - 1)
                     if qs[k + 1] - qs[k] <= 4)
        triples.extend((y, qs[k:k + 3]) for k in range(len(qs) - 2)
                       if qs[k + 2] - qs[k] <= 4)
    assert not triples
    result = {"status": "PASS", "stride": 32, "odd_y_upper_exclusive": 4096,
              "odd_y_tested": 2048, "vectors": len(first),
              "independent_enumerations_agree": True,
              "pairs_in_q_span_at_most_four": pairs,
              "triples_in_q_span_at_most_four": triples}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
