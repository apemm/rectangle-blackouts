"""Binding-gap rule with value set {0,1}: xi_e = sum over binding gaps q of e with M|q
of floor(M r_e / q) mod 2, reduced mod 2. Reports violations, mixed binding components."""
import sys, numpy as np
from collections import defaultdict
z = np.load(sys.argv[1])
r, s, dl = z["r"], z["s"], z["delta"]; M = int(z["M"]); n = len(z["i"])
q = M * (s - r) + dl
r, s, dl, q = np.unique(np.stack([r, s, dl, q]), axis=1)
res = q % M
if M == 2:
    bind = np.ones(len(r), dtype=bool)
else:
    t = int(sys.argv[2]); bind = (res == 0) | (dl == t) | (dl == -t)
Qb = defaultdict(set)
for rr, ss, qq in zip(r[bind].tolist(), s[bind].tolist(), q[bind].tolist()):
    Qb[rr].add(qq); Qb[ss].add(qq)
xi = np.zeros(n, dtype=np.int64)
for x, gs in Qb.items():
    xi[x] = t * (sum((x // (g // M)) % 2 for g in gs if g % M == 0) % 2)
bad = (xi[s] - xi[r]) == dl
assert not (bad & ~bind).any()
mixed_e = np.array([len(Qb[a]) > 1 or len(Qb[b]) > 1 for a, b in zip(r.tolist(), s.tolist())])
parent = np.arange(n)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
for rr, ss in zip(r[bind].tolist(), s[bind].tolist()):
    a1, b1 = find(rr), find(ss)
    if a1 != b1: parent[a1] = b1
cg = defaultdict(set)
for rr, qq in zip(r[bind].tolist(), q[bind].tolist()):
    cg[find(rr)].add(qq)
mixc = sum(len(v) > 1 for v in cg.values())
print(f"M={M}: constraints {len(r)}, binding {int(bind.sum())}, violated {int(bad.sum())} "
      f"(all on mixed-gap edges: {bool((bad <= mixed_e).all())}), binding components {len(cg)}, mixed {mixc}, "
      f"labels with >=2 binding gaps {sum(len(v) > 1 for v in Qb.values())}")
