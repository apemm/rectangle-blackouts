import sys, time
from wk3 import build, count
h, K = int(sys.argv[1]), int(sys.argv[2])
As = [tuple(int(t) for t in s.split(',')) for s in sys.argv[3:]]
t0 = time.time(); cells, M = build(h, K); print('build', round(time.time() - t0, 1), flush=True)
for A in As:
    print('A', A, 'K', K, 'windows', count(h, K, A, cells, M), round(time.time() - t0, 1), flush=True)
