"""Vectorized version of onelabel_thick.py (same families, numpy over lam; hits re-checked by mixed_ok)."""
import sys, numpy as np
from math import gcd
from lad import eta_array
from onelabel_thick_core import mixed_ok
import numpy as _n
Ep = 0; E = _n.array(eval(sys.argv[1]), dtype=_n.int64); P = len(E); LM = int(sys.argv[2])
vals = sorted(set(E.tolist()))
fams = 0; hitfams = []
for eA in vals:
  for eB in vals:
    e = eB - eA
    if e == 0: continue
    for eD in vals:
      rho = 2*eD - eA - eB; cs = eD - eA - eB
      r2 = 4*e*e - 4*rho*rho
      if r2 <= 0: continue
      k0 = int(round(r2**0.5))
      if k0*k0 != r2: continue
      for k in (k0, -k0):
        for sg in (1, -1):
          fams += 1
          # integer arithmetic: multiply by M = |k*rho| (or k for rho=0)
          lam = np.arange(4000, 4000 + 2*P*abs(k)*4, 2, dtype=np.int64)
          Gn = -4*e*(lam + cs)
          okG = Gn % k == 0
          G = Gn // k
          if rho == 0:
              wx = np.full(lam.shape, sg*2*e, dtype=np.int64); okw = np.ones(lam.shape, bool)
          else:
              num = 4*rho*rho*lam + 4*e*e*cs + eD*k*k      # wx = sg*num/(k*rho)
              den = k*rho
              okw = num % den == 0
              wx = sg*(num // den)
          t = wx - k - G
          ok = okG & okw & (t % 2 == 0)
          idx = np.nonzero(ok)[0]
          hits = 0; ex = None
          for XL in range(0, P, LM):
              XD = XL + wx[idx]; XA = XL + t[idx]//2; XB = XA + G[idx]
              m = (E[XD % P] == eD) & (E[XA % P] == eA) & (E[XB % P] == eB)
              for q in np.nonzero(m)[0]:
                  i = idx[q]
                  A = (int(XA[q]), eA); B = (int(XB[q]), eB); C = (XL, int(lam[i])); D = (int(XD[q]), eD)
                  if mixed_ok(A, B, C, D):
                      hits += 1
                      if ex is None: ex = (A, B, C, D)
          if hits: hitfams.append((eA, eB, eD, k, sg, hits, ex))
print("E'=%d: candidate thick families %d, families with hits %d" % (Ep, fams, len(hitfams)))
for f in hitfams[:40]: print('  ', f)
