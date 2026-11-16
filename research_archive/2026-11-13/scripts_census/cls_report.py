import re, glob, sys
from collections import Counter, defaultdict
pat = sys.argv[1]
fam = Counter(); comp = Counter(); depth = defaultdict(list); ex = defaultdict(list); oobs = 0; ntypes = set()
rowsof = defaultdict(list)
for f in sorted(glob.glob(pat)):
    for ln in open(f):
        if ln.startswith('HDR'):
            ntypes.add(f.split('_')[3:5].__str__())
        if not ln.startswith('VIOL'): continue
        m = re.match(r"VIOL sub (\d+) T (-?\d+) kind (\w+) family (.*?) comp (\S+) labels (\[.*?\]) depth (\S+) all_removed_by_exact_rules (\w+) oob (\d+) data (.*)", ln)
        sub, T, kind, f_, c, L, d, nb, oob, data = m.groups()
        oobs += int(oob)
        key = (kind, f_)
        fam[key] += 1; comp[(kind, f_, c)] += 1
        L = eval(L)
        depth[key].append(int(d) if d != 'None' else None)
        rowsof[key] += [(2*a+1, 2*b+2) for a, b in L]
        if len(ex[(kind, f_, c)]) < 2: ex[(kind, f_, c)].append((f.split('_')[2:5], T, L, d, data[:160]))
print('files', len(glob.glob(pat)), 'oob', oobs)
for k, v in sorted(fam.items(), key=lambda z: -z[1]):
    ds = [x for x in depth[k] if x is not None]
    mo = min(r[0] for r in rowsof[k]) if rowsof[k] else None
    print(f'{v:6d} {k[0]} {k[1]:38s} depth range [{min(ds) if ds else None}, {max(ds) if ds else None}]  min odd label row {mo}  max odd row {max(r[0] for r in rowsof[k]) if rowsof[k] else None}')
print('--- by composition')
for k, v in sorted(comp.items(), key=lambda z: (z[0][1], -z[1])):
    print(f'{v:6d} {k}  e.g. {ex[k][0]}')
