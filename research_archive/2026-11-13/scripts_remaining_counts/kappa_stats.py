import sys, math
exec(open('ne_count.py').read().split("cnt = 0")[0])  # reuse sieve and helpers
cnt=0; rows=[]
for w in range(2, Wmax+1):
    jmin = max(1, int(RAT*w*w/H)-2)
    for j in range(jmin, w):
        k = w - j
        d = {}; fac(k, d); dw = {}; fac(w, dw)
        for p,e in dw.items(): d[p] = d.get(p,0)+2*e
        fac(j*j+df*df, d)
        for U in divs(d):
            if (U - w*df) % j: continue
            M = (U - w*df)//j
            if M < 1: continue
            num = w*(M*M + df*M + k*w)
            if num % U: continue
            A = num//U
            if A <= M or A > H or (M*A) % w: continue
            Dx = M*A//w + k
            if Dx >= RAT*H:
                ep = M+df; t = math.gcd(ep,k); kap = ep//t; mu = k//t
                Y1 = A - M; Q = 2*M + Y1
                rows.append((kap, mu, M, k, w, j, Y1, Q, kap/M))
rows.sort(key=lambda r: -r[8])
print(len(rows))
import statistics
print("median kappa/M", statistics.median(r[8] for r in rows), "max", rows[0][8])
for r in rows[:10]: print(r)
print("frac with kappa > M^(1/2):", sum(1 for r in rows if r[0] > r[2]**0.5)/len(rows))
