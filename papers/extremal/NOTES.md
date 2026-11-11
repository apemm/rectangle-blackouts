# Notes on the extremal paper (state after revision round 5, 11 November 2026)

Files: `blackouts_extremal.tex`, `sections/sec1_intro.tex` to `sec9_open.tex`, `extremal.bib`,
`supplement.tex`, `e-jc.sty` (unchanged copy from combinatorics.org), `figs/`,
`data/seven_row_blackouts.txt`, `scripts/check_constructions.py`,
`removed/four_row_hand_proof.tex` (a copy of the proof that is in the paper).
Build: `pdflatex`, `bibtex`, `pdflatex` twice for the paper, `pdflatex` twice for the
supplement. Both builds are clean. The paper has 26 pages and the supplement 4.

## Numbering and labels

| Result | Number | Label |
|---|---|---|
| Threshold theorem, q_h <= m_h <= C h^2 tau*(h)^2 | Theorem 1 | `thm:threshold` |
| Lower bound at every width | Corollary 2 | `cor:everywidth` |
| Explicit construction, f = m + q_h for m >= M_h (existence of m_h) | Proposition 3 | `thm:general` |
| Small heights (Table 1) | Theorem 4 | `thm:small` |
| Row bound | Theorem 16 | `thm:rowbound` |
| Equality structure | Theorem 19 | `thm:equality` |
| Alternating seas | Proposition 22 | `prop:seas` |
| Constructions for a set of parity edges | Proposition 34 | `prop:partial` |
| f(4,m) = m+4 for m >= 6 | Proposition 37 | `prop:four` |
| Finite collar | Theorem 38 | `thm:collar` |

The companion paper cites `thm:rowbound`, `thm:equality`, `thm:small`, `thm:general`. The
label `thm:general` now sits on a proposition, and `thm:small` is stated as a table, without
parts (a) to (e).

## Round 3

- X1: the threshold theorem is Theorem 1 and leads the abstract and the introduction. The
  explicit construction is Proposition 3.
- X2: Remark 35 states c_0 = 3 * 2^35 (about 10^11, from 48 * 2^31 in the placement lemma) and
  that the bound of Theorem 1(b) is below M_h only for h above about 7 * 10^11. The crossover
  was computed with the exact maximum of the divisor function (search over highly composite
  numbers) for the bound c_0 (q_h + 4) tau*^2 + 6 h^2 + 4.
- X3: Section 3 now says that Neuwirth contracts columns to pairs, uses that the contracted
  graph is triangle-free with at most q_h edges (his Proposition 3) and then his cubic
  inequality (Theorem 1(i)). It cites his Remark 18 (maximum m+h-1 for h <= 3, m+4 for
  h = 4 <= m, m+6 for h = 5 < m) and notes that the graph maximum is 8 at h = m = 4 while
  f(4,4) = 7. He proves that the bound is attained (construction after Proposition 17) but
  gives no description of all extremal graphs for this bound. His equality statement
  (Theorem 8) is for the cubic inequality only. So the equality structure is ours.
- X4: Remark 23 says that spacing W_h is not always enough: lexicographic order is valid for
  h = 3, 5, 7 and not valid for h = 4, 6, 8 (checked by the script).
- X5: the square-grid bound is out of the abstract and the introduction. It is Remark 41.
- X6: `supplement.tex` holds the SAT encodings, the lemma that they are faithful, the table
  of the 739 instances, the script description and the Lean details. Section 7 of the paper
  is 4 short paragraphs.
- S1: Corollary 2, f(h,m) >= m + min(q_h, floor(m / (C' tau*(h)^2))) for every h >= 3 and
  m >= 1, with C' = 2 c_0. Fully proved through Proposition 34: (a) even h, any n parity
  edges, width ceil(c_0 n tau*^2); (b) odd h >= 5, n edges good for h-1, same width;
  (c) odd h >= 9, any n edges, width c_0 (n+4) tau*^2 + 6 h^2 + 4. For odd h >= 9 at least
  q_h / 2 edges are good for h-1, so (b) covers n <= q_h / 2 and (c) the rest. Heights up to 8
  use Proposition 3. No restriction lemma is needed: the blackout is defined as the part of
  an obstruction-free configuration in the columns 1 to m, and all doubles lie in these
  columns.
- S2: greedy blackouts with (B1), (B2), (B3) tested as defined, best of 3 runs, each checked
  from the definition. Widths 1180, 1872, 2154, 2919 for h = 12, 13, 14, 16, against
  M_h = 1121, 1559, 2113, 3655. They are in Remark 35.
- S3: at h = 16, 3 of 3 blackouts with (B1) to (B3) are valid and 5 of 5 with (B1) alone are
  not valid. The script prints this. It runs in under 2 minutes.
- S4: not in the theorem, for lack of space. The tail argument is complete and sits in the
  supplement (Section S3, 1 page): T_m is valid for every m >= 21 if the 7 x 45 board T is
  valid, and the script checks T and the widths 21 to 44. The paper states
  f(7,m) = m + 12 for m >= 21 and m_7 <= 21 as Remark 40, with the proof in the supplement.
  Theorem 4 keeps m >= 24. To promote it, move Section S3 into Section 6 (about 0.7 page)
  and change the last row of Table 1. The board contains a tilted rectangle with 3 black
  corners, so the obstruction lemmas of Section 5 do not apply to it and the tail needed
  its own argument.
- (B3) in Section 5 requires distinct columns (round 1). The script now tests exactly this
  definition, and the sets A_e follow Definition 30 exactly.
- Cuts to stay at 26 pages: the count of equality cases after Theorem 19, 6 references
  (G4G14 problem list, Katona, Furedi 1996, Reiman, de Caen and Szekely 1992, Benson in the
  introduction only), and shorter remarks.

## Round 4 (fixes from `papers/AUDIT_round3.md`)

1. Corollary proof: the step for h <= 8 now reads m >= 2 c_0 >= 211 = M_8 >= M_h.
2. Proof of Theorem 1(b): m_h <= M_8 = 211 for h <= 8, and the displayed bound
   c_0 (q_h + 4) tau*^2 + 6 h^2 + 5 for h >= 9 (the +1 is because M in Proposition 34(c) need
   not be an integer). C = c_0 is named.
3. After Corollary 2 the introduction says that it improves on the boundary cross only for
   m >= C' h tau*^2 and adds nothing for h <= 8.
4. Introduction: for even h the singletons are in row 1 or h, and for odd h there are up to
   4 blocks, each with its own 2 rows.
5. Remark 35: the displayed bound is not below M_h for any h < 710132287759, it is below at
   that height, and it is again at least M_h at h = 757474440275. Both numbers were
   recomputed over all intervals on which tau*(h) is constant, for h up to 8 * 10^11. The
   remark does not say what happens for all larger h.
6. Section 7: the boards at h = 5, 7 are called extra tests that no proof in the paper covers.
7. Abstract: it says h = 7 and m >= 24, which is what Theorem 4 says. The value 21 appears
   only in Remark 40 and in the open problems, with a reference to the remark.
8. Supplement, seven rows: the claim on 21 consecutive columns has its own 2 sentences.

Cuts in round 4 to stay at 26 pages: the references Moret and Shapiro, Kovari, Sos and
Turan, and the OEIS entry (the sequence is still linked), the sentence on hidden rectangles
in Section 2, and shorter remarks. Remark 35 names h = 757474440275 as one later height
where the bound is again at least M_h. It makes no claim for all larger h.

## Round 5 (supersedes the numbering table and the S2, S4 entries above)

Numbering of the introduction: Theorem 1 `thm:threshold`, Proposition 2 `thm:general`,
Theorem 3 `thm:small` (Table 1). In the body: Theorem 15 `thm:rowbound`, Theorem 18
`thm:equality`, Proposition 33 `prop:partial`, Corollary 34 `cor:everywidth`, Remark 35
`rem:constants`, Theorem 38 `thm:collar`.

- Seven rows: the tail argument is gone from the paper and the supplement. Theorem 3 says
  f(7,m) = m + 12 for m >= 21. The widths 21, 22, 23 are 3 finite boards (the 21-column
  word printed in Section 6, then the same word followed by 1 and by 2 columns in row 1),
  which the script checks from the definition with their sizes m + 12. The widths m >= 24
  use the 5 boards of `data/seven_row_blackouts.txt` and the collar theorem, as before, and
  do not depend on the 21-column word. The paper says m_7 <= 21 and never m_7 = 21.
- Corollary on every width: stated in Section 5 after the proof of Theorem 1(b), with one
  clause in the introduction.
- Remark 35 describes the placement as first-fit: the edges in a random order, each double
  in the leftmost column that is not bad with the doubles before it. The order of the edges
  is the only random choice, 3 orders per height, smallest width reported. The script
  reproduces the table with its fixed seed.

  | h | 12 | 13 | 14 | 16 | 20 | 24 |
  |---|---|---|---|---|---|---|
  | first-fit width | 1180 | 1872 | 2154 | 2919 | 7157 | 12915 |
  | M_h | 1121 | 1559 | 2113 | 3655 | 9109 | 19163 |
  | validity | definition | definition | definition | definition | Lemma 32 | Lemma 32 |

  For 20 and 24 the script only computes the columns. Their validity rests on the one-block
  lemma and on the script testing (B1) to (B3) as defined.

## What was checked and how

By hand: every proof in Sections 2 to 6 and Section S3 of the supplement.

By `scripts/check_constructions.py`: all explicit blackouts and test boards of Section 6,
the board T and its prefixes of widths 21 to 44, the four-row family for 6 <= m <= 13, the
boundary cross, the alternating seas for 3 <= h <= 8, and the greedy blackouts for
4 <= h <= 14 and h = 16 with the control at h = 16.

Not rerun, taken from the old manuscript and `jis/unsat/README.md`: the 739 LRAT proofs, the
SAT encodings, the candidate search for f(4,4) and f(4,5), and all Lean statements.

## To confirm before submission

- `repo` in the bibliography is https://github.com/apemm/rectangle-blackouts with no commit
  hash. The repository is not public yet. The paper refers to the supplement by its path in
  the repository.
- Hardy and Wright Theorem 315 (tau(n) = O(n^delta)) is quoted from memory of the 6th
  edition. Theorem 317 (Wigert) was confirmed in a second source.
- Title, MSC codes, license line and dates in the preamble are placeholders.
