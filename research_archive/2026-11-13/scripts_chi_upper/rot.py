"""(1) window count check: max_D |D_T ∩ [D,2D]| versus 8*rho_s(T).
(2) best single rotation: delta*(E) = max_alpha min_{d in E} ||alpha d|| for E = D_T^inf ∩ [1,X]
    (an UPPER bound for the infinite set; 1/delta* lower-bounds rotation colourings)."""
import sys, time
from math import floor, ceil
from dset import dset

def rho_s(T):
    T = abs(T); r = 1; p = 2
    while p * p <= T:
        if T % p == 0:
            e = 0
            while T % p == 0: T //= p; e += 1
            if p % 5 in (1, 4): r *= 2 * e + 1
        p += 1
    if T > 1 and T % 5 in (1, 4): r *= 3
    return r

def wincount(E):
    E = sorted(E); best = 0; j = 0
    for i in range(len(E)):
        while j < len(E) and E[j] <= 2 * E[i]: j += 1
        best = max(best, j - i)
    return best

def feasible(E, delta, cap=200000):
    G = [(0.0, 0.5)]
    for d in E:
        NG = []
        for (a, b) in G:
            j0 = floor(a * d) - 1; j1 = ceil(b * d) + 1
            for j in range(j0, j1 + 1):
                lo = max(a, (j + delta) / d); hi = min(b, (j + 1 - delta) / d)
                if lo < hi: NG.append((lo, hi))
            if len(NG) > cap: return None
        G = NG
        if not G: return False
    return True

def best_delta(E):
    E = sorted(E)
    lo, hi = 0.0, 0.5
    for _ in range(30):
        mid = (lo + hi) / 2
        f = feasible(E, mid)
        if f is None: lo = mid; continue  # too many intervals: certainly feasible-ish; treat as feasible
        if f: lo = mid
        else: hi = mid
    return lo

if __name__ == "__main__":
    Ts = [int(t) for t in sys.argv[1].split(",")]
    X = int(sys.argv[2])
    for T in Ts:
        t0 = time.time()
        D = dset(T, X)
        E = sorted(D)
        r = rho_s(T)
        wc = wincount(E)
        bd = best_delta(E)
        print(f"T={T} rho_s={r} |E|={len(E)} maxwin={wc} 8rho={8*r} delta*={bd:.5f} 1/delta*={1/bd:.2f} t={time.time()-t0:.1f}s", flush=True)
