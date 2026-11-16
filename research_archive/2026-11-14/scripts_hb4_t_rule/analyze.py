import sys, numpy as np
from collections import defaultdict
z = np.load(sys.argv[1])
r, s, dl, a, Y, role = (z[k] for k in ("r", "s", "delta", "a", "Y", "role"))
i, j = z["i"], z["j"]; M = int(z["M"]); S = int(z["S"])
T = j - i
Te, Tf = T[r], T[s]
q = M * (s - r) + dl
small = a <= S * S // 32
print("rows", len(r), "small-factor rows", int(small.sum()), "same-line rows", int((Te == Tf).sum()))
# line rigidity for small factors: per (a, line) set of q, over both endpoints
gaps = defaultdict(set)
for aa, t1, t2, qq in zip(a[small].tolist(), Te[small].tolist(), Tf[small].tolist(), q[small].tolist()):
    gaps[(aa, t1)].add(qq); gaps[(aa, t2)].add(qq)
print("small (a,T) keys", len(gaps), "max #gaps per key", max(map(len, gaps.values())))
# large factors: per (a, line) number of distinct gaps
gl = defaultdict(set)
for aa, t1, qq in zip(a[~small].tolist(), Te[~small].tolist(), q[~small].tolist()):
    gl[(aa, t1)].add(qq)
print("large (a,T) keys", len(gl), "max #gaps per key", max(map(len, gl.values())))
# number of distinct small factors per line
fl = defaultdict(set)
for aa, t1, t2 in zip(a[small].tolist(), Te[small].tolist(), Tf[small].tolist()):
    fl[t1].add(aa); fl[t2].add(aa)
print("max distinct small factors on one line", max(map(len, fl.values())))
# same-line rows by factor class
sl = Te == Tf
print("same-line small", int((sl & small).sum()), "same-line large", int((sl & ~small).sum()))
# per same-line: distinct rank gaps of delta=0 rows per line
g0 = defaultdict(set)
for t1, d, dd, aa in zip(Te[sl].tolist(), (s - r)[sl].tolist(), dl[sl].tolist(), a[sl].tolist()):
    g0[t1].add((d, dd, aa))
multi = {t: v for t, v in g0.items() if len({x[0] for x in v}) > 1}
print("lines with same-line rows", len(g0), "lines with >1 same-line rank gap", len(multi))
for t in list(multi)[:8]:
    print("  T", t, sorted(multi[t]))
