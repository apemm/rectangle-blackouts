import math
E=lambda a:(1+3**a)/2
f=lambda a:(E(a)+1)/(1+a)
lo,hi=0.1,3.0
for _ in range(200):
    m1=lo+(hi-lo)/3; m2=hi-(hi-lo)/3
    if f(m1)<f(m2): hi=m2
    else: lo=m1
a=(lo+hi)/2; th=f(a)
print("a*",round(a,7),"theta*",round(th,7),"E(a*)",round(E(a),7),"4^a*",round(4**a,4),"2-theta*",round(2-th,7))
print("middle term at x=theta*", E(a)+1-a*th)
# Legendre: phi(x)=max_a(a x - E(a)) + ... check root of x = min_a (E(a)+1-a x) via grid on max(x, min_a(E+1-ax))
def g(x):
    return min(E(b)+1-b*x for b in [i/2000 for i in range(1,8000)])
print("root check g(theta*)", g(th))
print("width const", 512*4*80*16*2.08)
print("U1 ratio", 1.04**2/0.125, "16*1.04", 16*1.04, "64*1.04*40", 64*1.04*40)
L=math.log(1e10); print("(1+1/log h)^3 at 1e10", (1+1/L)**3)
print("Lemma AP threshold h >", 2e5+1568*(1.8e5/2)**2)
print("1+10/614", 1+10/614, "1+10/294", 1+10/294)
# class separation 64p - 4(A-1) > 2W_h+1, p>=40h+1
def ok(h,slack=True):
    A=-(-h//2); W=(h-1)**2//4+1; p=40*h+1
    return 64*p-(4*(A-1) if slack else 0) > 2*W+1
last=max(h for h in range(10,20000) if ok(h)); last2=max(h for h in range(10,20000) if ok(h,False))
print("sep holds through",last,"without slack",last2, "all below?", all(ok(h) for h in range(10,last+1)))
# 2F-L range, F in [1000,3743], L odd in [1,13]
print("2F-L range", 2*1000-13, 2*3743-1)
# filler/odd-row residues: y_P=2iota+1, filler rows y_P+8(w+c) mod 64; odd label rows 2i+1, i=iota mod 32
bad=0
for iota in range(32):
    yP=2*iota+1
    rows=[(yP+8*(w+c))%64 for w in range(4) for c in (1,3)]+[yP%64]
    want=1 if iota%2==0 else 3
    bad+=sum(1 for r in rows if r%4!=want)
print("odd deep rows residue failures", bad)
print("R_FF+ neighbours", 210//32)
print("mod7_inset margins", 5000-14, 2*195, 4805, 2*13, 5000-3743)
print("thin", 5/152+1, 1/35+1)
print("rho/7sqrt", 224/32)
