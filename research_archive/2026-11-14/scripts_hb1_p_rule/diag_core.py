"""Fast version: main-diagonal block system, k-core (k=M), core solve.

Usage: py diag_core.py B S M orient [solve]
Constraint (r, s=r+d, delta) forbids xi_s - xi_r = delta, xi in [0,M).
Vertices of weighted degree < M are peeled; the remaining M-core is the
only part a greedy argument cannot settle.  'solve' runs a DFS with
forward checking on that core (sanity tool, not a proof device unless
it reports UNSAT with a complete search).
"""
import sys
from collections import defaultdict
import numpy as np
from diag_block import hilbert_array, legs_by_X


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1]
    i, j = xy[:, 0], xy[:, 1]
    odd, even = 2 * i + 1, 2 * j + 2
    n = B * B
    legs = legs_by_X(2 * B + 1, S)
    chunks = []
    for X, ys in legs.items():
        q = X // S
        for d in {q // M, -(-q // M)}:
            delta = q - M * d
            if d < 1 or d >= n or abs(delta) > M - 1:
                continue
            look = np.zeros(4 * B + 4, dtype=np.int64)
            for Y, L in ys.items():
                look[Y] = L
            for a_rows, b_rows in ((odd[d:], even[:-d]), (odd[:-d], even[d:])):
                L = look[np.abs(b_rows - a_rows)]
                s = a_rows + b_rows
                lo, hi = (s - L) // 2, (s + L) // 2
                oddr = np.where(lo % 2 == 1, lo, hi)
                evr = np.where(lo % 2 == 1, hi, lo)
                oi, oj = (oddr - 1) // 2, (evr - 2) // 2
                inside = (oi >= 0) & (oi < B) & (oj >= 0) & (oj < B)
                r = np.nonzero((L > 0) & ~inside)[0]
                if len(r):
                    chunks.append((r * n + (r + d)) * (2 * M) + (delta + M))
    if not chunks:
        return n, np.zeros((0, 3), dtype=np.int64)
    code = np.unique(np.concatenate(chunks))
    delta = code % (2 * M) - M
    pair = code // (2 * M)
    a, b = pair // n, pair % n
    return n, np.stack([a, b, delta], axis=1)


def core(n, E, k):
    alive = np.ones(len(E), dtype=bool)
    while True:
        deg = np.bincount(E[alive, 0], minlength=n) + np.bincount(E[alive, 1], minlength=n)
        bad = (deg > 0) & (deg < k)
        kill = alive & (bad[E[:, 0]] | bad[E[:, 1]])
        if not kill.any():
            return E[alive]
        alive &= ~kill


def solve(Ec, M, limit=2_000_000):
    verts = sorted(set(Ec[:, 0]) | set(Ec[:, 1]))
    adj = defaultdict(list)
    for a, b, d in Ec:
        adj[int(a)].append((int(b), int(d), 1))   # xi_b - xi_a != d
        adj[int(b)].append((int(a), int(d), -1))
    dom = {v: set(range(M)) for v in verts}
    val = {}
    nodes = [0]

    def forbidden(v, x):
        # removing values from neighbours given xi_v = x
        out = []
        for w, d, sgn in adj[v]:
            if w in val:
                continue
            bad = x + d if sgn == 1 else x - d
            if bad in dom[w]:
                out.append((w, bad))
        return out

    def ok(v, x):
        for w, d, sgn in adj[v]:
            if w in val:
                if (sgn == 1 and val[w] - x == d) or (sgn == -1 and x - val[w] == d):
                    return False
        return True

    sys.setrecursionlimit(100000)

    def dfs():
        nodes[0] += 1
        if nodes[0] > limit:
            raise TimeoutError
        free = [v for v in verts if v not in val]
        if not free:
            return True
        v = min(free, key=lambda u: (len(dom[u]), -len(adj[u])))
        for x in sorted(dom[v]):
            if not ok(v, x):
                continue
            val[v] = x
            rem = forbidden(v, x)
            wipe = False
            for w, bad in rem:
                dom[w].discard(bad)
                if not dom[w]:
                    wipe = True
            if not wipe and dfs():
                return True
            for w, bad in rem:
                dom[w].add(bad)
            del val[v]
        return False

    try:
        return dfs(), nodes[0], val
    except TimeoutError:
        return None, nodes[0], val


if __name__ == "__main__":
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    n, E = build(B, S, M, orient)
    Ec = core(n, E, M)
    cv = len(set(Ec[:, 0]) | set(Ec[:, 1])) if len(Ec) else 0
    print(f"B={B} S={S} M={M} {orient}: constraints={len(E)} avgdeg={2*len(E)/n:.4f} "
          f"{M}-core: vertices={cv} constraints={len(Ec)}")
    if len(sys.argv) > 5 and len(Ec):
        # solve each connected component of the core separately
        parent = {}
        def find(x):
            while parent.setdefault(x, x) != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b, _ in Ec:
            parent[find(int(a))] = find(int(b))
        comps = defaultdict(list)
        for row in Ec:
            comps[find(int(row[0]))].append(row)
        print(f"  core components: {len(comps)}, sizes(constraints) max={max(len(c) for c in comps.values())}")
        for key, rows in sorted(comps.items(), key=lambda kv: -len(kv[1])):
            res, nodes, _ = solve(np.array(rows), M)
            if res is not True:
                print(f"  component with {len(rows)} constraints: result={res} nodes={nodes}")
        print("  done")
