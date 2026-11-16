import sys
from d_shapes import census
from collections import Counter
h = int(sys.argv[1])
big = 0; tot = 0; mx = 0; fac = Counter()
from sympy import factorint
for yP in range(3, 64, 4):
    for Tm in (1, 3):
        nt, ns, npr, real = (None,)*4
        import d_shapes
        # re-run and keep shapes
        off = 32 if Tm == 3 else 48
        res = d_shapes.census(h, yP, Tm)
# recompute shapes list directly
import d_shapes as D
cnt = 0; ge80 = 0; maxprime_ratio = []
for yP in range(3, 64, 4):
    for Tm in (1, 3):
        off = 32 if Tm == 3 else 48
        Ts = max(y for y in range(h - 70, h + 1) if (y - yP - off) % 64 == 0)
        for yV in range(yP, Ts - 128, 64):
            if yV <= 177: continue
            u = (yV - 1) // 2
            for o, yG in ((0, Ts - 24), (2, Ts - 8)):
                g = yG - yV
                gam = [(d, u*g//(2*d)) for d in D.divisors_signed(u*g//2) if (u*g) % (2*d) == 0 and d % 4 == o and (u*g//(2*d)) % 4]
                for (d1,a1) in gam:
                    for (d2,a2) in gam:
                        if d1 == d2: continue
                        diff = 4*d1+a1-4*d2-a2
                        if diff % 32: continue
                        cnt += 1
                        if abs(diff) >= 80*h and abs(diff) <= h*h//2:
                            ge80 += 1
                            lp = max(factorint(abs(diff)//4))
                            maxprime_ratio.append(lp/h)
print("h", h, "pairs", cnt, "with 80h<=|diff|<=h^2/2:", ge80)
import statistics
if maxprime_ratio:
    print("largest prime factor / h: max", max(maxprime_ratio), "count in (20,40]:", sum(1 for r in maxprime_ratio if 20 < r <= 40))
