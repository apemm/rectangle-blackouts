# Simplified variants of the blackout problem

11 November 2026. Problem 001. This note looks at easier versions of the
puzzle: only axis-aligned rectangles, only square boards, both at once,
rectangles that are horizontal, vertical or at 45 degrees, and squares in
place of rectangles. The last two are listed as related questions on the
problem page.

**Outcome.**

1. Without tilted rectangles the threshold is exactly `q_h = floor(h^2/4)`.
   This is known (the paper and the archive). New here: for widths well
   below `q_h` the answer is `2m + o(h^2)`, by the Ruzsa and Szemeredi
   theorem, and the exact staircase of the archive must stop before the
   deficit reaches `h^(4/3 + o(1))`.
2. On square boards nothing new is proved. I checked the archived boards
   again. They answer one question that the paper lists as open: the first
   `n` with `f(n,n) > 2n` is 8.
3. **With rectangles that are horizontal, vertical or at 45 degrees the
   threshold is of order `h^2`:** `q_h <= m_45(h) <= 49 q_h`. The proof is
   a greedy placement with a one-row sea. For `h = 4, 5, 6` the exact
   threshold is `q_h + 2`, which is 6, 8, 11. The full problem has 6, 8,
   15. For `h = 7` the least width with a board is 13, 14 or 15.
4. The greedy proof stops working as soon as one more slope is allowed.
   The reason is a collision between one double and three sea points. It
   is the same family that forces two logarithms on private blocking sets.
5. With squares in place of rectangles the problem changes type. The
   answer grows linearly in the width with a slope that grows with `h`.

Status labels:

- **[proved]**: a complete argument is given here. Lemma 3, Theorem 4
  and Propositions 1 and 2 had one independent reading, which found no
  error. That reading also tested Lemma 3 on all pairs of rectangles of
  the 8 by 7 grid. Nothing else in this note has been audited.
- **[known]**: in the paper or the archive, with the file.
- **[computed]**: an exact computer search, with the script.
- **[heuristic]**: a count without proof.

Notation. Columns `x = 1..m`, rows `y = 1..h`. `S` is the set of black
points, `B_x` the set of black rows of column `x`, and `G_S` the bipartite
graph that joins row `y` to column `x` when `(x, y)` is black. A family
`F` of rectangles is fixed, and `S` is `F`-valid when distinct members of
`F` show distinct sets of white corners. Two rectangles collide exactly
when the symmetric difference of their corner sets is black.

## 1. Axis-aligned rectangles only

Write `f_ax(h, m)` for the largest axis-valid blackout.

### 1.1 What is known

- **[known]** For `m >= 3`, `S` is axis-valid exactly when `G_S` has no
  cycle of length 4 or 6. So `f_ax` is the largest number of edges of a
  bipartite graph of girth at least 8 with parts `h` and `m`
  (`papers/extremal/sections/sec3_rowbound.tex`, Lemma "girth").
- **[known]** `f_ax(h, m) = m + q_h` for `m >= q_h`, and for `h >= 4` the
  blackouts with `m + q_h` points are the complete bipartite families of
  doubles plus singletons (Neuwirth, and Theorem "equality structure" of
  the paper). So the axis-only threshold is exactly `q_h`.
- **[known]** There are `p_h (m)_{q_h} h^(m - q_h)` such blackouts, with
  `p_h` the number of balanced partitions of the rows
  (`jis/sections/sec04_graph.tex`). The generating function in `m` is
  rational with the single pole `1/h`.
- **[known]** `f_ax(h, m) = min(2m, m + q_h)` for
  `m >= q_h - floor(h/2) + 1`
  (`research_archive/2026-11-09/full_problem_push/square_finitewidth_progress.md`).
- **[known]** With `w = q_h - floor(h/2)` and `h - 3 >= 12(l + 1)`,

      f_ax(h, w - l) = 2(w - l) + 1 + floor((sqrt(4l + 1) - 1)/2)

  (`.../full_problem_push/axis_borderline_single_triple.md`).
- **[known]** Neuwirth's inequality
  `e^3 - (h + m) e^2 + 2hm e - h^2 m^2 <= 0`, with equality for
  generalized quadrangles.

### 1.2 Widths of order `h^2` below the threshold [proved]

Let `T(h)` be the largest size of a family of 3-subsets of `{1..h}` in
which two triples share at most one point and no three triples meet
pairwise in three different points.

**Proposition 1.**

1. Every axis-valid blackout of the `h x m` grid, `m >= 3`, has at most
   `2m + 3 T(h)` points.
2. `f_ax(h, T(h)) >= 3 T(h)`.
3. `T(h) = o(h^2)` and `T(h) >= h^2 exp(-C sqrt(log h))`.

So `2m <= f_ax(h, m) <= 2m + o(h^2)` for every `m <= q_h`. The lower
bound takes `m` doubles on distinct edges of a complete bipartite graph
on the rows. The largest gain over `2m` is `h^(2 - o(1))`, and it is
`o(h^2)`.

*Proof.* (1) In every column with `k >= 3` black rows choose
`floor(k/3)` disjoint triples of black rows. Triples from one column are
disjoint. Triples from two columns share at most one row, because there
is no cycle of length 4. Three triples that meet pairwise in three
different rows come from three columns and give a cycle of length 6. So
the number of triples is at most `T(h)`. Since `k <= 2 + 3 floor(k/3)`,
the number of points is at most `2m + 3 T(h)`.

(2) Give each of `T(h)` columns one triple of an extremal family. The
graph has no cycle of length 4 or 6.

(3) Three triples of such a family span at least 7 points: 9, minus at
most 3 for the pairwise meetings, plus 1 if all three share a point, and
the case of three different meeting points is excluded. So no 6 points
contain 3 triples, and the theorem of Ruzsa and Szemeredi gives
`o(h^2)`. For the lower bound take a set `A` in `{1..N}` without
arithmetic progressions of length 3 and the triples
`{(1, x), (2, x + a), (3, x + 2a)}` with `1 <= x <= N` and `a` in `A`.
Two points of a triple determine it. If three triples met pairwise in
three points, these points would lie in the three different classes, and
the common differences would satisfy `a2 + a3 = 2 a1`. So they would be
equal and two triples would coincide. There are fewer than `6N` points,
and Behrend's set has `N exp(-C sqrt(log N))` elements. QED

This explains a remark of Neuwirth: his cubic inequality allows a gain of
order `h^2` at `m = mu h^2`, `0 < mu < 1/4`, and that is never attained.
I did not find the statement `2m + o(h^2)` in the sources I could read.
De Caen and Szekely (1997) might contain it. I could not open that paper.

### 1.3 The staircase cannot continue to large deficits [proved]

**Proposition 2.** Let `T3(n)` be the largest size of a family as in
Section 1.2 whose triples have one point in each of three classes of size
`n`. Let `2 <= n1 <= h/3`. Then

    f_ax(h, m) >= 2m + T3(n1)   for   T3(n1) <= m <= q_h - h n1.

*Proof.* Split the rows into `X2`, `Y2` of size
`n2 = floor((h - 3 n1)/2)` and `UX`, `UY`, `U0` of size `n1`. Use the
doubles `X2 x Y2`, `UX x Y2` and `UY x X2`, and the triples of a family
on `UX x UY x U0`. The doubles form a bipartite graph. A row of `Y2`
is joined by doubles to one point of each triple at most, and so is a row
of `X2`. No double lies inside `UX + UY + U0`. So there is no cycle of
length 4 or 6. The number of columns is `n2 (n2 + 2 n1) + T3(n1)`, and

    n2 (n2 + 2 n1) >= q_h - h n1/2 - 3 n1^2/4 - h/2 >= q_h - h n1,

because `3 n1^2/4 <= h n1/4` and `h/2 <= h n1/4`. The number of points is
twice the number of columns plus `T3(n1)`. Removing doubles keeps the
gain. QED

With `T3(n) >= n^2 exp(-C sqrt(log n))` the gain at the deficit
`D = h n1` is at least `(D/h)^(2 - o(1))`. The staircase formula has gain
about `sqrt(D)`. So the formula fails once `D` exceeds
`h^(4/3 + o(1))`. Between `h/12` and that point I do not know the answer.

## 2. Square boards

### 2.1 What is known

- **[known]** `f(n, n) <= C n^(4/3) / (log n)^(1/3)`
  (`research_archive/2026-11-08/square_local_budget.md`). The paper states
  only `n^(4/3) + (2/3) n`. Before I read that note I derived the same
  bound again with a different covering. That is not an audit.
- **[known]** `f(n, n) >= c n^(6/5) / (log n)^(1/5)`
  (`research_archive/2026-11-09/odd_graph_entropy_square/square_progress.md`).
- **[known]** Product hosts and hosts with `n^(4/3)` points do not beat
  the exponent `6/5` by alteration
  (`research_archive/2026-11-10/squares_sidon_lower_bound.md`).
- **[known]** `f(n, n) = 4, 5, 7, 10, 12, 14` for `n = 2..7`, and
  `f(8,8) >= 17`, `f(9,9) >= 19`, `f(10,10) >= 21`
  (`research_archive/2026-11-10/squares_experiments/RESULT.md`).

### 2.2 Checked today [computed]

`scripts/sq/check_sq.py` lists every lattice rectangle of the `n x n`
grid from the definition and compares presentations. It finds 1192, 2044 and 3305 rectangles for
`n = 8, 9, 10`, the known counts. All 7 stored boards with 17 points on
the 8 by 8 grid are valid, and so are the 31 boards with 19 points and
the 48 boards with 21 points on the next two grids. One of them:

    ###.....
    ..####..
    .....#..
    .....##.
    #.....#.
    ......#.
    ......##
    .#.....#

So `f(8, 8) >= 17 > 16`. Since `f(n, n) <= 2n` for `n <= 7`, the first
`n` with `f(n, n) > 2n` is 8. The paper asks this in Section 9, item 4.

### 2.3 Square boards without tilted rectangles

**[proved]** for `n <= 8`, from the results of Section 1.1 and one new
construction:

| `n` | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- |
| `f_ax(n, n)` | 5 | 8 | 10 | 13 | 16 | 19 |
| Neuwirth's cubic bound | 5 | 8 | 10 | 13 | 16 | 19 |
| `f(n, n)` | 5 | 7 | 10 | 12 | 14 | at least 17 |

For `n = 8` take the rows `p, p', a, b, c, d, e, z` and the 8 columns

    {p,a,b}  {p,p',c}  {p',d,e}  {a,d}  {b,e}  {z,a}  {z,c}  {z,e}.

They have 19 points, no two share two rows, and no three meet pairwise in
three rows (`scripts/sq/axis8.py` checks this, and `scripts/sq/axis67.py`
checks the constructions with 13 and 16 points for `n = 6, 7`). The staircase construction gives
only 18 here. The cubic bound is attained for all `n <= 8` and for
`n = 15` (the quadrangle with 45 points). Asymptotically
`f_ax(n, n) ~ n^(4/3)`, and `f(n, n) = o(f_ax(n, n))` by Section 2.1.

## 3. Rectangles that are horizontal, vertical or at 45 degrees

A diagonal rectangle has the corners `V`, `V + s(1,1)`, `V + t(1,-1)`,
`V + s(1,1) + t(1,-1)` with `s, t` nonzero. Let `F45` be the family of
axis-aligned and diagonal rectangles, `f_45(h, m)` the largest
`F45`-valid blackout, and `m_45(h)` the least width from which
`f_45(h, m) = m + q_h`. Every valid blackout is `F45`-valid, so
`f_45 >= f` and `m_45(h) <= m_h`. Every `F45`-valid blackout is
axis-valid, so `f_45(h, m) <= m + q_h` and `m_45(h) >= q_h` for `h >= 4`.

### 3.1 The collisions of this family [proved]

**Lemma 3.** Let `G_S` have no cycle of length 4 or 6. Then `S` is
`F45`-valid unless it contains one of the following.

- (T2) Three black points `V`, `V + s(1,1)`, `V + t(1,-1)` such that the
  fourth corner `V + s(1,1) + t(1,-1)` is in the grid.
- (T3) Two black points in one column at an even distance.
- (T4) Black points `E, F` on a line of slope `-1` and black points
  `C, D` on a line of slope `+1`, such that `E, F` are opposite corners
  of an axis-aligned square with other corners `A, B`, and `C, D` are
  the translates of `B, A` by a nonzero multiple of `(1,-1)`. Or the
  same with the two slopes exchanged.
- (T5) Four black points that are the corners of a lattice square which
  is neither axis-aligned nor diagonal.

*Proof.* Let `R1, R2` collide and let `I` be the set of common corners.
Three corners determine a rectangle, so `I` has at most 2 points.

- `I` empty: both are fully black. A fully black axis rectangle is a
  cycle of length 4. A fully black diagonal rectangle contains (T2).
- `I = {P}`: if both are axis-aligned we get a cycle of length 6.
  Otherwise a diagonal rectangle through `P` has its other corners
  black, which is (T2) with fourth corner `P`.
- `I = {A, B}`, both axis-aligned: a cycle of length 4.
- `I = {A, B}`, both diagonal. A diagonal rectangle is determined by a
  diagonal, and a side of one is never a diagonal of the other. So `AB`
  is a side of both, and the other four corners form a fully black
  diagonal rectangle, which contains (T2).
- `I = {A, B}`, `R1` axis-aligned and `R2` diagonal. A side of `R1` is
  not a side of `R2`. If `AB` is a side of `R1` and a diagonal of `R2`,
  then `R2` has a horizontal or vertical diagonal of even length, and
  the two other corners of `R2`, or of `R1`, lie in one column at that
  distance: (T3). If `AB` is a diagonal of `R1` and a side of `R2`, then
  `R1` is a square and we get (T4). If `AB` is a diagonal of both, the
  other corners `C1, D1` of `R1` and `C2, D2` of `R2` lie on the circle
  with diameter `AB`. The segments `C1 D1` and `C2 D2` are diameters,
  and they are perpendicular: with `A = (0,0)` and `B = (u, w)` they are
  `(u, -w)` and `(w, u)`. So the four points form a square. It is not
  axis-aligned or diagonal, since `u`, `w`, `u - w`, `u + w` are all
  nonzero. This is (T5). QED

In the full problem (T5) is covered by the corner triples of that
square. Here the square does not belong to the family, so it has to be
listed separately.

### 3.2 The threshold is quadratic [proved]

**Theorem 4.** For `h >= 4` and `m >= 49 q_h` we have
`f_45(h, m) = m + q_h`. Hence `q_h <= m_45(h) <= 49 q_h`.

*Construction.* Use the parity edges `{a, b}`, `a` odd, `b` even. Each
gets its own column. Every other column is black in row 1 only. Call the
black points of doubles in rows `2..h` upper cells. Place the doubles one
at a time, each in the first column such that afterwards:

- (P1) No two upper cells in different columns lie on a common line of
  slope `+1` or `-1`.
- (P2) No two upper cells `(x, y)`, `(x', y')` in different columns have
  `|x - x'| = y + y' - 2` and `y + y' <= h + 1`.
- (P3) No three upper cells in three different columns form an isosceles
  right triangle.

*Counting.* Let `k - 1` doubles be placed. The new double has at most 2
upper cells, and there are at most `2(k - 1)` old ones. For a new upper
cell in row `r` and an old upper cell `Z`:

- (P1) and (P2) each exclude at most 2 columns.
- (P3): the third point `W` is an old upper cell. If the right angle is
  at `Z`, then `W` lies in one of 2 fixed columns, each with at most 2
  upper cells. If the right angle is at the new cell or at `W`, then `W`
  lies on one of 2 fixed lines of slope `+1` or `-1`, each with at most 1
  upper cell by (P1). Each choice of `W` fixes the new column. This
  excludes at most `4 + 2 + 2 = 8` columns.

With the `k - 1` used columns this excludes at most
`(1 + 8 + 8 + 32)(k - 1) = 49 (k - 1)` columns. So all `q_h` doubles fit
in the first `49 q_h` columns.

*Validity.* The doubles form a complete bipartite graph on the rows, so
`G_S` has no cycle of length 4 or 6. It remains to exclude (T2) to (T5).

- (T3): two black points of one column lie in rows of different parity.
- (T2): let `V`, `A = V + s(1,1)`, `C = V + t(1,-1)` be black. If `A`
  and `C` were in one column they would be at even distance. If `V` and
  one of `A, C` are upper cells, this contradicts (P1). If `V` is an
  upper cell and `A, C` are in row 1, then the fourth corner is in row
  `2 - row(V) <= 0`. If `V` is in row 1, then `A` and `C` are upper
  cells with `|x_A - x_C| = y_A + y_C - 2`, and the fourth corner is in
  row `y_A + y_C - 1`. If that row is in the grid, this contradicts (P2).
- (T4): let `B = A + (k, k)` with `k > 0`, so `E = (x_A + k, y_A)` and
  `F = (x_A, y_A + k)`. By (P1) they are not both upper cells, so
  `y_A = 1`. Then `D = A + t(1,-1)` is in the grid only for `t < 0`,
  and then `C` and `D` are upper cells on a line of slope `+1`, which
  contradicts (P1). The case `B = A + (k, -k)` is the same: the point
  `F = (x_A, y_A - k)` is in row 1, the corner `B + t(1,1)` is in the
  grid only for `t > 0`, and then `C` and `D` are upper cells on a line
  of slope `-1`.
- (T5): the 4 corners of such a square lie in 4 different rows and 4
  different columns. So at least 3 of them are upper cells, and they
  form an isosceles right triangle, which contradicts (P3). QED

The proof uses that row 1 is the bottom row twice: a right angle at an
upper cell with both ends in the sea points away from the grid, and a
right angle at a sea point is controlled by one equation per pair of
upper cells.

### 3.3 Data [computed]

A definition-level checker for `F45` and the greedy placement are in
`scripts/v45/core.py` and `scripts/v45/t2.py`. The outputs are the files
`scripts/v45/out_*.txt`.

| `h` | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `q_h` | 4 | 6 | 9 | 12 | 16 | 20 | 25 | 30 | 36 | 42 | 49 |
| greedy width, (P1) and (P2) only | 9 | 20 | 24 | 31 | 41 | 50 | 73 | 79 | 93 | 113 | 132 |
| greedy width, all three rules, with sea points allowed in (P3) | 18 | 29 | 49 | 71 | 94 | 124 | 149 | 177 | 207 | 254 | 285 |

- Every board of both greedy rows passes the definition-level check, at
  the greedy width and at 1 to 3 larger widths.
- Rule (P3) never mattered in these runs. The proof still needs it.
- With (P1) alone every board fails. The collisions are an axis
  rectangle against a diagonal rectangle with a right angle at a sea
  point, which is what (P2) excludes.

Exact thresholds, by two SAT encodings written separately
(`scripts/v45/t3.py` adds collision clauses lazily, `scripts/sq/eq45.py`
adds all of them at once).
"No board" means the solver proved that no blackout with `m + q_h`
points is `F45`-valid.

| `h` | `q_h` | no board at | least width with a board | full problem |
| --- | --- | --- | --- | --- |
| 4 | 4 | 4, 5 | 6 | 6 |
| 5 | 6 | 6, 7 | 8 | 8 |
| 6 | 9 | 9, 10 | 11 | 15 |
| 7 | 12 | 12 | 13, 14 or 15 | at most 21 |

For `h = 7` the solver proved that width 12 has no board, found the board
`16 56 45 14 4 1 47 12 34 67 23 1 36 27 25` at width 15 (black rows of
each column, checked again with `scripts/v45/core.py`), and did not
decide the widths 13 and 14. The limits were 7 minutes each with
`eq45.py` (`scripts/sq/eq45_h7.txt`) and 10 minutes each with `eq45b.py`
(`scripts/sq/eq45b_h7.txt`).

Boards exist at the next 5 widths for `h = 4, 5, 6`. Together with the
known thresholds 6, 8, 15 of the full problem this gives
`m_45(h) = 6, 8, 11` for `h = 4, 5, 6`, which is `q_h + 2` each time.
`scripts/sq/eq45.py` also reproduces 6 and 8 for the full family at
`h = 4, 5`. `scripts/sq/eq45b.py` is a third variant with the row classes
and a symmetry break as extra clauses. It gives the same answers and is
somewhat faster.

So for `h = 4, 5` the 45-degree rectangles alone already force the true
threshold, and at `h = 6` they force 2 of the 6 extra columns.

### 3.4 Boards without singletons are rigid for this family [proved]

Section 7 of `quadratic_threshold_reattack.md` shows the following. In a
stretch of consecutive doubles, every black point is alone on its line
of slope `+1`, or alone on its line of slope `-1`, or the apex of a right
angle whose fourth corner leaves the grid. Counting lines gives

    number of black points <= number of nonempty lines of slope +1 and -1.

A board of doubles only has `2 q_h` points and `2 (q_h + h - 1)` lines.
So all but about `2h` lines carry exactly one unit, and the black points
are the corners of zigzag paths. I do not know whether `m_45(h) - q_h`
stays bounded.

### 3.5 Why the proof stops at 45 degrees [proved]

Allow one more slope class, with directions `(a, b)` and `(-b, a)`,
`a != b`. A double with odd row `2k + 1` and `k = j a b` now collides
with the row-1 sea by itself: the three sea points in the columns
`c - j a^2`, `c + j (b^2 - a^2)`, `c + j b^2` cannot all be black
(Section 6 of `quadratic_threshold_reattack.md`). For 45 degrees
`a = b`, the three columns collapse and the collision disappears. For a
fixed finite set of slopes each double needs a bounded number of holes
in the sea, so I expect a quadratic threshold for every finite set of
slopes, with a constant that grows with the set. I did not prove this.
In the full problem the number of triples per double is the number of
factorizations of `k`, and the sum over all doubles is of order
`h^2 log^2 h`.

## 4. Squares in place of rectangles

Let `f_sq(h, m)` be the largest blackout for which all lattice squares,
tilted ones included, show distinct sets of white corners. Every valid
blackout has this property, so `f_sq >= f`.

- **[proved]** `f_sq(2, m) = m + floor((m + 4)/3)` for `m >= 2`. On 2
  rows the squares are the unit squares. Two neighbors collide when the
  columns on both sides of their common edge are full. Two disjoint
  squares collide when both are fully black. So the set of full columns
  has no two elements at distance 2 and at most one pair at distance 1.
  The largest such set is `{1, 2, 5, 8, ...}`.
- **[heuristic]** For fixed `h` the limit `rho_h = lim f_sq(h, m)/m`
  exists, because squares have width at most `h` and boards can be
  joined with white gaps. `rho_2 = 4/3`.
- **[heuristic]** `rho_h >= c h^(1/5)` by deleting points from a random
  set, and `rho_h = o(h)` by the corners theorem: a set of positive
  density has too many triples `(x,y), (x+d,y), (x,y+d)`, and each one
  is three black corners of a square.
- **[heuristic]** For axis-aligned squares only, the set of points with
  `x - y` in `S1` and `x + y` in `S2`, for sets without arithmetic
  progressions of length 3, has no three corners of a square and no four
  corners of a `d x 2d` rectangle. So the slope is `h^(1 - o(1))`.

So squares give a density problem, not a threshold problem. I did not
go further.

## 5. What this says about the main problem

- The threshold is `q_h` without tilted rectangles, and at most `49 q_h`
  with one tilted slope. In both cases two doubles exclude a bounded
  number of relative positions, and a one-row sea needs no holes.
- Each further slope adds a bounded number of excluded positions for
  those pairs of doubles whose rows it divides, and a bounded number of
  holes per double. Summed over all slopes these are divisor sums. This
  is where `h^2 log^2 h` comes from.
- The data for `h <= 6` show that the 45-degree rectangles carry a large
  part of the cost at small heights.

## 6. Open questions

1. Is `m_45(h) = q_h + O(1)`? Is it `q_h + 2` for all `h >= 4`? The
   first test is width 14 at `h = 7`.
2. Is `m_45(h) > q_h` for every `h >= 4`? A proof would give
   `m_h >= q_h + 1`, which is not known.
3. A quadratic threshold for every finite set of slopes.
4. The value of `f_ax(h, m)` for deficits between `h/12` and
   `h^(4/3)`.
5. `f_ax(n, n)` for `n >= 9`, and whether the cubic bound is attained
   there. A search of the OEIS for 3, 5, 8, 10, 13, 16 found no entry for
   this problem.

## 7. Files

All scripts are in `scripts/` next to this note. Run them with `py`.

- `scripts/sq/check_sq.py`: square boards from the definition. It reads
  the boards in `../2026-11-10/squares_experiments/data`.
- `scripts/sq/axis8.py`, `scripts/sq/axis67.py`: the axis-only
  constructions on square boards and the cubic bounds.
- `scripts/sq/eq45.py`: exact search for boards with `m + q_h` points,
  for the 45-degree family (`diag`) or all rectangles (`all`). Example:
  `py eq45.py diag 6 9 12 100000`. The last argument is a time limit that
  the solver ignores, so use `run_limited.py` for a hard limit per width.
- `scripts/v45/core.py`, `t1.py`, `t2.py`, `t3.py`: checker, hand tests,
  greedy and lazy search for the 45-degree family.
