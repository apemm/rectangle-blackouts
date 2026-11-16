# theta_m = inf_a (1+E_m(a))/(1+a), E_m(a) = ((1+3^(a/m))/2)^m; limit m->inf: E=3^(a/2).
# Also the k-threshold exponent (E-1)/a at the optimum and the heavy fraction exponent (E-1-2a)/(1+a).
import math
def E(a,m): return 3**(a/2) if m==0 else ((1+3**(a/m))/2)**m
for m in [1,2,3,5,10,0]:
    best=min(((1+E(a,m))/(1+a),a) for a in [i/1000 for i in range(1,6000)])
    th,a=best; e=E(a,m)
    print(f"m={'inf' if m==0 else m:>3}  theta={th:.4f} at a={a:.3f}  E(a)={e:.4f}  heavy-diag exponent (E-1-a*theta)={e-1-a*th:.4f}")
