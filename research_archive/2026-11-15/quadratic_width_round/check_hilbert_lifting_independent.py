"""Independent direct-word and digit-pair audit of affine lifting.

Build starting states from complete words modulo sixteen. Next digits
are tested by enumerating both rank digits, without modular inversion.
"""
from itertools import product
from pathlib import Path
import json
from check_hilbert_carry_independent import REV


def words_with_parents(child, bits):
    paths = [(0, child)]
    for place, bit in enumerate(bits):
        paths = [(rank+digit*4**place, parent)
                 for rank, state in paths
                 for digit, parent in REV[state, bit]]
    return dict(paths)


def initial_nodes(a, b):
    nodes = set()
    for bits in product(range(2), repeat=2):
        sections = [words_with_parents(child, bits) for child in range(4)]
        for left, right in product(sections, repeat=2):
            for c in range(16):
                pairs = []
                for x, px in left.items():
                    candidates = [(y, py) for y, py in right.items()
                                  if (a*x-b*y-c) % 16 == 0]
                    if len(candidates) != 1:
                        break
                    y, py = candidates[0]
                    pairs.append((px, py, (a*x-b*y-c)//16, x % 4))
                else:
                    nodes.add(frozenset(pairs))
    return nodes


def next_node(node, a, b, bit, c_digit, multiplier_lift):
    result = set()
    for left, right, carry, low in node:
        for x, px in REV[left, bit]:
            candidates = [(y, py) for y, py in REV[right, bit]
                          if (a*x-b*y+carry-c_digit
                              + b*multiplier_lift*low) % 4 == 0]
            if len(candidates) != 1:
                return None
            if multiplier_lift:
                continue
            y, py = candidates[0]
            value = a*x-b*y+carry-c_digit
            assert value % 4 == 0
            result.add((px, py, value//4, low))
    return frozenset(result)


def audit(a, b):
    starts = initial_nodes(a, b)
    nodes = set(starts)
    pending = list(starts)
    count = 0
    edge_count = 0
    while pending:
        node = pending.pop()
        for bit, c_digit in product(range(2), range(4)):
            for lift in (1, 2, 3):
                count += 1
                assert next_node(node, a, b, bit, c_digit, lift) is None
            target = next_node(node, a, b, bit, c_digit, 0)
            if target is not None:
                edge_count += 1
                if target not in nodes:
                    nodes.add(target)
                    pending.append(target)
    return {'a': a, 'b': b, 'initial_nodes': len(starts),
            'invariant_nodes': len(nodes), 'canonical_edges': edge_count,
            'forbidden_lifts_checked': count}


def main():
    results = [audit(a, b) for a, b in ((1, 1), (5, 1), (1, 5))]
    assert [r['invariant_nodes'] for r in results] == [131, 22, 30]
    data = {'status': 'passed', 'results': results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2)+'\n',
                                                encoding='utf-8')
    print(json.dumps(data))


if __name__ == '__main__':
    main()
