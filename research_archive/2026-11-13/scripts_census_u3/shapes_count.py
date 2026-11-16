"""Count homogeneous 2L2F shapes at stride s with depths Y1, Y2 in [1, H], split by sign of t, and apply
the Fo type congruence (Y1 = 8(o + c), c in {1, 3}, mod 64) and Fe (only Y1 odd; congruence depends on T).
delta range: |delta| <= max(4 s |t|, sqrt(20 |t| H)) + 16 (proved: outside it |Y1| >= delta^2/(20|t|) > H).
usage: py shapes_count.py s H"""
import sys
from math import isqrt
s = int(sys.argv[1]); H = int(sys.argv[2])
cnt = {'t>0': 0, 't<0': 0}; fo_ok = {'t>0': 0, 't<0': 0}; fe = {'t>0': 0, 't<0': 0}; mind = {}
for t in range(-(H // 2) // 32 * 32, 211, 32):
    if t == 0: continue
    R = max(4 * s * abs(t), isqrt(20 * abs(t) * H) + 1) + 16
    R -= R % 16
    for delta in range(-R, R + 1, 16):
        den = 4 * (delta - s * t)
        if den == 0: continue
        num = delta * delta + 4 * t * t
        if num % den: continue
        a = num // den
        if a % 4: continue
        if (a * (delta - 2 * s * t)) % (2 * t): continue
        Y1 = a * (delta - 2 * s * t) // (2 * t); Y2 = Y1 - 2 * t
        if not (1 <= Y1 <= H and 1 <= Y2 <= H): continue
        k = 't>0' if t > 0 else 't<0'; cnt[k] += 1
        o = (a // 4) % 4
        if Y1 % 2 == 0:
            if Y1 % 8 == 0 and (Y1 // 8 - o) % 8 in (1, 3): fo_ok[k] += 1
        else:
            fe[k] += 1
        mind[k] = min(mind.get(k, 10 ** 9), max(Y1, Y2))
print('s', s, 'H', H, 'shapes', cnt, 'Fo passing type congruence', fo_ok, 'Fe (T-dependent congruence)', fe, 'least max depth', mind)
