# Four low two-row profiles cover every bulk label

15 November 2026. The following four period-four seas give valid bulk
one-double windows and exclude every right triangle made of one odd label,
one even label, and one sea point, independently of the label order.

| Odd label residue | Even label residue | Odd-column row L | Row F at columns 2 mod 4 |
|---|---|---:|---:|
| 3 mod 4 | 0 mod 4 | 1 | 2 |
| 3 mod 4 | 2 mod 4 | 1 | 4 |
| 1 mod 4 | 0 mod 4 | 3 | 6 |
| 1 mod 4 | 2 mod 4 | 3 | 8 |

Columns divisible by four are label slots. In the one-double theorem,
only column zero is occupied by a double and the other such slots are
empty. In a dense core, all such slots can carry labels. The remaining
multi-label supports and the collars are not proved valid here.

## 1. A general two-row sea theorem

Let \(L\) be positive and odd, and let \(F\) be even with
\(F\ge2L\). Put row \(L\) at every odd column, row \(F\) at
columns \(2\pmod4\), and no black point at columns \(0\pmod4\).
This sea is identifying in the positive integer half-plane.

There is one black point per occupied column. A right angle at the lower
row with two upper-row endpoints is impossible modulo four: both
horizontal leg products and the squared vertical difference are one
modulo four. A right angle at the upper row with two lower endpoints
completes at row \(2L-F\le0\). A right angle at one of two equal-row
points would require two black points in one column. Thus the sea has no
admitted black right triangle, and no zero- or one-white presentation.

For two-white presentations, diagonal/diagonal uniqueness follows from
the three distinct possible black row sums \(2L,L+F,2F\), followed by
the one-point-per-column condition. Side/side uniqueness follows from the
unique nonzero ordered row difference, with horizontal sides again fixed
by their columns. In a mixed presentation, an equal-row black pair has
squared distance of even 2-adic valuation; a distinct-row pair has squared
distance of valuation one. Thus either both pairs have equal rows, in
which case the common white horizontal pair coincides with the black
diagonal, or both pairs use \(L,F\). In the latter case their midpoint
vertical displacement is zero, and perpendicularity forces zero
horizontal displacement, making the side rectangle degenerate.

## 2. One bulk even point can be added

Add \(E=(0,b)\), where
\[
 b>2F,\qquad b\equiv F+2\pmod4.                          \tag{1}
\]
A right angle at \(E\) completes below row one. With distinct sea rows,
a right angle at the lower row \(L\) is impossible modulo four:
the horizontal and vertical terms in its dot product are both three,
so their sum is two modulo four. A right angle at \(F\) has white
row \(b+L-F>F\). Its white column determines the middle sea column by
the perpendicularity equation, so its completion is unique. There are no
sea-only admitted right triangles to compete with it.

For two-white presentations containing \(E\), the row sums exclude
diagonal/diagonal collisions, and the row differences exclude side/side
collisions. The point \(E\) cannot belong to both rectangles, since
that would give three common vertices.

The squared distance from \(E\) to an \(F\) point has valuation
three: both differences are two modulo four. The distance from \(E\)
to an \(L\) point has valuation one. A sea-only pair has even valuation
if its rows agree, and valuation one otherwise. Hence the only mixed case
uses \(E\) with an \(L\) point, against a sea pair at \(L,F\).
If \(E\) belongs to the black side, the lower common white row is
\(L+(F-b)/2<0\), by \(b>2F\ge F+2L\).

It remains to put \(E\) on the black diagonal. Write the black side
as \((x,L),(y,F)\), and the black diagonal as \((z,L),(0,b)\).
Set
\[
 u=y-x,\quad v=-z,\quad t=z-x,\quad
 d=F-L,\quad\delta=b-F.
\]
Here \(u,v,d\) are odd, \(t\) is even, \(y\equiv2\pmod4\),
and \(\delta\equiv2\pmod4\). Equal norms and perpendicularity give
\[
 u^2-v^2=2d\delta+\delta^2,
 \qquad 2ut=u(u-v)-d\delta.                               \tag{2}
\]
The second equation modulo four implies \(u-v\equiv2\pmod4\).
Since \(y=u-v-t\equiv2\pmod4\), this forces \(t\equiv0\pmod4\).
But combining the two equations gives
\[
 (u-v)^2+\delta^2=4ut.                                    \tag{3}
\]
The left side is eight modulo sixteen, whereas the right side is zero
modulo sixteen. This contradiction excludes the last mixed case.

## 3. A bulk odd point can be added in the same column

Add \((0,a)\) with odd \(a>2F\). A right triangle using this point
and two sea points is impossible or completes below the strip. At a sea
vertex, two different sea parities give an odd dot product; two same-row
points would require vertical alignment with the label column. At the
odd label itself, two same-parity sea points give an odd dot product,
and a mixed-parity pair completes at \(L+F-a<1\).

A triangle using both label points and one sea point is also impossible.
At a label vertex, its vertical leg is not perpendicular to the sea leg.
At the sea vertex, both label rows are higher, and the dot product is
\(x^2+(a-f)(b-f)>0\).

Every sea point and the even label belong to the checkerboard class
\(x+y\equiv0\pmod2\); the odd label belongs to the other class.
In any two-white collision newly involving the odd label, one black pair
would therefore have odd squared length and the other even squared length.
All three presentation types require equal lengths. A shared odd label
would instead give three common vertices and the same rectangle.
Thus adding the odd point preserves the identifying property.

This proves the one-double theorem for every \(L,F\) satisfying the
initial assumptions and for \(a,b>2F\) with (1).

## 4. Exclude opposite-parity label/label/sea triangles

Now allow any number of label columns divisible by four. Within one
profile, require
\[
 a\equiv L+2\pmod4\quad\text{for every odd label row},
 \qquad b\equiv F+2\pmod4\quad\text{for every even label row}.
\tag{4}
\]
Consider a triangle with one label point of each parity and one sea point.
The following residues exclude a right angle at every vertex.

* At an \(L\) sea point, the horizontal product is odd and the
  vertical product is even.
* At an \(F\) sea point, the horizontal product is zero modulo four,
  and the vertical product is two modulo four.
* At the odd label with an \(L\) sea point, the horizontal product is
  zero modulo four and the vertical product is two modulo four.
* At the odd label with an \(F\) sea point, the horizontal product is
  even and the vertical product is odd.
* At the even label with an \(L\) sea point, the horizontal product is
  even and the vertical product is odd.
* At the even label with an \(F\) sea point, the horizontal product is
  zero modulo four and the vertical product is two modulo four.

The four profiles in the opening table satisfy (4) for every combination
of the two label residues. No reflection or restriction on the height's
residue class is needed. The finitely many rows at most 16 remain outside
the bulk theorem.

## 5. What remains for a dense core

Right triangles with two same-parity label points can remain. Their fourth
column is an ordinary sea column of the same sea type as their sea vertex.
At a label right-angle vertex, the completed row differs from that sea
row by a nonzero multiple of four. At a sea right-angle vertex, the only
possible case has two even labels and an \(F\) point; its completed
row is again congruent to \(F\pmod4\). Thus these completions are
white and have the same parity as the existing sea point at their column.
This excludes a direct opposite-parity axis owner but does not exclude
two such triangles sharing a white completion.

Multi-label two-white and six-black supports, all-label right triangles,
the order of the doubles, and joins between profiles remain open.
The sea and one-double theorems do not establish a full quadratic-width
blackout. They provide four explicit low-row profiles and a uniform
modular exclusion without the cap-singleton or parity-reflection issue.

Independent review checked the full written proof, including the
two-level sea, both even-label mixed role assignments, odd-label
insertion, and all six modular right-angle exclusions. It also confirmed
the separate sea-vertex triangle with two even labels retained in Section 5.
The lower-sea dot-product wording was corrected during that review.
