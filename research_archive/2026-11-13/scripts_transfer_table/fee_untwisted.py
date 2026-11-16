# Shape-level search for a Fee right triple (even label vertex E1, even label end E2,
# hole filler V) in the stride-12 board L***(3), under the untwisted placement
# rho_s = p^{-1}(s - kappa) mod 16l, and under the twisted one rho_s = p^{-1}(u s - kappa).
# Only layout positions and rows are checked; occupancy (which labels the colouring puts
# in the k = 0 class) is not modelled.
import sys

def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2; r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def legendre(a, q):
    return pow(a % q, (q - 1) // 2, q)

u = 3
h = 4_000_000
A, K = (h + 1) // 2, h // 2
kappa, b = 0, 0
iota, sigma = 5, 3            # type: i = 5 mod 32, s = 3 mod 16  -> T = 7 mod 32, T = 3 mod 4
yP = 2 * iota + 1
T = 2 * sigma + 1
off = 32 if T % 4 == 3 else 48
Tstar = max(y for y in range(h - 70, h + 1) if (y - yP - off) % 64 == 0)
yV = Tstar - 24               # hole row (offset 0)
alpha = u * 32                # V sits at the slot of label i1 + 32 of E1's class (a hole)

def rho(s, p, l, twisted):
    m = 16 * l
    return (pow(p, -1, m) * ((u * s if twisted else s) - kappa)) % m

def search(twisted, max_pairs=60):
    found = []
    pairs = 0
    p = 80 * h + 1
    while pairs < max_pairs and p < 160 * h:
        p += 2
        if p % 4 != 3 or not is_prime(p) or legendre(37, p) != p - 1:
            continue
        # one l per p, chosen so that the dt = 16 partner diagonal is in range
        for l in range(int(1.04 * h) + 1, int(2.08 * h)):
            if not is_prime(l) or legendre(37, l) != l - 1:
                continue
            m = 16 * l
            # dt = 16: p*dt = (u*)Ds (mod 16l)
            if twisted:
                Ds_res = (16 * p * pow(u, -1, m)) % m
            else:
                Ds_res = (16 * p) % m
            Ds = Ds_res if Ds_res < m // 2 else Ds_res - m
            if abs(Ds) < h // 4 and Ds % 16 == 0:
                break
        else:
            continue
        pairs += 1
        DM = 16 * p
        Dnu = u * Ds - DM
        # d = yV - y_E1 with y_E1 = 2 j1 + 2, j1 = i1 + s0, i1 = iota (32), s0 = sigma (16)
        # => j1 = iota + sigma (mod 16)
        for j1 in range(5000 // 2, (yV - 5000) // 2):
            if (j1 - iota - sigma) % 16:
                continue
            d = yV - (2 * j1 + 2)
            den = 8 * u * alpha + d
            num = 8 * alpha * Dnu
            if num % den:
                continue
            eta = -num // den  # eta (8 u alpha + d) = -8 alpha * (-Dnu)?  fixed below by check
            for eta in (num // den, -(num // den)):
                if eta == 0 or abs(eta) >= K or (eta - Ds) % 32:
                    continue
                found.append((p, l, Ds, j1, d, eta))
    return found, pairs

def verify(p, l, Ds, j1, d, eta, twisted):
    # build the actual points and test every condition
    m = 16 * l
    for i1 in range(iota, A, 32):
        s0 = j1 - i1
        if s0 % 16 != sigma or not (-(A - 1) <= s0 <= K - 1):
            continue
        s1 = s0 + Ds
        j2 = j1 + eta
        i2 = j2 - s1
        if not (0 <= i2 < A and 0 <= j2 < K and 0 <= i2 + 32 < A and 0 <= j2 + 32 < K):
            continue
        if not (-(A - 1) <= s1 <= K - 1):
            continue
        t0, t1 = rho(s0, p, l, twisted), rho(s1, p, l, twisted)
        if t1 - t0 != 16:
            continue
        M0, M1 = p * t0 + b, p * t1 + b
        E1 = (4 * (u * i1 + M0), 2 * j1 + 2)
        E2 = (4 * (u * i2 + M1), 2 * j2 + 2)
        V = (E1[0] + 4 * alpha, yV)
        W = (V[0] + E2[0] - E1[0], V[1] + E2[1] - E1[1])
        dotp = (V[0] - E1[0]) * (E2[0] - E1[0]) + (V[1] - E1[1]) * (E2[1] - E1[1])
        Wlabel_col = 4 * (u * (i2 + 32) + M1)
        ok = (dotp == 0 and W[0] == Wlabel_col and 1 <= W[1] <= h and V[0] == 4 * (u * (i1 + 32) + M0))
        if ok:
            return dict(i1=i1, s0=s0, j1=j1, i2=i2, s1=s1, j2=j2, t0=t0, t1=t1, E1=E1, E2=E2, V=V, W=W,
                        W_row_vs_label=(W[1], 2 * (i2 + 32) + 1, 2 * (j2 + 32) + 2))
    return None

for twisted in (False, True):
    found, pairs = search(twisted)
    print("twisted" if twisted else "untwisted", "prime pairs tried:", pairs, "shape solutions:", len(found))
    shown = 0
    for f in found:
        v = verify(*f, twisted)
        if v:
            print("  verified instance: p=%d l=%d Ds=%d d=%d eta=%d" % (f[0], f[1], f[2], f[4], f[5]))
            print("  ", v)
            shown += 1
            if shown >= 2:
                break
    sys.stdout.flush()
