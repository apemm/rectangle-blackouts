# Threshold: block form of the rigid layouts, the vertical-rival cost, and gap words

Research note, 10 November 2026. The bound m_0(h) = O(h^2) is not proved here. This note
does three things by hand, with no computation:

1. It states a 2-adic slope lemma that contains the even-side half of Theorem R and the
   mod-4 filler split as special cases (section 1).
2. It rewrites every Theorem R layout as a sequence of full blocks and shows that the
   vertical-rival problem lives inside single blocks, does not depend on the map t, and
   has a Pell-orbit structure (section 2). This isolates the one cost that the rigid
   layouts cannot avoid.
3. It classifies the fatal triangles with two label cells and one filler for every gap
   word that depends on the 2-adic valuation of the column offset (section 3). This
   explains the word 1,1,1,h,1,1,1 and gives predictions that the stored scan can test
   (section 4).

Notation as in `../2026-11-09/quadratic_gap_structure.md`: odd rows 2a+1 (0 <= a < k_o),
even rows 2b+2 (0 <= b < k_e), v the 2-adic valuation, a right angle is tilted if no leg
is horizontal or vertical. For odd h put K = (h-1)/2 and a* = K - a, so that the odd row
2a+1 is at distance 2a from row 1 and 2a* from row h.

## 1. The slope lemma

For a vector (X, d) with X != 0 and d != 0 put lambda(X, d) = v(d) - v(X).

**Lemma 1.** If (X_1, d_1) and (X_2, d_2) are perpendicular and neither is horizontal or
vertical, then lambda(X_1, d_1) + lambda(X_2, d_2) = 0.

Proof. X_1 X_2 = - d_1 d_2. Compare valuations. QED.

So a set of cells in which every tilted leg has negative slope valuation contains no
tilted right angle. Three uses follow.

**1.1 Even side of Theorem R, with slack.** Let label columns be 2^e sigma with e >= 2.
A leg between two even cells is (2^e x, 2c), with lambda = 1 + v(c) - e - v(x). A leg
between an even and an odd cell has odd vertical part, so lambda = -e - v(x) < 0. Hence
the two even-vertex cases of Theorem R hold under the weaker condition

    (T_e)  v(b - b') <= v(sigma - sigma') + e - 2   for labels with b != b'.

For e = 2 this is condition (T). The odd-vertex cases use (P) and need
p > (4^(e-1) + 1) h and p not dividing 4^(e-1) + 1; the proof is the proof of Theorem R
with 16 replaced by 4^e.

Remark. The slack does not buy density. (T_e) fixes sigma modulo 2^(J-e+2) instead of
2^J, which gives 2^(e-2) admissible slots per period, but the column spacing grows by
2^(e-2) and the prime by 4^(e-2). I record it because it shows that the valuation
argument is a statement about slopes, not about one particular spacing.

**1.2 Two-sided blocks.** Take slots sigma = 0, ..., 2^J - 1 with odd index a = sigma and
even index b = mu(sigma), where mu is a bijection of [0, 2^J) with
v(mu(s) - mu(s')) = v(s - s'). Every same-parity leg has lambda = 1 - e and every
opposite-parity leg has lambda <= -e, so the block has no tilted right angle among its
label cells, for any e >= 2. No prime is needed inside one block.

**1.3 Fillers of the opposite class modulo 4.** This is section 3 of
`../2026-11-09/full_problem_push/continuation_power_two_filler_coupling.md`, restated: if
label columns are multiples of 4, every label has a odd, and every filler is in a row
congruent to 1 modulo 4, then no triangle with one filler and two label cells of opposite
parity exists. Lemma 1 gives it in one line per case, and section 3 extends it.

## 2. Theorem R layouts are sequences of full blocks

Fix a Theorem R layout with spacing 4: sigma = a (mod p), sigma = t(b) (mod 2^J), with
p > 5h + 4 and 2^J >= k_e, and let B be the inverse of t on residues.

**Proposition 2 (block form).**

(a) The usable slots are the runs sigma in [np, np + k_o), n an integer. In run n the
slot np + j carries odd index j and even index B(j + np mod 2^J). If 2^J = k_e, every
run in one period p 2^J is full and the runs realize every label once.

(b) Consecutive runs are separated by more than h columns. A vertical rival therefore
uses two labels of the same run.

(c) For a label (a, b) put T = 2(b - a) + 1 and

    X(a, b) = { x != 0 : 0 <= a + x < k_o, 16 x^2 + (T - 2x)^2 = L^2 for an integer L,
                and 1 <= (2a + 2b + 2x + 3 -+ L)/2 <= h }.

Two occupied slots sigma and sigma' of one run form a vertical rival if and only if
sigma' - sigma lies in X(label at sigma) or sigma - sigma' lies in X(label at sigma').

(d) The sets X(a, b) do not depend on t, on p, or on the period chosen. The map t only
decides which label sits at the forbidden slot.

Proof. (a) is the definition. (b) The gap is 4 (p - k_o) > 4 (4h) columns, and a rival
has horizontal gap below h. (c) By (P) the label at slot sigma + x of the same run has
odd index a + x exactly. The even cell of the first label and the odd cell of the second
have horizontal gap 4x and vertical difference (2b + 2) - (2a + 2x + 1) = T - 2x, and
the two white rows are the ones displayed. The other opposite-parity pair is the same
statement with the roles of the two labels exchanged. (d) Nothing in (c) involves t.
QED.

**Corollary 2.1.** Summed over all labels, the number of pairs (label, forbidden gap) is
the same for every Theorem R layout of a given height. The layer problem is: color the
labels with N colors (the period index) so that the label at slot sigma and the label at
slot sigma + x of the same run differ whenever x is in X(label at sigma). The map t
changes the wiring of this graph and not its number of edges.

The same holds for Theorem R' with a small odd slope and for the two-prime CRT placement,
where a run is one diagonal b - a = const.

**Lemma 2.2 (Pell form).** With Y = 10x - T, the equation 16x^2 + (T - 2x)^2 = L^2 is

    Y^2 - 5 L^2 = -4 T^2.

Its integer solutions form orbits under (Y + L sqrt 5)/2 -> ((3 + sqrt 5)/2)(Y + L sqrt 5)/2,
that is (Y, L) -> ((3Y + 5L)/2, (Y + 3L)/2), and under sign changes. The number of orbits
up to sign is the number r(T) of ideals of norm T^2 in the integers of Q(sqrt 5),

    r(T) = product over primes l = +-1 (mod 5) with l^j exactly dividing T of (2j + 1).

Proof. 5 (20x^2 - 4Tx + T^2) = (10x - T)^2 + 4T^2. The unit (3 + sqrt 5)/2 has norm 1
and generates the units of norm 1 up to sign, the class number is 1, and T is odd, so
orbits correspond to ideals of norm T^2. Inert and ramified primes contribute one ideal
each. QED.

Example. T = 1 gives (Y, L) = (1,1), (4,2), (11,5), (29,13), (76,34), (199,89), ... and
the admissible values are x = -1 (L = 5), x = 3 (L = 13), x = 20 (L = 89), x = -52
(L = 233): one orbit, with |x| = 1, 3, 20, 52, ... growing geometrically.

**Consequences (the first is proved, the rest are counts).**

* Along one orbit |Y| grows by at least (3 + sqrt 5)/2 > 2.6 per step. So X(a, b) has at
  most 2 r(T) (1 + log(2h)/log 2.6) elements, and at most 2 r(T) of them in any range
  [y, 2.6 y).
* For T of size comparable to h, each orbit has O(1) elements in range, so
  |X(a, b)| is about r(T). The mean of r(T) over odd T below h is of order log h, and
  for a typical T it is 3^(omega_s(T)), where omega_s counts prime factors that split in
  Q(sqrt 5); that is (log h)^(0.55 + o(1)). This agrees with the count in section 5.5 of
  the earlier note and refines the exponent.
* In the linear case t = id, a run is a path, the conflict graph on the diagonal T is a
  distance graph with distance set X(T), and gaps larger than k_o/A are separated by
  cutting the run into A intervals. So only the small gaps cost colors. For a distance
  set with at most M elements in every range [y, 2y) the theorem of Peres and Schlag on
  lacunary sequences should give O(M log M) colors. I have not checked the multi-sequence
  form in the primary source, so this is a pointer and not a claim.

**What this says about the threshold.** In the rigid family the cost of vertical rivals
is the number of layers, the layer count is a maximum over runs because every run is
repeated once per period, and the per-label conflict count is fixed by the height. A
bounded number of layers would need the conflict graph of Corollary 2.1 to have bounded
chromatic number although its average degree is of order log h. The wiring freedom t is
the only parameter. I tried four ways to use it and none works:

1. Coloring by a modulo 2^m is proper exactly for conflicts with v(x) < m. The fraction
   of conflicts with 2^m dividing x is about 2^(-m), and whether a label has such a
   conflict depends only on the label. A bounded m leaves a positive fraction of labels
   in conflict once log h is large.
2. Residue colorings fail by section 5.4 of the earlier note.
3. A prime l inert in Q(sqrt 5) dividing T forces l to divide x, which is the statement
   that r(T) ignores inert primes. Making all cells of a region lie on one line modulo l
   only reaches the diagonals with l dividing T.
4. Restricting a region to rows near the boundary shortens the rival range (Lemma V(c))
   but does not change the number of conflicts per label at fixed density, because the
   fit condition is already part of X(a, b).

So I now state the obstacle as follows. Excluding right angles by congruences leaves O(1)
slots per label, and with O(1) slots per label the vertical rivals force about
r(T) layers on the diagonal T. The two known mechanisms meet in a single graph, the one
of Corollary 2.1, and O(h^2) by this route is equivalent to a bounded chromatic number
for that graph for some choice of t at every height. For heights of practical size the
graph is very sparse (0.29 conflicts per label at h = 79 and spacing 8 in the scan), so
two or three layers suffice there; the difficulty is only asymptotic.

## 3. Gap words that depend on the valuation of the offset

Setting. h is odd. Label columns are the multiples of s = 2^e, e >= 2, all occupied.
A filler at a column f that is not a multiple of s is in row 1 if v(f) is in Lambda_1 and
in row h if v(f) is in Lambda_h, where Lambda_1 and Lambda_h partition {0, ..., e-1}.
The word 1,1,1,h,1,1,1 at spacing 8 is Lambda_1 = {0, 1}, Lambda_h = {2}. All fillers in
row 1 is Lambda_h empty.

A triangle is fatal if its completion W is in the board and the column of W holds a
black cell in a row of the other parity.

**Theorem 3.** In this setting:

(a) No fatal triangle has one label cell and two fillers, and no triangle at all has
three fillers.

(b) A fatal triangle with two label cells and one filler is of one of four kinds. In
each, exactly one of the two label cells is in an odd row; a is its index.

| Kind | Right-angle vertex | Filler row | Necessary condition |
|---|---|---|---|
| A1 | the odd label cell | 1 | v(a) >= e - 1 + rho for some rho in Lambda_1 |
| B1 | the filler | 1 | v(a) = 2 rho - 1 for some rho in Lambda_1, rho >= 1 |
| A2 | the odd label cell | h | v(a*) >= e - 1 + rho for some rho in Lambda_h |
| B2 | the filler | h | v(a*) = 2 rho - 1 for some rho in Lambda_h, rho >= 1 |

In kinds A1 and A2 the second label cell is in an even row, above the vertex for A1 and
below it for A2, at a column offset X_2 with v(X_2) = 1 + v(a) - rho (respectively
1 + v(a*) - rho).

Proof. Write legs as (X, d) from the vertex.

*Vertex at a label cell Q in row y, one filler F in row 1, one label cell R.* The legs
are (X_1, -(y-1)) and (X_2, d_2), so X_1 X_2 = (y - 1) d_2, with s dividing X_2, X_2 != 0
and s not dividing X_1. W is in row 1 + d_2, so d_2 > 0, and in a column congruent to
X_1 modulo s relative to Q, hence a filler column with the same valuation class as F,
hence a row-1 column. W is fatal exactly when 1 + d_2 is even, that is when d_2 is odd.
If y is even, (y - 1) d_2 is odd, which contradicts X_2 even. So y = 2a + 1,
X_1 X_2 = 2 a d_2 with d_2 odd, and v(X_1) + v(X_2) = 1 + v(a). With rho = v(X_1) in
Lambda_1 and v(X_2) >= e this is A1.

*Vertex at a row-1 filler F, label cells P and R.* The legs are (X_i, d_i) with d_i > 0,
X_1 X_2 = - d_1 d_2, and X_1 = X_2 (mod s), neither divisible by s, so
v(X_1) = v(X_2) = rho in Lambda_1. W is in row 1 + d_1 + d_2 and in a column of the same
valuation class as F, so it is fatal exactly when d_1 + d_2 is odd. Then one cell is odd
with d = 2a and the other even with d odd, and 2 rho = 1 + v(a). This is B1.

*Row h.* Reflect rows. Distances to row h are 2a* for odd rows and odd for even rows
because h is odd. This gives A2 and B2.

*One label cell Q and two fillers.* If both fillers are in the same row and Q is the
vertex, W is in row 2 - y or 2h - y, outside the board. If the vertex is a filler and
the other filler is in the same row, a leg is horizontal. If the vertex is a filler and
the other filler is in the other row, W is in row h + d or 1 - d with d > 0, outside the
board. If Q is the vertex and the fillers are in rows 1 and h, then
X_1 X_2 = (y - 1)(h - y), W is in row h + 1 - y, which has the parity of y, and in a
column congruent to X_1 + X_2. If y is even the product is odd, so v(X_1) = v(X_2) = 0,
which is impossible because 0 belongs to only one of Lambda_1, Lambda_h. If y is odd, W
is in an odd row, and it is fatal only if s divides X_1 + X_2, which needs
v(X_1) = v(X_2), again impossible. Three fillers lie in two rows, so two of them are in
one row and every right angle among them has a horizontal leg. QED.

**Corollary 3.1 (the word 1,1,1,h,1,1,1).** For e = 3, Lambda_1 = {0,1}, Lambda_h = {2}:
A1 needs v(a) >= 2, B1 needs v(a) = 1 with the filler at offset 2 or 6 modulo 8 from the
label columns, A2 needs v(a*) >= 4, and B2 needs v(a*) = 3. A label whose odd index a is
odd and satisfies v(a*) <= 2 is in no fatal triangle with a filler.

**Corollary 3.2 (uniform words).** If Lambda_h is empty, only A1 and B1 occur, and both
need a even and nonzero. So a region whose labels all have a odd, with every filler in
row 1, has no fatal triangle with a filler, at any spacing 2^e >= 4 and for any order of
the labels. By reflection, a region whose labels all have a* odd, with every filler in
row h, has none either.

**Corollary 3.3 (h = 3 mod 4).** Then K is odd, so exactly one of a, a* is odd for every
a. Splitting the labels by the parity of a into two regions, with fillers in row 1 for a
odd and in row h for a even, removes every fatal triangle with a filler. The two regions
need one separation of (h-1)^2 columns (Lemma S). For h = 1 (mod 4) the indices with a
and a* both even are not covered by rows 1 and h; they need a filler row congruent to
3 modulo 4, which is not immune to vertical rivals.

Corollary 3.2 is the statement 1.3, proved here for the two boundary rows and for every
spacing. What Theorem 3 adds is the exact list for mixed words, which is what the stored
boards use. All boards found so far (heights 11, 15, 19) and the two target heights 23
and 27 are congruent to 3 modulo 4.

Limits. Theorem 3 is about the axis test at the completion. A triangle that is not fatal
still needs a white completion that no other rectangle shares. It says nothing about
triangles with three label cells, vertical rivals, or four- and six-cell collisions.

## 4. Predictions for the queued rerun (written before any run)

For the arithmetic-progression layout of `../2026-11-09/small_boards/epsilon_scan.md`,
odd h, spacing 8, any label order:

P1. Variant (i). Every fatal triangle with two label cells has its odd label cell at an
index a with v(a) >= 1 or v(K - a) >= 3, split as in Corollary 3.1.

P2. Variant (ii). Every fatal triangle with two label cells has v(a) >= 1 and a != 0.
The filler is at an offset of valuation rho with v(a) = 2 rho - 1 (vertex at the filler)
or v(a) >= 2 + rho (vertex at the odd label cell).

P3. Variant (ii) restricted to the labels with a odd, at spacing 4, 8 or 16: the number
of fatal triangles with two label cells is exactly zero in every shuffle.

P4. For h = 3 (mod 4), the split layout of Corollary 3.3 has no fatal triangle with a
filler. What remains per label is the three-label term of the scan (0.42 at h = 79,
spacing 8) and the label-label vertical rivals (0.29), both of which are label-only.

If any of P1 to P4 fails, Theorem 3 or its reading of the scan's definitions is wrong
and this section must be corrected before anything is built on it.

## 5. Where this leaves the threshold

* Right angles among label cells: solved in width O(h^2) (Theorem R and its relatives).
* Triangles with fillers: for h = 3 (mod 4), reduced by Corollary 3.3 to uniqueness of
  white completions. This is compatible with any label layout on columns divisible by 4,
  including the rigid ones, because Theorem 3 does not use the label order.
* Vertical rivals inside a rigid layout: the single graph of Corollary 2.1. This is the
  open point. A proof of O(h^2) along this route needs a bounded chromatic number; a
  proof that every right-angle-free layout of constant density is of the rigid kind
  would instead give a growing factor. I can prove neither.
* Mixed four-cell collisions, completion uniqueness, and collars between regions are not
  treated here.
