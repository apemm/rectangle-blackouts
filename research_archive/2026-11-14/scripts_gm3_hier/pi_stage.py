"""Two-block system Pi = W_9 + W_10 in three stages (each run under 60 s).
  py -B pi_stage.py build g attach   -> pi_<g>_<attach>.npz (all triples E, certified core K)
  py -B pi_stage.py sat   g attach   -> pi_<g>_<attach>_core_sol.npy (CaDiCaL on the core;
                                         every model is checked against every core class)
  py -B pi_stage.py ext   g attach   -> pi_<g>_<attach>_sol.npy (reverse peeling, full check)
"""
import sys, time
import numpy as np

stage, g, attach = sys.argv[1], sys.argv[2], sys.argv[3]
M, S, N = 3, 32, 1024
tag = f"pi_{g}_{attach}"
t0 = time.time()
J = 3 * N * N if attach == "O4" else N * N
lo, hi = J - (N // 2) ** 2, J + N * N

if stage == "build":
    import stab10_kern as sk
    from blk import hilbert_array, legs, weighted_core
    h = g if attach == "O4" else ("swap" if g == "id" else "id")
    xy = hilbert_array(2 * N)
    if h == "swap":
        xy = xy[:, ::-1].copy()
    odd = (2 * xy[:, 0] + 1).astype(np.int64); even = (2 * xy[:, 1] + 2).astype(np.int64)
    P = legs(4 * N - 1, S)
    qs, offs, Ys, Ls = [], [0], [], []
    for q in sorted(P):
        qs.append(q)
        for Y, L in P[q]:
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((9_000_000, 3), dtype=np.int64)
    cnt = sk.kern(odd, even, M, lo, hi, np.array(qs), np.array(offs), np.array(Ys), np.array(Ls), out, 4 * N)
    assert cnt <= len(out)
    E = np.unique(out[:cnt], axis=0)
    K = weighted_core(4 * N * N, E, M, mod=M)
    np.savez_compressed(tag + ".npz", E=(E - [lo, lo, 0]).astype(np.int32), K=(K - [lo, lo, 0]).astype(np.int32))
    print(f"{tag}: triples {len(E)}, certified core classes {len(K)}, labels {len(np.unique(K[:, :2]))}  ({time.time()-t0:.1f}s)")

elif stage == "sat":
    from pysat.solvers import Cadical153
    K = np.load(tag + ".npz")["K"].astype(np.int64)
    labs = np.unique(K[:, :2])
    idx = np.searchsorted(labs, K[:, :2])
    n = len(labs)
    var = lambda i, c: 3 * i + c + 1
    s = Cadical153()
    for i in range(n):
        s.add_clause([var(i, 0), var(i, 1), var(i, 2)])
    for (a, b), d in zip(idx.tolist(), K[:, 2].tolist()):
        for c in range(3):
            s.add_clause([-var(a, c), -var(b, (c + d) % 3)])
    print(f"  encoded {n} labels, {len(K)} classes  ({time.time()-t0:.1f}s)", flush=True)
    ok = s.solve()
    print(f"  CaDiCaL: {'SAT' if ok else 'UNSAT'}  ({time.time()-t0:.1f}s)")
    if ok:
        model = s.get_model()
        tv = np.array(model[:3 * n]) > 0
        tv = tv.reshape(n, 3)
        y = tv.argmax(axis=1)
        assert tv.any(axis=1).all()
        bad = int(((y[idx[:, 1]] - y[idx[:, 0]] - K[:, 2]) % 3 == 0).sum())
        print(f"  model check on the core: certified violations {bad}")
        assert bad == 0
        np.save(tag + "_core_sol.npy", np.stack([labs, y], axis=1).astype(np.int32))

elif stage == "ext":
    z = np.load(tag + ".npz"); E = z["E"].astype(np.int64)
    cs = np.load(tag + "_core_sol.npy").astype(np.int64)
    npi = hi - lo
    key = np.stack([E[:, 0], E[:, 1], E[:, 2] % M], axis=1)
    _, first = np.unique(key, axis=0, return_index=True)
    Ec = E[np.sort(first)]
    m = len(Ec)
    ends = np.concatenate([Ec[:, 0], Ec[:, 1]]); eid = np.concatenate([np.arange(m), np.arange(m)])
    order = np.argsort(ends, kind="stable"); ends_s, eid_s = ends[order], eid[order]
    ptr = np.searchsorted(ends_s, np.arange(npi + 1)).tolist(); eidl = eid_s.tolist()
    r_, u_, d_ = Ec[:, 0].tolist(), Ec[:, 1].tolist(), Ec[:, 2].tolist()
    incore = np.zeros(npi, dtype=bool); incore[cs[:, 0]] = True
    vl = [-1] * npi
    for v, x in cs.tolist():
        vl[v] = x
    degl = np.diff(np.array(ptr)).tolist()
    removed = [False] * npi; dead = [False] * m; dorder = []
    stack = [v for v in range(npi) if not incore[v] and degl[v] < M]
    while stack:
        v = stack.pop()
        if removed[v]: continue
        removed[v] = True; dorder.append(v)
        for k in range(ptr[v], ptr[v + 1]):
            e = eidl[k]
            if dead[e]: continue
            dead[e] = True
            w = u_[e] if r_[e] == v else r_[e]
            degl[w] -= 1
            if not removed[w] and not incore[w] and degl[w] < M: stack.append(w)
    assert len(dorder) + int(incore.sum()) == npi, "core solution does not match the core"
    for v in reversed(dorder):
        f = 0
        for k in range(ptr[v], ptr[v + 1]):
            e = eidl[k]
            if r_[e] == v:
                w = u_[e]
                if vl[w] >= 0: f |= 1 << ((vl[w] - d_[e]) % M)
            else:
                w = r_[e]
                if vl[w] >= 0: f |= 1 << ((vl[w] + d_[e]) % M)
        x = 0
        while f >> x & 1: x += 1
        assert x < M
        vl[v] = x
    y = np.array(vl, dtype=np.int64)
    assert (y >= 0).all()
    bad = int(((y[E[:, 1]] - y[E[:, 0]] - E[:, 2]) % M == 0).sum())
    print(f"{tag}: full assignment of Pi ({npi} labels, {len(E)} triples): certified violations {bad}  ({time.time()-t0:.1f}s)")
    if bad == 0:
        np.save(tag + "_sol.npy", y.astype(np.int8))
