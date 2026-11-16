"""Exact finite check; this is not a claim about the actual Hilbert order."""
from itertools import combinations
from math import isqrt
from pathlib import Path
import json


def verify(stride):
    s = stride
    m = s**4 // 32
    labels = [
        (0, m + 1, 4),
        (s, m + 3, 2),
        (s * (m - 1), m + s*s + 3, s*s + 2),
        (s * m, m + s*s + 1, s*s + 4),
    ]
    points = [(x, y) for x, odd, even in labels for y in (odd, even)]
    pair_tests = []
    for i, j in combinations(range(8), 2):
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]
        if not dx:
            continue
        norm = dx*dx + dy*dy
        root = isqrt(norm)
        assert root*root < norm < (root+1)**2
        if dy % 2 == 0:
            assert dy*dy*s < 64*abs(dx)
        pair_tests.append([i, j, norm, root])
    angle_tests = 0
    for i, j, k in combinations(range(8), 3):
        for a, b, c in ((i, j, k), (j, i, k), (k, i, j)):
            ux = points[b][0] - points[a][0]
            uy = points[b][1] - points[a][1]
            vx = points[c][0] - points[a][0]
            vy = points[c][1] - points[a][1]
            if ux and uy and vx and vy:
                assert ux*vx + uy*vy != 0
            angle_tests += 1
    A, B = (0, m+1), (s, 2)
    C, D = (s*m, m+s*s+1), (s*(m-1), s*s+2)
    P, Q = (D[0], C[1]), (C[0], D[1])
    assert {A, B, C, D}.issubset(points)
    assert P not in points and Q not in points
    ux, uy = B[0]-A[0], B[1]-A[1]
    tx, ty = P[0]-A[0], P[1]-A[1]
    assert ux*tx + uy*ty == 0
    assert Q == (B[0]+tx, B[1]+ty)
    assert ux and uy and tx and ty
    assert {A, B, P, Q} ^ {C, D, P, Q} == {A, B, C, D}
    return dict(
        stride=s, height=max(y for _, y in points), labels=labels,
        status="PASS", different_column_pair_tests=pair_tests,
        triple_vertex_tests=angle_tests,
        first_rectangle=[A, B, P, Q], second_rectangle=[C, D, P, Q],
        scope="An abstract Holder-compatible placement, not an actual Hilbert-order witness",
    )


if __name__ == "__main__":
    result = [verify(s) for s in (8, 16, 32, 64, 128, 256)]
    path = Path(__file__).with_name("holder_mixed_counterexample_check.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(status="PASS", strides=[r["stride"] for r in result],
                         output=str(path))))
