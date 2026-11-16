"""Small |dq| band: P(tau) for |q-q'| in [1,D], bulk Y>=h/8. Shows per-tau and kappa vs h."""
import sys, time
from bisect import bisect_left, bisect_right
from collections import defaultdict
from pair_corr import vectors
S = int(sys.argv[1]); D = int(sys.argv[2])
for lg in map(int, sys.argv[3:]):
    h = 2 ** lg; t0 = time.time()
    byY = defaultdict(list)
    for q, Y in vectors(S, h):
        if Y >= h // 8: byY[Y].append(q)
    for Y in byY: byY[Y].sort()
    row = []
    for tau in range(0, 41):
        tot = 0
        for Y, qs in byY.items():
            qs2 = byY.get(Y + 2 * tau)
            if not qs2: continue
            for q in qs:
                tot += bisect_right(qs2, q + D) - bisect_left(qs2, q + 1)
                tot += bisect_right(qs2, q - 1) - bisect_left(qs2, q - D)
        row.append(tot)
    m = sum(row[1:]) / 40
    print(f"S={S} D={D} h=2^{lg}: P0={row[0]} mean={m:.1f} kappa={row[0]/m if m else 0:.2f} t={time.time()-t0:.1f}s")
    print("   ", row)
