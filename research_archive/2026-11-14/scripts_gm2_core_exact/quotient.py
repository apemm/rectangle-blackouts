"""Shift-quotient test (Theorem II.1 of gap_mixing_round1_synthesis.md) on a saved M-core.

Usage: py -B quotient.py prefix M order(freq|rank|rand) [seed]
1. Partition the core labels into pieces whose induced constraints carry at most
   two distinct gaps, by greedy union along constraints (never forming the M = 3
   exceptional pairs {3, 9k+4}, {3, 9k+5} of Prop. I.6).
2. Give each piece a mod-M certified assignment (exact search, mode 'mod'; checked).
3. Quotient: crossing constraint e = (r in P, u in Q, delta) forbids
   kappa_Q - kappa_P = c_e := y_r - y_u + delta (mod M).  Peel the quotient to its
   weighted M-core over distinct (P, Q, c) triples and solve that core exactly.
4. Assemble xi = (y + kappa) mod M and check every core constraint.
Writes prefix_quot_sol.npy when it succeeds.
"""
import sys, time, random
from collections import defaultdict, Counter
import numpy as np
from dpll import solve_component
from core_stats import components

pre, M, order = sys.argv[1], int(sys.argv[2]), sys.argv[3]
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 0
C = np.load(pre + "_core.npy").astype(np.int64)
t0 = time.time()
E = C.tolist()
gap = [M * (u - r) + d for r, u, d in E]
labels = sorted({v for r, u, _ in E for v in (r, u)})
par = {v: v for v in labels}
pg = {v: set() for v in labels}                      # gaps induced in the piece
nb = {v: defaultdict(set) for v in labels}           # neighbour piece -> gaps of crossing edges
for k, (r, u, d) in enumerate(E):
    nb[r][u].add(gap[k]); nb[u][r].add(gap[k])


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]; x = par[x]
    return x


def exceptional(gs):
    if M != 3 or len(gs) != 2 or 3 not in gs:
        return False
    o = max(gs)
    return o % 9 in (4, 5)


cnt = Counter(gap)
idx = list(range(len(E)))
if order == "freq":
    idx.sort(key=lambda k: (-cnt[gap[k]], gap[k]))
elif order == "rank":
    idx.sort(key=lambda k: E[k][0])
else:
    random.Random(seed).shuffle(idx)
for k in idx:
    r, u, _ = E[k]
    a, b = find(r), find(u)
    if a == b:
        continue
    new = pg[a] | pg[b] | nb[a][b]
    if len(new) > 2 or exceptional(new):
        continue
    if len(nb[a]) < len(nb[b]):
        a, b = b, a
    par[b] = a; pg[a] = new; del pg[b]
    del nb[a][b]
    for w, gs in nb[b].items():
        if w == a:
            continue
        nb[a][w] |= gs
        nw = nb[w]; nw[a] |= nw.pop(b)
    del nb[b]
pieces = defaultdict(list)
for v in labels:
    pieces[find(v)].append(v)
print(f"{pre} order={order} seed={seed}: core labels {len(labels)}, constraints {len(E)}, pieces {len(pieces)}, "
      f"piece sizes max {max(len(p) for p in pieces.values())}, "
      f"pieces by gap count {sorted(Counter(len(pg[p]) for p in pieces).items())}", flush=True)

# certified assignment per piece
inside = defaultdict(list); cross = []
for (r, u, d) in E:
    a, b = find(r), find(u)
    (inside[a].append((r, u, d)) if a == b else cross.append((r, u, d)))
y = {v: 0 for v in labels}
fails = 0
for p, rows in inside.items():
    res, s, _ = solve_component(np.array(rows, dtype=np.int64), M, "mod", 200000)
    if res != "SAT":
        fails += 1; continue
    y.update(s)
    for r, u, d in rows:
        assert (y[u] - y[r] - d) % M != 0
print(f"  pieces without certified assignment: {fails}", flush=True)
assert fails == 0

# quotient
Q = {}
for r, u, d in cross:
    a, b = find(r), find(u)
    c = (y[r] - y[u] + d) % M         # forbids kappa_b - kappa_a = c
    if a > b:
        a, b, c = b, a, (-c) % M
    Q[(a, b, c)] = 1
pairc = Counter((a, b) for a, b, c in Q)
print(f"  piece pairs with crossing constraints {len(pairc)}, by number of forbidden shifts {sorted(Counter(pairc.values()).items())}", flush=True)
qE = np.array(list(Q), dtype=np.int64)
pid = {p: k for k, p in enumerate(sorted(pieces))}
qE[:, 0] = [pid[p] for p in qE[:, 0]]; qE[:, 1] = [pid[p] for p in qE[:, 1]]
# forbidding kappa_b - kappa_a = c (mod M) is a 'mod' constraint (a, b, c)
alive = np.ones(len(qE), dtype=bool); npc = len(pid)
while True:
    deg = np.bincount(qE[alive, 0], minlength=npc) + np.bincount(qE[alive, 1], minlength=npc)
    kill = alive & ((deg < M)[qE[:, 0]] | (deg < M)[qE[:, 1]])
    if not kill.any():
        break
    alive &= ~kill
qc = qE[alive]
nqc = len(np.unique(qc[:, :2])) if len(qc) else 0
print(f"  quotient: pieces {npc}, distinct (P,Q,c) {len(qE)}, weighted {M}-core pieces {nqc}, triples {len(qc)}", flush=True)

# solve quotient fully: core exactly, then peel extension (reuse exact search on the whole quotient)
res_all = True; kap = {}
for comp in components(qE):
    res, s, nodes = solve_component(comp, M, "mod", 3_000_000)
    if res != "SAT":
        print(f"  quotient component {len(np.unique(comp[:, :2]))} pieces: {res} nodes {nodes}"); res_all = False
    else:
        kap.update(s)
if res_all:
    inv = {k: p for p, k in pid.items()}
    xi = {}
    for k, p in inv.items():
        for v in pieces[p]:
            xi[v] = (y[v] + kap.get(k, 0)) % M
    bad = sum(1 for r, u, d in E if xi[u] - xi[r] == d)
    print(f"  assembled assignment: violated core constraints {bad}   ({time.time()-t0:.1f}s)")
    if bad == 0:
        np.save(pre + "_quot_sol.npy", np.array(sorted(xi.items()), dtype=np.int64))

# exact quotient: crossing constraint e forbids exactly the shift pairs with
# ((y_u + kQ) mod M) - ((y_r + kP) mod M) = delta  (a subset of the c_e line)
from csp import solve as csp_solve
inv = {k: p for p, k in pid.items()}
ng = set(); items = set()
for r, u, d in cross:
    a, b = pid[find(r)], pid[find(u)]
    tabl = tuple((kp, kq) for kp in range(M) for kq in range(M)
                 if (y[u] + kq) % M - (y[r] + kp) % M == d)
    for kp, kq in tabl:
        ng.add((a, kp, b, kq))
    items.add((a, b, tabl))
# weighted core of the exact quotient: each item forbids at most one shift of one end given the other
it = list(items); alive = [True] * len(it); degq = Counter()
for a, b, _ in it:
    degq[a] += 1; degq[b] += 1
changed = True
while changed:
    changed = False
    for k, (a, b, _) in enumerate(it):
        if alive[k] and (degq[a] < M or degq[b] < M):
            alive[k] = False; degq[a] -= 1; degq[b] -= 1; changed = True
corep = {v for k, (a, b, _) in enumerate(it) if alive[k] for v in (a, b)}
print(f"  exact quotient: nogoods {len(ng)}, distinct items {len(it)}, weighted {M}-core pieces {len(corep)}", flush=True)
res, kv, nodes = csp_solve(npc, list(ng), M, 3_000_000)
print(f"  exact quotient search: {res}, nodes {nodes}", flush=True)
if res == "SAT":
    xi = {v: (y[v] + kv[pid[find(v)]]) % M for v in labels}
    bad = sum(1 for r, u, d in E if xi[u] - xi[r] == d)
    print(f"  assembled from exact quotient: violated core constraints {bad}   ({time.time()-t0:.1f}s)")
    if bad == 0:
        np.save(pre + "_xquot_sol.npy", np.array(sorted(xi.items()), dtype=np.int64))
