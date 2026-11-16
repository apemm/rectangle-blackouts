"""Sparse exact check of the four local recursive embedding identities."""
from pathlib import Path
import json


def size(n):
    return n * (n + 1) // 2


def point(n, r):
    assert 0 <= r < size(n)
    if n == 1:
        return 0, 0
    a, k = (n + 1) // 2, n // 2
    if r < size(a):
        x, y = point(a, r)
        return y, x
    r -= size(a)
    if r < size(k):
        x, y = point(k, r)
        return x, y + a
    r -= size(k)
    if r < size(a - 1):
        x, y = point(a - 1, r)
        return a - 1 - y, a - 1 - x
    r -= size(a - 1)
    x, y = point(k, r)
    return x + a, y


def rank_interval(n, address):
    start = 0
    for digit in address:
        a, k = (n + 1) // 2, n // 2
        sizes = (a, k, a - 1, k)
        start += sum(size(s) for s in sizes[:digit])
        n = sizes[digit]
        assert n >= 1
    return n, start


def main():
    checks = 0
    for n in range(2, 33):
        cases = [((0, 0, 0), lambda x, y: (y, x)),
                 ((0, 0, 1), lambda x, y: (x, y + n)),
                 ((0, 2, 0), lambda x, y: (2 * n - 1 - y, 2 * n - 1 - x)),
                 ((1, 2, 0), lambda x, y: (2 * n - 1 - x, 6 * n - 1 - y))]
        for parent in (8 * n, 8 * n - 1):
            for address, transform in cases:
                leaf_size, first = rank_interval(parent, address)
                assert leaf_size == n
                for r in range(size(n)):
                    assert point(parent, first + r) == transform(*point(n, r))
                    checks += 1
    result = {"status": "PASS", "n_min": 2, "n_max": 32,
              "addresses": ["000", "001", "020", "120"],
              "point_identities_checked": checks}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
