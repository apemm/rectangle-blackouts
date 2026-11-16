"""Exact small-state probe for affine intersections of Hilbert row sections.

This probes full binary branching, not six-point configurations.  The
arithmetic relation is a*p-b*q=c, with positive odd a,b.  States contain
the two reversed section orientations and an integer multiplication carry.
"""
from collections import deque
from fractions import Fraction
import argparse
import itertools
import json


def forward(state, bit):
    axis, flip = divmod(state, 2)
    effective = bit ^ flip
    if axis == 0:
        return ((0, 2 + flip), (1, flip)) if not effective else (
            (2, flip), (3, 2 + (flip ^ 1)))
    return ((0, flip), (3, flip ^ 1)) if not effective else (
        (1, 2 + flip), (2, 2 + flip))


REVERSE = {}
for child in range(4):
    for bit in range(2):
        options = [(digit, parent) for parent in range(4)
                   for digit, nxt in forward(parent, bit) if nxt == child]
        assert len(options) == 2 and len({x[0] for x in options}) == 2
        REVERSE[child, bit] = dict(options)


def row_section(exponent, row, state=0):
    partial = [(0, state)]
    for pos in range(exponent - 1, -1, -1):
        bit = (row >> pos) & 1
        partial = [(4 * rank + digit, nxt) for rank, old in partial
                   for digit, nxt in forward(old, bit)]
    return sorted(rank for rank, _ in partial)


def affine_count(exponent, row1, row2, a, b, c, axis=0):
    """Count a*p-b*q=c by the reverse orientation/carry automaton."""
    # The leaf orientation is immaterial. Each rank has exactly one
    # reverse path ending at the prescribed top orientation.
    current = {(i, j, 0): 1 for i in range(4) for j in range(4)}
    modulus = 4 ** exponent
    low_c = c % modulus
    high_c = c // modulus
    for pos in range(exponent):
        bits = (row1 >> pos) & 1, (row2 >> pos) & 1
        digit_c = (low_c >> (2 * pos)) & 3
        nxt = {}
        for (s1, s2, carry), weight in current.items():
            for d1, p1 in REVERSE[s1, bits[0]].items():
                d2 = ((a * d1 - digit_c + carry) * pow(b, -1, 4)) % 4
                if d2 not in REVERSE[s2, bits[1]]:
                    continue
                p2 = REVERSE[s2, bits[1]][d2]
                new_carry = (a * d1 - b * d2 - digit_c + carry) // 4
                key = p1, p2, new_carry
                nxt[key] = nxt.get(key, 0) + weight
        current = nxt
    return current.get((axis, axis, high_c), 0)


def full_branch_graph(a, b, cap=100000, return_graph=False):
    assert a > 0 and b > 0 and a % 2 and b % 2
    states = [(i, j, carry) for i in range(4) for j in range(4)
              for carry in range(-b, a)]
    index = {s: k for k, s in enumerate(states)}
    controls = [(bit, digit) for bit in range(2) for digit in range(4)]
    valid = [0] * 8
    targets = [[0] * len(states) for _ in controls]
    for z, (s1, s2, carry) in enumerate(states):
        for t, (bit, digit_c) in enumerate(controls):
            edges = []
            for d1, p1 in REVERSE[s1, bit].items():
                d2 = ((a * d1 - digit_c + carry) * pow(b, -1, 4)) % 4
                if d2 not in REVERSE[s2, bit]:
                    continue
                p2 = REVERSE[s2, bit][d2]
                nc = (a * d1 - b * d2 - digit_c + carry) // 4
                assert -b <= nc < a
                edges.append(index[p1, p2, nc])
            if len(edges) == 2:
                valid[t] |= 1 << z
                targets[t][z] = sum(1 << v for v in set(edges))

    starts = [1 << i for i in range(len(states))]
    nodes = {s: i for i, s in enumerate(starts)}
    masks = starts[:]
    graph = []
    cursor = 0
    while cursor < len(masks):
        source = masks[cursor]
        out = []
        for control in range(8):
            if source & ~valid[control]:
                continue
            rem = source
            target = 0
            while rem:
                low = rem & -rem
                target |= targets[control][low.bit_length() - 1]
                rem -= low
            if target not in nodes:
                if len(nodes) >= cap:
                    return {"a": a, "b": b, "status": "node_cap", "nodes": len(nodes)}
                nodes[target] = len(masks)
                masks.append(target)
            out.append((nodes[target], control))
        graph.append(out)
        cursor += 1

    if return_graph:
        return {"states": states, "controls": controls, "masks": masks,
                "graph": graph}

    # DFS gives either an explicit full-branch cycle or a longest path.
    color = [0] * len(masks)
    depth = [0] * len(masks)
    parent = [None] * len(masks)
    cycle = None
    for start in range(len(masks)):
        if color[start]:
            continue
        color[start] = 1
        stack = [(start, 0)]
        while stack:
            node, edge_index = stack[-1]
            if edge_index == len(graph[node]):
                color[node] = 2
                depth[node] = max((1 + depth[v] for v, _ in graph[node]), default=0)
                stack.pop()
                continue
            stack[-1] = node, edge_index + 1
            target, control = graph[node][edge_index]
            if color[target] == 0:
                parent[target] = node, control
                color[target] = 1
                stack.append((target, 0))
            elif color[target] == 1:
                route = [(node, control)]
                p = node
                while p != target:
                    p, previous_control = parent[p]
                    route.append((p, previous_control))
                route.reverse()
                cycle = [{"states": [states[z] for z in range(len(states))
                                      if masks[v] >> z & 1],
                          "control": controls[t]} for v, t in route]
                break
        if cycle is not None:
            break
    if cycle is not None:
        return {"a": a, "b": b, "status": "full_branch_cycle",
                "nodes": len(nodes), "cycle": cycle}
    return {"a": a, "b": b, "status": "uniform_block_loss",
            "nodes": len(nodes), "block_length": max(depth) + 1}


def persistent_components(a, b):
    data = full_branch_graph(a, b, return_graph=True)
    graph = data["graph"]
    reverse = [[] for _ in graph]
    for v, edges in enumerate(graph):
        for w, _ in edges:
            reverse[w].append(v)
    seen = set()
    order = []
    for start in range(len(graph)):
        if start in seen:
            continue
        seen.add(start)
        stack = [(start, 0)]
        while stack:
            v, i = stack[-1]
            if i == len(graph[v]):
                order.append(v)
                stack.pop()
                continue
            stack[-1] = v, i + 1
            w, _ = graph[v][i]
            if w not in seen:
                seen.add(w)
                stack.append((w, 0))
    seen.clear()
    components = []
    for start in reversed(order):
        if start in seen:
            continue
        component = []
        stack = [start]
        seen.add(start)
        while stack:
            v = stack.pop()
            component.append(v)
            for w in reverse[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        keep = set(component)
        edges = [(v, w, t) for v in component for w, t in graph[v] if w in keep]
        if len(component) == 1 and not edges:
            continue
        local = {v: i for i, v in enumerate(component)}
        components.append({
            "nodes": [[data["states"][z] for z in range(len(data["states"]))
                       if data["masks"][v] >> z & 1] for v in component],
            "edges": [(local[v], local[w], data["controls"][t]) for v, w, t in edges],
            "row_bits": sorted({data["controls"][t][0] for _, _, t in edges}),
        })
    return {"a": a, "b": b, "components": components}


def block_max_counts(a, b, length):
    states = [(i, j, carry) for i in range(4) for j in range(4)
              for carry in range(-b, a)]
    index = {s: k for k, s in enumerate(states)}
    transitions = {}
    for bit in range(2):
        for digit_c in range(4):
            edges = []
            for s1, s2, carry in states:
                dest = []
                for d1, p1 in REVERSE[s1, bit].items():
                    d2 = ((a*d1-digit_c+carry)*pow(b, -1, 4)) % 4
                    if d2 in REVERSE[s2, bit]:
                        p2 = REVERSE[s2, bit][d2]
                        nc = (a*d1-b*d2-digit_c+carry)//4
                        dest.append(index[p1, p2, nc])
                edges.append(dest)
            transitions[bit, digit_c] = edges
    result = {}
    for bits in itertools.product(range(2), repeat=length):
        maximum = 0
        for digits in itertools.product(range(4), repeat=length):
            values = [1]*len(states)
            for control in reversed(list(zip(bits, digits))):
                values = [sum(values[w] for w in out)
                          for out in transitions[control]]
            maximum = max(maximum, max(values))
        result["".join(map(str, bits))] = maximum
    return {"a": a, "b": b, "length": length, "row_word_maxima": result}


def check_counts():
    tests = 0
    for exponent in range(1, 4):
        n = 2 ** exponent
        for axis in (0, 2):
            for row1 in range(n):
                left = row_section(exponent, row1, axis)
                for row2 in range(n):
                    right = set(row_section(exponent, row2, axis))
                    for a, b in ((1, 1), (3, 1), (5, 3)):
                        for c in (-n*n, -3, 0, 5, n*n):
                            direct = sum((a*p-c) % b == 0 and (a*p-c)//b in right
                                         for p in left)
                            actual = affine_count(exponent, row1, row2, a, b, c, axis)
                            assert actual == direct, (exponent, axis, row1, row2, a, b, c, direct, actual)
                            tests += 1
    return tests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out")
    args = parser.parse_args()
    data = {"exact_count_tests": check_counts(),
            "ratios": [full_branch_graph(a, b) for a, b in
                       ((1,1), (3,1), (5,1), (7,1), (5,3), (7,3), (9,1), (9,5))],
            "slope_five_structure": persistent_components(5, 1),
            "block_certificates": [block_max_counts(a, b, q) for a, b, q in
                                   ((3,1,3), (5,1,3), (7,1,2), (5,3,2))]}
    rendered = json.dumps(data, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as stream:
            stream.write(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
