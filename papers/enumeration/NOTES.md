# Enumeration paper: working notes

Paper: "Counting the Maximum Blackouts That Keep Every Lattice Rectangle Identifiable", for the
Journal of Integer Sequences. It is the companion of the extremal paper in `papers/extremal`.

## Files

- `main.tex` and `sections/sec*.tex`: the source. `figs/` holds the 3 figures in use.
- `enumeration.bib`, `jis.bst`: bibliography.
- `make_single_file.py`: writes `blackouts_enumeration.tex`, the single file for submission.
- `blackouts_enumeration.pdf`: built from the single file.
- `anc/four_row_gf.txt`: numerator, denominator and factors of the four-row series.
- `anc/four_row_certificate.py`: builds the automata of Proposition "the automaton" and
  proves the degree-420 recurrence on them (about 5 minutes). Output
  `anc/four_row_certificate.json`.
- `anc/four_row_block_words.py`: the 44 excluded block words of the forbidden-block remark,
  checked on all optima with m <= 10.
- `removed/forbidden_block_bound.tex`: the full proof of the forbidden-block bound.

## Build

    pdflatex main && bibtex main && pdflatex main && pdflatex main
    py make_single_file.py
    pdflatex blackouts_enumeration   (twice)

Current state: 22 pages, no undefined references, no overfull box above 5pt.

## What is proved where

- Proved in the paper: the lemmas of Section 2, the remark on A338885, the Strip Theorem, the
  kings bijection, all of Section 4 (three rows), "no hidden rectangle", "six columns of
  memory", the automaton, and Section 7 (regularity, ultimately periodic excess, rational
  series). Section 7 does not use the companion paper.
- Cited to the companion paper (Theorem "imports"): row bound, equality structure for
  h >= 4, the values of f on 2 to 5 rows. Nothing else.
- Computer-assisted: the four-row generating function and growth (certificate on the stated
  automata, exact by the Chinese remainder theorem), the five-row table, and the counts
  a_4(4), a_4(5), a_5(5), a_5(6), a_5(7). In Section 4 the polynomials P, P_B, P_E and the
  constants of the closed form were expanded with SymPy.
- Remark without proof: the forbidden-block bound (proof in `removed/`).

## Revision of 11 November (review guide)

- E1: forbidden-block theorem cut to a remark, proof moved to `removed/`.
- E3: fixed-height theorem proved without the large-width result. The excess bound is
  h(h-1)/2 from "no 2 columns share 2 black rows". States (a) regular for each excess,
  (b) f(h,m) - m ultimately periodic, (c) optima regular and series rational. One sentence
  cites the companion paper for "eventually constant".
- E4: certificate on the automaton of the proposition itself. State counts 60975, 138095,
  55575. The vector identity at index 445 holds modulo 48 primes below 2^31, and the size
  bound 8^445 * sum|q_j| makes it exact. The numerator is checked the same way.
- E5: table of values reduced to h <= 5.
- E6: one theorem for a_3(m). The closed form of E_m holds for m >= 2 (E_2 = 10).
- E7: A338885 result is a remark, attributed to Kagey (author of the entry).
- E8: five rows is a table and a short paragraph.
- Imports: the large-width item is gone.
- New citations: Stanley EC1 Section 4.7, Calkin and Wilf, Wilf's kings paper, Mertens,
  Massey for Berlekamp-Massey.

## Open items

- The title in `pemmasaniExtremal` follows the current draft in `papers/extremal`.
- The companion paper is cited as a whole, never by theorem number.

## Revision round 3 (audit, item 4)

- Four-row proof: added the bound for the numerator check, 3 * 8^444 * sum|q_j| + max|P_n|,
  which the 48 primes cover (product 1488 bits, needed 1455 bits), and the sentence that
  a_F(n) counts optima only for n >= 6 while the recurrence uses indices >= 25.
- `anc/four_row_certificate.py`: docstring reworded, and an assertion that the script bound
  covers the numerator check. The computation is unchanged and was not rerun.
- References to the companion paper rechecked after its renumbering. All are by name.
