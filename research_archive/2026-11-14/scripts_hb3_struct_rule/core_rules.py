"""Violation rates of explicit rules on the height-independent diagonal-block systems G_B^o
(S=32, M=3).  Builder re-implemented from the description in hilbert_p_height_independent_cores.md
(owner outside the block, in-block completions)."""
import sys
import math
from collections import defaultdict
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


def legs_by_X(Ymax, S):
    out = defaultdict(dict)
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        for u in range(1, Y, 2):
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                if X % S == 0:
                    out[X][Y] = (w + u) // 2
    return out


def build(B, S, M, orient):
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1]
    odd, even = 2 * xy[:, 0] + 1, 2 * xy[:, 1] + 2
    n = B * B
    legs = legs_by_X(2 * B + 1, S)
    chunks = []
    for X, ys in legs.items():
        q = X // S
        for d in {q // M, -(-q // M)}:
            delta = q - M * d
            if d < 1 or d >= n or abs(delta) > M - 1:
                continue
            look = np.zeros(4 * B + 4, dtype=np.int64)
            for Y, L in ys.items():
                look[Y] = L
            for a_rows, b_rows in ((odd[d:], even[:-d]), (odd[:-d], even[d:])):
                L = look[np.abs(b_rows - a_rows)]
                s = a_rows + b_rows
                lo, hi = (s - L) // 2, (s + L) // 2
                oddr = np.where(lo % 2 == 1, lo, hi)
                evr = np.where(lo % 2 == 1, hi, lo)
                oi, oj = (oddr - 1) // 2, (evr - 2) // 2
                inside = (oi >= 0) & (oi < B) & (oj >= 0) & (oj < B)
                r = np.nonzero((L > 0) & ~inside)[0]
                if len(r):
                    chunks.append((r * n + (r + d)) * (2 * M) + (delta + M))
    code = np.unique(np.concatenate(chunks))
    delta = code % (2 * M) - M
    pair = code // (2 * M)
    return n, np.stack([pair // n, pair % n, delta], axis=1), xy


def popc(r):
    s = np.zeros_like(r); t = r.copy()
    while t.any():
        s += t & 1; t >>= 1
    return s


def dsum(r, b):
    s = np.zeros_like(r); t = r.copy()
    while t.any():
        s += t % b; t //= b
    return s


if __name__ == "__main__":
    B, S, M = int(sys.argv[1]), 32, 3
    for orient in ("id", "swap"):
        n, E, xy = build(B, S, M, orient)
        i, j = xy[:, 0], xy[:, 1]
        r = np.arange(n, dtype=np.int64)
        T = j - i
        q1 = np.array([math.isqrt(max(1, 8 * (abs(int(t)) + 1))) // S for t in T])
        w = np.maximum(1, q1 // M)
        g = r ^ (r >> 1)
        rules = {
            "popcount(r) mod 3": popc(r) % M,
            "sum_k floor(r/2^k) mod 3": (2 * r - popc(r)) % M,
            "base-4 digit sum mod 3": dsum(r, 4) % M,
            "r mod 3": r % M,
            "base-3 digit sum mod 3": dsum(r, 3) % M,
            "Gray(r) mod 3": g % M,
            "(T + popcount r) mod 3": (T + popc(r)) % M,
            "floor(r/w(T)) mod 3": (r // w) % M,
            "random": np.random.default_rng(7).integers(0, M, n),
        }
        print(f"B={B} {orient}: constraints={len(E)}, delta=0 share={np.mean(E[:,2]==0):.3f}")
        for name, xi in rules.items():
            bad = int(np.sum(xi[E[:, 1]] - xi[E[:, 0]] == E[:, 2]))
            print(f"   {name:28s} violated {bad:6d} ({bad/len(E):.3f})")
