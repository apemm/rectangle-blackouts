"""Bounded all-double square probes with exactly two black cells per row."""
from pathlib import Path
import json
import sys
from probe_all_double_squares import run

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    for h in map(int, sys.argv[1:] or ['8', '9']):
        result = run(h, seconds=20, min_row_degree=2)
        print(json.dumps(result), flush=True)
        (here / f'all_double_two_regular_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
