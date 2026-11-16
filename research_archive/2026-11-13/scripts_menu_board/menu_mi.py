"""Sanity check of Lemma MI (independent menus of every size) and of the
three thin-margin conditions at P_u = max(40, 8u^2 + 4)."""
from sympy import factorint, isprime, sqrt_mod
from fractions import Fraction as Fr

def sqf_vec(n):
    return frozenset(p for p, e in factorint(n).items() if e % 2)

def independent(deltas):
    # Gaussian elimination over F_2 on squarefree-part vectors
    rows = [set(sqf_vec(d)) for d in deltas]
    basis = {}
    for r in rows:
        r = set(r)
        while r:
            piv = max(r)
            if piv in basis:
                r ^= basis[piv]
            else:
                basis[piv] = r
                break
        else:
            return False
    return True

def next_u(prev_deltas):
    D = max(prev_deltas) if prev_deltas else 1
    q = D + 1
    while not (isprime(q) and q % 4 == 1):
        q += 1
    x = sqrt_mod(-1, q)
    u0 = (x * pow(2, -1, q)) % q
    for k in range(q):
        u = u0 + k * q
        if (4 * u * u + 1) % (q * q) != 0:
            # make u odd by CRT with mod 2: add q*q if needed (q*q odd)
            if u % 2 == 0:
                u += q * q
            assert (4 * u * u + 1) % q == 0 and (4 * u * u + 1) % (q * q) != 0
            return u, q
    raise RuntimeError

menu, deltas = [], []
for m in range(1, 4):
    u, q = next_u(deltas)
    menu.append(u); deltas.append(4 * u * u + 1)
    print(m, "u =", u, "q =", q, "independent:", independent(deltas))

print("U5 = {1,3,5,7,13} independent:", independent([4*u*u+1 for u in (1,3,5,7,13)]))
print("{1,9} independent (325 = 5^2*13):", independent([5, 325]))
print("{1,9,?}: 5*13 vs 65 -> u with 4u^2+1 = 65 is u=4 (even), skip")

bad = []
for u in range(1, 400, 2):
    P = max(40, 8 * u * u + 4); Dl = 4 * u * u + 1
    r1 = 1 + Fr(Dl, 8 * u * (P - u) - Dl)          # rigid 2(e)
    r2 = 1 + Fr(u, 2 * P - 3 * u)                   # L-adic, Fee
    r3 = 1 + Fr(Dl, 4 * u * (2 * P - 3 * u) - 1)    # Prop 1(c)
    if max(r1, r2, r3) >= Fr(104, 100):
        bad.append(u)
    if u in (1, 3, 5):
        print(u, float(r1), float(r2), float(r3))
print("odd u < 400 with a margin >= 1.04:", bad)
