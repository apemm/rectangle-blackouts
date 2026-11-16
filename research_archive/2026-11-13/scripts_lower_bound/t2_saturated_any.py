"""Sanity check.  Parity bipartition (odd rows against even rows), any h >= 4, q = floor(h^2/4).
Is there a saturated board in which no 45-degree rectangle of the board has >= 3 black corners?
Each bishop class is a function with one cell per column; enumerate both classes, then pair them.
usage: py t2_saturated_any.py h [seconds]
"""
import sys, time
from class_functions import run

def main(h, tl):
    q = h * h // 4
    n_odd = (h + 1) // 2; n_even = h // 2
    deg = {r: (n_even if r % 2 == 1 else n_odd) for r in range(1, h + 1)}
    cap = max(deg.values())
    t0 = time.time()
    c0, s0, to0, e0 = run(h, q, cap, 0, tl * 0.4)
    c1, s1, to1, e1 = run(h, q, cap, 1, tl * 0.4)
    print('h', h, 'q', q, 'class0 functions', c0, 'class1 functions', c1, 'timeouts', to0, to1, 'sec', round(time.time() - t0, 1))
    if to0 or to1 or len(s0) < c0 or len(s1) < c1:
        print('enumeration incomplete: no conclusion')
        return
    byuse = {}
    for psi in s1:
        use = [0] * (h + 1)
        for y in psi:
            use[y] += 1
        byuse.setdefault(tuple(use), []).append(psi)
    found = 0; ncomp = 0; best = 0
    ex = None
    for phi in s0:
        use = [0] * (h + 1)
        for y in phi:
            use[y] += 1
        if any(use[r] > deg[r] for r in range(1, h + 1)):
            continue
        comp = tuple([0] + [deg[r] - use[r] for r in range(1, h + 1)])
        for psi in byuse.get(comp, ()):
            ncomp += 1
            d = len(set((a, b) if a < b else (b, a) for a, b in zip(phi, psi)))
            if d > best:
                best = d
            if d == q:
                found += 1
                ex = (phi, psi)
        if time.time() - t0 > tl:
            print('pairing timeout: no conclusion'); return
    print('pairs (phi,psi) with complementary row usage:', ncomp, '| largest number of distinct row pairs:', best, 'of', q)
    print('saturated boards with no 45-degree corner triple:', found)
    if ex:
        print('  ', ' '.join('%d-%d' % (min(a, b), max(a, b)) for a, b in zip(*ex)))

if __name__ == '__main__':
    main(int(sys.argv[1]), float(sys.argv[2]) if len(sys.argv) > 2 else 50)
