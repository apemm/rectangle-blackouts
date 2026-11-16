"""Four-filler mixed quadruples in a periodic one-point-per-slot layer (pure gap).
Coordinates (X, eta): slot X, row = T* - 8 eta; metric X^2 + 4 eta^2 (similar to the true one).
Support A (side), B (side), C, D (diagonal) with c1 = C - A = (d1, al), c2 = D - B = (d2, be), u = B - A = (G, e).
Lemma mixedeq <=> u.(c1+c2) = 0 and |u + c2 - c1| = |u|, D - C != +-u, G != 0 (grid conditions dropped: superset).
Reduction: G (d1 + d2) = -4 e (al + be) and (G - U)^2 = G^2 + 4 V (2e - V), U = d1 - d2, V = al - be.
For e != 0 and al + be != 0, G divides K = -4 e s, so the search over eta-combos and divisors is finite.
(e = 0 is impossible under the staircase; al + be = 0 forces c2 = -c1, n = 0.)
Usage: py quad4.py lad Ep    |  py quad4.py toy seed P maxeta W   (toy: validation against brute force)"""
import sys, numpy as np
from numba import njit

@njit(cache=False)
def spf_sieve(N):
    s = np.zeros(N + 1, dtype=np.int32)
    for i in range(2, N + 1):
        if s[i] == 0:
            for j in range(i, N + 1, i):
                if s[j] == 0: s[j] = i
    return s

@njit(cache=False)
def divisors(n, spf, out):
    # positive divisors of n into out, return count
    cnt = 1; out[0] = 1
    m = n
    while m > 1:
        p = spf[m]; k = 0
        while m % p == 0:
            m //= p; k += 1
        c0 = cnt; pw = 1
        for t in range(k):
            pw *= p
            for i in range(c0):
                out[cnt] = out[i] * pw; cnt += 1
    return cnt

@njit(cache=False)
def isqrt(n):
    if n < 0: return -1
    r = int(np.sqrt(n))
    while r * r > n: r -= 1
    while (r + 1) * (r + 1) <= n: r += 1
    return r

@njit(cache=False)
def search(E, P, vals, spf, maxout):
    nv = len(vals)
    # residues by value
    res = np.zeros((nv, P), dtype=np.int64); nres = np.zeros(nv, dtype=np.int64)
    for a in range(P):
        for k in range(nv):
            if E[a] == vals[k]:
                res[k, nres[k]] = a; nres[k] += 1
    out = np.zeros((maxout, 8), dtype=np.int64); no = 0
    dv = np.zeros(20000, dtype=np.int64)
    for iA in range(nv):
        for iB in range(nv):
            e = vals[iB] - vals[iA]
            if e == 0: continue
            for iC in range(nv):
                al = vals[iC] - vals[iA]
                for iD in range(nv):
                    be = vals[iD] - vals[iB]
                    s = al + be
                    if s == 0: continue
                    V = al - be
                    K = -4 * e * s
                    nd = divisors(abs(K), spf, dv)
                    for k in range(nd):
                        for sg in range(2):
                            G = dv[k] if sg == 0 else -dv[k]
                            Sp = K // G
                            Rq = G * G + 4 * V * (2 * e - V)
                            r = isqrt(Rq)
                            if r < 0 or r * r != Rq: continue
                            for rs in range(2):
                                if rs == 1 and r == 0: continue
                                U = G - r if rs == 0 else G + r
                                if (Sp - U) % 2 != 0: continue
                                d1 = (Sp + U) // 2; d2 = (Sp - U) // 2
                                if d1 == 0 or d2 == 0: continue
                                if d1 == G or G + d2 == 0 or G - U == 0: continue
                                if U == 0 and V == 0: continue
                                if U == 2 * G and V == 2 * e: continue
                                for t in range(nres[iA]):
                                    a = res[iA, t]
                                    if E[(a + d1) % P] != vals[iC]: continue
                                    if E[(a + G) % P] != vals[iB]: continue
                                    if E[(a + G + d2) % P] != vals[iD]: continue
                                    if no < maxout:
                                        out[no, 0] = a; out[no, 1] = G; out[no, 2] = d1; out[no, 3] = d2
                                        out[no, 4] = vals[iA]; out[no, 5] = vals[iB]; out[no, 6] = vals[iC]; out[no, 7] = vals[iD]
                                    no += 1
    return out, no

@njit(cache=False)
def brute(E, P, W):
    # ordered (A,B,C,D), all slots in [0,W), distinct, e != 0, conditions of Lemma mixedeq in (X,eta) metric
    cnt = 0
    for a in range(W):
        for b in range(W):
            if b == a: continue
            G = b - a; e = E[b % P] - E[a % P]
            if e == 0: continue
            nu = G * G + 4 * e * e
            for c in range(W):
                if c == a or c == b: continue
                for d in range(W):
                    if d == a or d == b or d == c: continue
                    wx = d - c; wy = E[d % P] - E[c % P]
                    if wx * wx + 4 * wy * wy != nu: continue
                    if (wx == G and wy == e) or (wx == -G and wy == -e): continue
                    sx = c + d - a - b; sy = E[c % P] + E[d % P] - E[a % P] - E[b % P]
                    if sx * G + 4 * sy * e != 0: continue
                    if sx == 0 and sy == 0: continue
                    cnt += 1
    return cnt

def run(E, P):
    vals = np.array(sorted(set(E.tolist())), dtype=np.int64)
    H = int(vals.max() - vals.min())
    spf = spf_sieve(8 * H * H + 10)
    out, no = search(E, P, vals, spf, 200000)
    return out[:min(no, 200000)], no

if __name__ == '__main__':
    if sys.argv[1] == 'lad':
        from lad import eta_array
        Ep = int(sys.argv[2]); E, P = eta_array(Ep)
        out, no = run(E, P)
        print("LAD E'=%d P=%d: four-filler mixed quadruples (ordered shapes mod P) = %d" % (Ep, P, no))
        for row in out[:20]: print(list(row))
    else:
        seed, P, me, W = map(int, sys.argv[2:6])
        rng = np.random.default_rng(seed)
        E = rng.integers(0, me + 1, size=P).astype(np.int64)
        out, no = run(E, P)
        # count placements inside the window [0, W)
        cnt = 0
        for a, G, d1, d2 in out[:, :4]:
            slots = [0, d1, G, G + d2]
            lo = -min(slots); hi = W - 1 - max(slots)
            for a0 in range(lo, hi + 1):
                if a0 % P == a % P: cnt += 1
        bc = brute(E, P, W)
        print('toy seed=%d P=%d maxeta=%d W=%d: reduced shapes %d, placements in window %d, brute force %d' % (seed, P, me, W, no, cnt, bc))
