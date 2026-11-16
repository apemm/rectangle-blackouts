"""Largest N-window width when only a family of tilted rectangles is forbidden.

Window of width K: columns 1..K, two points per column, row pairs distinct
edges of K_{A,B}; forbidden: a tilted rectangle of the h x K grid (in the
family) with >= 3 corners in P.  Family is given by a predicate on the
primitive side direction e = (c,d), c,d >= 1 (the side lying in the open
first quadrant; the other side is (-d,c)).

usage: py famwin.py h fam Kmax [A as comma list]   (fam: 45, r2, r3, all, 45+12)
"""
import sys, time
from math import gcd

def fam_ok(fam, c, d):
    if fam == '45':
        return (c, d) == (1, 1)
    if fam == '45+12':
        return (c, d) in ((1, 1), (1, 2), (2, 1))
    if fam.startswith('r'):
        r = int(fam[1:])
        return max(c, d) <= r
    if fam == 'all':
        return True
    raise ValueError(fam)

def rects(h, K, fam):
    out = []
    for c in range(1, max(h, K) + 1):
        for d in range(1, max(h, K) + 1):
            if gcd(c, d) != 1 or not fam_ok(fam, c, d):
                continue
            # Z=(x,y); Z+s(c,d); Z+t(-d,c); Z+s(c,d)+t(-d,c)
            for s in range(1, K + 1):
                if s * c > K - 1 or s * d > h - 1:
                    break
                for t in range(1, K + 1):
                    if t * d > K - 1 or t * c > h - 1:
                        break
                    w = s * c + t * d          # width extent
                    hh = s * d + t * c         # height extent
                    if w > K - 1 or hh > h - 1:
                        continue
                    for x in range(1 + t * d, K + 1 - s * c):
                        for y in range(1, h + 1 - hh):
                            Z = (x, y)
                            A = (x + s * c, y + s * d)
                            B = (x - t * d, y + t * c)
                            C = (A[0] - t * d, A[1] + t * c)
                            out.append((Z, A, B, C))
    return out

def search(h, K, fam, Apart, tlimit=55.0):
    Bpart = [y for y in range(1, h + 1) if y not in Apart]
    edges = [(a, b) for a in Apart for b in Bpart]
    R = rects(h, K, fam)
    cell = {}
    for i, r in enumerate(R):
        for p in r:
            cell.setdefault(p, []).append(i)
    cnt = [0] * len(R)
    used = [False] * len(edges)
    t0 = time.time()
    sol = []
    nodes = [0]

    def place(p):
        ok = True
        for i in cell.get(p, ()):
            cnt[i] += 1
            if cnt[i] >= 3:
                ok = False
        return ok

    def unplace(p):
        for i in cell.get(p, ()):
            cnt[i] -= 1

    def dfs(x):
        nodes[0] += 1
        if time.time() - t0 > tlimit:
            raise TimeoutError
        if x > K:
            return True
        for j, (a, b) in enumerate(edges):
            if used[j]:
                continue
            p1, p2 = (x, a), (x, b)
            o1 = place(p1)
            o2 = place(p2)
            if o1 and o2:
                used[j] = True
                sol.append((a, b))
                if dfs(x + 1):
                    return True
                sol.pop()
                used[j] = False
            unplace(p2)
            unplace(p1)
        return False

    found = dfs(1)
    return found, list(sol), nodes[0], len(R)

if __name__ == '__main__':
    h = int(sys.argv[1]); fam = sys.argv[2]; Kmax = int(sys.argv[3])
    if len(sys.argv) > 4:
        Apart = [int(v) for v in sys.argv[4].split(',')]
    else:
        Apart = list(range(1, h + 1, 2))
    q = len(Apart) * (h - len(Apart))
    T0 = time.time()
    for K in range(h, min(Kmax, q) + 1):
        try:
            f, s, n, nr = search(h, K, fam, Apart, tlimit=max(1.0, 55.0 - (time.time() - T0)))
        except TimeoutError:
            print(f"h={h} fam={fam} K={K}: TIMEOUT"); break
        print(f"h={h} fam={fam} K={K}: {'YES' if f else 'no'} nodes={n} rects={nr} {s if f else ''}", flush=True)
        if not f:
            break
        if time.time() - T0 > 55:
            print('time'); break
