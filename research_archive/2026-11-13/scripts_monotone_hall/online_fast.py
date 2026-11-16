# Faster version of online_mixed.py (mixed mode only): buckets by last_j, scan downward from j.
import sys, time
from online_mixed import kill_sets

def run(h, C=70):
    A, K = (h + 1) // 2, h // 2
    S = kill_sets(h)
    last_i, last_j, occ, killed = [], [], [], []
    buckets = {}  # last_j -> set of classes
    scans = 0
    for i in range(A):
        moved = []
        for j in range(K):
            T = 2 * (j - i) + 1
            ST = S.get(T, ())
            pos = [d for d in ST if d > 0 and i - d >= 0]
            neg = [-d for d in ST if d < 0 and i - d < A]
            best = -1
            for lj in range(j, -1, -1):
                b = buckets.get(lj)
                if not b: continue
                for c in b:
                    scans += 1
                    if j - lj > C * (i - last_i[c]): continue
                    if i in killed[c]: continue
                    o = occ[c]
                    if any((i - d) in o for d in pos): continue
                    best = c; break
                if best >= 0: break
            if best < 0:
                c = len(last_i)
                last_i.append(i); last_j.append(j); occ.append({i}); killed.append(set(i + d for d in neg))
            else:
                c = best
                buckets[last_j[c]].discard(c)
                last_i[c] = i; last_j[c] = j; occ[c].add(i); killed[c].update(i + d for d in neg)
            moved.append(c)
        for c in moved:
            buckets.setdefault(last_j[c], set()).add(c)
    return len(last_i), scans

if __name__ == "__main__":
    t0 = time.time()
    for h in [int(x) for x in sys.argv[1:]]:
        a, sc = run(h)
        print(h, "mixed", a, round(a / h, 3), "scans", sc, "t", round(time.time() - t0, 1), flush=True)
