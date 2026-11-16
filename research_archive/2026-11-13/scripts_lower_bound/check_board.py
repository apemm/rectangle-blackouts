"""Independent definition-level checker for an all-double board given as a list of row pairs.
Reports: (1) whether the pairs are exactly the edges of K_{A,B} for a balanced bipartition;
(2) the number of 45-degree rectangles with >= 3 black corners; (3) the number of all tilted
rectangles with >= 3 black corners; (4) whether the board is valid (all rectangles, all slopes).
usage: py check_board.py h "23 46 26 35 15 34 12 14 56"
"""
import sys
from math import gcd


def rectangles(h, m):
    """all lattice rectangles of the h x m grid as frozensets of 4 corners (x,y), 1<=x<=m, 1<=y<=h"""
    out = set()
    # axis aligned
    for x1 in range(1, m + 1):
        for x2 in range(x1 + 1, m + 1):
            for y1 in range(1, h + 1):
                for y2 in range(y1 + 1, h + 1):
                    out.add(frozenset(((x1, y1), (x1, y2), (x2, y1), (x2, y2))))
    # tilted: leftmost corner (x,r), sides (a,-b),(c,d), a,b,c,d>=1, ac=bd
    tilted = []
    for b in range(1, h):
        for d in range(1, h - b):
            n = b * d
            for a in range(1, n + 1):
                if n % a:
                    continue
                c = n // a
                for r in range(1 + b, h - d + 1):
                    for x in range(1, m - a - c + 1):
                        R = frozenset(((x, r), (x + a, r - b), (x + c, r + d), (x + a + c, r - b + d)))
                        out.add(R)
                        tilted.append((R, a == b and c == d))
    return out, tilted


def main(h, cols):
    m = len(cols)
    black = set()
    for i, (r, s) in enumerate(cols):
        black.add((i + 1, r))
        black.add((i + 1, s))
    # bipartition check
    adj = {r: set() for r in range(1, h + 1)}
    for r, s in cols:
        adj[r].add(s)
        adj[s].add(r)
    A = {cols[0][0]} | set().union(*[adj[s] for s in adj[cols[0][0]]]) if cols else set()
    B = set(range(1, h + 1)) - A
    complete = sorted(set(tuple(sorted(p)) for p in cols)) == sorted((min(r, s), max(r, s)) for r in A for s in B) and len(set(map(lambda p: tuple(sorted(p)), cols))) == m
    print('rows A =', sorted(A), 'B =', sorted(B), '| pairs are exactly K_{A,B}, each once:', complete,
          '| balanced:', abs(len(A) - len(B)) <= 1, '| width', m, 'q_h', h * h // 4)
    allr, tilted = rectangles(h, m)
    n45 = sum(1 for R, is45 in tilted if is45 and len(R & black) >= 3)
    nt = sum(1 for R, is45 in tilted if len(R & black) >= 3)
    print('45-degree rectangles with >=3 black corners:', n45)
    print('tilted rectangles (all slopes) with >=3 black corners:', nt)
    pres = {}
    coll = 0
    for R in allr:
        key = frozenset(R - black)
        if key in pres:
            coll += 1
        else:
            pres[key] = R
    print('rectangles:', len(allr), '| presentation collisions:', coll, '| valid:', coll == 0)


if __name__ == '__main__':
    h = int(sys.argv[1])
    cols = [tuple(int(ch) for ch in tok) if '-' not in tok else tuple(int(t) for t in tok.split('-')) for tok in sys.argv[2].split()]
    main(h, cols)
