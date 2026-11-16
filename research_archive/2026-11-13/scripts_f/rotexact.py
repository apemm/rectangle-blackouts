import numpy as np, sys, time, math
sys.path.insert(0, '.')
t0 = time.time()
rng = np.random.default_rng(7)
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

def good_exists(D, delta):
    # is there theta in [0,1/2] with ||theta d|| >= delta for all d?  sweep over bad intervals
    starts = []; ends = []
    for d in D:
        k = np.arange(0, d//2 + 2)
        starts.append((k - delta)/d); ends.append((k + delta)/d)
    s = np.concatenate(starts); e = np.concatenate(ends)
    o = np.argsort(s, kind='stable'); s = s[o]; e = e[o]
    reach = np.maximum.accumulate(e)
    gaps = np.nonzero(s[1:] > reach[:-1])[0]
    for g in gaps:
        th = (reach[g] + s[g+1])/2
        if 0 <= th <= 0.5: return th
    return None
def best_rot(D, lo, hi, it=14):
    best = None
    for _ in range(it):
        mid = (lo + hi)/2
        th = good_exists(D, mid)
        if th is not None: lo, best = mid, th
        else: hi = mid
        if time.time() - t0 > 52: break
    return lo, best
h = int(sys.argv[1])
for T in map(int, sys.argv[2:]):
    D, n = DT(T, h); k = len(D)
    Dp = sorted(set(max(1, d + int(rng.integers(-40, 41))) for d in D))
    d1, th = best_rot(D, 1/(2*k), 0.5)
    d2, _ = best_rot(Dp, 1/(2*len(Dp)), 0.5)
    print(f"T={T} kappa={k} maxD={max(D)} exact delta*={d1:.5f} kappa*delta={k*d1:.2f}  perturbed: {d2:.5f} ({len(Dp)*d2:.2f})  ln(maxD)/2={math.log(max(D))/2:.2f}  t={time.time()-t0:.1f}", flush=True)
