"""Sparse exact verification of the actual three-edge Hilbert P obstruction."""
import itertools
import json
import math
from check_hilbert_two_choice_obstruction import point, rank, is_rectangle


def main():
    q = 2048
    labels = [(1331100, (187, 1549)), (1331133, (190, 1545)),
              (1331166, (187, 1541))]
    cases = []
    for level in range(3):
        h = 2 * q

        def black(p):
            x, row = p
            if x % 32 or not 0 <= x // 32 < q * q:
                return False
            i, j = point(q, x // 32)
            return row in (2 * i + 1, 2 * j + 2)

        for r, xy in labels:
            assert point(q, r) == xy and rank(q, *xy) == r
        for (r, (i, j)), (s, (k, ell)) in itertools.combinations(labels, 2):
            witnesses = []
            for a, b in ((2 * i + 1, 2 * ell + 2), (2 * j + 2, 2 * k + 1)):
                X = 32 * (s - r)
                L = math.isqrt(X * X + (a - b) ** 2)
                if L * L != X * X + (a - b) ** 2:
                    continue
                low, high = (a + b - L) // 2, (a + b + L) // 2
                if not 1 <= low < high <= h:
                    continue
                assert (a + b - L) % 2 == 0
                mx = 16 * (r + s)
                C, D = (32 * r, a), (32 * s, b)
                P, Q = (mx, low), (mx, high)
                odd, even = (low, high) if low % 2 else (high, low)
                owner = rank(q, (odd - 1) // 2, (even - 2) // 2)
                U, V = (32 * owner, low), (32 * owner, high)
                tilted, axis = (C, P, D, Q), (U, P, Q, V)
                assert is_rectangle(tilted) and is_rectangle(axis)
                assert {p for p in tilted if not black(p)} == {p for p in axis if not black(p)}
                assert set(tilted) != set(axis)
                witnesses.append({"rows": [a, b], "X": X, "L": L,
                                  "completion": [low, high], "owner": owner})
            assert witnesses
            cases.append({"h": h, "ranks": [r, s], "witnesses": witnesses})
        labels = [(r + 2 * q * q, (i + q, j + q)) for r, (i, j) in labels]
        q *= 2
    print(json.dumps({"status": "PASS", "height_levels": 3,
                      "actual_edges_checked": len(cases), "cases": cases}))


if __name__ == "__main__":
    main()
