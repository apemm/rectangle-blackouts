"""Compare the enumeration in check_127_three_black.py with a direct one on 300 small random boards."""
import itertools, random

import check_127_three_black as chk


def direct(cols, h, m):
    black = {(x, y) for x, c in enumerate(cols) for y in c}
    pts = [(x, y) for x in range(m) for y in range(1, h+1)]
    out = set()
    for p, q in itertools.combinations(pts, 2):
        n = (p[0]-q[0])**2 + (p[1]-q[1])**2
        for r in pts:
            s = (p[0]+q[0]-r[0], p[1]+q[1]-r[1])
            if not (0 <= s[0] < m and 1 <= s[1] <= h) or r <= p or s <= r or r == q:
                continue
            if (r[0]-s[0])**2 + (r[1]-s[1])**2 != n:
                continue
            rect = frozenset((p, q, r, s))
            if len({c[0] for c in rect}) == 2 and len({c[1] for c in rect}) == 2:
                continue
            if len(rect & black) >= 3:
                out.add((rect, len(rect & black)))
    return out


random.seed(7)
total = 0
for trial in range(300):
    h = random.randint(4, 8)
    m = random.randint(4, 14)
    cols = [tuple(sorted(random.sample(range(1, h+1), random.choice((1, 2, 2, 3))))) for _ in range(m)]
    rows = [0]*(h+2)
    for x, c in enumerate(cols):
        for y in c:
            rows[y] |= 1 << x
    mine = {(frozenset(cs), sum(bl)) for cs, bl in chk.tilted_heavy(rows, h, m)}
    assert mine == direct(cols, h, m), trial
    total += len(mine)
print("300 boards agree,", total, "tilted rectangles with at least 3 black corners")
