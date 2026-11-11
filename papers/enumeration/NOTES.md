# Enumeration paper: working notes

Paper: "Counting the Maximum Blackouts That Keep Every Lattice Rectangle Identifiable", for the
Journal of Integer Sequences. It is the companion of the extremal paper in `papers/extremal`.

## Files

- `main.tex` and `sections/sec*.tex`: the source. `figs/` holds the 3 figures in use.
- `enumeration.bib`, `jis.bst`: bibliography. The entries are copied from `jis/pemmasani.bib`,
  plus `pemmasaniExtremal` for the companion paper.
- `make_single_file.py`: writes `blackouts_enumeration.tex`, the single file for submission.
- `blackouts_enumeration.pdf`: built from the single file.

## Build

    pdflatex main && bibtex main && pdflatex main && pdflatex main
    py make_single_file.py
    pdflatex blackouts_enumeration   (twice)

Current state: 22 pages, no undefined references, no overfull boxes.

## What is proved where

- Proved in the paper: Lemmas 2 to 9, Corollary 6 (A338885), Strip Theorem, kings bijection,
  all of Section 4 (three rows), Theorem 24 (no hidden rectangle), Theorem 25 (forbidden
  blocks), Lemma 26, Proposition 27 (automaton), Theorems 31 and 32 (fixed height).
- Cited to the companion paper (Theorem 10): row bound, equality structure for h >= 4, the
  values of f on 2 to 5 rows, and f(h,m) = m + q_h for all large m. Table 1 also uses the
  values of f on 6 and 7 rows.
- Computer-assisted: Theorem 28 and Corollary 29 (four rows), Proposition 30 (five rows), the
  counts of Table 1 with both sides at least 4. In Section 4 the polynomials P, P_B, P_E and the
  constants of the closed form were expanded with SymPy.

## Changes from the old manuscript `jis/pemmasani.tex`

- Three rows: Lemma "window rules" replaces the diamond test, the singleton dichotomy, the
  six-of-nine lemma and the forbidden-window lemma. The run series are defined through
  h_ij and h_ij^beta. The matrix J of the old Proposition "class {A,B}" is replaced by
  h^0 and 2 h^1 (the old second column of J is half of the new one, with the factor 2 moved).
- The three-row generating function is stated from m = 1 (it equals P/Q with no correction).
- The orbit count is a theorem with the closed form for even m.
- The forbidden-block bound is a theorem. Its proof excludes the template words separately,
  by Theorem 24.
- Fixed height: "eventually constant" from the companion paper replaces "eventually
  periodic", and the proof of rationality is shorter.
- Dropped for length: the table of four-row counts by pair set (one sentence kept), the
  second display of the minimal polynomial of rho_4, the evidence table (file names are in
  Section 8), the citations of Alanko et al. and Mertens.

## Open items

- The title in `pemmasaniExtremal` follows the current draft in `papers/extremal`.
- Theorem 10 must match the labels of the companion paper (see the list sent with the report).
