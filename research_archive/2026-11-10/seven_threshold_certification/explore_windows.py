"""Exploration only: for each reflection class of balanced partitions at
height 7 and each window length k, find the largest number of two-cell
columns in a valid window board (see certlib.encode_window).

The output window_targets.json lists, for each class and k, the value d such
that "at least d + 1" came back UNSAT here. Nothing in the certification
relies on this file: each bound that is used later is run again by run_one.py
with two solvers and proof logging, and only those runs are cited.
"""
import json
import sys
import time

from pysat.solvers import Solver

from certlib import (balanced_partitions, encode_window, rectangles_by_sides,
                     reflection_classes)

H = 7
KS = [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8, 9, 10, 11]


def main():
    parts = balanced_partitions(H)
    out = {}
    for part in reflection_classes(H):
        pi = parts.index(part)
        out[pi] = {}
        prev = 0
        for k in KS:
            rects = rectangles_by_sides(H, k)
            best = None
            d = min(k, 12, prev + (k - (KS[KS.index(k) - 1] if KS.index(k) else 0)))
            t0 = time.time()
            while d >= 1:
                cnf = encode_window(H, k, part, rects, d)
                with Solver(name='cadical195', bootstrap_with=cnf.clauses) as s:
                    if s.solve():
                        best = d
                        break
                d -= 1
            out[pi][k] = best
            prev = best
            print(pi, part, k, best, round(time.time() - t0, 1), flush=True)
        with open('window_targets.json', 'w') as fh:
            json.dump(out, fh, indent=1)


if __name__ == '__main__':
    main()
