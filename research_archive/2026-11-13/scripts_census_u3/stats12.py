"""Structural statistics of L***(3) over all 512 types (no obstruction search).
usage: py stats12.py h
Checks: (a) slot map injective on each type and every label slot n = rho_tau (mod 16), rho_tau = 3 iota + sigma;
(b) least column gap between two subclasses of one type, against 2 W_h + 1;
(c) heavy diagonals (kappa_T >= B/4) at stride 12 and, for comparison, at stride 4;
(d) edges of G_T[tau], class sizes in 'board' and 'stress' colourings; survivors under 'exact'."""
import sys, time
from collections import Counter
from lstar12 import params, primes12, build_type12, slot
from lstar import diag_graph

h = int(sys.argv[1]); t0 = time.time()
P = params(h); l, p = primes12(h); W = P['W']
print('h', h, 'B', P['B'], 'B/4', P['B'] / 4, 'l', l, 'p', p, 'p/h %.3f' % (p / h), '2W+1', 2 * W + 1)
heavy12 = set(); heavy4 = set(); edges = 0; sizes_b = Counter(); sizes_s = Counter(); surv = 0; survtypes = 0
mingap = None; labels_relaxed = 0; badmod = 0; collide = 0; surv_sizes = Counter()
for iota in range(32):
    for sigma in range(16):
        R = build_type12(h, iota, sigma, 'board', 'relaxed')
        for (T, kT, nv) in R['heavy']:
            heavy12.add(T)
        edges += R['nedges']
        rt = (3 * iota + sigma) % 16
        slots = {}
        tvals = sorted(set(sc['t'] for sc in R['subs'] if sc['labels']))
        for sc in R['subs']:
            if sc['labels']:
                sizes_b[len(sc['labels'])] += 1
            for (i, j) in sc['labels']:
                n = slot(i, sc['t'], p)
                labels_relaxed += 1
                badmod += (n - rt) % 16 != 0
                collide += n in slots
                slots[n] = (i, j)
        for a, b in zip(tvals, tvals[1:]):
            g = 4 * p * (b - a) - 12 * (P['A'] - 1)
            mingap = g if mingap is None else min(mingap, g)
        Rs = build_type12(h, iota, sigma, 'stress', 'relaxed')
        for sc in Rs['subs']:
            if sc['labels']:
                sizes_s[len(sc['labels'])] += 1
        Re = build_type12(h, iota, sigma, 'board', 'exact')
        k = sum(len(sc['labels']) for sc in Re['subs'])
        surv += k; survtypes += k > 0
        for sc in Re['subs']:
            if sc['labels']:
                surv_sizes[len(sc['labels'])] += 1
for s in range(-P['A'] + 1, P['K']):
    I, D = diag_graph(h, s)
    if I and 4 * len(D) >= P['B']:
        heavy4.add(2 * s + 1)
print('relaxed labels', labels_relaxed, 'slot mod-16 failures', badmod, 'slot collisions', collide)
print('least subclass column gap (lower bound 4p dt - 12(A-1))', mingap, 'vs 2W+1', 2 * W + 1, 'ok', mingap is None or mingap > 2 * W + 1)
print('heavy diagonals stride 12:', len(heavy12), sorted(heavy12)[:40])
print('heavy diagonals stride 4 :', len(heavy4), sorted(heavy4)[:40])
print('edges of G_T[tau] (all types, stride 12):', edges)
print('board class sizes', dict(sorted(sizes_b.items())), 'stress class sizes', dict(sorted(sizes_s.items())))
print('exact survivors', surv, 'in', survtypes, 'types; survivor class sizes', dict(sorted(surv_sizes.items())))
print('time %.1f' % (time.time() - t0))
