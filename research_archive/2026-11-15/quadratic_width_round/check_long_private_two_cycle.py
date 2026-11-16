"""Exact sparse nested-Hilbert audit of long two-role P cycles."""
from pathlib import Path
import json
from check_private_parity_stub_obstruction import point, rank, rectangle, orientation


def select_macro(side, gap, anchor):
    assert gap % 2 == 0 and anchor % 2 == 0
    candidates = []
    for a in (anchor, anchor + 1):
        r = rank(side, a, a + gap)
        ori = orientation(side, r)
        if ori in ((0, 0), (1, 1)):
            candidates.append((a, r, ori))
    assert len(candidates) == 1
    return candidates[0]


def check(S, M, D, L):
    C = (S * M) ** 2
    assert L >= 64 and L & (L - 1) == 0
    gap_inner = C // (8 * D)
    a, r_inner, ori_inner = select_macro(L // 8, gap_inner, 0)
    r0 = 64 * r_inner
    w1, w2 = point(L, r0 + 2), point(L, r0 + 4)
    assert sum(w1) == sum(w2)
    assert w2[1] - w1[0] == w1[1] - w2[0] == C // D - 1
    assert point(32, 292) == (6, 20) and point(32, 908) == (20, 6)
    assert orientation(32, 292) == orientation(32, 908) == (0, 0)
    B = 32 * L
    ra, rb = 292 * L * L + r0 + 2, 908 * L * L + r0 + 4
    p, q = (6 * L + w1[0], 20 * L + w1[1]), (20 * L + w2[0], 6 * L + w2[1])
    assert point(B, ra) == p and point(B, rb) == q
    t = 308 * L * L + 1
    z = (t - 1) // D
    T = (C - 1) * z
    assert rb - ra == 2 * t and T % B == 0 and (T // B) % 2 == 0
    gap_outer = T // B
    anchor = (2 * z + B + B - 1) // B
    anchor += anchor % 2
    bound = gap_outer + anchor + (z + B - 1) // B + 8
    macro_side = 1 << (4 * bound - 1).bit_length()
    a, r_outer, ori_outer = select_macro(macro_side, gap_outer, anchor)
    I, J = B * a, B * (a + gap_outer)
    side, first = B * macro_side, B * B * r_outer
    if ori_outer == (1, 1):
        p, q = (B - 1 - p[1], B - 1 - p[0]), (B - 1 - q[1], B - 1 - q[0])
    ca, cb = (I + p[0], J + p[1]), (I + q[0], J + q[1])
    ra, rb = first + ra, first + rb
    assert point(side, ra) == ca and point(side, rb) == cb
    assert sum(ca) == sum(cb)
    aa, ba = 1 + D * ca[0], D * (ca[1] + 1)
    ab, bb = 1 + D * cb[0], D * (cb[1] + 1)
    X, Y, hyp = 2 * S * M * t, (C - 1) * t, (C + 1) * t
    assert bb - aa == ba - ab == Y
    assert X * X + Y * Y == hyp * hyp and (hyp - Y) // 2 == t
    middle = (ra + rb) // 2
    cm = point(side, middle)
    midrows = (1 + D * cm[0], D * (cm[1] + 1))
    owners = []
    for ya, yb in ((aa, bb), (ba, ab)):
        low, high = (ya + yb - hyp) // 2, (ya + yb + hyp) // 2
        owner_cell = ((high - 1) // D, low // D - 1)
        assert low % D == 0 and (high - 1) % D == 0
        assert 1 <= low < high <= D * side
        assert low < min(midrows) and high > max(midrows)
        assert owner_cell[0] >= I + B and owner_cell[1] < I
        owner_rank = rank(side, *owner_cell)
        assert point(side, owner_rank) == owner_cell
        assert not first <= owner_rank < first + B * B
        owners.append((low, high, owner_rank))
    tested = 0
    for xi in range(M):
        xa, xb = S * (M * ra + xi), S * (M * rb + xi)
        xm = S * (M * middle + xi)
        for direction, (ya, yb) in enumerate(((aa, bb), (ba, ab))):
            low, high, owner_rank = owners[direction]
            P, Q = (xm, low), (xm, high)
            C1, C2 = (xa, ya), (xb, yb)
            for own in range(M):
                xo = S * (M * owner_rank + own)
                U, V = (xo, low), (xo, high)
                black = {(xa, aa), (xa, ba), C2, U, V}
                for mid in ((midrows[0],), (midrows[1],), midrows):
                    current = black | {(xm, row) for row in mid}
                    tilted, axis = (C1, P, C2, Q), (U, P, Q, V)
                    assert rectangle(tilted) and rectangle(axis)
                    assert P not in current and Q not in current
                    assert set(tilted) - current == set(axis) - current == {P, Q}
                    tested += 1
    return {"S": S, "M": M, "D": D, "L": L, "height": D * side,
            "t_and_half_factor": t, "slot_gap": M * (rb - ra),
            "primitive_triple": [2 * S * M, C - 1, C + 1],
            "actual_triple": [X, Y, hyp], "rank_gap": rb - ra,
            "source_ranks": [ra, rb], "source_cells": [ca, cb],
            "owners": owners, "outer_orientation": ori_outer,
            "local_assignments_checked": tested}


def main():
    cases = []
    for S, M, D in ((8, 1, 2), (32, 3, 2), (8, 7, 2), (6272, 1, 28)):
        minimum = max(64, (S * M) ** 2 // D + 16)
        first = 1 << (minimum - 1).bit_length()
        cases.extend(check(S, M, D, first * factor) for factor in (1, 2))
    result = {"status": "PASS", "cases": cases,
              "total_local_assignments": sum(c["local_assignments_checked"] for c in cases)}
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "cases": len(cases),
                      "total_local_assignments": result["total_local_assignments"]}))


if __name__ == "__main__":
    main()
