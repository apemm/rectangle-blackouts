"""Bounded fixed-parity all-double square probes; no saturation constraint."""
from pathlib import Path
import json
import sys
from probe_all_double_squares import run

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    for h in map(int, sys.argv[1:] or ['7', '8']):
        result = run(h, seconds=30, part=set(range(1, h + 1, 2)))
        print(json.dumps(result), flush=True)
        (here / f'parity_all_double_square_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
