from fractions import Fraction
from math import gcd
worst = None
for u in (1, 3, 5, 7, 13):
    for beta in range(1, 60, 2):
        for alpha in range(-400, 401):
            if alpha % 2 == 0 or gcd(alpha, beta) != 1:
                continue
            D = u*beta - alpha
            if D == 0:
                continue
            F = 4*(alpha - 2*u*beta)**2 + beta**2
            e = 32*beta*beta  # least admissible e
            u2 = Fraction(2*alpha*e*F, 4*beta*beta*D)
            r = abs(u2)
            if worst is None or r < worst[0]:
                worst = (r, u, alpha, beta)
print("least |u2| at e = 32 beta^2:", float(worst[0]), worst[1:])
