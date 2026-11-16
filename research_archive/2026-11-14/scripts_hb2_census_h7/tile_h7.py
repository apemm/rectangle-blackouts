"""P and R2s candidate systems of ONE tile of the multilevel diagonal tiling (C4).
Tile = aligned square [x0, x0+l) x [y0, y0+l) of the block's (bottom-indexed)
coordinates, its own Hilbert core (rank = Hilbert rank of the local coordinates
in the l-square), stride Sk; labels = bulk labels in the square with
G1 <= |j - i| < G2 (level k: G1 = l/2, G2 = l).
usage: py tile_h7.py h lo bres x0 y0 l Sk M"""
import sys, math, time, json
import numpy as np
from numba import njit
from h7common import d2xy, xy2d, block
import p_h7, r2s_h7, r2s_par, analyze_h7


@njit(cache=True)
def valid(i, j, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
    if i < 0 or j < 0 or i >= l or j >= l:
        return False
    gi = x0 + i; gj = y0 + j
    if gi < iA0 or gi > iA1 or gj < jK0 or gj > jK1:
        return False
    g = abs(gj - gi)
    return G1 <= g < G2


@njit(cache=True)
def scanP(l, d, delta, h, ares, bres, x0, y0, iA0, iA1, jK0, jK1, G1, G2, T0, T1, hyp, outR, outD, nout):
    nQ = l * l
    for T in range(T0, T1 + 1):
        for i in range(max(0, -T), min(l, l - T)):
            j = i + T
            if not valid(i, j, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
                continue
            r = xy2d(l, i, j)
            s = r + d
            if s >= nQ:
                continue
            fi, fj = d2xy(l, s)
            if not valid(fi, fj, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
                continue
            hit = False
            y1 = ares + 28 * i; y2 = bres + 28 * fj
            L = hyp[abs(y2 - y1)]
            if L > 0 and y1 + y2 - L >= 2 and y1 + y2 + L <= 2 * h:
                hit = True
            y1 = bres + 28 * j; y2 = ares + 28 * fi
            L = hyp[abs(y2 - y1)]
            if L > 0 and y1 + y2 - L >= 2 and y1 + y2 + L <= 2 * h:
                hit = True
            if hit:
                outR[nout[0]] = r; outD[nout[0]] = delta; nout[0] += 1
    return 0


@njit(cache=True)
def partnerT(l, M, Sk, odd_role, cand, x0, y0, iA0, iA1, jK0, jK1, G1, G2, out):
    n = 0
    nQ = l * l
    for c in range(cand.shape[0]):
        gi_row = cand[c, 1]; Dl = cand[c, 2]; X = cand[c, 3]
        qq = abs(X) // Sk
        sgn = 1 if X > 0 else -1
        d1 = qq // M; d2 = -(-qq // M)
        for di in range(2):
            d = d1 if di == 0 else d2
            if di == 1 and d2 == d1:
                continue
            if d < 1 or Dl * Dl >= 16 * d:
                continue
            dlt = qq - M * d
            for o in range(l):
                if odd_role:
                    ei = gi_row - x0; ej = o
                else:
                    ei = o; ej = gi_row - y0
                if not valid(ei, ej, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
                    continue
                r = xy2d(l, ei, ej)
                rf = r + sgn * d
                if rf < 0 or rf >= nQ:
                    continue
                fi, fj = d2xy(l, rf)
                if not valid(fi, fj, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
                    continue
                if odd_role and fi != ei + Dl:
                    continue
                if (not odd_role) and fj != ej + Dl:
                    continue
                if sgn > 0:
                    out[n, 0] = r; out[n, 1] = rf
                else:
                    out[n, 0] = rf; out[n, 1] = r
                out[n, 2] = dlt; out[n, 3] = c
                n += 1
    return n


@njit(cache=True)
def count_labels(x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
    n = 0
    for i in range(l):
        for j in range(l):
            if valid(i, j, x0, y0, l, iA0, iA1, jK0, jK1, G1, G2):
                n += 1
    return n


def build(h, lo, bres, x0, y0, l, Sk, M, G=None):
    B = block(h, lo, bres=bres)
    ares_l = 17 + 28 * x0; bres_l = bres + 28 * y0
    c = bres_l - ares_l
    G1, G2 = (l // 2, l) if G is None else G
    args = (x0, y0, B["iA0"], B["iA1"], B["jK0"], B["jK1"], G1, G2)
    nlab = count_labels(x0, y0, l, *args[2:])
    R, Dd, Dl = [], [], []
    for qq in range(1, (h - 1) // Sk + 1):
        X = Sk * qq
        tr = p_h7.triples(X, h)
        if not tr:
            continue
        hyp = np.zeros(2 * h + 2, np.int64)
        for Y, L in tr:
            hyp[Y] = L
        for d in sorted({qq // M, -(-qq // M)}):
            if d < 1:
                continue
            delta = qq - M * d
            zmax = math.isqrt(16 * d - 1)
            ivs = []
            for Y, L in tr:
                for sg in (1, -1):
                    if (sg * Y - c) % 28 == 0:
                        t = (sg * Y - c) // 28; ivs.append([t - zmax, t + zmax])
                    if (sg * Y + c) % 28 == 0:
                        t = -((sg * Y + c) // 28); ivs.append([t - zmax, t + zmax])
            ivs.sort(); mer = []
            for a, b in ivs:
                if mer and a <= mer[-1][1] + 1:
                    mer[-1][1] = max(mer[-1][1], b)
                else:
                    mer.append([a, b])
            for T0, T1 in mer:
                T0 = max(T0, -(l - 1)); T1 = min(T1, l - 1)
                if T0 > T1:
                    continue
                cap = 1 << 22
                oR = np.zeros(cap, np.int64); oD = np.zeros(cap, np.int64); no = np.zeros(1, np.int64)
                scanP(l, d, delta, h, ares_l, bres_l, *args[:2], *args[2:], T0, T1, hyp, oR, oD, no)
                n = int(no[0]); assert n < cap
                R.append(oR[:n].copy()); Dd.append(np.full(n, d)); Dl.append(oD[:n].copy())
    cat = lambda z: np.concatenate(z) if z else np.zeros(0, np.int64)
    R, Dd, Dl = cat(R), cat(Dd), cat(Dl)
    Pk = np.unique(np.stack([R, R + Dd, Dl], 1), axis=0) if len(R) else np.zeros((0, 3), np.int64)
    # R2s: row stage over the tile's global rows (stride Sk), partner stage inside the tile
    spf = r2s_h7.spf_sieve(4 * h + 10)
    sv = np.array((B["L"], B["F"], B["H"]), np.int64); sc = np.array([1, 0, 2], np.int64)
    lst = []; ncand = {}
    import os
    for odd_role in ((1, 0) if not os.environ.get('NO_R2S') else ()):
        if odd_role:
            lo_i, hi_i, rr = max(B["iA0"], x0), min(B["iA1"], x0 + l - 1), 17
        else:
            lo_i, hi_i, rr = max(B["jK0"], y0), min(B["jK1"], y0 + l - 1), bres
        if lo_i > hi_i:
            continue
        cand = r2s_par.run(h, lo_i, hi_i, rr, sv, sc, Sk, 1 if Sk % 49 == 0 else 0, spf, 1)
        ncand["O" if odd_role else "E"] = int(len(cand))
        out = np.zeros((1 << 22, 4), np.int64)
        n = partnerT(l, M, Sk, odd_role, cand, *args, out)
        lst.append(out[:n, :3])
    w = np.concatenate(lst) if lst else np.zeros((0, 3), np.int64)
    Rk = np.unique(w, axis=0) if len(w) else np.zeros((0, 3), np.int64)
    return nlab, Pk, Rk, ncand


if __name__ == "__main__":
    h, lo, bres, x0, y0, l, Sk, M = map(int, sys.argv[1:9])
    t0 = time.time()
    G = (int(sys.argv[9]), int(sys.argv[10])) if len(sys.argv) > 10 else None
    nlab, Pk, Rk, ncand = build(h, lo, bres, x0, y0, l, Sk, M, G)
    keep = ["constraints", "incident", "mean_inc", "max_inc", "degeneracy", "core_sizes", "greedy_stuck", "M_suffices", "method"]
    out = {"h": h, "bres": bres, "tile": [x0, y0, l], "Sk": Sk, "M": M, "labels": int(nlab), "R2s_row_cands": ncand}
    for nm, K in (("P", Pk), ("R2s", Rk)):
        r = analyze_h7.analyze(M, nlab, K); r.pop("inc_hist", None)
        out[nm] = {k: r.get(k) for k in keep}
    U = np.unique(np.concatenate([Pk, Rk]), axis=0)
    r = analyze_h7.analyze(M, nlab, U); r.pop("inc_hist", None)
    out["PuR2s"] = {k: r.get(k) for k in keep}
    out["sec"] = round(time.time() - t0, 1)
    print(json.dumps(out))
