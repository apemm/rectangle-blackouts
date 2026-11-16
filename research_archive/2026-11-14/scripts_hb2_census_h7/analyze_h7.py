"""Statistics and choice tests of a constraint system (earlier, later, delta):
each row forbids xi_later - xi_earlier = delta, xi in {0..M-1}.

Reports: constraints E, incident labels, mean incidence 2E/labels, max
weighted degree, weighted degeneracy (core numbers of the multigraph),
increasing-rank greedy, peeling certificate (valid when degeneracy <= M-1),
and an exact test on the M-core: 2-SAT for M = 2, backtracking for M = 3.
Every final assignment is checked against all constraints.
usage: py analyze_h7.py M labels file1.npz [file2.npz ...]
"""
import sys, time, json
import numpy as np
from numba import njit


@njit(cache=True)
def core_numbers(nv, indptr, nbr):
    deg = np.zeros(nv, np.int64)
    for v in range(nv):
        deg[v] = indptr[v + 1] - indptr[v]
    md = deg.max() if nv else 0
    # bucket sort
    cnt = np.zeros(md + 2, np.int64)
    for v in range(nv):
        cnt[deg[v]] += 1
    start = np.zeros(md + 2, np.int64)
    s = 0
    for k in range(md + 1):
        start[k] = s
        s += cnt[k]
    pos = np.zeros(nv, np.int64); vert = np.zeros(nv, np.int64)
    fill = start.copy()
    for v in range(nv):
        pos[v] = fill[deg[v]]; vert[pos[v]] = v; fill[deg[v]] += 1
    order = np.zeros(nv, np.int64)
    for i in range(nv):
        v = vert[i]
        order[i] = v
        for e in range(indptr[v], indptr[v + 1]):
            u = nbr[e]
            if deg[u] > deg[v]:
                du = deg[u]; pu = pos[u]; pw = start[du]; w = vert[pw]
                if u != w:
                    pos[u] = pw; vert[pu] = w; pos[w] = pu; vert[pw] = u
                start[du] += 1
                deg[u] -= 1
    return deg, order  # deg = core number; order = peeling order


@njit(cache=True)
def assign_reverse(nv, order, indptr, nbr, dl, sgn, M, choice):
    """Assign in reverse peeling order; constraint stored at v: xi_v - xi_u != dl*sgn
    where sgn = +1 if v is the later endpoint.  Returns number of stuck vertices."""
    done = np.zeros(nv, np.bool_)
    stuck = 0
    forb = np.zeros(M, np.bool_)
    for k in range(nv - 1, -1, -1):
        v = order[k]
        forb[:] = False
        for e in range(indptr[v], indptr[v + 1]):
            u = nbr[e]
            if done[u]:
                f = choice[u] + dl[e] * sgn[e]   # forbidden value for xi_v
                if 0 <= f < M:
                    forb[f] = True
        c = 0
        while c < M and forb[c]:
            c += 1
        if c == M:
            stuck += 1; c = 0
        choice[v] = c
        done[v] = True
    return stuck


def csr(u, v, dl, nv):
    src = np.concatenate([u, v]); dst = np.concatenate([v, u])
    d2 = np.concatenate([dl, dl])
    sg = np.concatenate([-np.ones(len(u), np.int64), np.ones(len(v), np.int64)])
    # at src=u (earlier): xi_u forbidden = xi_v - dl  -> sign -1 ; at src=v: xi_v = xi_u + dl
    o = np.argsort(src, kind="stable")
    src, dst, d2, sg = src[o], dst[o], d2[o], sg[o]
    indptr = np.zeros(nv + 1, np.int64)
    np.add.at(indptr, src + 1, 1)
    return np.cumsum(indptr), dst, d2, sg


def two_sat(nodes, cons):
    """cons: list of (a, b, delta) local indices, forbids x_b - x_a = delta, x in {0,1}."""
    n = len(nodes)
    g = [[] for _ in range(2 * n)]   # literal 2i = (x_i = 1), 2i+1 = (x_i = 0)
    lit = lambda i, val: 2 * i + (0 if val == 1 else 1)
    for a, b, dl in cons:
        for xa in (0, 1):
            xb = xa + dl
            if xb in (0, 1):  # forbid (xa, xb): clause (x_a != xa) or (x_b != xb)
                A = lit(a, 1 - xa); B = lit(b, 1 - xb)
                g[A ^ 1].append(B); g[B ^ 1].append(A)
    # Tarjan iterative
    idx = [0] * (2 * n); low = [0] * (2 * n); on = [False] * (2 * n); seen = [False] * (2 * n)
    comp = [-1] * (2 * n); st = []; c = 0; counter = 1
    for s0 in range(2 * n):
        if seen[s0]:
            continue
        stack = [(s0, 0)]
        while stack:
            v, it = stack.pop()
            if it == 0:
                seen[v] = True; idx[v] = low[v] = counter; counter += 1; st.append(v); on[v] = True
            recurse = False
            for k in range(it, len(g[v])):
                w = g[v][k]
                if not seen[w]:
                    stack.append((v, k + 1)); stack.append((w, 0)); recurse = True; break
                elif on[w]:
                    low[v] = min(low[v], idx[w])
            if recurse:
                continue
            if low[v] == idx[v]:
                while True:
                    w = st.pop(); on[w] = False; comp[w] = c
                    if w == v:
                        break
                c += 1
            if stack:
                p, _ = stack[-1]
                low[p] = min(low[p], low[v])
    sol = []
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            return None
        sol.append(1 if comp[2 * i] < comp[2 * i + 1] else 0)
    return sol


def backtrack(nodes, cons, M, limit=2_000_000):
    n = len(nodes)
    adj = [[] for _ in range(n)]
    for a, b, dl in cons:
        adj[b].append((a, dl)); adj[a].append((b, -dl))   # x_b != x_a + dl ; x_a != x_b - dl
    order = sorted(range(n), key=lambda i: -len(adj[i]))
    x = [-1] * n; steps = [0]
    def ok(i, val):
        for j, dl in adj[i]:
            if x[j] >= 0 and val == x[j] + dl:
                return False
        return True
    def rec(k):
        steps[0] += 1
        if steps[0] > limit:
            raise TimeoutError
        if k == n:
            return True
        i = order[k]
        for val in range(M):
            if ok(i, val):
                x[i] = val
                if rec(k + 1):
                    return True
                x[i] = -1
        return False
    sys.setrecursionlimit(10000 + 2 * n)
    try:
        return list(x) if rec(0) else None
    except TimeoutError:
        return "timeout"


def analyze(M, labels, cons):
    out = {"M": M, "labels": labels, "constraints": int(len(cons))}
    if len(cons) == 0:
        out.update({"incident": 0, "mean_inc": 0.0, "max_inc": 0, "degeneracy": 0,
                    "greedy_stuck": 0, "M_suffices": True, "method": "empty"})
        return out
    a = cons[:, 0]; b = cons[:, 1]; dl = cons[:, 2]
    assert (a < b).all()
    verts, inv = np.unique(np.concatenate([a, b]), return_inverse=True)
    nv = len(verts); u = inv[:len(a)]; v = inv[len(a):]
    deg = np.bincount(u, minlength=nv) + np.bincount(v, minlength=nv)
    out["incident"] = int(nv)
    out["mean_inc"] = 2 * len(cons) / labels
    out["mean_inc_on_incident"] = 2 * len(cons) / nv
    out["max_inc"] = int(deg.max())
    hist = np.bincount(deg)
    out["inc_hist"] = {int(k): int(c) for k, c in enumerate(hist) if c}
    indptr, nbr, d2, sg = csr(u, v, dl, nv)
    core, order = core_numbers(nv, indptr, nbr)
    K = int(core.max())
    out["degeneracy"] = K
    out["core_sizes"] = {int(k): int((core >= k).sum()) for k in range(2, K + 1)}
    # greedy in increasing rank (vertices are sorted by rank)
    ch = np.zeros(nv, np.int64)
    stuck_g = assign_reverse(nv, np.arange(nv)[::-1].copy(), indptr, nbr, d2, sg, M, ch)
    out["greedy_stuck"] = int(stuck_g)
    # peeling
    ch = np.zeros(nv, np.int64)
    stuck = assign_reverse(nv, order, indptr, nbr, d2, sg, M, ch)
    viol = int((ch[v] - ch[u] == dl).sum())
    if viol == 0:
        out.update({"M_suffices": True, "method": "peeling" if K <= M - 1 else "peeling(lucky)"})
        return out
    if M == 1:
        out.update({"M_suffices": False, "method": "M=1 with constraints"})
        return out
    # exact on the M-core
    inM = core >= M
    sel = inM[u] & inM[v]
    cu, cv, cd = u[sel], v[sel], dl[sel]
    nodes = np.unique(np.concatenate([cu, cv]))
    from scipy.sparse import coo_matrix
    from scipy.sparse.csgraph import connected_components
    loc = -np.ones(nv, np.int64); loc[nodes] = np.arange(len(nodes))
    A = coo_matrix((np.ones(len(cu)), (loc[cu], loc[cv])), shape=(len(nodes), len(nodes)))
    ncomp, lab = connected_components(A, directed=False)
    out["Mcore_vertices"] = int(len(nodes)); out["Mcore_components"] = int(ncomp)
    out["Mcore_largest"] = int(np.bincount(lab).max())
    fixed = {}
    res = "sat"
    for c in range(ncomp):
        cn = np.where(lab == c)[0]
        idx = {int(g): k for k, g in enumerate(cn)}
        es = np.where(lab[loc[cu]] == c)[0]
        cl = [(idx[int(loc[cu[e]])], idx[int(loc[cv[e]])], int(cd[e])) for e in es]
        sol = two_sat(cn, cl) if M == 2 else backtrack(cn, cl, M)
        if sol is None:
            res = "unsat"; break
        if sol == "timeout":
            res = "timeout"; break
        for k, g in enumerate(cn):
            fixed[int(nodes[g])] = sol[k]
    out["exact_Mcore"] = res
    if res != "sat":
        out["M_suffices"] = False if res == "unsat" else None
        out["method"] = "exact"
        return out
    # extend: assign M-core first (fixed), then the rest in reverse peeling order
    ch = -np.ones(nv, np.int64)
    for g, val in fixed.items():
        ch[g] = val
    rest = [w for w in order[::-1] if ch[w] < 0]
    adjl = None
    for w in rest:
        forb = set()
        for e in range(indptr[w], indptr[w + 1]):
            x = nbr[e]
            if ch[x] >= 0:
                forb.add(int(ch[x] + d2[e] * sg[e]))
        c = 0
        while c in forb:
            c += 1
        ch[w] = c if c < M else 0
    viol = int((ch[v] - ch[u] == dl).sum())
    out["M_suffices"] = viol == 0
    out["method"] = "exact core + peeling"
    out["final_violations"] = viol
    return out


if __name__ == "__main__":
    t = time.time()
    M = int(sys.argv[1]); labels = int(sys.argv[2])
    cons = np.concatenate([np.load(f)["cons"][:, :3] for f in sys.argv[3:]])
    cons = np.unique(cons, axis=0) if len(cons) else cons
    res = analyze(M, labels, cons)
    res["sec"] = round(time.time() - t, 1)
    h = res.pop("inc_hist", None)
    print(json.dumps(res))
    print("inc_hist", h)
