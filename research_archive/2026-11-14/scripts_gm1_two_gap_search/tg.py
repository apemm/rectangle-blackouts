"""Two-gap three-choice system at M=3.
xi: Z -> {0,1,2};  forbid xi[r+a]==xi[r];  xi[r+b]-xi[r]==s;  xi[r+b+1]-xi[r]==s-3.
"""
import sys, time
from pysat.solvers import Glucose4

def v2(n):
    if n == 0: return 10**9
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k

def uncovered(a, b):
    if a % 2: return False
    al = v2(a); m = 2 ** (al + 1)
    return b % m not in (0, m - 1)

def rels(a, b, s):
    """list of (shift k, forbidden integer difference d)"""
    out = [(a, 0)]
    if b > 0: out.append((b, s))
    out.append((b + 1, s - 3))
    return out

def var(r, v): return 3 * r + v + 1

def base_clauses(n):
    cl = []
    for r in range(n):
        cl.append([var(r, 0), var(r, 1), var(r, 2)])
        for u in range(3):
            for w in range(u + 1, 3):
                cl.append([-var(r, u), -var(r, w)])
    return cl

def pair_clauses(r, t, d):
    """forbid xi[t]-xi[r]==d"""
    cl = []
    for v in range(3):
        w = v + d
        if 0 <= w <= 2:
            if r == t:
                if d == 0: cl.append([-var(r, v)])
            else:
                cl.append([-var(r, v), -var(t, w)])
    return cl

def periodic_cnf(a, b, s, p):
    cl = base_clauses(p)
    for (k, d) in rels(a, b, s):
        for r in range(p):
            cl += pair_clauses(r, (r + k) % p, d)
    return cl

def interval_cnf(a, b, s, L):
    cl = base_clauses(L)
    for (k, d) in rels(a, b, s):
        for r in range(L - k):
            cl += pair_clauses(r, r + k, d)
    return cl

def solve(cl, n):
    with Glucose4(bootstrap_with=cl) as S:
        if S.solve():
            m = set(x for x in S.get_model() if x > 0)
            return [next(v for v in range(3) if var(r, v) in m) for r in range(n)]
        return None

def check_periodic(a, b, s, sol):
    p = len(sol)
    for (k, d) in rels(a, b, s):
        for r in range(p):
            if sol[(r + k) % p] - sol[r] == d: return False
    return True
