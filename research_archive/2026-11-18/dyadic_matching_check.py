"""Check the vertical-rival graphs of all XOR matchings at one height."""

import argparse
import hashlib
import json
from math import gcd, isqrt

import numpy as np
from numba import njit


def tree_hash(value):
    value = ((value ^ (value >> 16)) * 0x7FEB352D) & 0xFFFFFFFF
    value = ((value ^ (value >> 15)) * 0x846CA68B) & 0xFFFFFFFF
    return value ^ (value >> 16)


def permutation(size, mode):
    if mode == "identity":
        return np.arange(size, dtype=np.int32)
    if mode == "wrapped":
        multiplier = (isqrt(2 * size) + 1) | 1
        return np.array([multiplier * i % size for i in range(size)], dtype=np.int32)
    values = np.zeros(size, dtype=np.int32)
    for bit in range(size.bit_length() - 1):
        place = 1 << bit
        for i in range(size):
            prefix = i & (place - 1)
            flip = tree_hash(place - 1 + prefix) & 1
            values[i] |= (i & place) ^ (flip * place)
    return values


def leg_table(height):
    triples = set()
    for u in range(2, isqrt(height - 1) + 1):
        for v in range(1, u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1:
                continue
            x = 2 * u * v
            y = u * u - v * v
            z = u * u + v * v
            if x % 8:
                continue
            for scale in range(1, (height - 1) // z + 1, 2):
                triples.add((scale * x // 8, scale * y))

    factors = set()
    limit = (height - 1) // 8
    least = list(range(limit + 1))
    for prime in range(2, isqrt(limit) + 1):
        if least[prime] != prime:
            continue
        for value in range(prime * prime, limit + 1, prime):
            if least[value] == value:
                least[value] = prime
    for shift in range(1, limit + 1):
        product = 16 * shift * shift
        exponents = {2: 4}
        remaining = shift
        while remaining > 1:
            prime = least[remaining]
            remaining //= prime
            exponents[prime] = exponents.get(prime, 0) + 2
        divisors = [1]
        for prime, exponent in exponents.items():
            old = divisors.copy()
            power = 1
            for _ in range(exponent):
                power *= prime
                divisors.extend(d * power for d in old if d * power < 4 * shift)
        for a in divisors:
            b = product // a
            if a < b and a + b < height and (b - a) % 2:
                factors.add((shift, b - a))
    assert triples == factors
    return np.array(sorted(triples), dtype=np.int64).reshape(-1, 2)


@njit(cache=False)
def enumerate_edges(height, sigma, inverse, legs, start, stop, offsets, left, right, fill):
    odd_count = (height + 1) // 2
    even_count = height // 2
    oriented = 0
    for i in range(odd_count):
        for shift, dy in legs:
            for sign_x in (-1, 1):
                column = sigma[i] + sign_x * shift
                if column < 0 or column >= len(inverse):
                    continue
                j = inverse[column]
                if j >= odd_count:
                    continue
                for sign_y in (-1, 1):
                    leaf = i + (sign_y * dy - 1) // 2
                    if leaf < 0 or leaf >= even_count:
                        continue
                    matching = j ^ leaf
                    if not (start <= matching < stop) or (i ^ matching) >= even_count:
                        continue
                    oriented += 1
                    # If both orientations are present, the smaller first index owns the edge.
                    if j < i:
                        reverse_y = 2 * j - 2 * (i ^ matching) - 1
                        norm = 64 * shift * shift + reverse_y * reverse_y
                        root = int(np.sqrt(norm))
                        if root < height and root * root == norm:
                            continue
                    index = matching - start
                    if fill:
                        slot = offsets[index]
                        left[slot] = i
                        right[slot] = j
                        offsets[index] += 1
                    else:
                        offsets[index + 1] += 1
    return oriented


@njit(cache=False)
def color_matching(height, matching, edge_start, edge_stop, left, right):
    n = (height + 1) // 2
    offsets = np.zeros(n + 1, dtype=np.int32)
    for edge in range(edge_start, edge_stop):
        offsets[left[edge] + 1] += 1
        offsets[right[edge] + 1] += 1
    degree = offsets[1:].copy()
    offsets = np.cumsum(offsets)
    next_slot = offsets[:-1].copy()
    neighbors = np.empty(offsets[-1], dtype=np.int32)
    for edge in range(edge_start, edge_stop):
        i, j = left[edge], right[edge]
        neighbors[next_slot[i]] = j
        neighbors[next_slot[j]] = i
        next_slot[i] += 1
        next_slot[j] += 1

    # Run the degree-bucket core decomposition of Batagelj and Zaversnik.
    bins = np.zeros(degree.max() + 1, dtype=np.int32)
    for d in degree:
        bins[d] += 1
    first = 0
    for d in range(len(bins)):
        count = bins[d]
        bins[d] = first
        first += count
    order = np.empty(n, dtype=np.int32)
    position = np.empty(n, dtype=np.int32)
    for i in range(n):
        d = degree[i]
        position[i] = bins[d]
        order[position[i]] = i
        bins[d] += 1
    for d in range(len(bins) - 1, 0, -1):
        bins[d] = bins[d - 1]
    bins[0] = 0
    for point in range(n):
        v = order[point]
        for slot in range(offsets[v], offsets[v + 1]):
            u = neighbors[slot]
            if degree[u] <= degree[v]:
                continue
            d = degree[u]
            w = order[bins[d]]
            pu, pw = position[u], position[w]
            order[pu], order[pw] = w, u
            position[w], position[u] = pu, pw
            bins[d] += 1
            degree[u] -= 1

    colors = np.full(n, -1, dtype=np.int16)
    seen = np.full(n + 1, -1, dtype=np.int32)
    for step in range(n):
        i = order[n - 1 - step]
        if (i ^ matching) >= height // 2:
            continue
        for slot in range(offsets[i], offsets[i + 1]):
            color = colors[neighbors[slot]]
            if color >= 0:
                seen[color] = step
        c = 0
        while seen[c] == step:
            c += 1
        colors[i] = c
    for edge in range(edge_start, edge_stop):
        assert colors[left[edge]] != colors[right[edge]]
    return degree, order, colors


@njit(cache=False)
def extend_core_colors(height, matching, left, right, order, colors):
    n = len(colors)
    offsets = np.zeros(n + 1, dtype=np.int32)
    for k in range(len(left)):
        offsets[left[k] + 1] += 1
        offsets[right[k] + 1] += 1
    offsets = np.cumsum(offsets)
    slots = offsets[:-1].copy()
    neighbors = np.empty(offsets[-1], dtype=np.int32)
    for k in range(len(left)):
        i, j = left[k], right[k]
        neighbors[slots[i]] = j
        neighbors[slots[j]] = i
        slots[i] += 1
        slots[j] += 1
    for pos in range(n - 1, -1, -1):
        i = order[pos]
        if (i ^ matching) >= height // 2 or colors[i] >= 0:
            continue
        used = 0
        for k in range(offsets[i], offsets[i + 1]):
            c = colors[neighbors[k]]
            if c >= 0:
                used |= 1 << c
        assert used != 7
        c = 0
        while used & (1 << c):
            c += 1
        colors[i] = c
    for k in range(len(left)):
        assert colors[left[k]] != colors[right[k]]
    return colors


def color_three_core(height, matching, left, right, numbers, order):
    from pysat.solvers import Solver

    keep = numbers >= 3
    points = np.flatnonzero(keep)
    number = np.full(len(numbers), -1, dtype=np.int32)
    number[points] = np.arange(len(points))
    inside = keep[left] & keep[right]
    edges = np.column_stack((number[left[inside]], number[right[inside]])).tolist()
    clauses = [[3 * i + 1, 3 * i + 2, 3 * i + 3] for i in range(len(points))]
    for i, j in edges:
        for c in (1, 2, 3):
            clauses.append([-(3 * i + c), -(3 * j + c)])
    a, b = edges[0]
    clauses.extend([[3 * a + 1], [3 * b + 2]])
    with Solver(name="cadical195", bootstrap_with=clauses) as solver:
        if not solver.solve():
            return None
        model = set(x for x in solver.get_model() if x > 0)
    colors = np.full(len(numbers), -1, dtype=np.int16)
    for i, p in enumerate(points):
        colors[p] = next(c for c in range(3) if 3 * i + c + 1 in model)
    return extend_core_colors(height, matching, left, right, order, colors)


def check(height, mode, chunk, direct, three=False):
    n = (height + 1) // 2
    size = 1 << (n - 1).bit_length()
    sigma = permutation(size, mode)
    inverse = np.argsort(sigma).astype(np.int32)
    assert np.array_equal(sigma[inverse], np.arange(size))
    legs = leg_table(height)
    oriented_count = 0
    simple_count = 0
    first_core = None
    smallest_core = None
    three_unsat = []
    core_hist = {}
    color_hist = {}
    digest = hashlib.sha256()
    for start in range(0, size, chunk):
        stop = min(size, start + chunk)
        offsets = np.zeros(stop - start + 1, dtype=np.int64)
        empty = np.empty(0, dtype=np.int32)
        oriented_count += enumerate_edges(
            height, sigma, inverse, legs, start, stop, offsets, empty, empty, False
        )
        offsets = np.cumsum(offsets)
        simple_count += int(offsets[-1])
        left = np.empty(offsets[-1], dtype=np.int32)
        right = np.empty_like(left)
        cur = offsets[:-1].copy()
        enumerate_edges(height, sigma, inverse, legs, start, stop, cur, left, right, True)
        assert np.array_equal(cur, offsets[1:])
        for matching in range(start, stop):
            lo, hi = offsets[matching - start : matching - start + 2]
            numbers, order, colors = color_matching(height, matching, lo, hi, left, right)
            core = int(numbers.max())
            if core >= 3:
                vertices = np.flatnonzero(numbers >= 3).astype("<i4")
                if smallest_core is None or len(vertices) < smallest_core["vertices"]:
                    inside = (numbers[left[lo:hi]] >= 3) & (numbers[right[lo:hi]] >= 3)
                    record = dict(matching=matching, vertices=len(vertices), edges=int(inside.sum()),
                                  vertex_sha256=hashlib.sha256(vertices.tobytes()).hexdigest())
                    if len(vertices) <= 64:
                        record["indices"] = vertices.tolist()
                    if first_core is None:
                        first_core = record
                    smallest_core = record
                if three and colors.max() >= 3:
                    result = color_three_core(height, matching, left[lo:hi], right[lo:hi],
                                              numbers, order)
                    if result is None:
                        three_unsat.append(matching)
                    else:
                        colors = result
            if direct:
                edges = {
                    (min(i, j), max(i, j)) for i, j in zip(left[lo:hi], right[lo:hi])
                }
                brute = set()
                for i in range(n):
                    if (i ^ matching) >= height // 2:
                        continue
                    for j in range(n):
                        if i == j or (j ^ matching) >= height // 2:
                            continue
                        dx = 8 * (int(sigma[i]) - int(sigma[j]))
                        dy = 2 * i - 2 * (j ^ matching) - 1
                        value = dx * dx + dy * dy
                        z = isqrt(value)
                        if z < height and z * z == value:
                            brute.add((min(i, j), max(i, j)))
                assert brute == edges
            count = int(colors.max()) + 1
            core_hist[int(core)] = core_hist.get(int(core), 0) + 1
            color_hist[count] = color_hist.get(count, 0) + 1
            digest.update(colors.astype("<i2", copy=False).tobytes())
    return dict(height=height, mode=mode, matchings=size, oriented_events=oriented_count,
                simple_edges=simple_count, core_histogram=core_hist,
                palette_histogram=color_hist, color_sha256=digest.hexdigest(),
                first_core=first_core, smallest_core=smallest_core,
                three_color_unsat=three_unsat if three else None)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("height", type=int)
    parser.add_argument("--mode", choices=("tree", "wrapped", "identity"), default="tree")
    parser.add_argument("--chunk", type=int, default=1024)
    parser.add_argument("--direct", action="store_true", help="check each pair in each matching")
    parser.add_argument("--three", action="store_true", help="solve each nontrivial 3-core")
    args = parser.parse_args()
    if args.height < 2 or args.chunk < 1:
        parser.error("height must be at least 2 and chunk must be positive")
    print(json.dumps(check(args.height, args.mode, args.chunk, args.direct, args.three), sort_keys=True))

