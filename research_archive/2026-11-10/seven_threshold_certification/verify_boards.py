"""Brute-force checks of the stored seven-row boards. No solver is used.

1. The four stored 7 x 21 equality boards are valid and have the equality
   structure.
2. Every prefix of length 21, ..., 60 of the tail word
       core(21 columns), 1, 1, 1, 2, 2, 2, ...
   is valid, checked width by width against the full rectangle list of that
   width, and is an equality board with m + 12 black cells.
3. The 7 x 60 prefix contains no entirely black rectangle, columns 25 to 60
   are the constant singleton row 2, and every tilted rectangle of height at
   most seven spans at most ten columns. These are the finite inputs of the
   translation argument in README.md that covers every width above 60.
4. The stored 31-cell board of width 20 is valid.
"""
import json
import time

from certlib import (balanced_partitions, find_collision, is_equality_board,
                     rectangles_by_diagonals, rectangles_by_sides, word_to_black)

BOARDS21 = [
    '27,25,3,36,6,6,47,1,67,16,6,1,12,1,14,1,1,23,34,45,56',
    '23,34,45,56,7,7,47,7,67,7,2,27,12,7,14,2,2,25,5,36,16',
    '16,36,5,25,2,2,14,7,12,27,2,7,67,7,47,7,7,56,45,34,23',
    '56,45,34,23,1,1,14,1,12,1,6,16,67,1,47,6,6,36,3,25,27',
]
CORE = BOARDS21[2].split(',')
WORD20 = '36,5,25,2,2,14,7,12,27,2,7,67,7,47,7,7,56,45,34,23'
PARITY = ((1, 3, 5), (0, 2, 4, 6))        # rows 2,4,6 against rows 1,3,5,7


def main():
    began = time.time()
    out = {'height': 7}
    assert PARITY in balanced_partitions(7)

    r21 = rectangles_by_diagonals(7, 21)
    assert r21 == rectangles_by_sides(7, 21)
    out['boards_21'] = []
    for word in BOARDS21:
        black = word_to_black(word, 21)
        assert len(black) == 33
        assert find_collision(r21, black) is None
        assert is_equality_board(black, 7, 21, PARITY)
        out['boards_21'].append({'word': word, 'black_cells': 33, 'valid': True,
                                 'presentations': len(r21), 'partition': 'rows 2,4,6 | 1,3,5,7'})

    out['tail_prefixes'] = []
    for m in range(21, 61):
        word = (CORE + ['1'] * 3 + ['2'] * 36)[:m]
        black = word_to_black(word, m)
        rects = rectangles_by_diagonals(7, m)
        if m in (21, 40, 60):
            assert rects == rectangles_by_sides(7, m)
        assert len(black) == m + 12
        assert find_collision(rects, black) is None
        assert is_equality_board(black, 7, m, PARITY)
        out['tail_prefixes'].append({'m': m, 'black_cells': m + 12, 'rectangles': len(rects), 'valid': True})
        print('width', m, 'valid,', len(rects), 'rectangles', flush=True)

    word60 = CORE + ['1'] * 3 + ['2'] * 36
    black60 = word_to_black(word60, 60)
    rects60 = rectangles_by_diagonals(7, 60)
    hidden = sum(1 for R in rects60 if R <= black60)
    assert hidden == 0
    assert all(word60[c] == '2' for c in range(24, 60))
    span = 0
    for R in rectangles_by_diagonals(7, 30):
        rows = sorted(p // 30 for p in R)
        cols = sorted(p % 30 for p in R)
        axis = rows[0] == rows[1] and rows[2] == rows[3] and cols[0] == cols[1] and cols[2] == cols[3]
        if not axis:
            span = max(span, cols[3] - cols[0])
    assert span == 10
    out['tail_inputs'] = {'word_60': ','.join(word60), 'hidden_rectangles_in_width_60': hidden,
                          'constant_row_2_columns': [25, 60],
                          'max_tilted_column_span_height_7': span}

    black20 = word_to_black(WORD20, 20)
    assert len(black20) == 31
    assert find_collision(rectangles_by_diagonals(7, 20), black20) is None
    out['board_20'] = {'word': WORD20, 'black_cells': 31, 'valid': True}

    out['status'] = 'PASS'
    out['seconds'] = round(time.time() - began, 1)
    with open('verify_boards.json', 'w') as fh:
        json.dump(out, fh, indent=1)
    print('PASS', out['seconds'])


if __name__ == '__main__':
    main()
