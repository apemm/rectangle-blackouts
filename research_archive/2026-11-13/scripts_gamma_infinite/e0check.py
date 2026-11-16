import sympy as sp
x,y,r=sp.symbols('x y r')
# quartic from E0: (st)^2 = (20r^2+4r+1)(20r^2-4r+1)
print(sp.expand((20*r**2+4*r+1)*(20*r**2-4*r+1)))
w = y - 20*x**2
X = -10*w
Y = 5*x*(40*w-24)
expr = Y**2 - (X-10)*(X+10)*(X+6)
quart = y**2 - (400*x**4+24*x**2+1)
q, rem = sp.div(sp.expand(expr), sp.expand(quart), y)
print("remainder after reducing by quartic:", sp.simplify(rem))
# point count of E mod small primes
def cnt(p):
    c=1
    for X0 in range(p):
        f=((X0-10)*(X0+10)*(X0+6))%p
        if f==0: c+=1
        elif pow(f,(p-1)//2,p)==1: c+=2
    return c
print({p:cnt(p) for p in (3,7,11,13,17,19)})
