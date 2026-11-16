"""W_O(h) over all balanced bipartitions (one per reflection orbit).
usage: py osraf_all.py h Kmax per_bip_seconds
"""
import sys, time, itertools
sys.setrecursionlimit(10000)
from osraf import run
h = int(sys.argv[1]); Kmax = int(sys.argv[2]); tl = float(sys.argv[3])
seen = set(); res = {}
T0 = time.time()
for A in itertools.combinations(range(1, h + 1), h // 2):
    refl = tuple(sorted(h + 1 - a for a in A))
    if refl in seen: continue
    seen.add(tuple(A))
    b, st, s = run(h, Kmax, list(A), tl)
    res[A] = (b, st)
    if time.time() - T0 > 55: print('global time'); break
mx = max(v[0] for v in res.values())
print(f"h={h} orbits={len(res)} max W_O={mx}; incomplete={[A for A,v in res.items() if v[1]!='complete']}")
print('attaining:', [A for A, v in res.items() if v[0] == mx][:12])
from collections import Counter
print('distribution:', sorted(Counter(v[0] for v in res.values()).items()))
