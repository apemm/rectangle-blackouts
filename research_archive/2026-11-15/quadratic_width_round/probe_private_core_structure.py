from collections import Counter
from pathlib import Path
import json

folder = Path(__file__).resolve().parent
data = json.loads((folder / 'private_tile_gain_cores_side16.json').read_text())
certs = json.loads((folder / 'all_offset_private_tiles_side16.json').read_text())['certificates']
out = []
for item in data['small_final_cores']:
    degree = Counter(v for r, s, _ in item['edges'] for v in (r, s))
    assignment = certs.get(str(item['offset']), {'assignment': '0' * 256})['assignment']
    adjacency = [set() for _ in item['vertices']]
    for r, s, _ in item['edges']:
        adjacency[r].add(s)
        adjacency[s].add(r)
    def components(deleted):
        pending = set(range(len(adjacency))) - set(deleted)
        answer = []
        while pending:
            reached = {pending.pop()}
            queue = list(reached)
            while queue:
                v = queue.pop()
                nxt = adjacency[v] & pending
                pending -= nxt
                reached |= nxt
                queue.extend(nxt)
            answer.append(sorted(reached))
        return answer
    cuts = []
    for i in range(len(adjacency)):
        for j in range(i + 1, len(adjacency)):
            pieces = components([i, j])
            if len(pieces) > 1:
                cuts.append({'cut': [i, j], 'sizes': sorted(map(len, pieces))})
    out.append({'offset': item['offset'], 'degree_histogram': dict(Counter(degree.values())),
                'certificate_colors': ''.join(str(assignment[v]) for v in item['vertices']),
                'ranks': item['vertices'], 'two_cuts': cuts})
(folder / 'private_core_structure.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
