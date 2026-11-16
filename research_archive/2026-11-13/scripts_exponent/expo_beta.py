import math
L3 = math.log(3)
def E(a): return (1 + 3**a) / 2
def phi(x):
    y = x / L3
    if y <= 0.5: return 0.0
    return 0.5 - y + y * math.log(2 * y)

def theta_E_closed(beta):
    # min over a>0 of (E(a)-1+beta)/(1+a); interior iff beta > ln3/2
    if beta <= L3 / 2: return beta, 0.0
    # solve beta(a) = 1/2 + 3^a((1+a)ln3 - 1)/2 for a by bisection
    lo, hi = 0.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        b = 0.5 + 3**mid * ((1 + mid) * L3 - 1) / 2
        if b < beta: lo = mid
        else: hi = mid
    a = (lo + hi) / 2
    return (E(a) - 1 + beta) / (1 + a), a

def theta_grid(bE, bD, withD=True, n=200000, xmax=3.0):
    best = (1e9, None)
    for k in range(n + 1):
        x = xmax * k / n
        v = max(x, bE - phi(x), (bD - x) if withD else -1e9)
        if v < best[0]: best = (v, x)
    return best

def theta_a_grid(beta, n=200000, amax=6.0):
    best = (beta, 0.0)
    for k in range(1, n + 1):
        a = amax * k / n
        v = (E(a) - 1 + beta) / (1 + a)
        if v < best[0]: best = (v, a)
    return best

print("check theta*:", theta_E_closed(2.0), theta_a_grid(2.0))
print("crossover beta0 = ln3/2 =", L3 / 2)
print("beta | theta_E(beta) | a* | x*=B exponent | grid(max x, beta-phi) | beta/2 | theta with Bad_split (equal prices)")
for beta in [2.0, 1.9, 1.8, 1.75, 1.7, 1.6, 1.5, 1.4, 1.3, 1.25, 1.2, 1.1, 1.0, 0.9, 0.8, 0.75, 0.7, 0.6, 0.55, 0.5, 0.4, 0.25]:
    t, a = theta_E_closed(beta)
    g = theta_grid(beta, beta, withD=False, n=60000)
    gD = theta_grid(beta, beta, withD=True, n=60000)
    print(f"{beta:5.2f} | {t:.7f} | {a:.6f} | x={t:.5f} | grid {g[0]:.6f} at x={g[1]:.4f} | {beta/2:.4f} | withD {gD[0]:.6f}")

# phi(x) = x crossing (where D term would start binding at equal prices)
lo, hi = 0.6, 10.0
for _ in range(200):
    mid = (lo + hi) / 2
    if phi(mid) < mid: lo = mid
    else: hi = mid
x0 = (lo + hi) / 2
print("phi(x)=x at x =", x0, " corresponding beta = x+phi(x) =", 2 * x0)

print("\nTwo prices: theta(bE,bD) = max(theta_E(bE), bD/2) with Bad_split; theta_E(bE) without")
bEs = [2.0, 1.75, 1.5, 1.25, 1.0, 0.75, 0.55]
bDs = [2.0, 1.75, 1.5, 1.25, 1.0, 0.5]
print("bE\\bD " + " ".join(f"{b:7.2f}" for b in bDs) + " |  noBad")
maxerr = 0
for bE in bEs:
    row = []
    for bD in bDs:
        f = max(theta_E_closed(bE)[0], bD / 2)
        g = theta_grid(bE, bD, withD=True, n=30000)[0]
        maxerr = max(maxerr, abs(f - g))
        row.append(f)
    print(f"{bE:5.2f} " + " ".join(f"{v:7.4f}" for v in row) + f" | {theta_E_closed(bE)[0]:.4f}")
print("max |closed - grid| over table:", maxerr)
# inverse: price needed for a target exponent
for target in [1.4, 1.25, 1.0, 0.75]:
    lo, hi = 0.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if theta_E_closed(mid)[0] < target: lo = mid
        else: hi = mid
    print(f"theta_E(beta) = {target} needs beta_E = {(lo+hi)/2:.6f}")
