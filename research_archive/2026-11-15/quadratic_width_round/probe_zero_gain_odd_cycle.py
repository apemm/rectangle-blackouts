"""Extract an odd cycle and give direct norm witnesses for every edge."""
from collections import deque
from pathlib import Path
from math import isqrt
import argparse
import json
import numpy as np
from probe_hilbert_rank_difference_automaton import cell, action


def find_cycle(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, _ in edges:
        adj[int(u)].append(int(v))
        adj[int(v)].append(int(u))
    color = [-1] * n
    parent = [-1] * n
    depth = [0] * n
    for root in range(n):
        if color[root] >= 0 or not adj[root]:
            continue
        color[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] < 0:
                    color[v] = 1 - color[u]
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    queue.append(v)
                elif color[v] == color[u]:
                    a, b = u, v
                    left, right = [a], [b]
                    while depth[a] > depth[b]:
                        a = parent[a]
                        left.append(a)
                    while depth[b] > depth[a]:
                        b = parent[b]
                        right.append(b)
                    while a != b:
                        a, b = parent[a], parent[b]
                        left.append(a)
                        right.append(b)
                    cycle = left + right[-2::-1]
                    assert len(cycle) % 2 == 1
                    return cycle
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('events', type=Path)
    ap.add_argument('--side', type=int, required=True)
    ap.add_argument('--offset', type=int, required=True)
    ap.add_argument('--choices', type=int, default=3)
    ap.add_argument('--outer', type=int, default=0)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    edges = np.load(args.events)
    edges = edges[edges[:, 2] == 0]
    cycle = find_cycle(args.side ** 2, edges)
    result = {'side': args.side, 'offset': args.offset, 'choices': args.choices,
              'outer': args.outer, 'zero_events': len(edges), 'cycle': cycle}
    if cycle:
        witnesses = []
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            r, s = sorted((u, v))
            a = action(args.outer, *cell(args.side, r), args.side - 1)
            b = action(args.outer, *cell(args.side, s), args.side - 1)
            x = 32 * args.choices * (s - r)
            found = []
            for role, y in enumerate((2 * args.offset + 1 + 2 * (b[1] - a[0]),
                                      2 * args.offset + 1 + 2 * (a[1] - b[0]))):
                l = isqrt(x * x + y * y)
                if l * l == x * x + y * y:
                    found.append({'role': role, 'X': x, 'Y': y, 'L': l})
            assert found
            witnesses.append({'r': r, 's': s, 'cell_r': a, 'cell_s': b,
                              'norms': found})
        result['witnesses'] = witnesses
        result['status'] = 'ODD_CYCLE_DIRECT_NORMS_CHECKED'
    else:
        result['status'] = 'ZERO_GRAPH_BIPARTITE'
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'witnesses'}), flush=True)


if __name__ == '__main__':
    main()
