"""Run eq45.py one width at a time with a hard wall-clock limit per width."""
import subprocess, sys, time
family, h, m0, m1, limit = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
for m in range(m0, m1 + 1):
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, 'eq45.py', family, h, str(m), str(m), '1000000'],
                           capture_output=True, text=True, timeout=limit)
        print(r.stdout.strip(), flush=True)
        if r.returncode != 0: print('ERROR', r.stderr[-300:], flush=True)
    except subprocess.TimeoutExpired:
        print(f"{family} h={h} m={m}: TIMEOUT after {time.time()-t0:.0f}s (hard limit)", flush=True)
