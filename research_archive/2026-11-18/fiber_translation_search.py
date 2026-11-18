"""Search independent fiber translations and check all three-label tilted corners."""
import argparse
import hashlib
import json
from math import gcd
from pathlib import Path
import random

import numpy as np
from numba import njit

from check_ternary_placement import columns

HERE = Path(__file__).resolve().parent


def group_key(odd, even):
    scale = 1
    while (even - odd) % (3*scale) == 0:
        scale *= 3
    w = odd % scale
    a, b = (odd-w)//scale, (even-w)//scale
    if (b-a) % 6 != 1:
        a, b = b, a
    return scale, a % 6, b % 6, w


class Layout:
    def __init__(self, h, stride):
        self.h = h
        labels = np.array(columns(h, stride), dtype=np.int64)
        keys = [group_key(int(a), int(b)) for _, a, b in labels]
        self.keys = sorted(set(keys))
        ids = {key: k for k, key in enumerate(self.keys)}
        self.groups = np.array([ids[key] for key in keys], dtype=np.int64)
        self.scales = np.array([key[0] for key in self.keys], dtype=np.int64)
        self.labels = labels
        self.runs = []
        start = 0
        for pos in range(1, len(keys)+1):
            if pos == len(keys) or keys[pos][:3] != keys[start][:3]:
                scale = keys[start][0]
                segment = labels[start:pos, 0]
                segment -= int(segment.min())//(4*scale)*(4*scale)
                self.runs.append((start, pos, scale))
                start = pos

    def place(self, shifts):
        labels = self.labels.copy()
        labels[:, 0] += (4*self.scales*shifts)[self.groups]
        next_start = 0
        for begin, end, scale in self.runs:
            sub = labels[begin:end, 0]
            origin = (next_start + 4*scale-1)//(4*scale)*(4*scale)
            sub += origin
            next_start = int(sub.max()) + self.h*self.h//(2*scale) + 1
        order = np.argsort(labels[:, 0])
        result = labels[order]
        assert np.all(np.diff(result[:, 0]) > 0)
        return result, self.groups[order]


@njit(cache=False)
def find_corners(labels, groups, h, cap):
    n = len(labels)
    lookup = {labels[i, 0]: i for i in range(n)}
    examples = np.zeros((cap, 10), np.int64)
    total = single_fiber = 0
    for i in range(n):
        x = labels[i, 0]
        j = i+1
        while j < n and 2*(labels[j, 0] - x) <= h-1:
            xx = labels[j, 0]
            dx = xx - x
            for a in (1, 2):
                for b in (1, 2):
                    y, yy = labels[i, a], labels[j, b]
                    dy = yy-y
                    if dy == 0:
                        continue
                    g = gcd(dx, abs(dy))
                    ux, uy = -dy//g, dx//g
                    multiple = 4//gcd(4, abs(ux))
                    ux *= multiple
                    uy *= multiple
                    for pivot in (0, 1):
                        vx, vy = (x,y) if pivot == 0 else (xx,yy)
                        wx, wy = (xx,yy) if pivot == 0 else (x,y)
                        for sign in (-1, 1):
                            sx, sy = sign*ux, sign*uy
                            limit = ((h-max(vy,wy))//sy if sy > 0
                                     else (min(vy,wy)-1)//(-sy))
                            for step in range(1, limit+1):
                                zx, zy = vx+step*sx, vy+step*sy
                                if abs(step*sx) < dx or (abs(step*sx) == dx and zx < wx):
                                    continue
                                k = lookup[zx] if zx in lookup else -1
                                if k < 0 or (labels[k,1] != zy and labels[k,2] != zy):
                                    continue
                                locked = groups[i] == groups[j] and groups[i] == groups[k]
                                if total < cap:
                                    examples[total] = np.array((groups[i],groups[j],groups[k],
                                        vx,vy,wx,wy,zx,zy,locked))
                                total += 1
                                single_fiber += locked
            j += 1
    return total, single_fiber, examples[:min(cap,total)]


def search(h, stride, seed, rounds, output):
    layout = Layout(h, stride)
    rng = random.Random(seed)
    shifts = np.zeros(len(layout.keys), dtype=np.int64)
    history = []
    for iteration in range(rounds+1):
        labels, groups = layout.place(shifts)
        count, locked, conflicts = find_corners(labels, groups, h, 20000)
        row = dict(iteration=iteration, corners=count, within_fiber=locked)
        history.append(row)
        print(h, stride, json.dumps(row), flush=True)
        if not count or locked or iteration == rounds:
            digest = hashlib.sha256(labels.astype('<i8', copy=False).tobytes()).hexdigest()
            record = dict(height=h, stride=stride, seed=seed, history=history,
                          labels=len(labels), width=int(labels[-1,0]-labels[0,0]+1),
                          assignment_sha256=digest, example=conflicts[:1].tolist(),
                          translations=[[*key, int(v)] for key,v in zip(layout.keys,shifts) if v])
            if output:
                with (HERE / f'fiber_search_{h}_{stride}_{seed}.json').open('x') as stream:
                    json.dump(record, stream, indent=2)
                    stream.write('\n')
            return record
        changed = set()
        order = list(range(len(conflicts)))
        rng.shuffle(order)
        for pos in order:
            ids = {int(i) for i in conflicts[pos,:3]}
            if ids.isdisjoint(changed):
                # A leg inside one fiber fixes that fiber's geometry. Moving the
                # singleton participant changes the relative displacement.
                ids_list = list(conflicts[pos,:3])
                choices = sorted(i for i in ids if ids_list.count(i) == 1)
                group = rng.choice(choices)
                old = int(shifts[group])
                shift = rng.randrange(h)
                shifts[group] = shift + (shift >= old)
                changed.add(group)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('heights', nargs='+', type=int)
    p.add_argument('--stride', type=int, default=96)
    p.add_argument('--seed', type=int, default=186)
    p.add_argument('--rounds', type=int, default=40)
    p.add_argument('--save', action='store_true')
    args = p.parse_args()
    for height in args.heights:
        search(height, args.stride, args.seed, args.rounds, args.save)
