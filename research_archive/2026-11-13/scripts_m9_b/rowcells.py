"""Sanity check of row-only cells at stride 4u (u = 3) on one region with
random label occupancy of the offset-0 slots n = rho_tau (mod 16).
Cells: B8 (rival pair with a shallow point), D9 (Pb, one label + one filler,
shallow vertex), S11 (shallow end, filler vertex, label end), S12 (shallow end,
filler vertex, filler end). Expected count of in-grid configurations: 0.
Control: labels moved to offset 2 (wrong rho0) should produce hits.
"""
import random, math, sys

def build(h, u, iota, sigma, kappa_tau, nslots, seed, off_shift=0):
    rnd = random.Random(seed)
    yP = 2 * iota + 1
    r0 = 1 if iota % 2 else 3
    # T = 2s+1 mod 4 from sigma
    T4 = (2 * sigma + 1) % 4
    add = 32 if T4 == 3 else 48
    T0 = max(y for y in range(1, h + 1) if (y - yP - add) % 64 == 0)
    Ts = T0  # k_tau = 0
    rho_tau = (u * (iota + sigma) - kappa_tau) % 16
    rho0 = rho_tau % 4
    labels = {}  # slot -> (yodd, yeven)
    for n in range(nslots):
        if (n - rho_tau - off_shift) % 16 == 0 and rnd.random() < 0.6:
            # random label of the type, kept rows: 2i+1 > 300, rows < Ts-320
            for _ in range(50):
                i = iota + 32 * rnd.randrange(0, h // 64 + 1)
                s = sigma + 16 * rnd.randrange(-(h // 32), h // 32 + 1)
                j = i + s
                yo, ye = 2 * i + 1, 2 * j + 2
                if 2 * i + 1 > 300 and j >= 2 and yo < Ts - 320 and ye < Ts - 320 and i <= (h + 1) // 2 - 1 and j <= h // 2 - 1:
                    labels[n] = (yo, ye)
                    break
    fillers = {}
    for n in range(nslots):
        if n not in labels:
            fillers[n] = Ts - 24 + 8 * ((n - rho0) % 4)
    return r0, labels, fillers, Ts

def black(x, y, r0, labels, fillers, h):
    if y < 1 or y > h:
        return None
    if x % 4:
        return y == r0
    n = x // 4
    if n in labels:
        return y in labels[n]
    if n in fillers:
        return y == fillers[n]
    return None  # outside window: unknown

def rival(p, q, h):
    (x1, y1), (x2, y2) = p, q
    lo, hi = min(y1, y2), max(y1, y2)
    d = hi - lo
    if d % 2 == 0:
        return False
    t2 = (x1 - x2) ** 2
    j = 1
    while lo - j >= 1 and hi + j <= h:
        if 4 * j * (d + j) == t2:
            return True
        j += 1
    return False

def run(h, u, iota, sigma, kappa_tau, nslots, seed, off_shift=0):
    r0, labels, fillers, Ts = build(h, u, iota, sigma, kappa_tau, nslots, seed, off_shift)
    deepL = [(4 * n, y) for n, ys in labels.items() for y in ys]
    deepF = [(4 * n, y) for n, y in fillers.items()]
    X = 4 * nslots
    shallow = [(x, r0) for x in range(X) if x % 4]
    cnt = {"B8": 0, "D9": 0, "S11": 0, "S12": 0}
    # B8: rival pairs shallow-deep (j <= 2 since lo = r0 <= 3)
    for (xs, ys) in shallow:
        for (xd, yd) in deepL + deepF:
            if abs(xs - xd) <= 2 * h and rival((xs, ys), (xd, yd), h):
                cnt["B8"] += 1
    # D9: shallow vertex E, ends L (label point) and F (filler)
    for L in deepL:
        for F in deepF:
            # (xL-xE)(xF-xE) + (yL-r0)(yF-r0) = 0 -> xE^2 - (xL+xF)xE + xL xF + c = 0
            c = (L[1] - r0) * (F[1] - r0)
            B_, C_ = -(L[0] + F[0]), L[0] * F[0] + c
            disc = B_ * B_ - 4 * C_
            if disc < 0:
                continue
            r = math.isqrt(disc)
            if r * r != disc:
                continue
            for num in (-B_ + r, -B_ - r):
                if num % 2:
                    continue
                xE = num // 2
                if xE % 4 == 0:
                    continue
                W = (L[0] + F[0] - xE, L[1] + F[1] - r0)
                if 1 <= W[1] <= h:
                    cnt["D9"] += 1
    # S11 / S12: shallow end E, filler vertex V, deep end G
    for V in deepF:
        for G in deepL + deepF:
            if G == V:
                continue
            dx, dy = G[0] - V[0], G[1] - V[1]
            if dx == 0:
                continue
            # (xE - xV) dx + (r0 - yV) dy = 0
            numr = -(r0 - V[1]) * dy
            if numr % dx:
                continue
            xE = V[0] + numr // dx
            if xE % 4 == 0:
                continue
            W = (xE + dx, r0 + dy)
            if 1 <= W[1] <= h:
                key = "S11" if G in labels_set else "S12"
                cnt[key] += 1
    return cnt, len(labels)

if __name__ == "__main__":
    h = 1001
    tot = {}
    for (iota, sigma, kt, seed) in [(2, 5, 3, 1), (7, 3, 1, 2), (4, 10, 0, 3), (1, 1, 6, 4)]:
        for shift in (0, 8, 2):
            r0, labels, fillers, Ts = build(h, 3, iota, sigma, kt, 700, seed, shift)
            labels_set = set((4 * n, y) for n, ys in labels.items() for y in ys)
            globals()["labels_set"] = labels_set
            cnt, nl = run(h, 3, iota, sigma, kt, 700, seed, shift)
            print(f"iota={iota} sigma={sigma} r0={r0} shift={shift} labels={nl} {cnt}")
            sys.stdout.flush()
