"""Compare one-label violations per label: stride-4 census_class log vs stride-12 log.
usage: py cmp_s4.py s4log s12log"""
import sys, re
from collections import Counter
def load(fn, key12):
    c = Counter()
    for ln in open(fn):
        if not ln.startswith('VIOL'): continue
        kind = re.search(r'kind (\w+)', ln).group(1); fam = re.search(r'family (.*?) comp', ln).group(1)
        labs = eval(re.search(r'labels (\[.*?\])', ln).group(1))
        if len(labs) == 1: c[(labs[0], kind, fam.strip())] += 1
    return c
a = load(sys.argv[1], 0); b = load(sys.argv[2], 1)
la = set(k[0] for k in a); lb = set(k[0] for k in b)
common = la & lb
print('labels with one-label violations: stride4', len(la), 'stride12', len(lb), 'common', len(common))
da = Counter({k: v for k, v in a.items() if k[0] in lb}); db = Counter({k: v for k, v in b.items() if k[0] in la})
print('per-label (kind,family) multiset equal on common labels:', da == db)
print('only stride4 labels:', sorted(la - lb)[:20]); print('only stride12 labels:', sorted(lb - la)[:20])
