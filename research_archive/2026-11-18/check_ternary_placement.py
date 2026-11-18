"""Construct the ternary placement and directly test every pair of label columns."""
from itertools import combinations
from math import isqrt
import sys

from ternary_graph import color, coords, edges


def columns(h, stride, shear=0):
    runs = {}
    for odd in range(1, h + 1, 2):
        for even in range(2, h + 1, 2):
            scale = 1
            while (even - odd) % (3 * scale) == 0:
                scale *= 3
            w = odd % scale
            a, b = (odd - w) // scale, (even - w) // scale
            if (b - a) % 6 != 1:
                a, b = b, a
            alpha, beta = a % 6, b % 6
            assert (beta - alpha) % 6 == 1
            k = (beta - alpha - 1) // 6
            i, j = a // 6 + 1, b // 6 + k + 1
            runs.setdefault((scale, alpha, beta), []).append((w, i, j, odd, even))

    profiles, labels = {}, []
    next_start = 0
    for (scale, _, _), members in sorted(runs.items()):
        size = h // (6 * scale) + 2
        side = 1 << (size - 1).bit_length()
        if side not in profiles:
            i, j = coords(side)
            ranks = {(int(a), int(b)): r for r, (a, b) in enumerate(zip(i, j))}
            core, colors = color(side*side, edges(side, stride))
            assert core == 0
            profiles[side] = ranks, colors
        ranks, colors = profiles[side]
        start = (next_start + 4*scale - 1) // (4*scale) * (4*scale)
        last = start
        for w, i, j, a, b in members:
            rank = ranks[i, j]
            x = start + scale*(stride*rank + 4*int(colors[rank])) + 4*w + 4*scale*shear*w
            labels.append((x, a, b))
            last = max(last, x)
        next_start = last + h*h // (2*scale) + 1
    return labels


def check(h, stride):
    labels = columns(h, stride)
    assert len(labels) == h*h // 4
    assert len({x for x, _, _ in labels}) == len(labels)
    assert all(x % 4 == 0 for x, _, _ in labels)
    assert {(a, b) for _, a, b in labels} == {
        (a, b) for a in range(1, h + 1, 2) for b in range(2, h + 1, 2)}
    pairs = 0
    for (x, a, b), (xx, aa, bb) in combinations(labels, 2):
        for dy in (a - bb, aa - b):
            norm = (x - xx)**2 + dy**2
            assert isqrt(norm)**2 != norm, (h, x, xx, dy)
            pairs += 1
    width = max(v[0] for v in labels) - min(v[0] for v in labels) + 1
    return len(labels), pairs, width


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        h = int(arg)
        print(h, *check(h, 96), flush=True)
