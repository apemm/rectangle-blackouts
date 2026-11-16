import time, sys
from driver import build, analyse
h = int(sys.argv[1]) if len(sys.argv) > 1 else 12
Wd = 4 * ((h * h) // 4 + 1) + 40
t = time.time()
for r in range(2, h + 1):
    kind = build(h, Wd, [], lambda n, r=r: r)
    res, ex = analyse(h, kind)
    print(r, dict(res) if res else 'clean')
print('time', time.time() - t)
