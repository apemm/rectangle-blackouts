import sys, time
from s13_chi_lim import dist, colorable
T = 1045
t0 = time.time()
n = int(sys.argv[1]); k = int(sys.argv[2]); secs = float(sys.argv[3]); B = int(sys.argv[4]) if len(sys.argv) > 4 else 1200
D = [d for d in dist(T, B) if d < n]
cl = [0, 35, 209, 260, 434] if n > 434 else None
r = colorable(n, D, k, secs, clique=cl)
print("T", T, "n", n, "|D|", len(D), "k", k, "->", r, "t=%.1f" % (time.time() - t0))
