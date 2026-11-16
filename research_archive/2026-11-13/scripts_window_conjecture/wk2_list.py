import sys, time
from wk2 import build, count
h, K = int(sys.argv[1]), int(sys.argv[2])
As = [tuple(int(t) for t in s.split(',')) for s in sys.argv[3:]]
t0 = time.time(); cells, cid, L = build(h, K)
for A in As:
    print('A', A, 'K', K, 'windows', count(h, K, A, cells, cid, L), round(time.time() - t0, 1), flush=True)
