"""Finite permutation witnesses for all classified intrinsic P systems."""
from pathlib import Path
import json
from math import isqrt

MODULAR_CYCLE = [0, 6, 7, 2, 3, 11, 1, 9, 13, 14, 4, 8, 12, 5, 10, 15]


def compatible(a, b, delta):
    i, j = divmod(a, 4)
    k, ell = divmod(b, 4)
    return ell - i != delta and j - k != delta


def valid(word, constraints):
    return sorted(word) == list(range(16)) and all(
        compatible(word[r], word[r + gap], delta)
        for gap, delta in constraints for r in range(16 - gap))


def find_word(constraints):
    nodes = 0
    word = []

    def search(unused):
        nonlocal nodes
        nodes += 1
        assert nodes < 1000000, "This finite check is intentionally bounded."
        if not unused:
            return word[:]
        for x in unused:
            if all(len(word) < gap or compatible(word[-gap], x, delta)
                   for gap, delta in constraints):
                word.append(x)
                result = search(tuple(y for y in unused if y != x))
                if result is not None:
                    return result
                word.pop()
        return None

    result = search(tuple(range(16)))
    assert result is not None and valid(result, constraints)
    return result, nodes


def transpose(word):
    return [4 * (x % 4) + x // 4 for x in word]


def fill_chains(word, q):
    result = [None] * 16
    index = 0
    for start in range(q):
        for slot in range(start, 16, q):
            result[slot] = word[index]
            index += 1
    return result


def arithmetic_patterns(S, D):
    patterns = {}
    for q in range(1, 16):
        N = (S * q // 2) ** 2
        odd = N
        while odd % 2 == 0:
            odd //= 2
        divisors = set()
        for a in range(1, isqrt(odd) + 1):
            if odd % a == 0:
                divisors.update((a, odd // a))
        for a in divisors:
            Y = abs(N // a - a)
            assert Y % 2 and (S * q) ** 2 + Y * Y == (N // a + a) ** 2
            for sign in (-1, 1):
                numerator = sign * Y - (D - 1)
                if numerator % D:
                    continue
                target = numerator // D
                for delta in range(-3, 4):
                    T = target - delta
                    patterns.setdefault(T, set()).add((q, delta))
    return patterns


def repair(pattern, singles, doubles, h7_word, h7_tail_words, D):
    pattern = sorted(pattern)
    if len(pattern) == 1:
        q, delta = pattern[0]
        word = singles[str(abs(delta))]["word"]
        if delta < 0:
            word = transpose(word)
        return fill_chains(word, q)
    assert len(pattern) == 2, pattern
    if D == 28:
        if pattern == [(1, 3), (13, -3)]:
            return h7_word
        (q, delta), (q2, delta2) = pattern
        assert (q, q2) == (13, 15) and delta2 == delta - 2 and -1 <= delta <= 3
        return h7_tail_words[str(delta)]["word"]
    (q, delta), (q3, delta3) = pattern
    assert q3 == 3 * q and abs(delta) in (1, 2, 3)
    assert delta3 == delta - (4 if delta > 0 else -4)
    word = doubles[str(abs(delta))]["word"]
    if delta < 0:
        word = transpose(word)
    return fill_chains(word, q)


def main():
    for r, x in enumerate(MODULAR_CYCLE):
        y = MODULAR_CYCLE[(r + 1) % 16]
        assert (y % 4 - x // 4) % 4 and (x % 4 - y // 4) % 4
    for delta in range(-3, 4):
        shifted = [4 * (x // 4) + (x % 4 + delta) % 4 for x in MODULAR_CYCLE]
        for q in range(1, 16):
            assert valid(fill_chains(shifted, q), [(q, delta)])
    singles = {}
    doubles = {}
    for delta in range(4):
        word, nodes = find_word([(1, delta)])
        singles[str(delta)] = {"word": word, "search_nodes": nodes}
        for q in range(1, 16):
            assert valid(fill_chains(word, q), [(q, delta)])
            assert valid(fill_chains(transpose(word), q), [(q, -delta)])
    for delta in (1, 2, 3):
        word, nodes = find_word([(1, delta), (3, delta - 4)])
        doubles[str(delta)] = {"word": word, "search_nodes": nodes}
        for q in range(1, 6):
            assert valid(fill_chains(word, q), [(q, delta), (3 * q, delta - 4)])
            assert valid(fill_chains(transpose(word), q), [(q, -delta), (3 * q, 4 - delta)])
    h7_word, nodes = find_word([(1, 3), (13, -3)])
    h7_tail_words = {}
    for delta in range(-1, 4):
        word, count = find_word([(13, delta), (15, delta - 2)])
        h7_tail_words[str(delta)] = {"word": word, "search_nodes": count}
    audits = []
    for S, D in ((1024, 2), (2048, 2), (6272 * 16, 28), (6272 * 32, 28)):
        patterns = arithmetic_patterns(S, D)
        for T, pattern in patterns.items():
            assert valid(repair(pattern, singles, doubles, h7_word, h7_tail_words, D), pattern)
            if T % 4 == 0 and len(pattern) == 2:
                pairs = sorted(pattern)
                if D == 2:
                    (q, delta), (q3, delta3) = pairs
                    assert q3 == 3 * q and (delta, delta3) == (3, -1)
                else:
                    assert pairs in ([(1, 3), (13, -3)], [(13, 1), (15, -1)])
        audits.append({"S": S, "D": D, "offsets_checked": len(patterns),
                       "double_offsets": sum(len(p) == 2 for p in patterns.values()),
                       "aligned_offsets": sum(T % 4 == 0 for T in patterns),
                       "aligned_double_offsets": sum(T % 4 == 0 and len(p) == 2 for T, p in patterns.items()),
                       "max_constraints": max(map(len, patterns.values()))})
    result = {"status": "PASS", "modular_cycle": MODULAR_CYCLE,
              "single_gap_words": singles,
              "two_gap_words": doubles,
              "h7_word": {"word": h7_word, "search_nodes": nodes},
              "h7_tail_words": h7_tail_words,
              "arithmetic_audits": audits}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
