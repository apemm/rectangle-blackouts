# Cross-check of the hand case table of Appendix A (mod-7 cases only).
# Normalised levels: L=0, F=3, H=1; columns: low {3,5,6} (row L), high {1,2,4} (row H),
# period-zero 0 (row F); the label point I=(0,rho), rho in {0,5}.
LOW=[3,5,6]; HIGH=[1,2,4]; PZ=[0]
lev={'L':(0,LOW),'F':(3,PZ),'H':(1,HIGH)}
def pts(l): y,cols=lev[l]; return [(x,y) for x in cols]
def ok(A,B,C,D):
    U=((B[0]-A[0])%7,(B[1]-A[1])%7); S=((C[0]+D[0]-A[0]-B[0])%7,(C[1]+D[1]-A[1]-B[1])%7)
    V=((D[0]-C[0])%7,(D[1]-C[1])%7)
    return (U[0]*S[0]+U[1]*S[1])%7==0 and (V[0]**2+V[1]**2-U[0]**2-U[1]**2)%7==0
cases=[ # (name, rhos, I on side?, partner level, other pair levels)
 ('1b side',[0],True,'H',('L','H')),('2b side',[0],True,'H',('F','H')),
 ('4 side',[0],True,'F',('F','F')),('5a diag',[0],False,'L',('L','F')),
 ('6a side',[0],True,'L',('F','F')),('6b side',[0],True,'F',('L','F')),
 ('6b diag',[0],False,'F',('L','F')),('8a side',[0,5],True,'L',('L','H')),
 ('9a side',[0,5],True,'F',('F','H')),('9a diag',[0,5],False,'F',('F','H')),
 ('9b side',[0,5],True,'H',('F','F')),('10a side',[0,5],True,'L',('F','H')),
 ('10b side',[0,5],True,'F',('L','H')),('10c diag',[0,5],False,'H',('L','F'))]
for name,rhos,side,pl,(q1,q2) in cases:
    sols=0
    for rho in rhos:
        I=(0,rho)
        for P in pts(pl):
            for Q in pts(q1):
                for R in pts(q2):
                    if side:
                        for (A,B) in ((I,P),(P,I)):
                            for (C,D) in ((Q,R),(R,Q)):
                                sols+=ok(A,B,C,D)
                    else:
                        for (A,B) in ((Q,R),(R,Q)):
                            for (C,D) in ((I,P),(P,I)):
                                sols+=ok(A,B,C,D)
    print(name, 'residue solutions:', sols)
# margin claims at the extreme admissible values
import itertools
h=10**10
worst={}
for L,F,H,r in itertools.product([1,13],[1000,3743],[h-195,h],[5000,h-5000]):
    for nm,val,cond in [
      ('1a side H+(r-L)/2>h',H+(r-L)/2,'>h'),('1b diag (r+2H-L)/2>h',(r+2*H-L)/2,'>h'),
      ('2a side H+(r-F)/2>h',H+(r-F)/2,'>h'),('2b diag (r+2H-F)/2>h',(r+2*H-F)/2,'>h'),
      ('3 side (3L-r)/2<1',(3*L-r)/2,'<1'),('5 side (2L+F-r)/2<1',(2*L+F-r)/2,'<1'),
      ('7 side (3H-r)/2>h',(3*H-r)/2,'>h'),('8 (r+2L-H)/2<1',(r+2*L-H)/2,'<1'),
      ('10 (r+L+F-H)/2<1',(r+L+F-H)/2,'<1')]:
        good = val>h if cond=='>h' else val<1
        worst.setdefault(nm,True); worst[nm]&=good
for k,v in worst.items(): print(k, v)
