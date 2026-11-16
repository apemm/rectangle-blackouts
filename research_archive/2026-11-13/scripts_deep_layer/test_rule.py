import sys, time, random
from driver import build, analyse
from board import shapes

def block_labels(h, s, iota, M, mod=4):
    A = (h + 1) // 2; K = h // 2
    L = []
    for i in range(A):
        j = i + s
        if 0 <= j < K and i % mod == iota % mod:
            L.append((4 * (i + M), 2 * i + 1, 2 * j + 2))
    return L

def run(h, s, iota, M, rule, seed=0, label=''):
    W = (h * h) // 4 + 1
    A = (h + 1) // 2
    Wd = 4 * (M + A) + 2 * W + 40
    labels = block_labels(h, s, iota, M)
    rnd = random.Random(seed)
    cache = {}
    def fr(n):
        if n not in cache:
            cache[n] = rule(n, rnd)
        return cache[n]
    kind = build(h, Wd, labels, fr)
    res, ex = analyse(h, kind)
    return res, ex

if __name__ == '__main__':
    h = int(sys.argv[1]); s = int(sys.argv[2]); iota = int(sys.argv[3])
    W = (h * h) // 4 + 1
    M = (W // 2 + 10) // 8 * 8 + 8  # block start, M = 0 mod 8
    r0 = 2 * iota + 1
    rows8 = [y for y in range(2, h + 1) if y % 8 == r0 % 8]
    rows34 = [y for y in range(2, h + 1) if y % 4 == 3]
    rules = {
        'mod8': lambda n, rnd: rnd.choice(rows8),
        'mod4': lambda n, rnd: rnd.choice(rows34),
    }
    t = time.time()
    for name, rule in rules.items():
        for seed in range(2):
            res, ex = run(h, s, iota, M, rule, seed)
            tot = sum(res.values())
            print(name, seed, 'total', tot, dict(sorted(res.items())))
    print('time', time.time() - t)
