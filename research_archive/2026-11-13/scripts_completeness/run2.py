import sys
sys.path.insert(0, '.')
from foee_mod64 import run
from collections import defaultdict, Counter
tot = defaultdict(Counter); ns = 0
for seed, iota, M0, T0 in [(5,3,1,5),(6,8,9,35),(7,13,2,11),(8,0,5,-9),(9,22,14,1)]:
    r, n = run(seed, iota, M0, T0, nclass=4, kmax=5, qrange=2, rrange=1)
    ns += n
    for k, v in r.items(): tot[k].update(v)
print('solutions', ns)
for k in sorted(tot): print(k, dict(sorted(tot[k].items())))
