import sys
import numpy as np
from census import run
from validate import naive, board_random

def census_pres(viol, h):
    H1 = h + 1
    pt = lambda i: (i // H1, i % H1)
    S = set(); v1 = 0
    for v in viol:
        if v[0] in ('V2', 'V3'):
            S.add(frozenset([pt(v[2])]))
        elif v[0] in ('A2', 'T2'):
            w = v[2]
            S.add(frozenset([pt(w[0]), pt(w[1])]))
        elif v[0] == 'V1':
            v1 += 1
    return S, v1

ok = True
for seed in range(int(sys.argv[1])):
    h = [5, 6, 7][seed % 3]
    m = 14 + seed % 5
    kind = board_random(h, m, seed)
    bad = naive(kind, h)
    nb = set(bad.keys())
    viol, st = run(kind, h, m)
    cs, v1 = census_pres(viol, h)
    nb_nonempty = {p for p in nb if len(p) > 0}
    axis_only = []
    for p in nb_nonempty:
        allaxis = all(len({c[0] for c in key}) == 2 and len({c[1] for c in key}) == 2 for key in bad[p])
        if allaxis:
            axis_only.append(p)
    miss = nb_nonempty - cs - set(axis_only)
    extra = cs - nb_nonempty
    if miss or extra or axis_only:
        ok = False
    print(seed, h, m, 'naive', len(nb_nonempty), 'census', len(cs), 'V1', v1, 'empty-bad', frozenset() in nb,
          'miss', len(miss), 'extra', len(extra), 'axis-only', len(axis_only))
print('ALL OK' if ok else 'MISMATCH')
