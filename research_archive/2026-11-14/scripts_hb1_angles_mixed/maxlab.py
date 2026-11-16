import sys, json, math, numpy as np
from collections import Counter, defaultdict
from angles import setup, enumerate_angles
h, S, M, seed = map(int, sys.argv[1:5])
D = setup(h, S, M, seed)
t = enumerate_angles(D, slots=True)
inc = defaultdict(list)
for ev in t:
    v, p, f, g, sf, sg = ev
    inc[v].append(('V', ev)); inc[f].append(('F', ev)); inc[g].append(('G', ev))
dist = Counter(len(x) for x in inc.values())
top = sorted(inc, key=lambda z: -len(inc[z]))[:3]
out = {'hist_incidence': sorted(dist.items())}
for z in top:
    roles = Counter(r for r, _ in inc[z])
    evs = [(r, int(e[0]), int(e[2]), int(e[3])) for r, e in inc[z]]
    out[str(z)] = {'coords': D['xy'][z].tolist(), 'roles': dict(roles), 'events': evs[:8]}
print(json.dumps(out))
