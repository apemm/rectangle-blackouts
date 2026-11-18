"""Generate and check each row-color split of a necessary saturation formula."""
import argparse
import hashlib
import json
import subprocess
import tempfile
import time
from pathlib import Path
from saturated_slice import clauses_for


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('height', type=int)
    parser.add_argument('slice_width', type=int)
    parser.add_argument('run_width', type=int)
    parser.add_argument('--split-bits', type=int, default=3)
    parser.add_argument('--parts', type=int, nargs='+', required=True)
    parser.add_argument('--solver', type=Path, required=True)
    parser.add_argument('--checker', type=Path, required=True)
    parser.add_argument('--lean', type=Path)
    args = parser.parse_args()
    if not 0 <= args.split_bits <= args.height:
        parser.error('split-bits must be between zero and the height')
    count = 1 << args.split_bits
    if any(not 0 <= part < count for part in args.parts):
        parser.error('invalid proof part')
    pool, base, _, row, stats = clauses_for(args.height, args.slice_width, args.run_width)
    for part in args.parts:
        start = time.monotonic()
        assumptions = [[row(i) if part >> i & 1 else -row(i)] for i in range(args.split_bits)]
        cls = base + assumptions
        head = f'p cnf {pool.top} {len(cls)}\n'
        formula = (head + ''.join(' '.join(map(str,c)) + ' 0\n' for c in cls)).encode()
        with tempfile.TemporaryDirectory(prefix='blackout-saturated-part-') as work:
            work = Path(work)
            cnf, lrat, roundtrip = work/'in.cnf', work/'out.lrat', work/'roundtrip.cnf'
            cnf.write_bytes(formula)
            solver = subprocess.run([str(args.solver), '--lrat', '--binary=false', '-q', str(cnf), str(lrat)],
                                    capture_output=True, text=True)
            if solver.returncode != 20:
                raise RuntimeError(f'part {part} solver returned {solver.returncode}: {solver.stdout[-150:]}')
            checker = subprocess.run([str(args.checker), str(cnf), str(lrat)], capture_output=True, text=True)
            if checker.returncode or 'VERIFIED' not in checker.stdout or 'NOT VERIFIED' in checker.stdout:
                raise RuntimeError(f'part {part} check failed: {checker.stdout[-300:]} {checker.stderr[-150:]}')
            lean_pass = False
            if args.lean:
                source = Path(__file__).resolve().parents[2]/'jis/unsat/lean/Main.lean'
                lean = subprocess.run([str(args.lean), '--run', str(source), str(cnf), str(lrat), str(roundtrip)],
                                      capture_output=True, text=True)
                if lean.returncode or 's VERIFIED' not in lean.stdout or roundtrip.read_bytes() != formula:
                    raise RuntimeError(f'part {part} Lean check failed: {lean.stdout[-300:]} {lean.stderr[-150:]}')
                lean_pass = True
            rec = dict(height=args.height, run_width=args.run_width, slice_width=args.slice_width,
                       split_bits=args.split_bits, part=part, cnf_sha256=digest(cnf), lrat_sha256=digest(lrat),
                       lrat_bytes=lrat.stat().st_size, seconds=round(time.monotonic()-start,2),
                       lrat_check=True, lean_roundtrip=lean_pass)
            print(json.dumps(rec, sort_keys=True),flush=True)


if __name__ == '__main__':
    main()

