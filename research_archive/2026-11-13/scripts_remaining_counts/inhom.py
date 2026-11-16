import sys
from sympy import divisors, factorint
dF = int(sys.argv[1]); h = int(sys.argv[2]); show = int(sys.argv[3]) if len(sys.argv)>3 else 0
sols = []
for t in range(-h//2, h//2+1):
    if t == 0: continue
    w = dF - 2*t
    N = 10*w*w*(dF+2*t)
    if N == 0: continue
    for d in divisors(abs(N)):
        for s in (d, -d):
            P = s - 2*w
            num = (P - 8*t)*(P*P + w*w)
            den = 8*t*s
            if num % den: continue
            Y1 = num//den
            Y2 = Y1 + w
            if 1 <= Y1 <= h and 1 <= Y2 <= h:
                sols.append((t, s, P, Y1, Y2))
print(len(sols))
if show:
    for x in sols[:show]: print(x)
