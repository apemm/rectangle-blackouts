"""Feo (V filler vertex; P odd label, Q even label, same class) count by the divisor formula.
Class: labels at all i = iota mod LM (1 <= i < A, 0 <= i+s < K), slot n = i (M = 0), SAW rows by (n - iota) mod 4:
row(n) = R0 + 8*off[(n - iota) % 4], off = (-3,-2,-1,0), R0 = max{y <= h: y = 2*iota+1 mod 16}.
Right angle at V: 16 g (t - g) + f (2t - kappa) = 0, f = yV - yP, kappa = yV - yeP, g = nV - nP, t = nQ - nP.
Brute force over g (|g| <= G) as a check of the closed form t = D + N/D - 4f'."""
import sys
LM = 16
OFF = (-3, -2, -1, 0)

def run(h, iota, s, brute=False):
    A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota + 1) % 16
    R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
    labs = [i for i in range(1, A) if i % LM == iota and 0 <= i + s < K]
    S = set(labs)
    hits = []
    for iP in labs:
        yP = 2 * iP + 1; yeP = 2 * (iP + s) + 2
        if brute:
            G = h * h // 8
            for g in range(-G, G + 1):
                if g == 0: continue
                nV = iP + g
                if nV in S: continue
                yV = R0 + 8 * OFF[(nV - iota) % 4]
                f = yV - yP; kap = yV - yeP
                num = 16 * g * g + f * kap; den = 16 * g + 2 * f
                if den == 0 or num % den: continue
                t = num // den
                iQ = iP + t
                if iQ not in S: continue
                yQ = 2 * (iQ + s) + 2
                wy = yP + yQ - yV
                if 1 <= wy <= h:
                    hits.append((iP, g, t, yV))
    return R0, len(labs), hits

if __name__ == '__main__':
    h = int(sys.argv[1]); iota = int(sys.argv[2])
    tot = 0; nl = 0
    for s in [int(a) for a in sys.argv[3].split(',')]:
        R0, n, hits = run(h, iota, s, brute=True)
        tot += len(hits); nl += n
        print('s', s, 'labels', n, 'Feo(V vertex)', len(hits), hits[:6])
    print('h', h, 'labels', nl, 'Feo', tot)
