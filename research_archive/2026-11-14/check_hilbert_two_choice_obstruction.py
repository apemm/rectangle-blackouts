"""Check the five-label obstruction with integer geometry and all 32 bits."""
import itertools
import json
import math


def point(q, rank):
    if q == 1:
        return (0, 0)
    n = q // 2
    quadrant, r = divmod(rank, n * n)
    x, y = point(n, r)
    return ((y, x), (x, y + n), (x + n, y + n),
            (2 * n - 1 - y, n - 1 - x))[quadrant]


def rank(q, x, y):
    if q == 1:
        return 0
    n = q // 2
    if x < n and y < n:
        return rank(n, y, x)
    if x < n:
        return n * n + rank(n, x, y - n)
    if y >= n:
        return 2 * n * n + rank(n, x - n, y - n)
    return 3 * n * n + rank(n, n - 1 - y, 2 * n - 1 - x)


def is_rectangle(points):
    if len(set(points)) != 4:
        return False
    a, b, c, d = points
    return (a[0] + c[0] == b[0] + d[0]
            and a[1] + c[1] == b[1] + d[1]
            and (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
            == (b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2)


def main():
    labels = {"A": (295029, (132, 651)), "C": (295046, (139, 649)),
              "D": (295047, (138, 649)), "E": (295048, (138, 650)),
              "H": (295065, (138, 655))}
    edges = [("A", "C", 1, False), ("A", "D", -1, False),
             ("C", "D", 0, True), ("D", "E", 0, True),
             ("D", "H", -1, False), ("E", "H", 1, False)]
    for r, xy in labels.values():
        assert point(1024, r) == xy
        assert rank(1024, *xy) == r
    geometry_cases = 0
    for left, right, delta, reversed_parity in edges:
        lr, (li, lj) = labels[left]
        rr, (ri, rj) = labels[right]
        y1, y2 = ((2 * lj + 2, 2 * ri + 1) if reversed_parity
                  else (2 * li + 1, 2 * rj + 2))
        for bit_left in (0, 1):
            bit_right = bit_left + delta
            if bit_right not in (0, 1):
                continue
            x1, x2 = 32 * (2 * lr + bit_left), 32 * (2 * rr + bit_right)
            length_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
            L = math.isqrt(length_sq)
            assert L * L == length_sq
            assert (x1 + x2) % 2 == 0 and (y1 + y2 - L) % 2 == 0
            mx = (x1 + x2) // 2
            lo, hi = (y1 + y2 - L) // 2, (y1 + y2 + L) // 2
            assert 1 <= lo < hi <= 2048 and lo % 2 != hi % 2
            P, Q = (mx, lo), (mx, hi)
            C, D = (x1, y1), (x2, y2)
            assert is_rectangle([C, P, D, Q])
            odd, even = (lo, hi) if lo % 2 else (hi, lo)
            owner = rank(1024, (odd - 1) // 2, (even - 2) // 2)
            for owner_bit in (0, 1):
                ox = 32 * (2 * owner + owner_bit)
                assert ox != mx
                R, S = (ox, lo), (ox, hi)
                assert is_rectangle([R, P, Q, S])
                assert set([C, P, D, Q]) ^ set([R, P, Q, S]) == {C, D, R, S}
                geometry_cases += 1
    minimum_hits = len(edges)
    for values in itertools.product((0, 1), repeat=5):
        bits = dict(zip(labels, values))
        hit = sum(bits[right] - bits[left] == delta for left, right, delta, _ in edges)
        assert hit >= 1
        minimum_hits = min(minimum_hits, hit)
    for q in (1024, 2048, 4096):
        for r, xy in labels.values():
            # One diagonal identity embedding per doubling.
            old_q, rr, xx, yy = 1024, r, xy[0], xy[1]
            while old_q < q:
                rr += 2 * old_q * old_q
                xx += old_q
                yy += old_q
                old_q *= 2
            assert point(q, rr) == (xx, yy)
    print(json.dumps({"status": "PASS", "binary_assignments": 32,
                      "geometry_cases": geometry_cases,
                      "minimum_forbidden_edges": minimum_hits,
                      "embedding_sides_checked": [1024, 2048, 4096]}))


if __name__ == "__main__":
    main()
