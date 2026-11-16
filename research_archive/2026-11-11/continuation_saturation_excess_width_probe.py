"""Test the conjectured m <= h bound for unrestricted corner-free doubles."""
from pathlib import Path
import json
import sys
from continuation_saturation_corner_probe import run

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    for h in map(int, sys.argv[1:] or ['6', '7', '8']):
        result = run(h, part=False, width=h + 1, seconds=20)
        print(json.dumps(result), flush=True)
        (here / f'continuation_saturation_excess_width_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
