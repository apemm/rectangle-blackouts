"""Cross-check with the round's original search explore_windows.py (mode N), copied unchanged.
Usage: py xcheck_explore.py h lo hi  -- runs A-sets lo..hi-1 of the list of A with |A| = floor(h/2)
(for even h only A containing 1, which lists every edge set once)."""
import sys, itertools, time
from explore_windows import run
h = int(sys.argv[1]); lo = int(sys.argv[2]); hi = int(sys.argv[3])
parts = [A for A in itertools.combinations(range(1, h + 1), h // 2) if h % 2 == 1 or 1 in A]
t0 = time.time()
for A in parts[lo:hi]:
    best, nodes, to, el, q = run(h, A, 'N', 1e9)
    print('A', A, 'maxwidth', best['w'], 'count', best['count'], 'nodes', nodes, 'sec', round(el, 1), flush=True)
print('total', round(time.time() - t0, 1), 'of', len(parts))
