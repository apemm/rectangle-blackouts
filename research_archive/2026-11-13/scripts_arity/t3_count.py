
# Sanity check for the three-corner (T3) count with vertex at e.
# For x: S(x) = sum_{u,v<=x} #{(X1,X2) positive: X1*X2 = u*v} = sum tau(uv).
# Lower bound from the injective map: Q(x) = #{(a,b,c,d): ab<=x, cd<=x, gcd(b,c)=1}.
import math, time
def run(x):
    M = x * x
    tau = [0] * (M + 1)
    for d in range(1, M + 1):
        for k in range(d, M + 1, d):
            tau[k] += 1
    S = 0
    for u in range(1, x + 1):
        for v in range(1, x + 1):
            S += tau[u * v]
    Qc = 0
    for b in range(1, x + 1):
        for c in range(1, x + 1):
            if math.gcd(b, c) == 1:
                Qc += (x // b) * (x // c)
    L = math.log(x)
    return S, Qc, S / (x * x * L * L), Qc / (x * x * L * L)
for x in [50, 100, 200, 400]:
    t0 = time.time()
    S, Qc, r1, r2 = run(x)
    print(f"x={x}: sum tau(uv)={S}, injective lower count={Qc}, S/(x^2 log^2 x)={r1:.3f}, Q/(x^2 log^2 x)={r2:.3f}, {time.time()-t0:.1f}s")
