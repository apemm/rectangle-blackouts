# Pisot-rotation colourings of Cay(Z, D_T^inf).
# Colour c(x) = g(floor(N*{theta x}), x mod M), theta = alpha/sqrt5, alpha = p/q rational.
# Shifts: every signed d in S_T^inf.  Exact part |d| <= B (orbit enumeration, exact integers,
# phases in mpmath 60 digits); tails: residue states mod Q along each orbit, phase limit
# alpha*b/10 - alpha*T/(10 sqrt5) (up tail) or -alpha*b/10 - alpha*T/(10 sqrt5) (down tail),
# with an explicit error radius.  Usage: py bohr.py T k p q M N [B]
import sys, time
from math import isqrt, gcd, floor
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 60
S5 = mp.sqrt(5)

def fund(T):
    T = abs(T); out = set()
    for L in range(1, int(1.7*T)+2):
        Y = 5*L*L-4*T*T
        if Y < 0: continue
        X = isqrt(Y)
        if X*X != Y: continue
        for x in {X, -X}:
            if (x-L) % 2 == 0: out.add(((x-L)//2, L))
    return out
def up(a, b, Q=None):
    r = (a+b, a+2*b)
    return r if Q is None else (r[0] % Q, r[1] % Q)
def dn(a, b, Q=None):
    r = (2*a-b, b-a)
    return r if Q is None else (r[0] % Q, r[1] % Q)
PHI = (1+S5)/2; PHI2 = (1-S5)/2
def conj(a, b): return a + b*PHI2
def emb(a, b): return a + b*PHI

def shifts(T, alpha, M, B):
    """returns list of (lo, hi, r): phase interval of theta*d mod 1 (lo<=hi, real numbers,
    not reduced) and residue r = d mod M, covering all signed d in S_T^inf."""
    p, q = alpha.numerator, alpha.denominator
    th = mp.mpf(p)/q/S5
    Q = 10*q*M//gcd(q, M)
    exact = {}; tails = set(); rad = mp.mpf(0)
    for (a0, b0) in fund(T):
        for s in (1, -1):
            for step, kind in ((up, 'up'), (dn, 'dn')):
                a, b = s*a0, s*b0
                n = 0
                while True:
                    X = 2*a+b
                    if abs(X) > 10*B+abs(T)+10 and n > 3: break
                    if (X-T) % 10 == 0:
                        d = (X-T)//10
                        if d != 0 and abs(d) <= B: exact[d] = 1
                    a, b = step(a, b); n += 1
                # tail starts at (a,b): all later terms have |d| > B
                # error radius: up tail phase = alpha b/10 - alpha T/(10 s5) + alpha*beta'/(5 s5)
                if kind == 'up': small = abs(conj(a, b))
                else: small = abs(emb(a, b))
                e = abs(mp.mpf(p)/q)*small/(5*S5)
                rad = max(rad, e)
                st = (a % Q, b % Q); seen = set(); cur = st
                while cur not in seen:
                    seen.add(cur)
                    A, Bb = cur; X = (2*A+Bb) % Q
                    if (X - T) % 10 == 0:
                        dm = ((X - T) % Q)//10 % M   # d mod M  (Q multiple of 10M)
                        sg = 1 if kind == 'up' else -1
                        bq = Bb % (10*q)
                        tails.add((sg, bq, dm))
                    cur = step(A, Bb, Q)
    out = []
    for d in exact:
        ph = th*d
        out.append((ph, ph, d % M))
    c = mp.mpf(p)/q*T/(10*S5)
    for (sg, bq, dm) in tails:
        ph = sg*mp.mpf(p)*bq/(10*q) - c
        out.append((ph-rad, ph+rad, dm))
    return out, sorted(exact), len(tails), rad

def build(T, k, alpha, M, N, B, secs=50):
    from pysat.solvers import Cadical153
    sh, ex, nt, rad = shifts(T, alpha, M, B)
    V = lambda j, s, c: ((j*M+s)*k+c)+1
    cl = set()
    for (lo, hi, r) in sh:
        f1 = int(mp.floor(N*lo)); f2 = int(mp.ceil(N*hi))   # bins j+f1 .. j+f2 (conservative)
        # margin: exact points: hit bins j+floor(N ph), j+floor(N ph)+1 unless N ph integral
        for j in range(N):
            for t in range(f1, f2+1):
                j2 = (j+t) % N; s2 = r
                for s in range(M):
                    a = (j, s); b = (j2, (s+r) % M)
                    if a == b: return None, 'self-loop', len(sh)
                    if a > b: a, b = b, a
                    cl.add((a, b))
    sol = Cadical153()
    for j in range(N):
        for s in range(M):
            sol.add_clause([V(j, s, c) for c in range(k)])
    for (a, b) in cl:
        for c in range(k):
            sol.add_clause([-V(a[0], a[1], c), -V(b[0], b[1], c)])
    sol.add_clause([V(0, 0, 0)])
    import threading
    tm = threading.Timer(secs, lambda: sol.interrupt()); tm.start()
    res = sol.solve_limited(expect_interrupt=True); tm.cancel()
    g = None
    if res:
        m = sol.get_model(); g = {}
        for j in range(N):
            for s in range(M):
                g[(j, s)] = next(c for c in range(k) if m[V(j, s, c)-1] > 0)
    sol.delete()
    return res, g, (len(sh), len(ex), nt, float(rad), len(cl))

if __name__ == "__main__":
    T, k, p, q, M, N = map(int, sys.argv[1:7])
    B = int(sys.argv[7]) if len(sys.argv) > 7 else 10**15
    t0 = time.time()
    res, g, info = build(T, k, Fr(p, q), M, N, B)
    print(T, k, p, q, M, N, res, info, "%.1fs" % (time.time()-t0))
    if g and M == 1: print(''.join(str(g[(j, 0)]) for j in range(N)))
