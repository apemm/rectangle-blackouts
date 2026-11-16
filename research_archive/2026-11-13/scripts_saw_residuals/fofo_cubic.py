"""Two-label mixed quadruples with side {L1, F1} and diagonal {L2, F2}, L1, L2 label points of ONE class
(both odd: 'oo', or both even: 'ee'), F1, F2 SAW fillers. Exact solver via the cubic in p = x1 - x2:
  U = F1 - L1 = (x1, y1), V = F2 - L2 = (x2, y2) in (slot, row/4) units, L2 - L1 = (2d, d) (rows: 4d),
  |U| = |V| and |U - V|^2 = 4 d (2 x1 + y1)   (Lemma mixedeq, Sigma.U = 0),
  p^3 - 4 d p^2 + ((y1 - y2)^2 - 4 d y1) p - 4 d (y2^2 - y1^2) = 0,  q = x1 + x2 = (y2^2 - y1^2)/p.
Everything is done in ORIGINAL integer coordinates to avoid quarter units: X = 4 * slot, rows y.
Usage: py fofo_cubic.py h iota LM rule(saw|star) kind(oo|ee) [sstep]"""
import sys
import numpy as np
from numba import njit

@njit(cache=True)
def tsq(n):
    if n < 0: return -1
    r = int(np.sqrt(n))
    while r * r > n: r -= 1
    while (r + 1) * (r + 1) <= n: r += 1
    return r if r * r == n else -1

@njit(cache=True)
def census(h, iota, LM, rule, ee, sstep):
    A = (h + 1) // 2; K = h // 2
    OFF = np.array([-3, -2, -1, 0])
    tot = 0; nl = 0; hom = 0
    ex = np.zeros((20, 8), dtype=np.int64); nex = 0
    for s in range(-(h // 2), h // 2, sstep):
        T = 2 * s + 1
        yP0 = (2 * iota + 1) % 64
        if rule == 0:
            res, mod = (2 * iota + 1) % 16, 16
        else:
            res, mod = ((yP0 + (32 if T % 4 == 3 else 48)) % 64), 64
        R0 = 0
        for y in range(2, h + 1):
            if y % mod == res: R0 = y
        band = R0 - 24 - 80
        labs = []
        for i in range(1, A):
            if i % LM == iota and 0 <= i + s < K:
                yl = 2 * (i + s) + 2 if ee else 2 * i + 1
                if 2 * i + 1 <= band and 2 * (i + s) + 2 <= band:
                    labs.append(i)
        nl += len(labs)
        occ = set(labs)
        for i1 in labs:
            for i2 in labs:
                if i1 == i2: continue
                yl1 = 2 * (i1 + s) + 2 if ee else 2 * i1 + 1
                yl2 = 2 * (i2 + s) + 2 if ee else 2 * i2 + 1
                for a1 in range(4):
                    for a2 in range(4):
                        yf1 = R0 + 8 * OFF[a1]; yf2 = R0 + 8 * OFF[a2]
                        # original coords: U = (X1, Y1), V = (X2, Y2); L2 - L1 = (4t, 2t), t = i2 - i1
                        Y1 = yf1 - yl1; Y2 = yf2 - yl2; t = i2 - i1
                        # conditions: X1^2 + Y1^2 = X2^2 + Y2^2 ; Sigma.U = 0 with Sigma = 2(L2-L1) + V - U
                        # (2(4t,2t) + V - U).U = 0  ->  |U - V|^2 = 2 * 2 (4t X1 + 2t Y1) = 8t(2X1 + Y1)
                        # P = X1 - X2: P^3 - 8 t P^2 + ((Y1-Y2)^2 - 8 t Y1) P - 8 t (Y2^2 - Y1^2) = 0
                        c0 = 8 * t * (Y2 * Y2 - Y1 * Y1)
                        if c0 == 0: continue
                        ac = abs(c0)
                        # integer roots P divide c0: test candidates from the cubic's real roots instead
                        # numeric roots of the monic cubic
                        b2 = -8.0 * t; b1 = float((Y1 - Y2) ** 2 - 8 * t * Y1); b0 = float(-c0)
                        rts = np.roots(np.array([1.0 + 0j, b2 + 0j, b1 + 0j, b0 + 0j]))
                        for r in rts:
                            if abs(r.imag) > 1e-6 * (1 + abs(r.real)): continue
                            for P in range(int(np.floor(r.real)) - 1, int(np.ceil(r.real)) + 2):
                                if P == 0: continue
                                if P ** 3 + (-8 * t) * P * P + ((Y1 - Y2) ** 2 - 8 * t * Y1) * P - c0 != 0: continue
                                num = Y2 * Y2 - Y1 * Y1
                                if num % P: continue
                                Qs = num // P
                                if (P + Qs) % 2: continue
                                X1 = (P + Qs) // 2; X2 = (Qs - P) // 2
                                if X1 % 4 or X2 % 4: continue
                                g1 = X1 // 4; g2 = X2 // 4
                                if (g1 - a1) % 4 or (g2 - a2) % 4: continue
                                if (i1 + g1) in occ or (i2 + g2) in occ: continue
                                if g1 == 0 or g2 == 0: continue
                                if X1 == X2 and Y1 == Y2: continue
                                # corners p = A + N, q = B + N, N = (C + D - A - B)/2, A = L1, B = F1, C = L2, D = F2
                                Sx = 2 * 4 * t + X2 - X1; Sy = 2 * 2 * t + Y2 - Y1
                                if Sx % 2 or Sy % 2: continue
                                Ny = Sy // 2
                                ry1 = yl1 + Ny; ry2 = yf1 + Ny
                                if not (1 <= ry1 <= h and 1 <= ry2 <= h): continue
                                tot += 1
                                if a1 == a2: hom += 1
                                if nex < 20:
                                    ex[nex, 0] = s; ex[nex, 1] = i1; ex[nex, 2] = i2; ex[nex, 3] = g1
                                    ex[nex, 4] = g2; ex[nex, 5] = yf1; ex[nex, 6] = yf2; ex[nex, 7] = R0; nex += 1
    return nl, tot, hom, ex[:nex]

if __name__ == '__main__':
    h = int(sys.argv[1]); iota = int(sys.argv[2]); LM = int(sys.argv[3])
    rule = 0 if sys.argv[4] == 'saw' else 1; ee = sys.argv[5] == 'ee'
    sstep = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    nl, tot, hom, ex = census(h, iota, LM, rule, ee, sstep)
    print('h', h, 'iota', iota, 'LM', LM, sys.argv[4], sys.argv[5], 'labels', nl, 'quadruples', tot, 'same-row fillers', hom)
    for e in ex[:8]: print('   s,i1,i2,g1,g2,yF1,yF2,T* =', list(e))
