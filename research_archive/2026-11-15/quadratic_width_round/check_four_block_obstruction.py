"""Sparse exact audit of every state in the four-label P obstruction."""
from itertools import permutations
import json
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
        x += s * rx
        y += s * ry
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


def rectangle(vertices):
    a, b, c, d = vertices
    return (len(set(vertices)) == 4
            and a[0] + c[0] == b[0] + d[0]
            and a[1] + c[1] == b[1] + d[1]
            and sum((a[k] - c[k]) ** 2 for k in (0, 1))
            == sum((b[k] - d[k]) ** 2 for k in (0, 1)))


def check(S, D, I, margin):
    assert D > 0 and D % 2 == 0 and I % 2 == 0
    assert S * S % (2 * D) == 0
    J = I + S * S // D
    assert J % 2 == 0
    n = 1 << (J + 2 + (margin + D - 1) // D).bit_length()
    h = D * n
    block = rank(n, I, J) // 4 * 4
    labels = list(range(block, block + 4))
    assert {point(n, r) for r in labels} == {
        (I + i, J + j) for i in (0, 1) for j in (0, 1)}
    a, b = 1 + D * (I + 1), D * (J + 1)
    low, high = a - 1, b + 1
    assert b - a == S * S - 1
    owner = rank(n, J + 1, I)
    owner_block = owner // 4 * 4
    assert owner_block != block
    owner_labels = list(range(owner_block, owner_block + 4))
    rows = []
    for r in labels + [owner]:
        i, j = point(n, r)
        rows.extend((1 + D * i, D * (j + 1)))
    assert min(rows + [low, high]) > margin
    assert max(rows + [low, high]) < h - margin
    tested = 0
    witness_counts = {}
    for order in permutations(labels):
        assigned = [point(n, r) for r in order]
        witnesses = []
        for left in (0, 1):
            right = left + 2
            if assigned[left][0] == I + 1 and assigned[right][1] == J:
                witnesses.append((left, a, b))
            if assigned[left][1] == J and assigned[right][0] == I + 1:
                witnesses.append((left, b, a))
        assert witnesses
        witness_counts[len(witnesses)] = witness_counts.get(len(witnesses), 0) + 1
        left, row_left, row_right = witnesses[0]
        C = (S * (block + left), row_left)
        E = (S * (block + left + 2), row_right)
        P, Q = (S * (block + left + 1), low), (S * (block + left + 1), high)
        for owner_order in permutations(owner_labels):
            mapping = dict(zip(range(block, block + 4), order))
            mapping.update(zip(range(owner_block, owner_block + 4), owner_order))

            def black(p):
                x, y = p
                assert x % S == 0 and x // S in mapping
                i, j = point(n, mapping[x // S])
                return y in (1 + D * i, D * (j + 1))

            owner_slot = owner_block + owner_order.index(owner)
            U, V = (S * owner_slot, low), (S * owner_slot, high)
            tilted, axis = (C, P, E, Q), (U, P, Q, V)
            assert rectangle(tilted) and rectangle(axis)
            assert all(black(p) for p in (C, E, U, V))
            assert not black(P) and not black(Q)
            assert {p for p in tilted if not black(p)} == {P, Q}
            assert {p for p in axis if not black(p)} == {P, Q}
            tested += 1
    return {"S": S, "D": D, "I": I, "J": J, "h": h,
            "block_start": block, "owner_rank": owner,
            "protected_row_range": [min(rows), max(rows)],
            "margin": margin, "witness_histogram": witness_counts,
            "joint_permutations_checked": tested}


def main():
    for n in (1, 2, 4, 8, 16):
        assert all(rank(n, *point(n, r)) == r for r in range(n * n))
    cases = [check(256, 2, 0, 0), check(512, 2, 0, 0),
             check(6272 * 8, 28, 4000, 100000),
             check(6272 * 16, 28, 4000, 100000)]
    result = {"status": "PASS", "cases": cases,
              "total_joint_permutations": sum(c["joint_permutations_checked"] for c in cases)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
