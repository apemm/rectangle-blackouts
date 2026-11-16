"""Mixed class / non-class four-filler quadruples of LAD_6(E').  By the r-lemma the class points of a
quadruple are all four (strip theorem: impossible) or a nonempty subset of {A,D} or of {B,C}; quadruples
with no class point are E'-independent and excluded by 'quad4.py lad 0'.  This searches only the mixed combos."""
import sys, numpy as np
from numba import njit
from quad4 import spf_sieve, divisors, isqrt
from lad import eta_array

@njit(cache=False)
def search_mix(E, P, vals, iscl, spf):
    nv = len(vals)
    res = np.zeros((nv, P), dtype=np.int64); nres = np.zeros(nv, dtype=np.int64)
    for a in range(P):
        for k in range(nv):
            if E[a] == vals[k]:
                res[k, nres[k]] = a; nres[k] += 1
    no = 0; dv = np.zeros(40000, dtype=np.int64); ncombo = 0
    for iA in range(nv):
        for iB in range(nv):
            e = vals[iB] - vals[iA]
            if e == 0: continue
            for iC in range(nv):
                for iD in range(nv):
                    cA = iscl[iA]; cB = iscl[iB]; cC = iscl[iC]; cD = iscl[iD]
                    ok = ((cA or cD) and not cB and not cC) or ((cB or cC) and not cA and not cD)
                    if not ok: continue
                    ncombo += 1
                    al = vals[iC] - vals[iA]; be = vals[iD] - vals[iB]
                    s = al + be
                    if s == 0: continue
                    V = al - be; K = -4 * e * s
                    nd = divisors(abs(K), spf, dv)
                    for k in range(nd):
                        for sg in range(2):
                            G = dv[k] if sg == 0 else -dv[k]
                            Sp = K // G
                            Rq = G * G + 4 * V * (2 * e - V)
                            r = isqrt(Rq)
                            if r < 0 or r * r != Rq: continue
                            for rs in range(2):
                                if rs == 1 and r == 0: continue
                                U = G - r if rs == 0 else G + r
                                if (Sp - U) % 2 != 0: continue
                                d1 = (Sp + U) // 2; d2 = (Sp - U) // 2
                                if d1 == 0 or d2 == 0 or d1 == G or G + d2 == 0 or G - U == 0: continue
                                if (U == 0 and V == 0) or (U == 2 * G and V == 2 * e): continue
                                for t in range(nres[iA]):
                                    a = res[iA, t]
                                    if E[(a + d1) % P] == vals[iC] and E[(a + G) % P] == vals[iB] and E[(a + G + d2) % P] == vals[iD]:
                                        no += 1
    return no, ncombo

for Ep in map(int, sys.argv[1:]):
    E, P = eta_array(Ep)
    vals = np.array(sorted(set(E.tolist())), dtype=np.int64)
    iscl = np.array([v % 64 == 3 for v in vals], dtype=np.bool_)
    H = int(vals.max() - vals.min())
    spf = spf_sieve(8 * H * H + 10)
    no, nc = search_mix(E, P, vals, iscl, spf)
    print("E'=%d P=%d class rows %d: mixed combos %d, quadruples %d" % (Ep, P, int(iscl.sum()), nc, no))
