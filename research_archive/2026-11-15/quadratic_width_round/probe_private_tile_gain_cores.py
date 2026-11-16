"""Structural reductions of complete finite private-slot systems."""
from collections import Counter, defaultdict, deque
from pathlib import Path
import argparse
import json
import time

from check_all_offset_private_tiles_independent import independent_systems


def gains_from_events(events):
    out = defaultdict(set)
    for r, s, delta in events:
        out[r, s].add(delta % 3)
    return dict(out)


def peel(edges):
    adjacency = defaultdict(dict)
    for (r, s), gains in edges.items():
        assert r != s
        adjacency[r][s] = len(gains)
        adjacency[s][r] = len(gains)
    degree = {r: sum(row.values()) for r, row in adjacency.items()}
    queue = deque(r for r, deg in degree.items() if deg <= 2)
    alive = set(degree)
    order = []
    while queue:
        r = queue.popleft()
        if r not in alive:
            continue
        alive.remove(r)
        order.append(r)
        for s, weight in adjacency[r].items():
            if s in alive:
                degree[s] -= weight
                if degree[s] <= 2:
                    queue.append(s)
    return {key: gains for key, gains in edges.items()
            if key[0] in alive and key[1] in alive}, order


def force_contract(edges):
    """One round, with exact mod-3 potentials relative to DSU roots."""
    vertices = {r for pair in edges for r in pair}
    parent = {r: r for r in vertices}
    potential = dict.fromkeys(vertices, 0)

    def find(r):
        if parent[r] != r:
            old = parent[r]
            parent[r], p = find(old)
            potential[r] = (potential[r] + p) % 3
        return parent[r], potential[r]

    contractions = 0
    for (r, s), gains in edges.items():
        assert len(gains) < 3, ('empty binary relation', r, s)
        if len(gains) != 2:
            continue
        allowed, = set(range(3)) - gains
        rr, pr = find(r)
        ss, ps = find(s)
        if rr == ss:
            assert (ps - pr) % 3 == allowed, 'inconsistent forced cycle'
        else:
            parent[ss] = rr
            potential[ss] = (allowed - ps + pr) % 3
            contractions += 1
    out = defaultdict(set)
    for (r, s), gains in edges.items():
        rr, pr = find(r)
        ss, ps = find(s)
        reduced = {(g - ps + pr) % 3 for g in gains}
        if rr == ss:
            assert 0 not in reduced, 'forbidden forced difference'
            continue
        if rr > ss:
            rr, ss = ss, rr
            reduced = {(-g) % 3 for g in reduced}
        out[rr, ss].update(reduced)
    return dict(out), contractions


def reduce_system(edges):
    core, peeled = peel(edges)
    raw_core = core
    contractions = rounds = 0
    while core:
        if not any(len(g) == 2 for g in core.values()):
            break
        core, count = force_contract(core)
        contractions += count
        rounds += 1
        core, more = peel(core)
        peeled += more
    return core, raw_core, contractions, rounds


def compact(edges, cells=None):
    vertices = sorted({v for pair in edges for v in pair})
    renumber = {v: i for i, v in enumerate(vertices)}
    result = {'vertices': vertices,
              'edges': [[renumber[r], renumber[s], sorted(g)]
                        for (r, s), g in sorted(edges.items())]}
    if cells:
        result['cells'] = [cells[v] for v in vertices]
    return result


def binary_solution(edges):
    """Restrict every remaining color to {0,1}; use exact 2-SAT SCCs."""
    vertices = sorted({v for pair in edges for v in pair})
    number = {v: i for i, v in enumerate(vertices)}
    graph = [[] for _ in range(2 * len(vertices))]
    reverse = [[] for _ in graph]
    for (r, s), gains in edges.items():
        for a in (0, 1):
            for b in (0, 1):
                if (b - a) % 3 not in gains:
                    continue
                # The pair (r=a,s=b) is forbidden.
                for u, v in ((2 * number[r] + a, 2 * number[s] + 1 - b),
                             (2 * number[s] + b, 2 * number[r] + 1 - a)):
                    graph[u].append(v)
                    reverse[v].append(u)
    order = []
    seen = set()
    def dfs(u):
        seen.add(u)
        for v in graph[u]:
            if v not in seen:
                dfs(v)
        order.append(u)
    for u in range(len(graph)):
        if u not in seen:
            dfs(u)
    component = {}
    def visit(u, c):
        component[u] = c
        for v in reverse[u]:
            if v not in component:
                visit(v, c)
    for u in reversed(order):
        if u not in component:
            visit(u, len(component))
    if any(component[2 * i] == component[2 * i + 1] for i in range(len(vertices))):
        return None
    values = {v: int(component[2 * i + 1] > component[2 * i])
              for v, i in number.items()}
    assert all((values[s] - values[r]) % 3 not in g
               for (r, s), g in edges.items())
    return values


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--side', type=int, default=16)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    started = time.monotonic()
    systems, cells, _ = independent_systems(args.side, 32, 3)
    stats = Counter()
    raw_sizes = Counter()
    final_sizes = Counter()
    raw_examples = []
    final_examples = []
    for t, events in systems.items():
        gains = gains_from_events(events)
        core, raw, contractions, rounds = reduce_system(gains)
        stats['offsets'] += 1
        stats['maximum_contraction_rounds'] = max(stats['maximum_contraction_rounds'], rounds)
        stats['maximum_contracted_vertices'] = max(stats['maximum_contracted_vertices'], contractions)
        if raw:
            stats['weighted_core_offsets'] += 1
            nv = len({v for pair in raw for v in pair})
            raw_sizes[nv] += 1
            raw_examples.append((nv, len(raw), abs(t), t, raw))
            raw_examples.sort(key=lambda z: z[:4])
            del raw_examples[20:]
        else:
            stats['weighted_two_degenerate_offsets'] += 1
        if core:
            stats['unresolved_offsets'] += 1
            nv = len({v for pair in core for v in pair})
            final_sizes[nv] += 1
            final_examples.append((nv, len(core), abs(t), t, core))
            final_examples.sort(key=lambda z: z[:4])
            del final_examples[30:]
        else:
            stats['reduction_solved_offsets'] += 1
    output = {
        'side': args.side, 'statistics': dict(stats),
        'raw_core_size_histogram': dict(sorted(raw_sizes.items())),
        'final_core_size_histogram': dict(sorted(final_sizes.items())),
        'small_raw_cores': [{'offset': t, **compact(e, cells)}
                          for _, _, _, t, e in raw_examples],
        'small_final_cores': [{'offset': t, **compact(e, cells)}
                            for _, _, _, t, e in final_examples],
        'seconds': round(time.monotonic() - started, 3),
    }
    for item in output['small_final_cores']:
        edge_map = {(a, b): set(g) for a, b, g in item['edges']}
        solution = binary_solution(edge_map)
        item['binary_assignment'] = None if solution is None else [solution[i] for i in range(len(item['vertices']))]
        item['gain_histogram'] = dict(Counter(g for _, _, gs in item['edges'] for g in gs))
    args.out.write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({k: output[k] for k in ['statistics', 'raw_core_size_histogram',
                                            'final_core_size_histogram', 'seconds']}, indent=2))


if __name__ == '__main__':
    main()
