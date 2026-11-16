# For a stride-4 class (greedy max independent set in G_T), count filler rows
# r (odd, 3..h) at each empty slot that avoid M2a with every label odd point.
import sys
from math import isqrt
def sq(n): return n>=0 and isqrt(n)**2==n
def m2a(dx,dy):
    # dx = 4 delta, dy = 2 eps
    L2=dx*dx+dy*dy
    if not sq(L2): return False
    L=isqrt(L2)
    if L%4==2: return True
    if L%8==4 and dx%8==0: return True
    return False
def S_T(h,T):
    out=set()
    for d in range(-h,h+1):
        if d==0: continue
        L2=16*d*d+(2*d+T)**2
        if sq(L2) and isqrt(L2)<h: out.add(abs(d))
    return out
h=int(sys.argv[1])
A=(h+1)//2; K=h//2
tot_empty=0; tot_dead=0; tot_dead3=0; hist={}
for T in range(-(2*A-1),2*K,2):
    s=(T-1)//2
    I=[i for i in range(A) if 0<=i+s<K]
    if not I: continue
    D=S_T(h,T)
    cls=[];
    for i in I:
        if all(abs(i-k) not in D for k in cls): cls.append(i)
    occ=set(cls)
    for i0 in range(min(I),max(I)+1):
        if i0 in occ: continue
        tot_empty+=1
        good=[r for r in range(3,h+1,2) if not any(m2a(4*(i-i0),2*i+1-r) for i in occ)]
        good3=[r for r in good if r%4==3]
        if not good: tot_dead+=1
        if not good3: tot_dead3+=1
        hist[len(good3)]=hist.get(len(good3),0)+1
print('h',h,'empty slots',tot_empty,'no odd row',tot_dead,'no row = 3 mod 4',tot_dead3)
print(sorted(hist.items())[:12])
