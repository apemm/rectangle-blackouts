import sys, itertools
from common import all_D
h = int(sys.argv[1]); Ts = [int(t) for t in sys.argv[2:]]
D = all_D(h)
for T in Ts:
    d = D[T]; s = set(d)
    best = []
    # cliques containing 0: subsets of d with pairwise differences in s
    def ext(cl, cand):
        global best
        if len(cl) > len(best): best = cl[:]
        for i, v in enumerate(cand):
            ext(cl + [v], [u for u in cand[i+1:] if abs(u - v) in s])
    ext([], d)
    print(T, "k", len(d), "clique", [0] + best)
