"""Structural statistics of the twisted L***(3) over all 512 types (no obstruction search).
usage: py stats12t.py h
(a) primes: (37/l) = (37/p) = -1, p = 3 mod 4, ranges; (37/l) = (l/37) (reciprocity check);
(b) slot injectivity per type; every label slot n = rho_tau := 3(iota + sigma) (mod 16);
(c) (C7): (n - 3j) mod 16l takes one value per type (twisted), versus the untwisted rule on the same classes;
(d) least column gap between two subclasses of one type versus 2W_h + 1; Delta t = 0 (mod 16);
(e) same classes as the untwisted build (lstar12.build_type12): identical (s, colour, label set) lists;
(f) rho0 differs from the untwisted rho0 exactly on the types with sigma odd."""
import sys, time
from collections import Counter
from lstar12 import params, build_type12, primes12
from lstar12t import build_type12t, primes12t, legendre, slot

h = int(sys.argv[1]); t0 = time.time()
P = params(h); W = P['W']
l, p = primes12t(h); lu, pu = primes12(h)
print('h', h, 'B', P['B'], 'twisted l p', l, p, '(37/l)', legendre(37, l), '(l/37)', legendre(l, 37),
      '(37/p)', legendre(37, p), 'p mod 4', p % 4, 'l/h %.4f p/h %.3f' % (l / h, p / h), '| untwisted l p', lu, pu,
      '(37/pu)', legendre(37, pu), '(37/lu)', legendre(37, lu))
badmod = collide = 0; c7_tw = Counter(); c7_un = Counter(); mingap = None; dt16 = 0; same = 0; diff = 0
phase_diff = Counter(); nlab = 0; heavy = 0; edges = 0
for iota in range(32):
    for sigma in range(16):
        Rt = build_type12t(h, iota, sigma, 'board', 'relaxed')
        Ru = build_type12(h, iota, sigma, 'board', 'relaxed')
        ka = [(sc['s'], sc['colour'], tuple(sc['labels'])) for sc in Rt['subs']]
        kb = [(sc['s'], sc['colour'], tuple(sc['labels'])) for sc in Ru['subs']]
        same += ka == kb; diff += ka != kb
        heavy += len(Rt['heavy']); edges += Rt['nedges']
        rt = (3 * (iota + sigma)) % 16
        slots = {}; v_tw = set(); v_un = set(); tv = []
        for sc, su in zip(Rt['subs'], Ru['subs']):
            for (i, j) in sc['labels']:
                n = slot(i, sc['t'], p); nu = slot(i, su['t'], pu)
                nlab += 1
                badmod += (n - rt) % 16 != 0
                collide += n in slots; slots[n] = 1
                v_tw.add((n - 3 * j) % (16 * l)); v_un.add((nu - 3 * j) % (16 * lu))
                phase_diff[(sigma % 2, (n - nu) % 4)] += 1
            if sc['labels']:
                tv.append(sc['t'])
        c7_tw[len(v_tw)] += 1; c7_un[len(v_un)] += 1
        tv.sort()
        for a, b in zip(tv, tv[1:]):
            dt16 += (b - a) % 16 != 0
            g = 4 * p * (b - a) - 12 * (P['A'] - 1)
            mingap = g if mingap is None else min(mingap, g)
print('labels', nlab, 'mod-16 failures', badmod, 'slot collisions', collide, 'heavy', heavy, 'G_T edges', edges)
print('(C7) #values of (n-3j) mod 16l per type: twisted', dict(c7_tw), ' untwisted', dict(c7_un))
print('class lists identical to untwisted build:', same, 'types; different:', diff)
print('Delta t not = 0 mod 16:', dt16, '; least subclass gap', mingap, 'vs 2W+1', 2 * W + 1, 'ratio %.1f' % (mingap / (2 * W + 1)))
print('(sigma mod 2, (n_tw - n_untw) mod 4) counts:', dict(sorted(phase_diff.items())))
print('time %.1f' % (time.time() - t0))
