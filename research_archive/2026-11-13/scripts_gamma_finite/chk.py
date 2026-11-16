from bohr import shifts
from fractions import Fraction as Fr
from math import isqrt
import sys
for T in [5,145,295,55,305]:
    sh,ex,nt,rad=shifts(T,Fr(1,1),1,3000)
    br=[d for d in range(-3000,3001) if d and isqrt(20*d*d+4*T*d+T*T)**2==20*d*d+4*T*d+T*T]
    print(T, ex==br, len(ex), nt, float(rad), sorted(x for x in ex if x>0)[:12])
