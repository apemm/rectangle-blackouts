"""Evaluate the union inclusion-exclusion formula and check small grids independently."""
from collections import defaultdict
from itertools import combinations
import sys


def rectangles(h, m):
    diagonals = defaultdict(list)
    for p, q in combinations(range(h*m), 2):
        x, y = divmod(p, h)
        xx, yy = divmod(q, h)
        key = x + xx, y + yy, (x - xx)**2 + (y - yy)**2
        diagonals[key].append((1 << p) | (1 << q))
    return [a | b for group in diagonals.values() for a, b in combinations(group, 2)]


def leading_terms(h, m, rects):
    n = h*m
    edges = sorted({a ^ b for a, b in combinations(rects, 2)}, key=int.bit_count)
    minimal = []
    for e in edges:
        if not any((e & d) == d for d in minimal):
            minimal.append(e)
    weights = {0: 1}
    for edge in minimal:
        new = dict(weights)
        for u, value in weights.items():
            union = u | edge
            new[union] = new.get(union, 0) - value
        weights = {u: value for u, value in new.items() if value}
    by_size = defaultdict(int)
    for u, value in weights.items():
        by_size[u.bit_count()] += value
    base = 1 << (n + 1)
    encoded = sum(v * base**k * (1 + base)**(n - k) for k, v in by_size.items())
    f = (encoded.bit_length() - 1) // (n + 1)
    return f, encoded >> (f*(n + 1))


def exhaustive(h, m, rects):
    best = count = 0
    for black in range(1 << (h*m)):
        size = black.bit_count()
        if size < best or len({r & ~black for r in rects}) != len(rects):
            continue
        if size > best:
            best, count = size, 0
        count += 1
    return best, count


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        h, m = map(int, arg.split('x'))
        rects = rectangles(h, m)
        answer = leading_terms(h, m, rects)
        assert answer == exhaustive(h, m, rects)
        print(h, m, *answer, flush=True)
