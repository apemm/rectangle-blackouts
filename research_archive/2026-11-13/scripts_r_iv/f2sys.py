# Is there a completely multiplicative chi: odd primes -> F_2 with chi(p_l) != chi(q_l) for all lambda with be <= B?
# Rows: v(rho_l) mod 2. Solve A x = 1 over F_2 after peeling rows with a private column.
import sys
from math import gcd
from sympy import factorint

def lams(B, k):
    out = []
    for be in range(3, B + 1, 2):
        for al in range(1, be, 2):
            if gcd(al, be) != 1: continue
            d = be - al; v = 0
            while d % 2 == 0: d //= 2; v += 1
            if 2 + v < k: continue
            F = 4 * (al - 2 * be) ** 2 + be * be
            g = gcd(F, be - al)
            q = al * F // g; p = (al * F + 4 * (be - al) * be * be) // g
            assert gcd(p, q) == 1
            out.append((al, be, q, p))
    return out

def row(q, p):
    s = set()
    for r, e in factorint(p).items():
        if e % 2: s ^= {r}
    for r, e in factorint(q).items():
        if e % 2: s ^= {r}
    return frozenset(s)

if __name__ == '__main__':
    B = int(sys.argv[1]); k = int(sys.argv[2])
    L = lams(B, k)
    rows = [row(q, p) for (_, _, q, p) in L]
    print('lambdas', len(L), 'empty rows', sum(1 for r in rows if not r))
    alive = set(range(len(rows)))
    from collections import defaultdict
    col = defaultdict(set)
    for i, r in enumerate(rows):
        for c in r: col[c].add(i)
    stack = [c for c in col if len(col[c]) == 1]
    while stack:
        c = stack.pop()
        if len(col[c]) != 1: continue
        (i,) = tuple(col[c])
        alive.discard(i)
        for c2 in rows[i]:
            col[c2].discard(i)
            if len(col[c2]) == 1: stack.append(c2)
    core = sorted(alive)
    print('core rows', len(core))
    # gaussian elimination over F_2 using python ints as bitsets; augmented bit for target 1
    cols = sorted({c for i in core for c in rows[i]})
    idx = {c: j for j, c in enumerate(cols)}
    n = len(cols)
    vecs = []
    for i in core:
        v = 1 << n  # target bit
        for c in rows[i]: v |= 1 << idx[c]
        vecs.append(v)
    piv = {}
    bad = 0
    for v in vecs:
        while True:
            low = v & ((1 << n) - 1)
            if low == 0:
                if v >> n: bad += 1
                break
            b = low.bit_length() - 1
            if b in piv: v ^= piv[b]
            else:
                piv[b] = v; break
    print('core cols', n, 'rank', len(piv), 'inconsistent (odd square relations)', bad)
