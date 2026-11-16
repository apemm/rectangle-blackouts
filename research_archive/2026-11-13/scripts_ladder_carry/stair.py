"""Check the staircase property of LAD: for every filler pair, d_eta = 0 (then v2(gap) >= 2) or v2(d_eta) = v2(gap).
(rows differ by 8*d_eta, so v2(dy) = 3 + v2(d_eta)).  Over all pairs a in one period, gap in 1..2P."""
import sys
from lad import eta_array, v2
for Ep in range(0, int(sys.argv[1]) + 1):
    E, P = eta_array(Ep)
    bad = 0; vals = sorted(set(E.tolist()))
    for a in range(P):
        for g in range(1, 2 * P):
            de = int(E[(a + g) % P] - E[a])
            if de == 0:
                if v2(g) < 2: bad += 1
            elif v2(de) != v2(g): bad += 1
    print("E'=%d P=%d bad=%d  eta values (%d): max %d" % (Ep, P, bad, len(vals), max(vals)))
