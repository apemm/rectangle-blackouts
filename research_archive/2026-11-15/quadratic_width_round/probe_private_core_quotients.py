from pathlib import Path
import json
from check_all_offset_private_tiles import solve

folder = Path(__file__).resolve().parent
data = json.loads((folder / 'private_tile_gain_cores_side16.json').read_text())
results = []
for item in data['small_final_cores']:
    if item['offset'] not in (1732, -1733, -1739):
        continue
    found = []
    tested = 0
    for kind in ('residue', 'bands'):
        for a in range(1, 9):
            for b in range(1, 9):
                if kind == 'residue':
                    keys = [(i % a, j % b) for i, j in item['cells']]
                else:
                    keys = [(i // a, j // b) for i, j in item['cells']]
                classes = sorted(set(keys))
                if len(classes) > 16:
                    continue
                number = {key: ix for ix, key in enumerate(classes)}
                events = set()
                impossible = False
                for r, s, gains in item['edges']:
                    u, v = number[keys[r]], number[keys[s]]
                    for gain in gains:
                        if u == v:
                            if gain == 0:
                                impossible = True
                        elif u < v:
                            events.add((u, v, gain))
                        else:
                            events.add((v, u, (-gain) % 3))
                tested += 1
                if impossible:
                    continue
                sol, nodes = solve(len(classes), events, 3, True)
                if sol is not None:
                    assignment = [sol[number[key]] for key in keys]
                    assert all((assignment[s] - assignment[r]) % 3 not in gains
                               for r, s, gains in item['edges'])
                    found.append({'kind': kind, 'a': a, 'b': b, 'class_count': len(classes),
                                  'classes': classes, 'colors': sol, 'nodes': nodes})
    found.sort(key=lambda x: (x['class_count'], x['kind'], x['a'], x['b']))
    results.append({'offset': item['offset'], 'tested': tested, 'solutions': found[:10]})
(folder / 'private_core_quotients.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
