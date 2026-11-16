# Sanity check 2: same count as check_triples.py but with the Euclid parametrization (fast).
import sys, math, time
from collections import defaultdict
from math import gcd

def build(h):
    S = defaultdict(set)
    u = 2
    while u * u + 1 < h:
        for v in range(1, u):
            if (u - v) % 2 == 0 or gcd(u, v) != 1:
                continue
            L0 = u * u + v * v
            if L0 >= h:
                break
            d0 = u * v // 2          # 4 d0 = 2 u v
            b0 = u * u - v * v
            g = 1
            while g * L0 < h:
                d = g * d0; b = g * b0
                for sd in (d, -d):
                    for sb in (b, -b):
                        S[sb - 2 * sd].add(sd)
                g += 2
        u += 1
    return S

def main():
    for h in [int(a) for a in sys.argv[1:]]:
        t0 = time.time()
        S = build(h)
        tot_k = tot_a = tot_b = tot_refl = tot_sq = 0
        nT = 0; nT_with = 0
        worst = (0, None)
        hist = defaultdict(int)
        for T, s in S.items():
            if abs(T) >= h:
                continue
            nT += 1
            k = len(s)
            tot_k += k; tot_sq += k * k
            na = nb = nr = 0
            for a in s:
                for b in s:
                    c = a + b
                    if c in s:
                        if 5 * c == -T:
                            nr += 1
                        else:
                            na += 1
                    if -c in s:
                        nb += 1
            tot_a += na; tot_b += nb; tot_refl += nr
            r = 6 * na + 2 * nb
            if r > 0:
                nT_with += 1
            if r > worst[0]:
                worst = (r, T, k)
        print(f"h={h} nT={nT} sum|S_T|={tot_k} ({tot_k/h:.3f} h) sum|S_T|^2/h={tot_sq/h:.2f}"
              f" Na={tot_a} Nb={tot_b} refl={tot_refl} R={6*tot_a+2*tot_b} ({(6*tot_a+2*tot_b)/h:.4f} h)"
              f" T_with_relation={nT_with} worst(R,T,k)={worst} time={time.time()-t0:.1f}s")

main()
