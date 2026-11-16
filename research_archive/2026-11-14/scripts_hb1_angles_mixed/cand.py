"""Candidate right-angle events over all private choices.
Slot s belongs to label s//M with choice s%M. For each vertex choice xi_v,
run the exact enumerator with every slot of an active label occupied."""
import sys, json, numpy as np
from angles import setup, enumerate_angles
h, S, M = map(int, sys.argv[1:4])
D = setup(h, S, M, 0)
q2 = D['q'] ** 2
act = D['act']
own = -np.ones(M * q2 + 1, np.int64)
s = np.arange(M * q2)
own[:M*q2] = np.where(act[s // M], s // M, -1)
D['owner'] = own
cnt = np.zeros(q2, np.int64)
ev = 0
geo = set()
for xv in range(M):
    D['slot'] = M * np.arange(q2, dtype=np.int64) + xv
    # enumerate_angles returns label triples; slots of f,g are implicit, so
    # recompute events: we need (v,f,g,xi_v,xi_f,xi_g). Patch: return slots.
    t = enumerate_angles(D, slots=True)
    ev_here = t
    for (v, p, f, g, sf, sg) in ev_here:
        geo.add((v, p, f, g))
    ev += len(ev_here)
    for (v, p, f, g, sf, sg) in ev_here:
        for z in {v, f, g}:
            cnt[z] += 1
print(json.dumps({'h': h, 'S': S, 'M': M, 'labels': int(act.sum()),
  'events': ev, 'geometric_triples': len(geo),
  'max_events_per_label': int(cnt.max()), 'mean_mu': float(3*ev/act.sum()/M**3),
  'max_mu': float(cnt.max()/M**3), 'lll_target': (1-2.718281828/M**3)/(3*2.718281828)}))
