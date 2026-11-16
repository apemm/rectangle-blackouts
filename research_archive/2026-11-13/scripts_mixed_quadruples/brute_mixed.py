"""Brute-force mixed quadruples among label points of a stride-s one-prime scaffold.

Blocks c = 0..nb-1, each a FULL constant-offset diagonal T_c (superset of any class).
Label slot i (0<=i<A, 0<=i+s_T<K): odd point (s(i+P c), 2i+1), even point (s(i+P c), 2i+1+T).
Mixed quadruple (paper Def. obstruction (2), Lemma mixedeq): pairs {A,B}, {C,D}, AB not vertical,
|D-C| = |B-A|, C+D-A-B = 2n with n integral, nonzero, n.(B-A)=0, D-C != +-(B-A),
and p=A+n, q=B+n have rows in [1,h] (corners of the strip).
Classify every found quadruple by block pattern and parity pattern.
usage: py brute_mixed.py h s nb seed [T0 T1 ...]
"""
import sys, random
from collections import defaultdict, Counter

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def main():
    h, s, nb, seed = map(int, sys.argv[1:5])
    rng = random.Random(seed)
    A = (h + 1) // 2; K = h // 2
    p = max(20 * h, (s * s // 2 + 4) * h) + 1
    while not isprime(p): p += 1
    P = p
    Ts = [int(t) for t in sys.argv[5:]]
    while len(Ts) < nb:
        T = rng.randrange(-h + 2, h, 2) | 1
        if abs(T) < h: Ts.append(T)
    pts = []  # (x, y, block, slot, parity)
    for c, T in enumerate(Ts):
        st = (T - 1) // 2
        for i in range(A):
            j = i + st
            if 0 <= j < K:
                x = s * (i + P * c)
                pts.append((x, 2 * i + 1, c, i, 0))
                pts.append((x, 2 * j + 2, c, i, 1))
    W = (h - 1) ** 2 // 4 + 1
    groups = defaultdict(list)
    n = len(pts)
    for a in range(n):
        for b in range(a + 1, n):
            ux = pts[b][0] - pts[a][0]; uy = pts[b][1] - pts[a][1]
            if abs(ux) > 2 * W + 2: continue
            groups[ux * ux + uy * uy].append((a, b))
    found = []
    for L, prs in groups.items():
        if len(prs) < 2: continue
        for (a, b) in prs:
            A_ = pts[a]; B_ = pts[b]
            ux = B_[0] - A_[0]; uy = B_[1] - A_[1]
            if ux == 0: continue  # vertical side: rival pair, not a mixed quadruple
            for (c, d) in prs:
                if len({a, b, c, d}) < 4: continue
                C_ = pts[c]; D_ = pts[d]
                nx2 = C_[0] + D_[0] - A_[0] - B_[0]; ny2 = C_[1] + D_[1] - A_[1] - B_[1]
                if nx2 % 2 or ny2 % 2: continue
                nx, ny = nx2 // 2, ny2 // 2
                if nx == 0 and ny == 0: continue
                if nx * ux + ny * uy != 0: continue
                vx = D_[0] - C_[0]; vy = D_[1] - C_[1]
                if (vx, vy) in ((ux, uy), (-ux, -uy)): continue
                if not (1 <= A_[1] + ny <= h and 1 <= B_[1] + ny <= h): continue
                found.append((a, b, c, d))
    print("h", h, "s", s, "P", P, "offsets", Ts, "points", n, "mixed quadruples", len(found))
    pat = Counter()
    for (a, b, c, d) in found:
        bl = (pts[a][2], pts[b][2], pts[c][2], pts[d][2])
        par = (pts[a][4], pts[b][4], pts[c][4], pts[d][4])
        if len(set(bl)) == 1: typ = "one-block"
        elif bl[0] == bl[1] and bl[2] == bl[3]: typ = "I.2 (AB in one block, CD in another)"
        elif bl[0] == bl[2] and bl[1] == bl[3]: typ = "II (A,C | B,D)"
        elif bl[0] == bl[3] and bl[1] == bl[2]: typ = "II (A,D | B,C)"
        else: typ = "OTHER " + str(bl)
        pat[(typ, par[0] + par[1], par[2] + par[3], "AC-sameslot" if (pts[a][2], pts[a][3]) == (pts[c][2], pts[c][3]) else "")] += 1
    for k, v in sorted(pat.items()): print(v, k)
    for q in found[:6]:
        print([pts[t] for t in q])

main()
