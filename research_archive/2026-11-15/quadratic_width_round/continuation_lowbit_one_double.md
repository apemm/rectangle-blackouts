# Two lowbit profiles admit every bulk one-double window

15 November 2026. Fix \(S=2^e\ge4\) and \(c\in\{0,2\}\).
At columns not divisible by \(S\), use the sea row
\[
 c+2^{v_2(x)}.
\]
Leave all multiples of \(S\) empty except column zero, where a double
has odd row \(a\) and even row \(b\). Suppose
\[
 a>S+2c,\qquad b\equiv c\pmod S,\qquad b-c\ge2S.         \tag{1}
\]
Then the resulting black set is identifying in the positive integer
half-plane. Finite-strip restrictions preserve the result.

In particular, at \(S=4\), the profiles with sea rows \((1,2)\)
and \((3,4)\) cover the two residue classes of bulk even rows. This is
a one-double theorem. It does not assign many doubles simultaneously or
fill unused arithmetic slots in a sparser placement.

## 1. Add the even label point first

Translate rows down by \(c\). The sea levels are the powers of two
at most \(S/2\), and the even label point is \(E=(0,B)\), where
\(B=b-c\) is a multiple of \(S\) and \(B\ge2S\). The permitted
strip now starts at row \(1-c\). The translated sea is identifying
there by
[`continuation_lowbit_sea_theorem.md`](continuation_lowbit_sea_theorem.md).

For every sea point of level \(A\), its column and its row difference
from \(E\) both have valuation \(v_2(A)\). Hence their squared
distance has odd valuation and is not a square.

### One-white completions

A right angle at \(E\) completes at a row at most \(S-B\le-S\),
outside the permitted strip. A right angle at one of two equal-row sea
points would require the label column to be a sea column, impossible.

For two distinct sea levels \(A<V\), a right angle at the lower
level is impossible modulo four. Divide by \(A\). The even label's
row and column are divisible by four. If \(V/A=2\), both leg products
are \(3\pmod4\); otherwise both are \(1\pmod4\). Their sum
cannot vanish.

Thus an admitted triangle involving \(E\) has its right angle at
the middle sea level \(V\), and its white row is
\[
 y=B+A-V>S/2.                                             \tag{2}
\]
The difference \(B-y=V-A\) determines both sea levels uniquely.
If \(X\) is the white column and \(x_V\) the middle sea column,
orthogonality gives
\[
 Xx_V=(B-V)(A-V).                                         \tag{3}
\]
Here \(X\ne0\), since otherwise the two sea points would share a
column. Equation (3) determines the triangle. Its white row is above
all sea rows and below \(B\), so it is not black. Sea-only positive
completions lie below their largest sea level, hence below \(S/2\).
The possible sea-only rows \(-1,0\) for \(c=2\) are also disjoint
from (2). Therefore no one-white collision or fully black rectangle is
introduced.

### Two-white presentations

In a collision with two common white points, \(E\) cannot belong to
both rectangles: they would then share three vertices. If both black
pairs are diagonals, the pair containing \(E\) has row sum greater
than \(S\), whereas the sea-only pair has row sum at most \(S\).
If both are sides, the pair containing \(E\) has absolute row difference
at least \(B-S/2\), whereas the sea-only difference is less than
\(S/2\). Both cases are impossible.

For a mixed presentation, the sea-only black pair must use distinct
levels. Its squared distance otherwise has even valuation, contrary to
the pair containing \(E\). Equality of norm valuations makes the
two minimum sea levels equal, say \(A\).

If \(E\) is on the black side, let the other pair's higher sea row be
\(V\). The lower common white row is
\[
 A+(V-B)/2\le V-B/2\le-S/2.
\]
After adding back \(c\le2\), it remains nonpositive.

If \(E\) is on the black diagonal, divide by \(A\). Write the
side's levels as \((1,V')\) and the diagonal's levels as \((1,U')\),
where \(U'=B/A\). The integer \(U'\) is a multiple of \(2V'\),
although it need not be a power of two. If \(u\) is the side's odd
horizontal difference, perpendicularity gives
\[
 u\mid(V'-1)(U'-V').
\]
Removing the power-of-two factor \(V'\) yields
\[
 |u|\le(V'-1)(U'/V'-1)<U'-V'.
\]
The equal-norm equation instead implies \(|u|>U'-V'\). This is
the same contradiction as in the sea theorem. Thus the even point alone
preserves the identifying property.

## 2. Add the odd label point

Return to physical rows. All sea points and the even label point lie in
the checkerboard class \(x+y\equiv0\pmod2\). The new odd label
point \((0,a)\) lies in the other class.

First consider right triangles containing that odd point and two sea
points. At a sea vertex, mixed odd/even sea levels are excluded modulo
two. For two distinct even sea levels \(r,s\ge1\), orthogonality
would require
\[
 v_2(f_s-f_r)=r+v_2(x_s-x_r)=r+\min(r,s),
\]
but the actual row-difference valuation is \(\min(r,s)\). Two sea
points at one level have equal rows, and cannot give a right angle at a
sea point with the label column. At the odd label itself, two same-parity
sea rows give an odd dot product. A mixed-parity pair completes below row
one, since its fourth row is at most \(S+2c-a<1\).

A triangle containing both label points and one sea point is also
impossible. At a label point, the vertical leg to the other label is not
perpendicular to the sea leg. At the sea point, both label rows are higher,
so the dot product is
\(x^2+(a-f)(b-f)>0\).

Consequently the new odd point creates no admitted black right triangle,
and hence no fully black rectangle or one-white presentation.

Finally, any two-white collision involving the odd point would use it
in exactly one black pair, since a shared odd point would give three
common vertices. The squared length of that black pair is odd, because
its other endpoint is in the opposite checkerboard class. The other
black pair has even squared length. In every diagonal/diagonal,
side/side, or mixed two-white presentation, those lengths must agree.
This contradiction completes the proof.

## 3. Scope for the quadratic construction

The periods are fixed, so the low sea rows and excluded low label rows
are bounded independently of height. At \(S=4\), only the two even
residue classes are needed. Translation of the label column by a multiple
of \(S\) preserves the profile and theorem.

Several doubles in the same core introduce supports with two or more
label columns; none are excluded by a one-double theorem. Moreover, if
labels use a sublattice with a larger spacing than the sea period, the
remaining period-multiple columns are still empty in this theorem.
An occupancy-preserving filling of those holes requires a separate rule.
No quadratic-width board is asserted.

Independent review checked the complete proof, including even-point
completion uniqueness, both mixed cases, the shift-two boundary estimate,
all odd-point triangle cases, and the squared-distance parity argument.
The stated one-double theorem passed that review on 15 November 2026.
