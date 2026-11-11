"""Draw the two new figures of the extremal paper as TikZ files.

mixed.tex  two mixed pairs: an axis-aligned and a tilted rectangle with a common side or diagonal
seas.tex   the alternating boundary seas on four rows, with the doubles W_4 + 1 = 4 columns apart

The style matches the figures copied from jis/figs: dashed grid, white points as open circles,
black points gray and crossed, rectangles as thick outlines under the points.
Coordinates are one-based (column, row) with (1,1) the top-left point.

Run from this folder: py make_figures.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def picture(h, m, black, s, rects=(), shown=(), caption=None, shift=0.0, labels=True):
    out = [f'  \\begin{{scope}}[xshift={shift:.3f}cm]']
    lw = 0.6 * s
    grid = ' '.join(f'(1,-{j}) -- ({m},-{j})' for j in range(1, h + 1))
    grid += ' ' + ' '.join(f'({i},-1) -- ({i},-{h})' for i in range(1, m + 1))
    out.append(f'    \\draw[black,line width={0.4 * s:.2f}pt,dash pattern=on {1.5 * s:.2f}pt off '
               f'{1.5 * s:.2f}pt] {grid};')
    for colour, pts in rects:
        path = ' -- '.join(f'({x},-{y})' for x, y in pts)
        out.append(f'    \\draw[{colour},line width={2.84 * s:.2f}pt,line join=round] {path} -- cycle;')
    for j in range(1, h + 1):
        for i in range(1, m + 1):
            if (i, j) in black:
                out.append(f'    \\filldraw[fill=kgray,draw=black,line width={lw:.2f}pt] ({i},-{j}) '
                           f'circle (0.3);')
                out.append(f'    \\draw[black,line width={lw:.2f}pt] ({i - 0.212:.3f},-{j - 0.212:.3f}) -- '
                           f'({i + 0.212:.3f},-{j + 0.212:.3f}) ({i - 0.212:.3f},-{j + 0.212:.3f}) -- '
                           f'({i + 0.212:.3f},-{j - 0.212:.3f});')
            else:
                fill = 'kyellow' if (i, j) in shown else 'white'
                out.append(f'    \\filldraw[fill={fill},draw=black,line width={lw:.2f}pt] ({i},-{j}) '
                           f'circle (0.3);')
    if labels:
        for i in range(1, m + 1):
            out.append(f'    \\node[lab] at ({i},-0.45) {{{i}}};')
        for j in range(1, h + 1):
            out.append(f'    \\node[lab] at (0.45,-{j}) {{{j}}};')
    if caption:
        out.append(f'    \\node[capt,anchor=north] at ({(m + 1) / 2:.2f},-{h + 0.45:.2f}) {{{caption}}};')
    out.append('  \\end{scope}')
    return out


def tikz(s, body):
    return ([f'\\begin{{tikzpicture}}[x={s}cm,y={s}cm,baseline=(current bounding box.north)]']
            + body + ['\\end{tikzpicture}'])


def write(name, lines):
    with open(os.path.join(HERE, name), 'w', encoding='ascii', newline='\n') as fh:
        fh.write('\n'.join(lines) + '\n')


def is_rectangle(pts):
    (a, b, c, d) = pts
    u = (b[0] - a[0], b[1] - a[1])
    v = (d[0] - a[0], d[1] - a[1])
    assert u[0] * v[0] + u[1] * v[1] == 0 and u != (0, 0) and v != (0, 0)
    assert (a[0] + u[0] + v[0], a[1] + u[1] + v[1]) == c


def mixed():
    s = 0.62
    body = []
    r1 = [(1, 2), (3, 2), (3, 4), (1, 4)]
    r2 = [(1, 2), (2, 1), (3, 2), (2, 3)]
    is_rectangle(r1)
    is_rectangle(r2)
    black = {(1, 4), (3, 4), (2, 1), (2, 3)}
    body += picture(4, 3, black, s, rects=[('kblue', r1), ('kred', r2)], shown={(1, 2), (3, 2)},
                    caption='(a)')
    r1 = [(4, 1), (5, 4), (2, 5), (1, 2)]
    r2 = [(4, 1), (6, 3), (5, 4), (3, 2)]
    is_rectangle(r1)
    is_rectangle(r2)
    black = {(1, 2), (2, 5), (3, 2), (6, 3)}
    body += picture(5, 6, black, s, rects=[('kblue', r1), ('kred', r2)], shown={(4, 1), (5, 4)},
                    caption='(b)', shift=5.2 * s)
    write('mixed.tex', tikz(s, body))


def seas():
    h, gap = 4, 4
    edges = [(1, 3), (1, 4), (2, 3), (2, 4)]
    m = 1 + (len(edges) - 1) * gap + 2
    black = set()
    row, j = 1, 0
    for x in range(1, m + 1):
        if j < len(edges) and x == 1 + j * gap:
            black |= {(x, edges[j][0]), (x, edges[j][1])}
            row = h + 1 - row
            j += 1
        else:
            black.add((x, row))
    assert len(black) == m + len(edges)
    s = 0.62
    write('seas.tex', tikz(s, picture(h, m, black, s)))


if __name__ == '__main__':
    mixed()
    seas()
