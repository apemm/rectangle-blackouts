# The period-four checkerboard sea has an even-label mixed collision

15 November 2026. Matching singleton row parity to column parity excludes
the opposite-parity singleton P family. However, the proposed period-four
sea has a different collision involving one even label point and three
high-sea points. It occurs even when the low-row ordering excludes all
sea-only black right triangles.

## 1. The sea and the parity benefit

Use the sea
\[
 s(x)=\begin{cases}
 L,&x\text{ odd},\\
 F,&x\equiv2\pmod4,\\
 H,&x\equiv0\pmod4,
 \end{cases}                                               \tag{1}
\]
where \(L\) is odd and \(F,H\) are even. Label columns are
multiples of a fixed \(S\), with \(4\mid S\). At those columns,
replace the sea point by the prescribed opposite-parity double.

Two singleton points of opposite row parity also have opposite column
parity. Their squared distance is therefore \(2\pmod4\), and is
not a square. The same applies to an even label point and an odd singleton.
Thus only an odd label point can participate in the opposite-parity
label-to-singleton P family. This observation does not exclude mixed
supports whose black sea points all lie in the same even row.

## 2. An explicit mixed support

Let the even label point be
\[
 E=(0,b),\qquad b=H-8z,
\]
where \(z\ge2\) is an integer and \(1\le b<H\le h\). Suppose
the three columns
\[
 -4,\qquad4(z^2-1),\qquad4z^2                            \tag{2}
\]
are ordinary sea columns in the same core interval. Their high-sea black
points are
\[
 A=(-4,H),\quad C=(4(z^2-1),H),\quad B=(4z^2,H).
\]
Define two common points
\[
 P=(-4,H-4z),\qquad Q=(4z^2,H-4z).                        \tag{3}
\]
All rows in (3) lie strictly between \(b\) and \(H\).

The standard Pythagorean identity gives
\[
 [4(z^2-1)]^2+(8z)^2=[4(z^2+1)]^2.                       \tag{4}
\]
More directly, the two adjacent legs of \(EPCQ\) are
\((-4,4z)\) and \((4z^2,4z)\), whose dot product is zero.
Hence \(EPCQ\) is a tilted rectangle. The points \(A,P,Q,B\)
form an axis-aligned rectangle. Their common white part is exactly
\(\{P,Q\}\): columns in (2) contain only their high-sea points.
Their symmetric difference consists of four black points \(E,C,A,B\).

The vertical leg in (4) is \(8z\), not \(4z\). This factor is
necessary for the norm identity.

For \(S=4T\) with \(T\ge5\), the congruence
\[
 z\equiv2\pmod T                                        \tag{5}
\]
ensures that neither far column in (2) is a label column:
\(z^2\equiv4\) and \(z^2-1\equiv3\pmod T\). The near column
\(-4\) is also not a label column. Thus the obstruction uses a fixed
row congruence class at arbitrarily large heights. It requires room from
the label column to column \(-4\) on its left and \(4z^2\) on its
right. It does not prove that every possible finite placement has such
room.

For example, take
\[
 h=H=200,\quad L=3,\quad F=2,\quad S=64,\quad z=10,
 \quad b=120.
\]
Translate the label column to 640. The common white points are
\((636,160),(1040,160)\). The tilted rectangle's other vertices are
\((640,120),(1036,200)\), and the axis rectangle's other vertices are
\((636,200),(1040,200)\). All three sea columns are nonzero modulo 64.
The low rows have the favorable ordering \(F<L\).

There is a companion using the low even sea for the horizontal side.
Let \(z\ge3\) be odd and put \(b=H-4z>F\). Set
\[
 E=(0,b),\quad C=(2(z^2-1),H),\quad
 P=(-2,H-2z),\quad Q=(2z^2,H-2z).
\]
The identity
\[
 [2(z^2-1)]^2+(4z)^2=[2(z^2+1)]^2
\]
proves that \(EPCQ\) is a tilted rectangle. Both common columns
are \(2\pmod4\), so the sea points \((-2,F),(2z^2,F)\)
give an axis rectangle with the same white pair. If
\(z\equiv3\) or \(5\pmod8\), then
\(v_2(2(z^2-1))=4\). Hence \(v_2(S)\ge5\) keeps the high
point \(C\) outside the label lattice. The two low-sea columns have
2-adic valuation one and are automatically nonlabel columns.
The required finite interval extends two columns to the left of the
label and \(2z^2\) columns to its right. These examples have
\(b\equiv H+4\pmod8\), complementing the first family's residue.
Neither family asserts a collision for every row in its residue class.

## 3. A separate sea-only obstruction when L is below F

If \(L<F<H\), \(H-F\equiv2\pmod4\), and
\(H+L-F\) is in the strip, put
\[
 N=(F-L)(H-F).
\]
Then \(v_2(N)=1\). For every signed odd divisor \(u\) of \(N\),
put \(v=N/u\). At any chosen completion column \(w\equiv u\pmod4\),
the points
\[
 (w-u-v,F),\quad(w-v,L),\quad(w-u,H)
\]
are sea points forming a right triangle. Their fourth corner is
\((w,H+L-F)\). If \(N>2\), there are two distinct signed odd
divisors in the same residue class modulo four: use 1 and whichever sign
of the odd part of \(N\) is congruent to 1. These give distinct
rectangles with the same one-point white completion in a sufficiently
long ordinary sea interval.

For \((L,F,H)=(1,2,8)\), the completion \((9,7)\) is shared by
black triples
\[
 \{(2,2),(3,1),(8,8)\},\qquad
 \{(14,2),(11,1),(12,8)\}.
\]
Choosing \(F<L\) and \(H+L-F>h\) removes this particular sea-only
obstruction. It does not remove the even-label support in Section 2.

## 4. A valid partial fact about the odd label

Suppose \(H-F\equiv2\pmod4\), and an odd label point \((0,a)\)
satisfies \(L\equiv a+2\pmod4\) and \(a>L+F-1\). A black right
triangle consisting of this point and two sea points cannot complete
inside the strip.

With one \(L\) point and one even sea point, a right angle at either
sea point is impossible modulo two. With an \(F\) point and an
\(H\) point, a right angle at either sea point is impossible modulo
four, since \(H-F\equiv2\pmod4\). Two sea points in the same
row cannot form a right angle at a sea point with the label: that would
require their sea column to be the label column.

At the odd label itself, two odd-row sea legs have odd horizontal product
and even vertical product. Two even-row sea legs have even horizontal
product and odd vertical product. Both cases are impossible. For an
\(L/H\) pair, the horizontal product is divisible by four but the
vertical product is \(2\pmod4\). The only remaining \(L/F\)
case completes at row \(L+F-a<1\).

Thus the odd-label triangle test can pass while the even-label mixed
support fails. The period-four proposal does not give a valid one-label
window without an additional restriction that addresses Section 2.

Independent review checked both mixed-support parametrizations, common
corners, nonlabel-column congruences, the sea-only signed-divisor
construction, and the odd-label triangle cases. The written conclusions
passed with their stated finite-interval conditions. The companion checker
passes seven mixed examples and the sea-only example.
