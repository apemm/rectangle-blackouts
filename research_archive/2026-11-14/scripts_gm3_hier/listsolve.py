"""Complete list solver for the mod-M certified system (constraint (r,u,delta) forbids
y_u - y_r = delta mod M), with initial domains.  DSATUR order, forward checking, unit
propagation, chronological backtracking (adapted from the archive's dpll.py)."""
import heapq


def solve(verts, E, M, dom0, limit=3_000_000):
    """verts: list of labels; E: list of (r,u,delta) with both ends in verts;
    dom0: dict label -> bitmask.  Returns (status, {label: value}, nodes)."""
    idx = {v: k for k, v in enumerate(verts)}
    n = len(verts)
    adj = [[] for _ in range(n)]
    for r, u, d in E:
        a, b = idx[r], idx[u]
        adj[a].append((b, d, 1)); adj[b].append((a, d, -1))
    deg = [len(x) for x in adj]
    dom = [dom0.get(v, (1 << M) - 1) for v in verts]
    val = [-1] * n; trail = []
    pc = [bin(m).count("1") for m in range(1 << M)]
    if any(x == 0 for x in dom):
        return "UNSAT", None, 0
    heap = [(pc[dom[v]], -deg[v], v) for v in range(n)]; heapq.heapify(heap)

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
            for w, d, sg in adj[v]:
                y = (x + d) % M if sg == 1 else (x - d) % M
                fm = 1 << y
                if val[w] != -1:
                    if val[w] == y: return False
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

    # propagate initial singletons
    for v in range(n):
        if pc[dom[v]] == 1 and val[v] == -1:
            if not assign(v, dom[v].bit_length() - 1):
                return "UNSAT", None, 0
    base = len(trail)
    nodes = 0
    v = pick()
    if v == -1:
        return "SAT", {verts[k]: val[k] for k in range(n)}, 0
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
            if w == -1: return "SAT", {verts[k]: val[k] for k in range(n)}, nodes
            stack.append((w, [y for y in range(M) if dom[w] >> y & 1], len(trail)))
    return "UNSAT", None, nodes
