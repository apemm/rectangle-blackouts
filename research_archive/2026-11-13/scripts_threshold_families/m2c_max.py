# All M2c shapes via (n1, w, e): w | e^2+n1^2, Delta=2n1+(e^2+n1^2)/w, u2 = n1((n1+w)^2+e^2)/(e w)
# with u2>=1, u2+e<=h-1 (sea row r0>=1), shallowness. Report max |Delta|/h and the extremal shapes.
import sys
def run(h):
    best=[]; 
    for e in range(1,h):
        for n1 in range(-h*h//4, h*h//4+1) if False else range(-(h*h)//(4*e)-1, (h*h)//(4*e)+2):
            if n1==0: continue
            S=e*e+n1*n1
            # divisors w of S (both signs)
            d=1; ws=[]
            while d*d<=S:
                if S%d==0: ws+= [d,S//d]
                d+=1
            for a in ws:
                for w in (a,-a):
                    m=n1+w; num=n1*(m*m+e*e); den=e*w
                    if num%den: continue
                    u2=num//den
                    if u2<1 or u2+e>h-1: continue
                    D=2*n1+S//w; z=-(D+w)
                    if z%4==0 or (2*n1-z)%4==0: continue
                    assert n1*((D-n1)**2+e*e)==e*u2*(D-2*n1)
                    best.append((abs(D)/h,e,n1,w,u2,D,z))
    best.sort(reverse=True); return best[:6], len(best)
for h in map(int,sys.argv[1:]):
    b,n=run(h); print(h,n); [print('  ',x) for x in b]
