# Sanity checks for consolidated_board_v2 (residues and arithmetic only).
import math
# (1) Lemma S1L, residue form. Scaled coordinates: label A at 0, filler P = (a_P, 2 b_P),
# b_P = b0 + (a_P mod 4), b0 odd. Conditions: a_B^2 + 4 b_B^2 = d^2 + 4 e^2 (d = a_D - a_C,
# e = b_D - b_C) and (a_C + a_D - a_B) a_B + 4 (b_C + b_D - b_B) b_B = 0. Check mod 32.
M = 32
sol = 0
for b0 in range(1, M, 2):
    for aB in range(M):
        bB = b0 + aB % 4
        lhs = aB*aB + 4*bB*bB
        for aC in range(M):
            bC = b0 + aC % 4
            for aD in range(M):
                bD = b0 + aD % 4
                d = aD - aC; e = bD - bC
                if (lhs - d*d - 4*e*e) % M: continue
                if ((aC + aD - aB)*aB + 4*(bC + bD - bB)*bB) % M: continue
                sol += 1
print("S1L residue solutions mod 32:", sol)
# control: b0 even (wrong filler-row residue) should admit solutions
ctl = 0
for b0 in range(0, M, 2):
    for aB in range(M):
        bB = b0 + aB % 4; lhs = aB*aB + 4*bB*bB
        for aC in range(M):
            bC = b0 + aC % 4
            for aD in range(M):
                bD = b0 + aD % 4; d = aD - aC; e = bD - bC
                if (lhs - d*d - 4*e*e) % M == 0 and ((aC + aD - aB)*aB + 4*(bC + bD - bB)*bB) % M == 0:
                    ctl += 1
print("control (b0 even) residue solutions mod 32:", ctl)
# (2) seam all-row-g | Sea(3,g): rival pair C=(x,3), D=(x',g): 4j(g-3+j)=t^2, 1<=j<=2, g+j<=h.
bad = []
for h in range(424, 20001):
    g = h if h % 2 == 0 else (h - 1 if h % 4 == 1 else h - 3)
    for j in (1, 2):
        if g + j > h: continue
        v = 4*j*(g - 3 + j); r = math.isqrt(v)
        if r*r == v: bad.append((h, g, j))
print("g-row rival pairs for 424<=h<=20000:", len(bad))
# (3) exponent arithmetic
E = (1 + 3**0.91)/2
best = min((max(x, E + 1 - 0.91*x, 3 - x), x) for x in [i/10000 for i in range(10000, 25000)])
print("E(0.91)=%.4f; min exponent %.4f at x=%.4f; middle term at 1.5: %.4f" % (E, best[0], best[1], E + 1 - 0.91*1.5))
print("light width constant per unit B: %.4g" % (512*4*80*16*2.08))
print("x with sum c_T = O(h): %.4f" % ((E + 1)/1.91))
# (4) near-band depth needed for 1L3F label-on-side grid argument: y_L < T* - 72 - 2D
for D in (63, 114, 124, 184, 186):
    print("D=%d: need y_L < T* - %d" % (D, 72 + 2*D))
