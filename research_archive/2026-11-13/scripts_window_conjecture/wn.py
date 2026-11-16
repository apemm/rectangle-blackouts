"""Independent computation of W_N(h) from the definitions.

N-window of width k for a balanced bipartition (A,B) of rows 1..h:
2k points of the h x k grid, exactly two per column, the k row pairs
distinct edges of K_{A,B}, and every tilted lattice rectangle of the
h x k grid has at most 2 corners in the set.

Usage: py wn.py h [index_lo index_hi]   (bipartition indices, for splitting)
"""
import sys, itertools, math, time

def tilted_rects(h, k):
    """All tilted rectangles of the h x k grid (columns 1..k, rows 1..h),
    generated from Z, Z+u, Z+v, Z+u+v with u.v = 0, u not axis-parallel."""
    rects = set()
    for u1 in range(-(k - 1), k):
        for u2 in range(-(h - 1), h):
            if u1 == 0 or u2 == 0:
                continue
            g = math.gcd(abs(u1), abs(u2))
            p1, p2 = -u2 // g, u1 // g  # primitive perpendicular
            for s in range(-(k + h), k + h + 1):
                if s == 0:
                    continue
                v1, v2 = s * p1, s * p2
                if abs(v1) >= k or abs(v2) >= h:
                    continue
                for x in range(1, k + 1):
                    for y in range(1, h + 1):
                        pts = [(x, y), (x + u1, y + u2), (x + v1, y + v2),
                               (x + u1 + v1, y + u2 + v2)]
                        if all(1 <= a <= k and 1 <= b <= h for a, b in pts):
                            rects.add(frozenset(pts))
    return rects

def bipartitions(h):
    """Distinct edge sets K_{A,B}, A of size floor(h/2)."""
    seen = {}
    for A in itertools.combinations(range(1, h + 1), h // 2):
        B = tuple(r for r in range(1, h + 1) if r not in A)
        E = frozenset(frozenset((a, b)) for a in A for b in B)
        key = E
        if key not in seen:
            seen[key] = A
    out = sorted(seen.items(), key=lambda t: t[1])
    return [(A, sorted(tuple(sorted(e)) for e in E)) for E, A in out]

def run(h, idx_lo=None, idx_hi=None, kmax=None, idx_list=None):
    q = h * h // 4
    if kmax is None:
        kmax = min(q, h + 1)
    R = tilted_rects(h, kmax)
    pid = lambda x, y: (x - 1) * h + (y - 1)
    # group by max column; record the unique corner in that column
    bycol = {x: [] for x in range(1, kmax + 1)}
    for r in R:
        mx = max(p[0] for p in r)
        inmax = [p for p in r if p[0] == mx]
        assert len(inmax) == 1, r  # unique corner in largest column
        oldmask = 0
        for p in r:
            if p[0] != mx:
                oldmask |= 1 << pid(*p)
        bycol[mx].append((oldmask, inmax[0][1]))
    bps = bipartitions(h)
    lo = 0 if idx_lo is None else idx_lo
    hi = len(bps) if idx_hi is None else idx_hi
    results = []
    for i in (idx_list if idx_list is not None else range(lo, hi)):
        A, E = bps[i]
        counts = [0] * (kmax + 1)
        best = [0, None]

        def dfs(x, P, used, seq):
            # seq has x-1 columns; P bitmask of chosen points
            w = x - 1
            counts[w] += 1
            if w > best[0]:
                best[0] = w
                best[1] = list(seq)
            if x > kmax:
                return
            forb = set()
            for om, row in bycol[x]:
                c = (P & om).bit_count()
                if c >= 3:
                    return  # fails for every choice of column x
                if c == 2:
                    forb.add(row)
            for j, (r1, r2) in enumerate(E):
                if used >> j & 1 or r1 in forb or r2 in forb:
                    continue
                seq.append((r1, r2))
                dfs(x + 1, P | (1 << pid(x, r1)) | (1 << pid(x, r2)),
                    used | (1 << j), seq)
                seq.pop()

        dfs(1, 0, 0, [])
        results.append((i, A, best[0], best[1], counts))
        print(f"h={h} idx={i} A={A} maxwidth={best[0]} "
              f"witness={''.join(f'{a}{b} ' for a, b in best[1]).strip()} "
              f"counts={counts}", flush=True)
    return results

if __name__ == "__main__":
    t = time.time()
    h = int(sys.argv[1])
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else None
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print(f"h={h}: {len(bipartitions(h))} bipartitions (edge sets)")
    run(h, lo, hi)
    print(f"time {time.time() - t:.1f}s")
