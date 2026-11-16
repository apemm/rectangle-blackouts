import json, sys, itertools
def rects(n):
    R = set()
    for px in range(n):
        for py in range(n):
            for ux in range(-n+1, n):
                for uy in range(-n+1, n):
                    if (ux, uy) == (0, 0): continue
                    ax, ay = px+ux, py+uy
                    if not (0 <= ax < n and 0 <= ay < n): continue
                    for vx in range(-n+1, n):
                        for vy in range(-n+1, n):
                            if (vx, vy) == (0, 0): continue
                            if ux*vx + uy*vy != 0: continue
                            bx, by = px+vx, py+vy
                            cx, cy = ax+vx, ay+vy
                            if 0 <= bx < n and 0 <= by < n and 0 <= cx < n and 0 <= cy < n:
                                R.add(frozenset([(px,py),(ax,ay),(bx,by),(cx,cy)]))
    return R
def valid(n, black, R):
    seen = {}
    for r in R:
        key = frozenset(p for p in r if p not in black)
        if key in seen: return False, (sorted(seen[key]), sorted(r))
        seen[key] = r
    return True, None
import os
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "2026-11-10", "squares_experiments", "data") + os.sep
for n, k in [(8,17),(9,19),(10,21)]:
    d = json.load(open(base + f"boards_n{n}_k{k}.json"))
    R = rects(n)
    res = []
    for b in d["boards"]:
        black = set((i // n, i % n) for i in b)
        assert len(black) == k
        res.append(valid(n, black, R)[0])
    print(n, k, "rectangles:", len(R), "boards:", len(res), "all valid:", all(res))
    b = d["boards"][0]
    rows = [''.join('#' if (r*n+c) in b else '.' for c in range(n)) for r in range(n)]
    print('\n'.join(rows))
