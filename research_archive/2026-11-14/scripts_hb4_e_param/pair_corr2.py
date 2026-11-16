"""Per-tau pairing counts, restricted to bulk Y >= h/ylo_div."""
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
from pair_corr import vectors

S = int(sys.argv[1]); h = int(sys.argv[2]); ydiv = int(sys.argv[3])
V = vectors(S, h)
byY = defaultdict(list)
for q, Y in V:
    if Y >= h // ydiv:
        byY[Y].append(q)
for Y in byY: byY[Y].sort()
print(f"S={S} h={h} bulk Y>=h/{ydiv}: vectors={sum(len(v) for v in byY.values())}")
for (D1, D2) in [(1, 16), (17, 256), (257, 10**9)]:
    row = []
    for tau in range(0, 31):
        tot = 0
        for Y, qs in byY.items():
            qs2 = byY.get(Y + 2 * tau)
            if not qs2: continue
            for q in qs:
                tot += bisect_right(qs2, q + D2) - bisect_left(qs2, q + D1)
                tot += bisect_right(qs2, q - D1) - bisect_left(qs2, q - D2)
        row.append(tot)
    m = sum(row[1:]) / 30
    print(f" band [{D1},{D2}] P(0)={row[0]} mean={m:.1f} kappa={row[0]/m:.2f}")
    print("  per tau:", row)
