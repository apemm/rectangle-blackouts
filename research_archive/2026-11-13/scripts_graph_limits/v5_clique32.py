# Independent check of the 25-clique of the monotone/P constraint graph at h=32 (from the definition).
from math import isqrt
h=32; A=(h+1)//2; K=h//2
cl={0:[12,15],2:[7,9],4:[6],5:list(range(7,16)),7:[4,5,6],8:[2,5],10:[4],11:[3],13:[2,3],15:[0,1]}
V=[(i,j) for i in cl for j in cl[i]]
assert all(0<=i<A and 0<=j<K for i,j in V)
def sees(i,j,ip):  # even point of (i,j) at (4i, 2j+2); odd point of slot ip at (4ip, 2ip+1)
    q=(4*(i-ip))**2+(2*j+2-2*ip-1)**2; L=isqrt(q); return L*L==q and 0<L<h and L%2==1
bad=0
for a in range(len(V)):
    for b in range(a+1,len(V)):
        (i,j),(k,l)=sorted([V[a],V[b]])
        ok = i==k or (j>l) or sees(i,j,k) or sees(k,l,i)
        if not ok: bad+=1; print("not adjacent",(i,j),(k,l))
print("vertices",len(V),"non-adjacent pairs",bad)
