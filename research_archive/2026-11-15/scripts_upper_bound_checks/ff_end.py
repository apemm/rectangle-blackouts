from fractions import Fraction as Fr
from math import gcd
u,a,b,t=1,5,2,-320
m=Fr(a,b); P=2*t*m
Y1=t*(m-4*u)*(m*m+1)/(2*(m-2*u)); assert Y1.denominator==1; Y1=int(Y1)
U=(a-4*u*b)*(a*a+b*b); V=a**3-4*u*a*a*b-3*a*b*b+4*u*b**3; g=gcd(U,V); Up,Vp=U//g,V//g
alpha1=Fr(-2*t*Y1,1)/(8*u*t-P); assert alpha1.denominator==1; alpha1=int(alpha1)
L1=(0,0); F1=(alpha1,Y1); L2=(4*u*t,2*t); F2=(alpha1+int(4*u*t-P),Y1)   # F2 - F1 = (4ut-P, 0)
A,B,C,D=L1,F1,F2,L2
sub=lambda p,q:(p[0]-q[0],p[1]-q[1]); dot=lambda p,q:p[0]*q[0]+p[1]*q[1]
BA=sub(B,A); DC=sub(D,C); n2=(C[0]+D[0]-A[0]-B[0],C[1]+D[1]-A[1]-B[1])
print("P",P,"Y1",Y1,"U'",Up,"V'",Vp,"alpha1",alpha1)
print("|B-A|^2",dot(BA,BA),"|D-C|^2",dot(DC,DC),"(B-A).2n",dot(BA,n2),"D-C!=+-(B-A)",DC not in (BA,(-BA[0],-BA[1])))
d1=F1[1]-L1[1]; d2=F2[1]-L2[1]
print("rows (y increases toward the fillers): L1",L1[1],"L2",L2[1],"fillers",F1[1])
print("depth L1",d1,"divisible by |U'|",d1%abs(Up)==0,"| depth L2",d2,"divisible by |U'|",d2%abs(Up)==0,"by |V'|",d2%abs(Vp)==0)
