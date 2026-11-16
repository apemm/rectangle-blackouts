"""Check the explicit Hilbert P obstruction without enumerating the grid."""
import json
from pathlib import Path


def point(n, r):
    if n == 1:
        assert r == 0
        return 0, 0
    q = n // 2
    quadrant, local = divmod(r, q * q)
    x, y = point(q, local)
    if quadrant == 0:
        return y, x
    if quadrant == 1:
        return x, y + q
    if quadrant == 2:
        return x + q, y + q
    assert quadrant == 3
    return 2 * q - 1 - y, q - 1 - x


def rank(n, x, y):
    if n == 1:
        assert x == y == 0
        return 0
    q = n // 2
    if x < q and y < q:
        return rank(q, y, x)
    if x < q:
        return q * q + rank(q, x, y - q)
    if y >= q:
        return 2 * q * q + rank(q, x - q, y - q)
    return 3 * q * q + rank(q, q - 1 - y, 2 * q - 1 - x)


def check(S, q):
    N = S * S * q**3 // 16
    Q, h = 8 * q * N, 16 * q * N
    e, f = (6 * q, 2 * q * N + 6 * q - 1), (7 * q, 2 * q * N + 6 * q - 1)
    re, rf = rank(Q, *e), rank(Q, *f)
    assert point(Q, re) == e and point(Q, rf) == f
    assert rf - re == q * q
    assert 3 * re == 44 * q * q * N * N - 88 * q * q - 1
    assert tuple(v % q for v in e) == tuple(v % q for v in f)
    assert re % (q * q) == rf % (q * q)
    C, D = (S * re, 12 * q + 1), (S * rf, 4 * q * N + 12 * q)
    xm = S * (re + rf) // 2
    P, Z = (xm, 12 * q), (xm, 4 * q * N + 12 * q + 1)
    owner = (2 * q * N + 6 * q, 6 * q - 1)
    rg = rank(Q, *owner)
    assert point(Q, rg) == owner and S * rg != xm
    A = (S * rg, P[1])
    B = (S * rg, Z[1])
    tilted, axis = {C, D, P, Z}, {P, Z, A, B}
    assert len(tilted) == len(axis) == 4 and tilted != axis
    assert (P[0] - C[0]) * (Z[0] - C[0]) + (P[1] - C[1]) * (Z[1] - C[1]) == 0
    assert C[0] + D[0] == P[0] + Z[0] and C[1] + D[1] == P[1] + Z[1]
    assert all(0 <= x <= S * (Q * Q - 1) and 1 <= y <= h for x, y in tilted | axis)

    def black(p):
        x, y = p
        if x % S:
            return False
        i, j = point(Q, x // S)
        return y in (2 * i + 1, 2 * j + 2)

    assert all(black(p) for p in tilted ^ axis)
    assert {p for p in tilted if not black(p)} == {p for p in axis if not black(p)}
    return {"stride": S, "q": q, "N": N, "height": h, "grid_side": Q,
            "labels": [e, f], "ranks": [re, rf], "owner": owner,
            "owner_rank": rg, "tilted": sorted(tilted), "axis": sorted(axis),
            "status": "PASS"}


if __name__ == "__main__":
    checks = [check(S, 2**k) for S in (32, 64, 128) for k in range(1, 11)]
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps({"checks": checks, "status": "PASS"}, indent=2) + "\n")
    print(f"PASS: {len(checks)} exact sparse checks; largest height {max(c['height'] for c in checks)}")
