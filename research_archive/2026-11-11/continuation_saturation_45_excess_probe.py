"""Locate whether the h+1 obstruction already follows from 45-degree corners."""
from pathlib import Path
import json
from continuation_saturation_corner_probe import run

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    for h in (6, 7, 8):
        result = run(h, part=False, width=h + 1, shape_mode='45', seconds=10)
        print(json.dumps(result), flush=True)
        (here / f'continuation_saturation_45_excess_h{h}.json').write_text(
            json.dumps(result, indent=2) + '\n', encoding='utf-8')
