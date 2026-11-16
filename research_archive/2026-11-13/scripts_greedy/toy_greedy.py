# Toy line-structured cover: n labels with rows 0..n-1 (one parity, one label per row),
# N cyclic slots. (e,j) ~ (f,j') iff dj^2 + dr^2 is a perfect square (dr != 0, dj taken mod N
# as the representative in (-N/2, N/2]), or j = j' (coincidence).
# Random greedy: random label order, uniform free slot. Records: lambda = mean degree / N,
# success, and free fraction seen by labels vs exp(-lambda * tau).
import numpy as np, math, sys, time
rng = np.random.default_rng(1)

def offsets(dr, half):
    # all dj in [-half, half], dj != 0, with dj^2 + dr^2 a square: dr^2 = (L-dj)(L+dj)
    s = set(); A = dr*dr
    for u in range(1, dr+1):
        if A % u: continue
        v = A//u
        if (u+v) % 2: continue
        dj = (v-u)//2
        if 0 < dj <= half: s.add(dj); s.add(-dj)
    return np.array(sorted(s), dtype=np.int64)

def run(n, N, trials=3):
    half = N//2
    off = [None] + [offsets(dr, half) for dr in range(1, n)]
    deg = np.array([sum(len(off[abs(r-e)]) for r in range(n) if r != e) + (n-1) for e in range(n)])
    lam = deg.mean()/N
    res = []
    for t in range(trials):
        blocked = np.zeros((n, N), dtype=bool)
        order = rng.permutation(n); placed = np.zeros(n, bool); fails = 0
        ratios = []
        for k, f in enumerate(order):
            free = np.flatnonzero(~blocked[f])
            tau = k/n
            ratios.append((tau, len(free)/N))
            if len(free) == 0: fails += 1; continue
            j = rng.choice(free); placed[f] = True
            others = np.flatnonzero(~placed); others = others[others != f]
            blocked[others, j] = True
            for e in others:
                o = off[abs(int(e)-int(f))]
                if len(o): blocked[e, (j + o) % N] = True
        late = [r for (tau, r) in ratios if tau > 0.9]
        res.append((fails, np.mean(late)))
    return lam, deg.mean(), res

t0 = time.time()
n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
for N in [int(x) for x in sys.argv[2:]]:
    lam, D, res = run(n, N)
    pred = math.exp(-lam*0.95)
    print(f"n={n} N={N} D={D:.0f} D/N={lam:.2f} lnN={math.log(N):.2f} fails={[r[0] for r in res]} "
          f"late free frac={[round(r[1],4) for r in res]} exp(-lam*.95)={pred:.4f} t={time.time()-t0:.1f}s", flush=True)
