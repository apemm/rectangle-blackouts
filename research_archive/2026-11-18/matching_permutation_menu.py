"""Try binary tree permutations until the matching has an empty 3-core."""

import argparse
import hashlib
import json

import numpy as np

from dyadic_matching_check import color_matching, enumerate_edges, leg_table
from lift_one_matching import lift, seeded_tree


def check_menu(height, last_seed, chunk):
    n = 1 << (((height + 1) // 2) - 1).bit_length()
    legs = leg_table(height)
    sigma = seeded_tree(n, 0)
    inverse = np.argsort(sigma).astype(np.int32)
    empty = np.empty(0, dtype=np.int32)
    seed_used = np.full(n, -1, dtype=np.int16)
    residual = []
    for start in range(0, n, chunk):
        stop = min(start + chunk, n)
        offsets = np.zeros(stop - start + 1, dtype=np.int64)
        enumerate_edges(height, sigma, inverse, legs, start, stop, offsets, empty, empty, False)
        offsets = np.cumsum(offsets)
        left = np.empty(offsets[-1], dtype=np.int32)
        right = np.empty_like(left)
        current = offsets[:-1].copy()
        enumerate_edges(height, sigma, inverse, legs, start, stop, current, left, right, True)
        assert np.array_equal(current, offsets[1:])
        for t in range(start, stop):
            lo, hi = offsets[t - start : t - start + 2]
            numbers, _, _ = color_matching(height, t, lo, hi, left, right)
            if numbers.max() >= 3:
                residual.append(t)
            else:
                seed_used[t] = 0
    histogram = [len(residual)]
    print(json.dumps(dict(seed=0, remaining=len(residual))), flush=True)
    left = np.empty(4 * n, dtype=np.int32)
    right = np.empty_like(left)
    for seed in range(1, last_seed + 1):
        if not residual:
            break
        sigma = seeded_tree(n, seed)
        next_residual = []
        for t in residual:
            count, _, _ = lift(height, sigma, t, legs, left, right)
            if count > len(left):
                left = np.empty(count, dtype=np.int32)
                right = np.empty_like(left)
                actual, _, _ = lift(height, sigma, t, legs, left, right)
                assert actual == count
            numbers, _, _ = color_matching(height, t, 0, count, left, right)
            if numbers.max() >= 3:
                next_residual.append(t)
            else:
                seed_used[t] = seed
        residual = next_residual
        histogram.append(len(residual))
        print(json.dumps(dict(seed=seed, remaining=len(residual))), flush=True)
    return dict(height=height, matchings=n, residual_counts=histogram,
                remaining=residual, seed_sha256=hashlib.sha256(seed_used.astype("<i2").tobytes()).hexdigest())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("height", type=int)
    parser.add_argument("--last-seed", type=int, default=10)
    parser.add_argument("--chunk", type=int, default=1024)
    args = parser.parse_args()
    if args.height < 2 or args.chunk < 1 or not 0 <= args.last_seed <= 32767:
        parser.error("height, chunk, or seed count outside its range")
    print(json.dumps(check_menu(args.height, args.last_seed, args.chunk), sort_keys=True))
