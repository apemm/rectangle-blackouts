"""Exact finite-domain solve for recorded translated-patch cores."""
import argparse
from collections import defaultdict
import json
from pathlib import Path


def solve(vertices, edges, M=3, node_limit=1000000):
    neighbors = defaultdict(set)
    forbidden = defaultdict(set)
    for r, s, delta in edges:
        neighbors[r].add(s)
        neighbors[s].add(r)
        forbidden[r, s].add(delta)
        forbidden[s, r].add(-delta)
    nodes = 0

    def search(domains):
        nonlocal nodes
        nodes += 1
        if nodes > node_limit:
            raise RuntimeError("node limit exceeded; no conclusion")
        changed = True
        while changed:
            changed = False
            for (r, s), blocked in forbidden.items():
                supported = {a for a in domains[r]
                             if any(b - a not in blocked for b in domains[s])}
                if not supported:
                    return None
                if supported != domains[r]:
                    domains[r] = supported
                    changed = True
        undecided = [r for r in vertices if len(domains[r]) > 1]
        if not undecided:
            return {r: next(iter(domains[r])) for r in vertices}
        r = min(undecided, key=lambda x: (len(domains[x]), -len(neighbors[x]), x))
        for a in sorted(domains[r]):
            branch = {s: values.copy() for s, values in domains.items()}
            branch[r] = {a}
            answer = search(branch)
            if answer is not None:
                return answer
        return None

    answer = search({r: set(range(M)) for r in vertices})
    if answer is not None:
        assert all(answer[s] - answer[r] != delta for r, s, delta in edges)
    return answer, nodes


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    source = json.loads(args.input.read_text())
    results = []
    for ex in source["examples"]:
        answer, nodes = solve(ex["core_vertices"], ex["core_edges"], source["M"])
        results.append({"D": ex["D"], "vertices": len(ex["core_vertices"]),
                        "edges": len(ex["core_edges"]), "nodes": nodes,
                        "satisfiable": answer is not None, "assignment": answer})
    args.out.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps([{k: v for k, v in r.items() if k != "assignment"} for r in results]))
