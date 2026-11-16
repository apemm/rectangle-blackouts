import random, math, sys
random.seed(int(sys.argv[3]) if len(sys.argv) > 3 else 1)
n = int(sys.argv[1]); D = int(sys.argv[2]); p = D / n
# G2 = G(n,p) on groups
adj = [set() for _ in range(n)]
for g in range(n):
    # geometric skipping
    j = g
    while True:
        r = random.random()
        j += 1 + int(math.log(1 - r) / math.log(1 - p))
        if j >= n: break
        adj[g].add(j); adj[j].add(g)
maxdeg = max(len(a) for a in adj)
# codegree sample
mc = 0
for _ in range(20000):
    a, b = random.sample(range(n), 2)
    mc = max(mc, len(adj[a] & adj[b]))
astar = math.ceil(1 + (2 * n / D) * (1 + math.log(D)))
s = 2 * astar
ncl = n // s
Gamma_bound = 8 * (1 + math.log(D)) + 1
Gamma_actual = (s - 1) * maxdeg / n
K = D / (20 * (1 + math.log(D)))
print(f"n={n} D={D} maxdeg={maxdeg} sampled max codeg={mc} a*={astar} s={s} cliques={ncl}")
print(f"Gamma actual={Gamma_actual:.2f} bound={Gamma_bound:.2f}; C4 group part s-1={s-1} vs n/K={n/K:.0f}; C5 <= 4s={4*s}")
# random greedy conflict-free matching
labels = list(range(n)); random.shuffle(labels)
clique = lambda x: x // s if x < ncl * s else -1 - x
free = set(range(n)); blocked = {}
placed = 0; per = {}
for x in labels:
    c = clique(x)
    B = blocked.setdefault(c, set())
    cand = [g for g in random.sample(sorted(free), min(len(free), 400)) if g not in B]
    if not cand:
        cand = [g for g in free if g not in B]
    if not cand: continue
    g = cand[0]
    free.discard(g); B.update(adj[g]); placed += 1; per[c] = per.get(c, 0) + 1
inclique = [per.get(c, 0) for c in range(ncl)]
print(f"greedy placed {placed}/{n} = {placed/n:.3f}; per clique {inclique} (each <= alpha(G2) <= a*={astar}); 3/4 n = {0.75*n:.0f}")
