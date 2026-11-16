"""Bad-row sets for the two one-label families that survive SAW (row-1 sea types, r1 = 3 mod 4).
I_bad: odd label rows y_B = 2i+1 (i = iota mod 16) in an M2c with one SAW filler D (Theorem 2 of block_sea).
J_bad: even label rows y_e with a rival SAW filler (Lemma rival), label column at SAW offset 0.
SAW: filler at slot offset a (mod 4) has row T + 8*OFF[a mod 4], OFF = (-3,-2,-1,0), T = max{y<=h: y = r1 mod 16}."""
import sys
from math import isqrt
OFF = (-3, -2, -1, 0)
def divisors(n):
    n = abs(n); out = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d * d != n: out.append(n // d)
        d += 1
    return out
def run(h, iota, r1):
    T = max(y for y in range(1, h + 1) if y % 16 == r1)
    rows = [T + 8 * o for o in OFF]
    low = min(rows)
    Ibad = []
    for i in range(1, (h + 1) // 2):
        if i % 16 != iota: continue
        yB = 2 * i + 1
        if yB >= low - 40: continue
        u2 = yB - 1; hit = False
        for a, yD in enumerate(rows):
            e2 = yD - yB
            if e2 <= 0 or e2 % 2: continue
            e = e2 // 2
            if yB + e > h: continue
            N = e * u2
            for d in divisors(N):
                for n1 in (d, -d):
                    z = -N // n1
                    if z % 4 == 0 or (2 * n1 - z) % 4 == 0: continue
                    # n1*D^2 - (2 n1^2 + N) D + n1^3 + n1 e^2 + 2 N n1 = 0
                    A_ = n1; B_ = -(2 * n1 * n1 + N); C_ = n1 ** 3 + n1 * e * e + 2 * N * n1
                    disc = B_ * B_ - 4 * A_ * C_
                    if disc < 0: continue
                    s = isqrt(disc)
                    if s * s != disc: continue
                    for sg in (1, -1):
                        num = -B_ + sg * s
                        if num % (2 * A_): continue
                        Dl = num // (2 * A_)
                        if Dl % 4: continue
                        if (Dl // 4) % 4 != a: continue
                        hit = True
        if hit: Ibad.append(i)
    Jbad = []
    for ye in range(2, low - 40, 2):
        hit = False
        amax = isqrt(h * (h + 2 * h)) // 2 + 2 if ye > min(rows) else isqrt((h - min(rows) + 1) * (h + 50)) // 2 + 2
        for a in range(1, amax):
            for sg in (1, -1):
                yF = rows[(sg * a) % 4]
                d = abs(yF - ye); lo, hi = min(yF, ye), max(yF, ye)
                t = 4 * a
                L = isqrt(d * d + t * t)
                if L * L != d * d + t * t: continue
                jj = (L - d) // 2
                if jj >= 1 and lo - jj >= 1 and hi + jj <= h: hit = True
        if hit: Jbad.append(ye)
    return T, Ibad, Jbad
for h in [int(a) for a in sys.argv[1].split(',')]:
    tot_i = 0
    out = []
    for iota in (1, 9):
        T, Ib, Jb = run(h, iota, 3)
        out.append((iota, len(Ib), Ib[:8]))
    print('h', h, 'T', T, 'M2c bad odd rows per residue:', out, 'rival bad even rows:', len(Jb), 'of', (T - 64) // 2)
