"""Run wn.run on one representative per orbit of the row reflection y -> h+1-y.
Usage: py wn_sym.py h lo hi   (slice of the representative list)
Prints the representative list size first."""
import sys, time
import wn

h = int(sys.argv[1]); lo = int(sys.argv[2]); hi = int(sys.argv[3])
bps = wn.bipartitions(h)
key = lambda E: frozenset(frozenset(e) for e in E)
index = {key(E): i for i, (A, E) in enumerate(bps)}
reps = []
for i, (A, E) in enumerate(bps):
    Er = [(h + 1 - b, h + 1 - a) for a, b in E]
    j = index[key(Er)]
    if i <= j:
        reps.append((i, j))
print(f"h={h}: {len(bps)} edge sets, {len(reps)} reflection orbits", flush=True)
t = time.time()
print('partners', reps[lo:hi], flush=True)
wn.run(h, idx_list=[i for i, j in reps[lo:hi]])
print(f"time {time.time() - t:.1f}s")
