"""Enumerate full affine embeddings of reversed Hilbert digit sections.

This is finite evidence about residue classes, not an asymptotic claim.
"""
import argparse
from itertools import product
from pathlib import Path
import json
from check_hilbert_carry_independent import lower_words


def embeddings(length):
    modulus = 4**length
    results = {}
    for bits in product(range(2), repeat=length):
        sections = [lower_words(child, bits) for child in range(4)]
        normalized_targets = set()
        for section in sections:
            for origin in section:
                normalized_targets.add(frozenset((x-origin) % modulus for x in section))
        allowed = set()
        for section in sections:
            origin = section[0]
            delta = [(x-origin) % modulus for x in section]
            for ratio in range(1, modulus, 2):
                image = frozenset(ratio*x % modulus for x in delta)
                if image in normalized_targets:
                    allowed.add(ratio)
        results[''.join(map(str, bits))] = sorted(allowed)
    union = sorted(set().union(*map(set, results.values())))
    return {'length': length, 'modulus': modulus, 'union': union,
            'row_words': results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, default=5)
    args = parser.parse_args()
    data = embeddings(args.length)
    path = Path(__file__).with_name('probe_hilbert_modular_embeddings_'+str(args.length)+'.json')
    path.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: data[key] for key in ('length', 'modulus', 'union')}))


if __name__ == '__main__':
    main()
