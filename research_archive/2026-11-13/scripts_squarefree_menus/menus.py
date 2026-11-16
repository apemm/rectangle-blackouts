# Greedy menus of odd u with 4u^2+1 squarefree and the 4u^2+1 independent modulo squares.
def factor(n):
    f = {}; d = 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
basis = []  # rows over GF(2), as sets of primes, in reduced form
def reduce(s):
    s = set(s)
    for b, piv in basis:
        if piv in s: s ^= b
    return s
menu = []; skipped_nonsq = []
u = 1
while len(menu) < 12:
    D = 4 * u * u + 1; f = factor(D)
    if all(e == 1 for e in f.values()):
        r = reduce(f.keys())
        if r:
            piv = max(r); basis.append((r, piv)); menu.append((u, D, sorted(f)))
    else:
        skipped_nonsq.append(u)
    u += 2
for m in menu: print(m)
print('non-squarefree odd u skipped:', skipped_nonsq[:10])
