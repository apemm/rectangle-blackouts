"""Independent modular-word audit of the reverse Hilbert certificates.

The literal transition table comes from the displayed proof. This checker
does not import the carry automaton or its state-graph implementation.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

REV = {
    (0, 0): ((1, 0), (0, 2)), (0, 1): ((2, 0), (3, 3)),
    (1, 0): ((2, 1), (3, 2)), (1, 1): ((1, 1), (0, 3)),
    (2, 0): ((0, 0), (3, 1)), (2, 1): ((1, 2), (2, 2)),
    (3, 0): ((1, 3), (2, 3)), (3, 1): ((3, 0), (0, 1)),
}


def lower_words(child, bits):
    partial = [(0, child)]
    for j, bit in enumerate(bits):
        partial = [(rank + digit * 4**j, parent)
                   for rank, state in partial
                   for digit, parent in REV[state, bit]]
    assert len({rank for rank, state in partial}) == 2**len(bits)
    return [rank for rank, state in partial]


def modular_maxima(a, b, length):
    modulus = 4**length
    maxima = {}
    for bits in product(range(2), repeat=length):
        words = [lower_words(child, bits) for child in range(4)]
        maximum = 0
        for left in words:
            for right in words:
                counts = Counter((a*p-b*q) % modulus
                                 for p in left for q in right)
                maximum = max(maximum, max(counts.values()))
        maxima[''.join(map(str, bits))] = maximum
    return maxima


def hilbert(n):
    if n == 1:
        return [(0, 0)]
    m = n//2
    old = hilbert(m)
    return ([(y, x) for x, y in old]
            + [(x, y+m) for x, y in old]
            + [(x+m, y+m) for x, y in old]
            + [(2*m-1-y, m-1-x) for x, y in old])


def main():
    tables = []
    for a, b, length in ((3, 1, 3), (5, 1, 3), (7, 1, 2), (5, 3, 2)):
        table = modular_maxima(a, b, length)
        for word, count in table.items():
            expected = (6 if word[0] == word[1] else 5) if a == 3 else (
                (8 if word[0] == word[1] else 6) if (a, b) == (5, 1) else 3)
            assert count == expected, (a, b, word, count, expected)
        tables.append({'a': a, 'b': b, 'length': length, 'maxima': table})
    resonance = []
    for k in range(1, 10):
        n = 2**k
        points = hilbert(n)
        row = {rank for rank, point in enumerate(points) if point[0] == n//2-1}
        count = sum(5*p+1 in row for p in row)
        assert count == (n+5)//6
        assert all(points[n*n-1-r] == (n-1-x, y)
                   for r, (x, y) in enumerate(points))
        resonance.append({'side': n, 'count': count})
    data = {'tables': tables, 'slope_five_resonance': resonance,
            'rank_reversal': 'passed through side 512'}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'block_tables': len(tables), 'resonance_sizes': len(resonance),
                      'max_side': 512, 'status': 'passed'}))


if __name__ == '__main__':
    main()
