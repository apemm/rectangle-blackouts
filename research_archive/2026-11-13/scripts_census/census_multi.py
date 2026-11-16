"""Run census_class for many types in one process (amortizes imports and the divisor table).
usage: py census_multi.py h mode listfile start ; writes cls_<mode>_<h>_<iota>_<sigma>_0.log per type"""
import sys, time, io, contextlib, runpy
h, mode, lf, st = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
todo = [ln.strip() for ln in open(lf) if ln.strip()]
t0 = time.time(); i = st
while i < len(todo) and time.time() - t0 < 42:
    a, b = todo[i].split(':')
    buf = io.StringIO()
    sys.argv = ['census_class.py', h, a, b, mode, '0']
    with contextlib.redirect_stdout(buf):
        runpy.run_path('census_class.py', run_name='__main__')
    out = buf.getvalue()
    nx = [ln for ln in out.splitlines() if ln.startswith('NEXT')][0].split()
    assert nx[1] == nx[2], ('type not finished', todo[i])
    open(f'cls_{mode}_{h}_{a}_{b}_0.log', 'w').write(out)
    i += 1
print('NEXT', i, len(todo), 'time %.1f' % (time.time() - t0))
