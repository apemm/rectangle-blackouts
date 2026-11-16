# Exponent bookkeeping (log base Lambda, relative to Q) for the arbitrary-Y Holder lemma.
import numpy as np
S = np.linspace(1.001, 6, 2000)          # Holder exponents
T = np.linspace(1.0, 8, 701)             # class-size moment exponents
def mu(nu, om):
    return max(nu, np.max(T*om - (2**T - 1)))
def terms(nu, om):
    m = mu(nu, om)
    cw = 1.0 if om <= 3 else 4.0/3
    TA = np.min(-(1-1/S)*m + (3**S - 1)/S)
    TA = min(TA, 2 + min(0, 1-om, 3-2*om))
    TB = cw*om + np.min(-(1-1/S)*m + (2**S - 1)/S)
    if om <= 3: TB = min(TB, om + 1 + min(0, 1-om, 3-2*om))
    else: TB = min(TB, max(5-2*om, 4-2*om/3))
    TH = -m/2 + max(2, cw*om/2 + 0.75)
    return TA, TB, TH
def need_a(b):
    worst = -1e9; arg=None
    for nu in np.linspace(0, 12, 241):
        for om in np.linspace(0, 12, 241):
            t = max(terms(nu, om))
            if t > b:                      # must be paid by n*Lambda^a
                if t + nu > worst: worst, arg = t + nu, (nu, om, terms(nu,om))
    return worst, arg
for b in [0.0, 1.0, 1.4967, 1.5, 1.75]:
    a, arg = need_a(b)
    print("b=%.4f  minimal a = %.3f   worst (nu, omega)=(%.2f, %.2f) terms=%s" % (b, a, arg[0], arg[1], tuple(round(x,3) for x in arg[2])))
