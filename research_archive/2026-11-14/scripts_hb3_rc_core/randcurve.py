"""Random king-step Hilbert-type curve (Model K) and P candidate multigraph census.
Model K: every aligned dyadic square is a rank interval; a block of side s >= 2 is
traversed from an entry corner to a different exit corner; the parent's plan
(order of children = Hamiltonian path in K4 from child(entry) to child(exit), and the
children's entry/exit corners) is uniform among plans in which each child's exit
cell is king-adjacent to the next child's entry cell. Children are then generated
independently given their (entry, exit) types.
"""
import math, sys, time, random
import numpy as np

CORN = [(0, 0), (1, 0), (0, 1), (1, 1)]

def plans_for(half):
    """valid plans keyed by (entry, exit) parent corners (indices into CORN)."""
    def cell(child, corner):
        if half == 1:
            return child
        return (child[0] * half + corner[0] * (half - 1), child[1] * half + corner[1] * (half - 1))
    res = {}
    for en in range(4):
        for ex in range(4):
            if en == ex:
                continue
            cA, cB = CORN[en], CORN[ex]
            mids = [c for c in CORN if c != cA and c != cB]
            out = []
            for order in ([cA, mids[0], mids[1], cB], [cA, mids[1], mids[0], cB]):
                if half == 1:
                    ok = all(max(abs(order[t][0] - order[t + 1][0]), abs(order[t][1] - order[t + 1][1])) <= 1 for t in range(3))
                    if ok:
                        out.append((tuple(order), ((0, 0),) * 4))
                    continue
                # child corner sequences
                def rec(t, en_t, acc):
                    for ex_t in range(4):
                        if ex_t == en_t:
                            continue
                        if t == 3:
                            if ex_t == ex:
                                out.append((tuple(order), tuple(acc + [(en_t, ex_t)])))
                            continue
                        c1 = cell(order[t], CORN[ex_t])
                        for en_n in range(4):
                            c2 = cell(order[t + 1], CORN[en_n])
                            if max(abs(c1[0] - c2[0]), abs(c1[1] - c2[1])) == 1:
                                rec(t + 1, en_n, acc + [(en_t, ex_t)])
                rec(0, en, [])
            assert out, (half, en, ex)
            res[(en, ex)] = out
    return res

def random_curve(q, seed):
    rng = random.Random(seed)
    P = {1: plans_for(1), 2: plans_for(2), 4: plans_for(4)}
    xs = np.empty(q * q, dtype=np.int64); ys = np.empty(q * q, dtype=np.int64)
    pos = [0]
    # iterative stack: (x0, y0, s, en, ex)
    stack = [(0, 0, q, 0, 1)]
    while stack:
        x0, y0, s, en, ex = stack.pop()
        if s == 1:
            xs[pos[0]] = x0; ys[pos[0]] = y0; pos[0] += 1
            continue
        half = s // 2
        order, cs = rng.choice(P[min(half, 4)][(en, ex)])
        for t in (3, 2, 1, 0):
            c = order[t]
            stack.append((x0 + c[0] * half, y0 + c[1] * half, half, cs[t][0], cs[t][1]))
    return np.stack([xs, ys], axis=1)

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

def check_locality(xy, trials=200000, seed=1):
    rng = np.random.default_rng(seed)
    n = len(xy)
    r = rng.integers(0, n, trials); s = rng.integers(0, n, trials)
    m = r != s
    r, s = r[m], s[m]
    dx = np.abs(xy[r] - xy[s]).max(axis=1)
    worst = float((dx.astype(float) ** 2 / np.abs(r - s)).max())
    # consecutive cells king-adjacent
    step = np.abs(np.diff(xy, axis=0)).max(axis=1)
    return worst, int(step.max())

def pyth(X, h):
    hs = (X // 2) ** 2
    out = {}
    for a in range(1, math.isqrt(hs) + 1):
        if hs % a == 0:
            b = hs // a
            if a + b < h and (b - a) % 2:
                out[b - a] = a + b
    return out

def build(xy, h, S, M):
    A, K = (h + 1) // 2, h // 2
    n = len(xy)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    rs, ss = [], []
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            ysd = pyth(X, h)
            if not ysd:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ysd.items():
                hyp[y] = L
            hit = np.zeros(n - d, dtype=bool)
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(r2 - r1)]
                sm = r1 + r2
                hit |= (L > 0) & (sm - L >= 2) & (sm + L <= 2 * h)
            hit &= active[:-d] & active[d:]
            idx = np.nonzero(hit)[0]
            rs.append(idx); ss.append(idx + d)
    r = np.concatenate(rs); s = np.concatenate(ss)
    return r, s, int(active.sum())

def cores(r, s, n):
    """weighted degeneracy and size of the k-core for each k up to degeneracy."""
    deg = np.bincount(r, minlength=n) + np.bincount(s, minlength=n)
    maxdeg = int(deg.max())
    u = np.concatenate([r, s]); v = np.concatenate([s, r])
    order = np.argsort(u, kind="stable"); v = v[order]
    start = np.zeros(n + 1, dtype=np.int64)
    np.cumsum(np.bincount(u, minlength=n), out=start[1:])
    deg = deg.tolist(); start = start.tolist(); v = v.tolist()
    buckets = [[] for _ in range(maxdeg + 1)]
    verts = [x for x in range(n) if deg[x] > 0]
    for x in verts:
        buckets[deg[x]].append(x)
    removed = bytearray(n)
    cur = 0; done = 0; core_k = 0; total = len(verts)
    coreval = {}
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
        coreval[x] = core_k
        for t in range(start[x], start[x + 1]):
            y = v[t]
            if not removed[y]:
                deg[y] -= 1
                buckets[deg[y]].append(y)
                if deg[y] < cur:
                    cur = deg[y]
    sizes = {}
    for k in range(1, core_k + 1):
        sizes[k] = sum(1 for c in coreval.values() if c >= k)
    return maxdeg, core_k, sizes

if __name__ == "__main__":
    mode = sys.argv[1]; h = int(sys.argv[2]); S = int(sys.argv[3]); M = int(sys.argv[4])
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    t0 = time.time()
    xy = hilbert_array(q) if mode == "hil" else random_curve(q, seed)
    if mode == "loc":
        print("locality worst dx^2/dr, max step:", check_locality(xy)); sys.exit()
    r, s, nlab = build(xy, h, S, M)
    mx, dg, sizes = cores(r, s, q * q)
    print(f"{mode} seed={seed} h={h} S={S} M={M} E={len(r)} mean={2*len(r)/nlab:.3f} maxdeg={mx} degen={dg} cores={sizes} t={time.time()-t0:.1f}s")
