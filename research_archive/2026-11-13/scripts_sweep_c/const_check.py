import math
out=[]
def W(h): return (h-1)**2//4+1
# 1. obstruction 1(d): 64 l p - 2h > 2600 h^2 at the lower ends l>1.04h, p>40h
out.append(("1d 64*1.04*40", 64*1.04*40))
# 2. V3 family (d) emptiness threshold: 64 p > 2W_h with p >= 40h+1 ; find first h where it fails
h=100
while 64*(40*h+1) > 2*W(h): h+=1
out.append(("V3(d) first failing h for 64(40h+1)>2W_h", h))
h=100
while 64*(40*h+1) >= 2*W(h)+1: h+=1
out.append(("V3(d) first failing h for 64(40h+1)>=2W_h+1", h))
# 3. D-2L2F: 4*158h > 420^2
out.append(("h>=280 check", 4*158*280>420**2, 4*158*279>420**2))
# 4. cross-class |Dx| >= 4p - 4(A-1) > 158h for p>=40h+1
ok=all(4*(40*h+1)-4*((h+1)//2-1)>158*h for h in range(10,100000))
out.append(("4p-4(A-1)>158h",ok))
# 5. filled_mod7 counts
out.append(("F window size/14", (3743-1000+1)/14, "H window size/14",196/14))
hh=10**10
out.append(("F separation 2sqrt((h-4000)/195)", 2*math.sqrt((hh-4000)/195)))
out.append(("H separation 2sqrt(h-209)/13 approx", 2*math.sqrt((hh-209)/13)))
out.append(("(9) F-L min", 1000-14, "2max", 2*max(13,195), "H-F min", hh-195-3743))
out.append(("sec4 r-F min", 5000-3743, "r+F max vs H-L+2 min", (hh-5000+3743) < (hh-195-14+2)))
# 6. T2 sea sums normalized {0,3,1}
S=[0,3,1]; out.append(("sea sums mod 7", sorted({(a+b)%7 for a in S for b in S})))
# allowed triangle at high: x^2 + (r-1)(s-1) = 0 mod 7
sq={(x*x)%7 for x in range(1,7)}
for r in (0,5):
  for s in (0,5):
    sols=[x for x in range(1,7) if (x*x+(r-1)*(s-1))%7==0]
    out.append(("high root r,s",r,s,sols, [x for x in sols if x in sq]))
# low root: x^2 + r s = 0
out.append(("low root", [(r,s,[x for x in range(1,7) if (x*x+r*s)%7==0]) for r in (0,5) for s in (0,5)]))
# 7. Remark G exponent and E5 exponents
z=6; out.append(("RemG",(z-1)/2-3*math.log(z)))
# 8. Q3 Case 2a: U_x = 4*odd => U_x^2 mod 128
out.append(("Ux^2 mod128",{(4*o)**2%128 for o in range(1,200,2)}))
# 9. Phi residues: 8(o+c) mod 64 for o in 0..3, c in {1,3}
out.append(("Phi",{(o,c):(8*(o+c))%64 for o in range(4) for c in (1,3)}))
# 10. high/low span: number of j values bound
out.append(("j-range bound F+h-H",3743+195))
for x in out: print(x)
