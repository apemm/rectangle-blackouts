# count I.2 and II solutions of the equations for a fixed list of block offsets, definition-checked
import sys
exec(open('enum_types.py').read().split('odd_offsets = ')[0].replace('h, s = int(sys.argv[1]), int(sys.argv[2])','h, s = 600, 2').replace("maxprint = int(sys.argv[3]) if len(sys.argv) > 3 else 3","maxprint=0"))
Ts=[-265,-261,-239,-499]
Q = lambda T, a: (s * s + 4) * a * a + 4 * a * T + T * T
tot=0; fails=0
for c,T in enumerate(Ts):
  sl=set(slots(T))
  for c2,T2 in enumerate(Ts):
    if c2==c: continue
    dc=c2-c; sl2=set(slots(T2))
    for a in range(-10,11):
      if a==0: continue
      kap=(s*s+4)*a+2*T
      for b in range(-A,A+1):
        if b==0 or Q(T,a)!=Q(T2,b) or (b,T2) in ((a,T),(-a,-T)): continue
        num=-(2*s*s*a*P*dc+(2*a+T)*(T2-T))
        if num%kap: continue
        m=num//kap
        if (m+a-b)%2: continue
        e=(m+a-b)//2
        for iA in sl:
          if iA+a in sl and iA+e in sl2 and iA+e+b in sl2:
            ok=is_mixed(point(c,T,iA,0),point(c,T,iA+a,1),point(c2,T2,iA+e,0),point(c2,T2,iA+e+b,1))
            tot+=ok; fails+=(not ok)
print("I.2 equation solutions passing definition:",tot,"failing (strip):",fails)
