"""Cyclic block rule xi_r = (c*floor((r+phi)/g) + kappa) mod M.
(1) brute-force check of the rule on random rank sets for random two-gap M=3 systems it claims to solve;
(2) coverage of the uncovered class (a even, v2(b)<=v2(a), v2(b+1)<=v2(a)) by the rule's criterion:
    exists g | a with 3 not dividing a/g and floor(b/g) not congruent to 1 mod 3."""
import random
from lists import slots

def v2(n):
    if n == 0:
        return 10**9
    k = 0
    while n % 2 == 0:
        n //= 2; k += 1
    return k

def crit(a, b):
    for g in range(1, a + 1):
        if a % g == 0 and (a // g) % 3 != 0 and (b // g) % 3 != 1:
            return g
    return None

random.seed(7)
viol = 0; tested = 0; used = 0
for trial in range(3000):
    a = random.randint(1, 40); b = random.randint(0, 120); s = random.choice([1, 2])
    g = crit(a, b)
    if g is None:
        continue
    n = b // g
    # choose c in {1,2} with {n, n+1} not containing c*s mod 3
    c = next(c for c in (1, 2) if (c * s) % 3 not in (n % 3, (n + 1) % 3))
    used += 1
    phi = random.randint(0, 99); kap = random.randint(0, 2)
    ranks = sorted(random.sample(range(-200, 400), 150)); rs = set(ranks)
    xi = {r: (c * ((r + phi) // g) + kap) % 3 for r in ranks}
    for q in (3 * a, 3 * b + s):
        for d, de in slots(q, 3):
            for r in ranks:
                if r + d in rs:
                    tested += 1
                    viol += (xi[r + d] - xi[r] == de)
print("(1) systems", used, "constraints", tested, "violations", viol)

unc = 0; left = []
for a in range(2, 201, 2):
    al = v2(a)
    for b in range(0, 1001):
        if v2(b) > al or v2(b + 1) > al:
            continue
        unc += 1
        if crit(a, b) is None:
            left.append((a, b))
print("(2) uncovered pairs a<=200 even, b<=1000:", unc, " not covered by cyclic rule:", len(left))
print("   first few:", left[:40])
