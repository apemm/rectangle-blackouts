# Search solutions of k(w^2+M*A) = w*(M+df)*(A-M), M=N'-df>=1, A=N'+A', j=w-k>=1,
# with ratio Dx/A >= R where Dx = M*A/w + k. Enumerate (k,w) and divisors U of Phi = k w^2 (j^2+df^2).
import sys, math
from sympy import divisors
df = int(sys.argv[1]); W = int(sys.argv[2]); R = float(sys.argv[3])
sols = []
for w in range(2, W+1):
    for k in range(1, w):
        j = w - k
        Phi = k*w*w*(j*j+df*df)
        for U in divisors(Phi):
            if (U - w*df) % j: continue
            M = (U - w*df)//j
            if M < 1: continue
            num = w*(M*M + df*M + k*w)
            if num % U: continue
            A = num//U
            if A <= M: continue
            assert k*(w*w+M*A) == w*(M+df)*(A-M)
            if M*A % w: continue   # Z_x must be integer
            Dx = M*A//w + k
            if Dx >= R*A:
                sols.append((Dx/A, M, A, w, k, j))
sols.sort(reverse=True)
print(len(sols))
for s in sols[:25]: print(s)
