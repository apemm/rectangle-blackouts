"""Core structure of the candidate P multigraph and a min-conflicts test on the M-core."""
import sys, time, random
import numpy as np
from degeneracy_vs_mu import hilbert_array, pyth

def edges(h, S, M):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    xy = hilbert_array(q)
    active = (xy[:, 0] < A) & (xy[:, 1] < K)
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    out = []
    for d in range(1, ((h - 1) // S + M - 1) // M + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h: continue
            ys = pyth(X, h)
            if not ys: continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ys.items(): hyp[y] = L
            hit = np.zeros(q * q - d, dtype=bool)
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(r2 - r1)]; sm = r1 + r2
                hit |= (L > 0) & (sm - L >= 2) & (sm + L <= 2 * h)
            hit &= active[:-d] & active[d:]
            for r in np.nonzero(hit)[0].tolist():
                out.append((r, r + d, delta))
    return out

def kcore(E, k):
    adj = {}
    for i, (r, s, dl) in enumerate(E):
        adj.setdefault(r, []).append(i); adj.setdefault(s, []).append(i)
    deg = {x: len(l) for x, l in adj.items()}
    alive = set(adj); stack = [x for x in alive if deg[x] < k]
    dead_e = set()
    while stack:
        x = stack.pop()
        if x not in alive: continue
        alive.discard(x)
        for i in adj[x]:
            if i in dead_e: continue
            dead_e.add(i)
            r, s, _ = E[i]; y = s if r == x else r
            if y in alive:
                deg[y] -= 1
                if deg[y] < k: stack.append(y)
    Ec = [E[i] for i in range(len(E)) if i not in dead_e]
    return alive, Ec

def minconf(V, Ec, M, secs, seed=1):
    rng = random.Random(seed)
    V = list(V); ch = {x: 0 for x in V}
    adj = {x: [] for x in V}
    for i, (r, s, dl) in enumerate(Ec):
        adj[r].append(i); adj[s].append(i)
    viol = lambda i: ch[Ec[i][1]] - ch[Ec[i][0]] == Ec[i][2]
    bad = {i for i in range(len(Ec)) if viol(i)}
    t0 = time.time(); steps = 0; best = len(bad)
    while bad and time.time() - t0 < secs:
        i = rng.choice(tuple(bad)) if steps % 50 == 0 else next(iter(bad))
        x = rng.choice(Ec[i][:2])
        cost = [0] * M
        for j in adj[x]:
            r, s, dl = Ec[j]
            if r == x: f = ch[s] - dl
            else: f = ch[r] + dl
            if 0 <= f < M: cost[f] += 1
        m = min(cost)
        ch[x] = rng.randrange(M) if rng.random() < 0.05 else rng.choice([c for c in range(M) if cost[c] == m])
        for j in adj[x]:
            if viol(j): bad.add(j)
            else: bad.discard(j)
        best = min(best, len(bad)); steps += 1
    return len(bad), best, steps

if __name__ == "__main__":
    h, S, M = map(int, sys.argv[1:4])
    E = edges(h, S, M)
    pairs = {(r, s) for r, s, _ in E}
    V, Ec = kcore(E, M)
    cp = {(r, s) for r, s, _ in Ec}
    print(f"h={h} S={S} M={M} edges={len(E)} distinct_pairs={len(pairs)} "
          f"M-core: vertices={len(V)} edges={len(Ec)} distinct_pairs={len(cp)}", flush=True)
    if V:
        left, best, steps = minconf(V, Ec, M, 45)
        print(f"min-conflicts on M-core: remaining={left} best={best} steps={steps}", flush=True)
