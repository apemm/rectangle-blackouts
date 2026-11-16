# Sanity check: P candidate degree of a label as a function of y=|2T+1| (T=j-i),
# full-grid Hilbert placement x=S(M r+xi). Standard Hilbert variant (Wikipedia d2xy/xy2d).
import numpy as np, sys, time
t0=time.time()
k=int(sys.argv[1]); h=2**(k+1); n=2**k  # label side n: i,j<n, rows 2i+1,2j+2<=h
S=int(sys.argv[2]); M=int(sys.argv[3]); NS=int(sys.argv[4])
def xy2d(x,y):
    x=x.copy(); y=y.copy(); d=np.zeros_like(x); s=n//2
    while s>0:
        rx=((x&s)>0).astype(np.int64); ry=((y&s)>0).astype(np.int64)
        d+=s*s*((3*rx)^ry)
        m=(ry==0)
        f=m&(rx==1)
        x[f]=s-1-x[f]; y[f]=s-1-y[f]
        tmp=x[m].copy(); x[m]=y[m]; y[m]=tmp
        s//=2
    return d
def d2xy(d):
    t=d.copy(); x=np.zeros_like(d); y=np.zeros_like(d); s=1
    while s<n:
        rx=1&(t//2); ry=1&(t^rx)
        m=(ry==0)
        f=m&(rx==1)
        x[f]=s-1-x[f]; y[f]=s-1-y[f]
        tmp=x[m].copy(); x[m]=y[m]; y[m]=tmp
        x+=s*rx; y+=s*ry; t//=4; s*=2
    return x,y
rng=np.random.default_rng(1)
qmax=(h-1)//S
# candidate (d,delta) list: q=M d+delta in [1,qmax], |delta|<=M-1, d>=1
pairs=[(d,dl) for d in range(1,qmax//M+3) for dl in range(-(M-1),M) if 1<=M*d+dl<=qmax]
D=np.array([p[0] for p in pairs]); Q=np.array([M*p[0]+p[1] for p in pairs])
X=S*Q
print("h",h,"pairs",len(pairs))
bins=list(range(0,k+2))
for b in bins:
    # sample labels with y=|2T+1| in [2^b,2^(b+1))
    ys=rng.integers(2**b,2**(b+1),size=NS*3); ys=ys|1
    T=np.where(rng.random(ys.size)<0.5,(ys-1)//2,-(ys+1)//2)
    i=rng.integers(0,n,size=ys.size); j=i+T
    ok=(j>=0)&(j<n); i=i[ok][:NS]; j=j[ok][:NS]
    if i.size==0: continue
    r=xy2d(i,j)
    tot=np.zeros(i.size)
    for sgn in (1,-1):
        R=r[:,None]+sgn*D[None,:]
        valid=(R>=0)&(R<n*n)
        Rc=np.clip(R,0,n*n-1)
        ip,jp=d2xy(Rc.ravel()); ip=ip.reshape(R.shape); jp=jp.reshape(R.shape)
        for role in (0,1):
            if role==0: ya=2*i[:,None]+1; yb=2*jp+2
            else: ya=2*j[:,None]+2; yb=2*ip+1
            Y=np.abs(yb-ya)
            L2=X[None,:]**2+Y**2
            L=np.round(np.sqrt(L2)).astype(np.int64)
            pyth=(L*L==L2)&(L<=h-1)
            lo=(ya+yb-L)//2; hi=(ya+yb+L)//2
            c=pyth&valid&(lo>=1)&(hi<=h)
            tot+=c.sum(axis=1)
    print("y in [2^%d,2^%d): n=%d mean deg %.4f  max %d"%(b,b+1,i.size,tot.mean(),tot.max()),flush=True)
print("time",time.time()-t0)
