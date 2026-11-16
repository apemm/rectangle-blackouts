from collections import Counter
from blib import *
h = 112; prof = (3, 9, 110, 2)
rows = [r for r in range(1, h + 1) if row_ok(h, prof, r)]
labs = [(a, b) for a in rows if a % 2 for b in rows if b % 2 == 0]
c = Counter(b - a for a, b in labs)
print(sorted(c.items(), key=lambda t: -t[1])[:20])
