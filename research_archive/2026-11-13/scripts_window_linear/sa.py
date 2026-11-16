"""Simulated annealing for an N-window of width K (all tilted rectangles).
cost = number of tilted rectangles of the h x K grid with >= 3 corners in P.
usage: py sa.py h K seconds seed [A comma list]
"""
import sys, time, random, math
from math import gcd

def rects(h, K):
    out = []
    for c in range(1, max(h, K) + 1):
        for d in range(1, max(h, K) + 1):
            if gcd(c, d) != 1:
                continue
            for s in range(1, K + 1):
                if s * c > K - 1 or s * d > h - 1:
                    break
                for t in range(1, K + 1):
                    if t * d > K - 1 or t * c > h - 1:
                        break
                    if s * c + t * d > K - 1 or s * d + t * c > h - 1:
                        continue
                    for x in range(1 + t * d, K + 1 - s * c):
                        for y in range(1, h - (s * d + t * c) + 1):
                            out.append(((x, y), (x + s * c, y + s * d), (x - t * d, y + t * c),
                                        (x + s * c - t * d, y + s * d + t * c)))
    return out

h = int(sys.argv[1]); K = int(sys.argv[2]); T = float(sys.argv[3]); seed = int(sys.argv[4])
A = [int(v) for v in sys.argv[5].split(',')] if len(sys.argv) > 5 else list(range(1, h + 1, 2))
B = [y for y in range(1, h + 1) if y not in A]
E = [(a, b) for a in A for b in B]
random.seed(seed)
R = rects(h, K)
idx = {}
for i, r in enumerate(R):
    for p in r:
        idx.setdefault(p, []).append(i)
cnt = [0] * len(R)
def bad(c):
    return 1 if c >= 3 else 0
cost = 0
def add(p, sgn):
    global cost
    for i in idx.get(p, ()):
        before = bad(cnt[i]); cnt[i] += sgn; cost += bad(cnt[i]) - before
seq = random.sample(range(len(E)), K)
for x, j in enumerate(seq, 1):
    a, b = E[j]; add((x, a), 1); add((x, b), 1)
unused = [j for j in range(len(E)) if j not in seq]
t0 = time.time(); temp = 2.0; best = cost; it = 0
while time.time() - t0 < T and cost > 0:
    it += 1
    temp = max(0.05, 2.0 * (1 - (time.time() - t0) / T))
    x = random.randrange(K)
    if unused and random.random() < 0.5:
        u = random.randrange(len(unused)); j_new = unused[u]; j_old = seq[x]
        old = cost
        a, b = E[j_old]; add((x + 1, a), -1); add((x + 1, b), -1)
        a, b = E[j_new]; add((x + 1, a), 1); add((x + 1, b), 1)
        d = cost - old
        if d <= 0 or random.random() < math.exp(-d / temp):
            seq[x] = j_new; unused[u] = j_old
        else:
            a, b = E[j_new]; add((x + 1, a), -1); add((x + 1, b), -1)
            a, b = E[j_old]; add((x + 1, a), 1); add((x + 1, b), 1)
    else:
        y = random.randrange(K)
        if x == y: continue
        old = cost
        for (z, j) in ((x, seq[x]), (y, seq[y])):
            a, b = E[j]; add((z + 1, a), -1); add((z + 1, b), -1)
        for (z, j) in ((x, seq[y]), (y, seq[x])):
            a, b = E[j]; add((z + 1, a), 1); add((z + 1, b), 1)
        d = cost - old
        if d <= 0 or random.random() < math.exp(-d / temp):
            seq[x], seq[y] = seq[y], seq[x]
        else:
            for (z, j) in ((x, seq[y]), (y, seq[x])):
                a, b = E[j]; add((z + 1, a), -1); add((z + 1, b), -1)
            for (z, j) in ((x, seq[x]), (y, seq[y])):
                a, b = E[j]; add((z + 1, a), 1); add((z + 1, b), 1)
    best = min(best, cost)
print(f"h={h} K={K} A={A} rects={len(R)} iters={it} final={cost} best={best}")
if cost == 0:
    print([E[j] for j in seq])
