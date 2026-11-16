"""Feo with vertex a SAW filler V, P odd label, Q even label in one class (all slots i = iota mod 16 occupied).
Closed form (proved in the write-up): V must be a base filler with v2(yV - yP) = 4; with f' = (yV - yP)/16 (odd),
N = f'(20 f' - T), T = 2s+1, D | N (signed), g = D - 2f' (slot of V minus slot of P), t = D + N/D - 4f' (slot of Q minus slot of P).
Usage: py feo_closed.py h iota [check]   (check compares with feo_formula brute force on a few s)."""
import sys
from math import isqrt
LM = 16
OFF = (-3, -2, -1, 0)

def sdivs(N):
    N = abs(N); out = []
    d = 1
    while d * d <= N:
        if N % d == 0:
            out += [d, -d]
            if d * d != N: out += [N // d, -(N // d)]
        d += 1
    return out

def run(h, iota, s, excl_band=0):
    A = (h + 1) // 2; K = h // 2
    r1 = (2 * iota + 1) % 16
    R0 = max(y for y in range(2, h + 1) if y % 16 == r1)
    T = 2 * s + 1
    labs = [i for i in range(1, A) if i % LM == iota and 0 <= i + s < K]
    S = set(labs)
    hits = []
    for iP in labs:
        yP = 2 * iP + 1
        if yP > R0 - 24 - excl_band: continue
        for a in (1, 3):
            yV = R0 + 8 * OFF[a]
            f = yV - yP
            if f % 32 != 16: continue
            fp = f // 16
            N = fp * (20 * fp - T)
            if N == 0: continue
            for D in sdivs(N):
                g = D - 2 * fp
                if (g - a) % 4: continue
                if (iP + g) in S: continue
                t = D + N // D - 4 * fp
                iQ = iP + t
                if iQ not in S: continue
                yQ = 2 * (iQ + s) + 2
                if excl_band and yQ > R0 - 24 - excl_band: continue
                wy = yP + yQ - yV
                if 1 <= wy <= h:
                    hits.append((iP, g, t, yV))
    return len(labs), hits

if __name__ == '__main__':
    h = int(sys.argv[1]); iota = int(sys.argv[2])
    if len(sys.argv) > 3 and sys.argv[3] == 'check':
        from feo_formula import run as brute
        for s in (-50, -20, 0, 10, 30, 60):
            n, H = run(h, iota, s)
            _, _, B = brute(h, iota, s, brute=True)
            print('s', s, 'closed', sorted(H), 'brute', sorted(B), 'MATCH' if sorted(H) == sorted(B) else 'DIFF')
        sys.exit()
    eb = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nl = 0; tot = 0; per = {}
    K = h // 2
    for s in range(-(h // 2), h // 2):
        n, H = run(h, iota, s, eb)
        nl += n; tot += len(H)
    print('h', h, 'iota', iota, 'labels', nl, 'Feo', tot, 'per label %.4f' % (tot / max(nl, 1)))
