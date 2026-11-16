import sys
from bohr import shifts
from fractions import Fraction as Fr
import mpmath as mp
T=int(sys.argv[1]); a=Fr(sys.argv[2])
sh,ex,nt,rad=shifts(T,a,1,10**15)
th=mp.mpf(a.numerator)/a.denominator/mp.sqrt(5)
pos=[d for d in ex if d>0]
print("nt",nt,"rad",float(rad))
for d in sorted(ex,key=abs)[:40]:
    print(d, "%.4f"%float(mp.frac(th*d)), "mod T", d%T, "l|d" , d%(T//5)==0)
print("tails",[ (round(float(mp.frac(lo)),4)) for (lo,hi,r) in sh if lo!=hi])
