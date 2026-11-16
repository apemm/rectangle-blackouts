"""M = 3 two-gap systems q0 = 3a, q1 = 3b + s on integer ranks.
(1) verify the 3-adic rule xi = pi(floor(r/g) mod 3) on ranks -R..R for many (a,b,s);
(2) for given pairs, search for a P-periodic solution (circulant CSP on Z/P) with pysat."""
import sys, math
from pysat.solvers import Cadical153

def v(p, n):
    if n == 0: return 10 ** 9
    c = 0
    while n % p == 0: n //= p; c += 1
    return c

def cons(a, b, s):
    # (shift, forbidden difference); rank difference 0 ignored
    out = [(a, 0)]
    if b > 0: out.append((b, s))
    out.append((b + 1, s - 3))
    return out

def ok_on_range(xi, a, b, s, R):
    for r in range(-R, R + 1):
        for sh, dl in cons(a, b, s):
            if xi(r + sh) - xi(r) == dl: return False
    return True

def rule3(a, b, s):
    if v(3, b) > v(3, a):
        g = math.gcd(a, b); pi = (0, 1, 2) if s == 2 else (0, 2, 1)
    elif v(3, b + 1) > v(3, a):
        g = math.gcd(a, b + 1); pi = (0, 2, 1) if s == 2 else (0, 1, 2)
    else: return None
    return lambda r: pi[(r // g) % 3]

def periodic(a, b, s, Pmax):
    for P in range(1, Pmax + 1):
        sol = Cadical153(); var = lambda k, c: 3 * k + c + 1
        for k in range(P):
            sol.add_clause([var(k, c) for c in range(3)])
            for c in range(3):
                for c2 in range(c + 1, 3): sol.add_clause([-var(k, c), -var(k, c2)])
        bad = False
        for sh, dl in cons(a, b, s):
            for k in range(P):
                k2 = (k + sh) % P
                for c in range(3):
                    c2 = c + dl
                    if 0 <= c2 <= 2:
                        if k == k2 and c == c2: bad = True
                        sol.add_clause([-var(k, c), -var(k2, c2)])
        if bad: continue
        if sol.solve():
            m = sol.get_model(); seq = [next(c for c in range(3) if m[3 * k + c] > 0) for k in range(P)]
            return P, seq
    return None

if __name__ == "__main__":
    if sys.argv[1] == "verify":
        n = 0; fails = 0
        for a in range(1, 61):
            for b in range(0, 61):
                for s in (1, 2):
                    xi = rule3(a, b, s)
                    if xi is None: continue
                    n += 1
                    if not ok_on_range(xi, a, b, s, 400): fails += 1; print("FAIL", a, b, s)
        print("3-adic rule checked on", n, "triples (a<=60, b<=60), ranks -400..400; failures", fails)
    else:
        Pmax = int(sys.argv[2])
        for pr in sys.argv[3:]:
            q0, q1 = map(int, pr.split(","))
            a = q0 // 3; b, s = divmod(q1, 3)
            res = periodic(a, b, s, Pmax)
            print((q0, q1), "a,b,s =", (a, b, s), "->", ("period %d" % res[0]) if res else "no period <= %d" % Pmax,
                  ("" if not res else "".join(map(str, res[1]))[:120]))
