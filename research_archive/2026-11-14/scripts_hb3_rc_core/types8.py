"""For each of the 12 Model K types of an 8x8 block placed at label offset (i0, j0) with
j0 - i0 = OFF (mid-strip), search random admissible orders for one whose internal P
constraints (S=32, M=3) contain a weighted 3-core.  Completion owners are outside the block
because L >= S^2/4+1 = 257 exceeds every in-block row difference; mid-strip placement keeps
completion rows inside [1, h].  Prints a witness order (as a rank list) per type."""
import sys, math, random
import numpy as np
import randcurve as R
from gblock import vectors

S, M, B = 32, 3, 8
OFF = int(sys.argv[1]) if len(sys.argv) > 1 else 16
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
V = vectors(S, 2 * (OFF + B) + 3)  # X -> {Y: L}
legs = {}
for X, ys in V.items():
    for Y in ys:
        legs.setdefault(Y, set()).add(X // S)

def constraints(xy):
    # xy: local cells by rank; label rows odd 2(i0+x)+1, even 2(j0+y)+2 with j0 - i0 = OFF
    cons = []
    n = len(xy)
    for r in range(n):
        for s in range(r + 1, n):
            d = s - r
            (x1, y1), (x2, y2) = xy[r], xy[s]
            Ys = {abs(2 * (y2 + OFF - x1) + 1), abs(2 * (x2 - y1 - OFF) - 1)}
            for delta in range(1 - M, M):
                qq = M * d + delta
                if qq <= 0:
                    continue
                if any(qq in legs.get(Y, ()) for Y in Ys):
                    cons.append((r, s, delta))
    return cons

def has_core(cons, n, k=3):
    deg = [0] * n
    adj = [[] for _ in range(n)]
    for r, s, _ in cons:
        deg[r] += 1; deg[s] += 1; adj[r].append(s); adj[s].append(r)
    alive = [True] * n
    changed = True
    while changed:
        changed = False
        for v in range(n):
            if alive[v] and deg[v] < k:
                alive[v] = False; changed = True
                for w in adj[v]:
                    if alive[w]:
                        deg[w] -= 1
    return [v for v in range(n) if alive[v]]

P = {1: R.plans_for(1), 2: R.plans_for(2), 4: R.plans_for(4)}
def sample(en, ex, rng):
    out = []
    stack = [(0, 0, B, en, ex)]
    while stack:
        x0, y0, s, a, b = stack.pop()
        if s == 1:
            out.append((x0, y0)); continue
        half = s // 2
        order, cs = rng.choice(P[min(half, 4)][(a, b)])
        for t in (3, 2, 1, 0):
            c = order[t]
            stack.append((x0 + c[0] * half, y0 + c[1] * half, half, cs[t][0], cs[t][1]))
    return out

rng = random.Random(7)
for en in range(4):
    for ex in range(4):
        if en == ex:
            continue
        found = None
        for t in range(NS):
            xy = sample(en, ex, rng)
            core = has_core(constraints(xy), len(xy))
            if core:
                found = (t, core, xy); break
        if found:
            t, core, xy = found
            print(f"type ({en},{ex}): 3-core after {t+1} samples, core ranks {core}, cells {[xy[v] for v in core]}")
        else:
            print(f"type ({en},{ex}): none in {NS} samples")
        sys.stdout.flush()
