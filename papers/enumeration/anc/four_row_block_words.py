"""The excluded block words of the forbidden-block bound on four rows.

A block is 4 consecutive singleton columns, written as the word of its black rows. For
each pair set F the script lists the words that the bound excludes: the 4 template words,
the 16 other words obtained from a template by exchanging 2 letters, and the words
obtained from a template by changing one letter r to s with {r,s} in F. It then lists all
optima of the 4 x m grid for 6 <= m <= MMAX with the window test of
four_row_certificate.py and checks that no block of an optimum is an excluded word.

Usage:  py four_row_block_words.py [MMAX]   (default 10)
"""
import itertools
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import four_row_certificate as cert  # noqa: E402

TEMPLATES = ('2413', '3412', '2143', '3142')


def excluded(part):
    pairs = {frozenset((a, b)) for a in part[0] for b in part[1]}
    swaps, edits = set(TEMPLATES), set()
    for t in TEMPLATES:
        for p, q in itertools.combinations(range(4), 2):
            w = list(t)
            w[p], w[q] = w[q], w[p]
            swaps.add(''.join(w))
        for p in range(4):
            for s in '1234':
                if frozenset((int(t[p]), int(s))) in pairs:
                    w = list(t)
                    w[p] = s
                    edits.add(''.join(w))
    return swaps, edits


def optima(part, m):
    letters, ok = cert.build(part, only_test=True)
    out = []

    def grow(word, used):
        if len(word) == m:
            if used == 15:
                out.append(word)
            return
        for y in range(8):
            bit = 0
            if y >= 4:
                bit = 1 << (y - 4)
                if used & bit:
                    continue
            new = word + (y,)
            if ok(new[-7:]):
                grow(new, used | bit)

    grow((), 0)
    return out


def main():
    mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    for name, part in cert.PARTS.items():
        swaps, edits = excluded(part)
        bad = swaps | edits
        print(name, 'exchanges', len(swaps), 'changes', len(edits), 'excluded', len(bad))
        for m in range(6, mmax + 1):
            words = optima(part, m)
            blocks = hits = 0
            for w in words:
                for i in range(m - 3):
                    if all(y < 4 for y in w[i:i + 4]):
                        blocks += 1
                        if ''.join(str(y + 1) for y in w[i:i + 4]) in bad:
                            hits += 1
            print('  m =', m, 'optima', len(words), 'blocks', blocks, 'excluded blocks', hits)


if __name__ == '__main__':
    main()
