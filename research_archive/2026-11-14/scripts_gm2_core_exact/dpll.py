"""Complete backtracking solver with unit propagation for slot systems.

Variables: labels v with xi_v in {0..M-1}.  Constraint (r, u, delta) forbids
xi_u - xi_r = delta.  mode 'int' is the system itself; mode 'mod' is the
mod-M certified version (forbids xi_u - xi_r = delta mod M).
Search: DSATUR order (smallest domain, then largest degree), forward checking,
singleton domains propagated immediately (unit propagation on the direct
encoding), chronological backtracking.  Complete: 'UNSAT' only after the
whole tree is exhausted.

Usage: py -B dpll.py prefix M mode [node_limit]  -> writes prefix_<mode>_sol.npy
(rows: label, value) when every core component is solved.
"""
import sys, time, heapq
import numpy as np
from core_stats import components


def solve_component(E, M, mode, limit, seed=None):
    verts = np.unique(E[:, :2]).tolist()
    idx = {v: k for k, v in enumerate(verts)}
    n = len(verts)
    adj = [[] for _ in range(n)]          # (w, delta, sign): sign +1 means w is the 'u' end
    for r, u, d in E.tolist():
        a, b = idx[r], idx[u]
        adj[a].append((b, d, 1))
        adj[b].append((a, d, -1))
    deg = [len(x) for x in adj]
    if seed is not None:
        import random
        rg = random.Random(seed)
        deg = [dv + rg.random() for dv in deg]   # random tie-break among equal degrees
    full = (1 << M) - 1
    dom = [full] * n
    val = [-1] * n
    trail = []           # (var, old_mask) for domain changes, (var, None) for assignments
    pc = [bin(m).count("1") for m in range(1 << M)]
    heap = [(M, -deg[v], v) for v in range(n)]
    heapq.heapify(heap)

    def forbid_mask(v, x, w, d, sg):
        # values of w forbidden once xi_v = x
        if mode == "int":
            y = x + d if sg == 1 else x - d
            return (1 << y) if 0 <= y < M else 0
        y = (x + d) % M if sg == 1 else (x - d) % M
        return 1 << y

    def assign(v, x):
        """assign and propagate; return False on wipeout"""
        queue = [(v, x)]
        while queue:
            v, x = queue.pop()
            if val[v] != -1:
                if val[v] != x:
                    return False
                continue
            if not (dom[v] >> x) & 1:
                return False
            trail.append((v, None))
            val[v] = x
            if dom[v] != (1 << x):
                trail.append((v, dom[v])); dom[v] = 1 << x
            for w, d, sg in adj[v]:
                fm = forbid_mask(v, x, w, d, sg)
                if val[w] != -1:
                    if fm >> val[w] & 1:
                        return False
                    continue
                if dom[w] & fm:
                    trail.append((w, dom[w]))
                    dom[w] &= ~fm
                    if dom[w] == 0:
                        return False
                    heapq.heappush(heap, (pc[dom[w]], -deg[w], w))
                    if pc[dom[w]] == 1:
                        queue.append((w, dom[w].bit_length() - 1))
        return True

    def undo(pos):
        while len(trail) > pos:
            v, old = trail.pop()
            if old is None:
                val[v] = -1
                heapq.heappush(heap, (pc[dom[v]], -deg[v], v))
            else:
                dom[v] = old
                if val[v] == -1:
                    heapq.heappush(heap, (pc[old], -deg[v], v))

    def pick():
        while heap:
            s, nd, v = heap[0]
            if val[v] != -1 or pc[dom[v]] != s:
                heapq.heappop(heap); continue
            return v
        return -1

    nodes = 0
    stack = []           # (var, list of remaining values, trail position)
    v = pick()
    if v == -1:
        return "SAT", {verts[k]: val[k] for k in range(n)}, nodes
    stack.append((v, [x for x in range(M) if dom[v] >> x & 1], len(trail)))
    while stack:
        v, rest, pos = stack[-1]
        undo(pos)
        if not rest:
            stack.pop(); continue
        x = rest.pop(0)
        nodes += 1
        if nodes > limit:
            return "LIMIT", None, nodes
        if assign(v, x):
            w = pick()
            if w == -1:
                return "SAT", {verts[k]: val[k] for k in range(n)}, nodes
            stack.append((w, [y for y in range(M) if dom[w] >> y & 1], len(trail)))
    return "UNSAT", None, nodes


if __name__ == "__main__":
    pre, M, mode = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    limit = int(sys.argv[4]) if len(sys.argv) > 4 else 2_000_000
    seeds = [None] + list(range(int(sys.argv[5]))) if len(sys.argv) > 5 else [None]
    C = np.load(pre + "_core.npy").astype(np.int64)
    sol = {}
    allsat = True
    for E in components(C):
        t0 = time.time()
        for sd in seeds:
            res, s, nodes = solve_component(E, M, mode, limit, sd)
            if res != "LIMIT":
                break
        print(f"  component labels {len(np.unique(E[:, :2]))} constraints {len(E)}: {res}, nodes {nodes}, {time.time()-t0:.1f}s", flush=True)
        if res == "SAT":
            sol.update(s)
        else:
            allsat = False
    if allsat:
        arr = np.array(sorted(sol.items()), dtype=np.int64)
        np.save(f"{pre}_{mode}{M}_sol.npy", arr)
        print("all core components solved; assignment saved")
