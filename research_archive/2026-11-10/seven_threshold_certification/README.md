# Seven-row threshold: independent certification attempt

10 November 2026. This folder re-examines the claim `m_0(7) = 21` with a new encoder written from
the definitions. **The certification is incomplete.** The construction half of the claim is fully
checked. The exclusion half is confirmed at widths 12 to 14, almost confirmed at widths 15 and 16,
not attempted at widths 17 to 19, and confirmed for only 2 of 19 classes at width 20. No DRAT
proof was checked. The exclusion of widths 17 to 20 therefore still rests on the stored CaDiCaL
runs of 9 November.

Nothing here contradicts a stored result.

## 1. The claim and its logical structure

Height 7, width `m`. The paper gives `f(7,m) <= m + 12` for `m >= 3`, with equality exactly when an
equality board exists: every column has one or two black cells, and the twelve two-cell columns
realize each pair of a complete bipartite graph between a 3 + 4 partition of the rows exactly once.
That theorem is used here and is not under audit.

`m_0(7) = 21` is the conjunction of two statements.

- **(i) Exclusion.** No equality board exists at any width `m <= 20`.
- **(ii) Construction.** An equality board exists at every width `m >= 21`.

Statement (i) needs a separate argument at each width. Equality at width `m` does not pass to
width `m - 1` in general. Only an end column can be removed without changing the geometry, and
the result is an equality board only if that column is a singleton. A board whose two end columns
are both doubles gives nothing at width `m - 1`. So exclusion at width 20 alone does not exclude
width 19. The stored note is right to say that "no monotonicity assumption about equality widths
is needed", because it treats every width from 12 to 20.

The widths split as follows.

| Widths | Why no equality board exists |
|---|---|
| `m <= 11` | Twelve two-cell columns do not fit. |
| 12 to 16 | Stored work: the window-capacity theorem of `equality_window_capacity.md` (itself computer-assisted). This folder: direct SAT, section 4. |
| 17 to 20 | Stored work: 19 SAT instances per width, CaDiCaL 1.9.5, no proof log. This folder: section 4. |

The value `f(7,20) = 31` follows from (i) at width 20 and one valid 31-cell board.

## 2. How the stored exclusion was done, and whether its reductions are sound

Source: `2026-11-09/full_problem_push/seven_row_equality_width_exclusions.md` and
`seven_row_equality_threshold_sat.py`.

- **Partitions.** There are 35 partitions of the seven rows into classes of sizes 3 and 4. The
  stored runs use 19 of them, one from each orbit of the row reflection `y -> 8 - y` (three
  partitions are fixed, and (35 + 3) / 2 = 19). This is sound: the reflection maps lattice
  rectangles to lattice rectangles. No other row permutation is used. `certlib.reflection_classes`
  recomputes the count 19.
- **Column reflection.** One fixed double is required to lie in the left half, middle column
  included. Sound for the same reason.
- **Structure.** Each instance places the twelve doubles of its partition exactly once and lets
  every other column be any singleton. This is the equality structure of the paper's theorem.
- **Extra constraints.** Every window of 9 to 14 columns gets a cap on its number of doubles, taken
  from `f(7,9) = 17`, `f(7,10) = 18`, `f(7,11) = 20`, `f(7,12) = 21` and two restricted bounds at
  window lengths 13 and 14. These caps are earlier computer results. The stored UNSAT answers are
  conditional on them.
- **Solver.** CaDiCaL 1.9.5 through PySAT (`cadical195`), one run per instance, all UNSAT, total
  times 27 s, 111 s, 230 s and 603 s at widths 17 to 20. No second solver and no proof log.
- **Widths below 17** are not SAT instances in the stored work. They follow from the
  window-capacity theorem.

## 3. What was written here

All code is new. Nothing is imported from the 9 November folders.

| File | Role |
|---|---|
| `certlib.py` | Two rectangle generators (corner plus perpendicular sides, and pairs of equal diagonals with a common midpoint), a brute-force validity check, and the encoders. |
| `run_one.py` | Runs one instance and appends one JSON line. A SAT model is always re-checked by brute force with the generator that the encoder does not use. |
| `verify_boards.py` | Solver-free check of the stored boards and of the finite inputs of the tail argument. |
| `explore_windows.py`, `run_windows.sh`, `build_caps.py` | Window bounds, section 4.1. |
| `run_width.sh`, `run_rest.sh` | The height-7 runs, one process at a time. |
| `summarize.py` | Builds `summary.json` from the result files. |

**Validity encoding.** Two distinct rectangles share 0, 1 or 2 corners, and their symmetric
difference lies in the black set exactly when all unshared corners are black. The encoder has one
auxiliary variable per rectangle ("entirely black") with an at-most-one constraint, one auxiliary
variable per rectangle and corner ("the other three corners are black") with an at-most-one
constraint per cell, and explicit four-literal clauses for pairs that share two corners. It does
not use the no-hidden-rectangle theorem or any support argument.

**Three instance types.**

- `direct`: a valid black set with at least `k` cells. No structure theorem.
- `struct`: an equality board for one partition. Relies on the paper's structure theorem.
- `window`: section 4.1.

**Solvers.** CaDiCaL 1.9.5 (`cadical195`) and Glucose 4.1 (`glucose4`) from the system
`python-sat 1.9.dev15`. The copy in `full_problem_push/.runtime` was not used: its Python layer
does not match the binary module that `py` loads, and proof logging fails with it.

## 4. Results

### 4.1 Window bounds (new intermediate lemma)

Without extra constraints my encoder needs 180 s (CaDiCaL) and 124 s (Glucose) for a single class
at width 17, so the full exclusion was out of reach. I did not import the stored caps. Instead:

> **Window lemma.** Any `k` consecutive columns of an equality board for partition `P` form a
> valid `7 x k` board in which every column has one or two cells, two-cell columns join the two
> classes of `P`, and no pair repeats.

This holds because validity passes to sub-boards. For each of the 19 classes and each
`k = 7, ..., 11`, the instance "such a window with at least `d + 1` doubles" is UNSAT with both
solvers (188 instances, all UNSAT, 585 s in total; `window_results.jsonl`). The resulting caps `d`
are in `window_caps.json`:

| Window length | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|
| Largest number of doubles | 6 (7 for class 0) | 6 or 7 | 7 | 7 or 8 | 8 (7 for class 25) |

These are stronger than the unrestricted values used by the stored runs (8, 8, 9 doubles at
lengths 9, 10, 11), which is consistent, because my windows are restricted to one partition.
`struct` instances at height 7 add these caps and the column-reflection break. Each height-7
answer below is conditional on the window instances.

### 4.2 Certification table for statement (i)

"Classes" means reflection classes, 19 in total, indexed as in `certlib.balanced_partitions(7)`.
Class 20 is the ordinary parity partition (rows 2, 4, 6 against 1, 3, 5, 7), the only class with
boards at width 21. Stored results: 19 of 19 UNSAT at widths 17 to 20 with CaDiCaL.

| Width | CaDiCaL: UNSAT classes | Glucose: UNSAT classes | Both solvers | Proof log checked |
|---:|---|---|---|---|
| 12 | 19 of 19 | 19 of 19 | 19 of 19 | no |
| 13 | 19 of 19 | 19 of 19 | 19 of 19 | no |
| 14 | 19 of 19 | 19 of 19 | 19 of 19 | no |
| 15 | 18 of 19 (class 20 hit the 120 s limit) | 19 of 19 | 18 of 19 | no |
| 16 | 17 of 19 (classes 20 and 25 not run) | 17 of 19 (same) | 17 of 19 | no |
| 17 | not run | not run | 0 | no |
| 18 | not run | not run | 0 | no |
| 19 | not run | not run | 0 | no |
| 20 | 1 of 19 (class 0, 332 s) | 2 of 19 (classes 0 and 1, 483 s and 786 s) | 1 of 19 | no |

No instance returned SAT. Incidents (`struct_incidents.jsonl`):

- Class 20 at width 20 with CaDiCaL did not finish in 1200 s. This is a timeout, not an answer.
  The stored run needed at most 120 s per class, with its stronger caps at window lengths 12 to 14.
- Class 20 at width 20 with Glucose was aborted by hand after a few seconds to save budget.
- The last loop (widths 12 to 17) was stopped by the system for low memory during width 16 and was
  not restarted.

### 4.3 Proof logs

DRAT logging was switched on for the 188 window instances. The logs total 2.39 GB. Logs above
2 MB were deleted after recording size and SHA-256 in `window_results.jsonl`. The 62 logs that
remain in `proofs/` (with their CNF files) are all for window lengths 7 and 8. **No log was
checked**: no DRAT checker was installed, and the one attempt to build `drat-trim` was not
completed. No log was produced for a height-7 `struct` instance, because without a checker a log of
that size would only have been hashed and deleted.

### 4.4 Sanity checks of the encoder

All from `sanity_small_heights.jsonl`, both solvers, identical answers.

| Case | Result |
|---|---|
| `struct`, height 4: width 5, width 6 | all 3 partitions UNSAT; 2 of 3 SAT. So `m_0(4) = 6`. |
| `struct`, height 5: width 7, width 8 | all 10 UNSAT; 1 of 10 SAT. So `m_0(5) = 8`. |
| `struct`, height 6: width 14, width 15 | all 10 UNSAT; 1 of 10 SAT. So `m_0(6) = 15`. |
| `direct`, height 4: 9 cells at width 5, 10 cells at width 6 | UNSAT, SAT. |
| `direct`, height 5: 13 cells at width 7, 14 cells at width 8 | UNSAT, SAT. |
| `direct`, height 6: 23 cells at width 14, 24 cells at width 15 | no answer within 300 s and 200 s. |

Every SAT model passed the brute-force check. The `direct` runs at heights 4 and 5 use no
structure theorem and agree with the `struct` runs. A `direct` run at height 7 was not attempted.

At height 7 the encoder with caps, without the reflection break, accepts each of the four stored
`7 x 21` boards when the board is fixed and the partition is class 20, and rejects them for a
wrong partition (`acceptance_results.jsonl`). A free search for a width-21 board was not run.

## 5. Statement (ii): fully checked

`verify_boards.py` (no solver, 2.5 s, output `verify_boards.json`) checks by direct enumeration of
all rectangles, with two generators that agree:

- the four stored `7 x 21` boards are valid equality boards with 33 cells;
- for every `m` from 21 to 60, the prefix of length `m` of

  ```
  16,36,5,25,2,2,14,7,12,27,2,7,67,7,47,7,7,56,45,34,23,1,1,1,2,2,2,...
  ```

  is a valid equality board with `m + 12` cells (each width checked on its own rectangle list);
- the width-60 prefix has no entirely black rectangle, and its columns 25 to 60 are singleton row 2;
- every tilted rectangle of height at most 7 spans at most 10 columns;
- the stored 31-cell board of width 20 is valid.

**Widths above 60.** I read the argument in `seven_row_equality_tail.md` and found no gap. A
shorter version, which uses only the finite facts above, is this. Let `m > 60` and suppose two
distinct rectangles of the length-`m` prefix have the same white corners.

1. *Both axis-aligned.* Impossible in any board whose columns have at most two cells, with
   distinct, bipartite double pairs. If they share a vertical or a horizontal side, two columns
   carry the same pair. If they share one corner, the three or two columns involved carry a
   repeated pair, a triangle of pairs, or three cells. If they share nothing, both are entirely
   black, and again a pair repeats.
2. *Both tilted.* An entirely black tilted rectangle either lies in columns 1 to 60 (excluded by
   the check) or lies in the constant region, where all black cells are in one row. So the common
   white set is not empty, the rectangles share a corner, and together they span at most 21
   columns. If they reach beyond column 60 they lie in columns 41 onward. Shift both left by a
   whole number of columns until they lie in columns 25 to 60. The region is constant, so colors
   are unchanged, and the shifted pair is a collision in the width-60 board. Contradiction.
3. *One tilted (`R1`), one axis-aligned (`R2`).* The common white set `W` is not empty, because
   `R1` is not entirely black (step 2), and it has one or two cells. If `W` is a diagonal or a horizontal side of `R2`, then `R2` lies in the columns
   of `R1` and step 2 applies. Otherwise `R2` has `W` in one column and two black corners in
   another column, which is a double and so one of columns 1 to 21. If `R1` reaches beyond column
   60, shift `R1` left inside the constant region and move the column of `R2` that contains `W`
   with it. Colors are unchanged and the pair lies in the width-60 board. Contradiction.

Hence every prefix of length at least 21 is a valid equality board, and `f(7,m) = m + 12` for
all `m >= 21`, given the paper's upper bound.

## 6. Status of each statement

| Statement | Stored evidence | This folder | Status |
|---|---|---|---|
| Boards at widths 21 to 60 | brute force | brute force, new code | checked twice, no solver involved |
| Boards at all widths above 60 | written proof | proof re-read, shorter variant in section 5 | proved |
| 31-cell board at width 20 | brute force | brute force | checked twice |
| No equality board, widths 12 to 14 | window theorem | new encoder, two solvers | two independent routes, no checked proof log |
| Widths 15 and 16 | window theorem | new encoder, two solvers, classes 20 (and 25 at width 16) open | stored route complete, new route partial |
| Widths 17 to 19 | one CaDiCaL run per class | nothing | **single run** |
| Width 20 | one CaDiCaL run per class | class 0 with two solvers, class 1 with Glucose | **single run for 17 of 19 classes** |
| `m_0(4) = 6`, `m_0(5) = 8`, `m_0(6) = 15` | paper | reproduced | agree |

## 7. What it would take to finish

- Measured cost with this encoder: about 5.5 min per class with CaDiCaL and 8 to 13 min with
  Glucose at width 20, more than 20 min for class 20. A full pass at width 20 is of the order of
  2 to 4 hours per solver when run one process at a time. Window bounds at lengths 12 to 14 would
  shorten this, but the first attempt at length 12 did not finish in 280 s.
- Resume with `sh run_width.sh 20 cadical195 3600` (it runs all 19 classes; results append to
  `struct_results.jsonl`), then widths 19, 18, 17, and classes 20 and 25 at widths 15 and 16.
- Build a DRAT checker, re-run the window instances (10 min) with the 2 MB limit in `run_one.py`
  raised, and check the logs. Log the `struct` instances the same way.

Compute used: about 3 hours, one process at a time.
