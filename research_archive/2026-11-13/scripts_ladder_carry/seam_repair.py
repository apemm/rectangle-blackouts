"""Seam repair search.  For each buffer gap gam = h - g in {0,1,3} and each delta0 = h - T* in [0,63] (parity: T* odd,
so delta0 = h - T* has the parity of h + 1; gam = 0 needs h even, gam in {1,3} needs h odd), try T* -> T* - 64k (k = 0..3).
A choice is good if some right-end phase and some left-end phase avoid every seam mixed quadruple (d) and every seam
rival pair (e).  Usage: py seam_repair.py Ep"""
import sys
from lad import eta_array
Ep = int(sys.argv[1]); E, P = eta_array(Ep)
vals = sorted(set(E.tolist()))
def divpairs(n):
    n0 = abs(n); out = []; d = 1
    while d * d <= n0:
        if n0 % d == 0:
            for x in {d, n0 // d}:
                for sx in (1, -1): out.append((sx * x, n // (sx * x)))
        d += 1
    return out
cache = {}
def dbad(t0):
    if t0 in cache: return cache[t0]
    badR = set(); badL = set()
    for Q1 in range(P):
        s1 = t0 - 8 * int(E[Q1])
        for v2 in vals:
            m = ((t0 - 8 * v2) - s1) // 8
            if m == 0: continue
            for X, Y in divpairs(m * (s1 + 4 * m)):
                if (X + Y) % 2: continue
                a = (X + Y) // 2; c = (Y - X) // 2
                if a == 0 or (m * s1) % (2 * a): continue
                t = -m * s1 // (2 * a) - X
                if t % 2: continue
                Dl = t // 2
                if E[(Q1 + Dl) % P] != v2: continue
                if a < 0 and c < 0 and c < Dl < -a:
                    lo = Q1 + max(0, Dl); hi = Q1 + min(-a, Dl - c)
                    for z in range(lo + 1, min(hi, lo + P) + 1): badR.add(z % P)
                if a > 0 and c > 0 and -a < Dl < c:
                    lo = Q1 + max(-a, Dl - c); hi = Q1 + min(0, Dl)
                    for z in range(lo + 1, min(hi, lo + P) + 1): badL.add(z % P)
    cache[t0] = (badR, badL); return cache[t0]
def ebad(gam, delta):
    bad = []
    for v in vals:
        hc = delta + 8 * v; gc = hc - gam
        for j in range(1, 4):
            if gc > 0:
                if j > gam: continue
                q = j * (gc + j)
            elif gc < 0:
                if j > hc: continue
                q = j * (-gc + j)
            else: continue
            if q % 4: continue
            k2 = q // 4; k = int(round(k2 ** 0.5))
            if k >= 1 and k * k == k2: bad.append((v, k))
    badR = {n0 for n0 in range(P) if any(any(E[(n0 - i) % P] == v for i in range(1, k + 1)) for v, k in bad)}
    badL = {n0 for n0 in range(P) if any(any(E[(n0 + i) % P] == v for i in range(0, k)) for v, k in bad)}
    return badR, badL
worst = 0; fails = []
for gam in (0, 1, 3):
    for delta0 in range(0, 64):
        if gam == 0 and delta0 % 2 == 0: continue      # h even, T* odd -> delta odd
        if gam != 0 and delta0 % 2 == 1: continue      # h odd -> delta even
        ok = None
        for k in range(int(sys.argv[2]) if len(sys.argv) > 2 else 4):
            delta = delta0 + 64 * k; t0 = gam - delta
            dR, dL = dbad(t0); eR, eL = ebad(gam, delta)
            gR = P - len(dR | eR); gL = P - len(dL | eL)
            if gR > 0 and gL > 0: ok = (k, gR, gL); break
        if ok is None: fails.append((gam, delta0))
        else: worst = max(worst, ok[0])
        if ok is None or ok[0] > 0: print('gam=%d delta0=%2d -> %s' % (gam, delta0, ok))
print("E'=%d: largest T* shift needed (units of 64 rows): %d; unrepaired (gam, delta0): %s" % (Ep, worst, fails))
