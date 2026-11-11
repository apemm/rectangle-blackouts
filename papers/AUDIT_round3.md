# Audit, round 3

Scope: four new pieces of mathematics, checked from the definitions in each paper.

1. Extremal paper, Proposition `prop:partial`, Corollary `cor:everywidth`, Theorem
   `thm:threshold` after the restructuring, Remark `rem:constants`.
2. Extremal supplement, the section "Seven rows from width 21" (Lemma S2, `lem:tail`).
3. Enumeration paper, Theorems `thm:regular` and `thm:rational`.
4. Enumeration paper, Theorem `thm:fourgfexact` and `anc/four_row_certificate.py`.

Line numbers refer to the working tree files `extremal/sections/sec5_threshold.tex`,
`extremal/supplement.tex`, `enumeration/sections/sec7_height.tex`, and
`enumeration/sections/sec5_four.tex`.

## Verdicts

| Item | Verdict |
|---|---|
| 1. Partial edge sets, every width, threshold, constants | Correct with fixable gaps. No error in the mathematics. One unstated use of the size of `c_0`, and wording issues. |
| 2. `f(7,m) = m + 12` for `m >= 21` | Correct. One citation states less than the proof uses. |
| 3. Fixed height: regularity, periodicity, rationality | Correct. No gap found. It uses no large-width result. |
| 4. Four-row generating function and certificate | Correct with fixable gaps. The exactness argument is sound and the script checks what the paper says. The sentence on the numerator omits two terms of the bound. |

No statement in the four items is wrong.

## Item 1. Extremal paper, Section 5

### What I checked by reading

Every step below was checked by hand from the definitions.

- **Dependencies.** Lemmas `lem:rival`, `lem:sea`, `lem:chain`, `lem:count`,
  `lem:onedouble`, `lem:placement`, `lem:block`, `lem:reduction`, and `lem:criterion`.
  I rechecked the counts `768 tau*` and `12288 tau*`, the bound
  `(2^14 tau* + 1)^2 <= 2^30 tau*^2`, the total `2^30 tau*^2 + 8 tau* + 44000 tau* <= 2^31 tau*^2`,
  and the local lemma sum `6 c_1 / c_0 = 1/8`. The local lemma is applied correctly. The
  product in the display on lines 274 to 275 includes `L' = L`, which only makes the
  right side smaller.
- **Proposition `prop:partial` (a), (b).** `g = h` or `g = h - 1` is even with
  `2g - 1 > h`. For `g = h` the range of `j` in Definition `def:good` is empty, so every
  parity edge is good. `N = M` is an integer with `N >= c_0 n tau*^2`. The configuration
  `B` is well defined because (B1) fails for every pair, and for `n = 1` because
  `0` is not in `A_e`. Lemma `lem:block` applies with `I = Z`. The doubles are the `n`
  columns `X_e` with `1 <= X_e <= M <= m`, so the blackout has `m + n` points and all
  doubles are inside. Truncation to the columns `1..m` keeps validity, because a
  rectangle of the grid is a rectangle of the strip, so an obstruction in `S` is an
  obstruction in `B`.
- **Proposition `prop:partial` (c).** `g = h - 3` needs `2h - 7 > h`, which holds for
  `h >= 9`. The claim on lines 369 to 382 is right in every case: `r = h`; `r >= 3` with
  `h - r = 4u^2` and `s <= h - 3`; `r = h - 4u^2` with `s = h - 1`. The three numbers
  `4u^2 - 2`, `2(4u^2 - 1)`, `12u^2` are not squares. The intervals satisfy
  `I_{k+1}` starts 1 column after `I_k` ends, `z` is the first column of `I_3`, and
  `U_k` is inside `I_k` with a margin of `2W_h` on each side. Hence an obstruction that
  meets `U_k` lies in `I_k`. Outside the `U_k` the black points form a chain. The width
  is `N_1 + ... + N_4 + 24 W_h <= c_0 (n+4) tau*^2 + 6h^2`, and the `+4` for the ceilings
  is not needed, since `c_0 tau*^2` is an integer.
- **Corollary `cor:everywidth`.** All ranges:
  - `n = 0`: the claim is `f >= m`, which is Lemma `lem:cross`. That lemma has no
    restriction on `m`, so `m = 1, 2` are covered.
  - `n >= 1` and `h <= 8`: then `m >= 2 c_0 >= 2 * 10^11`, and `M_8 = 211`, so
    `m >= M_h` and the full value `m + q_h >= m + n` holds. Partial edge sets are never
    needed for `h <= 8`, and no width below the first double occurs with `n >= 1`.
  - `h >= 10` even: (a), with `M = c_0 n tau*^2 <= m`.
  - `h >= 9` odd, `n <= q_h / 2`: (b). The count of good edges is right: an edge is
    good for `h - 1` if and only if `r <= h - 2` and (`r = 1` or `h - r` is not a
    square). There are `(h-1)/2` odd rows `r <= h - 2`, at most
    `floor(sqrt(h-1)/2) < sqrt(h)/2` of them are bad, and `h - 3 >= 2 sqrt(h)` holds
    from `h = 9`, with equality there.
  - `h >= 9` odd, `n > q_h / 2`: (c). The display on lines 447 to 450 is right and
    needs `c_0 >= 82`.
  - `C' = 2 c_0` is right in every case.
- **Theorem `thm:threshold`.** It follows as stated. Existence of `m_h` is Proposition
  `thm:general`. Part (a) is Corollary `cor:small-m`. Part (b) for `h >= 9` is
  `prop:partial` (a) or (c) with `n = q_h`, and for `h <= 8` it is `M_h` with a larger
  constant.
- **Remark `rem:constants`.** `c_0 = 48 * 2^31 = 3 * 2^35 = 103079215104`.

### Gaps and remarks

1. **Line 437, "If `h <= 8`, then `m >= M_h`".** This uses `2 c_0 >= M_8 = 211`, that is
   `c_0 >= 106`. The proof never says so. The only size it states is `c_0 >= 100`
   (line 451), which is not enough for this step. With `c_0 = 3 * 2^35` the step is
   true. Fix: write "since `2 c_0 >= 211 = M_8`" on line 437, or say once that
   `c_0 >= 106` is used.
2. **Lines 428 to 431, proof of `thm:threshold` (b).** The constant `C` for `h <= 8`
   is not named. The bound has `+5` where the proposition gives `+4`. Both are harmless.
   Fix: "for `h <= 8` take `C >= M_8`", and `+4`.
3. **The corollary is weaker than Lemma `lem:cross` on a large range.** The boundary
   cross gives `f >= m + h - 1`. The corollary gives more only when
   `floor(m / (C' tau*^2)) >= h`, that is from `m >= 2 c_0 h tau*(h)^2`. For `h <= 8` it
   says nothing beyond Proposition `thm:general`: for `M_h <= m < 2 c_0 tau*^2` it
   states `f >= m`, while `f = m + q_h`. This is not an error. A referee will ask for
   it to be said. Fix: state the bound as
   `m + max(h - 1, min(q_h, floor(m / (C' tau*^2))))`, or add one sentence.
4. **Introduction, lines 62 to 63 of `sec1_intro.tex`:** "we let every singleton be
   black in one of 2 fixed rows". For odd `h >= 9` the construction uses the rows
   `1, h-1, h-3, 2, 4, h`. The first paragraph of Section 5 says it correctly ("of a
   long block of columns"). Fix the introduction in the same way.
5. **Remark `rem:constants`, crossover.** The number is right, with one caveat. With
   the bound `c_0 (q_h + 4) tau*^2 + 6h^2 + 5` of the proof, the first `h` with bound
   `< M_h` is `710132287759`. The comparison is not monotone, because `tau*` jumps:
   the bound is again `>= M_h` for some `h` up to `757474440275`, and it is `< M_h` for
   every larger `h` that I tested (up to `10^13`). So "only for `h` larger than about
   `7 * 10^11`" is correct. Do not change it to "for every `h` larger than".
6. **`sec7_verify.tex`, lines 14 to 16:** "For `h = 5` and `h = 7` these use the layout
   of Proposition `prop:partial`(c) with the sea rows `{1,h-1}` and `{2,h}` only". Part
   (c) is stated for `h >= 9`. The two-block variant is true for `h = 5, 7`, since
   there every edge `e` has `e` or `rho(e)` good for `h - 1` (I checked both heights),
   and the proof of (c) with the blocks 1 and 3 goes through. No proof in the paper
   covers it. Fix: say "a variant with 2 blocks", and that it is checked by computer
   only.
7. **Abstract:** "for `h = 7` and `m >= 24`" while Remark `rem:seven` gives `m >= 21`.
   Cosmetic.

### What I checked by computation (`audit_round3.py`)

- `good`: for odd `h = 9..1201`, at least `q_h / 2` parity edges are good for `h - 1`.
  The smallest share is `0.6` at `h = 9`. For odd `h = 9..401`, every parity edge `e` has
  one of `e`, `rho(e)` good for `h - 1` or `h - 3`. For even `h = 4..40`, every parity
  edge is good for `g = h`.
- `partial`: I computed `A_e` from Definition `def:good` by listing all private corner
  triples and mixed quadruples in the columns `-2W_h..2W_h`. I then built the blackout
  of the proposition and tested it against Definition `def:valid`.
  - Cases (a), (b): `h = 4..10`, random sets of `1` to `5` good edges, 228 boards, at
    the widths `m = ` (column of the last double), a random larger width, and a width
    past the last gadget. The free columns are black in row `1`, as in the proposition,
    and also in random rows from `{1, g}`, as Lemma `lem:block` allows. All valid, all
    with `m + n` points.
  - Case (c): `h = 9`, 14 boards with `1` to `6` doubles in `1` to `4` blocks, including
    empty blocks and the edge `{5,8}`, which is the only edge of class 4. All valid.
  - Controls: an edge that is not good, a board with sea rows `1, 9, 1`, are found not
    valid.
  - Limit of this test: the doubles are `4W_h + 1` apart, so no set of columns is bad
    for a trivial reason. The test covers Lemmas `lem:sea`, `lem:chain`,
    `lem:onedouble`, `lem:reduction`, the block layout of (c), and the truncation. It
    does not test (B1) to (B3) on doubles that are close.
- `seas`: Proposition `thm:general` for `h = 3..8` at `m = M_h`, `M_h + 1`,
  `M_h + W_h + 3`, and Lemma `lem:cross` for `h = 3..8`, `m = 1..7`.
- `const`: the arithmetic of `c_1`, `c_0`, the inequalities `2 c_0 >= M_h` for
  `h <= 8` and `c_0 (q_h/2 - 4) >= 6h^2 + 4` for odd `h = 9..3999`, and the crossover
  with exact integers and the record holders of the divisor function up to `10^27`.

### Not verified

- The existence statement of Lemma `lem:placement` is verified by reading only.
- Boards with close doubles, the greedy widths `1180, 1872, 2154, 2919`, and the
  `h = 16` experiment of the remark. I did not rerun `check_constructions.py`.
- The citations (Alon and Spencer, Hardy and Wright, Wigert, Henriot).

## Item 2. Supplement, seven rows from width 21

### By reading

The case argument is complete. I checked each case.

- The board has `21 + 3 + 21 = 45` columns. The 12 doubles are in the columns `1..21`
  and carry the 12 pairs of an odd and an even row.
- `m <= 45`: `T_m` is a restriction of `T`.
- `m > 45`, at most 1 common corner: both rectangles have 3 or more black corners. The
  columns from `25` on are black only in row 2, and a tilted rectangle has at most 2
  corners in one row. So a tilted one has a black corner in a column `<= 24`, and lies
  in the columns `1..34`. An axis-aligned one is not
  fully black, so it shares a corner with the tilted one, and its other column is a
  double.
- 2 common corners, side of both or diagonal of both: `R_3` is fully black and tilted.
  The argument for an axis-aligned `R_i` is right: `pq` cannot be a side of a tilted
  rectangle and of an axis-aligned one.
- Mixed pair, `AB` not vertical: if no point of the support is in a column `<= 24`,
  the support is in row 2, and `R_1` is degenerate.
- Mixed pair, `AB` vertical: `A, B` form a double, the rows of `p, q` have different
  parity, and a support in row 2 would give the rows `1` and `3`.
- In every case both rectangles lie in the columns `1..44`, so the width `45` is
  enough.

### Gap

1. **Line 174, "both rectangles lie in 21 consecutive columns (Section 5.1 of the
   paper)".** Section 5.1 states this only for the 4 points of the support. The lemma
   needs it for both rectangles, including `p` and `q`. It is true by the same three
   cases (both tilted share `p`; `R_2` axis-aligned has the columns of `p, q`; `R_1`
   axis-aligned with `pq` horizontal has the columns of `p, q`). Fix: add "and so do
   both rectangles" to the paragraph in Section 5.1, or give the three cases in the
   supplement.

### By computation

- `tail`: with my own enumerator, which lists every rectangle of the `7 x 70` grid
  from the definition (56255 rectangles), `T_m` is valid with `m + 12` points for
  every `m = 21..70`. This includes the required widths `21..45`.
- A second test, with a different enumeration, gives valid for
  `m = 21..25, 33, 44, 45, 46, 60, 100, 150`.
- Control: with row 2 directly after column 21 the board of width 45 is not valid. So
  the 3 columns in row 1 are needed, as the remark says.

### Not verified

- The upper bound is the row bound, which I did not audit again.

## Item 3. Enumeration paper, fixed height

### By reading

No large-width result is used. The proofs use Lemmas `lem:diff`, `lem:leftmost`,
`lem:span`, and `lem:girth` of the same paper.

- **Regularity.** A bounded window is not needed, and the proof does not use one. The
  automaton is nondeterministic. It guesses 2 traces `Y, Y'` and checks
  `Y_i triangle Y'_i subset B_i` letter by letter. An axis-aligned rectangle of any
  width needs only the letter `{r,s}` in the finite control. A tilted rectangle is one
  of finitely many words of length at most `W_h + 1`. The set of triples is an
  intersection of regular languages, the projection is a letter-to-letter image, and
  the complement is regular. This is sound.
- **Series.** `det(I - T(z,u))` has constant term 1, so the inverse exists.
- **Excess bound.** `|v| <= 2` gives `e(v) <= 2h - 2`. For `|v| >= 3` the converse of
  `lem:girth` applies, `sum binom(|B_i|, 2) <= binom(h, 2)`, and
  `|B_i| - 1 <= binom(|B_i|, 2)` holds also for `|B_i| = 0`. Factors of valid words are
  valid.
- **Counter.** For `w = uv` valid with `e(w) = k`, `k - c_h <= e(u) <= c_h`. The
  counter is finite. For `k > c_h` the language is empty, which is right.
- **Maximum.** Row 1 is a valid blackout (the argument given is right, also for
  `h = 1`), so `0 <= f(h,m) - m <= c_h`, and the maximum of finitely many ultimately
  periodic indicator sequences is ultimately periodic.
- **Optima and rationality.** The words of length in `D_k` form a regular language,
  the union over `0 <= k <= c_h` is finite, and a deterministic automaton gives the
  series.

### Gaps

None.

### By computation

None. No step of this proof is computational.

### Not verified

- The remark that part (a) follows from Guilhot, Little, and Parkinson, Theorem 1(3).

## Item 4. Enumeration paper, four-row generating function

### By reading

- **One index is enough.** `u_F(n+1) = T_F u_F(n)` for the vector over all states. So
  `sum_j q_j u_F(n+1-j) = T_F sum_j q_j u_F(n-j)`. If the vector is `0` at `n = 445`,
  it is `0` for every `n >= 445`. A check of the start coordinate alone would not give
  this. The vector check does. The indices `445 - j` run from `25` to `445`, so only
  `u_F(n)` with `n >= 25` occur, and `a_F(n) = ` number of optima holds there.
- **Entry bound.** There are 8 letters, so every entry of `u_F(n)` is in `[0, 8^n]`,
  and every entry of `R_F` has absolute value at most `8^445 sum |q_j|`. Right.
- **From the recurrence to `P_4 / Q_4`.** For `n >= 445` the coefficient of `z^n` in
  `Q_4 * sum_{m >= 6} a_4(m) z^m` is the recurrence, since `n - j >= 25 >= 6`. For
  `n <= 444` the script compares with `P_4`. The failure at `444` is
  `P_444 = 2^49`, not `0`.
- **Script against Proposition `prop:fourautomaton`.** The state is the last 6 letters
  and the set of pairs read. A letter is rejected if its pair was read. The test
  `ok(word)` looks at the tilted rectangles with their last corner in the new column,
  rejects a hidden one, one with a rival (the four cases of Lemma `lem:rival`, with the
  full pair set `F`), and one with the presentation of another tilted rectangle of the
  window. The script compares presentations only when at most 2 corners show. This is
  the same condition, by Lemma `lem:threecorners`. Acceptance is `U = F`.
- **Arithmetic.** Products are below `2^62` and fit in 64 bits. `exact()` forms
  `sum_j q_j u_F(445 - j)` and the numerator for each prime, and requires
  `len(P) = 445`.

### Gaps

1. **Lines 172 to 173, "In the same way the script checks that the product ... agrees
   with `P_4`".** The bound of the previous sentence does not cover this. A coefficient
   of the product is at most `3 * 8^444 sum |q_j|`, with the factor 3 for the 3 pair
   sets, and the difference to `P_n` adds `max |P_n|`. The script does handle it: its
   bound is `max(6 * 8^445 sum|q_j|, 2 max|P_n|)`, and I checked that the product of
   the 48 primes exceeds `2 (3 * 8^444 sum|q_j| + max|P_n|)`. Fix: one sentence in the
   proof with this bound.
2. **Line 163 to 165.** The proof should say that `a_F(n)` counts optima only for
   `n >= 6`, and that the recurrence at `n >= 445` uses only `n - j >= 25`. It is true
   and one clause is enough.
3. **Docstring of the script, lines 5 to 19.** It says the script "works modulo two
   primes" and then that `exact()` uses enough primes. This agrees with the paper,
   which speaks of 48 primes. No change needed, but the first sentence can mislead.

### By computation

- I ran a copy of `four_row_certificate.py` outside the repository. It finished in
  289 seconds. Output: `60975`, `138095`, `55575` states; the vector identity first
  holds at index `445` for each pair set; `number_of_primes = 48`;
  `bits_of_product = 1488`; `bits_of_bound = 1458`; `vector_identity_exact = true`;
  `numerator_exact = true`. These agree with the stored
  `four_row_certificate.json` and with the paper.
- `four`: from `four_row_gf.txt`, `deg P = 444`, `deg Q = 420`, `Q(0) = 1`,
  `P_444 = 2^49`, `P_6 = 26`, `P_7 = -826`. The series of `P/Q` gives
  `a_4(6..13) = 26, 292, 2118, 13332, 75398, 402656, 2037848, 9894016`, as in the table.
- `sum |q_j|` has 120 bits. `2 * 8^445 sum|q_j|` has 1456 bits, and the product of the
  48 largest primes below `2^31` has 1488 bits. So the claim "less than half the
  product" holds. For the bare bound of the paper 47 primes would do. The script uses
  a bound that is 3 times larger, which is why it takes 48.
- SymPy factors `Q` with (degree, multiplicity) =
  `(1,2), (1,2), (5,3), (5,3), (6,3), (11,5), (17,3), (19,3), (20,5), (21,5)`. The
  polynomials `g_5`, `g~_5`, `g_6`, `g_20` of the theorem are among the factors.
  `gcd(P, Q) = 1`.
- Independent count: for `m = 6, 7, 8, 9` I tested every candidate (4 doubles on a
  4-cycle of rows, singletons elsewhere) against Definition `def:valid` with my own
  enumerator. The counts for the pair sets of `12|34`, `13|24`, `14|23` are
  `0, 20, 6`; `4, 256, 32`; `128, 1780, 210`; `920, 11128, 1284`. They equal the counts
  of the automata in the certificate. This uses the imported equality structure to
  restrict to candidates.

### Not verified

- Corollary `cor:fourgrowth` (root isolation, the constant `c`).
- The degrees `162`, `153`, `107` of the three denominators.
- The counts of the automata for `m >= 10` against the definition.
- The Berlekamp-Massey step, which is not part of the proof.

## The checking script

`papers/audit_round3.py`, run as `py audit_round3.py [part ...]`. With no argument it
runs `enum tail good seas const four partial` in about 2 minutes. `four9` extends the
four-row count to `m = 9` and takes about 3 minutes.

| Part | What it covers |
|---|---|
| `enum` | The two rectangle enumerators give the same tilted rectangles on 5 grids, the number of axis-aligned rectangles is `binom(h,2) binom(m,2)`, the largest span is `W_h`, and the two validity tests agree on 4000 random blackouts. |
| `tail` | Item 2. |
| `good`, `partial`, `seas`, `const` | Item 1. |
| `four`, `four9` | Item 4, except the run of the certificate script. |
