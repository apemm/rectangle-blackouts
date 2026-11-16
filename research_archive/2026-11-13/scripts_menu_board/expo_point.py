# Evaluate (beta_k(a)+2)/(1+a) at the stated a*_k (any a>0 gives a valid
# exponent in Theorem N_menu, so a single evaluation is an upper bound).
from mpmath import mp, mpf, power
mp.dps = 40
astar = {1:'0.9124153',2:'1.1056653',3:'1.2096718',4:'1.2756813',5:'1.3215661',
         6:'1.3554037',7:'1.3814256',8:'1.4020770',9:'1.4188737',10:'1.4328078'}
for k,a in astar.items():
    a = mpf(a)
    beta = power((1+power(3,a/k))/2,k)-1
    print(k, mp.nstr((beta+2)/(1+a), 15))
a = mpf('1.5833613')
print('inf', mp.nstr((1+power(3,a/2))/(1+a), 15))
