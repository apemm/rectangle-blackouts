"""Run one SAT instance and append one JSON line to a results file.

Usage:
  py run_one.py OUT.jsonl direct H M K SOLVER
  py run_one.py OUT.jsonl struct H M PART SOLVER [caps=FILE] [nobreak] [proof=DIR] [fix=WORD]
  py run_one.py OUT.jsonl window H K PART SOLVER D [proof=DIR]

PART is an index into certlib.balanced_partitions(H).
direct: valid black set with at least K cells, no structure assumed.
struct: equality board for the partition. caps=FILE adds the proved window
        bounds stored in FILE (see window_caps.json) and, unless nobreak is
        given, the column-reflection symmetry break.
        fix=WORD fixes the board to the given column word (encoder acceptance test).
window: valid window board of width K with at least D two-cell columns.

A SAT answer is checked by brute force with the diagonal rectangle generator,
which the encoder does not use. With proof=DIR an UNSAT answer writes the CNF
and the DRAT proof, records size and SHA-256, and deletes the files when the proof exceeds 2 MB.
"""
import hashlib
import json
import os
import sys
import time

from certlib import (balanced_partitions, black_to_word, encode_direct,
                     encode_structured, encode_structured_caps, encode_window,
                     find_collision, is_equality_board, rectangles_by_diagonals,
                     rectangles_by_sides, word_to_black, write_dimacs)

LIMIT = 2 * 1024 * 1024


def sha(path):
    hsh = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            hsh.update(chunk)
    return hsh.hexdigest()


def main():
    from pysat.solvers import Solver
    out, kind, h, m = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    opts = dict(a.split('=', 1) for a in sys.argv[5:] if '=' in a)
    pos = [a for a in sys.argv[5:] if '=' not in a and a != 'nobreak']
    rec = {'kind': kind, 'h': h, 'm': m}
    began = time.time()
    rects = rectangles_by_sides(h, m)
    assumptions = []
    if kind == 'direct':
        k, solver = int(pos[0]), pos[1]
        rec.update(k=k)
        cnf = encode_direct(h, m, k, rects)
        tag = f'direct_h{h}_m{m}_k{k}'
    else:
        pi, solver = int(pos[0]), pos[1]
        part = balanced_partitions(h)[pi]
        rec.update(part_index=pi, part=[[r + 1 for r in side] for side in part])
        if kind == 'struct':
            if 'caps' in opts:
                table = json.load(open(opts['caps']))
                caps = {int(k): v for k, v in table['caps'][str(h)][str(pi)].items()}
                brk = 'nobreak' not in sys.argv
                cnf = encode_structured_caps(h, m, part, rects, caps, brk)
                rec.update(caps=caps, reflection_break=brk)
            else:
                cnf = encode_structured(h, m, part, rects)
            if 'fix' in opts:
                black = word_to_black(opts['fix'], m)
                assumptions = [p + 1 if p in black else -(p + 1) for p in range(h * m)]
                rec.update(fixed_word=opts['fix'])
            tag = f'struct_h{h}_m{m}_p{pi}'
        else:
            d = int(pos[2])
            rec.update(doubles_at_least=d)
            cnf = encode_window(h, m, part, rects, d)
            tag = f'window_h{h}_k{m}_p{pi}_d{d}'
    rec.update(solver=solver, vars=cnf.nv, clauses=len(cnf.clauses),
               rectangles=len(rects), encode_seconds=round(time.time() - began, 3))
    proof_dir = opts.get('proof')
    t0 = time.time()
    with Solver(name=solver, bootstrap_with=cnf.clauses, with_proof=bool(proof_dir)) as s:
        sat = s.solve(assumptions=assumptions)
        rec.update(status='SAT' if sat else 'UNSAT', solve_seconds=round(time.time() - t0, 3))
        try:
            rec['stats'] = s.accum_stats()
        except Exception:
            pass
        if sat:
            model = set(l for l in s.get_model() if 0 < l <= h * m)
            black = frozenset(l - 1 for l in model)
            check = rectangles_by_diagonals(h, m)
            assert find_collision(check, black) is None, 'model fails brute-force check'
            rec.update(black_cells=len(black), word=black_to_word(black, h, m),
                       brute_force_valid=True, presentations=len(check))
            if kind == 'struct':
                assert is_equality_board(black, h, m, part) and len(black) == m + len(part[0]) * len(part[1])
            if kind == 'direct':
                assert len(black) >= rec['k']
                rec['equality_structure'] = is_equality_board(black, h, m)
        elif proof_dir:
            assert not assumptions
            proof = s.get_proof() or []
            os.makedirs(proof_dir, exist_ok=True)
            cnf_path = os.path.join(proof_dir, f'{tag}_{solver}.cnf')
            drat_path = os.path.join(proof_dir, f'{tag}_{solver}.drat')
            write_dimacs(cnf, cnf_path)
            with open(drat_path, 'w', newline='\n') as fh:
                for line in proof:
                    fh.write(line + '\n')
            info = {'lines': len(proof)}
            for name, path in (('cnf', cnf_path), ('drat', drat_path)):
                size = os.path.getsize(path)
                info[name] = {'file': os.path.basename(path), 'bytes': size,
                              'sha256': sha(path), 'kept': size <= LIMIT}
            if not info['drat']['kept']:
                os.remove(drat_path)
                os.remove(cnf_path)
                info['cnf']['kept'] = False
            rec['proof'] = info
    with open(out, 'a') as fh:
        fh.write(json.dumps(rec) + '\n')
    print(json.dumps({k: v for k, v in rec.items() if k not in ('stats', 'proof')}), flush=True)


if __name__ == '__main__':
    main()
