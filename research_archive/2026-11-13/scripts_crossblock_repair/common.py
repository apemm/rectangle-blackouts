import math, random

def isqrt_exact(n):
    if n < 0: return None
    r = math.isqrt(n)
    return r if r*r == n else None

def is_prime(n):
    if n < 2: return False
    i = 2
    while i*i <= n:
        if n % i == 0: return False
        i += 1
    return True

def next_prime(n):
    while not is_prime(n): n += 1
    return n

def params(h):
    A = (h+1)//2; K = h//2
    return A, K

def diag_slots(h, s):
    """slots i of diagonal j = i + s: 0<=i<A, 0<=i+s<K"""
    A, K = params(h)
    lo = max(0, -s); hi = min(A, K - s)
    return list(range(lo, hi))

def dist_set(h, s, stride=4):
    """D_T: |d| with (stride d)^2 + (2d+T)^2 = L^2, 0<L<h, |d| < n_T"""
    T = 2*s+1
    sl = diag_slots(h, s); n = len(sl)
    D = set()
    for d in range(-(n-1), n):
        if d == 0: continue
        q = (stride*d)**2 + (2*d+T)**2
        L = isqrt_exact(q)
        if L is not None and L < h:
            D.add(abs(d))
    return D

def greedy_classes(h, s, stride=4):
    sl = diag_slots(h, s)
    D = dist_set(h, s, stride)
    col = {}
    for i in sl:
        used = set(col[i-d] for d in D if (i-d) in col)
        c = 0
        while c in used: c += 1
        col[i] = c
    M = max(col.values())+1 if col else 0
    classes = [[i for i in sl if col[i] == c] for c in range(M)]
    return classes, D

def all_classes(h, stride=4):
    A, K = params(h)
    out = []  # list of (s, slots list)
    for s in range(-(A-1), K):
        cl, D = greedy_classes(h, s, stride)
        for c in cl:
            if c: out.append((s, c))
    return out
