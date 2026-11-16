"""Sanity check: exact Lemma F incident sums, unrestricted vs congruence-restricted lists.
Block: slot columns 7j, j in [0,N). Labels (a, b=a+T): a = 1 mod 14 odd rows, T = 1 mod 14 (b = 2 mod 14).
Restricted list of label: j with 7j = s1*a (mod p1), 7j = s2*b (mod p2).
Lemma F event (parity pi): x_f - x_e = X, X^2+y^2=L^2, y = rho_f - rho_e != 0,
u- = x_e+(X-L)/2, u+ = x_e+(X+L)/2 slot columns inside [0,7N).
Prints avg incident sum per label (both parities), split by whether p | y.
"""
import sys, math
from collections import defaultdict

def pyth_offsets(y):
    # all signed X with X^2+y^2=L^2, X != 0, X,(X-L)/2,(X+L)/2 multiples of 7
    y2 = y*y; out = []
    d = 1
    while d*d < y2:
        if y2 % d == 0:
            e = y2//d
            if (d - e) % 2 == 0:
                X = (e-d)//2; L = (e+d)//2
                for Xs in (X, -X):
                    if Xs % 7 == 0 and (Xs-L) % 14 == 0 and (Xs+L) % 14 == 0:
                        out.append((Xs, L))
        d += 1
    return out

def count_ap(lo, hi, r, Q):
    if hi < lo: return 0
    return (hi - r)//Q - (lo - 1 - r)//Q

def run(h, Ts, N, p1, s1, p2, s2):
    labels = []
    for T in Ts:
        for a in range(1, h+1, 14):
            if a + T <= h: labels.append((a, a+T))
    n = len(labels)
    inv7_1 = pow(7, -1, p1); inv7_2 = pow(7, -1, p2); Q = p1*p2
    def res(a, b):
        r1 = (inv7_1*s1*a) % p1; r2 = (inv7_2*s2*b) % p2
        # CRT
        for r in range(r1, Q, p1):
            if r % p2 == r2: return r
    R = [res(a, b) for (a, b) in labels]
    size = [count_ap(0, N-1, r, Q) for r in R]
    cache = {}
    tot = {('U', 0): 0.0, ('R', 0): 0.0, ('R', 'div'): 0.0, ('U', 1): 0.0, ('R', 1): 0.0}
    out = {}
    for par in (0, 1):  # 0 odd points (row a), 1 even points (row b)
        p = p1 if par == 0 else p2
        U = 0.0; Rs = 0.0; Rdiv = 0.0; Udiv = 0.0
        for i in range(n):
            ri = labels[i][par]
            for k in range(n):
                if k == i: continue
                y = labels[k][par] - ri
                if y == 0: continue
                ay = abs(y)
                if ay not in cache: cache[ay] = pyth_offsets(ay)
                for (X, L) in cache[ay]:
                    dj = X//7; lo = max(0, -dj, -((X-L)//14)); hi = min(N-1, N-1-dj, N-1-((X+L)//14))
                    if hi < lo: continue
                    cu = (hi - lo + 1)/(N*N)
                    U += cu
                    if ay % p == 0: Udiv += cu
                    if (dj - (R[k]-R[i])) % Q == 0:
                        c = count_ap(lo, hi, R[i], Q)/(size[i]*size[k])
                        Rs += c
                        if ay % p == 0: Rdiv += c
        out[par] = (U/n, Udiv/n, Rs/n, Rdiv/n)
    return n, N, out

if __name__ == '__main__':
    h = int(sys.argv[1]); D = int(sys.argv[2]); ratio = float(sys.argv[3])
    p1, s1, p2, s2 = map(int, sys.argv[4:8])
    Ts = [1 + 14*t for t in range(D)]
    labels_n = sum(len(range(1, h+1-T, 14)) for T in Ts)
    N = int(ratio*labels_n)
    n, N, out = run(h, Ts, N, p1, s1, p2, s2)
    print(f"h={h} n={n} N={N} p1={p1} s1={s1} p2={p2} s2={s2}")
    for par in (0, 1):
        U, Ud, Rs, Rd = out[par]
        print(f" parity {'odd' if par==0 else 'even'}: unrestricted {U:.4f} (p|y part {Ud:.4f})  restricted {Rs:.4f} (p|y part {Rd:.4f})  ratio {Rs/U:.3f}")
