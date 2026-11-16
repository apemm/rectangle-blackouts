# Sanity check: greedy increasing transversal chain x_T (one label per diagonal).
# Conflict: x_T - x_T' = d in S_T, where 16 d^2 + (T+2d)^2 = L^2, L odd, 0 < L < h.
import sys, math, time

def kill_sets(h):
    A = (h + 1) // 2
    K = h // 2
    Tmin, Tmax = -(2 * A - 3), 2 * K - 1   # T = 2s+1, s in (-A, K)
    S = {}
    u = 2
    while u * u + 1 < h:
        for v in range(1, u):
            if (u - v) % 2 == 0 or math.gcd(u, v) != 1:
                continue
            l0 = u * u + v * v
            if l0 >= h:
                break
            g = 1
            while g * l0 < h:
                d0 = g * u * v // 2
                w0 = g * (u * u - v * v)
                for sd in (1, -1):
                    for sw in (1, -1):
                        d = sd * d0
                        T = sw * w0 - 2 * d
                        if Tmin <= T <= Tmax:
                            S.setdefault(T, set()).add(d)
                g += 2
        u += 1
    return A, K, Tmin, Tmax, S

def greedy(h):
    A, K, Tmin, Tmax, S = kill_sets(h)
    size = 64 * h
    occ = bytearray(size)
    killed = bytearray(size)
    x = 0
    first = None
    tot = 0
    for T in range(Tmin, Tmax + 1, 2):
        ds = S.get(T, ())
        tot += len(ds)
        pos = [d for d in ds if d > 0]
        neg = [-d for d in ds if d < 0]
        x += 1
        while True:
            if killed[x]:
                x += 1
                continue
            ok = True
            for d in pos:
                if x - d >= 0 and occ[x - d]:
                    ok = False
                    break
            if ok:
                break
            x += 1
        occ[x] = 1
        if first is None:
            first = x
        for d in neg:
            killed[x + d] = 1
    R = x - first
    n = (Tmax - Tmin) // 2 + 1
    return A, n, R, tot

if __name__ == "__main__":
    t0 = time.time()
    for h in (64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384):
        A, n, R, tot = greedy(h)
        print(h, "diagonals", n, "sum|S_T|", tot, "mean", round(tot / n, 3),
              "R", R, "R/h", round(R / h, 3), "classes<=A+R+1", A + R + 1,
              "per h", round((A + R + 1) / h, 3), "t", round(time.time() - t0, 1))
