"""Check the 2-adic local criterion for S5 (cross-block even-even A2 pairs).

A2: 4 delta^2 + eps^2 = L'^2, eps = Dj, Dn = eps - delta.
Claim: with d = v2(eps), a = v2(Dn): solutions exist only if a = d or a <= d - 3.
Also tabulate which (d, a) occur, for eps, delta = 0 mod 16, eps != 0, delta != 0.
Second check (l-adic, Prop 1(d)): no solution has l | Dn with (5/l) = -1, l > |eps|.
"""
import math
from collections import Counter

def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c

seen = Counter(); bad = 0; n = 0
EMAX = 4000
for e in range(16, EMAX, 16):
    E2 = e*e
    # 4 delta^2 + e^2 = L'^2  <=>  (L'-2delta)(L'+2delta) = e^2 ; f1 = L'-2delta
    for f1 in range(1, e + 1):
        if E2 % f1: continue
        g = E2 // f1
        if (g - f1) % 4: continue
        delta = (g - f1) // 4
        if delta == 0 or delta % 16: continue
        for dl in (delta, -delta):
            for ee in (e, -e):
                Dn = ee - dl
                n += 1
                d = v2(abs(ee)); a = v2(abs(Dn)) if Dn else 99
                seen[(d, min(a, 12))] += 1
                if not (a == d or a <= d - 3): bad += 1
print("solutions:", n, "violations of criterion:", bad)
for d in range(4, 12):
    row = {a: seen[(d, a)] for a in range(0, 13) if seen[(d, a)]}
    if row: print("v2(eps) =", d, " v2(Dn) counts:", row)
# l-adic check
def isprime(m):
    if m < 2: return False
    for q in range(2, int(m**0.5)+1):
        if m % q == 0: return False
    return True
viol = 0; tested = 0
for e in range(16, 2000, 16):
    E2 = e*e
    for f1 in range(1, e+1):
        if E2 % f1: continue
        g = E2 // f1
        if (g - f1) % 4: continue
        delta = (g - f1)//4
        if delta == 0 or delta % 16: continue
        for dl in (delta, -delta):
            Dn = e - dl
            for l in range(e+1, 2*e+3):
                if l % 5 in (2, 3) and isprime(l):
                    tested += 1
                    if Dn % l == 0: viol += 1
print("l-adic: (solution, l) pairs tested:", tested, "with l | Dn:", viol)
