"""R2s candidate system of one H7 residue block (sigma = 1).

Support: A = (0, y) label point of e, B = (u, s) sea point, C = (X, y + delta)
same-parity label point of f, D = (X + v, s) sea point, m = s - y,
delta = 28*Delta != 0.  Lemma mixedeq: |D-C| = |B-A| and (B-A).(C+D-A-B) = 0,
n = (C+D-A-B)/2 integral, common corners p = A+n, q = B+n with rows in [1,h].
Equivalently (proof in the write-up): with N = delta(2m - delta) and a
factorisation N = p*q (p = v - u, q = v + u), u = (q - p)/2 != 0 divides m*delta,
t = -m*delta/u is even, X = (t - p)/2.  Sea types: type(u) = type(X + v) = s
(columns relative to e's column, which is 0 mod 7).  X = 0 mod Smod and the
Hilbert precondition |X|/Smod >= 1 + floor(Delta^2/16).
Stage 1 (row stage) depends only on (parity, s, row of A); stage 2 attaches
partners: every label e on that row, f at rank r_e +- d with the right offset.
usage: py r2s_h7.py h lo bres M out.npz [prune7=1] [Smod=6272]
"""
import sys, time, math
import numpy as np
from numba import njit
from h7common import d2xy, xy2d, block

import os
QR7 = np.array([0, 2, 2, 1, 2, 1, 1], np.int64)   # type code by x mod 7: 0=F, 1=L(NR), 2=H(QR)
if os.environ.get("SWAP_LH"):
    QR7 = np.array([0, 1, 1, 2, 1, 2, 2], np.int64)  # reflected sea: L on QR columns, H on NR


def spf_sieve(n):
    spf = np.zeros(n + 1, np.int64)
    for p in range(2, n + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    return spf


@njit(cache=True)
def factor_into(x, spf, P, E, k):
    while x > 1:
        p = spf[x]
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        found = False
        for z in range(k):
            if P[z] == p:
                E[z] += e
                found = True
                break
        if not found:
            P[k] = p
            E[k] = e
            k += 1
    return k


@njit(cache=True)
def row_stage(h, lo_idx, hi_idx, res, svals, scodes, Smod, prune7, spf, typ7, out, hil=1):
    """out rows: (s_index, i, Delta, X, u, v). Returns count."""
    n = 0
    P = np.zeros(64, np.int64); E = np.zeros(64, np.int64)
    divs = np.zeros(200000, np.int64)
    for si in range(3):
        s = svals[si]; sc = scodes[si]
        for i in range(lo_idx, hi_idx + 1):
            y = res + 28 * i
            m = s - y
            for Dl in range(lo_idx - i, hi_idx - i + 1):
                if Dl == 0:
                    continue
                if prune7 and (m % 7 != 0) and (Dl % 7 != 0):
                    continue
                dl = 28 * Dl
                w2 = 2 * m - dl
                if w2 == 0:
                    continue
                # strip conditions for the common corners
                if y + dl // 2 < 1 or y + dl // 2 > h or s + dl // 2 < 1 or s + dl // 2 > h:
                    continue
                N = dl * w2
                k = 0
                k = factor_into(abs(dl), spf, P, E, k)
                k = factor_into(abs(w2), spf, P, E, k)
                # enumerate divisors
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
                        if n < out.shape[0]:
                            out[n, 0] = si; out[n, 1] = i; out[n, 2] = Dl
                            out[n, 3] = X; out[n, 4] = u; out[n, 5] = v
                        n += 1
    return n


@njit(cache=True)
def partner_stage(Q, M, Smod, odd_role, cand, oth0, oth1, iA0, iA1, jK0, jK1, out):
    """For each candidate (si, i, Delta, X, u, v) and each label e on that row,
    emit constraint (earlier, later, delta, cand_index)."""
    n = 0
    nQ = Q * Q
    for c in range(cand.shape[0]):
        i = cand[c, 1]; Dl = cand[c, 2]; X = cand[c, 3]
        qq = abs(X) // Smod
        sgn = 1 if X > 0 else -1
        d1 = qq // M; d2 = -(-qq // M)
        for di in range(2):
            d = d1 if di == 0 else d2
            if di == 1 and d2 == d1:
                continue
            if d < 1 or Dl * Dl >= 16 * d:
                continue
            dlt = qq - M * d
            for o in range(oth0, oth1 + 1):
                if odd_role:
                    ei = i; ej = o
                else:
                    ei = o; ej = i
                r = xy2d(Q, ei, ej)
                rf = r + sgn * d
                if rf < 0 or rf >= nQ:
                    continue
                fi, fj = d2xy(Q, rf)
                if fi < iA0 or fi > iA1 or fj < jK0 or fj > jK1:
                    continue
                if odd_role:
                    if fi != ei + Dl:
                        continue
                else:
                    if fj != ej + Dl:
                        continue
                if n < out.shape[0]:
                    if sgn > 0:
                        out[n, 0] = r; out[n, 1] = rf
                    else:
                        out[n, 0] = rf; out[n, 1] = r
                    out[n, 2] = dlt; out[n, 3] = c
                n += 1
    return n


def build(h, lo, bres, Ms, prune7=1, Smod=6272, svals=None, verbose=True):
    B = block(h, lo, bres=bres)
    if svals is None:
        svals = (B["L"], B["F"], B["H"])
    scodes = np.array([1, 0, 2], np.int64)   # L, F, H
    spf = spf_sieve(4 * h + 10)
    res = {}
    t0 = time.time()
    cands = {}
    for odd_role in (1, 0):
        if odd_role:
            lo_i, hi_i, rr = B["iA0"], B["iA1"], B["ares"]
        else:
            lo_i, hi_i, rr = B["jK0"], B["jK1"], bres
        out = np.zeros((1 << 21, 6), np.int64)
        n = row_stage(h, lo_i, hi_i, rr, np.array(svals, np.int64), scodes, Smod, prune7, spf, QR7, out)
        assert n <= out.shape[0], n
        cands[odd_role] = out[:n].copy()
    t1 = time.time()
    allc = {}
    for M in Ms:
        lst = []
        for odd_role in (1, 0):
            cand = cands[odd_role]
            if odd_role:
                o0, o1 = B["jK0"], B["jK1"]
            else:
                o0, o1 = B["iA0"], B["iA1"]
            cap = 1 << 23
            out = np.zeros((cap, 4), np.int64)
            n = partner_stage(B["Q"], M, Smod, odd_role, cand, o0, o1, B["iA0"], B["iA1"], B["jK0"], B["jK1"], out)
            assert n <= cap, n
            o = out[:n].copy()
            o = np.concatenate([o, np.full((n, 1), odd_role, np.int64)], 1)
            lst.append(o)
        allc[M] = np.concatenate(lst)
    if verbose:
        print("row stage", round(t1 - t0, 1), "s; candidates O", len(cands[1]), "E", len(cands[0]),
              "; partner stage", round(time.time() - t1, 1), "s")
    return B, cands, allc


if __name__ == "__main__":
    h, lo, bres, M = map(int, sys.argv[1:5]); outf = sys.argv[5]
    prune7 = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    Smod = int(sys.argv[7]) if len(sys.argv) > 7 else 6272
    B, cands, allc = build(h, lo, bres, [M], prune7, Smod)
    w = allc[M]
    cons = np.unique(w[:, :3], axis=0) if len(w) else np.zeros((0, 3), np.int64)
    np.savez_compressed(outf, cons=cons, candO=cands[1], candE=cands[0],
                        meta=np.array([h, M, lo, B["Q"], B["labels"], bres, Smod]))
    print("h", h, "lo", lo, "bres", bres, "M", M, "labels", B["labels"], "witnesses", len(w),
          "constraints", len(cons))
