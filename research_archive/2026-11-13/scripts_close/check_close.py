# Sanity checks for the stride-4u closure (analytic proofs are primary).
from math import gcd
import sys

def riv_bruteforce(u, al, be, emax):
    # smallest e>0 (and all e<=emax) with n1=2al e/be, v=al e F/(4be^2 D0), z=-v be/al all integers
    F = 4*(al-2*u*be)**2 + be**2
    D0 = u*be - al
    sols = []
    for e in range(be, emax+1, be):
        if (2*al*e) % be: continue
        num = al*e*F; den = 4*be*be*D0
        if num % den: continue
        v = num//den
        if (v*be) % al: continue
        # check (I1),(I2) with Delta=4ue, n1, w, u2=2v
        n1 = 2*al*e//be; Delta = 4*u*e; z = -(v*be)//al; w = -z - Delta
        assert e*(2*v) == n1*(Delta + w)
        assert (Delta - 2*n1)*w == e*e + n1*n1
        sols.append((v, e))
    return F, D0, sols

bad = 0; checked = 0; bad_table = 0
for u in (1, 3, 5):
    for be in range(1, 22, 2):
        for al in range(1, u*be, 2):
            if gcd(al, be) != 1: continue
            D0 = u*be - al
            F, D0, sols = riv_bruteforce(u, al, be, 4*be*be*D0*3)
            g = gcd(F, D0)
            q = al*F//g; p = (al*F + 4*be*be*D0)//g
            gT = gcd(al*F, 4*be*be*D0)
            pred = [(q*m, (p-q)*m) for m in range(1, 4)]
            checked += 1
            if sols[:3] != pred:
                bad += 1
                if bad < 5: print("mismatch", u, al, be, sols[:3], pred)
            if gT != g: bad_table += 1
            assert g % 1 == 0 and (4*u*u+1) % g == 0, (u, al, be, g)
            # Lemma IV(u) bounds
            assert q > al*be*be or (u == 1 and q >= al*be*be)
            assert 4*u*be**3 <= p*(4*u*u+1)
            assert p <= (128*u**3/27 + 4*u)*be**3 + 1e-9
print("R_IV(u): pairs checked", checked, "formula mismatches", bad, "pairs where table g differs", bad_table)

def gUV(u, a, b):
    U = (a-4*u*b)*(a*a+b*b); V = a**3 - 4*u*a*a*b - 3*a*b*b + 4*u*b**3
    return U, V
for u in (1, 3, 5, 7, 9):
    M = 8*u*(4*u*u+1); worst = 0
    for b in range(1, 120):
        for a in range(-600, 601):
            if gcd(a, b) != 1: continue
            U, V = gUV(u, a, b)
            if U == 0: continue
            G = gcd(U, V)
            if M % G: print("gcd fail", u, a, b, G); sys.exit()
    print("gcd(U_u,V_u) | 8u(4u^2+1) on box, u =", u)

# exponent x_m
def xm(m):
    best = 10
    a = 0.0005
    while a < 4:
        val = (((1+3**(a/m))/2)**m + 1)/(1+a)
        best = min(best, val); a += 0.0005
    return best
print("x_1 =", round(xm(1), 6), " x_2 =", round(xm(2), 6))
