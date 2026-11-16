# Sanity check (toy): (3,4)-lines in a slot/row grid.
# 1) Lemma F geometry on the (3,4) line: X=21k, y=28k -> L=35|k|, u+- multiples of 7.
# 2) T3 adjacent-slot right angle: (7,14).(-2(rho-a), rho-a) = 0.
# 3) Random lists: max common neighbourhood on lines vs D/m and vs bound D/(384m).
import random, math, collections
ok=True
for k in range(-40,41):
    if k==0: continue
    X,y=21*k,28*k; L=math.isqrt(X*X+y*y)
    ok &= (L*L==X*X+y*y and L==35*abs(k) and (X-L)%14==0 and (X+L)%14==0)
for d in range(-60,61,7):
    ok &= (7*(-2*d)+14*d==0)
print("algebra ok:",ok)
random.seed(1)
K=60; M0=4          # rows 28k, k<K, M0 labels per row  -> n = K*M0 labels in one class
n=K*M0
for m,D in [(4,40),(4,160),(8,160),(16,640)]:
    N=m*n
    lists={}
    for k in range(K):
        for t in range(M0):
            lists[(k,t)]=random.sample(range(N),D)
    pts=collections.Counter()
    for (k,t),Ls in lists.items():
        for j in Ls: pts[(j,k)]+=1
    lines=collections.defaultdict(list)
    for (j,k),c in pts.items():
        lines[j-3*k].append(c)
    best=0; avg=[]
    for l,cs in lines.items():
        s=sum(cs); avg.append(s)
        if len(cs)>=3:
            cs=sorted(cs); best=max(best,s-cs[0]-cs[1])
    print(f"m={m} D={D} N={N}: max common(line) ={best}, mean line size={sum(avg)/len(lines):.2f}, D/m={D/m:.1f}, D/(384m)={D/(384*m):.3f}")
