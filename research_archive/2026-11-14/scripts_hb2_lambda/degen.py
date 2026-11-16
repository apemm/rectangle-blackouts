"""Degeneracy of the Lambda3 candidate constraint hypergraph (all private choices).
Constraint = (v, f, g, xi_f - xi_v, xi_g - xi_v): given two of the three
choices it forbids at most one value of the third.  Peeling degeneracy d*:
greedy in reverse peeling order succeeds when M >= d* + 1."""
import sys, json, heapq
import numpy as np
from collections import defaultdict
from angles import setup, enumerate_angles

h, S, M = map(int, sys.argv[1:4])
D = setup(h, S, M, 0)
q2 = D['q'] ** 2
act = D['act']
own = -np.ones(M * q2 + 1, np.int64)
s = np.arange(M * q2)
own[:M * q2] = np.where(act[s // M], s // M, -1)
D['owner'] = own
cons = set()
for xv in range(M):
    D['slot'] = M * np.arange(q2, dtype=np.int64) + xv
    for (v, p, f, g, sf, sg) in enumerate_angles(D, slots=True):
        cons.add((v, f, g, sf % M - xv, sg % M - xv))
deg = defaultdict(int)
role = [defaultdict(int), defaultdict(int), defaultdict(int)]
inc = defaultdict(list)
two = 0
for k, (v, f, g, df, dg) in enumerate(cons):
    J = {v, f, g}
    if f == g:
        two += 1
    for z in J:
        deg[z] += 1
        inc[z].append(k)
    role[0][v] += 1; role[1][g] += 1; role[2][f] += 1
cl = list(cons)
alive = [True] * len(cl)
d = dict(deg)
heap = [(dd, z) for z, dd in d.items()]
heapq.heapify(heap)
removed = set()
dstar = 0
while heap:
    dd, z = heapq.heappop(heap)
    if z in removed or dd != d[z]:
        continue
    dstar = max(dstar, dd)
    removed.add(z)
    for k in inc[z]:
        if alive[k]:
            alive[k] = False
            v, f, g, _, _ = cl[k]
            for y in {v, f, g}:
                if y != z and y not in removed:
                    d[y] -= 1
                    heapq.heappush(heap, (d[y], y))
nl = int(act.sum())
print(json.dumps({'h': h, 'S': S, 'M': M, 'labels': nl, 'constraints': len(cons),
                  'two_label': two, 'mean_deg': 3 * len(cons) / nl,
                  'max_deg': max(deg.values()) if deg else 0,
                  'max_vertex': max(role[0].values()) if cons else 0,
                  'max_near': max(role[1].values()) if cons else 0,
                  'max_far': max(role[2].values()) if cons else 0,
                  'degeneracy': dstar, 'greedy_ok': dstar + 1 <= M,
                  'MS4_over_16h': M * S ** 4 / (16 * (h - 1))}))
