# Notes on the extremal paper (state after revision round 1, 10 November 2026)

Files: `blackouts_extremal.tex`, `sections/sec1_intro.tex` to `sec9_open.tex`, `extremal.bib`,
`e-jc.sty` (unchanged copy from combinatorics.org), `figs/`, `data/seven_row_blackouts.txt`,
`scripts/check_constructions.py`, `removed/four_row_hand_proof.tex`.
Build: `pdflatex`, `bibtex`, `pdflatex` twice. The build is clean: no undefined references and
no overfull boxes. The PDF has 25 pages.

Labels used by the companion paper and not to be renamed: `thm:rowbound`, `thm:equality`,
`thm:small`, `thm:general`.

## Decisions

- Spacing in the alternating seas: the paper states and proves spacing W_h + 1, so
  M_h = q_h + (q_h - 1) W_h. The Lean files still use spacing 2 W_h + 2, and Section 7 says so.
- Near-quadratic threshold: Theorem 2(b), m_h <= C h^2 tau*(h)^2, with a complete proof in
  Section 5. The polylogarithmic refinements appear only in Remark `rem:sharper`, with no claim.
- Monotonicity is stated as open (Section 9).

## Revision round 1

Audit fixes (`AUDIT_sections_4_5.md`), all applied:

- Section 4: "the columns of R" is defined as the interval from the smallest to the largest
  column. The last step of (iii) now ends with "D_2 is a second double in the columns of R_1".
  Case (c) says c >= 3. Case (d) says real t.
- Section 5: `lem:placement` is applied only to nonempty sets. `lem:block` states its own
  hypothesis (no bad L) and no longer refers to the range 1..N. The case L = {e} refers to the
  paragraph before the proof. The vertical case is named in Section 5.1.
- (B3) now also requires that the columns X_e, e in L, are distinct. Without this, a point
  could carry 2 labels when 2 columns coincide, and the type of a point was not well defined.
  The probability bound for (B3) is written with a fixed list of types and a fixed
  translation class. The |L| >= 2 branch and the rival-pair branches of `lem:block` are
  written out.
- The remark on the computer test moved to Section 7, with the sentence on h = 5, 7.
- Introduction: "a few black points" instead of "3 or 4".

Length cuts:

- f(4,m) = m+4: the hand proof is removed (kept in `removed/four_row_hand_proof.tex`). The
  companion paper imports this value from here, so it cannot be cited there. The paper now
  uses Theorem 1 for m >= 13 and a computer check of the 7 widths 6 to 12. Theorem 3 says that
  part (b) is computer-assisted for m <= 12.
- The 5 seven-row blackouts are in `data/seven_row_blackouts.txt`. The text shows the one of
  width 24. The checker script reads the file.
- The lemma on the SAT encodings is folded into the text of Section 7.
- The square-grid bound is a remark with a proof sketch, marked as a sketch. The abstract and
  the introduction no longer say "we show". The full proof is in the old manuscript
  (`jis/sections/appC_square.tex`).
- Dropped: the outline paragraph, the citations for the cardinality encodings, PySAT, and the
  Math Stack Exchange post.

## Changes to statements of the old manuscript

- Theorem D: threshold q_h + (q_h - 1) W_h instead of q_h + (q_h - 1)(2 W_h + 1).
- f(4,m) for 6 <= m <= 12 rests on a computer check (see above).
- The boundary cross lemma has a new proof through the criterion.
- f(5,5) >= 10: the hand table for S_0 is dropped. The paper cites the finite check (130
  rectangles) and the Lean kernel check.
- Square grids: remark with sketch, no explicit constant.
- f(7,8) = 16 is part of Theorem 3(e). The witness 27,367,46,2,6,24,125,16 is the first model
  in `jis/data/table_counts/sat_7x8_16.json`.
- The row bound theorem no longer states the transposed bound h + q_m.

## What was checked and how

By hand: every proof in Sections 2 to 6.

By `scripts/check_constructions.py` (definition-level check, about 16 seconds): all explicit
blackouts and test boards of Section 6, the four-row family for 6 <= m <= 13, the boundary
cross, the alternating seas with spacing W_h + 1 for 3 <= h <= 8 (and their failure with
spacing W_h at h = 4, 6), and the construction of Section 5 for 4 <= h <= 13. The last test
does not exercise (B2) and (B3), as the audit notes. Those rest on the written proof.

Not rerun, taken from the old manuscript and `jis/unsat/README.md`: the 739 LRAT proofs, the
SAT encodings, the candidate search for f(4,4) and f(4,5), and all Lean statements.

## To confirm before submission

- `repo` in the bibliography is https://github.com/apemm/rectangle-blackouts with no commit
  hash. The repository is not public yet.
- Hardy and Wright Theorem 315 (tau(n) = O(n^delta)) is quoted from memory of the 6th
  edition. Theorem 317 (Wigert) was confirmed in a second source.
- The sentence on Neuwirth's contraction (Section 3) says that a column with 3 black rows
  would give a triangle. Check the tone.
- Title, MSC codes, license line and dates in the preamble are placeholders.
