"""Leftover M=3 two-gap classes: a even, alpha = v2(a); s=1 with v2(b)=alpha, or s=2 with v2(b+1)=alpha;
and not covered by the 3-adic rule. Search the least period P <= Pmax of a periodic solution."""
import sys, time
from collections import Counter
src = open("two_gap_m3.py").read().split('if __name__ == "__main__":')[0]
exec(src)
amax, bmax, Pmax = map(int, sys.argv[1:4]); t0 = time.time(); per = Counter(); none = []
for a in range(2, amax + 1, 2):
    al = v(2, a)
    for b in range(1, bmax + 1):
        for s in (1, 2):
            if s == 1 and v(2, b) != al: continue
            if s == 2 and v(2, b + 1) != al: continue
            if rule3(a, b, s) is not None: continue
            res = periodic(a, b, s, Pmax)
            if res: per[res[0]] += 1
            else: none.append((3 * a, 3 * b + s))
print("least periods found:", sorted(per.items()), "unsolved (q0,q1) with P<=%d:" % Pmax, none[:20], len(none),
      "time %.1fs" % (time.time() - t0))
