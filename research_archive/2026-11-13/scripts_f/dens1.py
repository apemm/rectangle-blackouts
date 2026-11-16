import numpy as np, sys, time, math
rng = np.random.default_rng(1)
t0 = time.time()

def DT(T, h):
    A = (h + 1)//2; K = h//2; s = (T - 1)//2
    lo = max(0, -s); hi = min(A, K - s); n = hi - lo
    out = set()
    CH = 10**6
    for a in range(-(n - 1), n, CH):
        d = np.arange(a, min(a + CH, n), dtype=np.int64)
        Q = 20*d*d + 4*T*d + T*T
        L = np.floor(np.sqrt(Q.astype(np.float64))).astype(np.int64)
        for c in (-1, 0, 1):
            LL = L + c
            ok = (LL*LL == Q) & (LL > 0) & (LL < h) & (d != 0)
            for x in d[ok]:
                out.add(abs(int(x)))
    return sorted(out), n

def gsplit(T):
    g = 1; t = abs(T); p = 2
    while p*p <= t:
        if t % p == 0:
            e = 0
            while t % p == 0:
                t //= p; e += 1
            if p % 5 in (1, 4): g *= 2*e + 1
        p += 1
    if t > 1 and t % 5 in (1, 4): g *= 3
    return g

def rot_density(D, ns=400000):
    D = np.array(D, dtype=np.float64)
    best = 0.0
    for _ in range(ns // 20000):
        th = rng.random(20000)
        x = np.outer(th, D)
        x = np.abs(x - np.round(x))
        m = x.min(axis=1)
        best = max(best, m.max())
    return best

def zp_greedy(D, P, reps=60):
    Dm = np.unique(np.concatenate([np.array(D) % P, (-np.array(D)) % P]))
    Dm = Dm[Dm != 0]
    best = 0
    for _ in range(reps):
        order = rng.permutation(P)
        blocked = np.zeros(P, bool); cnt = 0
        for v in order:
            if not blocked[v]:
                cnt += 1
                blocked[(v + Dm) % P] = True
                blocked[v] = True
        best = max(best, cnt)
    return best / P

h = int(sys.argv[1]) if len(sys.argv) > 1 else 2*10**6
Ts = [int(x) for x in sys.argv[2:]]
for T in Ts:
    D, n = DT(T, h)
    k = len(D)
    D32 = [d//32 for d in D if d % 32 == 0]
    # perturbed comparison: same archimedean profile, arithmetic destroyed
    Dp = sorted(set(max(1, d + int(rng.integers(-40, 41))) for d in D))
    r = rot_density(D); rp = rot_density(Dp)
    zp = max(zp_greedy(D, P) for P in (1009, 2003, 3001))
    zpp = max(zp_greedy(Dp, P) for P in (1009, 2003, 3001))
    print(f"T={T} g={gsplit(T)} n_T={n} kappa={k} |D32|={len(D32)} rot={r:.4f} rot_pert={rp:.4f} "
          f"ZPgreedy={zp:.4f} ZP_pert={zpp:.4f} 1/kappa={1/k:.4f} t={time.time()-t0:.1f}", flush=True)
