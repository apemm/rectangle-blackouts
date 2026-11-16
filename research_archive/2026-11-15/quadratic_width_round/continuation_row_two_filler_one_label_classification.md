# One-label classification for row-two arithmetic fillers

15 November 2026. Put row one at every column outside `4Z`, and row two
at every column in `4Z`. This period-four sea is identifying in the
positive integer half-plane. Replace its point at column zero by

\[
             O=(0,a),\quad E=(0,b),\qquad
             a\ge3,\ a\equiv3\pmod4,\quad
             b=2+4z\le h,\ z\ge1\text{ odd}.
 \tag{1}
\]

The one-label triangles have distinct parked completions, but this does
not make the one-label board valid. Every `b>=14` in the proposed class
`b=6 mod 8` has a mixed two-white collision. Only one additional unused
arithmetic slot is needed. The exceptional shallow case b=6 has no
one-label collision.

All statements refer to the indicated sea columns actually being present
inside the finite interval under consideration. There is no assertion
that several inserted labels preserve this classification.

## 1. The pure sea

Write L for a row-one point and U for a row-two point. A right angle
using three sea points with both levels must have its vertex at the
singleton level. If that vertex is U, the fourth row is zero. If the
vertex is L, the two U endpoints would need horizontal offsets +1 and
-1, since their vertical differences are both one. Their columns would
differ by two, whereas both U columns are divisible by four. Thus there
is no admitted three-black rectangle, and no hidden rectangle.

For two-white collisions of diagonal/diagonal type, the black row sums
2, 3, and 4 distinguish the row types. A fixed midpoint and length
determine a same-row pair. In the different-row case the only alternative
swaps the two endpoint columns, which would require both sea rows at the
same column. For side/side type, the nonzero row difference determines
the vertical translation, and perpendicularity determines the horizontal
translation. Horizontal sides would again require both sea rows at the
same two columns. Hence these types cannot collide.

For mixed side/diagonal type, the sum of the four black row coordinates
is even. There are therefore zero, two, or four U points. If each black
pair is horizontal, equal length and midpoint make the proposed white
diagonal coincide with its black diagonal, so the second rectangle is
degenerate. Otherwise both black pairs use the two different rows. Their
midpoints have the same height; the midpoint displacement is horizontal,
and perpendicularity to a nonvertical side makes that displacement zero.
This is again degenerate. The pure sea is identifying.

## 2. Every admitted one-label triangle

No triangle using O and two sea points completes in the positive strip.
At O the fourth row is at most `4-a`, with the possible row-two/row-two
case also excluded modulo four because `a-2` is odd. The same-row
row-one case completes at `2-a<=-1`. In the mixed-row case a right angle
at O would require a horizontal product divisible by four to cancel
`(a-1)(a-2)=2 mod 4`, which is impossible. At a row-one vertex, the
equation is

\[
                  x(y-x)=a-1\equiv2\pmod4,
\]

with `4|y` and `4 not|x`. Its left side is either 3 or 0 modulo four.
At a row-two vertex the corresponding horizontal product is divisible
by four while `a-2` is odd. A same-row sea leg at a sea vertex would
require an unavailable sea point at column zero.

A triangle using both O and E and one sea point is impossible. A label
vertex has a nonperpendicular vertical leg. At a sea vertex both label
rows are higher, so the relevant dot product is positive.

At E a triangle with two sea points completes at a row at most `4-b<1`.
A right angle at an L vertex would require

\[
                      x(y-x)=b-1\equiv1\pmod4,
\]

with the same column residues as before, and is impossible. The only
remaining right angle is at U. All such triangles are exactly

\[
 E=(0,b),\qquad U=(4k,2),\qquad
 L=(4k-z/k,1),\qquad k\in\mathbb Z\setminus\{0\},\ k\mid z.
 \tag{2}
\]

Indeed, the right-angle equation is `k(4k-x)=z`. Since z is odd, both
k and `z/k` are odd, and the L column in (2) is allowed. Their fourth
point is

\[
                        W=(-z/k,b-1).
 \tag{3}
\]

It is white at an odd column whose existing sea point has the same odd
row parity. These are precisely the parked completions. Different signed
divisors k give different W, so a single label creates no collision of
one-white presentations. The completion is never in the label column.
There is no hidden rectangle involving the label.

For labels at several columns, this injectivity no longer applies.
For two labels with the same b, write their signed completion offsets
as distinct signed divisors `d_1,d_2` of z. Their completions agree
exactly when

\[
                  x_2-x_1=d_2-d_1,
                  \qquad d_1\equiv d_2\pmod4.
 \tag{4}
\]

This statement still requires the corresponding sea columns to remain
unused. The possible spacing is at most `2z=(b-2)/2`, not z. The signed
divisors cannot be discarded.

## 3. The opposite-parity singleton P test does pass

An actual P pair between O and a row-two filler would have an odd
integer norm L and lower alternative row `(a+2-L)/2>=1`. Thus
`a-2<L<=a`, forcing `L=a`. The resulting equation

\[
                        X^2=4(a-1)
\]

is impossible: `4|X`, while the right side is 8 modulo 16. An even
label with a row-one sea point also has nonintegral distance. An odd
sea column gives squared norm 2 modulo four; a column 2 modulo four
gives squared norm 5 modulo eight.

Thus this virtual-axis P exclusion is correct. It does not exclude
the mixed collision below, whose axis rectangle uses two ordinary
row-one sea points and needs no distant row-pair owner.

## 4. Exhausting the two-white one-label cases

Same-kind diagonal/diagonal and side/side collisions with the label
are excluded by row sums or differences. The only small-row exception
to these inequalities is a=3. In diagonal/diagonal type, an O-to-L
pair could then match two U rows, but its column sum is not divisible
by four whereas the two-U sum is. In side/side type, the required
different-row sea pair has horizontal difference not divisible by four,
whereas the O-to-U pair has horizontal difference divisible by four.
If O and E belong to
different black pairs, equal midpoint or side displacement would require
row one and row two at the same sea column. If they belong to one pair,
the row sum is too large or the black side is vertical.

For a mixed support, the sum of all four black coordinates is even
in each coordinate. To see this, let P,Q be its common whites. The
black diagonal has sum `P+Q`, and the black side has sum `P+Q+2t`
for an integer translation t.

If only O is inserted, the number of U sea points must be even.
For zero U points, the O-to-L squared norm is either 5 modulo eight
or has 2-adic valuation three; it cannot equal a horizontal squared
length. For two U points, pairing O with L again cannot match the
U-to-U horizontal norm. Pairing O with U gives norm 1 modulo eight,
whereas the remaining L-to-U norm is 2 or 5 modulo eight. Thus no
one-odd mixed support exists.

If both O and E occur, row parity forces one L and one U sea point.
Column parity forces the L column to be 2 modulo four. The three
possible black pairings fail respectively by valuations three versus
at least four, residues 1 versus 5 modulo eight, or residues 1 versus
5 modulo eight. Hence two inserted points in the one double do not
create a mixed support.

It remains to use E and three sea points. Row parity forces either
one or three U points. A mixed support with E in the black side has
a common point at row at most `3-b/2<=0`, so it is outside the strip.

Suppose E is on the black diagonal with an L point and the black side
uses L and U. Write the black side as `(x,1),(y,2)` and the diagonal
as `(w,1),(0,b)`. Set `u=y-x`, `v=-w`, and `delta=b-2>0`. Equal norms
and perpendicularity imply

\[
             u^2-v^2=\delta(\delta+2),\qquad
             u(w-x-y)=-\delta.
\]

The second equation gives `0<|u|<=delta`, contradicting the first.
Thus the black diagonal must consist of E and a U point, while the
black side is horizontal.

Write the U point as `C=(4k,2)`. Its norm from E is integral exactly
when

\[
                         k^2+z^2=l^2.
 \tag{5}
\]

Since z is odd, k is even and l is odd. The common horizontal pair is

\[
                P=(2(k-l),2+2z),\qquad
                Q=(2(k+l),2+2z).
 \tag{6}
\]

Both columns are 2 modulo four. Therefore its horizontal black side
can only use the row-one sea, not row-two fillers. Conversely, every
nonzero signed k satisfying (5), with the indicated columns present,
gives exactly such a mixed collision. This exhausts the admitted
two-white supports involving the single inserted label.

## 5. The explicit obstruction and the shallow exception

For every odd z>=3, take

\[
               k=(z^2-1)/2,\qquad l=(z^2+1)/2.
\]

Then (6) becomes

\[
 E=(0,2+4z),\quad C=(2(z^2-1),2),
 \quad P=(-2,2+2z),\quad Q=(2z^2,2+2z).
\]

The tilted rectangle `E,P,C,Q` and the axis rectangle with additional
black points `(-2,1),(2z^2,1)` have exactly the same white set `{P,Q}`.
All common rows lie strictly between 2 and b. Only the nonzero
arithmetic column `2(z^2-1)` needs to be an unused filler slot.
The finite interval needs room two columns to the left and `2z^2`
columns to the right. Adding the odd point O at zero cannot change
this collision.

For z=1, equation (5) has only k=0, which is unavailable because column
zero is the double. The preceding classification then has no hidden
rectangle, no repeated parked completion, and no two-white collision.
Thus the one-label window with b=6 and a=3 modulo four is identifying.
This is a fixed shallow row, not coverage of the even label pool.

The first obstruction at b=14 has C=(16,2), P=(-2,8), and Q=(18,8).
It already defeats the proposed complementary residue class.

## 6. Finite complete checks

The [checker](check_row_two_filler_one_label.py) enumerates every rectangle
with at least two black corners, using every black pair both as a side
and as a diagonal. Any collision has at most two common white points,
since three common vertices determine a rectangle. It compares the
resulting white presentations directly.

The [saved checks](check_row_two_filler_one_label.json) pass six finite
windows. Three b=6 windows have no collision. The b=14 and b=22 windows
have exactly the predicted left/right mixed presentations, and every
singleton completion has the signed-divisor form (3). These finite checks
support the classification; the preceding proof supplies its general scope.

Independent written review passed on 15 November 2026. It checked the
pure sea, every triangle vertex case, signed completion uniqueness,
singleton P exclusions, small-a same-kind cases, all mixed norm residue
pairings, the crossed-case divisibility contradiction, and the b=6 exception.
