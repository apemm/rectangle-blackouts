"""Exact star elimination for three integer Hilbert slot choices at stride 32.

Build all signed norm events with the archived rank-lag generator. The kernel
uses actual endpoint differences. Save only small result records.
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys

import numpy as np
from numba import njit

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "2026-11-15" / "quadratic_width_round"))
from probe_hilbert_rank_difference_automaton import enumerate_lag, odd_legs


def pairs(side):
    n = side * side
    offset = -2 * side
    chunks = []
    for q, y in odd_legs(6 * side - 3, 32, 3 * n - 1):
        # Y ranges from 2s+1 to 6s-3, with negative signed difference.
        k = (-y - 2 * offset - 1) // 2
        if abs(k) >= side:
            continue
        for lag in {q // 3, (q + 2) // 3}:
            if not 0 < lag < n:
                continue
            delta = q - 3 * lag
            for role in (0, 1):
                hits = enumerate_lag(side, lag, k, role, 0)
                if hits:
                    r = np.asarray(hits, dtype=np.int64)
                    chunks.append(((r * n + r + lag) << 3) + delta + 2)
    if not chunks:
        return np.zeros((0, 2), np.int32), np.zeros(0, np.uint8)
    packed = np.concatenate(chunks)
    del chunks
    packed.sort()
    keys = packed >> 3
    starts = np.r_[0, np.flatnonzero(keys[1:] != keys[:-1]) + 1]
    masks = np.bitwise_or.reduceat((1 << (packed & 7)).astype(np.uint8), starts)
    key = keys[starts]
    return np.column_stack((key // n, key % n)).astype(np.int32), masks


def transitions():
    # Mask bit delta+2 means neighbor minus center = delta is forbidden.
    table = np.zeros((32, 256), dtype=np.uint8)
    for mask in range(32):
        bans = [sum(1 << c for c in range(3) if mask & (1 << (d - c + 2)))
                for d in range(3)]
        for states in range(256):
            nxt = 0
            for prior in range(8):
                if states & (1 << prior):
                    for ban in bans:
                        nxt |= 1 << (prior | ban)
            table[mask, states] = nxt
    return table


@njit(cache=False)
def robust_vertex(v, offsets, adj, masks, active, table):
    states = 1
    for j in range(offsets[v], offsets[v+1]):
        if active[adj[j]]:
            states = table[masks[j], states]
            if states & 128:
                return False
    return True


@njit(cache=False)
def peel(n, edges, pair_masks, table):
    offsets = np.zeros(n+1, np.int32)
    for u,v in edges:
        offsets[u+1] += 1
        offsets[v+1] += 1
    offsets = np.cumsum(offsets)
    idx = offsets[:-1].copy()
    adj = np.empty(2*len(edges), np.int32)
    masks = np.empty(2*len(edges), np.uint8)
    for e in range(len(edges)):
        u,v = edges[e]
        mask = pair_masks[e]
        rev = 0
        for i in range(5):
            if mask & (1 << i):
                rev |= 1 << (4-i)
        adj[idx[u]], masks[idx[u]] = v, mask
        adj[idx[v]], masks[idx[v]] = u, rev
        idx[u] += 1
        idx[v] += 1
    active = np.ones(n, np.bool_)
    queue = np.empty(n, np.int32)
    front = end = 0
    for u in range(n):
        if robust_vertex(u, offsets, adj, masks, active, table):
            active[u] = False
            queue[end] = u
            end += 1
    while front < end:
        u = queue[front]
        front += 1
        for j in range(offsets[u],offsets[u+1]):
            v = adj[j]
            if active[v] and robust_vertex(v, offsets, adj, masks, active, table):
                active[v] = False
                queue[end] = v
                end += 1
    return active, queue[:end]


@njit(cache=False)
def greedy(n, edges, pair_masks, order):
    offsets = np.zeros(n+1, np.int32)
    for u,v in edges:
        offsets[u+1] += 1
        offsets[v+1] += 1
    offsets = np.cumsum(offsets)
    idx = offsets[:-1].copy()
    incidence = np.empty(2*len(edges), np.int32)
    for e in range(len(edges)):
        for v in edges[e]:
            incidence[idx[v]] = e
            idx[v] += 1
    colors = np.full(n, -1, np.int8)
    for v in order[::-1]:
        allowed = 7
        for j in range(offsets[v], offsets[v+1]):
            e = incidence[j]
            u, w = edges[e]
            other = w if u == v else u
            if colors[other] < 0:
                continue
            for c in range(3):
                d = colors[other]-c if u == v else c-colors[other]
                if pair_masks[e] & (1 << (d+2)):
                    allowed &= ~(1 << c)
        assert allowed
        colors[v] = 0 if allowed & 1 else (1 if allowed & 2 else 2)
    for e in range(len(edges)):
        u, v = edges[e]
        assert not (pair_masks[e] & (1 << (colors[v]-colors[u]+2)))
    return colors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sides', nargs='+', type=int)
    args = ap.parse_args()
    lookup = transitions()
    for s in args.sides:
        edges, masks = pairs(s)
        active, order = peel(s*s, edges, masks, lookup)
        in_core = active[edges[:,0]] & active[edges[:,1]]
        modular = sum(len({(i-2)%3 for i in range(5) if k & (1<<i)}) * int(v)
                      for k,v in enumerate(np.bincount(masks, minlength=32)))
        rec = dict(side=s, pairs=len(edges), modular_events=modular,
                   core_vertices=int(active.sum()), core_pairs=int(in_core.sum()))
        if not active.any():
            colors = greedy(s*s,edges,masks,order)
            rec['checked_full_greedy_coloring'] = True
        print(json.dumps(rec), flush=True)
        (HERE / f'star_side{s}.json').write_text(json.dumps(rec,indent=2)+'\n')


if __name__ == '__main__':
    main()
