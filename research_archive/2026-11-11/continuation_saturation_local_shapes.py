"""Small shape-restricted relaxations to locate the saturated obstruction."""
from pathlib import Path
import json
from continuation_saturation_corner_probe import run

if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    for mode in ('unit', '45'):
        for h in (5, 6, 7, 8):
            result = run(h, seconds=10, shape_mode=mode)
            print(json.dumps({k: v for k, v in result.items() if k != 'first_collisions'}), flush=True)
            (here / f'continuation_saturation_{mode}_h{h}.json').write_text(
                json.dumps(result, indent=2) + '\n', encoding='utf-8')
