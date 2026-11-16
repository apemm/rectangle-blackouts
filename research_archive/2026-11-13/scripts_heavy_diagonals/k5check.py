# Check the K5 {0,35,209,260,434} in Cay(Z, D_1045^inf) and its scaled copies c*K5 in G_{c*1045}(h).
import math
def Q(T,d): return 20*d*d+4*T*d+T*T
def issq(n): r=math.isqrt(n); return r*r==n
V=[0,35,209,260,434]
for c in [1,3,5]:
    T=1045*c; Ls=[]
    ok=True
    for a in V:
        for b in V:
            if a<b:
                d=c*(b-a)
                good=[sg for sg in (1,-1) if issq(Q(T,sg*d))]
                if not good: ok=False
                Ls.append(min(math.isqrt(Q(T,sg*d)) for sg in good) if good else None)
    hmin=max(Ls)+1
    # n_T at height h for T>0: K - (T-1)/2 ; need > 434c
    h=hmin
    while (h//2)-(T-1)//2 <= 434*c: h+=1
    print("c",c,"T",T,"all edges present",ok,"max L",max(Ls),"least h",h)
