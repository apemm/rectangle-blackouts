"""Step 1: pure sea, pure collar, and one-label substitution at h = 112, profile (3, 9, 110, 2)."""
import time, json
from blib import *
h = 112; prof = (3, 9, 110, 2); D = 2 * Wh(h) + 1
t0 = time.time()
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
print('rows', rows, 'labels', len(labs), 'D', D)
# (a) collar block with no label at all (sea + both collars + tails)
lay = Layout(h); build_block(lay, prof, [(1, {})], D)
f, st = check_windows(lay, D)
print('empty block width', len(lay.col), {k: len(v) for k, v in f.items()}, round(time.time() - t0, 1), flush=True)
# (b) one label at a time, in the middle of a periodic sea of width 2D on each side
bad = []
for e in labs:
    lay = Layout(h)
    lay.seg(2 * D, lambda x: sea(prof, x), 'sea'); lay.pad7(lambda x: sea(prof, x), 'pad')
    x = lay.x(); lay.col.append(e); lay.tag.append('label'); lay.labels[x] = e
    lay.seg(2 * D, lambda x: sea(prof, x), 'sea')
    b = to_board(lay, x - D, x + D + 1)
    anchors = [(D, e[0]), (D, e[1])]
    whites = [(D, y) for y in range(1, h + 1) if y not in e]
    r = census(b, anchors, whites)
    c = {k: len(r[k]) for k in ('V1', 'V2', 'V3', 'V4', 'V5')}
    if any(c.values()):
        bad.append((e, c))
print('one-label failures', len(bad), bad[:10])
lit = [r for r in range(1, h + 1) if row_ok(h, prof, r, exact=False)]
print('rows passing literal (10):', lit)
print('time', round(time.time() - t0, 1))
