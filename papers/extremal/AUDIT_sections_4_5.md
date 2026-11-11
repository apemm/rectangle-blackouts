# Audit of Sections 4 and 5 (Theorem 1 and Theorem 2(b))

Date: 2026-11-10. Files read: `sections/sec1_intro.tex`, `sec2_prelim.tex`, `sec3_rowbound.tex`,
`sec4_seas.tex`, `sec5_threshold.tex`. No other note in the repository was used as evidence.

## Verdicts

| Result | Verdict |
|---|---|
| Theorem 1 (`thm:general`, via Proposition `prop:seas`) | Correct. 3 presentation gaps, all fixable in one line each. No case breaks the spacing `W_h + 1`. |
| Theorem 2(b) (`thm:threshold`(b), Section 5) | Correct. 5 small gaps or imprecisions, all fixable. No missing bad event, and the local lemma hypothesis holds with the stated constants. |

I found no mathematical error in either proof. The lists below contain every point where a
sentence is unjustified as written, ambiguous, or weaker than it looks.

## How each part was checked

**By reading, line by line, from the definitions in the paper:**

- Section 2: Lemmas `lem:diff`, `lem:threecorners`, `lem:compress`, `lem:leftmost`, `lem:span`,
  `lem:facts`, `lem:mixedeq`, `lem:criterion`. Also `lem:girth` (forward direction), because
  `lem:criterion` uses it.
- Section 4: all of Proposition `prop:seas`, cases (a) to (f), statements (1) to (3), the 3 cases
  of condition (iii), and the arithmetic `1 + (q_h - 1)(W_h + 1) = M_h`.
- Section 5: every lemma and the final proof, including all constants
  (`768 + 12288 <= 2^14`, `(2^14 t + 1)^2 <= 2^30 t^2`, `2^30 t^2 + 8t + 44000 t <= 2^31 t^2`,
  `6 c_1 / c_0 = 1/8`, `24 W_h <= 6 h^2`), the odd-height claim, the block layout, and the
  restriction to columns `1..m`.

**By computation** (my own enumerator, described at the end): the items in the section
"Computational checks". These cover small heights only.

**Not checked:**

- Section 3 beyond one read of `lem:H`, `lem:mantel` and `thm:rowbound` (the upper bound
  `f(h,m) <= m + q_h`). I saw no problem, but I did not audit it at the same depth.
- The citation of the local lemma (Alon and Spencer, Lemma 5.1.1) against the book. I used the
  standard general form: `Pr(A_i) <= x_i * prod_{j ~ i} (1 - x_j)` with `0 <= x_i < 1`.
- Conditions (B2) and (B3) were never exercised by the computations (see check 7). They are
  verified by reading only.
- Remark `rem:sharper`, Remark `rem:check`, and Sections 6 to 9.

## Theorem 1: gaps and remarks

The case list for `K` is complete: `{u,v}`, `{(0,a),(0,b)}`, `{u,d}` opposite, `{u,d}` adjacent,
`{v,d}`, and `|K| >= 3`. I looked for a failure of spacing `W_h + 1` in these situations and found
none:

- Two rectangles that share 2 corners: all 3 cases of condition (iii) hold.
- A rectangle whose column range holds a double that is not at a corner column: this is case (a).
- Two different doubles: the only place where 2 doubles could matter is the "both tilted" step.
  There `D_2` lies strictly between the columns of `p` and `q`, both of which are in the column
  range of `R_1`. So `D_2` is a second double inside the column range of `R_1`, which spacing
  `W_h + 1` forbids. The spacing `2W_h + 2` is not needed.
- Ends of the grid: no step uses a column outside the column range of a rectangle.
- `h = 3`: in (a) the bound reads `|w_2| <= 0`, which still gives `w_1^2 > (x_2 - x_1)^2 / 4`.
  The contradiction in the axis-aligned case of (iii) needs `1 != h`, which holds.
- Parity of `h` plays no role. `H` may be any triangle-free graph.

1. **`sec4_seas.tex`, proof of `prop:seas`, sentence "It has span at most `W_h`, so its columns
   contain at most 1 double", and every later use of "the columns of `R`".** The phrase is not
   defined. The proof is correct only if it means all columns from the smallest to the largest
   column of `R`, not the at most 4 columns that hold a corner. With the second reading, the
   sentence "With no double, all black points in the columns of `R` lie in one boundary row" is
   false (a double strictly between 2 corner columns switches the sea row), and the final step
   "`D_2 != D_1` and `|D_2 - D_1| < W_h`" has no contradiction to reach, because `D_2` is not a
   corner column of `R_1`. Fix: define "the columns of `R`" as the interval of columns from its
   leftmost to its rightmost corner. The final step then shortens to: `D_2` lies in the columns of
   `R_1`, which contain only the double `D_1`, but `p` and `q` are on one side of `D_1`.

2. **Same proof, case (c), sentence "Since their rows are at least 2, we get
   `|w_2| <= (c-3)/2`".** For `c = 2` the right side is negative. The inequality is still a
   correct deduction, and it shows that the case cannot occur, but the text then continues as if
   the endpoints exist. No error results. Fix: add "in particular `c >= 3`".

3. **Same proof, case (d), "`n = t(-(c-1), |x_1|)` for some `t != 0`".** Here `t` is a rational
   number, not an integer. The argument uses only the sign of `t`, so it is correct. Fix: say
   "for some real `t != 0`".

Remark `rem:spacing` (spacing `W_h` fails for `h = 4` and `h = 6` in lexicographic order) is
confirmed by computation (check 3).

## Theorem 2(b): gaps and remarks

**Completeness of the bad events.** I traced every pair of distinct rectangles with equal
presentations:

- Both axis-aligned (including both fully black): excluded by the 4-cycle and 6-cycle argument in
  `lem:reduction`. Parity edges form a bipartite graph, and the row pairs are distinct.
- No common corner or 1 common corner (hidden rectangles included): one rectangle is tilted with
  at least 3 black corners. This is a corner triple.
- 2 common corners, side-side or diagonal-diagonal: `lem:compress` gives a fully black rectangle.
  This is a corner triple or a 4-cycle.
- 2 common corners, mixed, `AB` not vertical: a mixed quadruple.
- 2 common corners, mixed, `AB` vertical: `R_1` is axis-aligned, `A, B` are the 2 points of a
  double, and `{C, D}` is a rival pair. This is the only axis-aligned rival that the mixed
  quadruples miss, and it is covered.
- An obstruction that touches 0 doubles: `lem:sea` (inside a block) or `lem:chain` and `lem:rival`
  (odd-height background).
- 1 double: private obstructions, the sets `A_e`, the gadget, and `lem:onedouble`(c).
- 2, 3 or 4 doubles: (B2) and (B3). An obstruction has at most 4 points, so `|L| <= 4`.

**Probabilities and the local lemma.** Each pattern (type assignment plus translation class) fixes
all differences `X_e - X_{e_0}`, `e` in `L`, because every `e` in `L` occurs as a type. So each
pattern has probability at most `N^{-(|L|-1)}`. The pattern counts are at most `2^30 t^2` for (B1),
`8t` for (B2), and `11000 * 4t` for (B3), with `t = tmax(h)`. These give `p_2, p_3, p_4` with
`c_1 = 2^31`. With `x_L = 2 p_{|L|}` and `N >= 48 c_1 n t^2`, the sum of `x_L` over the sets that
contain a fixed edge is at most `1/8`, the sum over the sets that meet `L` is at most `1/2`, and
`x_L (1 - 1/2) = p_{|L|} >= Pr(E_L)`. The hypothesis of the local lemma holds.

**All widths.** The configuration `B` is defined on all of `Z`. For every `m >= N` (even `h`) or
`m >= M` (odd `h`), the set `S` is `B` cut to columns `1..m`. A subset of an obstruction-free
configuration is obstruction-free, every column of `S` is a singleton or a double, and all `q_h`
doubles are inside. So `|S| = m + q_h` and the claim covers every width above the threshold.

**Parity and small `h`.** `h <= 8` goes through Theorem 1. Even `h >= 10` uses `g = h`. Odd
`h >= 9` uses `g = h - 1` and `g = h - 3`, and `2(h-3) - 1 > h` needs exactly `h >= 9`. The
odd-height claim is correct: I checked each branch, including `r' = 1 + 4u^2 <= h - 2` and
`h - r' = 4v^2` with `s' = 2 <= h - 3`.

1. **`sec5_threshold.tex`, proof of Theorem 2(b), odd `h`, sentence "For `k = 1, 2` apply
   Lemma `lem:placement` to `E_k` ...".** Lemma `lem:placement` requires `n >= 1`, but a set
   `E_k` can be empty. For `h = 11` and `h = 13` the natural split has `E_4` empty (check 6). The
   definition of `N_k` already uses `max(|E_k|, 1)`, so the intent is clear. Fix: add "if `E_k` is
   not empty".

2. **Lemma `lem:block`, first sentence "Let `E` and `(X_e)` be as in Lemma `lem:placement`".**
   The lemma uses only that no `L` with `2 <= |L| <= 4` is bad. It does not use `N` or the range
   `{1..N}`. In the odd case the lemma is applied to the translated columns `x_e = s_k - 1 + X_e`,
   which are not in `{1..N_k}`. The sentence after the lemma covers this ("do not change if all
   columns are translated"), so there is no error. Fix: state the hypothesis as "a set of parity
   edges good for `g` and columns `X_e` such that no `L` is bad".

3. **Lemma `lem:block`, proof, case `L = {e}`, sentence "the corresponding point of `Q` lies in
   column `X_e + a`, to which (2) applies".** This needs 2 facts that the proof does not state:
   column `X_e + a` is not a column `X_f` (true because `f` would be in `L`), and it is not
   `X_f + a'` with a different rule (true because (B1) fails). Both are in the paragraph before
   the proof. No error. Fix: refer to that paragraph.

4. **Lemma `lem:placement`, proof, bound for (B3), sentence "By Lemma `lem:count`, there are then
   at most `4 tmax` choices of `Q` up to horizontal translations".** `lem:count` counts ordered
   tuples with a marked right angle (triples) or a marked side and diagonal (quadruples). The
   union bound therefore runs over ordered tuples with typed points, and each unordered `Q` is
   counted at least once. The proof says "order the points of `Q` as in `lem:count`", which is
   enough, but it does not say that a point of type `(e, c)` and a point of type `(e, c')` in
   different columns give probability 0. The bound `N^{-(|L|-1)}` holds in every case. No error.

5. **Section 5.1, sentence "The points of an obstruction always lie in `2W_h + 1` consecutive
   columns", case "If `R_1` is axis-aligned and `pq` is not vertical, then `pq` is horizontal".**
   Correct, but the case `R_1` axis-aligned with `pq` vertical is silently moved to the rival
   pairs. For a rival pair the statement holds because `C, D` are corners of the tilted `R_2`.
   The text says this in the sentence before, so this is a remark on order only.

Two remarks outside the proof:

- **Remark `rem:check`** says that blackouts were built for `4 <= h <= 13`. The proof of
  Section 5 defines the odd construction only for `h >= 9`, because `g = h - 3` needs
  `2g - 1 > h`. For `h = 5` and `h = 7` every parity edge or its reflection is good for
  `g = h - 1` (check 6), so the pairs `{1, h-1}` and `{2, h}` suffice there, but the remark should say which
  construction was used for odd `h < 9`.
- **Introduction, sentence "A confusion between 2 rectangles needs 3 or 4 black points in a
  special position".** A rival pair has 2 points (plus the double). Wording only.

## Computational checks

All checks use my own code. Rectangles are generated from the definition: axis-aligned rectangles
directly, and tilted rectangles from a corner `p`, a side `u`, and a perpendicular side
`k(-u_2, u_1)/gcd`. The bound `|u_1| <= (h-1)^2` used in the loop does not rely on `lem:span`.
The script is `scripts/audit_sections_4_5.py`.

A pass on small `h` does not validate an asymptotic proof. These checks only fail to refute.

1. **Enumerator and validity checker.** On the `3x5`, `4x6` and `5x5` grids, the generated
   rectangles equal the set of all 4-subsets of points that form a rectangle (33, 110, 130). The
   fast validity checker compares only rectangles with at least 2 black corners (justified by
   `lem:threecorners`). It agrees with a naive checker that compares all presentations on 900
   random blackouts. The largest span of a tilted rectangle equals `W_h` for `3 <= h <= 11`.
2. **Proposition `prop:seas`.** 604 configurations for `3 <= h <= 8`, all valid, all with
   `m + q` points. They include the complete bipartite graph on every balanced bipartition for
   `h <= 5` and on 12 bipartitions for `h = 6, 7, 8`, with spacing exactly `W_h + 1`, the first
   double in column 1, random edge orders, and widths `M_h`, `M_h + 1`, `M_h + W_h + 2`. They
   also include random triangle-free graphs (not always bipartite) with random spacings
   `>= W_h + 1` and random margins from 0.
3. **Remark `rem:spacing`.** With spacing `W_h`, the lexicographic order on rows `1..h/2` versus
   the rest is invalid for `h = 4` and `h = 6`, and valid for `h = 3, 5, 7`. With random orders,
   spacing `W_h` is invalid in 40 of 40 trials (`h = 4`), 12 of 40 (`h = 5`), 36 of 40 (`h = 6`),
   21 of 40 (`h = 7`), and 0 of 40 (`h = 3`).
4. **Lemmas `lem:sea`, `lem:chain`, `lem:rival`, `lem:count`, and the `2W_h + 1` claim**, for
   `3 <= h <= 11`, over all corner triples, mixed quadruples and rival pairs up to horizontal
   translation (built from Definition `def:mixed`, not from `lem:mixedeq`). No obstruction lies in
   rows `{1, g}` for an even `g` with `2g - 1 > h`. For even `g` with `2g - 1 <= h` such
   obstructions exist, so the hypothesis is needed. No corner triple or mixed quadruple is a
   chain. Every rival pair satisfies the conclusions of `lem:rival`. The counts in `lem:count` are
   at most half of the stated bounds. The largest width of a mixed quadruple is `W_h + 2` columns.
5. **Lemma `lem:onedouble`** for even `h = 4, 6, 8, 10, 12` with `g = h` (all parity edges), and
   for `h = 9, 11, 13` with `g = h - 1` and `g = h - 3` (all good edges). No private obstruction
   lies inside a gadget, and no rival pair joins a double point and a point in row 1 or `g`. The
   largest `|A_e|` is 18 for `h = 8` and 32 for `h = 11`, against the bound `2^14 tmax(h)`. The
   largest `|a|` is 12 for `h = 8` and 30 for `h = 13`, within `2W_h`.
6. **Odd-height claim.** For every odd `h` from 9 to 301 and every parity edge, one of `e`,
   `rho(e)` is good for `h - 1` or `h - 3`. No failure.
7. **Whole construction, validity from Definition `def:valid`.** Even `h = 4, 6, 8, 10, 12`
   (`g = h`): 6 or 7 random placements each that are not bad for any `L`, in a short window, then
   4 blackouts per placement (free singletons all in row 1, all in row `g`, or random; widths
   `max X_e`, `N`, `N + 7`, `N + 2W_h + 3`). Odd `h = 9, 11, 13`: 4 placements each of the
   4-block layout exactly as in the paper, at widths `M` and `M + 3W_h`. All 150 or so blackouts
   are valid and have `m + q_h` points. Widths went up to 3317.
   - Control with teeth: when the prescriptions on `X_e + A_e` are dropped, every tested
     blackout is invalid (4 to 82 collisions). So the sets `A_e` and the gadget rule are tested.
   - Control without teeth: in about 9000 candidate columns for `h = 8, 10`, every candidate
     that met (B2) or (B3) also met (B1). At these heights the sets `X_e + A_e` keep the doubles
     so far apart that (B2) and (B3) never decide anything. So check 7 does not test (B2), (B3),
     or the `|L| >= 2` branch of `lem:block`. Those rest on reading alone.
