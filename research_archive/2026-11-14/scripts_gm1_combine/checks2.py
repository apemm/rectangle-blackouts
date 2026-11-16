"""(1) least number of size-2 lists that kills a single two-slot gap at M=3 on [0,N).
(2) binary solvability of the two-gap M=3 system on long intervals versus the 2-adic condition.
(3) random test of the 2-adic signature rule for B_t components (general M, t)."""
import itertools, random
from lists import slots, cons, solve, few_restricted

def v2(n):
    if n == 0:
        return 10**9
    k = 0
    while n % 2 == 0:
        n //= 2; k += 1
    return k

M = 3
print("(1) single gaps, least number of restricted labels (N=12):")
for q in [4, 5, 7, 8, 10, 11]:
    print("  q=", q, few_restricted([q], M, 12, 3))

print("(2) binary palettes on [0,N) versus condition v2(b)>v2(a) or v2(b+1)>v2(a):")
bad = 0; tot = 0
for a in range(1, 9):
    for b in range(0, 9):
        for s in (1, 2):
            g = [3 * a, 3 * b + s]
            N = 4 * a + 2 * b + 8
            C = cons(g, M, N)
            ok2 = any(solve(N, [P] * N, C) is not None for P in [(0, 1), (1, 2), (0, 2)])
            cond = v2(b) > v2(a) or v2(b + 1) > v2(a)
            tot += 1
            if ok2 != cond:
                bad += 1
                print("  mismatch", a, b, s, ok2, cond)
print("  checked", tot, "triples; mismatches:", bad)

print("(3) 2-adic signature rule on random rank sets:")
random.seed(1)
viol = 0; tested = 0
for trial in range(4000):
    M = random.randint(2, 6)
    t = random.randint(1, M - 1)
    v = random.randint(0, 3)
    # divisible gaps M*a with v2(a)=v
    gaps = set()
    for _ in range(random.randint(0, 3)):
        gaps.add(M * (2 ** v) * random.choice([1, 3, 5, 7]))
    # nondivisible gaps: binding slot rank differences must have v2 > v
    for _ in range(random.randint(0, 3)):
        q = random.randint(1, 120)
        if q % M == 0:
            continue
        okq = all(v2(d) > v for d, de in slots(q, M) if de in (t, -t))
        if okq:
            gaps.add(q)
    if not gaps:
        continue
    ranks = sorted(random.sample(range(-60, 200), 80))
    rs = set(ranks)
    phase = random.randint(0, 50)
    comp = random.randint(0, 1)
    xi = {r: t * (((r + phase) // (2 ** v) + comp) % 2) for r in ranks}
    for q in gaps:
        for d, de in slots(q, M):
            for r in ranks:
                if r + d in rs:
                    tested += 1
                    if xi[r + d] - xi[r] == de:
                        viol += 1
print("  constraints tested", tested, "violations", viol)
