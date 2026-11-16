# Sanity check of T2 Section 2 and (3) in normalized F_7 coordinates.
sq={1,2,4}
def lev(x):
    if x%7==0: return 3   # filler F
    return 1 if x%7 in sq else 0  # high H=1, low L=0
out=[]
for X in range(7):           # sea column residue (labels at column 0)
    s=lev(X)
    for r in (0,5):
        for t in (0,5):
            # vectors from sea point (X,s) to label points (0,r),(0,t): (-X, r-s),( -X, t-s) mod 7
            if (X*X+(r-s)*(t-s))%7==0:
                W=((0+0-X)%7,(r+t-s)%7)
                out.append((X,s,r,t,W,lev(W[0])))
print("sea-rooted right angles mod 7 (X,level,r,t,W,level(Wcol)):",out)
seasums=sorted({(a+b)%7 for a in (0,3,1) for b in (0,3,1)})
print("sea sums",seasums,"mixed label sum",(0+5)%7,"zero label sum",0)
# Lemma 1 sanity: closed form X^2*(y^2+2yz-(s-b)^2)=y^2 z^2 for role (a,c|b,s), random brute force
import random
random.seed(1)
bad=0;tested=0
for _ in range(300):
    a,b,c,s=[random.randint(-30,30) for _ in range(4)]
    sols=[]
    for X in range(-200,201):
        if X==0: continue
        for xi in range(-200,201):
            if xi in (0,X): continue
            A=(0,a);B=(X,c);C=(0,b);D=(xi,s)
            u=(B[0]-A[0],B[1]-A[1]); v=(D[0]-C[0],D[1]-C[1])
            if u[0]**2+u[1]**2!=v[0]**2+v[1]**2: continue
            H=(C[0]+D[0]-A[0]-B[0],C[1]+D[1]-A[1]-B[1])
            if u[0]*H[0]+u[1]*H[1]!=0 or H==(0,0): continue
            if v==u or v==(-u[0],-u[1]): continue
            sols.append((X,xi))
    tested+=1
    if len(sols)>2: bad+=1; print("more than 2:",a,b,c,s,sols)
print("lemma1 (a,c|b,s) tested",tested,"cases with >2 solutions:",bad)
