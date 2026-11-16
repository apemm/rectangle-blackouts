"""Exact first moment of fatal cross-block (E;O,E) configurations under a uniformly random
block order (stride 4, greedy P-free constant-offset classes, block c at 4(i+Pc)).
fatal := V,P slots in class k0 (slots i0, i0+t1), Q,R slots in class k' (iQ, iQ+t1), R row in grid.
Usage: py check2_moment.py h lam [mode]   mode = greedy | full (one class per diagonal)"""
import sys, math, time
from collections import defaultdict
from common import *

h = int(sys.argv[1]); lam = float(sys.argv[2]); mode = sys.argv[3] if len(sys.argv) > 3 else "greedy"
A, K = params(h)
P = next_prime(int(lam*h)+1)
t0 = time.time()
if mode == "full":
    cls = [(s, diag_slots(h, s)) for s in range(-(A-1), K)]
    cls = [c for c in cls if c[1]]
else:
    cls = all_classes(h)
C = len(cls)
FULL = (1 << A) - 1
def bits(sl):
    b = 0
    for i in sl: b |= 1 << i
    return b
def sh(b, t):  # bit i set iff i+t in b
    return (b >> t) if t >= 0 else ((b << (-t)) & FULL)
bys = defaultdict(list)
for (s, sl) in cls: bys[s].append(bits(sl))
def rng(lo, hi):  # mask of i in [lo,hi)
    lo = max(lo, 0); hi = min(hi, A)
    if hi <= lo: return 0
    return ((1 << hi) - 1) ^ ((1 << lo) - 1)
t1max = int(h*K/(8*(P-h) - 10*K)) + 1
E_by_s = defaultdict(float); lab_by_s = defaultdict(int)
Etot = 0.0; nconf_pairs = 0
for (s0, sl0) in cls:
    T0 = 2*s0+1; B0 = bits(sl0); lab_by_s[s0] += len(sl0)
    for t1 in list(range(1, t1max+1)) + list(range(-t1max, 0)):
        Pm = B0 & sh(B0, t1)
        if not Pm: continue
        g = math.gcd(abs(t1), abs(T0)); t1p = t1//g; ep = (10*t1 - T0)//g
        nmax = (K-1)//(8*abs(t1p))
        nmin = max(1, -(-(P-h)//abs(ep)))
        for n in list(range(nmin, nmax+1)) + list(range(-nmax, -nmin+1)):
            N = ep*n; c2 = 8*t1p*n
            q = (N + P//2)//P; ds = N - P*q; dc = -q
            if dc == 0 or abs(dc) > C-1: continue
            s1 = s0 + ds
            if s1 not in bys: continue
            u = c2 - ds
            Rm = rng(-t1-c2, A-t1-c2)
            w = (C-abs(dc))/(C*(C-1))
            for B1 in bys[s1]:
                cnt = bin(Pm & sh(B1, u) & sh(B1, u+t1) & Rm).count("1")
                if cnt:
                    E_by_s[s0] += w*cnt; Etot += w*cnt; nconf_pairs += 1
labels = sum(len(sl) for _, sl in cls)
print(f"h={h} P={P} lam={P/h:.2f} mode={mode} classes={C} labels={labels} t1max={t1max} time={time.time()-t0:.1f}s")
print(f"E[fatal] = {Etot:.3f}   per label = {Etot/labels:.3e}   E/h = {Etot/h:.3f}  E/(h log^2 h)={Etot/(h*math.log(h)**2):.4f}")
# split by arithmetic of T0
def divisors(n):
    n = abs(n); out = []
    for d in range(1, math.isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n: out.append(n//d)
    return out
def phi(n):
    r = n; m = n; p = 2
    while p*p <= m:
        if m % p == 0:
            while m % p == 0: m //= p
            r -= r//p
        p += 1
    if m > 1: r -= r//m
    return r
c16 = 8*P/K   # 16*lam with K=h/2
def Phi(T):
    return sum(phi(d)/d*max(0.0, math.log(d/c16)-1) for d in divisors(T) if d > c16)
grp = defaultdict(lambda: [0.0, 0, 0.0])
for s in lab_by_s:
    T = 2*s+1; key = len(divisors(T))
    key = "tau<=2" if key <= 2 else ("tau<=4" if key <= 4 else ("tau<=8" if key <= 8 else "tau>8"))
    grp[key][0] += E_by_s[s]; grp[key][1] += lab_by_s[s]; grp[key][2] += Phi(T)*lab_by_s[s]
for k in sorted(grp):
    e, l, ph = grp[k]
    print(f"  {k:7s}: labels={l:8d}  E={e:9.3f}  E/label={e/l:.3e}  mean Phi={ph/l:.3f}  ratio E/(labels*Phi)={(e/ph if ph else float('nan')):.4f}")
tot_phi = sum(Phi(2*s+1)*lab_by_s[s] for s in lab_by_s)
print(f"  overall E/(sum_labels Phi) = {Etot/tot_phi if tot_phi else float('nan'):.4f}")
