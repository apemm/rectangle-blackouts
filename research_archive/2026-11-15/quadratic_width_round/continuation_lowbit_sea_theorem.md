# The lowbit sea and its shift by two are identifying

15 November 2026. Let
\[
 \mathcal B=\{(x,2^{v_2(x)}):x\in\mathbb Z\setminus\{0\}\}.
\]
As black sets in the integer positive half-plane, both \(\mathcal B\)
and its vertical translate \(\mathcal B+(0,2)\) are identifying:
no two distinct lattice rectangles have the same white part.

The same holds after restricting to any finite strip and deleting any
black points. In particular, for every \(S=2^e\), the sea that puts
\(2^{v_2(x)}\), or \(2+2^{v_2(x)}\), at columns \(S\nmid x\)
and leaves the other columns empty is identifying. This theorem concerns
the sea alone. Adding label doubles still requires separate support tests.

## 1. Elementary properties

There is one black point per occupied column. The positive power-of-two
rows have unique unordered two-term sums and unique nonzero ordered
differences. For example, a nonzero difference has the form
\(2^r(2^s-1)\), so its valuation and odd part recover both exponents.

For black points in distinct rows, the horizontal and vertical differences
have the same 2-adic valuation, equal to the smaller row exponent.
Their squared distance therefore has odd 2-adic valuation. For two black
points in the same row, their squared distance is an integer square and
has even 2-adic valuation.

Three common rectangle vertices determine the rectangle. Therefore a
collision between distinct rectangles can have at most two white points.
It remains to exclude fully black rectangles, repeated one-white
completions, and repeated two-white presentations.

## 2. Every positive one-white completion is unique

Consider a right triangle of three black points. A right angle at one
of two equal-row points would require a second black point in its column,
so that case is impossible. If the two equal-row points are the endpoints
of the hypotenuse, and their row is below the right-angle vertex, the
fourth row is nonpositive. If their row is above the right-angle vertex,
divide coordinates by the lower row. The two leg products are each
\(1\pmod4\), so their dot product is \(2\pmod4\), impossible.

Now suppose the three rows are distinct. A right angle at the highest
row completes at a nonpositive row. A right angle at the lowest row is
impossible modulo four. To see the latter, divide coordinates by that
lowest row. Its column is odd. If the two higher rows are both at least
four, both horizontal leg products and vertical leg products are
\(1\pmod4\). If one higher row is two, both products are
\(3\pmod4\). Either way their sum is \(2\pmod4\).

Thus every positive completion has distinct rows \(a<b<c\), with the
right angle at \(b\), and its fourth row is
\[
 y=a+c-b.                                                 \tag{1}
\]
The row \(y\) determines these three levels. First
\(a=2^{v_2(y)}\). Writing \(b=aV,c=aU\), the equation
\(y/a-1=U-V\) determines \(V\) by its valuation and then \(U\).
In particular \(y\) is not a power of two, so the fourth point is white.

Divide all coordinates by \(a\), and write \(U=VR\), where
\(V,R\) are powers of two at least two. Let the horizontal leg from
the middle point to the low point be \(u\), and the horizontal leg
to the high point be \(Vw\). Both \(u,w\) are odd. Orthogonality is
\[
 uw=(V-1)(R-1)=K<U.                                      \tag{2}
\]
The completion column \(X\) equals the high column plus \(u\).
The high column has valuation \(\log_2U\), so
\[
 u\equiv X-U\pmod{2U}.                                  \tag{3}
\]
But \(u\) is a signed divisor of \(K\), hence \(|u|<U\).
There is at most one such integer in a prescribed residue class modulo
\(2U\). Equations (2)–(3) determine every vertex. This proves uniqueness
and also excludes a fully black rectangle.

## 3. Two-white presentations of the same kind

If both rectangles use the common white pair as a diagonal, their black
diagonals have the same midpoint and length. The unique power-of-two row
sums fix the unordered black row pair. The only possible second pair
would interchange the two columns between these rows, requiring two
black points in a column. Thus the black pair is unique.

If both rectangles use the common white pair as a side, order that pair
once and for all. Its nonzero vertical difference fixes the ordered black
row pair. Perpendicularity then determines the horizontal translation
uniquely. A vertical side cannot be black, since columns have one point.
For a horizontal common side, every black side uses its two fixed columns,
and again there is at most one possible row. Thus this presentation is
also unique.

## 4. A mixed diagonal/side presentation is impossible above the axis

Suppose a black side and a black diagonal have equal length and correspond
to the same white pair. By the valuation fact in Section 1, either both
black pairs have equal-row endpoints or both have distinct-row endpoints.
The equal-row case would force the common white horizontal pair to
coincide with the black diagonal, which is degenerate.

In the distinct-row case, the two pairs have the same minimum row, by
the valuation of their squared lengths. Divide all coordinates by that
row. Write the side's row pair as \((1,V)\) and the diagonal's row
pair as \((1,U)\), where \(U,V\ge2\) are powers of two. The
black coordinates remain integers after this division. Write their
signed horizontal differences, from the low point to the high point,
as \(u,v\). Both are odd.

The lower common white row is
\[
 1+(U-V)/2.                                               \tag{4}
\]
If \(U<V\), this is nonpositive. If \(U=V\), the midpoint
vertical displacement is zero, so perpendicularity forces zero horizontal
displacement as well. The side rectangle degenerates.

If \(U>V\), write \(U=VR\). Let the low diagonal point be
horizontally displaced by an integer \(t\) from the low side point.
Perpendicularity gives
\[
 2ut=u(u-v)-(V-1)(U-V).
\]
Thus \(u\mid(V-1)(U-V)\). Since \(u\) is odd and \(V\)
is a power of two,
\[
 |u|\le(V-1)(R-1)<U-V.                                   \tag{5}
\]
Equal lengths instead give
\[
 u^2-v^2=(U-V)(U+V-2)\ge(U-V)^2,
\]
and \(v\ne0\), so \(|u|>U-V\), contradicting (5).
This proves the unshifted theorem.

## 5. The additional rows admitted by a shift of two

A vertical shift does not change rectangle identities. To prove the
shift-by-two theorem, it suffices to include original white rows \(-1,0\)
in the preceding uniqueness tests.

A completion at row zero must have two equal low endpoints at row \(a\)
and right-angle vertex at row \(2a\). Dividing by \(a\), the two
horizontal legs are odd and have product \(-1\), so they are 1 and
\(-1\). The completion column equals the right-angle column. Its
valuation determines \(2a\), and the triangle is unique.

A completion at row \(-1\) must use rows \(1,2,4\), with the right
angle at row four. Equal endpoint rows give an even completion and cannot
occur. In the distinct-row case, valuation gives the lowest row one, and
\(1+V-U=-1\) forces \((V,U)=(2,4)\). Write the horizontal legs
to rows one and two as \(u,2w\). Then \(uw=-3\). The four choices
\(u=1,-1,3,-3\) give \(u+2w=-5,5,1,-1\). The right-angle column
is \(4\pmod8\), so these give four distinct completion residues
modulo eight. The column therefore determines a unique triangle.

For a mixed presentation, (4), multiplied by its minimum black row,
can be at least \(-1\) with \(U<V\) only in two cases:
\((U,V)=(2,4)\), or \((U,V)=(4,8)\) with minimum black row one.
Both are impossible:

* For \((2,4)\), reflection lets \(u>0\). The norm equation
  \(u^2-v^2=-8\) forces \(u=1,v=\pm3\). The perpendicularity
  formula gives \(t=2\) or 5. The two low-row columns are odd, so
  \(t\) must be even. Hence \(t=2,v=3\). The high side column
  \(x+1\) has valuation two, so \(x\equiv3\pmod8\). The high
  diagonal column \(x+5\) is then divisible by four, contrary to its
  row two.
* For \((4,8)\), the odd norm solutions have
  \((u,|v|)=(3,7)\) or \((9,11)\). Perpendicularity would require
  \(u\mid28\), which neither value satisfies.

The diagonal/diagonal and side/side arguments do not depend on row positivity.
This proves the shifted theorem too.

## 6. Limits and a sharp obstruction to further positive translation

At original white point \((20,-2)\), the unshifted sea has two black
triangles:
\[
 \{(28,4),(29,1),(19,1)\},\qquad
 \{(20,4),(23,1),(17,1)\}.
\]
Their right-angle vertices are the row-four points. Translating the sea
up by any integer at least three puts this collision in the positive
strip. The points are present at every period \(S\ge8\).
In particular, the parity-compatible shift four fails.

Finally, black-set deletion preserves the identifying property: a collision
requires the full symmetric difference of two rectangles to be black.
Deleting black points cannot create such a containment. This justifies
all finite-strip restrictions and period truncations asserted at the start.
It does not justify adding doubles at the empty arithmetic columns.

Independent review checked the entire proof, including all right-angle
row cases, signed-divisor uniqueness, both mixed branches, the additional
white rows admitted by shift two, and the explicit failure at row minus
two. The theorem passed that review on 15 November 2026.
