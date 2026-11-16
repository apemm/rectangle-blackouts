"""Round-peeling assignment: remove all vertices of weighted degree < M per
round; assign in reverse round order, sequentially inside a round.  Each
vertex then sees at most (its degree at the start of its round) < M
assigned constraints, so a free value exists.  Output: full choice array."""
import sys
import time
import numpy as np


def certify(path, out):
    z = np.load(path)
    h, S, M, q, labels = map(int, z["meta"])
    C = np.unique(z["witness"][:, :3], axis=0)
    verts, cu = np.unique(np.concatenate([C[:, 0], C[:, 1]]), return_inverse=True)
    nv, m = len(verts), len(C)
    u, v, dl = cu[:m], cu[m:], C[:, 2]
    rnd = np.full(nv, -1, np.int64)
    alive_e = np.ones(m, bool)
    k = 0
    while (rnd < 0).any():
        deg = np.bincount(u[alive_e], minlength=nv) + np.bincount(v[alive_e], minlength=nv)
        kill = (rnd < 0) & (deg < M)
        if not kill.any():
            raise SystemExit("nonempty M-core: no certificate by peeling")
        rnd[kill] = k
        alive_e &= (rnd[u] < 0) & (rnd[v] < 0)
        k += 1
    # CSR adjacency with signed delta: from x's view, constraint xi_v - xi_u = dl
    src = np.concatenate([u, v]); dst = np.concatenate([v, u])
    sgn = np.concatenate([-dl, dl])     # at src: forbidden xi_src = xi_dst + sgn
    o = np.argsort(src, kind="stable")
    dst, sgn = dst[o].tolist(), sgn[o].tolist()
    start = np.searchsorted(src[o], np.arange(nv + 1)).tolist()
    order = np.lexsort((np.arange(nv), -rnd)).tolist()
    choice = [-1] * nv
    for x in order:
        forb = set()
        for p in range(start[x], start[x + 1]):
            c = choice[dst[p]]
            if c >= 0:
                forb.add(c + sgn[p])
        val = 0
        while val in forb:
            val += 1
        assert val < M
        choice[x] = val
    ch = np.array(choice)
    assert int((ch[v] - ch[u] == dl).sum()) == 0
    full = np.zeros(q * q, np.int8)
    full[verts] = ch
    np.savez_compressed(out, xi=full, meta=np.array([h, S, M]))
    return {"h": h, "S": S, "M": M, "constraints": m, "rounds": k,
            "nonzero": int((ch > 0).sum()), "violations": 0}


if __name__ == "__main__":
    t = time.time()
    r = certify(sys.argv[1], sys.argv[2])
    print(r, "sec", round(time.time() - t, 1))
