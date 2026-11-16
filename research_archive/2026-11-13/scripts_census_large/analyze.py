"""Map census violations to verdicts of the merged table of consolidated_board_v2 section 3.
usage: py analyze.py logfile [relocout]
C (counted, relocated): D4 (label on the diagonal), D10, D11, B6 (R_IV; R-e at these heights), D12, D13.
Everything else found in a single-class window is a cell the table marks E: it is FLAGGED.
B6 instances are checked against the R_IV edge definition (sea_census_rigid B4)."""
import sys, re, ast
from math import gcd
from collections import Counter, defaultdict

C_FAMS = {'D10': 'D10', 'D11 (M2c label+filler)': 'D11', 'D4 (Thm 1(6))': 'D4',
          'B6 (in-class oo M2c, R_IV)': 'B6', 'D12 (homog., d>0)': 'D12', 'D13 (homog., d<0)': 'D13'}

def riv_pairs(bemax=200):
    out = {}
    for be in range(3, bemax, 2):
        for al in range(1, be, 2):
            if gcd(al, be) != 1:
                continue
            F = 4 * (al - 2 * be) ** 2 + be ** 2
            g = gcd(F, be - al)
            q = al * F // g; p = (al * F + 4 * (be - al) * be * be) // g
            v2 = ((be - al) & -(be - al)).bit_length() - 1
            out[(al, be)] = (q, p, v2)
    return out
RIV = riv_pairs()

def riv_match(u1, u2):
    a, b = sorted((u1, u2))
    hits = []
    for lam, (q, p, v2) in RIV.items():
        if a * p == b * q and a % q == 0 and (a // q) % 2 == 1:
            hits.append((lam, q, p, v2, a // q))
    return hits

log = sys.argv[1]
hdr = None; rows = []
for ln in open(log):
    if ln.startswith('HDR'):
        hdr = ln
        m = re.search(r"\{'r0': (\d+).*?'Ts': (\d+)", ln); r0 = int(m.group(1)); Ts = int(m.group(2))
    if not ln.startswith('VIOL'):
        continue
    sub = int(ln.split()[2]); size = int(re.search(r'size (\d+)', ln).group(1))
    kind = re.search(r'kind (\w+)', ln).group(1)
    fam = re.search(r'family (.*?) comp ', ln).group(1)
    comp = re.search(r' comp (.*?) labels ', ln).group(1)
    labs = ast.literal_eval(re.search(r' labels (\[.*?\]) oob', ln).group(1))
    oob = int(re.search(r' oob (\d+)', ln).group(1))
    data = ast.literal_eval(re.search(r' data (\(.*\))', ln).group(1))
    rows.append((sub, size, kind, fam, comp, labs, oob, data))
print(hdr.strip()[:330] if hdr else 'no header')
cnt = Counter(); flags = []; reloc = set(); oobmax = 0; riv_ok = riv_bad = 0; depth = defaultdict(list)
multi = Counter()
for (sub, size, kind, fam, comp, labs, oob, data) in rows:
    oobmax = max(oobmax, oob)
    v = C_FAMS.get(fam)
    key = (kind, fam, 'C' if v else 'FLAG', len(labs))
    cnt[key] += 1
    if size >= 2:
        multi[(kind, fam, len(labs))] += 1
    if not v:
        flags.append((sub, size, kind, fam, comp, labs, data))
        continue
    for L in labs:
        reloc.add(L)
        depth[v].append(Ts - max(2 * L[0] + 1, 2 * L[1] + 2))
    if v == 'B6':
        A, B, C_, D, p, q = data
        odd = [z for z in (A, B, C_, D) if z[1] % 2 == 1 and z[1] != r0]
        us = sorted(set((z[1] - r0) // 2 for z in odd))
        if len(us) == 2 and riv_match(*us):
            riv_ok += 1
        else:
            riv_bad += 1; print('B6 NOT AN R_IV EDGE', us, data)
print('violations', len(rows), 'max oob', oobmax)
for k, v in sorted(cnt.items()):
    print('  ', k, v)
print('violations in windows with >= 2 kept labels (kind, family, #labels):', dict(multi))
print('two-or-more-label violations:', sum(v for k, v in cnt.items() if k[3] >= 2))
for f, d in depth.items():
    print('  depth T* - (deepest endpoint row) of %s labels: min %d max %d' % (f, min(d), max(d)))
print('B6 checked against R_IV: ok', riv_ok, 'bad', riv_bad)
print('FLAGS', len(flags))
for fl in flags[:30]:
    print('  FLAG', fl)
print('labels to relocate', len(reloc))
if len(sys.argv) > 2:
    a, b = map(int, re.search(r'type \((\d+), (\d+)\)', hdr).groups())
    with open(sys.argv[2], 'a') as f:
        for (i, j) in sorted(reloc):
            f.write('%d %d %d %d\n' % (a, b, i, j))
