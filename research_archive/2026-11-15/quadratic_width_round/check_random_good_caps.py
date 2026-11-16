"""Independent finite checks of the clamped Hilbert cap construction.

This checks the combinatorial repair, not the remaining blackout supports.
"""
from fractions import Fraction
from pathlib import Path
import json
import random


def curve(n):
    if n == 1:
        return [(0, 0)]
    s = n // 2
    p = curve(s)
    return ([(y, x) for x, y in p]
            + [(x, y + s) for x, y in p]
            + [(x + s, y + s) for x, y in p]
            + [(2*s - 1 - y, s - 1 - x) for x, y in p])


def check(n0, n1, good0, good1, rng):
    n = max(n0, n1)
    N = 1
    while N < 4*n:
        N *= 2
    points = curve(N)
    count = N*N
    good = [set(good0), set(good1)]
    sizes = [n0, n1]
    assert all(good)
    ends = [(min(g), max(g)) for g in good]
    nodes = {}
    length = 1
    while length <= count:
        for start in range(0, count, length):
            end = start + length - 1
            alpha = 0 if points[start][0] == points[end][0] else 1
            assert points[start][alpha] == points[end][alpha]
            nodes[(start, length)] = (alpha, points[start][alpha])
        length *= 4

    # The bad-node area is a sum of two independent one-dimensional costs.
    # Exhaust all offsets separately, choose the minimum of each, and verify
    # their exact expectation bound with rational arithmetic.
    offsets = []
    mean = Fraction(0)
    for alpha in (0, 1):
        costs = []
        for offset in range(1, N - sizes[alpha]):
            weight = 0
            lo, hi = ends[alpha]
            for (_, length), (role, c) in nodes.items():
                if role == alpha:
                    value = min(hi, max(lo, c - offset))
                    if value not in good[alpha]:
                        weight += length
            costs.append(weight)
        offsets.append(1 + min(range(len(costs)), key=costs.__getitem__))
        mean += Fraction(sum(costs), len(costs))
    b = n0 + n1 - len(good[0]) - len(good[1])
    depths = N.bit_length()
    assert mean <= Fraction(count*b*depths, N-n-1)

    values = [tuple(min(ends[a][1], max(ends[a][0], p[a]-offsets[a]))
                    for a in (0, 1)) for p in points]
    bad_node_area = 0
    cap_data = {}
    for key, (alpha, _) in nodes.items():
        start, length = key
        value = values[start][alpha]
        assert value == values[start+length-1][alpha]
        valid = value in good[alpha]
        cap_data[key] = (valid, alpha, value)
        if not valid:
            bad_node_area += length
    assert bad_node_area <= mean
    assert cap_data[(0, count)][0]

    candidates = set()
    for rank, value in enumerate(values):
        if all(value[a] not in good[a] for a in (0, 1)):
            length = 1
            while True:
                key = (rank//length*length, length)
                if cap_data[key][0]:
                    candidates.add(key)
                    break
                length *= 4
    caps = []
    occupied_cap = [None]*count
    for start, length in sorted(candidates, key=lambda k: -k[1]):
        if occupied_cap[start] is not None:
            continue
        caps.append((start, length))
        _, alpha, value = cap_data[(start, length)]
        for r in range(start, start+length):
            assert occupied_cap[r] is None
            occupied_cap[r] = (alpha, value)
    cap_area = sum(length for _, length in caps)
    assert cap_area <= 4*bad_node_area

    surviving = []
    doubles = set()
    for rank, p in enumerate(points):
        original = tuple(p[a]-offsets[a] for a in (0, 1))
        genuine = all(0 <= original[a] < sizes[a] for a in (0, 1))
        if occupied_cap[rank] is not None:
            row = {occupied_cap[rank][0]: occupied_cap[rank][1]}
        elif genuine and all(original[a] in good[a] for a in (0, 1)):
            row = dict(enumerate(original))
            assert original not in doubles
            doubles.add(original)
        else:
            alpha = 1 if values[rank][1] in good[1] else 0
            assert values[rank][alpha] in good[alpha]
            row = {alpha: values[rank][alpha]}
        assert row and all(v in good[a] for a, v in row.items())
        surviving.append(row)
    relocated = n0*n1 - len(doubles)
    assert relocated <= n*b + cap_area
    assert sum(map(len, surviving)) - count + relocated == n0*n1
    odd_only = sum(set(row) == {0} for row in surviving)
    assert odd_only <= N*(n1-len(good[1])) + cap_area

    checked = 0
    if N <= 16:
        pairs = ((r, s) for r in range(count) for s in range(r+1, count))
    else:
        pairs = (sorted(rng.sample(range(count), 2)) for _ in range(25000))
    for r, s in pairs:
        for alpha in surviving[r].keys() & surviving[s].keys():
            delta = surviving[r][alpha] - surviving[s][alpha]
            assert delta*delta < 16*(s-r)
            checked += 1
    return dict(n=[n0, n1], N=N, bad_rows=b, offsets=offsets,
                cap_area=cap_area, bad_node_area=bad_node_area,
                exact_mean=str(mean), relocated=relocated,
                odd_only=odd_only, locality_checks=checked)


def main():
    rng = random.Random(15112026)
    results = []
    for n0, n1 in [(2, 2), (3, 4), (4, 3), (5, 5), (7, 6), (12, 11)]:
        for _ in range(5):
            good0 = [i for i in range(n0) if rng.randrange(3)] or [n0//2]
            good1 = [i for i in range(n1) if rng.randrange(3)] or [n1//2]
            results.append(check(n0, n1, good0, good1, rng))
    result = dict(status="PASS", cases=len(results),
                  locality_checks=sum(r["locality_checks"] for r in results),
                  scope="Cap repair and excess accounting only; no full-board validity claim.",
                  results=results)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "results"}))


if __name__ == "__main__":
    main()
