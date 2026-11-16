# brute-force intra-class X1 on a full diagonal: E=(x,1), x=2 mod 4 vertex; F even pt; G odd pt row=5 mod 8
import sys
from math import isqrt
def labels(h,T):
    A=(h+1)//2; K=h//2; s=(T-1)//2
    L=[]
    for i in range(A):
        j=i+s
        if 0<=j<K: L.append(i)
    return L,s
def x1_brute(h,T):
    L,s=labels(h,T)
    ev=[(4*i,2*(i+s)+2,i) for i in L]
    od=[(4*i,2*i+1,i) for i in L if (2*i+1)%8==5]
    edges=[]
    for (xF,yF,iF) in ev:
        for (xG,yG,iG) in od:
            if yF+yG-1>h: continue
            # E=(x,1): (xF-x)(xG-x)+(yF-1)(yG-1)=0 -> x^2-(xF+xG)x+xF*xG+(yF-1)(yG-1)=0
            S=xF+xG; P=xF*xG+(yF-1)*(yG-1)
            D=S*S-4*P
            if D<0: continue
            r=isqrt(D)
            if r*r!=D: continue
            for x2 in {S+r,S-r}:
                if x2%2: continue
                x=x2//2
                if x%4!=2: continue
                yW=yF+yG-1
                if yW%2==0 and yW<=h: edges.append((iG,iF,x))
    return edges
def x1_formula(h,T):
    L,s=labels(h,T); Ls=set(L); out=[]
    for iG in L:
        if iG%4!=2: continue
        u=iG//2
        for k in L:
            yF=2*(k+s)+2; yG=2*iG+1
            if yF+yG-1>h or k==iG: continue
            w=k-3*u; R=w*w-u*(5*u+T)
            if R>=0 and isqrt(R)**2==R: out.append((iG,k))
    return out
h=int(sys.argv[1])
for T in [1,-1,3,-3,5,-5,-15,7,-25,9]:
    b=x1_brute(h,T); f=x1_formula(h,T)
    bs=set((a,c) for a,c,_ in b); fs=set(f)
    from collections import Counter
    deg=Counter(); 
    for a,c in bs: deg[a]+=1; deg[c]+=1
    print(T,len(bs),len(fs),bs==fs, deg.most_common(2))
