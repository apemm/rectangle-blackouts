"""FFo triples (vertex V = filler, ends L = odd label point, F2 = filler) inside one class of a LAD region and their
W-collisions (V3).  (X, eta) units: slot X rel (class slots X = 0 mod 64), depth eta, row = T* - 8 eta, metric X^2 + 4 eta^2.
Right angle at V: (X_L - X_V) beta + 4 (eta_L - eta_V) e2 = 0, F2 = V + (beta, e2), W = L + (beta, e2).
Also reports W in a label column (fatal) and W equal to the filler of its column (fully black).
Usage: py ffo_v3.py h iota Tstar Ep"""
import sys, numpy as np
from collections import defaultdict
from lad import eta_array
h, iota, Ts, Ep = map(int, sys.argv[1:5]); E, P = eta_array(Ep)
vals = np.array(sorted(set(E.tolist())))
Dwin = 8 * int(vals.max()) + 24
labels = [(i - iota, (Ts - 2 * i - 1) / 8.0, i) for i in range(iota, (h - 1) // 2 + 1, 64) if 2 * i + 1 < Ts - Dwin - 128]
labslots = {X for X, _, _ in labels}
Wmap = defaultdict(list); ntri = 0; nlab = 0; nblack = 0
for XL, etaL, i in labels:
    if etaL != int(etaL): continue
    etaL = int(etaL)
    R = 4 * etaL * int(vals.max()) + 8
    al = np.arange(-R, R + 1, dtype=np.int64)
    al = al[al != 0]
    XV = XL - al
    eV = E[XV % P]
    for e2v in vals:
        e2 = e2v - eV
        num = -4 * (etaL - eV) * e2
        ok = (e2 != 0) & (num % al == 0)
        beta = np.where(ok, num // np.where(al == 0, 1, al), 0)
        ok &= (beta != 0) & (E[(XV + beta) % P] == e2v) & ((XV % 64) != 0) & (((XV + beta) % 64) != 0)
        for q in np.nonzero(ok)[0]:
            b = int(beta[q]); ee = int(e2[q])
            XW = XL + b; etaW = etaL + ee
            if not (Ts - 8 * etaW >= 1): continue
            ntri += 1
            if XW % 64 == 0 and XW in labslots: nlab += 1
            if XW % 64 != 0 and int(E[XW % P]) == etaW: nblack += 1
            Wmap[(XW, etaW)].append((i, int(XV[q]), b, ee))
coll = {k: v for k, v in Wmap.items() if len(v) > 1}
print('h=%d iota=%d: FFo triples %d, W in a label column %d, fully black %d, W with >=2 triples %d' % (h, iota, ntri, nlab, nblack, len(coll)))
for k, v in list(coll.items())[:5]: print('  W', k, v)
