"""Average I(w) over random w in P, split by |X_w| <= h (moderate) vs |X_w| >= h^1.5 (flat)."""
import sys, math, time
import numpy as np
from tri_count import pyth_set

def I_of(P, keys, Xmax, h, X1, y1):
    X3 = P[:, 0] - X1; y3 = P[:, 1] - y1
    ok = (X3 != 0) & (y3 != 0) & (np.abs(y3) < h) & ((X1 * P[:, 1] - P[:, 0] * y1) != 0)
    idx = np.nonzero(ok)[0]
    k3 = (X3[idx] + 2 * Xmax) * (4 * h) + (y3[idx] + 2 * h)
    pos = np.minimum(np.searchsorted(keys, k3), keys.size - 1)
    return int((keys[pos] == k3).sum())

t0 = time.time()
rng = np.random.default_rng(7)
for h in [int(s) for s in sys.argv[1:]]:
    P = pyth_set(h)
    Xmax = int(np.abs(P[:, 0]).max()) + 1
    keys = np.sort((P[:, 0] + 2 * Xmax) * (4 * h) + (P[:, 1] + 2 * h))
    mod = np.nonzero(np.abs(P[:, 0]) <= h)[0]
    flat = np.nonzero(np.abs(P[:, 0]) >= h ** 1.5)[0]
    L = math.log(h)
    out = []
    for name, pool in (("moderate |X|<=h", mod), ("flat |X|>=h^1.5", flat)):
        sm = rng.choice(pool, size=min(150, pool.size), replace=False)
        vals = [I_of(P, keys, Xmax, h, int(P[i, 0]), int(P[i, 1])) for i in sm]
        out.append(f"{name}: frac of P={pool.size/len(P):.3f} meanI={np.mean(vals):.2f} meanI/h={np.mean(vals)/h:.4f} meanI*L^2/h={np.mean(vals)*L*L/h:.2f} max={max(vals)}")
    print(f"h={h} |P|={len(P)} ; " + " ; ".join(out) + f"  [{time.time()-t0:.1f}s]", flush=True)
