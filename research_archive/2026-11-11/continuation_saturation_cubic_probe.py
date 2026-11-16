"""One small cubic, all-double, corner-free relaxation."""
from pathlib import Path
import json
from continuation_saturation_corner_probe import run

if __name__ == '__main__':
    result = run(8, width=12, min_row_degree=3, seconds=20)
    print(json.dumps(result), flush=True)
    Path(__file__).with_name('continuation_saturation_cubic_h8.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
