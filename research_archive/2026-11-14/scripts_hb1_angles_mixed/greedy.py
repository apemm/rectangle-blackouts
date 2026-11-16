"""Rank-order greedy over all candidate right-angle events (choices included)."""
import sys, json, numpy as np
from collections import defaultdict
from angles import setup, enumerate_angles
h, S, M = map(int, sys.argv[1:4])
D = setup(h, S, M, 0)
q2 = D['q'] ** 2
act = D['act']
own = -np.ones(M * q2 + 1, np.int64)
s = np.arange(M * q2)
own[:M*q2] = np.where(act[s // M], s // M, -1)
D['owner'] = own
events = []
for xv in range(M):
    D['slot'] = M * np.arange(q2, dtype=np.int64) + xv
    for (v, p, f, g, sf, sg) in enumerate_angles(D, slots=True):
        ev = {v: xv, f: sf % M, g: sg % M}
        if f == g and sf != sg:
            continue  # inconsistent choice for one label
        events.append(ev)
by_last = defaultdict(list)
for ev in events:
    by_last[max(ev)].append(ev)
xi = {}
fail = 0
maxforb = 0
for e in sorted(by_last):
    forb = set()
    for ev in by_last[e]:
        if all(xi.get(z, 0) == c for z, c in ev.items() if z != e):
            forb.add(ev[e])
    maxforb = max(maxforb, len(forb))
    allowed = [c for c in range(M) if c not in forb]
    if allowed:
        xi[e] = allowed[0]
    else:
        xi[e] = 0
        fail += 1
# verify
bad = sum(all(xi.get(z, 0) == c for z, c in ev.items()) for ev in events)
print(json.dumps({'h': h, 'S': S, 'M': M, 'events': len(events), 'greedy_failures': fail,
                  'max_forbidden': maxforb, 'violated_after': bad}))
# local search repair
import random
rng = random.Random(1)
inc = defaultdict(list)
for k, ev in enumerate(events):
    for z in ev:
        inc[z].append(k)
def viol(k):
    return all(xi.get(z, 0) == c for z, c in events[k].items())
V = {k for k in range(len(events)) if viol(k)}
steps = 0
while V and steps < 200000:
    steps += 1
    k = rng.choice(tuple(V))
    z = rng.choice(list(events[k]))
    best, bestc = None, None
    old = xi.get(z, 0)
    for c in range(M):
        xi[z] = c
        cost = sum(viol(j) for j in inc[z])
        if bestc is None or cost < bestc or (cost == bestc and rng.random() < 0.5):
            best, bestc = c, cost
    xi[z] = best
    for j in inc[z]:
        if viol(j): V.add(j)
        else: V.discard(j)
print(json.dumps({'local_search_steps': steps, 'violated_final': len(V)}))
