import sys
from bohr import shifts
from fractions import Fraction as Fr
T=int(sys.argv[1]); a=Fr(sys.argv[2]); B=int(float(sys.argv[4]))
for M in map(int,sys.argv[3].split(',')):
    sh,ex,nt,rad=shifts(T,a,M,B)
    tails=[(float(lo),r) for (lo,hi,r) in sh if lo!=hi]
    rs=sorted({r for (_,r) in tails})
    small0=[d for d in ex if d%M==0]
    print("M",M,"#exact",len(ex),"#tailclasses",nt,"tail residues",len(rs), rs[:20], "rad %.2e"%rad, "exact d=0 mod M:",small0[:8])
