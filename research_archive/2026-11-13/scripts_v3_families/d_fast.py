import sys
from sympy import primerange
from d_shapes import divisors_signed
def run(h):
    P = set(p for p in primerange(20*h+1, 40*h+1) if p % 20 in (3, 7))
    pairs = 0; real = 0; ex = None; pairs_span = 0
    for yP in range(3, 64, 4):
        for Tm in (1, 3):
            off = 32 if Tm == 3 else 48
            Ts = max(y for y in range(h-70, h+1) if (y-yP-off) % 64 == 0)
            for yV in range(yP, Ts-128, 64):
                if yV <= 177: continue
                u = (yV-1)//2
                for o, yG in ((0, Ts-24), (2, Ts-8)):
                    g = yG-yV; N = u*g//2
                    gam = [(d, N//d) for d in divisors_signed(N) if N % d == 0 and d % 4 == o and (N//d) % 4]
                    for (d1,a1) in gam:
                        for (d2,a2) in gam:
                            if d1 == d2: continue
                            diff = 4*d1+a1-4*d2-a2
                            if diff % 32: continue
                            pairs += 1
                            q = abs(diff)//4
                            if q*4 > h*h//2 or q*4 < 80*h: continue
                            pairs_span += 1
                            for k in range(1, q//(20*h)+1):
                                if q % k == 0 and q//k in P:
                                    real += 1; ex = (h, yV, yG, d1, a1, d2, a2, diff, q//k)
    return pairs, pairs_span, len(P), real, ex
for h in map(int, sys.argv[1:]):
    print(run(h))
