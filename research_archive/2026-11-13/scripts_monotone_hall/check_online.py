# Independent check of online_fast output from the original norm formula.
import math, sys
import online_fast as of

def run_classes(h, C=70):
    # re-run with label recording (copy of of.run with members)
    A, K = (h + 1) // 2, h // 2
    S = of.kill_sets(h)
    last_i, last_j, occ, killed, mem = [], [], [], [], []
    buckets = {}
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
                    if j - lj > C * (i - last_i[c]): continue
                    if i in killed[c]: continue
                    if any((i - d) in occ[c] for d in pos): continue
                    best = c; break
                if best >= 0: break
            if best < 0:
                c = len(last_i); last_i.append(i); last_j.append(j); occ.append({i}); killed.append(set(i + d for d in neg)); mem.append([(i, j)])
            else:
                c = best; buckets[last_j[c]].discard(c)
                last_i[c] = i; last_j[c] = j; occ[c].add(i); killed[c].update(i + d for d in neg); mem[c].append((i, j))
            moved.append(c)
        for c in moved:
            buckets.setdefault(last_j[c], set()).add(c)
    return mem

def conflict(h, a, b):
    (i, j), (i2, j2) = a, b
    for (x, y, u) in ((i, j, i2), (i2, j2, i)):
        v = 16 * (x - u) ** 2 + (2 * (y - u) + 1) ** 2
        L = math.isqrt(v)
        if L * L == v and L < h: return True
    return False

for h in (33, 64, 97, 128):
    mem = run_classes(h)
    A, K = (h + 1) // 2, h // 2
    labs = [l for c in mem for l in c]
    assert len(labs) == A * K and len(set(labs)) == A * K
    bad = 0
    for c in mem:
        for t in range(1, len(c)):
            (i0, j0), (i1, j1) = c[t - 1], c[t]
            assert i1 > i0 and 0 <= j1 - j0 <= 70 * (i1 - i0)
        for x in range(len(c)):
            for y in range(x + 1, len(c)):
                if conflict(h, c[x], c[y]): bad += 1
    print(h, "classes", len(mem), "conflicts", bad)
