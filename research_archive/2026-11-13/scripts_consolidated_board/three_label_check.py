"""Check the in-class {F,o,o,o} mixed-quadruple parametrisation, and the mod-64 kill.
Odd label points of one class: L(x) = (4x, 2x) + base, slots x = iota mod 32.
(alpha) side A,B and diagonal end C labels, D = F.  (beta) A = F, B and diagonal C, D labels.
Part 1: sympy identities.  Part 2: brute force from Lemma mixedeq on integer slots:
for every triple of slots (multiples of 32 apart) and every integer n, test the mixed-quadruple
equations directly, record F, and confirm row(F) - row_label = 0 (mod 64) whenever the triple
has the class residue (the base row is 2*iota+1 at slot iota)."""
import sympy as sp, itertools, math

a, b, c, d, t = sp.symbols('a b c d t', real=True)
L = lambda x: sp.Matrix([4 * x, 2 * x])
# alpha
A, B, C = L(a), L(b), L(c)
n = sp.Matrix([t, -2 * t])
D = A + B - C + 2 * n
e1 = sp.expand((n.T * (B - A))[0])
e2 = sp.expand(((D - C).T * (D - C))[0] - ((B - A).T * (B - A))[0])
print("alpha n.(B-A) =", e1, "; |D-C|^2-|B-A|^2 =", sp.factor(e2.subs(t**2, 4 * (c - a) * (b - c))))
# beta
P, Q = b - d, b - c
mu = -4 * P * Q / (P + Q)
nu2 = 4 * P * Q * (P - Q) ** 2 / (P + Q) ** 2
nu = sp.symbols('nu')
B2, C2, D2 = L(b), L(c), L(d)
nn = mu * sp.Matrix([2, 1]) + nu * sp.Matrix([1, -2])
F = C2 + D2 - B2 - 2 * nn
f1 = sp.simplify(((nn.T * (B2 - F))[0]).subs(nu**2, nu2))
f2 = sp.simplify((((D2 - C2).T * (D2 - C2))[0] - ((B2 - F).T * (B2 - F))[0]).subs(nu**2, nu2))
print("beta n.(B-F) =", f1, "; |D-C|^2-|B-F|^2 =", f2)

# Part 2: brute force over slots, iota = 0 base (label at slot x has point (4x, 2x+1))
def pt(x): return (4 * x, 2 * x + 1)
hits = 0; bad = 0
slots = [32 * k for k in range(0, 40)]
for (x1, x2, x3) in itertools.permutations(slots, 3):
    # alpha: A=pt(x1), B=pt(x2), C=pt(x3); D = A+B-C+2n, n integer perpendicular to B-A
    Ax, Ay = pt(x1); Bx, By = pt(x2); Cx, Cy = pt(x3)
    ux, uy = Bx - Ax, By - Ay
    g = math.gcd(ux, uy); px, py = -uy // g, ux // g
    for k in range(-400, 401):
        if k == 0: continue
        nx, ny = k * px, k * py
        Dx, Dy = Ax + Bx - Cx + 2 * nx, Ay + By - Cy + 2 * ny
        if (Dx - Cx) ** 2 + (Dy - Cy) ** 2 != ux * ux + uy * uy: continue
        if (Dx - Cx, Dy - Cy) in ((ux, uy), (-ux, -uy)): continue
        if Dx % 4: continue
        hits += 1
        if (Dy - 1) % 64 != 0: bad += 1
    # beta: B=pt(x1), C=pt(x2), D=pt(x3); F = C+D-B-2n, n.(B-F)=0, |D-C|=|B-F|
    Bx, By = pt(x1); Cx, Cy = pt(x2); Dx, Dy = pt(x3)
    P1x, P1y = Cx + Dx - Bx, Cy + Dy - By
    L2 = (Dx - Cx) ** 2 + (Dy - Cy) ** 2
    R = 60
    for nx in range(-R * 40, R * 40 + 1, 1):
        pass
print("alpha brute hits:", hits, " with row(F) != label row mod 64:", bad)

# beta brute: solve n from n.(B-P1) = -2|n|^2 and |B-P1|^2 - 4|n|^2 = |D-C|^2 over a box
hits = 0; bad = 0
for (x1, x2, x3) in itertools.permutations(slots[:24], 3):
    Bx, By = pt(x1); Cx, Cy = pt(x2); Dx, Dy = pt(x3)
    P1x, P1y = Cx + Dx - Bx, Cy + Dy - By
    wx, wy = Bx - P1x, By - P1y
    L2 = (Dx - Cx) ** 2 + (Dy - Cy) ** 2
    W2 = wx * wx + wy * wy
    if (W2 - L2) % 4: continue
    N2 = (W2 - L2) // 4          # |n|^2
    if N2 <= 0: continue
    r = math.isqrt(N2)
    for nx in range(-r, r + 1):
        rem = N2 - nx * nx
        s = math.isqrt(rem)
        if s * s != rem: continue
        for ny in {s, -s}:
            if nx * wx + ny * wy != -2 * N2: continue
            Fx, Fy = P1x - 2 * nx, P1y - 2 * ny
            # check the original equations from scratch
            Ax, Ay = Fx, Fy
            assert Cx + Dx == Ax + Bx + 2 * nx and Cy + Dy == Ay + By + 2 * ny
            assert nx * (Bx - Ax) + ny * (By - Ay) == 0
            assert (Dx - Cx) ** 2 + (Dy - Cy) ** 2 == (Bx - Ax) ** 2 + (By - Ay) ** 2
            if Fx % 4: continue
            hits += 1
            if (Fy - 1) % 64 != 0: bad += 1
print("beta brute hits:", hits, " with row(F) != label row mod 64:", bad)
