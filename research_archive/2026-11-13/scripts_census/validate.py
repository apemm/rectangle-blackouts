"""Validate the anchored checker against naive searches on small random boards.
(1) Set equality of every obstruction kind (all anchors) against a naive enumeration of all
    rectangles and all mixed pairs of the h x m grid, on random black sets.
(2) Validity: on random equality boards (all parity edges as distinct doubles), 'some (V1)-(V5)
    violation' must agree with 'two distinct rectangles share a presentation'."""
import sys, random, time
from math import gcd
from itertools import combinations
from checker import Board, census


def all_rects(h, m):
    pts = [(x, y) for x in range(m) for y in range(1, h + 1)]
    R = set()
    for P in pts:
        for Q in pts:
            if Q <= P:
                continue
            ux, uy = Q[0] - P[0], Q[1] - P[1]
            g = gcd(abs(ux), abs(uy))
            vx, vy = -uy // g, ux // g
            for k in range(1, h + m + 2):
                for s in (1, -1):
                    P2 = (P[0] + s * k * vx, P[1] + s * k * vy); Q2 = (Q[0] + s * k * vx, Q[1] + s * k * vy)
                    if all(0 <= z[0] < m and 1 <= z[1] <= h for z in (P2, Q2)):
                        R.add(frozenset((P, Q, Q2, P2)))
    return R


def tilted(rect):
    xs = sorted(set(z[0] for z in rect)); ys = sorted(set(z[1] for z in rect))
    return not (len(xs) == 2 and len(ys) == 2)


def diagonals(rect):
    c = list(rect)
    out = []
    for a, b in combinations(c, 2):
        others = [z for z in c if z != a and z != b]
        if a[0] + b[0] == others[0][0] + others[1][0] and a[1] + b[1] == others[0][1] + others[1][1]:
            out.append((a, b))
    return out


def sides(rect):
    d = diagonals(rect)
    ds = set(frozenset(x) for x in d)
    return [tuple(p) for p in combinations(rect, 2) if frozenset(p) not in ds]


def naive(S, h, m, rects):
    blk = lambda z: z in S
    def park(W):
        return all((y - W[1]) % 2 == 0 for (x, y) in S if x == W[0])
    V1 = set(); V2 = set(); parkedW = {}
    for r in rects:
        if not tilted(r):
            continue
        nb = sum(1 for z in r if blk(z))
        if nb == 4:
            V1.add(r)
        elif nb == 3:
            W = [z for z in r if not blk(z)][0]
            if park(W):
                parkedW.setdefault(W, set()).add(r)
            else:
                V2.add(r)
    V3 = set(W for W, s in parkedW.items() if len(s) >= 2)
    bydiag = {}; byside = {}
    for r in rects:
        for d in diagonals(r):
            bydiag.setdefault(frozenset(d), []).append(r)
        for s_ in sides(r):
            byside.setdefault(frozenset(s_), []).append(r)
    V4 = set(); V5 = set()
    for pq, R1s in byside.items():
        for R2 in bydiag.get(pq, []):
            for R1 in R1s:
                if len(R1 & R2) != 2:
                    continue
                AB = R1 - pq; CD = R2 - pq
                sup = AB | CD
                if len(sup) != 4 or not all(blk(z) for z in sup):
                    continue
                a, b = list(AB)
                if a[0] == b[0]:
                    pass  # vertical side: covered by rival pairs below
                else:
                    V4.add(frozenset(sup))
    for r in rects:
        if not tilted(r):
            continue
        for (p, q) in diagonals(r):
            if p[0] == q[0] and (p[1] - q[1]) % 2 != 0:
                CD = r - {p, q}
                if all(blk(z) for z in CD):
                    V5.add(frozenset(CD))
    return V1, V2, V3, V4, V5


def fast(S, h, m):
    b = Board(h, m)
    for (x, y) in S:
        b.put(x, y, 'x')
    whites = [(x, y) for x in range(m) for y in range(1, h + 1) if (x, y) not in S]
    res = census(b, sorted(S), whites, grid=True)
    return (set(res['V1'].keys()), set(res['V2'].keys()), set(res['V3'].keys()),
            set(res['V4'].keys()), set(res['V5'].keys()))


def presentations_collide(S, h, m, rects):
    seen = {}
    for r in rects:
        pres = frozenset(z for z in r if z not in S)
        if pres in seen:
            return True
        seen[pres] = r
    return False


def random_equality_board(h, m, rng):
    odd = [y for y in range(1, h + 1) if y % 2]; even = [y for y in range(1, h + 1) if y % 2 == 0]
    edges = [(o, e) for o in odd for e in even]
    if m < len(edges):
        return None
    cols = list(range(m)); rng.shuffle(cols)
    S = set()
    for c, (o, e) in zip(cols, edges):
        S.add((c, o)); S.add((c, e))
    for c in cols[len(edges):]:
        S.add((c, rng.randint(1, h)))
    return S


if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    t = time.time()
    # part 1: kind-level set equality
    nb = 0; tot = [0] * 5
    for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
        h = rng.randint(4, 7); m = rng.randint(5, 14)
        rows = rng.sample(range(1, h + 1), rng.randint(2, h))
        S = set()
        for x in range(m):
            k = rng.choice([1, 1, 2])
            for y in rng.sample(rows, min(k, len(rows))):
                S.add((x, y))
        rects = all_rects(h, m)
        A = naive(S, h, m, rects); B = fast(S, h, m)
        for i in range(5):
            tot[i] += len(A[i])
            if A[i] != B[i]:
                print('MISMATCH kind', i + 1, 'h', h, 'm', m, 'naive-fast', list(A[i] - B[i])[:3], 'fast-naive', list(B[i] - A[i])[:3])
                sys.exit(1)
        nb += 1
    print('part1 boards', nb, 'naive counts V1..V5 total', tot, 'all equal; time %.1f' % (time.time() - t))
    # part 2: validity agreement on equality boards
    agree = 0; valid = 0; n = 0; RC = {}
    for trial in range(int(sys.argv[3]) if len(sys.argv) > 3 else 40):
        h = 4 if trial % 4 else 5; q = ((h + 1) // 2) * (h // 2)
        m = rng.choice([6, 7, 8]) if h == 4 else rng.choice([8, 9, 10])
        S = random_equality_board(h, m, rng)
        rects = RC.get((h, m)) or RC.setdefault((h, m), all_rects(h, m))
        col = presentations_collide(S, h, m, rects)
        B = fast(S, h, m)
        viol = any(len(z) for z in B)
        n += 1
        if col == viol:
            agree += 1
        else:
            print('DISAGREE h', h, 'm', m, 'collision', col, 'violations', [len(z) for z in B], sorted(S))
            sys.exit(1)
        valid += (not col)
    print('part2 equality boards', n, 'agree', agree, 'valid', valid, 'time %.1f' % (time.time() - t))
