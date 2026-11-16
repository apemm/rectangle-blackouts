# Validate census.py against a naive all-rectangle presentation hash on small full boards
# (every parity edge present as a double on the board), and on known examples.
import random, sys
import numpy as np
from census import run

def naive(kind, h):
    m = kind.shape[0]
    pts = [(x, y) for x in range(m) for y in range(1, h + 1)]
    black = {(x, y) for (x, y) in pts if kind[x, y]}
    seen = set(); pres = {}
    for i, P in enumerate(pts):
        for Q in pts[i + 1:]:
            sx, sy = P[0] + Q[0], P[1] + Q[1]
            D2 = (Q[0] - P[0]) ** 2 + (Q[1] - P[1]) ** 2
            for X in range(-m, m + 1):
                Y2 = D2 - X * X
                if Y2 < 0:
                    continue
                Y = int(round(Y2 ** 0.5))
                if Y * Y != Y2:
                    continue
                for YY in {Y, -Y}:
                    if (sx + X) % 2 or (sy + YY) % 2:
                        continue
                    C1 = ((sx + X) // 2, (sy + YY) // 2); C2 = ((sx - X) // 2, (sy - YY) // 2)
                    if C1 in (P, Q) or C2 in (P, Q):
                        continue
                    if not (0 <= C1[0] < m and 0 <= C2[0] < m and 1 <= C1[1] <= h and 1 <= C2[1] <= h):
                        continue
                    key = frozenset([P, Q, C1, C2])
                    if key in seen:
                        continue
                    seen.add(key)
                    pr = frozenset(c for c in key if c not in black)
                    pres.setdefault(pr, []).append(key)
    bad = {k: v for k, v in pres.items() if len(v) > 1}
    return bad

def board_random(h, m, seed):
    rng = random.Random(seed)
    kind = np.zeros((m, h + 1), np.int8)
    odd = [y for y in range(1, h + 1) if y % 2]; even = [y for y in range(1, h + 1) if y % 2 == 0]
    edges = [(a, b) for a in odd for b in even]
    cols = rng.sample(range(m), len(edges))
    for c, (a, b) in zip(cols, edges):
        kind[c, a] = 4; kind[c, b] = 5
    for c in range(m):
        if c not in cols:
            kind[c, rng.randint(1, h)] = 1
    return kind

if __name__ == '__main__':
    tot = 0
    for seed in range(int(sys.argv[1]) if len(sys.argv) > 1 else 6):
        h = 5 if seed % 2 else 6
        m = 16
        kind = board_random(h, m, seed)
        bad = naive(kind, h)
        nbad_naive = sum(1 for v in bad.values())
        viol, st = run(kind, h, m)
        # naive "bad presentations"; census violations; compare as booleans and counts of
        # presentations with a tilted member
        tilted_bad = 0
        for pr, recs in bad.items():
            tilted = False
            for key in recs:
                xs = sorted({c[0] for c in key}); ys = sorted({c[1] for c in key})
                if not (len(xs) == 2 and len(ys) == 2):
                    tilted = True
            if tilted:
                tilted_bad += 1
        print(seed, 'naive bad presentations', nbad_naive, 'with tilted member', tilted_bad,
              'census violations', len(viol), 'kinds', sorted({v[0] for v in viol}))
