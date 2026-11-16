"""Opposite-parity P candidate graph of the full-grid Hilbert placement.

x_e = S(M r_e + xi_e), 0 <= xi_e < M.  A witness (r, s, delta, a) means:
r < s, and the slot gap q = M(s-r)+delta gives X = S q with an integral
cross-parity diagonal of length L <= h-1, smaller half-factor a=(L-Y)/2,
and in-strip vertical completion rows.  Same conventions as
hilbert_finite_choice_search.py (archive 2026-11-14); integer tests only.

Speed-up: instead of scanning all ranks for each (d, delta), only the
earlier labels r whose diagonal index T_r = j_r - i_r lies in the band
|2 T_r + 1 -/+ Y| <= 2 zmax(d) are generated, where zmax(d) is the
largest z with z^2 < 16 d (Hilbert locality).  Completeness of this band
is proved in the write-up.
"""
import math
import sys
import time
import numpy as np


def d2xy(q, t):
    """Standard low-bit rotation algorithm (same curve as the archive)."""
    t = t.astype(np.int64).copy()
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    s = 1
    while s < q:
        rx = (t // 2) & 1
        ry = (t ^ rx) & 1
        reflect = (ry == 0) & (rx == 1)
        x[reflect] = s - 1 - x[reflect]
        y[reflect] = s - 1 - y[reflect]
        swap = ry == 0
        saved = x[swap].copy()
        x[swap] = y[swap]
        y[swap] = saved
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


def xy2d(q, x, y):
    x = x.astype(np.int64).copy()
    y = y.astype(np.int64).copy()
    d = np.zeros_like(x)
    s = q // 2
    while s > 0:
        rx = ((x & s) > 0).astype(np.int64)
        ry = ((y & s) > 0).astype(np.int64)
        d += s * s * ((3 * rx) ^ ry)
        reflect = (ry == 0) & (rx == 1)
        x[reflect] = q - 1 - x[reflect]
        y[reflect] = q - 1 - y[reflect]
        swap = ry == 0
        saved = x[swap].copy()
        x[swap] = y[swap]
        y[swap] = saved
        s //= 2
    return d


def pythagorean_rows(X, h):
    """Verbatim logic of hilbert_two_choice_rivals.pythagorean_rows, but
    returning (Y>0, L, a) with a the smaller half-factor."""
    value = (X // 2) ** 2
    out = []
    for a in range(1, math.isqrt(value) + 1):
        if value % a:
            continue
        b = value // a
        if a + b < h and (b - a) % 2:
            out.append((b - a, a + b, a))
    return out


def diagonal_cells(A, K, t0, t1):
    """All (i, j) with 0<=i<A, 0<=j<K, t0 <= j-i <= t1."""
    t0 = max(t0, -(A - 1))
    t1 = min(t1, K - 1)
    if t0 > t1:
        return np.zeros(0, np.int64), np.zeros(0, np.int64)
    I, J = [], []
    for t in range(t0, t1 + 1):
        lo = max(0, -t)
        hi = min(A - 1, K - 1 - t)
        if lo > hi:
            continue
        i = np.arange(lo, hi + 1, dtype=np.int64)
        I.append(i)
        J.append(i + t)
    return np.concatenate(I), np.concatenate(J)


def merge(intervals):
    intervals.sort()
    out = []
    for a, b in intervals:
        if out and a <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def build(h, S, M, dlo=1, dhi=10**9):
    A, K = (h + 1) // 2, h // 2
    q = 1 << (max(A, K) - 1).bit_length()
    n = q * q
    W = ((h - 1) // S + M - 1) // M
    tables = q <= 4096
    if tables:  # exact lookup tables, built in chunks to bound memory
        CI = np.empty(n, np.int16); CJ = np.empty(n, np.int16)
        RK = np.empty((q, q), np.int32)
        for c0 in range(0, n, 1 << 21):
            t = np.arange(c0, min(n, c0 + (1 << 21)), dtype=np.int64)
            x, y = d2xy(q, t)
            CI[t] = x; CJ[t] = y; RK[x, y] = t
    R, Sx, Dl, Fa = [], [], [], []
    gathered = 0
    for d in range(max(1, dlo), min(W, dhi) + 1):
        zmax = math.isqrt(16 * d - 1)
        for delta in range(1 - M, M):
            X = S * (M * d + delta)
            if X <= 0 or X >= h:
                continue
            trip = pythagorean_rows(X, h)
            if not trip:
                continue
            hyp = np.zeros(2 * h + 2, dtype=np.int64)
            fac = np.zeros(2 * h + 2, dtype=np.int64)
            ivs = []
            for Y, L, a in trip:
                hyp[Y] = L
                fac[Y] = a
                for c in ((Y - 1) // 2, (-Y - 1) // 2):
                    ivs.append([c - zmax, c + zmax])
            for t0, t1 in merge(ivs):
                i_r, j_r = diagonal_cells(A, K, t0, t1)
                if len(i_r) == 0:
                    continue
                r = RK[i_r, j_r].astype(np.int64) if tables else xy2d(q, i_r, j_r)
                s = r + d
                ok = s < n
                r, s, i_r, j_r = r[ok], s[ok], i_r[ok], j_r[ok]
                if tables:
                    i_s = CI[s].astype(np.int64); j_s = CJ[s].astype(np.int64)
                else:
                    i_s, j_s = d2xy(q, s)
                act = (i_s < A) & (j_s < K)
                gathered += len(r)
                for row1, row2 in ((2 * i_r + 1, 2 * j_s + 2),
                                   (2 * j_r + 2, 2 * i_s + 1)):
                    Y = np.abs(row2 - row1)
                    L = hyp[Y]
                    tot = row1 + row2
                    hit = act & (L > 0) & (tot - L >= 2) & (tot + L <= 2 * h)
                    if hit.any():
                        R.append(r[hit]); Sx.append(s[hit])
                        Dl.append(np.full(int(hit.sum()), delta, np.int64))
                        Fa.append(fac[Y[hit]])
    cat = lambda z: np.concatenate(z) if z else np.zeros(0, np.int64)
    R, Sx, Dl, Fa = cat(R), cat(Sx), cat(Dl), cat(Fa)
    # deduplicate witnesses (r, s, delta, a): bands of different Y overlap
    key = np.stack([R, Sx, Dl, Fa], axis=1)
    key = np.unique(key, axis=0) if len(key) else key.reshape(0, 4)
    return {"h": h, "S": S, "M": M, "q": q, "labels": A * K,
            "gathered": gathered, "witness": key}


if __name__ == "__main__":
    h, S, M = map(int, sys.argv[1:4])
    out = sys.argv[4]
    t = time.time()
    res = build(h, S, M, *map(int, sys.argv[5:7]))
    np.savez_compressed(out, witness=res["witness"],
                        meta=np.array([h, S, M, res["q"], res["labels"]]))
    w = res["witness"]
    cons = np.unique(w[:, :3], axis=0) if len(w) else w
    print(h, S, M, "witnesses", len(w), "constraints", len(cons),
          "gathered", res["gathered"], "sec", round(time.time() - t, 1))
