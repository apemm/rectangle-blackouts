import sys, math
from sympy import divisors
dF = int(sys.argv[1]); h = int(sys.argv[2])
sols = []
for t in range(-h//2, h//2+1):
    if t == 0: continue
    w = dF - 2*t
    N = 10*w*w*(dF+2*t)
    if N == 0: continue
    for d in divisors(abs(N)):
        for s in (d, -d):
            P = s - 2*w
            num = (P - 8*t)*(P*P + w*w); den = 8*t*s
            if num % den: continue
            Y1 = num//den; Y2 = Y1 + w
            if 1 <= Y1 <= h and 1 <= Y2 <= h: sols.append((t, s, P, Y1, Y2, w))
print(len(sols), "t<0:", sum(1 for x in sols if x[0]<0))
# structure: g = gcd(P, 2t), shape a/b = P/(2t) reduced; the size of the reduced shape
from collections import Counter
hs = []
for (t,s,P,Y1,Y2,w) in sols:
    g = math.gcd(P, 2*t); a, b = P//g, 2*t//g
    if b < 0: a, b = -a, -b
    hs.append((max(abs(a),abs(b)), g, a, b, t, s, Y1, Y2))
hs.sort()
print("shape heights quantiles:", [hs[int(q*(len(hs)-1))][0] for q in (0,0.25,0.5,0.75,1)])
print("gcd g quantiles:", sorted(x[1] for x in hs)[::max(1,len(hs)//8)])
c = Counter((x[2],x[3]) for x in hs)
print("distinct shapes", len(c), "most common", c.most_common(8))
