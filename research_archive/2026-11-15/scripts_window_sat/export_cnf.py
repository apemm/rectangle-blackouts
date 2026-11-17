"""Write the CNF of win.py for given (h, k) as DIMACS. Usage: python export_cnf.py WINDIR OUTDIR h k [h k ...]"""
import sys, hashlib, json, os
sys.path.insert(0, sys.argv[1])
import win
out = sys.argv[2]; a = list(map(int, sys.argv[3:]))
for h, k in zip(a[::2], a[1::2]):
    vp, cl, P, S, nr = win.build(h, k)
    nv = max(abs(l) for c in cl for l in c)
    body = 'p cnf %d %d\n' % (nv, len(cl)) + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl)
    name = 'window_h%d_k%d.cnf' % (h, k)
    open(os.path.join(out, name), 'w', newline='\n').write(body)
    print(json.dumps(dict(name=name, h=h, k=k, vars=nv, clauses=len(cl), rectangles=nr,
                          sha256=hashlib.sha256(body.encode()).hexdigest())), flush=True)
