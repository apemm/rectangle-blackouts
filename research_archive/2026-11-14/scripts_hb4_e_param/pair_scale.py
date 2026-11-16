"""kappa(h) = P(0)/mean_{1<=tau<=30} P(tau), all |dq|>=1, bulk Y >= h/8."""
import sys, time
from collections import defaultdict
from pair_corr import vectors
S = int(sys.argv[1])
for lg in map(int, sys.argv[2:]):
    h = 2 ** lg; t0 = time.time()
    V = vectors(S, h)
    cnt = defaultdict(int)
    for q, Y in V:
        if Y >= h // 8: cnt[Y] += 1
    # number of (q,q') pairs with q != q' : n(Y) n(Y+2tau) minus same-q pairs (same q impossible for tau!=0? q fixed, Y,Y' both legs: allowed) 
    byY = defaultdict(set)
    for q, Y in V:
        if Y >= h // 8: byY[Y].add(q)
    def P(tau):
        tot = 0
        for Y, n in cnt.items():
            m = cnt.get(Y + 2 * tau)
            if m:
                tot += n * m - len(byY[Y] & byY[Y + 2 * tau])
        return tot
    p0 = P(0); ps = [P(t) for t in range(1, 31)]
    mean = sum(ps) / 30
    print(f"S={S} h=2^{lg} vec={len(V)} P0={p0} mean={mean:.1f} kappa={p0/mean:.2f} P(1)={ps[0]} P0/P1={p0/max(ps[0],1):.2f} t={time.time()-t0:.1f}s", flush=True)
