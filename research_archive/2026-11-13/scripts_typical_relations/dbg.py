import sys; sys.argv=['x','1045','6000']
exec(open('cover.py').read().split("T = int(sys.argv[1])")[0])
A,Ls=Aset(1045,6000)
print(A)
th=0.440814
print(min(min((th*a)%1,1-(th*a)%1) for a in A))
for dl in (0.10,0.12,0.13,0.15,0.159,0.161):
    print(dl, covers_float(A,dl))
dl=0.13
lefts=[];rights=[]
for a in A:
    j=np.arange(0,a//2+2); lefts.append((j-dl)/a); rights.append((j+dl)/a)
l=np.concatenate(lefts); r=np.concatenate(rights); o=np.argsort(l); l=l[o]; r=r[o]
cm=np.maximum.accumulate(r)
bad=np.where(~(l[1:]<cm[:-1]-1e-13))[0]
print(len(bad), [(l[i+1],cm[i]) for i in bad[:5]], l[0], cm[-1])
