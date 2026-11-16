"""Local search for the relaxed conservation problem (see conserve.py)."""
import random, sys
from conserve import ok_pair

def score(f, D, F, relaxed):
    L = len(f)
    parent = list(range(L))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a in range(L):
        for b in range(a+1, L):
            if not ok_pair(b - a, f[b] - f[a], D, F, relaxed):
                ra, rb = find(a), find(b)
                if ra != rb: parent[ra] = rb
    comps = {}
    for u in range(L): comps.setdefault(find(u), set()).add(f[u])
    return sum(len(s) for s in comps.values())

def search(D, F, relaxed, iters, seed):
    rnd = random.Random(seed); L = 2**D; best = 0; bf = None
    cands = [[(u >> k) % 2**F for u in range(L)] for k in range(D)]
    for c in cands:
        s = score(c, D, F, relaxed)
        if s > best: best, bf = s, c
    for r in range(iters):
        f = list(bf) if rnd.random() < 0.5 and bf else [rnd.randrange(2**F) for _ in range(L)]
        s = score(f, D, F, relaxed)
        for _ in range(200):
            u = rnd.randrange(L); old = f[u]; f[u] = rnd.randrange(2**F)
            s2 = score(f, D, F, relaxed)
            if s2 >= s: s = s2
            else: f[u] = old
        if s > best: best, bf = s, list(f)
    return best, bf

if __name__ == '__main__':
    for (D, F) in [(3,2),(4,2),(4,3),(5,2),(5,3),(5,4),(6,3),(6,4)]:
        b, f = search(D, F, True, 30, 1)
        bs, _ = search(D, F, False, 10, 2)
        print(f"D={D} F={F}: relaxed best N={b}, strict best N={bs}, 2^F={2**F}, leaves={2**D}")
