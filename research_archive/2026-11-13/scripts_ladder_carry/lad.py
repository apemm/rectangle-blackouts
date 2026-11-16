"""LAD_6(E') layer as eta(rel): filler row = T* - 8*eta, rel = n - rho0 (slot relative to label residue).
Label (class) slots are rel = 0 mod 64.  Written from ladder_layer.md Theorem 4."""
import numpy as np

def phi(tau, Ep):
    if tau % 2: return 1 + 2 * (((tau - 1) // 2) % 4)
    if tau % 4 == 2: return 2 + 4 * (((tau - 2) // 4) % 4)
    if tau % 8 == 4: return 4 + 8 * (((tau - 4) // 8) % 4)
    if tau % 16 == 8: return 8 + 16 * (((tau - 8) // 16) % 4)
    return 16 * ((tau // 16) % (2 ** Ep))

def eta(rel, Ep):
    o = rel % 4
    if o == 1: return 2          # T* - 16
    if o == 3: return 0          # T*
    if o == 2: return 1 + 4 * (((rel - 2) // 4) % 4)   # T* - 8 - 32 k
    return 3 + 4 * phi(rel // 4, Ep)                    # T* - 24 - 32 phi

def period(Ep):
    return 4 * max(64, 16 * 2 ** Ep)

def eta_array(Ep):
    P = period(Ep)
    return np.array([eta(r, Ep) for r in range(P)], dtype=np.int64), P

def v2(n):
    n = abs(n)
    if n == 0: return 99
    c = 0
    while n % 2 == 0: n //= 2; c += 1
    return c
