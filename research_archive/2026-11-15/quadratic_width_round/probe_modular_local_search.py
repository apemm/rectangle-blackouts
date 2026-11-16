"""Min-conflicts local search for the certified modular model. Low memory.

A zero-violation assignment is checked directly and saved. A nonzero residual
proves nothing.
"""
import sys, time, json
import numpy as np
events, side, seconds = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
ev = np.load(events); n = side * side
u = ev[:, 0].astype(np.int64); v = ev[:, 1].astype(np.int64); g = ev[:, 2].astype(np.int8)
rng = np.random.default_rng(1)
col = rng.integers(0, 3, n).astype(np.int8)
start = time.monotonic(); best = None; it = 0; p = 0.3
while True:
    fu = (col[v] - g) % 3; fv = (col[u] + g) % 3
    bad = fu == col[u]; nb = int(bad.sum())
    if best is None or nb < best[0]:
        best = (nb, col.copy())
    if it % 50 == 0:
        print(it, nb, round(time.monotonic() - start), flush=True)
    if nb == 0 or time.monotonic() - start > seconds:
        break
    cnt = (np.bincount(u * 3 + fu, minlength=3 * n) + np.bincount(v * 3 + fv, minlength=3 * n)).reshape(n, 3)
    cur = cnt[np.arange(n), col]
    noisy = cnt + rng.random((n, 3)) * 0.5
    target = noisy.argmin(1).astype(np.int8)
    move = (cur > cnt.min(1)) & (rng.random(n) < p)
    # plateau moves on conflicted vertices
    plateau = (cur > 0) & (cur == cnt.min(1)) & (rng.random(n) < 0.1)
    col = np.where(move | plateau, target, col)
    it += 1
nb, col = best
bad = ((col[v] - col[u] - g) % 3 == 0)
assert int(bad.sum()) == nb
out = events.replace('_events.npy', '_modular_local_search')
json.dump(dict(side=side, events=len(ev), iterations=it, best_violations=nb,
               status='SAT_DIRECTLY_CHECKED' if nb == 0 else 'RESIDUAL_NOT_A_PROOF'), open(out + '.json', 'w'), indent=2)
if nb == 0:
    np.savez_compressed(out + '.npz', colors=col)
print('best', nb)
