import numpy as np
S = np.linspace(1.01, 6, 150)[:,None]
T2 = np.linspace(0.0, 4, 41)[None,:]     # partner class-weight exponent t''
T = np.linspace(1.0, 8, 141)
def mu(nu, om): return max(nu, np.max(T*om - (2**T - 1)))
def terms(nu, om):
    m = mu(nu, om); cw = 1.0 if om <= 3 else 4.0/3
    TA = float(np.min(-(1-1/S)*m + (3**S - 1)/S)); TA = min(TA, 2 + min(0, 1-om, 3-2*om))
    TB1 = cw*om + float(np.min(-(1-1/S)*m + (2**S - 1)/S))
    TB2 = float(np.min((cw - T2)*om - (1-1/S)*nu + (2**S + 2**(T2*S) - 2)/S))
    TB = min(TB1, TB2)
    if om <= 3: TB = min(TB, om + 1 + min(0, 1-om, 3-2*om))
    else: TB = min(TB, max(5-2*om, 4-2*om/3))
    TH = -m/2 + max(2, cw*om/2 + 0.75)
    return TA, TB, TH
for b in [0.0, 1.4967, 1.5, 2.0]:
    worst=-1e9; arg=None
    for nu in np.linspace(0, 16, 41):
        for om in np.linspace(0, 12, 49):
            tt=terms(nu,om); t=max(tt)
            if t > b and t+nu > worst: worst, arg = t+nu, (round(nu,2), round(om,2), [round(x,2) for x in tt])
    print("b=%.4f minimal a=%.3f worst=%s" % (b, worst, arg))
