"""Feo with the right angle at the odd label point P (legs P->V filler, P->Q even label of the same class).
Equation: 16 g t + f (T + 2t) = 0, g = nV - nP, t = nQ - nP, f = yV - yP, T = 2s+1.
Brute force over t (Q in class) and closed form check. Fourth corner W = V + Q - P (even row, deep column: fatal).
Usage: py feo_pvertex.py h iota"""
import sys
LM = 16
OFF = (-3, -2, -1, 0)

def run(h, iota, s):
    A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota + 1) % 16
    R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
    T = 2 * s + 1
    labs = [i for i in range(1, A) if i % LM == iota and 0 <= i + s < K]
    S = set(labs)
    hits = []
    for iP in labs:
        yP = 2 * iP + 1
        for iQ in labs:
            t = iQ - iP
            if t == 0: continue
            for a in range(4):
                yV = R0 + 8 * OFF[a]
                f = yV - yP
                if f <= 0: continue
                num = -f * (T + 2 * t)
                if num % (16 * t): continue
                g = num // (16 * t)
                if g == 0 or (g - a) % 4 or (iP + g) in S: continue
                yQ = 2 * (iQ + s) + 2
                wy = yV + yQ - yP
                if 1 <= wy <= h:
                    hits.append((iP, iQ, g, yV, f))
    return len(labs), hits

h = int(sys.argv[1]); iota = int(sys.argv[2])
nl = 0; tot = 0; ex = []
for s in range(-(h // 2), h // 2):
    n, H = run(h, iota, s); nl += n; tot += len(H)
    if H and len(ex) < 5: ex.append((s, H[:2]))
print('h', h, 'labels', nl, 'Feo(P vertex)', tot, 'per label %.4f' % (tot / nl))
for e in ex: print('  ', e)
