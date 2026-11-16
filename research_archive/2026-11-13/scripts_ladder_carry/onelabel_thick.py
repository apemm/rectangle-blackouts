"""Thick (linear-in-depth) one-label/three-filler mixed quadruples in LAD_6(E').
Units: slot X (label slots X = 0 mod 64), depth eta (row = T* - 8 eta); metric X^2 + 4 eta^2.
Label L = C (diagonal), fillers A, B (side), D (diagonal).  With e = eta_B - eta_A != 0, S = k, c_s = eta_D - eta_A - eta_B,
rho = 2 eta_D - eta_A - eta_B, the square condition is identically satisfied in lam = eta_L iff k^2 + 4 rho^2 = 4 e^2.
Then G = -4 e (lam + c_s)/k and w_x = X_D - X_L = +-(4 rho lam / k + beta) (rho != 0) or +-2e (rho = 0, T1).
We test every such family against the layer over a full set of residues and report families with hits.
Each hit is re-checked against Lemma mixedeq directly.  Usage: py onelabel_thick.py Ep"""
import sys
from fractions import Fraction as Fr
from lad import eta_array

Ep = int(sys.argv[1]); E, P = eta_array(Ep)
eta = lambda X: int(E[X % P])
vals = sorted(set(E.tolist()))

def mixed_ok(A, B, C, D):
    # (X, eta) metric X^2 + 4 eta^2; Lemma mixedeq: u.(C+D-A-B) = 0, |D-C| = |B-A|, D-C != +-u, G != 0, sigma != 0
    G = B[0] - A[0]; e = B[1] - A[1]
    if G == 0: return False
    Sx = C[0] + D[0] - A[0] - B[0]; Sy = C[1] + D[1] - A[1] - B[1]
    if Sx == 0 and Sy == 0: return False
    if Sx * G + 4 * Sy * e != 0: return False
    wx = D[0] - C[0]; wy = D[1] - C[1]
    if wx * wx + 4 * wy * wy != G * G + 4 * e * e: return False
    if (wx, wy) in ((G, e), (-G, -e)): return False
    return len({A[0], B[0], C[0], D[0]}) == 4

fams = 0; hitfams = []
for eA in vals:
    for eB in vals:
        e = eB - eA
        if e == 0: continue
        for eD in vals:
            rho = 2 * eD - eA - eB; cs = eD - eA - eB
            r2 = 4 * e * e - 4 * rho * rho
            if r2 <= 0: continue
            k0 = int(round(r2 ** 0.5))
            if k0 * k0 != r2: continue
            for k in (k0, -k0):
                for sg in (1, -1):
                    fams += 1
                    if rho == 0:
                        al = Fr(0); be = Fr(2 * e)
                    else:
                        al = Fr(4 * rho, k); be = Fr(4 * e * e * cs, k * rho) + Fr(eD * k, rho)
                    hits = 0; ex = None
                    for lam in range(4000, 4000 + 2 * P * abs(k) * 16, 2):
                        G = Fr(-4 * e * (lam + cs), k)
                        wx = sg * (al * lam + be)
                        if G.denominator != 1 or wx.denominator != 1: continue
                        G = int(G); wx = int(wx)
                        twoXA0 = wx - k - G
                        if twoXA0 % 2: continue
                        for XL in range(0, P, 64):
                            XD = XL + wx; XA = XL + twoXA0 // 2; XB = XA + G
                            if eta(XD) == eD and eta(XA) == eA and eta(XB) == eB:
                                A = (XA, eA); B = (XB, eB); C = (XL, lam); D = (XD, eD)
                                if mixed_ok(A, B, C, D):
                                    hits += 1
                                    if ex is None: ex = (A, B, C, D)
                    if hits: hitfams.append((eA, eB, eD, k, sg, hits, ex))
print("E'=%d: candidate thick families %d, families with hits %d" % (Ep, fams, len(hitfams)))
for f in hitfams[:30]: print('  ', f)
