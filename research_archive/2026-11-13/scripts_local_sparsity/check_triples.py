# Sanity check: count three-term relations e1 d1 + e2 d2 + e3 d3 = 0 inside S_T(h).
import sys, math, time
from collections import defaultdict

def build(h):
    S = defaultdict(set)   # T -> set of signed d
    for d in range(1, h // 4 + 1):
        dd = 16 * d * d
        for b in range(1, h, 2):
            L2 = dd + b * b
            L = math.isqrt(L2)
            if L >= h:
                break
            if L * L == L2:
                for sd in (d, -d):
                    for sb in (b, -b):
                        T = sb - 2 * sd
                        S[T].add(sd)
    return S

def main():
    for h in [int(a) for a in sys.argv[1:]]:
        t0 = time.time()
        S = build(h)
        tot_k = 0; tot_a = 0; tot_b = 0; tot_refl = 0; tot_sq = 0
        nT = 0
        worst = (0, None)
        for T, s in S.items():
            if abs(T) >= h:
                continue
            # verify definition
            for d in s:
                L2 = 20 * d * d + 4 * T * d + T * T
                L = math.isqrt(L2)
                assert L * L == L2 and 0 < L < h and d != 0
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
            if r > worst[0]:
                worst = (r, T, k)
        print(f"h={h} diagonals_with_S={nT} sum|S_T|={tot_k} ({tot_k/h:.3f} h) sum|S_T|^2={tot_sq} ({tot_sq/h:.2f} h)"
              f" N_a(nonrefl)={tot_a} N_b={tot_b} refl={tot_refl} R=6Na+2Nb={6*tot_a+2*tot_b} ({(6*tot_a+2*tot_b)/h:.4f} h)"
              f" worst={worst} time={time.time()-t0:.1f}s")

main()
