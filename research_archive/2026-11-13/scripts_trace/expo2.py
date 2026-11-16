E=lambda a:(1+3**a)/2
a=0.9124153643995896
best=min((max(x, E(a)+1-a*x, 2-x),x) for x in [1+i*1e-5 for i in range(100001)])
print(best)
th=1.496742912669481
print(max(th,E(a)+1-a*th,2-th))
# joint min over a and x on grid
bb=min((max(x,E(aa)+1-aa*x,2-x),aa,x) for aa in [0.85+j*0.001 for j in range(130)] for x in [1.49+k*1e-4 for k in range(150)])
print(bb)
