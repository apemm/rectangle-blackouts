# Full residue enumeration over the 36 role assignments of Appendix A (cross-check only).
from itertools import combinations_with_replacement as cwr
LOW=[3,5,6]; HIGH=[1,2,4]
lev={'L':(0,LOW),'F':(3,[0]),'H':(1,HIGH)}
def pts(l): y,cols=lev[l]; return [(x,y) for x in cols]
def ok(A,B,C,D):
    U=((B[0]-A[0])%7,(B[1]-A[1])%7); S=((C[0]+D[0]-A[0]-B[0])%7,(C[1]+D[1]-A[1]-B[1])%7)
    V=((D[0]-C[0])%7,(D[1]-C[1])%7)
    return (U[0]*S[0]+U[1]*S[1])%7==0 and (V[0]**2+V[1]**2-U[0]**2-U[1]**2)%7==0
odd={'L','F'}
res={}
for parity,rhos in (('odd',[0]),('even',[0,5])):
    for ms in cwr('LFH',3):
        nodd=sum(1 for l in ms if l in odd)
        if parity=='odd' and nodd%2==0: continue
        if parity=='even' and nodd%2==1: continue
        for pl in sorted(set(ms)):
            rest=list(ms); rest.remove(pl); q1,q2=rest
            for side in (True,False):
                for rho in rhos:
                    I=(0,rho); n=0
                    for P in pts(pl):
                        for Q in pts(q1):
                            for R in pts(q2):
                                if side:
                                    pairs=[((I,P),(Q,R)),((P,I),(Q,R)),((I,P),(R,Q)),((P,I),(R,Q))]
                                else:
                                    pairs=[((Q,R),(I,P)),((R,Q),(I,P)),((Q,R),(P,I)),((R,Q),(P,I))]
                                for (A,B),(C,D) in pairs:
                                    n+=ok(A,B,C,D)
                    name=('(I,%s;%s,%s)'%(pl,q1,q2)) if side else ('(%s,%s;I,%s)'%(q1,q2,pl))
                    if n: res.setdefault(name,[]).append(rho)
print('assignments with residue solutions:', res)
