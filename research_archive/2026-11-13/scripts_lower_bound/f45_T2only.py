"""Sanity exploration: saturated boards (width q_h, all doubles, K_{A,B}) that are valid for the
family F45 (axis-aligned and 45-degree rectangles only).  Randomized DFS with the necessary conditions
T2/T3/T4/T5 of simplified_variants.md, then a definition-level check of F45-validity.
usage: py f45_search.py h Acsv seconds [seed]
"""
import sys, time, random


def f45_valid(cols, h):
    """definition-level check: all axis-aligned and 45-degree rectangles have distinct presentations"""
    m = len(cols)
    black = set()
    for i, (r, s) in enumerate(cols):
        black.add((i + 1, r))
        black.add((i + 1, s))
    pres = {}

    def add(corners):
        key = frozenset(c for c in corners if c not in black)
        if len(key) >= 3:
            return True
        cs = frozenset(corners)
        if key in pres and pres[key] != cs:
            return False
        pres[key] = cs
        return True

    for x1 in range(1, m + 1):
        for x2 in range(x1 + 1, m + 1):
            for y1 in range(1, h + 1):
                for y2 in range(y1 + 1, h + 1):
                    if not add(((x1, y1), (x1, y2), (x2, y1), (x2, y2))):
                        return False
    for x in range(1, m + 1):
        for y in range(1, h + 1):
            for s in range(1, h):
                for t in range(1, h):
                    c = ((x, y), (x + s, y + s), (x + t, y - t), (x + s + t, y + s - t))
                    if all(1 <= p[0] <= m and 1 <= p[1] <= h for p in c):
                        if not add(c):
                            return False
    return True


def search(h, A, tl, seed):
    rng = random.Random(seed)
    B = [r for r in range(1, h + 1) if r not in A]
    pairs = [(min(r, s), max(r, s)) for r in A for s in B]
    q = len(pairs)
    t0 = time.time()
    black = set()
    cols = []
    used = set()
    dpairs = {}
    apairs = {}
    best = [0]
    result = [None]
    nodes = [0]

    def try_add(c, pr):
        new = [(c, pr[0]), (c, pr[1])]
        if False:
            return None
        added_d = []
        added_a = []
        pts = list(black)
        ok = True
        for N in new:
            nx, ny = N
            for P in pts + [p for p in new if p != N]:
                px, py = P
                dx = px - nx
                dy = py - ny
                if dx == 0:
                    continue
                if False and dy != 0 and abs(dx) != abs(dy):
                    for sgn in (1, -1):
                        q1 = (nx - sgn * dy, ny + sgn * dx)
                        q2 = (px - sgn * dy, py + sgn * dx)
                        if q1 in black and q2 in black:
                            ok = False
                            break
                    if not ok:
                        break
                    if (dx + dy) % 2 == 0:
                        mx2 = nx + px
                        my2 = ny + py
                        q1 = ((mx2 - dy) // 2, (my2 + dx) // 2)
                        q2 = ((mx2 + dy) // 2, (my2 - dx) // 2)
                        if q1 in black and q2 in black:
                            ok = False
                            break
                if abs(dx) == abs(dy):
                    k = abs(dx)
                    left = N if nx < px else P
                    right = P if nx < px else N
                    if right[1] > left[1]:
                        v = left[0] - left[1]
                        umid = left[0] + left[1] + k
                        for (u2, vmid2) in apairs.get(k, ()):
                            if False:
                                ok = False
                                break
                        if not ok:
                            break
                        if (v, umid) not in dpairs.setdefault(k, set()):
                            added_d.append((k, (v, umid)))
                            dpairs[k].add((v, umid))
                    else:
                        u = left[0] + left[1]
                        vmid = left[0] - left[1] + k
                        for (v2, umid2) in dpairs.get(k, ()):
                            if False:
                                ok = False
                                break
                        if not ok:
                            break
                        if (u, vmid) not in apairs.setdefault(k, set()):
                            added_a.append((k, (u, vmid)))
                            apairs[k].add((u, vmid))
            if not ok:
                break
        if ok:
            allp = pts + new
            for N in new:
                nx, ny = N
                dn = []
                an = []
                for P in allp:
                    if P == N:
                        continue
                    dx = P[0] - nx
                    dy = P[1] - ny
                    if dx == dy:
                        dn.append(P)
                    elif dx == -dy:
                        an.append(P)
                for P in dn:
                    for Q in an:
                        fx = P[0] + Q[0] - nx
                        fy = P[1] + Q[1] - ny
                        if 1 <= fx <= q and 1 <= fy <= h:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    break
                for P in dn:
                    px, py = P
                    for Q in allp:
                        if Q == P or Q == N:
                            continue
                        if Q[0] - px == -(Q[1] - py):
                            fx = nx + Q[0] - px
                            fy = ny + Q[1] - py
                            if 1 <= fx <= q and 1 <= fy <= h:
                                ok = False
                                break
                    if not ok:
                        break
                if not ok:
                    break
                for P in an:
                    px, py = P
                    for Q in allp:
                        if Q == P or Q == N:
                            continue
                        if Q[0] - px == (Q[1] - py):
                            fx = nx + Q[0] - px
                            fy = ny + Q[1] - py
                            if 1 <= fx <= q and 1 <= fy <= h:
                                ok = False
                                break
                    if not ok:
                        break
                if not ok:
                    break
        if not ok:
            for k, e in added_d:
                dpairs[k].discard(e)
            for k, e in added_a:
                apairs[k].discard(e)
            return None
        return (new, added_d, added_a)

    def dfs(c):
        nodes[0] += 1
        if result[0] is not None:
            return
        if time.time() - t0 > tl:
            return
        if c > best[0]:
            best[0] = c
        if c == q:
            result[0] = list(cols)
            return
        order = [p for p in pairs if p not in used]
        rng.shuffle(order)
        for pr in order:
            u = try_add(c + 1, pr)
            if u is None:
                continue
            new, ad, aa = u
            black.update(new)
            cols.append(pr)
            used.add(pr)
            dfs(c + 1)
            used.discard(pr)
            cols.pop()
            black.difference_update(new)
            for k, e in ad:
                dpairs[k].discard(e)
            for k, e in aa:
                apairs[k].discard(e)
            if result[0] is not None or time.time() - t0 > tl:
                return

    dfs(0)
    return result[0], best[0], nodes[0], time.time() - t0, q


if __name__ == '__main__':
    h = int(sys.argv[1])
    A = tuple(int(t) for t in sys.argv[2].split(','))
    tl = float(sys.argv[3])
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    res, best, nodes, el, q = search(h, A, tl, seed)
    print('h', h, 'A', A, 'q', q, 'best depth', best, 'nodes', nodes, 'sec', round(el, 1))
    if res:
        print('FOUND', ' '.join('%d-%d' % p for p in res))
        print('definition-level F45 validity:', f45_valid(res, h))
