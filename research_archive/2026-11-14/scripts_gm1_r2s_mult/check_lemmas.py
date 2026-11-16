"""Sanity checks (not proofs) of the new lemmas on brute-force R2s solutions.
(1) +-V lemma with a toy 2-power modulus S' = 2^e: if 2^e | X and 2^e | X+V, with v2(m) in {0,1}
    and v2(delta) >= 2, then v2(delta) + v2(m) >= 2e + 1.
(2) identity 4 U X = g^2 + delta^2 - 2K and the zone bounds |U| <= K/(2|X|) (inner arc, N>0),
    |U| <= K/(4|X|) (outer arc with g^2 < N+K), |T| < K/|X| (outer arc with g^2 > N+K)."""
import random, math
random.seed(3)
def v2(x):
    c = 0
    while x % 2 == 0: x //= 2; c += 1
    return c
viol1 = 0; tested1 = 0; viol2 = 0; tested2 = 0
for trial in range(300000):
    delta = 4 * random.randint(1, 400) * random.choice((1, -1))
    m = random.choice((1, -1)) * random.randint(2, 200000)
    if v2(m) > 1 or abs(delta) >= 2 * abs(m): continue
    N = delta * (2 * m - delta); K = 2 * m * delta
    for U in range(1, 60):
        for U_ in (U, -U):
            if (m * delta) % U_: continue
            T = -(m * delta) // U_
            R = U_ * U_ + N
            if R <= 0: continue
            Vr = math.isqrt(R)
            if Vr * Vr != R: continue
            for V in (Vr, -Vr):
                x2 = U_ + T - V
                if x2 % 2: continue
                X = x2 // 2
                if X == 0: continue
                g = V - U_
                tested2 += 1
                if 4 * U_ * X != g * g + delta * delta - 2 * K: viol2 += 1
                if N > 0:
                    if g * g < N and 2 * abs(U_) * abs(X) > K: viol2 += 1
                    if N < g * g < N + K and 4 * abs(U_) * abs(X) > K: viol2 += 1
                    if g * g > N + K and abs(T) * abs(X) >= K: viol2 += 1
                for e in (2, 3, 4):
                    if X % (2 ** e) == 0 and (X + V) % (2 ** e) == 0:
                        tested1 += 1
                        if v2(delta) + v2(m) < 2 * e + 1: viol1 += 1
print('lemma (1): cases with 2^e | X and 2^e | X+V:', tested1, 'violations', viol1)
print('lemma (2): solutions tested', tested2, 'violations', viol2)
