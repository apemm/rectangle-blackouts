# Sanity checks for the (M10) audit. Exact or 50-digit arithmetic only.
from math import gcd
try:
    import mpmath as mp
    mp.mp.dps = 50
except ImportError:
    mp = None

def f(a, k):
    three = mp.mpf(3)
    if k == 'inf':
        beta = three ** (a / 2) - 1
    else:
        beta = ((1 + three ** (a / k)) / 2) ** k - 1
    return (beta + 2) / (1 + a)

stated = {1: '1.4967430', 2: '1.4295235', 3: '1.3986921', 4: '1.3807492', 5: '1.3689531',
          6: '1.3605886', 7: '1.3543412', 8: '1.3494942', 9: '1.3456226', 10: '1.3424580',
          'inf': '1.3108172'}
for k in list(range(1, 11)) + ['inf']:
    g = lambda a: mp.diff(lambda t: f(t, k), a)
    a0 = mp.findroot(g, 1.0)
    x = f(a0, k)
    ok = x < mp.mpf(stated[k])
    print(k, 'a*=', mp.nstr(a0, 12), 'x=', mp.nstr(x, 14), 'stated', stated[k], 'upper' if ok else 'NOT UPPER')
# theta* truncation check
x1 = f(mp.findroot(lambda a: mp.diff(lambda t: f(t, 1), a), 1.0), 1)
print('x1 > 1.4967429 ?', x1 > mp.mpf('1.4967429'))

# G11: density of {k in Z : M | d0 - 64k} is gcd(64,M)/M or 0; compare with v3's m = M/gcd(2,M)
bad_draft = 0; mism = 0
for M in range(1, 5001):
    m = M // gcd(2, M)
    if gcd(32, m) * M != gcd(64, M) * m:
        mism += 1
    # draft reading with v3's m: gcd(64,m)/m <= 64/M ?
    if gcd(64, m) * M > 64 * m:
        bad_draft += 1
    # brute density over one period for a few d0 (even depths)
    for d0 in (0, 2, 64, 6):
        cnt = sum(1 for k in range(M) if (d0 - 64 * k) % M == 0)
        assert cnt * M <= gcd(64, M) * M  # cnt/M <= gcd(64,M)/M
print('v3 identity gcd(32,m)/m == gcd(64,M)/M mismatches:', mism)
print('M <= 5000 where gcd(64,m)/m > 64/M with v3 m:', bad_draft, '(first:', next(M for M in range(1,5001) if gcd(64, M//gcd(2,M))*M > 64*(M//gcd(2,M))), ')')

# Width factors
P = lambda u: max(40, 8 * u * u + 4)
print('per-P factor', 4 * 2 * 16 * 2.08 * 512, ' at P=40:', 4 * 2 * 16 * 2.08 * 512 * 40)
for U in ([1, 3], [1, 3, 5, 7, 13]):
    print(U, sum(P(u) for u in U) / 40)

# Lemma MI with u_1 = 1: next q = 1 mod 4 prime > max Delta, root of 4u^2+1 mod q, non-root lift mod q^2, odd.
def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
U = [1]; qs = [5]
for step in range(2):
    D = max(4 * u * u + 1 for u in U)
    q = D + 1
    while not (q % 4 == 1 and isprime(q)): q += 1
    u0 = next(x for x in range(q) if (4 * x * x + 1) % q == 0)
    for t in range(q):
        c = u0 + q * t
        if (4 * c * c + 1) % (q * q) != 0:
            break
    if c % 2 == 0: c += q * q
    U.append(c); qs.append(q)
for u, q in zip(U, qs):
    Dl = 4 * u * u + 1
    v = 0; n = Dl
    while n % q == 0: n //= q; v += 1
    print('u', u, 'Delta', Dl, 'q', q, 'v_q', v, 'q divides earlier:', [ (4*w*w+1) % q == 0 for w in U if w < u])

# Thin-margin polynomial 64u^3 - 112u^2 + 32u - 26 > 0 for odd u >= 3 (analytic; spot check)
print(all(64*u**3 - 112*u**2 + 32*u - 26 > 0 for u in range(3, 2001, 2)))
