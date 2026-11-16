"""Shared builders for the J_11 DEC test (S = 32, M = 3, cand version).

Hilbert recursion (2) exactly as in the archive (blk.py): H_2n lists Q1 = transpose,
Q2 = +(0,n), Q3 = +(n,n), Q4 = (2n-1-y, n-1-x).  Cells are (x, y); odd row 2x+1,
even row 2y+2, T = y - x.  A cand triple (r, r+d, delta), q = M d + delta, |delta| <= M-1,
exists iff some cross pair (odd row of one endpoint, even row of the other) has
Y = |even - odd| with (S q)^2 + Y^2 a perfect square.
"""
import numpy as np
import numba as nb
from math import isqrt

S, M = 32, 3


def hilbert_array(q, dtype=np.int32):
    xy = np.zeros((1, 2), dtype=dtype); n = 1
    while n < q:
        b = n * n
        nxt = np.empty((4 * b, 2), dtype=dtype)
        nxt[:b] = xy[:, ::-1]
        nxt[b:2 * b] = xy + np.array((0, n), dtype=dtype)
        nxt[2 * b:3 * b] = xy + np.array((n, n), dtype=dtype)
        nxt[3 * b:, 0] = 2 * n - 1 - xy[:, 1]
        nxt[3 * b:, 1] = n - 1 - xy[:, 0]
        xy = nxt; n *= 2
    return xy


def legs(Ymax):
    """dict q -> sorted list of odd Y <= Ymax with (S q)^2 + Y^2 a square.
    Uses Y^2 = u w, u < w both odd, X = (w - u)/2; divisors of Y^2 from a sieve."""
    spf = list(range(Ymax + 1))
    for p in range(2, isqrt(Ymax) + 1):
        if spf[p] == p:
            for k in range(p * p, Ymax + 1, p):
                if spf[k] == k:
                    spf[k] = p
    out = {}
    for Y in range(1, Ymax + 1, 2):
        f = {}
        z = Y
        while z > 1:
            p = spf[z]; f[p] = f.get(p, 0) + 2; z //= p
        divs = [1]
        for p, e in f.items():
            divs = [dv * p ** k for dv in divs for k in range(e + 1)]
        Y2 = Y * Y
        for u in divs:
            if u < Y:
                w = Y2 // u
                X = (w - u) // 2
                if X > 0 and X % S == 0:
                    out.setdefault(X // S, []).append(Y)
    return {q: sorted(set(v)) for q, v in out.items()}


def pack_legs(P, dmax):
    """arrays (d, delta, offs, Ys) over all (q, slot) with 1 <= d <= dmax."""
    ds, dl, offs, Ys = [], [], [0], []
    for q in sorted(P):
        for d in sorted({q // M, (q + M - 1) // M}):
            delta = q - M * d
            if d < 1 or d > dmax or abs(delta) > M - 1:
                continue
            ds.append(d); dl.append(delta)
            Ys.extend(P[q]); offs.append(len(Ys))
    return (np.array(ds, dtype=np.int64), np.array(dl, dtype=np.int64),
            np.array(offs, dtype=np.int64), np.array(Ys, dtype=np.int64))


@nb.njit(parallel=True, cache=True)
def _count(odd, even, lo, hi, ds, offs, Ys, nchunk):
    cnts = np.zeros(nchunk, dtype=np.int64)
    span = hi - lo
    csz = (span + nchunk - 1) // nchunk
    for c in nb.prange(nchunk):
        r0 = lo + c * csz; r1 = min(hi, r0 + csz)
        cnt = 0
        for t in range(ds.shape[0]):
            d = ds[t]
            rr1 = min(r1, hi - d)
            k0 = offs[t]; k1 = offs[t + 1]
            for r in range(r0, rr1):
                y0 = even[r + d] - odd[r]
                if y0 < 0:
                    y0 = -y0
                y1 = even[r] - odd[r + d]
                if y1 < 0:
                    y1 = -y1
                hit = False
                for k in range(k0, k1):
                    if Ys[k] == y0 or Ys[k] == y1:
                        hit = True
                if hit:
                    cnt += 1
        cnts[c] = cnt
    return cnts


@nb.njit(parallel=True, cache=True)
def _fill(odd, even, lo, hi, ds, dl, offs, Ys, nchunk, starts, out):
    span = hi - lo
    csz = (span + nchunk - 1) // nchunk
    for c in nb.prange(nchunk):
        r0 = lo + c * csz; r1 = min(hi, r0 + csz)
        p = starts[c]
        for t in range(ds.shape[0]):
            d = ds[t]
            rr1 = min(r1, hi - d)
            k0 = offs[t]; k1 = offs[t + 1]
            for r in range(r0, rr1):
                y0 = even[r + d] - odd[r]
                if y0 < 0:
                    y0 = -y0
                y1 = even[r] - odd[r + d]
                if y1 < 0:
                    y1 = -y1
                hit = False
                for k in range(k0, k1):
                    if Ys[k] == y0 or Ys[k] == y1:
                        hit = True
                if hit:
                    out[p, 0] = r; out[p, 1] = r + d; out[p, 2] = dl[t]
                    p += 1


def window_triples(odd, even, lo, hi, P, nchunk=96):
    """all distinct cand triples (r, u, delta) with lo <= r < u < hi (global ranks)."""
    ds, dl, offs, Ys = pack_legs(P, hi - lo - 1)
    cnts = _count(odd, even, lo, hi, ds, offs, Ys, nchunk)
    starts = np.concatenate([[0], np.cumsum(cnts)[:-1]]).astype(np.int64)
    out = np.empty((int(cnts.sum()), 3), dtype=np.int64)
    _fill(odd, even, lo, hi, ds, dl, offs, Ys, nchunk, starts, out)
    # distinct rows via a packed 1D key (r < 2^24, d < 2^24, delta + 4 < 8)
    key = (out[:, 0] << 27) | ((out[:, 1] - out[:, 0]) << 3) | (out[:, 2] + 4)
    del out
    key = np.unique(key)
    r = key >> 27; d = (key >> 3) & ((1 << 24) - 1); dl_ = (key & 7) - 4
    return np.stack([r, r + d, dl_], axis=1)


def certified_classes(E):
    """one representative triple (r, u, delta) per certified class (r, u, delta mod M)."""
    key = np.stack([E[:, 0], E[:, 1], E[:, 2] % M], axis=1)
    _, first = np.unique(key, axis=0, return_index=True)
    return E[np.sort(first)]


def core(n, C, k=M, anchor=None):
    """weighted k-core on distinct certified classes C (rows r, u, delta mod M).
    Labels flagged in anchor are never peeled."""
    alive = np.ones(len(C), dtype=bool)
    while True:
        deg = np.bincount(C[alive, 0], minlength=n) + np.bincount(C[alive, 1], minlength=n)
        bad = deg < k
        if anchor is not None:
            bad &= ~anchor
        kill = alive & (bad[C[:, 0]] | bad[C[:, 1]])
        if not kill.any():
            return C[alive]
        alive &= ~kill
