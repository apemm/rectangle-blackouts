# Check: J - u = u[delta^2(1+1/r) + G(3-1/r) + u^2] / (2[N(1-1/r)^2 - u^2]),  G = g1 g2, r = N/G.
import sympy as sp
g1,g2,N,dl = sp.symbols('g1 g2 N delta')
K = N + dl**2
X = lambda g: -(g + K/(N/g - g))/2
J = X(g1) - X(g2); u = g2 - g1; G = g1*g2; r = N/G
rhs = u*(dl**2*(1+1/r) + G*(3-1/r) + u**2)/(2*(N*(1-1/r)**2 - u**2))
print('J-u formula:', sp.simplify(J - u - rhs) == 0)
