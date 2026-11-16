# Brute-force check of the pair bound in Lemma P: for parity edges e,f and column offset x != 0,
# the doubles at columns 0 and x contain a corner triple or a rival pair only for at most
# G2(e,f) - 1 values of x, where G2 = 9 + 2*sum_{c in e, c' in f, c-c' odd} tau(|c-c'|^2).
import math, itertools
def tau(n): return sum(1 for d in range(1,n+1) if n%d==0)
def rival(C,D,h):
    (cx,c),(dx,cp)=C,D
    if c>cp: (cx,c),(dx,cp)=(dx,cp),(cx,c)
    if (cp-c)%2==0: return False
    t2=(cx-dx)**2
    if t2==0: return False
    for j in range(1,h):
        if c-j<1 or cp+j>h: break
        if 4*j*(cp-c+j)==t2: return True
    return False
def corner(P,h):
    for Q0,Q1,Q2 in itertools.permutations(P,3):
        a=(Q1[0]-Q0[0],Q1[1]-Q0[1]); b=(Q2[0]-Q0[0],Q2[1]-Q0[1])
        if 0 in a or 0 in b: continue
        if a[0]*b[0]+a[1]*b[1]!=0: continue
        y4=Q1[1]+Q2[1]-Q0[1]
        if 1<=y4<=h: return True
    return False
worst=0; viol=0
for h in [9,12,15]:
    edges=[(r,s) for r in range(1,h+1,2) for s in range(2,h+1,2)]
    for e in edges:
        for f in edges:
            if e==f: continue
            G2=9+2*sum(tau(abs(c-cp)**2) for c in e for cp in f if (c-cp)%2)
            bad=0
            for x in range(-h*h,h*h+1):
                if x==0: continue
                P=[(0,e[0]),(0,e[1]),(x,f[0]),(x,f[1])]
                if corner(P,h) or any(rival(C,D,h) for C in P[:2] for D in P[2:]): bad+=1
            worst=max(worst,bad/G2)
            if bad>G2-1: viol+=1
    print("h",h,"pairs",len(edges)*(len(edges)-1),"violations",viol,"max bad/G2",round(worst,3))
