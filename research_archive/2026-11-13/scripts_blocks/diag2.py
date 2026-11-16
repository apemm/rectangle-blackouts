import random, time
from blib import *
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
E = [e for e in labs if e[1] - e[0] in (-7, 7, 21)]
rng = random.Random(1)
for mult in (10, 30, 60):
    t0 = time.time()
    c = E[:11]; N = mult * len(c)
    place, hist = place_class(h, prof, D, c, N, rng, maxit=60)
    print(mult, N, 'ok' if place else 'FAIL', len(hist), hist[0], hist[-1], round(time.time() - t0, 1), flush=True)
