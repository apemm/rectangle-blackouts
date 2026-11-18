"""Generate one matching graph by lifting column equations one binary digit at a time."""

import argparse
import hashlib
import json

import numpy as np
from numba import njit

from dyadic_matching_check import color_matching, color_three_core, leg_table, permutation, tree_hash


def seeded_tree(size, seed):
    if not seed:
        return permutation(size, "tree")
    sigma = np.zeros(size, dtype=np.int32)
    for bit in range(size.bit_length() - 1):
        place = 1 << bit
        for i in range(size):
            key = (place - 1 + (i & (place - 1))) ^ tree_hash(seed)
            flip = tree_hash(key) & 1
            sigma[i] |= (i & place) ^ (flip * place)
    return sigma


@njit(cache=False)
def lift(height, sigma, matching, legs, left, right):
    n = len(sigma)
    odd_count, even_count = (height + 1) // 2, height // 2
    places = np.empty(64, dtype=np.int64)
    points = np.empty(64, dtype=np.int64)
    events = 0
    simple = 0
    examined = 0
    for r, d in legs:
        for sx in (-1, 1):
            for sy in (-1, 1):
                shift = (sy * d - 1) // 2
                places[0], points[0] = 1, 0
                stack = 1
                while stack:
                    stack -= 1
                    place, i = places[stack], points[stack]
                    examined += 1
                    if place < n:
                        mask = 2 * place - 1
                        # The next bit is the same test for both sibling candidates.
                        j0 = ((i + shift) ^ matching) & mask
                        if (sigma[j0] - sigma[i] - sx * r) & mask:
                            continue
                        places[stack], points[stack] = 2 * place, i
                        places[stack + 1], points[stack + 1] = 2 * place, i + place
                        stack += 2
                        continue
                    k = i + shift
                    if i >= odd_count or k < 0 or k >= even_count:
                        continue
                    j = k ^ matching
                    if j >= odd_count or (i ^ matching) >= even_count:
                        continue
                    if sigma[j] - sigma[i] != sx * r:
                        continue
                    events += 1
                    if j < i:
                        reverse_y = 2 * j - 2 * (i ^ matching) - 1
                        norm = 64 * r * r + reverse_y * reverse_y
                        z = int(np.sqrt(norm))
                        if z < height and z * z == norm:
                            continue
                    if simple < len(left):
                        left[simple], right[simple] = i, j
                    simple += 1
    return simple, events, examined


def inspect(height, matching, seed, three):
    n = 1 << (((height + 1) // 2) - 1).bit_length()
    if matching < 0 or matching >= n:
        raise ValueError("matching index outside the padded square")
    sigma = seeded_tree(n, seed)
    legs = leg_table(height)
    capacity = 4 * n
    while True:
        left = np.empty(capacity, dtype=np.int32)
        right = np.empty(capacity, dtype=np.int32)
        count, events, states = lift(height, sigma, matching, legs, left, right)
        if count <= capacity:
            break
        capacity = count
    left, right = left[:count], right[:count]
    numbers, order, colors = color_matching(height, matching, 0, count, left, right)
    sat = None
    if three and int(colors.max()) >= 3:
        result = color_three_core(height, matching, left, right, numbers, order)
        sat = result is not None
        if sat:
            colors = result
    core = np.flatnonzero(numbers >= 3).astype("<i4")
    inside = (numbers[left] >= 3) & (numbers[right] >= 3)
    return dict(height=height, matching=matching, seed=seed, examined_states=states,
                oriented_events=events, simple_edges=count, degeneracy=int(numbers.max()),
                three_core_vertices=len(core), three_core_edges=int(inside.sum()),
                three_core_sha256=hashlib.sha256(core.tobytes()).hexdigest(),
                colors=int(colors.max()) + 1, three_sat=sat,
                color_sha256=hashlib.sha256(colors.astype("<i2").tobytes()).hexdigest())


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("height", type=int)
    p.add_argument("matching", type=int)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--three", action="store_true")
    a = p.parse_args()
    print(json.dumps(inspect(a.height, a.matching, a.seed, a.three), sort_keys=True))

