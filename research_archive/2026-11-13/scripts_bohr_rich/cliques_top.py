import sys
from common import all_D
from cliques_lib import maxclique_list
h = int(sys.argv[1]); top = int(sys.argv[2])
D = all_D(h)
Ts = sorted(D, key=lambda T: -len(D[T]))[:top]
hist = {}
best = (0, None, None)
for T in Ts:
    d = D[T]; cl = maxclique_list(d)
    w = len(cl) + 1
    hist[w] = hist.get(w, 0) + 1
    if w > best[0]: best = (w, T, [0] + cl)
print("h", h, "top", top, "hist", sorted(hist.items()), "best", best)
