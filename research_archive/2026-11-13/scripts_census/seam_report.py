import re, glob, ast
from collections import defaultdict
from lstar import j1star_bad, k_shift
rows = []
for f in sorted(glob.glob('seam_*.log')):
    for ln in open(f):
        if not ln.startswith('JOB'): continue
        m = re.match(r"JOB (\d+) h (\d+) r0 (\d+) D0 (\d+) k (\d+) T\* (\d+) end (\w) ph (\d) nviol (\d+) (\{.*\}) rival\(o,kap,j\) (\[.*?\]) J1\*bad (\[.*?\]) oob (\d+)", ln)
        g = m.groups()
        rows.append(dict(job=int(g[0]), h=int(g[1]), r0=int(g[2]), D0=int(g[3]), k=int(g[4]), Ts=int(g[5]), end=g[6], ph=int(g[7]),
                         n=int(g[8]), kinds=ast.literal_eval(g[9].replace("('", "('")), rv=ast.literal_eval(g[10]), oob=int(g[12])))
rows = {r['job']: r for r in rows}
print('jobs parsed', len(rows), 'oob total', sum(r['oob'] for r in rows.values()))
def pred_bad_phases(end, pairs):
    bad = set()
    for o, kap in pairs:
        for ph in range(4):
            rr = range(1, kap + 1) if end == 'R' else range(0, kap)
            if any(((ph - r) if end == 'R' else (ph + r)) % 4 == o for r in rr):
                bad.add(ph)
    return bad
mism = []; other = []; summary = defaultdict(dict)
for r in rows.values():
    nonriv = {k: v for k, v in r['kinds'].items() if k[0] != 'V5' or k[2] != 'Fg'}
    if nonriv: other.append((r['job'], nonriv))
    obs_pairs = sorted(set((int(o), kap) for o, kap, j in r['rv']))
    board_k = k_shift(r['h'], r['r0'], r['D0'])
    if r['k'] == board_k:
        pairs = j1star_bad(r['h'], r['r0'], r['D0']) if r['k'] == 0 else []
        badp = pred_bad_phases(r['end'], pairs)
        obs_bad = r['n'] > 0
        if (r['ph'] in badp) != obs_bad or (obs_bad and obs_pairs != sorted(pairs)):
            mism.append((r['job'], r['h'], r['r0'], r['D0'], r['k'], r['end'], r['ph'], obs_pairs, pairs))
    key = (r['h'], r['r0'], r['D0'], r['k'], r['end'])
    summary[key][r['ph']] = (r['n'], tuple(sorted(set(r['rv']))))
print('non-rival-pair seam violations:', other)
print('mismatches against Table J1* + (Phi):', mism)
for key in sorted(summary):
    d = summary[key]
    print(key, {ph: d[ph] for ph in sorted(d)})
