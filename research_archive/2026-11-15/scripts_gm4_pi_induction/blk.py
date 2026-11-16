"""Block system builder (cand / gen) for the main-diagonal block G_B^o, plus
segment bookkeeping.  Hilbert recursion and leg enumeration follow the archive
definitions (H_2n: Q1 transposed, Q2 translated up, Q3 translated diagonally,
Q4 reflected); the kernel enumerates cross pairs (odd row of one label, even
row of the other) at both slots d = floor(q/M), ceil(q/M).
"""
import numpy as np
import numba as nb


def hilbert_array(q):
    xy = np.zeros((1, 2), dtype=np.int64); n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=np.int64)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + (0, n)
        nxt[2 * b:3 * b] = xy + (n, n)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt; n *= 2
    return xy


def legs(Ymax, S):
    out = {}
    for Y in range(1, Ymax + 1, 2):
        Y2 = Y * Y
        u = 1
        while u < Y:
            if Y2 % u == 0:
                w = Y2 // u
                X = (w - u) // 2
                if X > 0 and X % S == 0:
                    out.setdefault(X // S, []).append((Y, (w + u) // 2))
            u += 2
    return out


@nb.njit(cache=True)
def kernel(odd, even, B, M, owner_test, qs, offs, Ys, Ls, out):
    n = odd.shape[0]
    look = np.zeros(4 * B + 8, dtype=np.int64)
    cnt = 0
    for t in range(qs.shape[0]):
        q = qs[t]
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = Ls[k]
        d1 = q // M
        d2 = (q + M - 1) // M
        for dd in range(2):
            d = d1 if dd == 0 else d2
            if dd == 1 and d2 == d1:
                continue
            delta = q - M * d
            if d < 1 or d >= n or delta > M - 1 or delta < -(M - 1):
                continue
            for r in range(n - d):
                for role in range(2):
                    if role == 0:
                        a = odd[r]; b = even[r + d]
                    else:
                        a = odd[r + d]; b = even[r]
                    y = b - a
                    if y < 0:
                        y = -y
                    L = look[y]
                    if L == 0:
                        continue
                    if owner_test:
                        s = a + b
                        lo = (s - L) // 2
                        hi = (s + L) // 2
                        if lo % 2 == 1:
                            oo = lo; ee = hi
                        else:
                            oo = hi; ee = lo
                        oi = (oo - 1) // 2
                        oj = (ee - 2) // 2
                        if oi >= 0 and oi < B and oj >= 0 and oj < B:
                            continue
                    if cnt < out.shape[0]:
                        out[cnt, 0] = r
                        out[cnt, 1] = r + d
                        out[cnt, 2] = delta
                        out[cnt, 3] = q
                    cnt += 1
        for k in range(offs[t], offs[t + 1]):
            look[Ys[k]] = 0
    return cnt


def build(B, S, M, orient, version, cap=9_000_000):
    """returns xy (cells per rank, after orientation) and E: distinct (r, u, delta, q)"""
    xy = hilbert_array(B)
    if orient == "swap":
        xy = xy[:, ::-1].copy()
    odd = np.ascontiguousarray(2 * xy[:, 0] + 1).astype(np.int64)
    even = np.ascontiguousarray(2 * xy[:, 1] + 2).astype(np.int64)
    P = legs(2 * B - 1, S)
    qs, offs, Ys, Ls = [], [0], [], []
    for q in sorted(P):
        qs.append(q)
        for Y, L in P[q]:
            Ys.append(Y); Ls.append(L)
        offs.append(len(Ys))
    out = np.zeros((cap, 4), dtype=np.int64)
    cnt = kernel(odd, even, B, M, version == "gen", np.array(qs, dtype=np.int64),
                 np.array(offs, dtype=np.int64), np.array(Ys, dtype=np.int64),
                 np.array(Ls, dtype=np.int64), out)
    assert cnt <= cap
    E = np.unique(out[:cnt], axis=0)
    return xy, E


def segments(xy):
    """segment index of each rank: number of main-diagonal cells of rank <= r, minus 1"""
    diag = xy[:, 0] == xy[:, 1]
    return np.cumsum(diag) - 1


def weighted_core(n, E, k, mod=None):
    """weighted k-core on distinct triples; if mod is given, count distinct
    certified classes (neighbour, delta mod M) instead (Lemma CC)."""
    if mod is not None:
        key = np.stack([E[:, 0], E[:, 1], E[:, 2] % mod], axis=1)
        _, first = np.unique(key, axis=0, return_index=True)
        E = E[np.sort(first)]
    alive = np.ones(len(E), dtype=bool)
    while True:
        deg = np.bincount(E[alive, 0], minlength=n) + np.bincount(E[alive, 1], minlength=n)
        bad = deg < k
        kill = alive & (bad[E[:, 0]] | bad[E[:, 1]])
        if not kill.any():
            return E[alive]
        alive &= ~kill
