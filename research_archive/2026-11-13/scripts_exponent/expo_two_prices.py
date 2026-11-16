import math, importlib.util, sys
spec = importlib.util.spec_from_file_location("eb", "expo_beta.py")
L3 = math.log(3)
def E(a): return (1 + 3**a) / 2
def phi(x):
    y = x / L3
    return 0.0 if y <= 0.5 else 0.5 - y + y * math.log(2 * y)
def thE(beta):
    if beta <= L3/2: return beta
    lo, hi = 0.0, 10.0
    for _ in range(200):
        m = (lo+hi)/2
        if 0.5 + 3**m*((1+m)*L3-1)/2 < beta: lo = m
        else: hi = m
    a = (lo+hi)/2
    return (E(a)-1+beta)/(1+a)
def grid(bE, bD, n=40000, xmax=3.0):
    best = bE  # option 2: everything to Theorem E (no light region)
    for k in range(n+1):
        x = xmax*k/n
        best = min(best, max(x, bE - phi(x), bD - x))
    return best
bEs = [2.0, 1.75, 1.5, 1.25, 1.135085, 1.0, 0.75, 0.55, 0.4]
bDs = [2.0, 1.75, 1.5, 1.25, 1.0, 0.5]
print("bE\bD  " + " ".join(f"{b:7.3f}" for b in bDs) + " | DC (no Bad_split)")
err = 0
for bE in bEs:
    row = []
    for bD in bDs:
        f = max(thE(bE), min(bE, bD/2))
        err = max(err, abs(f - grid(bE, bD)))
        row.append(f)
    print(f"{bE:7.4f} " + " ".join(f"{v:7.4f}" for v in row) + f" | {thE(bE):.4f}")
print("max |formula - grid| =", err)
print("1+phi(1) =", 1 + phi(1.0))
