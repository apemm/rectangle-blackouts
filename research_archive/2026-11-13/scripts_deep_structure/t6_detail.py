import sys
from layout import build, report, greedy_class
h=int(sys.argv[1]); W=int(sys.argv[2]); s=int(sys.argv[3]); dp,dm,dr=[int(v) for v in sys.argv[4].split(':')]
iota8=1; r1=3; r0=1; A=(h+1)//2; nu=1
R=max(y for y in range(1,h+1) if y%16==r1); Rp,Rm,rho=R-dp,R-dm,R-dr
M=4*((W//4-A)//8)
rowf=lambda n: rho if n%2==nu else (Rp if n%4==(nu+1)%4 else Rm)
cls=greedy_class(h,s,iota8,excl_rows=(Rp,Rm,rho,R-16,Rp-16,Rm-16))
S,k=build(h,W,r0,[(M,s,cls)],rowf)
pts,tr,mx,rv=__import__('chk').analyse(S,h,W)
tag=lambda q: k.get(q,'?')
print('R',R,'rows',Rp,Rm,rho,'labels(slot:oddrow)',[(i,2*i+1) for i in cls],'M',M)
for r in tr:
    if r[8]==1:
        V=(r[0],r[1]);P1=(r[2],r[3]);P2=(r[4],r[5]);Wc=(r[6],r[7])
        print('T',tag(V),tag(P1),tag(P2),'V',V,'P1',P1,'P2',P2,'W',Wc)
for r in mx:
    A_,B,C,D=(pts[r[0]],pts[r[1]],pts[r[2]],pts[r[3]])
    t=''.join(sorted([tag(A_),tag(B)]))+'/'+''.join(sorted([tag(C),tag(D)]))
    if 'S' in t or 'FF' in t: print('M',t,A_,B,C,D,'p',(r[4],r[5]),'q',(r[6],r[7]))
