import sys
from math import isqrt
T=int(sys.argv[1]); B=int(sys.argv[2])
s=set()
for d in range(-B,B+1):
    if d==0: continue
    Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
    if L*L==Q: s.add(abs(d))
D=sorted(s); print(len(D), D[:60])
