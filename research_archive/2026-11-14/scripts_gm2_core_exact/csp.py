"""Complete binary-CSP solver (forward checking, singleton propagation, DSATUR order,
chronological backtracking).  Constraints are nogoods (a, xa, b, xb): not (v_a = xa and v_b = xb).
solve(n, nogoods, M, limit) -> ("SAT", values) | ("UNSAT", None) | ("LIMIT", None), nodes"""
import heapq
from collections import defaultdict


def solve(n, nogoods, M, limit=2_000_000):
    tab = defaultdict(lambda: [0] * M)       # (v, w) -> forb mask of w for each value of v
    for a, xa, b, xb in nogoods:
        tab[(a, b)][xa] |= 1 << xb
        tab[(b, a)][xb] |= 1 << xa
    adj = [[] for _ in range(n)]
    for (v, w), t in tab.items():
        adj[v].append((w, t))
    deg = [len(x) for x in adj]
    full = (1 << M) - 1
    dom = [full] * n; val = [-1] * n; trail = []
    pc = [bin(m).count("1") for m in range(1 << M)]
    heap = [(M, -deg[v], v) for v in range(n)]; heapq.heapify(heap)

    def assign(v, x):
        queue = [(v, x)]
        while queue:
            v, x = queue.pop()
            if val[v] != -1:
                if val[v] != x: return False
                continue
            if not (dom[v] >> x) & 1: return False
            trail.append((v, None)); val[v] = x
            if dom[v] != (1 << x):
                trail.append((v, dom[v])); dom[v] = 1 << x
            for w, t in adj[v]:
                fm = t[x]
                if val[w] != -1:
                    if fm >> val[w] & 1: return False
                    continue
                if dom[w] & fm:
                    trail.append((w, dom[w])); dom[w] &= ~fm
                    if dom[w] == 0: return False
                    heapq.heappush(heap, (pc[dom[w]], -deg[w], w))
                    if pc[dom[w]] == 1: queue.append((w, dom[w].bit_length() - 1))
        return True

    def undo(pos):
        while len(trail) > pos:
            v, old = trail.pop()
            if old is None:
                val[v] = -1; heapq.heappush(heap, (pc[dom[v]], -deg[v], v))
            else:
                dom[v] = old
                if val[v] == -1: heapq.heappush(heap, (pc[old], -deg[v], v))

    def pick():
        while heap:
            s, _, v = heap[0]
            if val[v] != -1 or pc[dom[v]] != s:
                heapq.heappop(heap); continue
            return v
        return -1

    nodes = 0
    v = pick()
    if v == -1: return "SAT", list(val), 0
    stack = [(v, [x for x in range(M) if dom[v] >> x & 1], len(trail))]
    while stack:
        v, rest, pos = stack[-1]
        undo(pos)
        if not rest:
            stack.pop(); continue
        x = rest.pop(0); nodes += 1
        if nodes > limit: return "LIMIT", None, nodes
        if assign(v, x):
            w = pick()
            if w == -1: return "SAT", list(val), nodes
            stack.append((w, [y for y in range(M) if dom[w] >> y & 1], len(trail)))
    return "UNSAT", None, nodes
