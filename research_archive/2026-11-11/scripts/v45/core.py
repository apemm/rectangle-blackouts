from itertools import combinations
_cache = {}
def rects(h, m):
    """All allowed rectangles as frozensets of (x,y) points."""
    k = (h, m)
    if k in _cache: return _cache[k]
    R = set()
    for x1, x2 in combinations(range(1, m+1), 2):
        for y1, y2 in combinations(range(1, h+1), 2):
            R.add(frozenset([(x1,y1),(x1,y2),(x2,y1),(x2,y2)]))
    n_axis = len(R)
    for x in range(1, m+1):
        for y in range(1, h+1):
            for s in range(-(h-1), h):
                if s == 0: continue
                for t in range(-(h-1), h):
                    if t == 0: continue
                    pts = [(x,y),(x+s,y+s),(x+t,y-t),(x+s+t,y+s-t)]
                    if all(1 <= px <= m and 1 <= py <= h for px, py in pts):
                        R.add(frozenset(pts))
    _cache[k] = list(R)
    return _cache[k]

def is_valid(h, m, S):
    S = set(S)
    seen = {}
    for R in rects(h, m):
        key = frozenset(p for p in R if p not in S)
        if key in seen:
            return False, (tuple(sorted(seen[key])), tuple(sorted(R)))
        seen[key] = R
    return True, None
