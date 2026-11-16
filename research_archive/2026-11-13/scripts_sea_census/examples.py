import sys
from collections import Counter
from board import build
from census import run
from driver import classify, LET
h = int(sys.argv[1]); p = int(sys.argv[2]); nu = int(sys.argv[3]); iota = int(sys.argv[4]); mu = int(sys.argv[5])
pat = sys.argv[6]
kind, blk, info, labels, blocks = build(h, iota, mu, 0, p, nu)
viol, st = run(kind, h, info['Xmax'])
H1 = h + 1
pt = lambda i: (i // H1 + info['x0'], i % H1)
fam, ex = classify(viol, kind, blk, h)
shown = Counter()
for v in viol:
    f, e = classify([v], kind, blk, h)
    name = list(f)[0]
    if pat in name and shown[name] < int(sys.argv[7] if len(sys.argv) > 7 else 3):
        shown[name] += 1
        def lab(i):
            x, y = i // H1, i % H1
            return '%s%s' % (LET[int(kind[x, y])], pt(i))
        if v[0] == 'T2':
            print(name, [(lab(r[0]), lab(r[1]), 'side' if r[2] == 0 else 'diag') for r in v[1]], 'white', pt(v[2][0]), pt(v[2][1]))
        elif v[0] == 'A2':
            print(name, lab(v[1][0]), lab(v[1][1]), 'white', pt(v[2][0]), pt(v[2][1]))
        elif v[0] == 'V2':
            print(name, [lab(i) for i in v[1]], 'W', pt(v[2]))
        elif v[0] == 'V3':
            print(name, [[lab(i) for i in r] for r in v[1]], 'W', pt(v[2]))
        else:
            print(name, [lab(i) for i in v[1]])
print(info)
