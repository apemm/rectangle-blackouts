"""Sparse exact checks: recursive mixed collision and the height-4096 P triangle."""
from itertools import combinations
from math import isqrt
from pathlib import Path
import json


def point(q, rank):
    assert q >= 1 and q & (q-1) == 0 and 0 <= rank < q*q
    if q == 1:
        return (0, 0)
    n = q//2
    quadrant, offset = divmod(rank, n*n)
    x, y = point(n, offset)
    return ((y, x), (x, y+n), (x+n, y+n),
            (2*n-1-y, n-1-x))[quadrant]


def check_family(s):
    u = s*s//2
    q, h = 4*u*u, 8*u*u
    base, t = u**4 + 8*u*u, 2*u*u
    I, J = u*u + 2*u, 2*u
    ranks = (base, base+1, base+t-1, base+t)
    expected = ((I, J), (I+1, J), (I+u-1, J+u), (I+u, J+u))
    assert tuple(point(q, r) for r in ranks) == expected
    labels = [(s*r, 2*i+1, 2*j+2)
              for r, (i, j) in zip(ranks, expected)]
    pts = [(x, y) for x, a, b in labels for y in (a, b)]
    A, B, D, C = pts[0], pts[3], pts[5], pts[6]
    P, Q = (D[0], C[1]), (C[0], D[1])
    assert P not in pts and Q in pts
    ux, uy = B[0]-A[0], B[1]-A[1]
    tx, ty = P[0]-A[0], P[1]-A[1]
    assert ux*tx + uy*ty == 0
    assert Q == (B[0]+tx, B[1]+ty)
    assert {A, B, P, Q} - set(pts) == {P}
    assert {C, D, P, Q} - set(pts) == {P}
    assert all(1 <= y <= h for _, y in pts + [P, Q])
    assert max(x for x, _ in pts+[P, Q]) < s*q*q
    nonhorizontal_integral_pairs = []
    for i, j in combinations(range(8), 2):
        dx, dy = pts[j][0]-pts[i][0], pts[j][1]-pts[i][1]
        if dx and dy:
            norm = dx*dx+dy*dy
            if isqrt(norm)**2 == norm:
                nonhorizontal_integral_pairs.append((i, j))
    assert not nonhorizontal_integral_pairs
    return dict(stride=s, side=q, height=h, base_rank=base, ranks=ranks,
                coordinates=expected, labels=labels, common_white=P,
                common_black=Q, status="PASS",
                nonhorizontal_integral_pairs_in_four_labels=[])


def check_triangle():
    h, q = 4096, 2048
    ranks = (1331100, 1331133, 1331166)
    coordinates = ((187, 1549), (190, 1545), (187, 1541))
    assert tuple(point(q, r) for r in ranks) == coordinates
    cases = [
        (0, 1, 375, 3092, 2915, 276, 3191, 3990830),
        (0, 2, 375, 3084, 3435, 12, 3447, 3952606),
        (1, 2, 3092, 375, 2915, 276, 3191, 3990830),
    ]
    for a, b, ya, yb, length, low, high, owner in cases:
        X = 32*(ranks[b]-ranks[a])
        assert X*X+(yb-ya)**2 == length*length
        assert (ya+yb-length, ya+yb+length) == (2*low, 2*high)
        oi, oj = point(q, owner)
        assert {2*oi+1, 2*oj+2} == {low, high}
        assert 2*owner != ranks[a]+ranks[b]
        assert 1 <= low < high <= h
    return dict(height=h, ranks=ranks, coordinates=coordinates,
                witnesses=cases, status="PASS")


def check_dilated_angle(s, scale):
    assert s >= 8 and s & (s-1) == 0
    assert scale >= 1 and scale & (scale-1) == 0
    assert (scale.bit_length()-1) % 2 == 0
    u = s*s*scale**3//2
    q, h = 4*u*u, 8*u*u
    base, t = u**4 + 8*scale*scale*u*u, 2*u*u
    I, J = u*u + 2*scale*u, 2*scale*u
    ranks = (base, base+scale*scale, base+scale*scale*t)
    expected = ((I, J), (I+scale, J), (I+scale*u, J+scale*u))
    assert tuple(point(q, r) for r in ranks) == expected
    A = (s*ranks[0], 2*I+1)
    B = (s*ranks[1], 2*J+2)
    C = (s*ranks[2], 2*(J+scale*u)+2)
    W = (A[0]+C[0]-B[0], A[1]+C[1]-B[1])
    assert (A[0]-B[0])*(C[0]-B[0]) + (A[1]-B[1])*(C[1]-B[1]) == 0
    assert A[0] < W[0] < C[0]
    assert len({A[0], B[0], C[0], W[0]}) == 4
    assert all(1 <= y <= h for x, y in (A, B, C, W))
    assert all(0 <= z < q for pair in expected for z in pair)
    assert all(r % (scale*scale) == 0 for r in ranks)
    assert all(z % scale == 0 for pair in expected for z in pair)
    return dict(stride=s, scale=scale, height=h, side=q, ranks=ranks,
                coordinates=expected, black_points=(A, B, C),
                fourth_corner=W, status="PASS")


def terminal_orientation(side, rank):
    swap = negative = 0
    while side > 1:
        side //= 2
        digit, rank = divmod(rank, side*side)
        swap ^= digit in (0, 3)
        negative ^= digit == 3
    return int(swap), int(negative)


def check_orientation_angle():
    q, h, stride = 2**24, 2**25, 32
    macro_rank = 247398398
    assert point(2**14, macro_rank) == (9983, 1)
    assert terminal_orientation(2**14, macro_rank) == (0, 0)
    local_ranks = (22, 61, 524244)
    local_points = ((7, 1), (1, 6), (504, 518))
    assert tuple(point(1024, r) for r in local_ranks) == local_points
    ranks = tuple(macro_rank*1024**2 + r for r in local_ranks)
    expected = ((10222599, 1025), (10222593, 1030), (10223096, 1542))
    assert tuple(point(q, r) for r in ranks) == expected
    assert all(terminal_orientation(q, r) == (1, 0) for r in ranks)
    A = (stride*ranks[0], 2*expected[0][0]+1)
    B = (stride*ranks[1], 2*expected[1][1]+2)
    C = (stride*ranks[2], 2*expected[2][1]+2)
    W = (A[0]+C[0]-B[0], A[1]+C[1]-B[1])
    assert (A[0]-B[0], A[1]-B[1]) == (-1248, 20443137)
    assert (C[0]-B[0], C[1]-B[1]) == (16773856, 1024)
    assert (A[0]-B[0])*(C[0]-B[0]) + (A[1]-B[1])*(C[1]-B[1]) == 0
    assert all(1 <= y <= h for x, y in (A, B, C, W))
    assert A[0] < W[0] < C[0]
    assert len({A[0], B[0], C[0], W[0]}) == 4
    return dict(stride=stride, height=h, side=q, ranks=ranks,
                coordinates=expected, terminal_orientation="swap",
                black_points=(A, B, C), fourth_corner=W, status="PASS")


def check_orientation_low_bits_angle():
    u, block, macro_side, stride = 2**21, 2**22, 2**16, 32
    q, h = block*macro_side, 2*block*macro_side
    macro_rank = 2**28+2
    assert point(macro_side, macro_rank) == (2**14+1, 1)
    assert terminal_orientation(macro_side, macro_rank) == (0, 0)
    local_ranks = (76, 140, 2*u*u-1204)
    local_points = ((1, 11), (9, 11), (u-47, u+11))
    assert tuple(point(block, r) for r in local_ranks) == local_points
    ranks = tuple(macro_rank*block*block+r for r in local_ranks)
    I, J = (2**14+1)*block, block
    expected = tuple((I+i, J+j) for i, j in local_points)
    assert tuple(point(q, r) for r in ranks) == expected
    assert all(terminal_orientation(q, r) == (1, 1) for r in ranks)
    assert {(r % 8, i % 8, j % 8) for r, (i, j) in zip(ranks, expected)} == {(4, 1, 3)}
    A = (stride*ranks[0], 2*expected[0][0]+1)
    B = (stride*ranks[1], 2*expected[1][1]+2)
    C = (stride*ranks[2], 2*expected[2][1]+2)
    W = (A[0]+C[0]-B[0], A[1]+C[1]-B[1])
    assert (A[0]-B[0])*(C[0]-B[0]) + (A[1]-B[1])*(C[1]-B[1]) == 0
    assert all(1 <= y <= h for x, y in (A, B, C, W))
    assert A[0] < W[0] < C[0]
    assert len({A[0], B[0], C[0], W[0]}) == 4
    assert W[1] == 137451536387
    return dict(stride=stride, height=h, side=q, ranks=ranks,
                coordinates=expected, terminal_orientation="minus swap",
                common_residue_mod_8=(4, 1, 3),
                black_points=(A, B, C), fourth_corner=W, status="PASS")


if __name__ == "__main__":
    result = dict(recursive_mixed=[check_family(2**e) for e in range(3, 9)],
                  actual_P_triangle=check_triangle(),
                  dilated_angles=[check_dilated_angle(s, scale)
                                  for s, scale in ((8, 1), (8, 4), (8, 16),
                                                   (16, 4), (32, 4), (32, 64))],
                  terminal_orientation_angle=check_orientation_angle(),
                  terminal_orientation_low_bits_angle=check_orientation_low_bits_angle())
    path = Path(__file__).with_name("hilbert_recursive_mixed_check.json")
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(dict(status="PASS", output=str(path))))
