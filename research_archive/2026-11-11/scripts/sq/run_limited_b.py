"""Run eq45b.py for given widths, one at a time, with a hard wall-clock limit per width."""
import subprocess, sys, time
h, limit, widths = sys.argv[1], float(sys.argv[2]), sys.argv[3:]
for m in widths:
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, 'eq45b.py', h, m], capture_output=True, text=True, timeout=limit)
        print(r.stdout.strip(), flush=True)
        if r.returncode != 0: print('ERROR', r.stderr[-300:], flush=True)
    except subprocess.TimeoutExpired:
        print(f"diag+sym h={h} m={m}: TIMEOUT after {time.time()-t0:.0f}s (hard limit)", flush=True)
