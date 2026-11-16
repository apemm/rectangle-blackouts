# The quadratic threshold: findings of a second attack

11 November 2026. Problem 001, fixed height `h`, least equality width `m_h`.

**Outcome. `m_h = O(h^2)` is not proved here, and no lower bound above
`q_h = floor(h^2/4)` is proved either.** This note records what the attack
found, so that the next attempt does not repeat it. It ends with the exact
steps where I am stuck.

Status labels:

- **[proved]**: a complete argument is given here. Nothing in this note has
  had an independent audit.
- **[rechecked]**: a statement from my working notes of 10 November that I
  derived again today.
- **[working notes]**: a statement from those notes that I did not derive
  again. Treat it as a claim to check.
- **[heuristic]**: a count with no proof.

Notation. Rows `1..h`. A label is a parity edge `{a, b}`, `a` odd, `b` even.
Write `a = 2i+1`, `b = 2j+2`, so `0 <= i < A` and `0 <= j < K`, where `A`
and `K` are the numbers of odd and even rows. The offset of a label is
`T = b - a`, an odd integer. `Lambda = 1 + log h`.

## 1. Where the problem stands

- The extremal paper proves `q_h <= m_h <= C h^2 tau*(h)^2`
  (`papers/extremal/sections/sec5_threshold.tex`). The proof gives every
  double a private set of sea columns and uses the local lemma.
- The archive has `m_h <= C h^2 Lambda^2 (log log h)^C`
  (`research_archive/2026-11-09/CLAIM_LEDGER.md`, row T1). It depends on a
  cited divisor-moment theorem.
- Private blocking sets cannot do better than `h^2 Lambda^2` (row T11).
- Vertical rivals alone can be excluded in width `O(h^2)` (row T29,
  `full_problem_push/global_P_linear_coloring.md`). The proof colors the
  labels with `O(h)` colors. Color `c` is a block of width `O(h)`, and the
  label `(a, b)` sits at column `2(a-1) + P c`.
- That coloring does not give a valid board. A block can contain a hidden
  tilted rectangle (row T30). No fixed list of block colors per label can
  prevent this (row T17).

So an absolute bound needs a coloring that respects the geometry, and a sea
that fits it.

## 2. Which right angles survive in the one-prime scaffold [rechecked]

Put the label `(i, j)` with color `c` at column `x = 4i + 4p c`, with `p`
a prime greater than `10h`. Call a black point odd or even by its row.
Write a right angle as (vertex; end, end).

- (O; O, O): the dot product is `20 (i1-i0)(i2-i0)` modulo `p`, so one leg
  is horizontal and the angle is axis-aligned.
- (O; O, E): the dot product is
  `2 (i1-i0)(8 i2 + 2 j2 - 10 i0 + 1)` modulo `p`. The bracket is odd and
  smaller than `10h` in absolute value, so again a leg is horizontal.
- (O; E, E) and (E; O, O): the dot product is odd.

So every tilted right angle among label points has an even vertex and at
least one even end. Only two types remain: (E; E, E) and (E; O, E). This is
Section 1 of `global_P_remaining_geometry.md`. It holds for every coloring.

## 3. Monotone blocks

Call a block monotone if its labels, sorted by `i`, have nondecreasing `j`.

1. **A monotone block has no (E; E, E) angle. [rechecked]** The even points
   of the block form a chain, and a chain contains no tilted right angle
   (Lemma "chains" of the paper). In formulas the dot product is
   `16 d1 d2 + 4 e1 e2`, where `d` and `e` are the differences of `i` and
   `j`, and the two terms have the same sign.
2. **Monotone blocks need only about `h` colors. [rechecked]** The classes
   are chains in the grid of labels with distinct `i`. By Dilworth's
   theorem the least number of such chains is the largest antichain, which
   has `A + K - 1` labels. The diagonals `j - i = const` attain it.
3. **Across blocks, a right angle needs a steep leg inside one block.
   [proved]** Let the legs be `(X1, Y1)` and `(X2, Y2)`, so
   `X1 X2 = -Y1 Y2` and `|Y1|, |Y2| < h`. Two points in different blocks
   are more than `36h` columns apart. If both legs left the vertex's block,
   then `|X1 X2| > h^2 > |Y1 Y2|`. So one leg stays in the block of the
   vertex, and its slope is at least `36` in absolute value. If every block
   also has `|j - j'| <= 70 |i - i'|` for its labels (a Lipschitz
   condition), then no leg between two even points of a block is that
   steep. So monotone Lipschitz blocks exclude every (E; E, E) angle, in
   one block or across blocks.
4. **The remaining type inside a monotone block. [rechecked]** Let the
   vertex be the even point of label 0, the odd end belong to label 1, and
   the even end to label 2. Put `t1 = i1 - i0`, `t2 = i2 - i0`,
   `c2 = j2 - j0`, and let `T0` be the offset of label 0. The angle is
   right when

       8 t1 t2 = (T0 - 2 t1) c2.

   In a monotone block `c2` has the sign of `t2`, so `t1` lies strictly
   between `0` and `T0/2`. I call this the shadow of label 0. The fourth
   corner is in an odd row. So a pair of labels (0 and 2) forbids one
   position for a third label inside the shadow of label 0.
5. **Constant offset. [rechecked]** If all labels of a block have the same
   offset, then `c2 = t2` and the equation becomes `10 t1 = T0`, which is
   impossible because `T0` is odd. Such a block has no tilted right angle
   at all. But it must be short: see Section 4.

What this does not give. Rows T29 and T18 choose the labels of a block by
Hall's theorem or by a list coloring, one odd row at a time. That choice is
not monotone. I do not have a proof that `O(h)` blocks can be P-proper,
monotone and Lipschitz at once (Stuck step 1).

## 4. Collinear odd points cannot be dense

1. **A universal blocker. [proved]** In a block the odd points lie on the
   line `row = x/2 + const`. Let a label with offset `T` sit at slot `i`.
   The triple `(4, 3, 5)` scaled by `|T|` gives a vertical rival between
   its even point and the odd point at slot `i - T` when that slot is
   occupied: the horizontal distance is `4|T|`, the vertical distance is
   `|T - 2(-T)| = 3|T|`, and the diameter is `5|T|`. The rival exists when
   `5|T| <= h - 1` and both points are at least `|T|` rows from the top
   and the bottom. So a label with a small offset forces one slot of its
   block to stay empty, whatever the other labels are.
2. **Consequence. [proved]** A block whose slots are all occupied has a
   vertical rival as soon as it contains a label with offset `T`,
   `5|T| <= h - 1`, away from the boundary rows, and the slot `i - T`.
   So no dense order with long runs of collinear odd points is valid.
   This covers the Chinese remainder order and the skew orders of item 4.
3. **Constant-offset runs. [working notes]** A run with offset `T` has no
   vertical rival exactly when it is shorter than a number `x_min(T)`,
   with `x_min(T) <= |T|`, `x_min(T) = |T|/7` when `7` divides `T`, and
   `x_min(T) >= sqrt(2|T|)/8` always. Cutting the diagonals into such runs
   needs about `(K/2) log K` runs. With one block per run this gives width
   `h^2 log h`.
4. **Skew orders have no tilted right angle away from wraps. [proved]**
   Put slot `x` at column `s x`, with the label
   `(x mod A, lambda x mod K)`, where `s` is even, `lambda` is odd, and
   `gcd(A, K) = gcd(lambda, K) = 1`. Take three label points whose slots
   lie in a window where neither coordinate wraps. Then no three of them
   form a tilted right angle. Proof: with `d1, d2` the slot differences
   from the vertex and `T0` the offset of the vertex label, the eight
   types give
   - (O; O, O): `(s^2 + 4) d1 d2`, not zero.
   - (E; E, E): `(s^2 + 4 lambda^2) d1 d2`, not zero.
   - (O; E, E) and (E; O, O): an odd number.
   - (O; O, E): `d1 ((s^2 + 4 lambda) d2 + 2 T0)`. The first bracket is
     `0` modulo `4` times `d2`, and `2 T0` is `2` modulo `4`.
   - (E; E, O): `d1 ((s^2 + 4 lambda) d2 - 2 lambda T0)`, the same
     argument with `lambda T0` odd.
   - Vertex in one column and both ends in another column: the same two
     equations with `d1 = d2`.
   The case `lambda = 1` is the Chinese remainder order. So order kills
   right angles, and by item 2 the same order creates vertical rivals.
   This is the basic tension.

## 5. Loads in a random-like order [heuristic]

The first two rows are per label and the last two per black point, at a
constant density `theta` of double columns.

| Family | Load | Source |
| --- | --- | --- |
| Vertical rivals | about `0.4 log h` at full density | sum of `1/L` over primitive triples |
| (E; E, E) inside random blocks of density `1/C` | about `log h / C^2` | solutions of `t1 t2 = c1 c2` |
| Right angle at a label point with two label ends, fourth corner in a double column | about `2.4 theta^3 log^2 h` | `sum 1/(ab)` over coprime `a, b <= h` |
| The same, fourth corner in a row-1 sea column and in an even row | about `1.2 theta^2 log^2 h` | half of the corners |

Entropy check. There are about `exp(q log N)` ways to put `q` labels in
`N` columns. A first-moment count needs the total number of bad events to
be at most `q log N`.

- Vertical rivals: the count is `c q Lambda q / N`. So `N` of order `q`
  is borderline, with the constant deciding. This fits row T29.
- Triples with the fourth corner in a double column: the count is of order
  `theta^3 q log^2 h`. This needs `theta` of order `(log h)^(-1/3)`.

So random-like placements stop at about `h^2 (log h)^(1/3)` for the triple
family even if every pair family is free. Structure has to remove the
triples. The one-prime scaffold of Section 2 removes most of them.

## 6. The sea [proved]

**One-label collisions with a row-1 sea.** Let a label have its odd point
`F` at column `c` and row `2k+1`, `k >= 2`. For every factorization
`k = j a b` with `a, b` coprime and `a != b`, put `u = j a^2`,
`v = j b^2`. Then the three row-1 points in the columns

    c - u,   c + v - u,   c + v

cannot all be black. Proof: with `E = (c + v - u, 1)`, the segment `EF` is
a diagonal of a tilted rectangle whose other diagonal `AB` is horizontal,
in row `k+1`, between the columns `c - u` and `c + v`. The axis rectangle
with side `AB` and the other side in row 1 has the same presentation as
the tilted one when the three row-1 points are black. This is the family
of row T11, read for a one-row sea.

Two consequences.

1. A single double with odd row at least 5 is invalid in a full row-1
   sea. The sea needs a hole in each triple. A hole is a column that is
   white in row 1: a double without row 1, or a singleton in another row.
2. **Doubles block for each other.** If every label sits in an even column
   and every even column near it holds a double without row 1, then every
   triple contains a hole: `u`, `v` or `v - u` is even. This is free
   shared blocking. The price is that every fourth corner of a right angle
   of label points then lies in a double column, so the label points must
   have no tilted right angle at all with its fourth corner in the grid.

## 7. Full windows are rigid for the 45-degree lines [proved]

Take a window of consecutive columns that are all doubles, and a black
point `V` at least `h` columns from both ends of the window. Every white
point near `V` already completes one axis rectangle with three black
corners. So no tilted rectangle near `V` can have exactly three black
corners.

Look only at the lines of slope `+1` (diagonals) and `-1` (antidiagonals)
through `V`, and at the four rays NE, NW, SE, SW.

- If NE and SE both hold black points, the fourth corner is in the grid.
  The same holds for NW and SW. So these pairs are forbidden.
- NE and NW can both hold black points only if the two nearest ones, `s`
  and `t` rows above `V`, have `s + t > h - row(V)`. Then the fourth
  corner is above the grid. I call `V` an up-apex. SE and SW give a
  down-apex with `s + t >= row(V)`.

So every such `V` is alone on its diagonal, or alone on its antidiagonal,
or an apex. Give a point that is alone on a line weight 1 for that line,
and give an apex weight 1/2 for each of its two lines. A line with two or
more black points gets weight only from its lowest point (if it is an
up-apex) and its highest point (if it is a down-apex). So every line gets
at most 1. Hence

    number of black points  <=  number of nonempty diagonals
                                + number of nonempty antidiagonals.

A full board of width `q` has `2q` black points and `2(q + h - 1)` such
lines. So all but about `2h` lines are tight: each tight line holds one
point, or a chain whose lowest point is an up-apex and whose highest point
is a down-apex, with every point in between alone on its other line. The
black points are the corners and some interior points of zigzag paths.

**An exact identity.** Call the black points of one line a chain when
there are at least two. For a black point let `d` and `a` be the numbers
of its neighbors in the chains of its diagonal and its antidiagonal, each
0, 1 or 2. The rules above allow only the types `(0, *)`, `(*, 0)` and
`(1, 1)`, where `(1, 1)` is an apex. A chain has two ends, an apex is an
end of two chains, and following chains through apexes always moves to
the right. So the chains form zigzag paths, and each path has exactly two
ends that are not apexes. Counting nonempty lines as
"points alone on the line, plus chains" gives, for a board of doubles
only in which no diagonal rectangle is fully black,

    (points alone on both lines) + (zigzag paths) + (empty lines) = 2h - 2.

With `t` singleton columns the right side becomes `t + 2h - 2` plus a
term for the points that are vertices of right angles with the fourth
corner in the grid. Every such right angle needs its own white point in a
singleton column, in a row of the class of that singleton.

So a board of doubles only has at most `2h - 2` zigzag paths for its
`h^2/2` black points.

This is consistent. With `g = h/2` odd and not divisible by 3, the points

    (p, n) = (s + k g, 2s + k g)  and  (s + k g, 2s + (k+1) g),
    0 <= s < g,  k an integer,

in the coordinates `p = (x - y)/2`, `n = (x + y)/2` of one color class of
the bishop coloring, give one black point in every column, use every row
once per period `h`, and have no right angle with its fourth corner in the
grid. So counting on these lines cannot exclude a full board. Two more
conditions must be added before it could:

- Two perpendicular black pairs of equal span, one on a diagonal and one
  on an antidiagonal, collide when the midpoint of one lies on the line of
  the other and the midpoints differ. (The axis square on the first pair
  and the 45-degree rectangle on the second share two corners.) In the
  periodic pattern above all spans equal `h/2`, so the pattern itself is
  invalid.
- The pairs of rows in the columns must all differ.

I did not find a contradiction, and I did not find a valid full pattern.

## 8. Related problems

1. **Monotonicity. [rechecked]** Adding a white column to a valid board
   fails exactly when a point of the new column is the fourth corner of
   two tilted rectangles whose other corners are black. Adding a column
   with one black point adds more cases. I have no operation that always
   works, so `f(h, m+1) >= f(h, m)` stays open.
2. **A lower bound above `q_h`. [rechecked]** In a board of doubles only,
   every white point completes exactly one axis rectangle with three black
   corners. So the board is valid only if no tilted rectangle has exactly
   three black corners and at most one is fully black. Section 7 is the
   strongest consequence I could draw, and it is not a contradiction.
   No counting argument can work at this density: for every slope class
   other than 45 degrees the black points are too few to force a pair on
   both lines through a point.
3. **The first `n` with `f(n,n) > 2n` is 8.** This is in the archive
   (`research_archive/2026-11-07/REPORT.md`), but the paper lists it as
   open (Section 9, item 4). Today I checked the boards in
   `research_archive/2026-11-10/squares_experiments/data` with a separate
   enumerator of all lattice rectangles: 7 boards of the 8 by 8 grid with
   17 points, 31 boards of the 9 by 9 grid with 19 points and 48 boards of
   the 10 by 10 grid with 21 points are valid. The enumerator finds 1192,
   2044 and 3305 rectangles, which are the known counts.

4. **One tilted slope is easy. [proved]** If only axis-aligned rectangles
   and rectangles with sides of slope `+1` and `-1` have to be told
   apart, the threshold is at most `49 q_h`
   (`simplified_variants.md`, Theorem 4). The proof is a greedy placement
   with a one-row sea. It fails for every further slope because of
   Section 6. The exact thresholds of that variant are `q_h + 2` for
   `h = 4, 5, 6`, so the 45-degree rectangles alone exclude boards with
   fewer than 2 singleton columns at these heights.

## 9. Earlier working notes that I did not derive again [working notes]

- Separating blocks by gaps of length `h` and forbidding steep legs costs
  each label about `|T|/gamma` columns. The best total is `h^(5/2)`.
- A periodic odd sawtooth (odd rows `4 alpha + 3`, `alpha = kappa sigma`
  modulo `A`) has a vertical rival for about a fifth of all labels,
  whatever the even rows are.
- No design by residue classes removes all vertical rivals: the two
  points of one label already differ by a square.
- Requiring a strict 2-adic gap between all pairs forces the columns to be
  constant modulo about `2A`, hence cubic width.
- In a random block model the local lemma needs `h sqrt(log h)` blocks for
  the (E; E, E) family alone.

## 10. Where I am stuck

1. **A monotone palette.** Show that the labels can be split into `O(h)`
   blocks such that each block has one label per odd row, has no vertical
   rival in the placement of row T29, and has `j` nondecreasing in `i`
   with bounded slope. Row T29 gives the first two properties and Section 3
   needs the third. The natural attempt lets block `c` follow the diagonal
   `j = i + lambda_c` within a band of width `F`. Each label then has
   about `F` candidate blocks, of which a fraction `h^(-1/16)` is eligible,
   so `F` must grow like a power of `h`, and a monotone choice inside such
   a wide band needs a matching argument that I do not have.
2. **The (E; O, E) angles.** Each one is created by two labels and
   forbids one position of a third (Section 3, item 4). Its fourth corner
   is in an odd row. It is harmless in a row-1 sea column and fatal in a
   double column. I found no rule that keeps all fourth corners out of
   double columns.
3. **A sea for blocks.** Section 6 shows that a one-row sea needs holes
   near every label. The periodic seas of rows T3 and T4 give them for
   most labels, but their letters change with the column, and then the
   parity rule of item 2 changes too. I did not combine the two.
4. **A lower bound.** I have no mechanism at all. Every family of
   collisions that does not depend on the sea can be avoided by itself in
   width `O(h^2)`.
