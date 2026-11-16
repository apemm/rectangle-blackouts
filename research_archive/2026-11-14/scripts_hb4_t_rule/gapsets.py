import sys, numpy as np
from collections import defaultdict, Counter
z = np.load(sys.argv[1])
r, s, dl, a = (z[k] for k in ("r", "s", "delta", "a"))
i, j = z["i"], z["j"]; M = int(z["M"])
T = j - i; q = M * (s - r) + dl
lab = defaultdict(set); line = defaultdict(set); linefac = defaultdict(set)
for rr, ss, qq, aa in zip(r.tolist(), s.tolist(), q.tolist(), a.tolist()):
    lab[rr].add(qq); lab[ss].add(qq)
    line[int(T[rr])].add(qq); line[int(T[ss])].add(qq)
    linefac[int(T[rr])].add(aa); linefac[int(T[ss])].add(aa)
print("labels with constraints", len(lab), "dist of |Q(e)|", sorted(Counter(map(len, lab.values())).items()))
print("lines with constraints", len(line), "dist of |Q(T)|", sorted(Counter(map(len, line.values())).items()))
print("dist of #factors per line", sorted(Counter(map(len, linefac.values())).items()))
# lines sorted by |T|: show gap sets for the multi-gap lines (first few)
mg = sorted((t for t, v in line.items() if len(v) > 1), key=abs)
print("multi-gap lines (first 15):", [(t, sorted(line[t])) for t in mg[:15]])
