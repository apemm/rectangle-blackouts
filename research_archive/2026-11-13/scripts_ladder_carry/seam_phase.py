import sys
from lad import eta_array
Ep, t0min, t0max = map(int, sys.argv[1:4]); E, P = eta_array(Ep)
vals = sorted(set(E.tolist()))
def divpairs(n):
    n0 = abs(n); out = []; d = 1
    while d * d <= n0:
        if n0 % d == 0:
            for x in {d, n0 // d}:
                for sx in (1, -1):
                    out.append((sx * x, n // (sx * x)))
        d += 1
    return out
def shapes(t0):
    res = []
    for Q1 in range(P):
        s1 = t0 - 8 * int(E[Q1])
        for v2 in vals:
            m8 = (t0 - 8 * v2) - s1
            m = m8 // 8
            if m == 0: continue
            N = m * (s1 + 4 * m)
            for X, Y in divpairs(N):
                if (X + Y) % 2: continue
                a = (X + Y) // 2; c = (Y - X) // 2
                if a == 0 or (m * s1) % (2 * a): continue
                t = -m * s1 // (2 * a) - X
                if t % 2: continue
                Dl = t // 2
                if E[(Q1 + Dl) % P] != v2: continue
                res.append((Q1, Dl, a, c))
    return res
safe = []
for t0 in range(t0min, t0max + 1, 2):
    sh = shapes(t0)
    badR = set(); badL = set(); full = False
    for Q1, Dl, a, c in sh:
        if a < 0 and c < 0 and c < Dl < -a:      # LAD left, buffer right: z0 in (max(Q1,Q1+Dl), min(Q1-a, Q1+Dl-c)]
            lo = Q1 + max(0, Dl); hi = Q1 + min(-a, Dl - c)
            if hi - lo >= P: full = True
            for z in range(lo + 1, min(hi, lo + P) + 1): badR.add(z % P)
        if a > 0 and c > 0 and -a < Dl < c:      # buffer left, LAD right: first LAD slot z0' in (max(Q1-a, Q1+Dl-c), min(Q1, Q1+Dl)]
            lo = Q1 + max(-a, Dl - c); hi = Q1 + min(0, Dl)
            if hi - lo >= P: full = True
            for z in range(lo + 1, min(hi, lo + P) + 1): badL.add(z % P)
    gR = P - len(badR); gL = P - len(badL)
    print('t0=%4d shapes=%3d  good right-end phases %3d  good left-end phases %3d' % (t0, len(sh), gR, gL))
    if gR > 0 and gL > 0: safe.append(t0)
print('t0 with good phases at both ends:', safe)
