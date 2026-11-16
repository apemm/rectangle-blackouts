# U3top: hole row rho = T1 (top row = r1+8 mod 16), base rows rho-8 (n=nu+1 mod 4) and rho-24 (n=nu+3 mod 4)
import sys, time
from layout import build, report, greedy_class
h=int(sys.argv[1]); W=int(sys.argv[2]); svals=[int(v) for v in sys.argv[3].split(',')]
iota8=int(sys.argv[4]); swap=int(sys.argv[5]) if len(sys.argv)>5 else 0
r1=(2*iota8+1)%16; r0=1 if iota8%2 else 3; A=(h+1)//2; nu=iota8%2
T1=max(y for y in range(1,h+1) if y%16==(r1+8)%16); rho=T1; Rp,Rm=(rho-8,rho-24) if not swap else (rho-24,rho-8)
M=4*((W//4-A)//8)
rowf=lambda n: rho if n%2==nu else (Rp if n%4==(nu+1)%4 else Rm)
tot={}; nl=0; t0=time.time()
for s in svals:
    cls=[i for i in greedy_class(h,s,iota8,excl_rows=()) if 2*i+1 < rho-40]
    cls=[i for i in cls if not (r0==3 and i in (0,2)) and not (r0==3 and i+s in (0,1))]
    nl+=len(cls)
    S,k=build(h,W,r0,[(M,s,cls)],rowf)
    C,ex=report(S,k,h,W)
    for a,b in C.items():
        if not a.startswith('Tparked'): tot[a]=tot.get(a,0)+b
    for a,b in C.items():
        if not a.startswith('Tparked') and len(sys.argv)>6: print('   ',a,ex[a])
print('h',h,'iota8',iota8,'r0',r0,'rows rho,R+,R-',(rho,Rp,Rm),'labels',nl,tot, round(time.time()-t0,1))
