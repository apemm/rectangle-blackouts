"""Candidate P multigraph (in-strip, as in the archive's finite search) for
small strides, to see whether weighted degeneracy tracks the mean degree.
Stride below 32 is used ONLY as a device to raise the mean degree; the
same-parity exclusion is not claimed there.
"""
import math, sys, time
import numpy as np

def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64)
    n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt
        n *= 2
    return xy

def pyth(X, h):
    hs = (X // 2) ** 2
    out = {}
    for a in range(1, math.isqrt(hs) + 1):
        if hs % a == 0:
            b = hs // a
            if a + b < h and (b - a) % 2:
                out[b - a] = a + b
    return out

def run(h, S, M):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    rs, ss, ds = [], [], []
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            ys = pyth(X, h)
            if not ys:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ys.items():
                hyp[y] = L
            hit = np.zeros(q * q - d, dtype=bool)
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(r2 - r1)]
                sm = r1 + r2
                hit |= (L > 0) & (sm - L >= 2) & (sm + L <= 2 * h)
            hit &= active[:-d] & active[d:]
            idx = np.nonzero(hit)[0]
            rs.append(idx); ss.append(idx + d); ds.append(np.full(len(idx), delta))
    r = np.concatenate(rs); s = np.concatenate(ss)
    E = len(r)
    nlab = int(active.sum())
    mu = 2 * E / nlab
    # weighted degeneracy by bucket peeling
    n = q * q
    deg = np.bincount(r, minlength=n) + np.bincount(s, minlength=n)
    maxdeg = int(deg.max())
    # CSR
    u = np.concatenate([r, s]); v = np.concatenate([s, r])
    order = np.argsort(u, kind="stable")
    v = v[order]
    start = np.zeros(n + 1, dtype=np.int64)
    np.cumsum(np.bincount(u, minlength=n), out=start[1:])
    deg = deg.tolist(); start = start.tolist(); v = v.tolist()
    buckets = [[] for _ in range(maxdeg + 1)]
    verts = [x for x in range(n) if deg[x] > 0]
    for x in verts:
        buckets[deg[x]].append(x)
    removed = bytearray(n)
    k = 0; cur = 0; done = 0; core_k = 0
    total = len(verts)
    while done < total:
        while cur > 0 and buckets[cur - 1]:
            cur -= 1
        while not buckets[cur]:
            cur += 1
        x = buckets[cur].pop()
        if removed[x] or deg[x] != cur:
            continue
        removed[x] = 1; done += 1
        core_k = max(core_k, cur)
        for t in range(start[x], start[x + 1]):
            y = v[t]
            if not removed[y]:
                deg[y] -= 1
                buckets[deg[y]].append(y)
                if deg[y] < cur:
                    cur = deg[y]
    return E, nlab, mu, maxdeg, core_k

if __name__ == "__main__":
    h = int(sys.argv[1]); S = int(sys.argv[2]); Ms = [int(t) for t in sys.argv[3:]]
    for M in Ms:
        t0 = time.time()
        E, nlab, mu, mx, dg = run(h, S, M)
        K = 4 * h / S / S
        model = 16 / (math.pi * S) * math.log(K) + 1.10 / S
        print(f"h={h} S={S} M={M} edges={E} mean_deg={mu:.3f} model~{model:.3f} "
              f"max_deg={mx} weighted_degeneracy={dg} t={time.time()-t0:.1f}s")
        sys.stdout.flush()
