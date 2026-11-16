import random, sys, time
from obs import triples
# Region A test: row-1 shallow sea, deep doubles {2i+1 (i odd), even}, fillers rows = 3 mod 4.
# Control: allow i even.
def board(h, width, allow_even_i, seed):
    rnd = random.Random(seed)
    S = set()
    A = (h + 1) // 2; K = h // 2
    for x in range(width):
        if x % 4:
            S.add((x, 1))
        else:
            if rnd.random() < 0.7:
                while True:
                    i = rnd.randrange(1, A)
                    if allow_even_i or i % 2 == 1:
                        break
                j = rnd.randrange(0, K)
                S.add((x, 2 * i + 1)); S.add((x, 2 * j + 2))
            else:
                rows = [y for y in range(3, h + 1) if y % 4 == 3]
                S.add((x, rnd.choice(rows)))
    return S

def shallow(P):
    return P[1] == 1 and P[0] % 4 != 0

h = int(sys.argv[1]); width = int(sys.argv[2])
t0 = time.time()
for allow in (False, True):
    tot = {}
    for seed in range(3):
        S = board(h, width, allow, seed)
        for t in triples(S, h):
            corners = t[1:4]
            ns = sum(shallow(P) for P in corners)
            if ns >= 1 and t[0] != 'parked':
                tot[(t[0], ns)] = tot.get((t[0], ns), 0) + 1
    print('allow_even_i', allow, 'fatal/V1 triples with shallow corner:', tot)
print('time', round(time.time() - t0, 1))
