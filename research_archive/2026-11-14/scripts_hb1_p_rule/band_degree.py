"""Candidate P-constraint degree of each label, binned by |T| = |j - i|.

Candidate family as in the choice-evidence note: ranks r<s, d=s-r,
|delta|<=M-1, X=S(Md+delta), cross-parity pair with X^2+Y^2=L^2 and
both completion rows in [1,h].  Sanity check only.
"""
import sys, math
import numpy as np


def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64)
    n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt
        n *= 2
    return xy


def pyth_rows(X, h):
    """odd Y>0 with X^2+Y^2=L^2, L<=h-1, via ab=(X/2)^2, opposite parity."""
    out = {}
    N = (X // 2) ** 2
    a = 1
    while a * a < N:
        if N % a == 0:
            b = N // a
            if (a + b) % 2 == 1 and a + b <= h - 1:
                out[b - a] = a + b
        a += 1
    return out


def main(h, M, S):
    q = h // 2
    xy = hilbert_array(q)
    i, j = xy[:, 0], xy[:, 1]
    odd, even = 2 * i + 1, 2 * j + 2
    n = q * q
    deg = np.zeros(n, dtype=np.int64)
    dmax = ((h - 1) // S + M - 1) // M
    for d in range(1, dmax + 1):
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            ys = pyth_rows(X, h)
            if not ys:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            for y, L in ys.items():
                hyp[y] = L
            hit = np.zeros(n - d, dtype=np.int64)
            for r1, r2 in ((odd[:-d], even[d:]), (even[:-d], odd[d:])):
                L = hyp[np.abs(r2 - r1)]
                s = r1 + r2
                hit += ((L > 0) & (s - L >= 2) & (s + L <= 2 * h)).astype(np.int64)
            deg[:-d] += hit
            deg[d:] += hit
    T = np.abs(j - i)
    print(f"h={h} M={M} S={S} labels={n} constraints={deg.sum()//2} mean={deg.mean():.4f} max={deg.max()}")
    edges = [0, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (T >= lo) & (T < hi)
        if m.sum() == 0:
            continue
        print(f"  |T| in [{lo},{hi}): labels={m.sum():8d} mean deg={deg[m].mean():.4f} max={deg[m].max()}")


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
