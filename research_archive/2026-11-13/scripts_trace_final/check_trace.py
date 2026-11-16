import mpmath as mp
from sympy import factorint
mp.mp.dps = 40

def beta(k, a):
    if k == 'inf':
        return mp.power(3, a/2) - 1
    return ((1 + mp.power(3, a/k))/2)**k - 1

def f(k, a):
    return (beta(k, a) + 2)/(1 + a)

stated = {1: '1.4967430', 2: '1.4295235', 3: '1.3986921', 4: '1.3807492', 5: '1.3689531',
          6: '1.3605886', 7: '1.3543412', 8: '1.3494942', 9: '1.3456226', 10: '1.3424580', 'inf': '1.3108172'}
for k in list(range(1, 11)) + ['inf']:
    # minimise by findroot on derivative, starting from grid minimum
    grid = [mp.mpf(i)/1000 for i in range(1, 5000)]
    a0 = min(grid, key=lambda a: f(k, a))
    a_star = mp.findroot(lambda a: mp.diff(lambda t: f(k, t), a), a0)
    x = f(k, a_star)
    s = mp.mpf(stated[k])
    print(k, 'a*=', mp.nstr(a_star, 10), 'x=', mp.nstr(x, 14), 'stated', stated[k], 'upper?', s >= x, 'slack', mp.nstr(s - x, 3))

# x_inf at the stated a
print('x_inf at a=1.5833613:', mp.nstr(f('inf', mp.mpf('1.5833613')), 14))
# monotonic decrease check
xs = []
for k in range(1, 41):
    xs.append(min(f(k, mp.mpf(i)/2000) for i in range(1000, 4000)))
print('decreasing 1..40 (grid):', all(xs[i] > xs[i+1] for i in range(len(xs)-1)))

# widths
P = lambda u: max(40, 8*u*u + 4)
c = 512*4*2*16*mp.mpf('2.08')
print('per-P factor', c, 'v4', c*40)
for U in ([1, 3], [1, 3, 5, 7, 13]):
    print(U, [P(u) for u in U], sum(P(u) for u in U)/40)

# margins at u=3 and the cubic
u = 3; D = 4*u*u + 1; Pu = P(u)
print('rigid2e', 1 + mp.mpf(D)/(8*u*(Pu-u) - D), 'Ladic', 1 + mp.mpf(u)/(2*Pu - 3*u), 'P1c', 1 + mp.mpf(D)/(4*u*(2*Pu-3*u) - 1))
print('gap coeff u=3', 4*(Pu - mp.mpf(u)/2), 'F2 denoms', [4*(P(v)-v) for v in (3, 5, 7, 13)], 'I.2', 8*u*(2*Pu-u))
bad = [v for v in range(3, 20001, 2) if not (64*v**3 - 112*v**2 + 32*v - 26 > 0 and P(v) > 14*v)]
print('cubic/Ladic failures odd 3..20000:', bad)
print('Prop4 heights', 420**2/(4*158), 420**2/(4*298))

# squarefree menu of squarefree_menus.md
menu = [1, 3, 5, 7, 11, 13, 15, 17, 21, 23, 25, 27]
facs = {v: factorint(4*v*v + 1) for v in menu}
print({v: facs[v] for v in menu})
print('all squarefree:', all(max(fc.values()) == 1 for fc in facs.values()))
primes = sorted({p for fc in facs.values() for p in fc})
rows = []
for v in menu:
    r = 0
    for i, p in enumerate(primes):
        if facs[v].get(p, 0) % 2:
            r |= 1 << i
    rows.append(r)
# F2 rank
basis = []
for r in rows:
    for b in basis:
        r = min(r, r ^ b)
    if r:
        basis.append(r)
print('F2 rank', len(basis), 'of', len(menu))
skipped = [v for v in range(1, 28, 2) if max(factorint(4*v*v+1).values()) > 1]
print('non-squarefree odd u <= 27:', skipped)
# Lemma MI menu from note: 1, 9, 113643
print('MI', [(v, factorint(4*v*v+1)) for v in (9, 113643)])
