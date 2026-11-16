"""Where do the cores sit?  Mean weighted degree and k-core membership by dyadic band of
Y = |2T+1|, T = j - i, for the Hilbert curve and the Model K random curve."""
import sys, time
import numpy as np
import randcurve as R

def core_numbers(r, s, n):
    deg = np.bincount(r, minlength=n) + np.bincount(s, minlength=n)
    maxdeg = int(deg.max())
    u = np.concatenate([r, s]); v = np.concatenate([s, r])
    order = np.argsort(u, kind="stable"); v = v[order]
    start = np.zeros(n + 1, dtype=np.int64)
    np.cumsum(np.bincount(u, minlength=n), out=start[1:])
    deg0 = deg.copy()
    deg = deg.tolist(); start = start.tolist(); v = v.tolist()
    buckets = [[] for _ in range(maxdeg + 1)]
    for x in range(n):
        if deg[x] > 0:
            buckets[deg[x]].append(x)
    removed = bytearray(n); cn = np.zeros(n, dtype=np.int64)
    cur = 0; done = 0; ck = 0; total = int((deg0 > 0).sum())
    while done < total:
        while cur > 0 and buckets[cur - 1]:
            cur -= 1
        while not buckets[cur]:
            cur += 1
        x = buckets[cur].pop()
        if removed[x] or deg[x] != cur:
            continue
        removed[x] = 1; done += 1; ck = max(ck, cur); cn[x] = ck
        for t in range(start[x], start[x + 1]):
            y = v[t]
            if not removed[y]:
                deg[y] -= 1; buckets[deg[y]].append(y)
                if deg[y] < cur:
                    cur = deg[y]
    return deg0, cn

if __name__ == "__main__":
    mode, h, S, M = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    seed = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    q = 1 << (max((h + 1) // 2, h // 2) - 1).bit_length()
    xy = R.hilbert_array(q) if mode == "hil" else R.random_curve(q, seed)
    r, s, nlab = R.build(xy, h, S, M)
    deg, cn = core_numbers(r, s, q * q)
    Y = np.abs(2 * (xy[:, 1] - xy[:, 0]) + 1)
    band = np.floor(np.log2(Y)).astype(int)
    print(f"{mode} h={h} S={S} M={M} mean={deg.sum()/nlab:.3f} degen={cn.max()}")
    for b in range(band.max() + 1):
        m = band == b
        if m.sum() == 0:
            continue
        line = f" Y in [2^{b},2^{b+1}): labels={m.sum():7d} meandeg={deg[m].mean():.3f}"
        for k in (2, 3, 4):
            line += f" {k}core={int((cn[m] >= k).sum()):6d}"
        print(line)
