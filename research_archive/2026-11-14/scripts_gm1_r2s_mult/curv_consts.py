"""Numerical sup of the normalized second and third derivatives of g = G(X) on the R2s curve
2X = K g/(g^2 - N) - g, in units where |N| = 1 (G'' scales as |N|^(-1/2), G''' as |N|^(-1)).
Closed forms (u = x^2 - sgn N, x = g/sqrt|N|):
 N>0: F' = -P/(2u^2), P = u^2 + k(u+2); F'' = k x (u+4)/u^3;  G''' = -96 k u^4 [k(u+1)(u+4)^2 - P(u^2+8u+8)/2]/P^5
 N<0: u = x^2+1, P = u^2 + k(2-u); F'' = k x (4-u)/u^3;    G''' = -96 k u^4 [k(u-1)(u-4)^2 + P(u^2-8u+8)/2]/P^5
 G'' = -F''/F'^3.  Also checked against finite differences of the inverse function."""
import math
def g2g3(x, k, pos):
    if pos:
        u = x*x - 1; P = u*u + k*(u+2); Fp = -P/(2*u*u); Fpp = k*x*(u+4)/u**3
        G3 = -96*k*u**4*(k*(u+1)*(u+4)**2 - P*(u*u+8*u+8)/2)/P**5
    else:
        u = x*x + 1; P = u*u + k*(2-u); Fp = -P/(2*u*u); Fpp = k*x*(4-u)/u**3
        G3 = -96*k*u**4*(k*(u-1)*(u-4)**2 + P*(u*u-8*u+8)/2)/P**5
    return -Fpp/Fp**3, G3
def F(x, k, pos):
    return (k*x/(x*x-1) - x)/2 if pos else (-k*x/(x*x+1) - x)/2
# finite-difference check of G''' via inverse function at a few points
def inv(Xt, k, pos, lo, hi):
    for _ in range(200):
        mid = (lo+hi)/2
        if (F(mid,k,pos) - Xt) * (F(lo,k,pos) - Xt) <= 0: hi = mid
        else: lo = mid
    return (lo+hi)/2
for (x0, k, pos, lo, hi) in [(0.5, 1.3, True, -0.999, 0.999), (2.0, 1.3, True, 1.0001, 50), (0.7, 0.6, False, -50, 50)]:
    X0 = F(x0, k, pos); h = 1e-3
    vals = [inv(X0 + j*h, k, pos, lo, hi) for j in (-2,-1,0,1,2)]
    fd3 = (vals[4] - 2*vals[3] + 2*vals[1] - vals[0])/(2*h**3)
    fd2 = (vals[3] - 2*vals[2] + vals[1])/h**2
    print('check x0', x0, 'k', k, 'N>0' if pos else 'N<0', 'G2', g2g3(x0,k,pos)[0], 'fd', fd2, 'G3', g2g3(x0,k,pos)[1], 'fd', fd3)
for pos, ks in ((True, [1.0, 1.25, 1.5, 1.75, 2.0]), (False, [0.05, 0.25, 0.5, 0.75, 1.0])):
    for k in ks:
        best2 = best3 = 0
        for i in range(1, 400001):
            x = i * 1e-4 * (1 if True else 1)
            if pos and abs(x - 1) < 1e-7: continue
            a, b = g2g3(x, k, pos)
            best2 = max(best2, abs(a)); best3 = max(best3, abs(b))
        print('N>0' if pos else 'N<0', 'kappa', k, 'sup|G2|', round(best2, 4), 'sup|G3|', round(best3, 4))
