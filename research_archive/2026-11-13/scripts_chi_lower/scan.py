import sys, time, itertools
from nbchi import build, chi
sp=[11,19,29,31,41,59,61,71,79,89,101,109]
Ts=[]
for w in (1,2,3):
    for c in itertools.combinations(sp[:8] if w<3 else sp[:6], w):
        T=5
        for l in c: T*=l
        Ts.append((w,T))
Ts+= [(1,5*121),(2,5*121*19),(1,5*11**3)]
t0=time.time(); hist={}
for w,T in Ts:
    if time.time()-t0>95: break
    G=build(T,10**10,"nb"); k,om=chi(G,8)
    hist.setdefault((w,k,om),[]).append(T)
    if k>=5: print("FOUND",T,k,om,flush=True)
for key in sorted(hist): print(key,len(hist[key]),hist[key][:6])
print("time",time.time()-t0)
