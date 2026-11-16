"""Seam rival pairs SAW*-type filler layer | Sea(r0,g), as in J1(e).
Filler rows c = T* - 24 + 8o (o = offset 0..3), T* = h - D, D = D0 + 64k.
Buffer: deep columns (slot n >= n0 on the right end, n < n0' on the left end) hold row g.
Rival pair {filler (4n, c), buffer (4(n+kap), g)}: by Lemma rival, j >= 1 with
lower - j >= 1, upper + j <= h, and 4j(|g-c| + j) = (4 kap)^2.
For each case (h mod 4, sea row) and each D0 in [0,63] of the right residue,
find the least shift k in 0..3 for which end phases exist that avoid every bad pair.
Also cross-check the closed form against a brute force over actual rectangle geometry.
"""
import math, itertools

def g_of(h):
    if h % 2 == 0: return h
    return h - 1 if h % 4 == 1 else h - 3

def bad_pairs(h, D):
    g = g_of(h); Ts = h - D
    out = []
    for o in range(4):
        c = Ts - 24 + 8 * o
        lo, hi = min(c, g), max(c, g)
        d = hi - lo
        if d % 2 == 0: continue
        for j in range(1, h - hi + 1):
            if lo - j < 1: break
            v = j * (d + j)
            if v % 4: continue
            k2 = v // 4; kap = math.isqrt(k2)
            if kap * kap == k2 and kap >= 1:
                out.append((o, kap, j))
    return out

def right_ok(phi, bads):
    # SAW slots n < n0, phase phi = n0 - rho0 mod 4; filler at n in [n0-kap, n0-1] with offset o is bad
    for o, kap, j in bads:
        for r in range(1, kap + 1):
            if (phi - r) % 4 == o: return False
    return True

def left_ok(phi, bads):
    # SAW slots n >= n0', phi = n0' - rho0; filler at n in [n0', n0'+kap-1] with offset o is bad
    for o, kap, j in bads:
        for r in range(0, kap):
            if (phi + r) % 4 == o: return False
    return True

def brute_pairs(h, D, kmax=12):
    """Geometric brute force: filler at (0,c), buffer point at (4kap, g); test every tilted
    rectangle with diagonal CD whose other diagonal is vertical with lattice ends in rows 1..h,
    rows of p,q of different parity."""
    g = g_of(h); Ts = h - D; out = []
    for o in range(4):
        c = Ts - 24 + 8 * o
        for kap in range(1, kmax + 1):
            x2, y2 = 4 * kap, g
            L2 = x2 * x2 + (y2 - c) ** 2
            L = math.isqrt(L2)
            if L * L != L2: continue
            # vertical diagonal through midpoint, length L
            mx2, my2 = x2, c + y2  # doubled midpoint
            if mx2 % 2: continue
            if (my2 + L) % 2: continue
            yp, yq = (my2 + L) // 2, (my2 - L) // 2
            if yq < 1 or yp > h: continue
            if (yp - yq) % 2 == 0: continue
            out.append((o, kap))
    return sorted(set(out))

h_by_case = {1: 4001, 3: 4003}
report = []
for hm in (1, 3):
    h = h_by_case[hm]
    for r0, r1mod4 in ((1, 3), (3, 1)):
        for D0 in range(64):
            if (h - D0) % 4 != r1mod4: continue
            # cross-check closed form vs brute force for k = 0..3
            for k in range(4):
                bp = sorted(set((o, kap) for o, kap, j in bad_pairs(h, D0 + 64 * k)))
                bb = brute_pairs(h, D0 + 64 * k)
                assert bp == bb, (h, r0, D0, k, bp, bb)
            best = None
            for k in range(4):
                bads = bad_pairs(h, D0 + 64 * k)
                R = [p for p in range(4) if right_ok(p, bads)]
                Lp = [p for p in range(4) if left_ok(p, bads)]
                if R and Lp:
                    best = (k, bads, R, Lp); break
            report.append((hm, r0, D0, best))

need = [(hm, r0, D0, b) for hm, r0, D0, b in report if b is None or b[0] > 0]
print("cases checked:", len(report))
print("cases needing a shift (k>0) or failing:")
for x in need: print(x)
fails = [x for x in report if x[3] is None]
print("fails:", len(fails))
kap4 = [(hm, r0, D0, [b for b in bad_pairs(h_by_case[hm], D0) if b[1] >= 4]) for hm, r0, D0, _ in report]
print("k=0 cases with kappa>=4:", [(a, b, c, d) for a, b, c, d in kap4 if d])
