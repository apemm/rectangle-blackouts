"""Exploration (sanity check only): maximal all-double windows.

A window is k consecutive columns, each with exactly two black cells whose rows
form distinct edges of K_{A,B}.  Necessary conditions for being a window of a
valid equality board:
  (N)  no tilted rectangle inside the window has >= 3 black corners;
  (V)  no tilted rectangle with a vertical diagonal on rows of different parts
       has its other two corners black (virtual axis owner);
  (C)  no two distinct rectangles inside the window have equal presentations.
Modes: 'N' uses (N) only, 'NV' uses (N),(V), 'full' uses all three.

usage: py explore_windows.py h mode [timelimit] [partition as comma list of A]
"""
import sys, time, itertools
from math import gcd


def tilted_shapes(h):
    out = []
    for b in range(1, h):
        for d in range(1, h - b):
            n = b * d
            for a in range(1, n + 1):
                if n % a == 0:
                    out.append((a, b, n // a, d))
    return out


def run(h, A, mode, tlimit):
    A = sorted(A)
    B = [r for r in range(1, h + 1) if r not in A]
    part = {r: 0 for r in A}
    part.update({r: 1 for r in B})
    pairs = [(min(r, s), max(r, s)) for r in A for s in B]
    q = len(pairs)
    shapes = tilted_shapes(h)
    # rectangles by offsets relative to max column: list of corner tuples (dx<=0, row)
    # tilted rectangle with leftmost corner (x, r): corners (x,r),(x+a,r-b),(x+c,r+d),(x+a+c,r-b+d)
    tilted = []  # (span, [(dx,row)*4]) with dx relative to max column
    for (a, b, c, d) in shapes:
        span = a + c
        for r in range(1 + b, h - d + 1):
            cs = [(-span, r), (a - span, r - b), (c - span, r + d), (0, r - b + d)]
            # vertical diagonal? corners 1 and 2 in one column iff a == c
            vd = None
            if a == c:
                vd = (1, 2)  # indices of vertical diagonal corners
            tilted.append((span, cs, vd))
    best = {'w': 0, 'ex': [], 'count': 0}
    t0 = time.time()
    cols = []  # list of (r,s)
    black = set()
    pres = {}
    used = set()
    nodes = [0]
    timeout = [False]

    def check_new(c):
        """check rectangles with max column c; return list of presentation keys added or None"""
        added = []
        # tilted
        for span, cs, vd in tilted:
            if span >= c:
                continue
            pts = [(c + dx, row) for dx, row in cs]
            nb = 0
            wh = []
            for p in pts:
                if p in black:
                    nb += 1
                else:
                    wh.append(p)
            if nb >= 3:
                return None, added
            if nb == 2:
                if mode != 'N':
                    if vd is not None:
                        p1, p2 = pts[vd[0]], pts[vd[1]]
                        if p1 not in black and p2 not in black and part[p1[1]] != part[p2[1]]:
                            return None, added
                if mode == 'full':
                    key = (min(wh), max(wh))
                    if key in pres:
                        return None, added
                    pres[key] = 1
                    added.append(key)
        if mode == 'full':
            # axis rectangles with max column c, >=2 black corners
            r1, s1 = cols[c - 1]
            for x in range(1, c):
                r0, s0 = cols[x - 1]
                rowsx = (r0, s0)
                rowsc = (r1, s1)
                # choose two rows y1<y2; black count
                cand_rows = set(rowsx) | set(rowsc)
                for y1 in range(1, h + 1):
                    for y2 in range(y1 + 1, h + 1):
                        nb = (y1 in rowsx) + (y2 in rowsx) + (y1 in rowsc) + (y2 in rowsc)
                        if nb < 2:
                            continue
                        wh = []
                        for p in ((x, y1), (x, y2), (c, y1), (c, y2)):
                            if p not in black:
                                wh.append(p)
                        if len(wh) == 0:
                            return None, added
                        if len(wh) == 1:
                            key = (wh[0], wh[0])
                        else:
                            key = (min(wh), max(wh))
                        if key in pres:
                            return None, added
                        pres[key] = 1
                        added.append(key)
        return True, added

    def dfs(c):
        # columns 1..c placed
        nodes[0] += 1
        if nodes[0] % 2000 == 0 and time.time() - t0 > tlimit:
            timeout[0] = True
            return
        if c > best['w']:
            best['w'] = c
            best['ex'] = [list(cols)]
            best['count'] = 1
        elif c == best['w']:
            best['count'] += 1
            if len(best['ex']) < 6:
                best['ex'].append(list(cols))
        if c == q:
            return
        for pr in pairs:
            if pr in used:
                continue
            if timeout[0]:
                return
            cols.append(pr)
            used.add(pr)
            p1 = (c + 1, pr[0])
            p2 = (c + 1, pr[1])
            black.add(p1)
            black.add(p2)
            ok, added = check_new(c + 1)
            if ok:
                dfs(c + 1)
            for k in added:
                del pres[k]
            black.discard(p1)
            black.discard(p2)
            used.discard(pr)
            cols.pop()

    dfs(0)
    return best, nodes[0], timeout[0], time.time() - t0, q


if __name__ == '__main__':
    h = int(sys.argv[1])
    mode = sys.argv[2]
    tl = float(sys.argv[3]) if len(sys.argv) > 3 else 40
    if len(sys.argv) > 4:
        parts = [tuple(int(t) for t in sys.argv[4].split(','))]
    else:
        parts = []
        k = h // 2
        for A in itertools.combinations(range(1, h + 1), k):
            if h % 2 == 0 and 1 not in A:
                continue
            parts.append(A)
    per = tl / max(1, len(parts))
    for A in parts:
        best, nodes, to, el, q = run(h, A, mode, per)
        print('h', h, 'A', A, 'mode', mode, 'q', q, 'maxwidth', best['w'], 'count', best['count'],
              'nodes', nodes, 'timeout', to, 'sec', round(el, 1))
        for ex in best['ex'][:3]:
            print('   ', ' '.join('%d%d' % p if h < 10 else '%d-%d' % p for p in ex))
