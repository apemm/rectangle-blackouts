"""Sparse exact geometry check for every nonempty private-stub parity."""
from pathlib import Path
import json
from check_four_block_obstruction import point, rank, rectangle


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


def check(S, M, D, anchor=0, margin=0):
    assert (S * M) ** 2 % (8 * D) == 0
    D0 = (S * M) ** 2 // (8 * D)
    assert D0 >= 2 and D0 % 2 == 0 and anchor % 2 == 0
    padding = (margin + 8 * D - 1) // (8 * D)
    Q = 1 << (D0 + anchor + padding + 4).bit_length()
    selected = []
    for a in (anchor, anchor + 1):
        macro = rank(Q, a, D0 + a)
        ori = orientation(Q, macro)
        if ori in ((0, 0), (1, 1)):
            selected.append((a, macro, ori))
    assert len(selected) == 1
    a, macro, ori = selected[0]
    side, first = 8 * Q, 64 * macro
    I, J = 8 * a, 8 * (D0 + a)
    cells = {r: point(side, first + r) for r in (2, 3, 4)}
    if ori == (0, 0):
        expected = {2: (I + 1, J + 1), 3: (I + 1, J), 4: (I + 2, J)}
    else:
        expected = {2: (I + 6, J + 6), 3: (I + 7, J + 6), 4: (I + 7, J + 5)}
    assert cells == expected
    rows = {r: (1 + D * i, D * (j + 1)) for r, (i, j) in cells.items()}
    length = (S * M) ** 2 + 1
    assert rows[4][1] - rows[2][0] == rows[2][1] - rows[4][0] == length - 2
    owners = {}
    for direction, (ya, yb) in enumerate(((rows[2][0], rows[4][1]),
                                          (rows[2][1], rows[4][0]))):
        low, high = (ya + yb - length) // 2, (ya + yb + length) // 2
        assert low % D == 0 and (high - 1) % D == 0
        owner_cell = ((high - 1) // D, low // D - 1)
        owner_rank = rank(side, *owner_cell)
        assert not first <= owner_rank < first + 64
        assert margin < low < high < D * side - margin
        owners[direction] = (low, high, owner_rank, owner_cell)
    tested = 0
    for t in range(M):
        xa = S * (M * (first + 2) + t)
        xb = S * (M * (first + 4) + t)
        xm = S * (M * (first + 3) + t)
        for target in ((0,), (1,), (0, 1)):
            direction = 0 if 1 in target else 1
            ya, yb = ((rows[2][0], rows[4][1]) if direction == 0
                      else (rows[2][1], rows[4][0]))
            low, high, owner_rank, owner_cell = owners[direction]
            P, Qp = (xm, low), (xm, high)
            C, E = (xa, ya), (xb, yb)
            assert (xb - xa) ** 2 + (yb - ya) ** 2 == length ** 2
            for midpoint in ((0,), (1,), (0, 1)):
                for own_t in range(M):
                    xo = S * (M * owner_rank + own_t)
                    assert xo != xm
                    U, V = (xo, low), (xo, high)
                    black = {(xa, y) for y in rows[2]}
                    black.update((xb, rows[4][p]) for p in target)
                    black.update((xm, rows[3][p]) for p in midpoint)
                    black.update((U, V))
                    tilted, axis = (C, P, E, Qp), (U, P, Qp, V)
                    assert rectangle(tilted) and rectangle(axis)
                    assert C in black and E in black and U in black and V in black
                    assert P not in black and Qp not in black
                    assert set(tilted) - black == set(axis) - black == {P, Qp}
                    tested += 1
    return {"S": S, "M": M, "D": D, "height": D * side,
            "orientation": ori, "block_start": first,
            "cells": cells, "rows": rows, "owners": owners,
            "local_assignments_checked": tested, "margin": margin}


def main():
    cases = [check(128, M, 2) for M in (1, 2, 3, 4, 7, 16)]
    cases.append(check(224, 1, 2))
    cases.extend(check(50176, M, 28, 450, 100000) for M in (1, 3))
    result = {"status": "PASS", "cases": cases,
              "total_local_assignments": sum(c["local_assignments_checked"] for c in cases)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "cases": len(cases),
                      "total_local_assignments": result["total_local_assignments"]}))


if __name__ == "__main__":
    main()
