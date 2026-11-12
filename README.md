# Rectangle blackouts

Black out as many points of an h x m grid as possible so that every rectangle with corners on grid
points (tilted ones included) is still determined by its visible corners. The blackout is chosen
before the rectangle. This is Problem 1 of Peter Kagey's list (peterkagey.com/problems/001).

## Papers

The results are proved in the two manuscripts in `papers/`.

- `papers/extremal/blackouts_extremal.pdf`: "The maximum size of a blackout that keeps every
  lattice rectangle identifiable". It has the extremal results: the row bound, the threshold
  theorem, the explicit construction, the exact values for small heights, and the bounds for
  square grids. The source is `blackouts_extremal.tex` with `sections/`, and the supplement is
  `supplement.pdf`.
- `papers/enumeration/blackouts_enumeration.pdf`: "Counting the Maximum Blackouts That Keep Every
  Lattice Rectangle Identifiable". It has the counting results: two, three and four rows, the
  five-row counts, and the rationality of the counting series at fixed height. The source is
  `main.tex` with `sections/`, and `blackouts_enumeration.tex` is the single file made from it.

The folder `jis/` has the source of the earlier combined manuscript (`jis/pemmasani.tex`), and the
scripts, data and UNSAT evidence that both papers cite.

## Results

Here f(h,m) is the maximum size of a valid blackout of h rows and m columns, a_h(m) is the number
of maximum blackouts, q_h = floor(h^2/4), and W_h = 1 + floor((h-1)^2/4). Results marked
(computer) rest on a finite computation, checked by at least two separately written programs.

- Every grid: h+m-1 <= f(h,m), and f(h,m) <= m + q_h for m >= 3.
- Two rows, m >= 3: f = m+1, with exactly m*2^(m-1) optima (Strip Theorem).
- Three rows, m >= 3: f = m+2. The optima are counted exactly:
  a_3(m) = 4(m-1)(3m+2)3^(m-5) + E_m for m >= 4, with a closed form for E_m, a rational generating
  function, and a_3(m) ~ (4/81) m^2 3^m.
- Four rows: f = m+4 for m >= 6, and f(4,4) = 7, f(4,5) = 8 (computer). No valid blackout hides a
  rectangle for m >= 4. The generating function of a_4(m) is rational with a denominator of degree
  420, and a_4(m) ~ c m^4 3.3520^m (computer).
- Five rows: f(5,5) = 10, f(5,6) = 11, f(5,7) = 12, and f(5,m) = m+6 for every m >= 8 (computer,
  with the finite collar theorem).
- Six rows (computer): f(6,m) = m+7 for 8 <= m <= 11, f(6,m) = m+8 for 12 <= m <= 14, and
  f(6,m) = m+9 for every m >= 15. So f(h,m) is known for every h <= 6 and every m.
- Seven rows (computer): f(7,m) = m+12 for every m >= 21. The widths 9 to 20 are open.
- Every height: let m_h be the least width from which f(h,m) = m + q_h holds at every larger
  width. Then q_h <= m_h <= C h^2 tau*(h)^2 for every h >= 4, where tau*(h) is the largest number
  of divisors of an integer up to h^2. So m_h = h^(2+o(1)). The proof places the columns with 2
  black points at random and uses the local lemma.
- Every height, explicitly: f(h,m) = m + q_h for every h >= 3 and every m >= q_h + (q_h - 1) W_h,
  by the alternating boundary seas. The known values are m_4 = 6, m_5 = 8, m_6 = 15, and
  m_7 <= 21.
- Every width: f(h,m) >= m + min(q_h, floor(m / (C' tau*(h)^2))).
- Small cells (computer): f(6,6) = 12, f(6,7) = 13, f(7,7) = 14, f(6,8) = 15, f(7,8) = 16. The guess
  f = h+m for both sides at least 4 fails at 5 x 8 and 6 x 8.
- Square grids: f(n,n) < n^(4/3) + (2/3) n for n >= 3, and f(n,n) >= c n^(6/5) (1+ln n)^(-2/5)
  for some c > 0.
- A tilted lattice rectangle of height n has width at most floor(n^2/4) + 1 = A033638(n), with
  equality possible. This proves the conjecture in A338885 that its row n has largest entry
  A033638(n).

The key step is that the axis-aligned rectangles are identifiable exactly when the row-column
incidence graph of the blackout has no 4-cycle and no 6-cycle (m >= 3). Replacing each column by a
tree on its black rows gives a triangle-free graph on the rows, and Mantel's theorem gives the
upper bound. For bipartite graphs of girth at least 8 this bound is due to Neuwirth. The
constructions for three and four rows are checked against every tilted rectangle.

In the OEIS, f(h,m) is A397315 and f(n,n) is A398321. The counts a_h(m) are A399580, with the
rows A001787 (2 rows), A401223 (3 rows), A401224 (4 rows) and A401225 (5 rows, from width 8).
A401226 counts the three-row optima up to symmetry, and A398448 is E_m.

The notes `notes/notes.pdf` (source `notes/notes.tex`) are a longer companion that walks through
the results with small examples and about 25 figures. The figures are drawn by
`notes/make_figures.py`, which checks every blackout it draws against the definition first.

## Verification

`python verify_narrow.py` (standard library only) enumerates rectangles by their diagonals, checks
the incidence-graph lemma on 74,304 blackouts, checks the tilted rectangle lists and the
constructions at widths up to 128, and runs the two finite four-row checks.

`papers/extremal/scripts/check_constructions.py` checks the explicit blackouts of the extremal
paper against the definition. `papers/enumeration/anc/four_row_certificate.py` certifies the
recurrence of degree 420 for four rows.

The ILP engine and the brute-force oracle used for the table of values are in `solver/`, with
their tests; they need the packages in `requirements.txt`. The predictions and their outcomes are
in `data/ledger.md`. The supplement of the extremal paper (`papers/extremal/supplement.tex`)
describes the SAT encodings behind the computer-assisted upper bounds, proves that they are
faithful, and lists the instances and the certificates. `jis/supplement.tex` gives the table of
values and lists, for each computer-assisted statement, its method, its independent check and its
evidence file; `jis/scripts/README.md` gives the commands.

The Lean 4 formalization is in `lean/`, and `lean/README.md` says what each file proves.

## Build

- Extremal paper, from `papers/extremal/`: `pdflatex blackouts_extremal`, `bibtex
  blackouts_extremal`, then `pdflatex blackouts_extremal` twice. For the supplement, `pdflatex
  supplement` twice.
- Enumeration paper, from `papers/enumeration/`: `pdflatex main`, `bibtex main`, `pdflatex main`
  twice, then `python make_single_file.py` and `pdflatex blackouts_enumeration` twice.
- Earlier manuscript, from `jis/`: `pdflatex pemmasani`, `bibtex pemmasani`, `pdflatex pemmasani`
  twice, then `pdflatex supplement` twice.
- Notes, from `notes/`: `python make_figures.py`, then `pdflatex notes` 3 times.

`game/index.html` is a playable version of the problem on grids up to 10 x 10 (open it in a
browser). It is the rectangle game from my website, with larger grids.

## Open

- Is m_h = O(h^2)? What is m_7, and what is f(7,m) for 9 <= m <= 20?
- Is f(h,m+1) >= f(h,m) + 1 for all h >= 2 and m >= 3?
- The generating function and growth rate of a_5(m).
- The order of growth of f(n,n), between n^(6/5) and n^(4/3) up to logarithms.

## License

MIT, see `LICENSE`.
