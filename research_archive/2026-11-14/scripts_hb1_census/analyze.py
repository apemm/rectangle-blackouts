"""Graph statistics of a saved P candidate constraint system."""
import json
import sys
import time
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components


def core_peel(u, v, nv, k):
    """Vertices of the k-core of the multigraph with edge list (u, v)."""
    alive_e = np.ones(len(u), bool)
    alive_v = np.ones(nv, bool)
    rounds = 0
    while True:
        deg = np.bincount(u[alive_e], minlength=nv) + np.bincount(v[alive_e], minlength=nv)
        kill = alive_v & (deg < k)
        if not kill.any():
            break
        alive_v &= ~kill
        alive_e &= alive_v[u] & alive_v[v]
        rounds += 1
    return alive_v, alive_e, rounds


def analyze(path):
    z = np.load(path)
    h, S, M, q, labels = map(int, z["meta"])
    w = z["witness"]
    out = {"h": h, "S": S, "M": M, "labels": labels}
    if len(w) == 0:
        out.update({"constraints": 0, "incident_labels": 0, "mean_incidence": 0.0,
                    "max_incidence": 0, "greedy_success": True})
        return out
    dd = w[:, 1] - w[:, 0]
    assert dd.max() < 1 << 9 and (w[:, 2] + M - 1).max() < 1 << 3
    ck = (w[:, 0] << 12) | (dd << 3) | (w[:, 2] + M - 1)
    ukey, first, inv = np.unique(ck, return_index=True, return_inverse=True)
    inv = inv.ravel()
    C = w[first, :3]
    out["witnesses"] = int(len(w))
    out["constraints"] = int(len(C))
    out["max_witnesses_per_constraint"] = int(np.bincount(inv).max())
    verts, cu = np.unique(np.concatenate([C[:, 0], C[:, 1]]), return_inverse=True)
    nv = len(verts)
    u, v = cu[:len(C)], cu[len(C):]          # u earlier, v later
    out["incident_labels"] = int(nv)
    degw = np.bincount(u, minlength=nv) + np.bincount(v, minlength=nv)
    out["mean_incidence"] = 2 * len(C) / labels
    out["mean_incidence_on_incident"] = 2 * len(C) / nv
    out["max_incidence"] = int(degw.max())
    out["incidence_hist"] = {int(a): int(b) for a, b in zip(*np.unique(degw, return_counts=True))}
    pk, pc = np.unique(u * nv + v, return_counts=True)
    P = np.stack([pk // nv, pk % nv], 1)
    degs = np.bincount(P[:, 0], minlength=nv) + np.bincount(P[:, 1], minlength=nv)
    out["simple_edges"] = int(len(P))
    out["max_simple_degree"] = int(degs.max())
    out["max_deltas_per_pair"] = int(pc.max())
    bminus = np.bincount(v, minlength=nv)
    out["max_earlier_constraints_bminus"] = int(bminus.max())
    # factors: witness factor a attached to each endpoint
    wu, wv = cu[:len(C)][inv], cu[len(C):][inv]
    a = w[:, 3]
    assert a.max() < 1 << 20
    allF = np.unique((np.concatenate([wu, wv]) << 20) | np.concatenate([a, a]))
    F = np.bincount(allF >> 20, minlength=nv)
    Fm_pairs = np.unique((wv << 20) | a)
    Fm = np.bincount(Fm_pairs >> 20, minlength=nv)
    out["distinct_factors_global"] = int(len(np.unique(a)))
    out["factor_one_witnesses"] = int((a == 1).sum())
    out["max_F"] = int(F.max())
    out["mean_F_on_incident"] = float(F.mean())
    out["F_hist"] = {int(x): int(c) for x, c in zip(*np.unique(F, return_counts=True))}
    out["max_Fminus"] = int(Fm.max())
    out["lemma_bminus_le_4Fminus"] = bool((bminus <= 4 * Fm).all())
    out["max_bminus_over_Fminus"] = float((bminus[Fm > 0] / Fm[Fm > 0]).max())
    # components
    A = coo_matrix((np.ones(len(P)), (P[:, 0], P[:, 1])), shape=(nv, nv))
    ncomp, lab = connected_components(A, directed=False)
    sizes = np.bincount(lab)
    out["components"] = int(ncomp)
    out["largest_component"] = int(sizes.max())
    out["component_size_hist_top"] = {int(x): int(c) for x, c in
                                      list(zip(*np.unique(sizes, return_counts=True)))[-5:]}
    # cores
    a2, e2, r2 = core_peel(P[:, 0], P[:, 1], nv, 2)
    out["simple_2core_vertices"] = int(a2.sum())
    out["simple_2core_edges"] = int(e2.sum())
    k = 1
    cores = {}
    while True:
        ak, ek, rk = core_peel(u, v, nv, k + 1)
        if not ak.any():
            break
        k += 1
        cores[k] = [int(ak.sum()), int(ek.sum()), rk]
    out["weighted_degeneracy"] = k
    out["weighted_cores"] = cores   # k: [vertices, constraints, peel rounds]
    ks, kk = 1, 1
    while True:
        ak, ek, _ = core_peel(P[:, 0], P[:, 1], nv, kk + 1)
        if not ak.any():
            break
        kk += 1
    out["simple_degeneracy"] = kk
    # greedy in increasing rank, smallest admissible choice
    order = np.argsort(v, kind="stable")
    vs, us, ds = v[order].tolist(), u[order].tolist(), C[order, 2].tolist()
    choice = [0] * nv          # vertices are indexed in increasing rank
    fails = 0
    maxforb = 0
    ptr = 0
    m = len(vs)
    for x in range(nv):
        forb = set()
        while ptr < m and vs[ptr] == x:
            f = choice[us[ptr]] + ds[ptr]   # forbids xi_x - xi_u = delta
            if 0 <= f < M:
                forb.add(f)
            ptr += 1
        maxforb = max(maxforb, len(forb))
        c = 0
        while c in forb:
            c += 1
        if c >= M:
            fails += 1
            c = 0
        choice[x] = c
    ch = np.array(choice)
    viol = int((ch[v] - ch[u] == C[:, 2]).sum())
    out["greedy_max_forbidden"] = maxforb
    out["greedy_stuck_labels"] = fails
    out["greedy_violations_final"] = viol
    out["greedy_success"] = viol == 0
    return out


if __name__ == "__main__":
    t = time.time()
    res = analyze(sys.argv[1])
    res["sec"] = round(time.time() - t, 1)
    with open(sys.argv[2], "w") as f:
        json.dump(res, f)
    print(json.dumps({k: v for k, v in res.items() if not k.endswith("hist") and k != "component_size_hist_top"}))
