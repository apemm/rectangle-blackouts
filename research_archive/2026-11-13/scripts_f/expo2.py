import numpy as np
from scipy.optimize import brentq
ln3=np.log(3.0); E=lambda a:(1+3.0**a)/2
A=np.linspace(1e-6,8,8001)
tail=lambda xi: np.min(E(A)-1-A*xi)          # rigorous Rankin exponent of (1/h)#{kappa>Lambda^xi}
def phi(xi):
    y=xi/ln3; return 0.0 if y<=0.5 else 0.5-y+y*np.log(2*y)
print("check tail vs -phi:", tail(1.5), -phi(1.5), tail(2.0), -phi(2.0))
xi1=brentq(lambda xi: phi(xi)-1, 1.0, 3.0); print("phi(xi)=1 at xi=",xi1, " so gamma >=", xi1-1)
X=np.linspace(0,2.5,25001)
def theta(beta,gamma,bad=True):
    best=9
    for x in X[::25]:
        cut_hi=(x+gamma)/beta
        e=[x, 2+tail(cut_hi)]
        if bad:
            e.append(2-x)
            # sum_{Lambda^x<kappa<=Lambda^{cut_hi}} kappa^beta, Rankin both sides
            v=np.min(E(A)-1+(beta-A)*np.where(A>=beta,x,cut_hi))
            e.append(2-x-gamma+v)
        best=min(best,max(e))
    return best
for g in [0,0.25,0.5,0.75,0.9,0.974,1.0]:
    print(f"beta=1 gamma={g}: with Bad_split {theta(1,g):.4f}   without {theta(1,g,False):.4f}")
