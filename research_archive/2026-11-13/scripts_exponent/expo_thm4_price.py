import math
L3 = math.log(3)
def E(a): return (1 + 3**a) / 2
def Phi(xi):
    y = xi / L3
    if y <= 0.5: return 0.0
    return 0.5 - y + y * math.log(2 * y)
AS = [k * 0.002 for k in range(0, 3001)]  # a in [0,6]
def Psi(x, bd, g):
    best = 1e9
    for a in AS:
        cut = x if a >= bd else (x + g) / bd
        v = E(a) - 1 + (bd - a) * cut
        if v < best: best = v
    return best
def theta4(bd, g, bE, bD, withD=True):
    best = (1e9, None)
    for k in range(0, 1201):
        x = k * 0.0025
        terms = [x, bE - Phi((x + g) / bd)]
        if withD:
            terms += [bD - x, bD - x - g + Psi(x, bd, g)]
        v = max(terms)
        if v < best[0]: best = (v, x)
    return best
# consistency with independence_density_f Theorem 4 values at prices 2,2
print("bd=1,g=0 (should be ~1.4967):", theta4(1, 0, 2, 2))
print("bd=0.5,g=0 with/without (note: 1.172/0.991):", theta4(0.5, 0, 2, 2), theta4(0.5, 0, 2, 2, False))
print("bd=1,g=0.5 (note: 1.25):", theta4(1, 0.5, 2, 2))
for (bd, g) in [(1, 0.5), (1, 1.0), (0.5, 0)]:
    for beta in [2.0, 1.5, 1.0]:
        w = theta4(bd, g, beta, beta)
        wo = theta4(bd, g, beta, beta, False)
        print(f"H({bd},{g}) price beta={beta}: with Bad_split {w[0]:.4f} (x={w[1]:.4f}); without {wo[0]:.4f}")
