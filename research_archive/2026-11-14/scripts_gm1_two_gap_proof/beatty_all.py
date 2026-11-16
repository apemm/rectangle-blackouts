from fractions import Fraction as F
import sys
exec(open('beatty.py').read().split('A=int')[0])
A=int(sys.argv[1]); B=int(sys.argv[2])
fails=[]
for a in range(1,A+1):
    for b in range(0,B+1):
        if beatty(a,b) is None: fails.append((a,b))
print(len(fails), fails[:100])
