import sys, time
from layout import build, report, greedy_class
h = int(sys.argv[1]); W = int(sys.argv[2]); svals=[int(v) for v in sys.argv[3].split(',')]
d1 = int(sys.argv[4]) if len(sys.argv)>4 else 16   # second base row = R - d1
iota8=1; r1=3; r0=1; A=(h+1)//2; nu=1
R = max(y for y in range(1,h+1) if y%16==r1); rho=R-8
M = 4*((W//4-A)//8)
rowf = lambda n: rho if n%2==nu else (R if n%4==(nu+1)%4 else R-d1)
for s in svals:
    cls = greedy_class(h, s, iota8, excl_rows=(R, R-16, R-d1, R-d1-16))
    S,k = build(h,W,r0,[(M,s,cls)],rowf)
    C,ex = report(S,k,h,W)
    bad={a:b for a,b in C.items() if not a.startswith('Tparked')}
    print('BH16m4 h',h,'s',s,'d1',d1,'labels',cls,bad)
    for a in bad: print('    ',a,ex[a])
