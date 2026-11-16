"""Definition-level recheck of every window listed by classify.py: distinct K_{A,B} edges,
two points per column, and no tilted rectangle of the h x K grid with >= 3 corners in P,
by enumerating all 4-corner tilted rectangles (corners Z, Z+u, Z+v, Z+u+v, u.v = 0, u not
axis-parallel) and counting corners in P.  Usage: py verify_list.py h file..."""
import sys, ast
from math import gcd
h = int(sys.argv[1])
def rects(h, k):
    out = set()
    for u1 in range(-(k-1), k):
        for u2 in range(-(h-1), h):
            if u1 == 0 or u2 == 0: continue
            g = gcd(abs(u1), abs(u2)); p1, p2 = -u2 // g, u1 // g
            for s in range(1, k + h):
                v1, v2 = s * p1, s * p2
                if abs(v1) >= k or abs(v2) >= h: break
                for x in range(1, k + 1):
                    for y in range(1, h + 1):
                        c = [(x, y), (x+u1, y+u2), (x+v1, y+v2), (x+u1+v1, y+u2+v2)]
                        if all(1 <= a <= k and 1 <= b <= h for a, b in c):
                            out.add(frozenset(c))
    return out
R = rects(h, h)
n = bad = 0
for f in sys.argv[2:]:
    for l in open(f):
        if not l.startswith('A'): continue
        A = ast.literal_eval(l[2:l.index(')') + 1])
        cols = [tuple(map(int, c.split('-'))) for c in l[l.index(')') + 1:].split('|')[0].split()]
        assert len(cols) == h and len(set(cols)) == h
        assert all((a in A) != (b in A) for a, b in cols)
        P = {(x + 1, r) for x, c in enumerate(cols) for r in c}
        assert len(P) == 2 * h
        n += 1
        if any(len(r & P) >= 3 for r in R): bad += 1
print('rectangles', len(R), 'windows checked', n, 'bad', bad)
