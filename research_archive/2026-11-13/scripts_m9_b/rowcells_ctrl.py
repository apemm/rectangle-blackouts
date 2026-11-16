"""Control for rowcells.py: drop the R-c cut (2i+1 > 300) and the R-b cut
(rows < T* - 320). D9 and S11 should then report hits, and every D9 hit
should have y_L <= 205 and a base filler (odd offset)."""
import random, math, sys
sys.path.insert(0, ".")
import rowcells as rc

def build2(h, u, iota, sigma, kappa_tau, nslots, seed):
    rnd = random.Random(seed)
    yP = 2 * iota + 1
    r0 = 1 if iota % 2 else 3
    T4 = (2 * sigma + 1) % 4
    add = 32 if T4 == 3 else 48
    Ts = max(y for y in range(1, h + 1) if (y - yP - add) % 64 == 0)
    rho_tau = (u * (iota + sigma) - kappa_tau) % 16
    rho0 = rho_tau % 4
    labels = {}
    for n in range(nslots):
        if (n - rho_tau) % 16 == 0 and rnd.random() < 0.8:
            for _ in range(80):
                i = iota + 32 * rnd.randrange(0, h // 64 + 1)
                s = sigma + 16 * rnd.randrange(-(h // 32), h // 32 + 1)
                j = i + s
                if i >= 4 and j >= 2 and i <= (h + 1) // 2 - 1 and j <= h // 2 - 1:
                    labels[n] = (2 * i + 1, 2 * j + 2); break
    fillers = {n: Ts - 24 + 8 * ((n - rho0) % 4) for n in range(nslots) if n not in labels}
    return r0, labels, fillers, Ts, rho0

h = 1001
for (iota, sigma, kt, seed) in [(2, 5, 3, 1), (7, 3, 1, 2), (1, 1, 6, 4)]:
    r0, labels, fillers, Ts, rho0 = build2(h, 3, iota, sigma, kt, 700, seed)
    rc.build = lambda *a, **k: (r0, labels, fillers, Ts)
    rc.labels_set = set((4 * n, y) for n, ys in labels.items() for y in ys)
    cnt, nl = rc.run(h, 3, iota, sigma, kt, 700, seed)
    # D9 detail: list y_L and filler offset of each hit
    hits = []
    deepL = [(4 * n, y) for n, ys in labels.items() for y in ys]
    for L in deepL:
        for nF, yF in fillers.items():
            F = (4 * nF, yF)
            c = (L[1] - r0) * (F[1] - r0); B_ = -(L[0] + F[0]); C_ = L[0] * F[0] + c
            disc = B_ * B_ - 4 * C_
            if disc < 0: continue
            r = math.isqrt(disc)
            if r * r != disc: continue
            for num in (-B_ + r, -B_ - r):
                if num % 2: continue
                xE = num // 2
                if xE % 4 == 0: continue
                if 1 <= L[1] + F[1] - r0 <= h:
                    hits.append((L[1], (nF - rho0) % 4))
    bad = [x for x in hits if x[0] > 205 or x[1] % 2 == 0]
    print(f"iota={iota} r0={r0} labels={nl} {cnt} D9 yL range={min([x[0] for x in hits], default=None)}..{max([x[0] for x in hits], default=None)} violating_V2-6={len(bad)}")
