"""Exact checks of the explicit one-gap sixteen-label construction."""
import json
from itertools import product
from pathlib import Path

CYCLE = [(0, 0), (1, 2), (1, 3), (0, 2), (0, 3), (2, 3),
         (0, 1), (2, 1), (3, 1), (3, 2), (1, 0), (2, 0),
         (3, 0), (1, 1), (2, 2), (3, 3)]


def placement(q, u):
    slots = [k for r in range(q) for k in range(r, 16, q)]
    labels = [(i, (j + u) % 4) for i, j in CYCLE]
    output = [None] * 16
    for slot, label in zip(slots, labels):
        output[slot] = label
    assert set(output) == set(product(range(4), repeat=2))
    return output


def main():
    assert set(CYCLE) == set(product(range(4), repeat=2))
    for k in range(16):
        i, j = CYCLE[k]
        ip, jp = CYCLE[(k + 1) % 16]
        assert (jp - i) % 4 and (j - ip) % 4
    modular = integer = 0
    for q in range(1, 16):
        for u in range(4):
            p = placement(q, u)
            for k in range(16 - q):
                i, j = p[k]
                ip, jp = p[k + q]
                assert (jp - i - u) % 4 and (j - ip - u) % 4
            modular += 1
        for u in range(-3, 4):
            p = placement(q, u)
            for k in range(16 - q):
                i, j = p[k]
                ip, jp = p[k + q]
                assert jp - i != u and j - ip != u
            integer += 1
    result = {"status": "PASS", "cycle_labels": 16,
              "modular_instances": modular, "integer_instances": integer}
    Path(__file__).with_suffix('.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
