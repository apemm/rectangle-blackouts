# Sea-mediated collisions, spacing four, and the junction of two seas

Research note, 10 November 2026. Hand proofs only. The bound m_0(h) = O(h^2) is not proved.
This continues `one_label_collisions_and_holes.md` (Theorem 4 and its corollaries).

Notation as there: h odd, K = (h-1)/2, odd rows 2a+1, even rows 2b+2, a* = K - a, v the
2-adic valuation. Label columns (slots) are the multiples of s. A hole is a slot that holds
a single black cell.

## 1. One principle behind type (I), the hole law and a second rival graph

**Lemma 5 (horizontal diameters).** Let B_1 = (x_1, y_1) and B_2 = (x_2, y_2) be black
cells in different columns with y_1 = y_2 (mod 2), y_1 != y_2, and x_1 = x_2 (mod 2).
Suppose their distance is an even integer 2l. Put c = (x_1 + x_2)/2, w = (y_1 + y_2)/2,
W = (c - l, w), Z = (c + l, w). If W and Z are white and the columns c - l and c + l hold
black cells in a common row, the board is not valid.

Proof. B_1, B_2 and W, Z are the two diagonals of a rectangle: same midpoint, same
length. The axis rectangle on W, Z and the two black cells of the common row has the same
white pair. The rectangles differ because y_1 != y_2. QED.

Uses:

* B_1 a label cell and B_2 a filler in row 1 or h gives type (I) of Theorem 4.
* B_1 a label cell and B_2 a hole in any row rho of the parity of B_1 gives a hole law for
  every row, not only for rows 1 and h: in a region whose odd columns are in row 1, a hole
  at (c, rho) is forbidden if some label cell (X, y), y = rho (mod 2), has
  (c - X)^2 + (y - rho)^2 = (2l)^2 with l - (c - X)/2 odd. The number of label cells that
  forbid a given (hole, row) is again governed by tau of a square, so no filler row is
  free of the (log h)^2 load. An even row removes type (II) and (III) for the hole, by
  Theorem 4, but not this.
* B_1 and B_2 cells of two labels gives the conditions of 1.1.

**1.1 Horizontal rivals in a uniform region.** Take s = 4, every slot a label, every other
column a filler in row 1. Let two label cells of the same parity be at slot gap x != 0 with
rows differing by 2 delta, delta != 0.

**Corollary 5.1.** The two cells collide with the sea in exactly these cases:

(H1) delta is odd and 4x^2 + delta^2 is a square;

(H2) delta = 2 (mod 4) and x^2 + (delta/2)^2 is a square.

If 4 divides delta and the distance is an even integer, W and Z are slots.

Proof. The distance is 2l with l^2 = 4x^2 + delta^2, and W, Z are in the columns
2x -+ l relative to the first cell. If delta is odd, l is odd and both columns are odd.
If delta = 2 delta', then l = 2l', x^2 + delta'^2 = l'^2, and the columns 2(x -+ l') are
2 modulo 4 exactly when delta' is odd. QED.

In a region with all a odd, the odd cells meet only (H2), with delta = a' - a. The even
cells meet (H1) and (H2) with delta = b' - b. Inside a linear run (indices advancing by
fixed steps r_o, r_e per slot) the conditions read (1 + r_o^2) x^2 = square and
(4 + r_e^2) x^2 = square or (1 + r_e^2/4) x^2 = square, which never hold. So linear runs
are free of horizontal rivals for the same reason that they are free of right angles, and
the conditions bite only between runs.

When W and Z are slots, the same rectangle collides if the two labels there share a row.
That is a collision of four label cells and is not treated here.

## 2. Spacing four

**Corollary 5.2.** Let s = 4, every slot a label with no cell in row 1, every other column
a filler in row 1. Then no label, whatever a, is in a collision of type (I-1).

Proof. u v = a^2, and the columns -u, v, v - u must all be fillers, so v(u), v(v) <= 1 and
v(u) + v(v) is even. Then v(u) = v(v), u/2^v(u) and v/2^v(u) are odd with product an odd
square, and 8 divides v - u. QED.

At spacing 8 the label with v(a) = 1 had the collision u = 1, v = a^2. So spacing 4 is the
better lattice for a uniform sea: it is twice as dense and it has no one-label collision
at all. The restriction to a odd is still needed for fatal triangles (Corollary 3.2).

## 3. The junction

Let the odd columns be in row 1 left of a column J and in row h from J on, over a stretch
of at least (h-1)^2/4 columns on each side.

**Theorem 6.** Let a label at column X < J - 1 have its even cell in row y, and put
N = (y - 1)(h - y). If X + N >= J, the board is not valid, unless the cell
(X + N + 1, h + 1 - y) is black. The same holds for a label at X' > J with X' - N < J.

Proof. N is odd. The cells E = (X, y), F_1 = (X + 1, 1), F_2 = (X + N, h) are black, and
the legs (1, 1 - y) and (N, h - y) from E are perpendicular. The completion is
S = (X + N + 1, h + 1 - y), in an even row and an even column. If S is white, its column
holds a black cell in an odd row r, either a filler or the odd cell of a label. The pair
(r, h + 1 - y) is a label elsewhere, and the axis rectangle on S, (X + N + 1, r) and that
label has the white set {S}. QED.

Consequences.

* N >= h - 2. So the last (h - 2)/s slots before J, and the first after it, cannot hold
  labels. A label with even row y needs distance more than (y-1)(h-y) from J.
* There are enough labels for this. Within distance D of J there are D/s slots, and the
  labels with N < D number about D/4 in each region. So sorting each region by N,
  increasing towards the junction, satisfies Theorem 6.
* The separation used in the P4 test (first half row 1, second half row h, total
  (h-1)^2) satisfies Theorem 6, because N <= (h-1)^2/4. This agrees with the zero count of
  fatal triangles across the separation.

**The slots near J.** They are holes, and the hole law applies. One sea that passes type
(I), for s = 4 and h = 3 (mod 4):

    region 1 (a odd)  |  buffer 1          |  buffer 2          |  region 2 (a even)
    fillers in row 1  |  odd columns row 1  |  odd columns row h  |  fillers in row h
                      |  even columns row h |  even columns row 1 |

**Lemma 6.1.** With this sea, a label of region 1 is in a collision of type (I) only in
this case: v(a*) = 1, u v = a*^2 with v(u) = v(v) = 1, and its distance Delta = J - X
satisfies v - u < Delta <= v. Region 2 is the reflection.

Proof. (I-1): v - u is a multiple of 8. In region 1 it is a label, in buffer 1 it is in
row h. If it is in buffer 2 or beyond, X + v is an odd column right of J, in row h, and
X - u is in row 1. (I-h): the filler at X + v - u is in row h, so it is an even column of
buffer 1 or of region 2. Since a* is even, u and v are even. X - u is in region 1, so it
is a label unless v(u) = 1, and then it is in row 1 and v(v) = 2 v(a*) - 1. X + v lies
right of X + v - u. In buffer 1 it is in row h. In region 2 or beyond it is a label or in
row h. In buffer 2 it is an even column; it is a filler in row 1 exactly when it is
2 modulo 4 or a hole, and v(v) = 1 gives v(a*) = 1. QED.

So type (I) at the junction is a finite list of forbidden distances per label, of total
length the sum of u over the factor pairs. Types (II) and (III) at the junction are not
classified here. Fatal triangles with two labels and one buffer filler exist for pairs of
region-1 labels at slot gap x_2 when a* |d_2| / (2 x_2) is the offset of an even buffer
column; that is a condition on pairs, to be met by the order.

**Prediction for the P4 layout (not a run).** The separation used in the test has holes in
row 1 next to region 1. By Corollary 4.3 a region-1 label with a = 3 at column X collides
whenever X + 8 is such a hole, with white pair (X - 1, 4), (X + 9, 4). So the P4 layout as
tested has two-white collisions although it has no fatal triangle. The test did not count
two-white collisions.

## 4. Linear runs with a constant offset

For the record, because it shows where the freedom of a dense layout is. Let s = 4 and let
a run be slots j = 0, ..., R-1 with odd row 4(alpha_0 + j) + 3 and even row
2(b_0 + 2j) + 2. Then the odd cells and the even cells lie on two parallel lines, the
offset T = (even row) - (odd row) is constant, and:

* no three cells of the run form a tilted right angle (the same-parity legs are parallel
  and a mixed leg (4x, e), e odd, is never perpendicular to the direction (1, 1));
* no two cells of the run are horizontal rivals (section 1.1);
* two labels of the run at gap x are vertical rivals only if x = U/4 for a Pythagorean
  triple (U, V, L) with U - V = T or V - U = T and 4 dividing U. The triple (4m, 3m, 5m)
  always gives |x| = |T|. If every prime factor of T is 3 or 5 modulo 8, the gaps are
  multiples of T.

So a run shorter than its smallest gap has no internal collision among label cells. Every
order of the labels is a concatenation of such runs (a run may have length 1), so this
constrains nothing by itself. All remaining label-only conditions are conditions between
runs. This is the equal-offset chain picture of `crt_scaffold_independent_reductions.md`,
restated for a dense lattice.

## 5. The dense CRT order: what it removes and where it fails

Region 1 for h = 3 (mod 4) has odd indices a = 2 alpha + 1 with 0 <= alpha < A,
A = (K+1)/2, and even indices 0 <= b < K. Since gcd(A, K) = 1, the map

    sigma -> (alpha, b) = (sigma mod A, rho sigma mod K),   0 <= sigma < AK,

with rho a unit modulo K, is a bijection onto the labels of the region. Put the label of
sigma at column 4 sigma. This order has no hole at all.

**Proposition 7.** (a) If A is an odd prime, no three odd cells form a tilted right angle.
(b) If K is an odd prime not dividing 4 + rho^2, no three even cells form a tilted right
angle. (c) For rho = -2 and A odd, every label with offset
T_0 = 2b - 4 alpha - 1 = A is the vertex of right angles with one odd and one even
endpoint: for each x_2 != 0 with no wrap of b between sigma and sigma + x_2, and each
sign, the even cell at sigma + x_2 and the odd cell at sigma +- (A - 4 x_2) (one wrap of
alpha, index alpha -+ 4 x_2) are perpendicular from the odd cell at sigma, whenever the
index alpha -+ 4 x_2 lies in [0, A).

Proof. (a) Legs are (4 x_i, 4 d_i) with d_i = x_i (mod A) and |d_i| < A. Perpendicular
means x_1 x_2 + d_1 d_2 = 0, so 2 d_1 d_2 = 0 (mod A) and some d_i = 0. (b) Legs are
(4 x_i, 2 c_i) with c_i = rho x_i (mod K), so (4 + rho^2) c_1 c_2 = 0 (mod K). (c) The
even endpoint is e = T_0 - 4 x_2 = A - 4 x_2 rows above the vertex, and the legs are
(4 x_2, A - 4 x_2) and (+-4 (A - 4 x_2), -+16 x_2). QED.

Example of (c): h = 27, A = 7, K = 13, the label (alpha, b) = (4, 12), x_2 = 1. The cells
are in rows 19 (vertex), 22 (column offset 4) and 3 (column offset 12), and the
completion is in row 6 of a label column. So this order is not valid at height 27.

Both A and K are prime for h = 11, 27, 75, 123, ... . For general (rho, T_0) the mixed
right angles satisfy x_1 beta = n_1 e with A beta = e + 4 x_2 and n_1 != 0 the number of
wraps of alpha. A heuristic count gives a bounded number per label for rho = -2 and about
log h per label for other slopes. I do not see a slope that removes them: Theorem R
removes them by taking the modulus above 5h, which makes e + 4 x_2 too small to be a
multiple of it, and that is what creates the holes.

So the three rigid options are now all accounted for:

| Layout | Right angles of label cells | Cost |
|---|---|---|
| Sparse, modulus above 5h (Theorem R) | none | holes, which carry the (log h)^2 load of section 1 |
| Dense CRT, prime moduli | none of one parity, mixed ones remain | a bounded or logarithmic number of fatal triangles per label |
| Runs with constant offset | none inside a run | every condition between runs |

### 5.1 Correction: the mixed right angles are rare, the vertical rivals are not

The count in the paragraph before the table is too pessimistic for rho = -2. Take A and K
prime and rho = -2, and write T_0 = 2b - 4 alpha - 1 for the label at sigma.

**Proposition 7'.** (i) No right angle has its vertex at a cell of one parity and both
endpoints at cells of the other parity. (ii) A right angle with vertex at the odd cell of
sigma, an even endpoint at sigma + x_2 (w wraps of b, row difference e) and an odd
endpoint exists only if

    g = T_0 - 2 K w = k A,   k odd,   k | e,   e g > 0.

(iii) A right angle with vertex at the even cell of sigma, an odd endpoint at sigma + x_2
(w' wraps of alpha) and an even endpoint exists only if K divides T_0 + 4 A w'.

Proof. (i) The two legs are (4 x_i, e_i) with e_i odd, and 16 x_1 x_2 + e_1 e_2 is odd.
(ii) The legs are (4 x_2, e) and (4 x_1, 4 d_1) with x_1 = d_1 + n_1 A, n_1 != 0,
|d_1| < A, and e = T_0 - 4 x_2 - 2 K w. Perpendicularity is d_1 (e + 4 x_2) = -4 x_2 n_1 A,
so d_1 g = -4 x_2 n_1 A. Since |d_1| < A and A is prime, A | g, and |4 x_2 n_1| < |g|.
With 4 x_2 = g - e this forces e g > 0, then n_1 = +-1 and k | x_2, so k | e.
(iii) The legs are (4 x_2, e') and (4 x_1, 2 c_1) with 2 x_1 = -c_1 + m K, m != 0,
|c_1| < K, and e' = -T_0 + 4 x_2 - 4 A w'. Perpendicularity is
c_1 (e' - 4 x_2) = -4 x_2 m K, and e' - 4 x_2 = -(T_0 + 4 A w') does not depend on x_2.
Since |c_1| < K and K is prime, K divides it. QED.

Consequences. For w = 0 and w' = 0 only the labels with T_0 in {+-A, +-3A} or
T_0 = +-K are affected. That is O(h) labels out of about h^2/8. For other wraps the
condition fixes T_0 modulo A (or K) in terms of the wrap count, and k | e costs a factor
1/|k|, so I expect O(h log h) affected labels in total. I did not prove that bound. The
h = 27 example has T_0 = 7 = A, as (ii) requires. The table row for the dense CRT order
should read "none, except at O(h) labels (w = 0), expected O(h log h) in all".

The dense CRT order fails for a different reason. Between two wraps it is a run with
constant offset T_0, with the even rows descending. A run with offset T has a vertical
rival at slot gap |T| from the triple (4,3,5), and at gap (U/4)|T|/q for every primitive
triple (U, V) with 4 | U and q = |U - V| or U + V dividing T. The pieces between wraps have length
about A, so every label with |T_0| below the length of its piece has a rival. That is a
positive fraction of the labels.

### 5.2 The run decomposition that the rival condition forces

In the index plane the labels with one offset T = 2t - 1 are the diagonal b - 2 alpha = t,
of length about (K - |t|)/2. A run on this diagonal is free of vertical rivals exactly
when it is shorter than

    x_min(T) = min (U/4) |T| / q

over primitive triples (U, V) with 4 | U and q dividing T, where q is |U - V| or U + V.
Both occur: the odd cell of sigma against the even cell of sigma + x has row difference
T + 4x, and the reverse pair has T - 4x. Every such q has all prime factors congruent to
+-1 modulo 8. So x_min(T) = |T| when T has no such prime factor (only q = 1 remains, from
U - V = +-1), and x_min(T) = |T|/7 when 7 | T (from (4, 3) with q = 7). In general
x_min(T) >= sqrt(2|T|)/8: if U > V then q < 2U and x > |T|/8; if U < V then
U^2 >= 2V + 1 > q, and x >= U|T|/(8 max(q, U)) >= sqrt(2|T|)/8 because q <= |T|.

So a diagonal with |t| >= K/5 and x_min(T) = |T| is one run, and a diagonal with small
|t| splits into at least (K - |t|) / (4|t|) runs. Summing over t, any layout made of
constant-offset runs has at least about (K/2) log K runs. The interactions between these
runs are the whole remaining problem. Separating the runs by h columns of fillers costs
h^2 log h columns and brings back the holes, so it is no better in order than the known
bound.

## 6. Status

Proved in this note and the previous one, for h = 3 (mod 4), spacing 4:

* inside a fully occupied uniform region with a odd: no collision of one label with
  fillers (Theorem 4, Corollary 5.2), no fatal triangle with a filler (Corollary 3.2);
* at a junction: a label-free buffer of h - 2 columns on each side and the order by
  N = (y-1)(h-y) are necessary (Theorem 6), and one buffer sea reduces type (I) to a
  finite list of forbidden distances (Lemma 6.1).

Not proved, in order of importance:

1. An order of the labels of a full region with no tilted right angle of three label
   cells, no vertical rival, no horizontal rival (H1, H2), and distinct completions for
   the triangles S1 to S4. Linear runs settle all four inside a run. Between runs I have
   no mechanism that is not either sparse (Theorem R) or random.
2. Types (II) and (III) and the two-label triangles at the junction.
3. Four-cell collisions of label cells, labels with a cell in row 1 or h, and heights
   other than 3 modulo 4.

On the question itself. Every route to a sparse layout meets the same count: a black cell
at (c, rho) is tested against every label cell of its row parity at integer distance, and
the number of such tests is a divisor sum of squares, of order (log h)^2 on average. A
dense lattice passes these tests because the tested columns are labels. So an O(h^2)
construction along these lines must be dense on its lattice, and the open problem is
item 1: a dense order. I do not have evidence either way on whether one exists for large
h. The small boards show it does for h <= 19.
