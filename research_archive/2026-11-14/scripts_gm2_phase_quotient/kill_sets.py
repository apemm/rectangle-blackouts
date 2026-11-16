"""Minimal tau-killing slot subsets inside 3-core components of G_B^o, and whether they are local.
A slot set K 'kills' if A(K) = empty (no tau with ||tau d - delta/M|| >= 1/M for all (d, delta) in K).
Also: for each core label v, is the slot set of its closed neighbourhood (edges among v and its neighbours)
tau-admissible?  Usage: py -B kill_sets.py B S M orient"""
import sys
from collections import defaultdict, Counter
from core_cert import build, core, admissible


def minimal_kill(slots, M):
    s = sorted(slots)
    # shortest killing prefix by d
    lo, hi = 1, len(s)
    if admissible(s, M): return None, None
    while lo < hi:
        mid = (lo + hi) // 2
        if admissible(s[:mid], M): lo = mid + 1
        else: hi = mid
    pref = s[:lo]
    K = list(pref)
    for x in list(pref):
        T = [y for y in K if y != x]
        if not admissible(T, M): K = T
    return lo, sorted(K)


def main():
    B, S, M, orient = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    import os, json
    cache = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"core_{B}_{M}_{orient}.json")
    if os.path.exists(cache):
        incore = [tuple(c) for c in json.load(open(cache))]
        trip = {(r, u, dl): q for r, u, dl, q in incore}
    else:
        trip = build(B, S, M, orient)
    Kset, comps = core(trip, M)
    comps.sort(key=len, reverse=True)
    incore = [(r, u, dl, q) for (r, u, dl), q in trip.items() if r in Kset and u in Kset]
    adj = defaultdict(list)
    for (r, u, dl, q) in incore:
        adj[r].append((u, dl, q)); adj[u].append((r, dl, q))
    for comp in comps:
        cs = set(comp)
        slots = {(u - r, dl) for (r, u, dl, q) in incore if r in cs}
        n, Kill = minimal_kill(slots, M)
        print(f"comp {len(comp)} labels, {len(slots)} slots: admissible prefix length {n-1 if n else None}, minimal kill set {Kill}",
              "gaps", [M * d + dl for d, dl in (Kill or [])])
    # local test: closed neighbourhood slot sets
    tot = 0; bad = 0; sizes = Counter()
    for v in Kset:
        N = {v} | {w for w, _, _ in adj[v]}
        sl = set()
        for x in N:
            for w, dl, q in adj[x]:
                if w in N:
                    r, u = min(x, w), max(x, w); sl.add((u - r, dl))
        tot += 1
        if not admissible(sl, M): bad += 1; sizes[len(sl)] += 1
    print(f"closed neighbourhoods: {tot}, tau-inadmissible {bad}; slot-count histogram of inadmissible ones {sorted(sizes.items())[:12]}")


if __name__ == "__main__":
    main()
