# Independent brute-force check of the top pointwise counterexample (no T1 enumeration).
import math
S=32; M=3; h=2**21
Y=76773; Yp=76725
qs=[65155,62755,37125,39525]; ds=[21718,20918,12375,13175]
center=(Y+Yp)//2
if center%2==0: center+=1
def issq(n): r=math.isqrt(n); return r*r==n
for k,(q,d) in enumerate(zip(qs,ds)):
    yk = Y if k<2 else Yp
    L2=(S*q)**2+yk*yk; L=math.isqrt(L2)
    w=8*math.sqrt(d); hits=[]
    for dl in range(-(M-1),M):
        qq=M*d+dl
        lo=int(math.ceil(center-w)); hi=int(math.floor(center+w))
        for yy in range(lo|1,hi+1,2):
            t=(S*qq)**2+yy*yy
            if issq(t) and math.isqrt(t)<=h-1: hits.append((qq,yy))
    print("edge",k+1,"q=%d=3*%d%+d"%(q,d,q-M*d),"Y=%d L=%d exact=%s L<=h-1:%s window hits=%s"%(yk,L,L*L==L2,L<=h-1,hits))
print("d1-d2=%d d4-d3=%d |Y-Y'|=%d center=%d"%(ds[0]-ds[1],ds[3]-ds[2],abs(Y-Yp),center))
