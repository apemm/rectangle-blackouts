"""LAD | Sea(r0, g) seam (J1 for LAD).  Rows: LAD filler at slot X has row T* - 8 eta(X); buffer deep points in row g.
t0 = T* - g (odd, -63..3).  Parts (a)-(c) of J1 are proved by hand for LAD; this checks (d) and (e).
(d) all-deep mixed quadruples with one row-g point and one LAD point on each pair:
    side {G1, S1}, diagonal {G2, S2}; slots Q1 (S1), Q2 = Q1 + Dl (S2), P1 = Q1 - a, P2 = Q2 - c (row g),
    a^2 - c^2 = m (sig1 + 4m), a (a - c + 2 Dl) = -m sig1 / 2,  sig1 = s1 - g, s2 - s1 = 8m.
    Seam: LAD slots < z0 <= buffer slots, so a < 0, c < 0, c < Dl < -a (or the mirror, handled by X -> -X).
(e) rival pairs filler (row c) / row-g point at slot distance kap: j (|g - c| + j) = 4 kap^2, 1 <= j <= h - max(g, c),
    j <= min(g, c) - 1.  Report the bad (eta, kap) pairs and the end phases that avoid them.
Usage: py seam.py Ep"""
import sys
from lad import eta_array
Ep = int(sys.argv[1]); E, P = eta_array(Ep)
vals = sorted(set(E.tolist()))

def divpairs(n):
    n0 = abs(n); out = []
    d = 1
    while d * d <= n0:
        if n0 % d == 0:
            for x in (d, n0 // d):
                for sx in (1, -1):
                    X = sx * x; Y = n // X
                    out.append((X, Y))
        d += 1
    return out

# (d) for both orientations: orientation +1 = LAD left of seam; mirror X -> -X gives LAD right (a > 0, c > 0)
tot = 0; ex = []
for t0 in range(-63, 4, 2):
    for Q1 in range(P):
        s1 = t0 - 8 * int(E[Q1])          # sig1 = s1 - g, measured from g
        for v2 in vals:
            sig2 = t0 - 8 * v2
            if (sig2 - s1) % 8: continue
            m = (sig2 - s1) // 8
            if m == 0: continue
            N = m * (s1 + 4 * m)
            for X, Y in divpairs(N):
                if (X + Y) % 2: continue
                a = (X + Y) // 2; c = (Y - X) // 2
                if a == 0: continue
                if (m * s1) % (2 * a): continue
                t = -m * s1 // (2 * a) - X
                if t % 2: continue
                Dl = t // 2
                for orient in (1, -1):
                    if orient == 1 and not (a < 0 and c < 0 and c < Dl < -a): continue
                    if orient == -1 and not (a > 0 and c > 0 and -a < Dl < c): continue
                    if E[(Q1 + Dl) % P] != v2: continue
                    tot += 1
                    if len(ex) < 10: ex.append((t0, Q1, Dl, a, c, m))
print("E'=%d (d) seam mixed quadruples (one row-g point per pair): %d" % (Ep, tot))
for x in ex: print('   t0,Q1,Dl,a,c,m =', x)

# (e) rival pairs: depth of filler below h is d_f = (h - T*) + 8 eta; g = h - gam with gam in {0,1,3}
print("(e) rival pairs filler/row-g: bad (gam, delta = h - T*, eta, kap, j)")
for gam in (0, 1, 3):
    for delta in range(0, 64, 2):     # h - T* even (h, T* same parity when gam != 0 ... list all)
        bad = []
        for v in vals:
            c_below_h = delta + 8 * v        # h - c
            gc = c_below_h - gam             # g - c (>0 if filler below g)
            for j in range(1, 4):
                if gc > 0:
                    if j > gam: continue      # j <= h - g
                    q = j * (gc + j)
                elif gc < 0:
                    if j > c_below_h: continue  # j <= h - c
                    q = j * (-gc + j)
                else:
                    continue
                if q % 4: continue
                k2 = q // 4; k = int(round(k2 ** 0.5))
                if k * k == k2 and k >= 1: bad.append((v, k, j))
        if bad:
            # right end: buffer slots n >= n0; bad if some n in [n0-k, n0-1] has eta = v.  phases n0 mod P
            good = [n0 for n0 in range(P) if all(all(E[(n0 - i) % P] != v for i in range(1, k + 1)) for v, k, j in bad)]
            goodL = [n0 for n0 in range(P) if all(all(E[(n0 + i) % P] != v for i in range(0, k)) for v, k, j in bad)]
            print('  gam=%d delta=%2d bad=%s  good right-end phases %d/%d, left-end %d/%d' % (gam, delta, bad[:6], len(good), P, len(goodL), P))
