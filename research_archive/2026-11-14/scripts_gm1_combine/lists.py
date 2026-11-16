"""Exact list tests for slot systems on a rank interval [0, N).
A gap q at block size M gives slots (d, delta) with d in {floor(q/M), ceil(q/M)}, d >= 1,
delta = q - M d.  Full candidate system: every pair (r, r+d) inside the interval is constrained.
"""
import itertools, sys

def slots(q, M):
    out = set()
    for d in (q // M, -(-q // M)):
        if d >= 1 and abs(q - M * d) <= M - 1:
            out.add((d, q - M * d))
    return sorted(out)

def cons(gaps, M, N):
    c = []
    for q in gaps:
        for d, de in slots(q, M):
            for r in range(N - d):
                c.append((r, r + d, de))
    return c

def solve(N, lists, C):
    # backtracking in increasing rank; constraints indexed by later endpoint
    back = [[] for _ in range(N)]
    for r, u, de in C:
        back[u].append((r, de))
    x = [None] * N
    def rec(u):
        if u == N:
            return True
        for v in lists[u]:
            if all(v - x[r] != de for r, de in back[u]):
                x[u] = v
                if rec(u + 1):
                    return True
        x[u] = None
        return False
    return x if rec(0) else None

PAIRS = [(0, 1), (0, 2), (1, 2)]

def all_size2_unsat(gaps, M, Nmax):
    """smallest N for which some assignment of 2-element lists is unsolvable"""
    for N in range(2, Nmax + 1):
        C = cons(gaps, M, N)
        for L in itertools.product(PAIRS, repeat=N):
            if solve(N, L, C) is None:
                return N, L
    return None

def few_restricted(gaps, M, N, kmax):
    """least number k of labels with 2-element lists (others full) giving an unsolvable instance"""
    C = cons(gaps, M, N)
    full = tuple(range(M))
    for k in range(0, kmax + 1):
        for pos in itertools.combinations(range(N), k):
            for Ls in itertools.product(PAIRS, repeat=k):
                L = [full] * N
                for p, l in zip(pos, Ls):
                    L[p] = l
                if solve(N, L, C) is None:
                    return k, pos, Ls
    return None

if __name__ == "__main__":
    M = 3
    print("single nondivisible gap, all lists of size 2:")
    for q in [1, 2, 4, 5, 7, 8]:
        print(" q=", q, slots(q, M), all_size2_unsat([q], M, 9))
    print("two-gap systems covered by Theorem 2, all lists size 2, and few restricted labels:")
    for (a, b, s) in [(1, 0, 1), (1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 2, 1), (3, 1, 1)]:
        g = [3 * a, 3 * b + s]
        r1 = all_size2_unsat(g, M, 8)
        r2 = few_restricted(g, M, 12, 3)
        print(" (a,b,s)=", (a, b, s), "gaps", g, "allsize2:", r1, " few:", r2)
