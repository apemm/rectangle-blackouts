# Link of 0 in Gamma: vertices = elements of +-R_+ in Z_(2) of height <= H, edges when difference in +-R_+.
import sys, time
from math import gcd, isqrt
from fractions import Fraction as F
H = int(sys.argv[1])
def issq(n): return n >= 0 and isqrt(n)**2 == n
def adj(d):  # d Fraction != 0 ; in +-R_+ ?
    u, v = d.numerator, d.denominator
    if v % 2 == 0: return False
    return issq(20*u*u + 4*u*v + v*v) or issq(20*u*u - 4*u*v + v*v)
R = set()
for p in range(-H, H+1):
    for q in range(1, H+1):
        if p == 0 or gcd(p, q) != 1 or (p*q) % 2: continue
        N = p*p - p*q - q*q
        r = F(p*q, 2*N)
        R.add(r); R.add(-r)
V = sorted(R)
t0 = time.time()
E = []
for i in range(len(V)):
    for j in range(i+1, len(V)):
        if adj(V[j]-V[i]): E.append((i, j))
print("H", H, "vertices", len(V), "edges", len(E), "time %.1f" % (time.time()-t0))
deg = [0]*len(V)
for i, j in E: deg[i] += 1; deg[j] += 1
top = sorted(range(len(V)), key=lambda i: -deg[i])[:8]
print("top degrees", [(str(V[i]), deg[i]) for i in top])
import pickle
pickle.dump((V, E), open("link_H%d.pkl" % H, "wb"))
