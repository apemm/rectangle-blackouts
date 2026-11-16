"""Exact checks of the three M=3 two-gap formulas and the shift (mod-3) property.
System: xi in {0,1,2}; (C0) xi[r+a]!=xi[r]; (C1) xi[r+b]-xi[r]!=s (b>=1); (C2) xi[r+b+1]-xi[r]!=s-3.
'Mod-3 certified' means the differences avoid delta modulo 3 (so every shift by kappa mod 3 also works).
All rules are periodic with period P; checking r in [0,P) covers all of Z."""
import math, sys
from fractions import Fraction

def v(p, n):
    if n == 0: return 99
    k = 0
    while n % p == 0: n //= p; k += 1
    return k

def check(rule, P, a, b, s, mod3=False):
    cons = [(a, 0)]
    if b >= 1: cons.append((b, s))
    cons.append((b + 1, s - 3))
    for r in range(P):
        for d, dl in cons:
            diff = rule(r + d) - rule(r)
            if mod3:
                if diff % 3 == dl % 3: return False
            else:
                if diff == dl: return False
    return True

def block_combine(a, b, s):
    w = v(3, a); h = 3 ** w
    g = h if (b // h) % 3 != 1 else 2 * h
    n = b // g
    assert n % 3 != 1
    c = 3 - s if n % 3 == 0 else s
    return (lambda r: (c * (r // g)) % 3), 3 * g

def block_search(a, b, s):
    w = v(3, a); h = 3 ** w
    g = 2 * h if (b // (2 * h)) % 3 != 1 else h
    B = b // g
    c = (s * (B + 2)) % 3
    assert c in (1, 2)
    return (lambda r: (c * (r // g)) % 3), 3 * g

def beatty(a, b, s):
    eps = 1 if s == 2 else -1
    if b <= a - 1: th = Fraction(1, a)
    elif b <= 2 * a: th = Fraction(-2, b)
    elif b <= 3 * a - 1: th = Fraction(-3, b + 1)
    else:
        m = -(-b // (3 * a)); th = Fraction(3 * m, b)
    t = eps * th
    P = 3 * t.denominator
    return (lambda r: math.floor(t * r) % 3), P

def odd_binary(a, b, s):
    t = s if b % 2 == 0 else 3 - s
    return (lambda r: t * (r % 2)), 2

if __name__ != '__main__':
    sys.argv = [sys.argv[0], '0', '0']
bad = {'combine': 0, 'search': 0, 'beatty': 0, 'oddbin': 0, 'combine_mod3': 0, 'beatty_mod3': 0}
cnt = 0
AMAX, BMAX = int(sys.argv[1]), int(sys.argv[2])
for a in range(1, AMAX + 1):
    for b in range(0, BMAX + 1):
        for s in (1, 2):
            cnt += 1
            if a % 2 == 0:
                f, P = block_combine(a, b, s)
                if not check(f, P, a, b, s): bad['combine'] += 1
                if not check(f, P, a, b, s, True): bad['combine_mod3'] += 1
                f, P = block_search(a, b, s)
                if not check(f, P, a, b, s): bad['search'] += 1
            else:
                f, P = odd_binary(a, b, s)
                if not check(f, P, a, b, s): bad['oddbin'] += 1
            if a >= 2:
                f, P = beatty(a, b, s)
                if not check(f, P, a, b, s): bad['beatty'] += 1
                if not check(f, P, a, b, s, True): bad['beatty_mod3'] += 1
print('triples', cnt, 'failures', bad)
