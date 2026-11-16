"""Parallel version of r2s_h7.row_stage (identical filters; prange over (s, row)).
Checked equal to the serial version by r2s_par.py --test."""
import sys
import numpy as np
from numba import njit, prange
import r2s_h7
from r2s_h7 import factor_into

CAP = 512


@njit(parallel=True, cache=True)
def row_stage_par(h, lo_idx, hi_idx, res, svals, scodes, Smod, prune7, spf, typ7, hil):
    nr = hi_idx - lo_idx + 1
    cnt = np.zeros(3 * nr, np.int64)
    out = np.zeros((3 * nr, CAP, 6), np.int64)
    for job in prange(3 * nr):
        si = job // nr
        i = lo_idx + job % nr
        s = svals[si]; sc = scodes[si]
        P = np.zeros(64, np.int64); E = np.zeros(64, np.int64)
        divs = np.zeros(100000, np.int64)
        y = res + 28 * i
        m = s - y
        c = 0
        for Dl in range(lo_idx - i, hi_idx - i + 1):
            if Dl == 0:
                continue
            if prune7 and (m % 7 != 0) and (Dl % 7 != 0):
                continue
            dl = 28 * Dl
            w2 = 2 * m - dl
            if w2 == 0:
                continue
            if y + dl // 2 < 1 or y + dl // 2 > h or s + dl // 2 < 1 or s + dl // 2 > h:
                continue
            N = dl * w2
            k = 0
            k = factor_into(abs(dl), spf, P, E, k)
            k = factor_into(abs(w2), spf, P, E, k)
            nd = 1
            divs[0] = 1
            for z in range(k):
                cur = nd
                pw = 1
                for e in range(E[z]):
                    pw *= P[z]
                    for w in range(cur):
                        divs[nd] = divs[w] * pw
                        nd += 1
            for z in range(k):
                P[z] = 0; E[z] = 0
            md = m * dl
            hmin = 1 + (Dl * Dl) // 16 if hil else 1
            for w in range(nd):
                for sg in (1, -1):
                    p = sg * divs[w]
                    q = N // p
                    if (q - p) % 2 != 0:
                        continue
                    u = (q - p) // 2
                    if u == 0 or md % u != 0:
                        continue
                    t = -(md // u)
                    if t % 2 != 0 or (t - p) % 2 != 0:
                        continue
                    X = (t - p) // 2
                    if X == 0 or X % Smod != 0:
                        continue
                    if abs(X) // Smod < hmin:
                        continue
                    v = u + p
                    if typ7[u % 7] != sc or typ7[(X + v) % 7] != sc:
                        continue
                    if c < CAP:
                        out[job, c, 0] = si; out[job, c, 1] = i; out[job, c, 2] = Dl
                        out[job, c, 3] = X; out[job, c, 4] = u; out[job, c, 5] = v
                    c += 1
        cnt[job] = c
    return cnt, out


@njit(parallel=True, cache=True)
def row_stage_list(h, lo_idx, hi_idx, rowlist, res, svals, scodes, Smod, prune7, spf, typ7, hil):
    nr = rowlist.shape[0]
    cnt = np.zeros(3 * nr, np.int64)
    out = np.zeros((3 * nr, CAP, 6), np.int64)
    for job in prange(3 * nr):
        si = job // nr
        i = rowlist[job % nr]
        s = svals[si]; sc = scodes[si]
        P = np.zeros(64, np.int64); E = np.zeros(64, np.int64)
        divs = np.zeros(100000, np.int64)
        y = res + 28 * i
        m = s - y
        c = 0
        for Dl in range(lo_idx - i, hi_idx - i + 1):
            if Dl == 0:
                continue
            if prune7 and (m % 7 != 0) and (Dl % 7 != 0):
                continue
            dl = 28 * Dl
            w2 = 2 * m - dl
            if w2 == 0:
                continue
            if y + dl // 2 < 1 or y + dl // 2 > h or s + dl // 2 < 1 or s + dl // 2 > h:
                continue
            N = dl * w2
            k = 0
            k = factor_into(abs(dl), spf, P, E, k)
            k = factor_into(abs(w2), spf, P, E, k)
            nd = 1
            divs[0] = 1
            for z in range(k):
                cur = nd
                pw = 1
                for e in range(E[z]):
                    pw *= P[z]
                    for w in range(cur):
                        divs[nd] = divs[w] * pw
                        nd += 1
            for z in range(k):
                P[z] = 0; E[z] = 0
            md = m * dl
            hmin = 1 + (Dl * Dl) // 16 if hil else 1
            for w in range(nd):
                for sg in (1, -1):
                    p = sg * divs[w]
                    q = N // p
                    if (q - p) % 2 != 0:
                        continue
                    u = (q - p) // 2
                    if u == 0 or md % u != 0:
                        continue
                    t = -(md // u)
                    if t % 2 != 0 or (t - p) % 2 != 0:
                        continue
                    X = (t - p) // 2
                    if X == 0 or X % Smod != 0:
                        continue
                    if abs(X) // Smod < hmin:
                        continue
                    v = u + p
                    if typ7[u % 7] != sc or typ7[(X + v) % 7] != sc:
                        continue
                    if c < CAP:
                        out[job, c, 0] = si; out[job, c, 1] = i; out[job, c, 2] = Dl
                        out[job, c, 3] = X; out[job, c, 4] = u; out[job, c, 5] = v
                    c += 1
        cnt[job] = c
    return cnt, out


def run(h, lo_i, hi_i, rr, sv, sc, Smod, prune7, spf, hil=1):
    cnt, out = row_stage_par(h, lo_i, hi_i, rr, sv, sc, Smod, prune7, spf, r2s_h7.QR7, hil)
    assert cnt.max(initial=0) <= CAP, cnt.max()
    rows = [out[j, :cnt[j]] for j in np.nonzero(cnt)[0]]
    return np.concatenate(rows) if rows else np.zeros((0, 6), np.int64)


if __name__ == "__main__":
    from h7common import block
    h, lo, bres, Smod, hil = map(int, sys.argv[1:6])
    B = block(h, lo, bres=bres)
    spf = r2s_h7.spf_sieve(4 * h + 10)
    Fr = B["F"] if B["F"] < h else 55
    sv = np.array((B["L"], Fr, B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
    for odd_role in (1, 0):
        lo_i, hi_i, rr = (B["iA0"], B["iA1"], 17) if odd_role else (B["jK0"], B["jK1"], bres)
        a = run(h, lo_i, hi_i, rr, sv, sc, Smod, 1, spf, hil)
        o = np.zeros((1 << 21, 6), np.int64)
        n = r2s_h7.row_stage(h, lo_i, hi_i, rr, sv, sc, Smod, 1, spf, r2s_h7.QR7, o, hil)
        print("role", odd_role, "par", len(a), "serial", n,
              "equal", set(map(tuple, a.tolist())) == set(map(tuple, o[:n].tolist())))
