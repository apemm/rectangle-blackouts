import re, glob, sys
from collections import defaultdict
for pat in sys.argv[1:]:
    stats = defaultdict(lambda: [0, -10**9, 10**9, set()])  # count, max dist below lowest filler, min, labels
    kept = 0; files = glob.glob(pat)
    for f in files:
        Ts = None; X0 = None
        for ln in open(f):
            if ln.startswith('HDR'):
                Ts = int(re.search(r"'Ts': (\d+)", ln).group(1)); kept += int(re.search(r'kept labels (\d+)', ln).group(1))
            if not ln.startswith('VIOL'): continue
            fam = re.search(r'family (.*?) comp', ln).group(1); comp = re.search(r'comp (\S+)', ln).group(1)
            L = eval(re.search(r'labels (\[.*?\])', ln).group(1)); data = eval(re.search(r'data (\(.*\))', ln).group(1))
            pts = []
            def flat(z):
                if isinstance(z, tuple) and len(z) == 2 and all(isinstance(u, int) for u in z): pts.append(z)
                elif isinstance(z, (tuple, list)):
                    for u in z: flat(u)
            flat(data if 'V5' not in ln else [(data[0], data[1]), (data[2], data[3])])
            labrows = set(r for a, b in L for r in (2*a+1, 2*b+2))
            ys = [y for (x, y) in pts if y in labrows]
            if not ys: continue
            dist = (Ts - 24) - min(ys)   # rows of the deepest label point used, below the lowest filler row
            key = fam + ' ' + comp.split('|')[0]
            s = stats[key]; s[0] += 1; s[1] = max(s[1], dist); s[2] = min(s[2], dist)
            for lab in L: s[3].add((f, lab))
    print(pat, 'files', len(files), 'kept labels', kept)
    for k, s in sorted(stats.items(), key=lambda z: -z[1][0]):
        print(f'   {s[0]:6d}  {k:40s} label point used: rows below lowest filler row in [{s[2]}, {s[1]}]   distinct labels hit {len(s[3])}')
