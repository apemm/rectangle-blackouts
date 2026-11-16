"""Sparse exact check of the immutable b=2 permutation P-rival."""
from itertools import product
import json
import math
from pathlib import Path


def point(n, d):
    x = y = 0
    s = 1
    while s < n:
        rx = (d // 2) & 1
        ry = (d ^ rx) & 1
        if ry == 0:
            if rx:
                x, y = s - 1 - x, s - 1 - y
            x, y = y, x
        x, y = x + s * rx, y + s * ry
        d //= 4
        s *= 2
    return x, y


def rank(n, x, y):
    if n == 1:
        return 0
    s = n // 2
    if x < s and y < s:
        return rank(s, y, x)
    if x < s:
        return s * s + rank(s, x, y - s)
    if y >= s:
        return 2 * s * s + rank(s, x - s, y - s)
    return 3 * s * s + rank(s, s - 1 - y, 2 * s - 1 - x)


def orientation(n, d):
    swap = neg = 0
    for _ in range(n.bit_length() - 1):
        digit = d & 3
        if digit in (0, 3):
            swap ^= 1
        if digit == 3:
            neg ^= 1
        d //= 4
    return swap, neg


def rectangle(p):
    a, b, c, d = p
    return (len(set(p)) == 4 and a[0] + c[0] == b[0] + d[0]
            and a[1] + c[1] == b[1] + d[1]
            and (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2
            == (b[0] - d[0]) ** 2 + (b[1] - d[1]) ** 2)


def check(S, row_step=2, anchor=0, margin=0):
    assert S % 8 == 0 and row_step % 2 == 0 and anchor % 2 == 0
    assert S * S % (8 * row_step) == 0
    D0 = S * S // (8 * row_step)
    assert D0 % 2 == 0
    padding = (margin + 8 * row_step - 1) // (8 * row_step)
    Q0 = 1 << (D0 + anchor + padding + 4).bit_length()
    chosen = []
    for a in (anchor, anchor + 1):
        r = rank(Q0, a, D0 + a)
        if orientation(Q0, r) in ((0, 0), (1, 1)):
            chosen.append((a, r, orientation(Q0, r)))
    assert len(chosen) == 1
    a, macro_rank, ori = chosen[0]
    n, base = 8 * Q0, 64 * macro_rank
    I, J = 8 * a, 8 * (D0 + a)
    for r in range(64):
        x, y = point(8, r)
        if ori == (1, 1):
            x, y = 7 - y, 7 - x
        assert point(n, base + r) == (I + x, J + y)
    blocks = [(base + 2) // 2, (base + 4) // 2]
    rows = []
    for block in blocks:
        (i, j), (k, ell) = point(n, 2 * block), point(n, 2 * block + 1)
        if i == k:
            rows.append(row_step * i + 1)
        else:
            assert j == ell
            rows.append(row_step * (j + 1))
    C, D = (S * (base + 2), rows[0]), (S * (base + 4), rows[1])
    assert abs(rows[0] - rows[1]) == S * S - 1
    L = S * S + 1
    assert (D[0] - C[0]) ** 2 + (D[1] - C[1]) ** 2 == L * L
    low, high = (sum(rows) - L) // 2, (sum(rows) + L) // 2
    assert 1 <= low < high <= row_step * n
    P, Q = (S * (base + 3), low), (S * (base + 3), high)
    odd, even = (low, high) if low % 2 else (high, low)
    assert (odd - 1) % row_step == 0 and even % row_step == 0
    owner_rank = rank(n, (odd - 1) // row_step, even // row_step - 1)
    owner_block = owner_rank // 2
    assert owner_block not in blocks
    protected_ranks = [base + r for r in (2, 3, 4, 5)] + [owner_rank]
    protected_rows = []
    for r in protected_ranks:
        i, j = point(n, r)
        protected_rows.extend((row_step * i + 1, row_step * (j + 1)))
    if margin:
        assert min(protected_rows + [low, high]) > margin
        assert max(protected_rows + [low, high]) < row_step * n - margin
    tested = 0
    for values in product((0, 1), repeat=3):
        swaps = dict(zip(blocks + [owner_block], values))

        def black(p):
            x, row = p
            if x % S:
                return False
            slot = x // S
            original = slot ^ swaps.get(slot // 2, 0)
            i, j = point(n, original)
            return row in (row_step * i + 1, row_step * (j + 1))

        owner_slot = owner_rank ^ swaps[owner_block]
        U, V = (S * owner_slot, low), (S * owner_slot, high)
        tilted, axis = (C, P, D, Q), (U, P, Q, V)
        assert black(C) and black(D) and black(U) and black(V)
        assert not black(P) and not black(Q)
        assert rectangle(tilted) and rectangle(axis)
        assert {p for p in tilted if not black(p)} == {p for p in axis if not black(p)} == {P, Q}
        tested += 1
    return {"S": S, "row_step": row_step, "anchor": anchor, "margin": margin,
            "h": row_step * n, "orientation": ori, "block_rank": base,
            "invariant_rows": rows, "common_rows": [low, high],
            "protected_row_range": [min(protected_rows), max(protected_rows)],
            "owner_rank": owner_rank, "swap_assignments_checked": tested}


def main():
    for n in (1, 2, 4, 8, 16):
        assert all(rank(n, *point(n, r)) == r for r in range(n * n))
    cases = [check(S) for S in (32, 64, 96, 128, 160, 192, 224, 256, 288)]
    cases.extend(check(6272 * sigma, row_step=28, anchor=450, margin=100000)
                 for sigma in (4, 8))
    result = {"status": "PASS", "cases": cases,
              "total_swap_assignments": sum(c["swap_assignments_checked"] for c in cases)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
