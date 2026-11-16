import random
from blib import *
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
# parked triples in one-label substitution
tot = 0; ex = []
for e in labs:
    lay = Layout(h)
    lay.seg(2 * D, lambda x: sea(prof, x), 'sea'); lay.pad7(lambda x: sea(prof, x), 'pad')
    x = lay.x(); lay.col.append(e); lay.tag.append('label'); lay.labels[x] = e
    lay.seg(2 * D, lambda x: sea(prof, x), 'sea')
    b = to_board(lay, x - D, x + D + 1)
    r = census(b, [(D, e[0]), (D, e[1])], [(D, y) for y in range(1, h + 1) if y not in e])
    n = sum(len(S) for S in r['parked'].values())
    tot += n
    if n and len(ex) < 3:
        W, S = next(iter(r['parked'].items()))
        ex.append((e, W[0] - D, W[1], [sorted((q[0] - D, q[1]) for q in k) for k in S]))
print('parked triples over one-label configs:', tot)
for t in ex: print(t)
