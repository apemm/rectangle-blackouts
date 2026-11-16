# Time-resolved check of the line-product prediction (1 - tau*(n-1)/N) * exp(-tau*(lambda - (n-1)/N))
# for the toy cover of toy_greedy.py (coincidence line kept exact, other lines exponential).
import numpy as np, math, sys
from toy_greedy import offsets
rng = np.random.default_rng(7)
n, N = int(sys.argv[1]), int(sys.argv[2])
half = N//2
off = [None] + [offsets(dr, half) for dr in range(1, n)]
deg = np.array([sum(len(off[abs(r-e)]) for r in range(n) if r != e) + (n-1) for e in range(n)])
lam = deg.mean()/N; lc = (n-1)/N
blocked = np.zeros((n, N), dtype=bool); order = rng.permutation(n); placed = np.zeros(n, bool)
bins = {}
fails = 0
for k, f in enumerate(order):
    free = np.flatnonzero(~blocked[f]); tau = k/n
    b = int(tau*10); bins.setdefault(b, []).append(len(free)/N)
    if len(free) == 0: fails += 1; continue
    j = rng.choice(free); placed[f] = True
    others = np.flatnonzero(~placed)
    blocked[others, j] = True
    for e in others:
        o = off[abs(int(e)-int(f))]
        if len(o): blocked[e, (j+o) % N] = True
print(f"n={n} N={N} lambda={lam:.3f} coincidence part={lc:.3f} fails={fails}")
for b in sorted(bins):
    tau = (b+0.5)/10
    pred = (1 - tau*lc)*math.exp(-tau*(lam-lc))
    naive = math.exp(-tau*lam)
    print(f"tau~{tau:.2f} observed={np.mean(bins[b]):.4f} line-product={pred:.4f} exp(-lam tau)={naive:.4f} first-moment={max(0,1-tau*lam):.4f}")
