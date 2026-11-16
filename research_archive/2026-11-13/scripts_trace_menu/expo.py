from mpmath import mp, mpf, findroot, log, diff
mp.dps = 40
def beta(k,a):
    if k is None: return 3**(a/2)
    return ((1+mpf(3)**(a/k))/2)**k - 1 if k else None
def f(k,a):
    if k is None: return (1+mpf(3)**(a/2))/(1+a)
    return (beta(k,a)+2)/(1+a)
claimed = {1:'1.4967430',2:'1.4295235',3:'1.3986921',4:'1.3807492',5:'1.3689531',6:'1.3605886',7:'1.3543412',8:'1.3494942',9:'1.3456226',10:'1.3424580',None:'1.3108172'}
for k in [1,2,3,4,5,6,7,8,9,10,None]:
    g = lambda a: diff(lambda t: f(k,t), a)
    a0 = findroot(g, mpf(1.2))
    x = f(k,a0)
    # grid check
    gm = min(f(k,mpf(i)/20000) for i in range(1,80000,7))
    print(k, 'a*=%s'%mp.nstr(a0,10), 'x=%s'%mp.nstr(x,13), 'grid>=x:', gm>=x-mpf('1e-12'), 'claim', claimed[k], 'ok' if mpf(claimed[k])>=x else 'TOO SMALL')
# heavy fraction: 2 - x < x
# Lemma MI check
from sympy import factorint, isprime
for u,q in [(1,5),(9,13),(113643,337)]:
    D=4*u*u+1
    v=0; t=D
    while t%q==0: t//=q; v+=1
    print(u,D,q,'v_q=',v, 'u odd', u%2==1)
print('P sums', sum([40,76]) /40, sum([40,76,204,396,1356])/40, 4*2*16*2.08*512, 136314.88*40)
