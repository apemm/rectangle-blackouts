import numpy as np
ln3 = np.log(3.0)
def E(a): return (1 + 3.0**a)/2
A = np.linspace(0, 6, 6001)
def rank_tail(x):            # rigorous Rankin: (1/h)#{kappa > L^x} <= L^{min_a>0 E(a)-1-a x}
    a = A[A > 0]; return np.min(E(a) - 1 - a*x)
def rank_sum(x, beta):       # (1/h) sum_{L^x < kappa <= L^{x/beta}} kappa^beta, Rankin with a>=beta (lower cut) or a<=beta (upper cut)
    a = A
    cut = np.where(a >= beta, x, x/beta) if beta > 0 else np.where(a >= beta, x, 1e9)
    v = E(a) - 1 + (beta - a)*cut
    return np.min(v)
X = np.linspace(0.3, 2.5, 2201)
def theta_beta(beta, bad=True):
    best = (9, None)
    for x in X:
        e = [x]
        if bad:
            e.append(2 - x)                       # light Bad_split (Prop 3)
            e.append(2 - x + rank_sum(x, beta))   # heavy handled by (F_beta)
        e.append(2 + (rank_tail(x/beta) if beta > 0 else -9))  # too heavy -> Theorem E
        m = max(e)
        if m < best[0]: best = (m, x)
    return best
print("theta*(check, beta=1):", theta_beta(1.0), theta_beta(1.0, bad=False))
for b in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.63093, 0.7, 0.8, 0.9, 0.95, 1.0]:
    print(f"beta={b:.3f}  with Bad_split: {theta_beta(b)[0]:.5f} (x={theta_beta(b)[1]:.3f})   without: {theta_beta(b, bad=False)[0]:.5f}")
# uniform K0 = Lambda^c on heavy diagonals
def phi(xi):
    y = xi/ln3
    return 0.0 if y <= 0.5 else 0.5 - y + y*np.log(2*y)
print("phi(1) =", phi(1.0))
for c in [0.0, 0.1, 0.135, 0.2, 0.3, 0.5, 0.75, 1.0]:
    best = 9
    for x in X:
        if x < c: continue
        best = min(best, max(x, 2 - x, 2 - x - phi(x) + c))
    print(f"K0=Lambda^{c}: exponent {best:.5f}")
