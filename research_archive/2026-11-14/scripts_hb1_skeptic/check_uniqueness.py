"""Sanity check of the Hilbert recursion (2), locality (1), and the
fixed-factor uniqueness lemma (one candidate gap per label, factor, role, side),
plus the factor-one unique-gap-per-label statement, on the complete candidate
multigraph (all local choices).  Small sizes only."""
import math, sys
from collections import defaultdict

def hilbert(q):
    pts = [(0, 0)]
    s = 1
    while s < q:
        new = []
        new += [(y, x) for (x, y) in pts]
        new += [(x, y + s) for (x, y) in pts]
        new += [(x + s, y + s) for (x, y) in pts]
        new += [(2 * s - 1 - y, s - 1 - x) for (x, y) in pts]
        pts = new
        s *= 2
    return pts

def check_locality(q):
    H = hilbert(q)
    assert len(set(H)) == q * q
    for r in range(len(H)):
        for t in range(r + 1, len(H)):
            a, b = H[r], H[t]
            assert max((a[0]-b[0])**2, (a[1]-b[1])**2) < 16 * (t - r)
    return True

def isqrt_exact(n):
    r = math.isqrt(n)
    return r if r * r == n else None

def run(q, S, M, h):
    H = hilbert(q)
    A = (h + 1) // 2; K = h // 2
    labels = [(r, i, j) for r, (i, j) in enumerate(H) if i < A and j < K]
    rank = {(i, j): r for r, i, j in labels}
    pos = {r: (i, j) for r, i, j in labels}
    rs = sorted(pos)
    # candidate constraints: (focal, partner, role, side, q, factor)
    by_key = defaultdict(set)      # (focal, factor, role, side) -> set of q
    f1_label = defaultdict(set)    # focal -> set of q for factor one
    ncand = 0
    W = h // S + 2
    for e in rs:
        ie, je = pos[e]
        for f in range(e - W, e + W + 1):
            if f == e or f not in pos: continue
            d = abs(f - e)
            if M * (d - 1) + 1 > h: continue
            fi, fj = pos[f]
            side = 1 if f > e else -1
            for role in (0, 1):
                # role 0: odd of e with even of f ; role 1: even of e with odd of f
                if role == 0:
                    y = (2 * fj + 2) - (2 * ie + 1)
                else:
                    y = (2 * je + 2) - (2 * fi + 1)
                Y = abs(y)
                for dx in range(-(M - 1), M):
                    qq = M * d + dx
                    if qq <= 0: continue
                    X = S * qq
                    if X >= h: continue   # vertical completion needs L <= h-1 > X
                    L = isqrt_exact(X * X + Y * Y)
                    if L is None: continue
                    a = (L - Y) // 2
                    ncand += 1
                    by_key[(e, a, role, side)].add(qq)
                    if a == 1:
                        f1_label[e].add(qq)
    bad = [k for k, v in by_key.items() if len(v) > 1]
    bad1 = [k for k, v in f1_label.items() if len(v) > 1]
    return ncand, len(by_key), len(bad), len(bad1)

if __name__ == "__main__":
    for q in (4, 8, 16):
        check_locality(q)
    print("locality ok through q=16")
    for (q, S, M, h) in [(32, 8, 3, 64), (32, 8, 5, 64), (64, 8, 3, 128), (64, 4, 4, 128)]:
        print((q, S, M, h), run(q, S, M, h))
