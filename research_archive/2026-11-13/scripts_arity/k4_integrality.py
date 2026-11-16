
# Sanity check: four-cell mixed supports need X | yz AND X^2+y^2-w^2 a square.
# Compare Sum_{y,z,w in box} #{X: X|yz, X^2+y^2-w^2 = square} with Sum tau(|yz|) over the box.
import math, sys, time

def divisors_list(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return ds

def is_sq(n):
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n

def run(h):
    t0 = time.time()
    # tau sieve up to h*h*... products |yz| <= h^2
    M = h * h + 1
    tau = [0] * (M + 1)
    for d in range(1, M + 1):
        for k in range(d, M + 1, d):
            tau[k] += 1
    rng = [v for v in range(-h, h + 1) if v != 0]
    # naive tau bound: sum over y,z (nonzero) of tau(|yz|), times number of w (2h+1)
    s_tau = 0
    for y in rng:
        for z in rng:
            s_tau += tau[abs(y * z)]
    s_tau *= (2 * h + 1)
    # true count: for each (y,w): R = w^2 - y^2.
    true = 0
    for y in rng:
        ay = abs(y)
        for w in range(-h, h + 1):
            R = w * w - y * y
            if R == 0:
                # all X dividing yz
                for z in rng:
                    true += 2 * tau[abs(y * z)]  # X and -X
                continue
            # X^2 - X'^2 = R, X = (u+v)/2, uv = R
            Xs = set()
            aR = abs(R)
            for u in divisors_list(aR):
                v = aR // u
                if (u + v) % 2 == 0:
                    if R > 0:
                        X = (u + v) // 2
                    else:
                        X = abs(u - v) // 2
                    if X != 0:
                        Xs.add(X)
            for X in Xs:
                g = math.gcd(X, ay)
                step = X // g
                # z in rng with step | z ; both signs of X
                cnt = 2 * (h // step)  # positive and negative z
                true += 2 * cnt
    return s_tau, true, time.time() - t0

for h in [20, 40, 80, 120]:
    s, t, dt = run(h)
    L = 1 + math.log(h)
    print(f"h={h}: tau-bound sum={s}, true count={t}, ratio true/tau={t/s:.4f}, ratio*h={t/s*h:.3f}, true/(h^2 L^2)={t/(h*h*L*L):.3f}, {dt:.1f}s")
    sys.stdout.flush()
