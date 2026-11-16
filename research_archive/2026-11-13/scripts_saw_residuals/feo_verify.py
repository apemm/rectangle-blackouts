"""Independent check of Feo hits far from the band: build the SAW board (lcd.build), verify the right angle,
that P, Q, V are black with the claimed roles, and that W is in the grid, white, in a column with an odd black point."""
import os, sys
os.environ['LM'] = '16'
from lcd import build
from feo_closed import run
h = int(sys.argv[1]); iota = 1; nshow = 0; ok = 0; bad = 0
for s in range(-(h // 2), h // 2, 7):
    n, H = run(h, iota, s, 0)
    H = [x for x in H if 2 * x[0] + 1 < x[3] - 150]
    if not H: continue
    kind, cb, cn, labs, (R0, M, base, Wd) = build(h, iota, s, [-3, -2, -1, 0], [], 1)
    for (iP, g, t, yV) in H:
        P = (4 * (iP + M), 2 * iP + 1); V = (4 * (iP + g + M), yV); iQ = iP + t
        Q = (4 * (iQ + M), 2 * (iQ + s) + 2); W = (P[0] + Q[0] - V[0], P[1] + Q[1] - V[1])
        dot = (P[0] - V[0]) * (Q[0] - V[0]) + (P[1] - V[1]) * (Q[1] - V[1])
        good = dot == 0 and kind[P] == 3 and kind[Q] == 4 and kind[V] == 2 and 1 <= W[1] <= h and kind[W] == 0 \
            and any(cb[W[0], k] % 2 == 1 for k in range(cn[W[0]]))
        ok += good; bad += (not good)
        if nshow < 4: print('s', s, 'P', P, 'V', V, 'Q', Q, 'W', W, 'ok' if good else 'FAIL'); nshow += 1
print('h', h, 'verified', ok, 'failed', bad)
