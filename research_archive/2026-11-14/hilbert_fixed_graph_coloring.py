"""Inspect actual P edges of an unjittered full Hilbert label family."""
import argparse
from collections import defaultdict, deque
import json
from pathlib import Path
import numpy as np
from hilbert_finite_choice_search import hilbert_array
from hilbert_two_choice_rivals import pythagorean_rows


def inspect(h, S=32):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    inverse = np.empty((q, q), dtype=np.int64)
    inverse[xy[:, 0], xy[:, 1]] = np.arange(q * q)
    edges = set()
    for d in range(1, (h - 1) // S + 1):
        ys = pythagorean_rows(S * d, h)
        if not ys:
            continue
        hyp = np.zeros(2 * q + 2, dtype=np.int64)
        for y, L in ys.items():
            hyp[abs(y)] = L
        for a, b in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
            L = hyp[np.abs(b - a)]
            total = a + b
            hit = (L > 0) & (total - L >= 2) & (total + L <= 2 * h)
            hit &= active[:-d] & active[d:]
            ranks = np.nonzero(hit)[0]
            low, high = (total[ranks] - L[ranks]) // 2, (total[ranks] + L[ranks]) // 2
            o = np.where(low % 2, low, high)
            e = np.where(low % 2, high, low)
            owner = inverse[(o - 1) // 2, (e - 2) // 2]
            for r in ranks[2 * owner != 2 * ranks + d]:
                edges.add((int(r), int(r) + d))
    graph = defaultdict(list)
    rank_tm_bad, coord_tm_bad = [], []
    for r, s in sorted(edges):
        graph[r].append(s)
        graph[s].append(r)
        if r.bit_count() % 2 == s.bit_count() % 2 and len(rank_tm_bad) < 4:
            rank_tm_bad.append([r, s])
        rc = tuple(int(v).bit_count() % 2 for v in xy[r])
        sc = tuple(int(v).bit_count() % 2 for v in xy[s])
        if rc == sc and len(coord_tm_bad) < 4:
            coord_tm_bad.append([r, s])
    colors, parent = {}, {}
    cycle = []
    for start in graph:
        if start in colors:
            continue
        colors[start], parent[start] = 0, None
        queue = deque([start])
        while queue and not cycle:
            r = queue.popleft()
            for s in graph[r]:
                if s not in colors:
                    colors[s], parent[s] = 1 - colors[r], r
                    queue.append(s)
                elif colors[s] == colors[r]:
                    path_r, path_s = [r], [s]
                    while parent[path_r[-1]] is not None:
                        path_r.append(parent[path_r[-1]])
                    while parent[path_s[-1]] is not None:
                        path_s.append(parent[path_s[-1]])
                    while path_r[-1] == path_s[-1]:
                        lca = path_r.pop()
                        path_s.pop()
                        if not path_r or not path_s:
                            break
                    cycle = path_r + [lca] + path_s[::-1]
                    break
        if cycle:
            break
    return {"h": h, "S": S, "actual_edges": len(edges),
            "incident_labels": len(graph), "bipartite": not cycle,
            "odd_cycle_ranks": cycle, "odd_cycle_coordinates": [xy[r].tolist() for r in cycle],
            "rank_thue_morse_counterexamples": rank_tm_bad,
            "coordinate_thue_morse_counterexamples": coord_tm_bad}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("h", type=int)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    result = inspect(args.h)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
