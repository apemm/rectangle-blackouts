# Full count C_df(H) = #{(M,A,w,k): k(w^2+MA)=w(M+df)(A-M), 1<=M, M<A<=H, M*A % w==0, Dx=MA/w+k >= 78H}
# (only the Pi'>0, j>=1 branch; other branches are proved empty/small)
import sys, time
df = int(sys.argv[1]); H = int(sys.argv[2]); RAT = float(sys.argv[3]) if len(sys.argv)>3 else 78.0
Wmax = int(H/RAT)+2
LIM = Wmax*Wmax + df*df + 10
spf = list(range(LIM+1))
i = 2
while i*i <= LIM:
    if spf[i] == i:
        for q in range(i*i, LIM+1, i):
            if spf[q] == q: spf[q] = i
    i += 1
def fac(n, d):
    while n > 1:
        p = spf[n]; c = 0
        while n % p == 0: n //= p; c += 1
        d[p] = d.get(p,0)+c
def divs(d):
    ds = [1]
    for p,e in d.items():
        ds = [x*p**t for x in ds for t in range(e+1)]
    return ds
cnt = 0; out = []
t0 = time.time()
for w in range(2, Wmax+1):
    jmin = max(1, int(RAT*w*w/H)-2)
    for j in range(jmin, w):
        k = w - j
        d = {}
        fac(k, d); 
        dw = {}; fac(w, dw)
        for p,e in dw.items(): d[p] = d.get(p,0)+2*e
        fac(j*j+df*df, d)
        for U in divs(d):
            if (U - w*df) % j: continue
            M = (U - w*df)//j
            if M < 1: continue
            num = w*(M*M + df*M + k*w)
            if num % U: continue
            A = num//U
            if A <= M or A > H: continue
            if (M*A) % w: continue
            Dx = M*A//w + k
            if Dx >= RAT*H:
                cnt += 1; out.append((M,A,w,k,j,Dx/H))
print("df",df,"H",H,"count",cnt,"time",round(time.time()-t0,1))
for o in out[:12]: print(o)
