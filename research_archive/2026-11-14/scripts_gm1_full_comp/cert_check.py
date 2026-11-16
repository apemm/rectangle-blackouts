"""Independent check: for random (a, b, s) with a even and v3(a) <= 4, take the P_k-periodic solution found on Z/P_k
(P_k = 2*3^k, k = v3(a)+1) and verify the original constraints directly on integer ranks -R..R."""
import random
src = open("dyadic_period.py").read().split("if __name__")[0]
exec(src)
def v(p, n):
    c = 0
    while n % p == 0: n //= p; c += 1
    return c
random.seed(1)
tests = [(84, 86, 2), (344, 338, 2), (1360, 1370, 2)]
for _ in range(60):
    k = random.randint(1, 4); m = random.choice([1, 2, 4, 5, 7, 8, 10, 11]) * 2
    a = 3 ** (k - 1) * m * random.choice([1, 2, 4]); b = random.randint(0, 3000); s = random.choice([1, 2])
    tests.append((a, b, s))
bad = 0
for a, b, s in tests:
    k = v(3, a) + 1; P = 2 * 3 ** k
    sh = [(a % P, 0), (b % P, s), ((b + 1) % P, s - 3)]
    seq = solve_mod(P, sh)
    xi = lambda r: seq[r % P]
    cons = [(a, 0), (b + 1, s - 3)] + ([(b, s)] if b > 0 else [])
    okk = seq is not None and all(xi(r + sh_) - xi(r) != dl for r in range(-3000, 3001) for sh_, dl in cons)
    bad += (not okk)
print("tests", len(tests), "failures", bad, "; (252,260) uses P =", 2 * 3 ** (v(3, 84) + 1))
