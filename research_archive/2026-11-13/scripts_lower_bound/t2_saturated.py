"""Sanity exploration.  Parity partition, h even, q = h^2/4.
Decide whether there is a saturated board (all doubles, every (odd,even) row pair once) in which no
45-degree rectangle of the board has >= 3 black corners (condition T2 only).
The two bishop classes decouple: each is a function with one cell per column.
usage: py t2_saturated.py h [seconds]
"""
import sys, time
from class_functions import run


def main(h, tl):
    q = h * h // 4
    cap = h // 2
    c0, s0, to0, e0 = run(h, q, cap, 0, tl / 3)
    c1, s1, to1, e1 = run(h, q, cap, 1, tl / 3)
    print('h', h, 'q', q, 'class0 functions', c0, 'class1 functions', c1, 'timeouts', to0, to1)
    if to0 or to1:
        print('enumeration incomplete')
        return
    byuse = {}
    for psi in s1:
        use = [0] * (h + 1)
        for y in psi:
            use[y] += 1
        byuse.setdefault(tuple(use), []).append(psi)
    found = 0
    examples = []
    t0 = time.time()
    for phi in s0:
        use = [0] * (h + 1)
        for y in phi:
            use[y] += 1
        comp = tuple([0] + [cap - use[r] for r in range(1, h + 1)])
        for psi in byuse.get(comp, ()):
            seen = set()
            ok = True
            for a, b in zip(phi, psi):
                key = (a, b) if a < b else (b, a)
                if key in seen:
                    ok = False
                    break
                seen.add(key)
            if ok:
                found += 1
                if len(examples) < 3:
                    examples.append((phi, psi))
        if time.time() - t0 > tl / 3:
            print('pairing timeout')
            break
    print('saturated boards with no 45-degree corner triple:', found)
    for phi, psi in examples:
        print('  ', ' '.join('%d-%d' % (min(a, b), max(a, b)) for a, b in zip(phi, psi)))


if __name__ == '__main__':
    h = int(sys.argv[1])
    tl = float(sys.argv[2]) if len(sys.argv) > 2 else 50
    main(h, tl)
