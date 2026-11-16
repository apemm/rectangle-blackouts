import sys, math, numpy as np
from collections import defaultdict
z = np.load(sys.argv[1])
r, s, dl, a = (z[k] for k in ("r", "s", "delta", "a"))
i, j = z["i"], z["j"]; M = int(z["M"]); S = int(z["S"])
T = j - i; q = M * (s - r) + dl
trip = np.unique(np.stack([r, s, dl, q]), axis=1)  # distinct (r,s,delta)
r, s, dl, q = trip
n = len(i)
# per-label gap sets
Q = defaultdict(set)
for rr, ss, qq in zip(r.tolist(), s.tolist(), q.tolist()):
    Q[rr].add(qq); Q[ss].add(qq)
mixed = np.array([len(Q[x]) > 1 for x in r.tolist()]) | np.array([len(Q[x]) > 1 for x in s.tolist()])
# binding-residue gap sets for V={0,1}
def report(name, xi):
    bad = (xi[s] - xi[r]) == dl
    print(f"{name:28s} violated {int(bad.sum()):7d} / {len(r)}  ({bad.mean():.3%}); on mixed-gap edges {int((bad & mixed).sum())}, single-gap {int((bad & ~mixed).sum())}")
rng = np.random.default_rng(1)
report("random {0..M-1}", rng.integers(0, M, n))
report("random {0,1}", rng.integers(0, 2, n))
Ta = np.abs(T).astype(float)
qh = np.rint(np.sqrt(8 * (Ta + 1)) / S).astype(np.int64)
ranks = np.arange(n)
xi = np.where(qh > 0, (M * ranks // np.maximum(qh, 1)) % 2, 0)
report("factor-one T-scale parity", xi)
# local gap-set rule (reads Q(e))
xi2 = np.zeros(n, dtype=np.int64); xi3 = np.zeros(n, dtype=np.int64)
for x, gs in Q.items():
    tot = 0; tot3 = 0
    for g in gs:
        if g % M == 0:
            tot += (x // (g // M)) % 2
        # residues +-1 bind for V={0,1}; nothing to add (xi const is safe)
    xi2[x] = tot % 2
    xi3[x] = sum((x // (g // M)) % 2 for g in gs if g % M == 0) % M
report("gap-set parity (V={0,1})", xi2)
report("gap-set sum mod M", xi3)
# how many binding-residue edges (V={0,1}) exist
bind = (q % M == 0) | (q % M == 1) & (dl == 1) | (q % M == M - 1) & (dl == -1)
print("edges binding for V={0,1}:", int(bind.sum()))
# components of binding graph with a single gap?
parent = list(range(n))
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
print("binding components", len(cg), "with >1 gap", sum(len(v) > 1 for v in cg.values()))
