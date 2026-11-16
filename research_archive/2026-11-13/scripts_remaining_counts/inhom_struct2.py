import sys, math
from sympy import divisors
dF = int(sys.argv[1]); h = int(sys.argv[2])
rows = []
for t in range(-h//2, h//2+1):
    if t == 0: continue
    w = dF - 2*t; N = 10*w*w*(dF+2*t)
    if N == 0: continue
    for d in divisors(abs(N)):
        for s in (d, -d):
            P = s - 2*w; num = (P - 8*t)*(P*P + w*w); den = 8*t*s
            if num % den: continue
            Y1 = num//den; Y2 = Y1 + w
            if 1 <= Y1 <= h and 1 <= Y2 <= h:
                g = math.gcd(P, 2*t); a, b = P//g, 2*t//g
                if b < 0: a, b, g = -a, -b, -g
                n = a - 2*b; z = n*g + 2*dF
                rows.append((t, s, a, b, g, n, z, Y1, Y2))
import collections
print(len(rows))
print("|z| quantiles", sorted(abs(r[6]) for r in rows)[::len(rows)//10])
print("|g| quantiles", sorted(abs(r[4]) for r in rows)[::len(rows)//10])
print("|n| quantiles", sorted(abs(r[5]) for r in rows)[::len(rows)//10])
print("|t| quantiles", sorted(abs(r[0]) for r in rows)[::len(rows)//10])
# z relation to s
print("s/z ratios sample", collections.Counter(round(r[1]/r[6],3) for r in rows).most_common(6))
for r in rows[:: max(1,len(rows)//25)]: print(r)
