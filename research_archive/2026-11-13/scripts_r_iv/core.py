from collections import defaultdict
from sympy import factorint
from f2sys import lams
def zcore(B, k):
    L = lams(B, k)
    rows = []
    for (_, _, q, p) in L:
        d = defaultdict(int)
        for r, e in factorint(p).items(): d[r] += e
        for r, e in factorint(q).items(): d[r] -= e
        rows.append({r: e for r, e in d.items() if e})
    col = defaultdict(set)
    for i, r in enumerate(rows):
        for c in r: col[c].add(i)
    alive = set(range(len(rows)))
    stack = [c for c in col if len(col[c]) == 1]
    while stack:
        c = stack.pop()
        if len(col[c]) != 1: continue
        (i,) = tuple(col[c]); alive.discard(i)
        for c2 in rows[i]:
            col[c2].discard(i)
            if len(col[c2]) == 1: stack.append(c2)
    core = sorted(alive)
    return L, rows, core
