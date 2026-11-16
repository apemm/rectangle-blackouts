import math
# 1) mod7_inset Section 1 finite-field check
Q={1,2,4}; N={3,5,6}
sq={(x*x)%7 for x in range(7)}
print("allowed r (chi(r(1-r))=1):",[r for r in range(7) if (r*(1-r))%7 in Q])
res=[]
for a in Q:
  for b in N:
    c=(a+b-1)%7
    if c in Q:
      d=(1-(b-a)**2)%7
      res.append((a,b,(d-2*c)%7, ((d-2*c)%7) in sq))
print("mixed cases (a,b,d-2c,is_square):",res)
# need u^2(d-2c)=c^2 with c!=0: impossible iff d-2c nonsquare or zero
print("all impossible:",all((t[2]==0) or (t[2] not in sq) for t in res))
# residue 0: c=0
r0=[(a,b,(1-(b-a)**2)%7) for a in Q for b in N if (a+b-1)%7==0]
print("residue-0 pairs:",r0, "d nonsquare:",[t[2] not in sq for t in r0])
# 2) binary_boundary Sec 2 brute force with inset levels P<Q, central a,b strictly inside, opposite parity
def check(P,Qv,X):
  bad=[]
  for a in range(P+1,Qv):
    for b in range(P+1,Qv):
      if (a-b)%2==0: continue
      for x in range(-X,X+1):
        if x==0: continue
        for z in range(-X,X+1):
          if z==0: continue
          for (A,B,C,D) in [((0,a),(x,P),(0,b),(z,Qv)),((0,a),(x,Qv),(0,b),(z,P))]:
            U=(B[0]-A[0],B[1]-A[1]); V=(D[0]-C[0],D[1]-C[1])
            if U[0]**2+U[1]**2!=V[0]**2+V[1]**2: continue
            Hs=(C[0]+D[0]-A[0]-B[0],C[1]+D[1]-A[1]-B[1])
            if U[0]*Hs[0]+U[1]*Hs[1]!=0: continue
            if Hs==(0,0) or V==U or V==(-U[0],-U[1]): continue
            bad.append((P,Qv,A,B,C,D))
  return bad
tot=[]
for P in range(1,4):
  for Qv in range(P+3,P+14):
    tot+=check(P,Qv,60)
print("binary_boundary Sec2 inset counterexamples:",len(tot), tot[:3])
# 3) numeric ratios for Lambda, ell at h=1e10
h=1e10
print("(1+log h)/log h =",(1+math.log(h))/math.log(h), " ^8 =",((1+math.log(h))/math.log(h))**8)
print("(1+loglog 3h)/loglog h =",(1+math.log(math.log(3*h)))/math.log(math.log(h)))
print("loglog h at 1e10 =",math.log(math.log(h)))
# 4) margins with T3 ranges
print("r-L min",5000-14,"2(h-H) max",2*195,"H-r min",(-195)-(-5000),"2(L-1) max",26,"r-F min",5000-3743)
# 5) 2(2^s-1) vs 3^s-1
for s in [0.5,0.9124154,1,1.5,2,2.2]:
  print(s, 2*(2**s-1), 3**s-1)
# 6) W_h span: max (a+c) over ac=bd, b+d<=h-1, check equals floor((h-1)^2/4)+1 for small h
def maxspan(h):
  best=0
  for b in range(0,h):
    for d in range(0,h-b):
      if b+d>h-1: continue
      p=b*d
      if p==0: continue
      for a in range(1,p+1):
        if p%a==0: best=max(best,a+p//a)
  return best
print([(h,maxspan(h),(h-1)**2//4+1) for h in range(3,16)])
