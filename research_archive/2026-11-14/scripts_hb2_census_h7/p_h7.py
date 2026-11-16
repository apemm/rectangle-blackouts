"""P candidate system of one H7 residue block (sigma = 1, S = 6272).

Witness: labels e (rank r) and f (rank r + d), slot gap q' = M d + delta,
X = S q' < h, one cross-parity pair of their points (odd of one, even of
the other) with X^2 + Y^2 = L^2, L <= h - 1, and vertical completion rows
(y1 + y2 -+ L)/2 in [1, h]  (same conventions as scripts_hb1_census/pgraph.py).
Constraint (r, r+d, delta) forbids xi_{r+d} - xi_r = delta.
Band method: row difference = c + 28 (T_e + z) with |z| <= isqrt(16d - 1)
(Hilbert locality, audited), so only earlier labels on the diagonals
T_e = j_e - i_e in a band around (+-Y - c)/28 can be hit.
usage: py p_h7.py h M lo out.npz [bres]
"""
import math, sys, time
import numpy as np
from numba import njit
from h7common import S, d2xy, xy2d, block


def triples(X, h):
    v = (X // 2) ** 2
    out = []
    for a in range(1, math.isqrt(v) + 1):
        if v % a == 0:
            b = v // a
            if a + b <= h - 1 and (b - a) % 2:
                out.append((b - a, a + b))
    return out


@njit(cache=True)
def scan(Q, d, delta, h, ares, bres, iA0, iA1, jK0, jK1, T0, T1, hyp,
         outR, outD, nout):
    nQ = Q * Q
    for T in range(T0, T1 + 1):
        ilo = max(iA0, jK0 - T)
        ihi = min(iA1, jK1 - T)
        for i in range(ilo, ihi + 1):
            j = i + T
            r = xy2d(Q, i, j)
            s = r + d
            if s >= nQ:
                continue
            fi, fj = d2xy(Q, s)
            if fi < iA0 or fi > iA1 or fj < jK0 or fj > jK1:
                continue
            hit = False
            # role 1: odd of e, even of f
            y1 = ares + 28 * i
            y2 = bres + 28 * fj
            Y = abs(y2 - y1)
            L = hyp[Y]
            if L > 0 and y1 + y2 - L >= 2 and y1 + y2 + L <= 2 * h:
                hit = True
            # role 2: even of e, odd of f
            y1 = bres + 28 * j
            y2 = ares + 28 * fi
            Y = abs(y2 - y1)
            L = hyp[Y]
            if L > 0 and y1 + y2 - L >= 2 and y1 + y2 + L <= 2 * h:
                hit = True
            if hit:
                if nout[0] < outR.shape[0]:
                    outR[nout[0]] = r
                    outD[nout[0]] = delta
                nout[0] += 1
    return 0


def build(h, M, lo, bres=8, Sm=S):
    B = block(h, lo, bres=bres)
    Q, ares = B["Q"], B["ares"]
    c = bres - ares
    R, D, Dl = [], [], []
    ntrip = 0
    cells = 0
    for qq in range(1, (h - 1) // Sm + 1):
        X = Sm * qq
        tr = triples(X, h)
        if not tr:
            continue
        hyp = np.zeros(2 * h + 2, np.int64)
        for Y, L in tr:
            hyp[Y] = L
        ntrip += len(tr)
        for d in sorted({qq // M, -(-qq // M)}):
            if d < 1:
                continue
            delta = qq - M * d
            zmax = math.isqrt(16 * d - 1)
            ivs = []
            for Y, L in tr:
                for sg in (1, -1):
                    # role 1: c + 28 (T + z) = sg*Y ; role 2: -c + 28(-T + z') = sg*Y
                    if (sg * Y - c) % 28 == 0:
                        t = (sg * Y - c) // 28
                        ivs.append([t - zmax, t + zmax])
                    if (sg * Y + c) % 28 == 0:
                        t = -((sg * Y + c) // 28)
                        ivs.append([t - zmax, t + zmax])
            if not ivs:
                continue
            ivs.sort()
            mer = []
            for a, b in ivs:
                if mer and a <= mer[-1][1] + 1:
                    mer[-1][1] = max(mer[-1][1], b)
                else:
                    mer.append([a, b])
            for T0, T1 in mer:
                cap = 1 << 22
                outR = np.zeros(cap, np.int64); outD = np.zeros(cap, np.int64)
                nout = np.zeros(1, np.int64)
                scan(Q, d, delta, h, ares, bres, B["iA0"], B["iA1"], B["jK0"],
                     B["jK1"], T0, T1, hyp, outR, outD, nout)
                n = int(nout[0]); assert n <= cap
                cells += (T1 - T0 + 1)
                R.append(outR[:n].copy()); D.append(np.full(n, d)); Dl.append(outD[:n].copy())
    cat = lambda z: np.concatenate(z) if z else np.zeros(0, np.int64)
    R, D, Dl = cat(R), cat(D), cat(Dl)
    key = np.unique(np.stack([R, R + D, Dl], 1), axis=0) if len(R) else np.zeros((0, 3), np.int64)
    return B, key, ntrip


if __name__ == "__main__":
    h, M, lo = map(int, sys.argv[1:4]); out = sys.argv[4]
    bres = int(sys.argv[5]) if len(sys.argv) > 5 else 8
    t = time.time()
    B, key, ntrip = build(h, M, lo, bres)
    np.savez_compressed(out, cons=key, meta=np.array([h, M, lo, B["Q"], B["labels"], bres]))
    print("h", h, "M", M, "lo", lo, "bres", bres, "Q", B["Q"], "labels", B["labels"],
          "triples", ntrip, "constraints", len(key), "sec", round(time.time() - t, 1))
