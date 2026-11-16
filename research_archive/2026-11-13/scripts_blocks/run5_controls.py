"""Controls: (a) wrong-residue labels; (b) two independently placed classes interleaved with no
separation; (c) restriction of placed classes to random subsets (holes keep F), non-strict and strict."""
import time, random
from blib import *
t0 = time.time()
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
L, F, H, g = prof
rng = random.Random(7)
# (a)
wrong = [(a, b) for a in range(1, h + 1, 2) for b in range(2, h + 1, 2)
         if a > F + 4 and b > F + 4 and a + F < H - L + 2 and b + F < H - L + 2
         and ((a - L) % 7 not in (0, 5 * g % 7) or (b - L) % 7 not in (0, 5 * g % 7))]
sample = rng.sample(wrong, 60); nbad = 0
for e in sample:
    hit, nrec, cnt = class_violations(h, prof, D, 1, {e: 0})
    nbad += nrec > 0
print('(a) wrong-residue labels with a one-label record: %d of %d' % (nbad, len(sample)), round(time.time() - t0, 1), flush=True)
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
E = [e for e in labs if e[1] - e[0] in (-7, 7, 21)]
c1, c2 = E[:11], E[11:]
for strict in (False, True):
    p1, _ = place_class(h, prof, D, c1, 330, rng, strict=strict)
    p2, _ = place_class(h, prof, D, c2, 360, rng, strict=strict)
    # (b) interleave: class 2 slots moved into class 1's range (no collision)
    used = set(p1.values()); merged = dict(p1)
    for e, s in p2.items():
        t = s % 330
        while t in used:
            t = (t + 1) % 330
        used.add(t); merged[e] = t
    hit, nrec, cnt = class_violations(h, prof, D, 330, merged, strict)
    print('(b) strict=%s interleaved classes: records %d %s' % (strict, nrec, cnt), flush=True)
    # (c) restriction to random subsets
    tot = 0; trials = 20
    for _ in range(trials):
        sub = {e: s for e, s in p1.items() if rng.random() < 0.5}
        if not sub:
            continue
        hit, nrec, cnt = class_violations(h, prof, D, 330, sub, strict)
        tot += nrec
    print('(c) strict=%s restrictions of a clean class to random halves: total records %d over %d trials' % (strict, tot, trials), round(time.time() - t0, 1), flush=True)
