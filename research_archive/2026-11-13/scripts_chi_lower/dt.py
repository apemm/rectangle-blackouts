import sys
from math import isqrt
def S(T,B):
    s=[]
    for d in range(-B,B+1):
        if d==0: continue
        Q=20*d*d+4*T*d+T*T; L=isqrt(Q)
        if L*L==Q: s.append((d,L))
    return s
for T in map(int,sys.argv[2:]):
    print(T, S(T,int(sys.argv[1])))
