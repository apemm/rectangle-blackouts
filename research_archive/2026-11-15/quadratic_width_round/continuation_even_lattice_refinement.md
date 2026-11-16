# Refining a cap core onto every even column

15 November 2026. The refinement lemma and Sections 1–3 passed independent
review. Review found an unparked cross-parity triangle in the proposed
row-one sea extension; Section 4 records that obstruction. This note
does not prove a valid complete board. It gives a way to fill a coarser
cap core onto every even column while preserving the geometric inequality
that excludes nonhorizontal same-parity integral distances.

The resulting ordinary columns can all use row one. This replaces the
H7 modular sieve by a different parity sieve. Its remaining supports and
its end collars require their own proofs; the H7 completeness theorem
does not transfer automatically.

## 1. A discrete refinement lemma

Let two total virtual row functions on ranks `0,...,R-1` satisfy

\[
 |f_\alpha(r)-f_\alpha(s)|^2\le C^2|r-s|,
 \qquad |f_\alpha(r+1)-f_\alpha(r)|\le2.
 \tag{1}
\]

The functions have opposite row parities, and at each rank at least one
of their values is good. Fix an integer `M >= max(1,C^2/2)`. At fine
rank `t`, put

\[
 F_\alpha(t)=f_\alpha(\lfloor t/M\rfloor),
 \qquad 0\le t<MR,
 \tag{2}
\]

and give that rank physical column `x=2t`. Then, for distinct fine ranks,

\[
 |F_\alpha(t)-F_\alpha(u)|^2\le2|2t-2u|.
 \tag{3}
\]

Indeed, let `k` be the distance between the two coarse ranks. If `k=0`,
the row difference is zero. If `k=1`, its square is at most four, while
the physical column distance is at least two. For `k>=2`, the fine-rank
distance is at least `M(k-1)+1`, and

\[
 C^2 k\le2C^2(k-1)\le4M(k-1)<4|t-u|.
\]

For a nonzero vertical difference, (3) lies strictly below the next
integer square:

\[
 X^2< X^2+(\Delta y)^2\le X^2+2X<(X+1)^2,
 \qquad X=|2t-2u|.
 \tag{4}
\]

Thus these same-parity pairs do not have integral Euclidean length. The
nonstrict inequality in (3) is sufficient for this conclusion.

## 2. Application to the good-cap virtual functions

Start with physical odd/even row lists of step two, rather than the H7
lists of step 28. The clipped raw Hilbert coordinate functions have
adjacent physical increments at most two. Replacing one coordinate by
its common endpoint value on a cap interval preserves that property:
inside the interval it is constant, and its endpoint values are unchanged.
Disjoint caps therefore preserve both hypotheses in (1).

Use the two total virtual functions from the cap-palette construction.
At each coarse rank at least one value is good. Formula (2) consequently
has at least one good option at every fine rank as well.

Retain each genuine double only at its original coarse column `2Mr`.
Every other even column selects exactly one good option, preferring the
even option. Padding and replicated columns are singletons, even when
both options are good. This creates no duplicate double label.

If `J` coarse ranks have an unavailable even option, at most `MJ` fine
ranks are intrinsically odd-only. The factor `M` is fixed independently
of height. The earlier subquadratic exceptional-count conclusion therefore
survives this refinement, provided its row-set hypotheses hold for the
new profiles. The same applies to the quadratic number of occupied slots.

Put one black point at row one in every odd column of the core. The number
of black points is then one per column plus one per retained genuine
double. Restoring the relocated genuine pairs externally would restore
the same exact excess count.

This argument does not permit arbitrary permutations of the coarse
objects after refinement. Such a permutation can destroy the adjacent
increment bound in (1). A new interpolation or a separate local-choice
proof would be required.

## 3. Exact parity exclusions for the row-one sea

Assume all inserted points have row greater than one. They occupy even
columns; sea points occupy odd columns and row one.

1. A vertical rival with one sea endpoint is impossible. If the inserted
   row is even, both coordinate differences are odd, so their squared
   length is two modulo four. If the inserted row is odd, any integral
   length is odd, whereas the sum of endpoint rows is even. The proposed
   vertical endpoints would have half-integral rows.
2. A mixed four-support with exactly one sea point is impossible: the
   sum of its four black column coordinates must be even, while one odd
   column and three even columns have odd sum. A support with three sea
   points is excluded in the same way.
3. A right triangle with one inserted point and two sea points has no
   in-strip completion. A right angle at a sea point would require the
   inserted point in its column. A right angle at the inserted point
   completes at row `2-y<=0`.
4. A right triangle with two inserted points and one sea point has its
   completion in an odd column. Therefore no such completion lands at
   an inserted column. The FW issue is absent inside this core.

The second statement uses only the midpoint identity for a diagonal pair
and an opposite-side pair. It also applies to the analogous hidden
rectangle parity identity.

## 4. Remove the additional sea-vertex case by a row split

A right angle at the sea point, with two inserted endpoints, is impossible
unless both inserted rows are even. Each horizontal leg is odd. If at
least one inserted row is odd, the product of the vertical legs is even,
so the dot product is odd.

Suppose every even inserted row satisfies

\[
 y>(h+1)/2.
 \tag{5}
\]

In the remaining case, the completion row is `y_1+y_2-1>h`, outside the
strip. This removes sea-vertex triangles for this upper-half even-row
block. A reflected version handles a corresponding lower-half block
when its boundary row and row parities are chosen correctly. No all-height
cover is asserted here.

For a right angle at an inserted point `A`, with the other inserted point
`C` and a sea point, write `C-A=(X,delta)` and the sea leg as
`(xi,1-y_A)`. The equation is

\[
 X\xi=-\delta(1-y_A).
\]

Here `X` is even and `xi` is odd. If `A` is even, parity forces `delta`
even, giving the intended parked completion at row `1+delta`. If `A`
is odd, parity does not force `delta` even. The proposed automatic parking
claim is therefore false. An exact counterexample at height five is

\[
 A=(0,3),\qquad C=(2,4),\qquad B=(1,1),\qquad W=(3,2).
\]

The two legs at `A` are `(2,1)` and `(1,-2)`, with zero dot product.
The completion is in-strip and has the opposite row parity from its
row-one sea column. The even inserted row four satisfies (5). Thus the
upper-half split does not remove this new fatal family. A different
spacing or modular rule is required before this profile can support the
desired reduction.

## 5. What remains

The parity sieve still leaves inserted-only supports, mixed supports with
two sea points, and collisions between parked triples. It does not prove
the H7 list is complete for this different sea. In particular, the shared
corner reductions must be rederived, and the R2s row bound must be checked
with the new locality and row classes before any cap count is imported.

The filled end collars, the reflected height cover, and a choice mechanism
for the dense even-column point set also remain. This note supplies an
interpolation lemma and a local parity reduction, not an unconditional
quadratic-width construction.
