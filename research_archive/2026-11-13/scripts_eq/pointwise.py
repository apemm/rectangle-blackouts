"""Check Lemma 2: |D_T cap QZ| <= 2 g(|T|) (1 + 2 ln(sqrt5 h/|T|)/(3 Q ln phi)),
the Pisano facts ord_{2^k}(phi) = 3*2^(k-1), -1 not a power of phi mod 4,
and the Markov tail #{T: w_T >= M} <= pi h (ln h + 2)/(Q M)."""
import sys, math
from dyadic import dsets

def g(n):
    r = 1; p = 2; m = n
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p; e += 1
            if p % 5 in (1, 4):
                r *= 2 * e + 1
        p += 1
    if m > 1 and m % 5 in (1, 4):
        r *= 3
    return r

def pisano(mod):
    a, b, n = 0, 1, 0
    while True:
        a, b = b, (a + b) % mod; n += 1
        if a == 0 and b == 1:
            return n

for k in range(1, 12):
    assert pisano(2 ** k) == 3 * 2 ** (k - 1)
# phi^n = F_n phi + F_{n-1}; -1 mod 4 means F_n = 0, F_{n-1} = 3 mod 4
F = [0, 1]
for i in range(60):
    F.append(F[-1] + F[-2])
assert not any(F[n] % 4 == 0 and F[n - 1] % 4 == 3 for n in range(1, 60))
print("Pisano facts ok")

lp = math.log((1 + 5 ** 0.5) / 2)
for h in [int(x) for x in sys.argv[1:]]:
    D = dsets(h); lnh = math.log(h)
    for a in range(1, 8):
        Q = 2 ** a
        worst = 0.0; viol = 0
        w = {}
        for T, v in D.items():
            wt = sum(1 for d in v if d % Q == 0); w[T] = wt
            if wt == 0:
                continue
            b = 2 * g(abs(T)) * (1 + 2 * math.log(5 ** 0.5 * h / abs(T)) / (3 * Q * lp))
            worst = max(worst, wt / b); viol += wt > b
        line = "h=%d Q=%d lemma2 viol=%d max ratio=%.3f |" % (h, Q, viol, worst)
        for M in (1, 2, 4, 8):
            cnt = sum(1 for x in w.values() if x >= M)
            line += " M=%d: %d<=%.0f" % (M, cnt, math.pi * h * (lnh + 2) / (Q * M))
        print(line)
