"""Exact small checks and a census of the unresolved opposite-parity rivals."""
import argparse
import json
import math
from pathlib import Path
import random


def hilbert(q):
    assert q >= 1 and q & (q - 1) == 0
    if q == 1:
        return [(0, 0)]
    n = q // 2
    small = hilbert(n)
    return ([(y, x) for x, y in small] + [(x, y + n) for x, y in small]
            + [(x + n, y + n) for x, y in small]
            + [(2 * n - 1 - y, n - 1 - x) for x, y in small])


def check_order(q):
    points = hilbert(q)
    assert len(set(points)) == q * q
    assert all(0 <= x < q and 0 <= y < q for x, y in points)
    assert all(abs(x - u) + abs(y - v) == 1
               for (x, y), (u, v) in zip(points, points[1:]))
    size = 1
    while size <= q:
        b = size * size
        boxes = []
        for start in range(0, q * q, b):
            p = points[start:start + b]
            boxes.append((p[0][0] // size, p[0][1] // size))
            assert len({(x // size, y // size) for x, y in p}) == 1
        assert all(abs(x - u) + abs(y - v) == 1
                   for (x, y), (u, v) in zip(boxes, boxes[1:]))
        size *= 2
    pairs = 0
    ratio = 0.0
    for r in range(len(points)):
        for s in range(r):
            gap2 = max((points[r][0] - points[s][0]) ** 2,
                       (points[r][1] - points[s][1]) ** 2)
            assert gap2 < 16 * (r - s)
            ratio = max(ratio, gap2 / (r - s))
            pairs += 1
    return {"q": q, "pairs": pairs, "largest_observed_holder_ratio": ratio}


def check_jitter(q, M, row_step, stride, seed=14):
    points = hilbert(q)
    rng = random.Random(seed)
    columns = [stride * (M * r + rng.randrange(M)) for r in range(q * q)]
    pairs = 0
    for r in range(len(points)):
        for s in range(r):
            X = columns[r] - columns[s]
            assert X >= stride * (r - s)
            for axis in (0, 1):
                y = row_step * (points[r][axis] - points[s][axis])
                if y:
                    assert 0 < y * y < 2 * X
                    value = X * X + y * y
                    assert math.isqrt(value) ** 2 != value
            pairs += 1
    return {"q": q, "M": M, "row_step": row_step, "stride": stride,
            "pairs": pairs, "status": "PASS"}


def rival_census(h, stride=32):
    import numpy as np
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = np.array(hilbert(q), dtype=np.int64)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    degree = np.zeros(q * q, dtype=np.int32)
    count = 0
    witnesses = []
    for d in range(1, (h - 1) // stride + 1):
        X = stride * d
        # (L-y)(L+y)=X^2, with odd L and y. Write L-y=2a,
        # L+y=2b. Then ab=(X/2)^2 and a,b have opposite parity.
        half_square = (X // 2) ** 2
        hyp_by_y = {}
        for aa in range(1, math.isqrt(half_square) + 1):
            if half_square % aa:
                continue
            bb = half_square // aa
            if (aa + bb) < h and (bb - aa) % 2:
                hyp_by_y[bb - aa] = aa + bb
                hyp_by_y[aa - bb] = aa + bb
        if not hyp_by_y:
            continue
        for first, second in ((odd, even), (even, odd)):
            y = second[d:] - first[:-d]
            hit = np.isin(y, list(hyp_by_y)) & active[:-d] & active[d:]
            positions = np.nonzero(hit)[0]
            count += len(positions)
            degree[positions] += 1
            degree[positions + d] += 1
            for s in positions[:max(0, 4 - len(witnesses))]:
                t = int(s) + d
                witnesses.append({"rank_pair": [int(s), t], "X": X,
                                  "y": int(y[s]), "L": hyp_by_y[int(y[s])],
                                  "labels": [xy[s].tolist(), xy[t].tolist()]})
    values, counts = np.unique(degree[active], return_counts=True)
    return {"h": h, "stride": stride, "labels": int(active.sum()),
            "opposite_parity_integral_distance_pairs": count,
            "mean_incidence": 2 * count / int(active.sum()),
            "maximum_incidence": int(degree.max()),
            "degree_histogram": {int(x): int(n) for x, n in zip(values, counts)},
            "witnesses": witnesses}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--rival-heights", nargs="*", type=int,
                        default=[128, 256, 512, 1024, 2048])
    parser.add_argument("--strides", nargs="*", type=int, default=[32, 64])
    args = parser.parse_args()
    result = {"orders": [check_order(q) for q in (1, 2, 4, 8, 16, 32)],
              "local_choices": [check_jitter(16, M, step, stride)
                                for M in (1, 2, 7)
                                for step, stride in ((2, 32), (14, 1568))],
              "rival_census": []}
    print("Ordering and local-choice checks PASS", flush=True)
    for stride in args.strides:
        for h in args.rival_heights:
            row = rival_census(h, stride)
            result["rival_census"].append(row)
            print(json.dumps(row), flush=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
