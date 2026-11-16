"""Coverage of the linear-block family xi(r) = c*floor(r/g) mod 3."""
import sys
sys.path.insert(0, r".")
from tg import uncovered, rels

def D(k, g):
    q, rr = divmod(k, g)
    return {q % 3} if rr == 0 else {q % 3, (q + 1) % 3}

def lb_ok(a, b, g):
    if 0 in D(a, g): return None
    U = D(b, g) | D(b + 1, g)
    for t in (1, 2):
        if t not in U: return t
    return None

def lb_any(a, b):
    for g in range(1, a + b + 3):
        t = lb_ok(a, b, g)
        if t: return g, t
    return None

def brute_check(a, b, s, g, c, R=None):
    """direct check of xi(r)=c*floor(r/g) mod 3 on the period 3g (plus margin)"""
    per = 3 * g
    xi = lambda r: (c * (r // g)) % 3
    for (k, d) in rels(a, b, s):
        for r in range(per):
            if xi(r + k) - xi(r) == d: return False
    return True

if __name__ == "__main__":
    N = int(sys.argv[1])
    fails = []
    for a in range(2, N + 1, 2):
        for b in range(1, N + 1):
            if not uncovered(a, b): continue
            res = lb_any(a, b)
            if res is None: fails.append((a, b)); continue
            g, t = res
            for s in (1, 2):
                c = (s * (2 if t == 2 else 1)) % 3  # c*t = s mod 3 -> c = s*t^{-1}; t^{-1}=t
                assert brute_check(a, b, s, g, c), (a, b, s, g, c)
    print("fails", len(fails), fails[:60])
