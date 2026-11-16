# Mixed four-point supports in a Hilbert placement

14 November 2026. This supplements
[the Hilbert placement](continuation_hilbert_placement.md).
It gives a structural reduction at stride \(O(h^{1/4})\), not a
constant-stride completion theorem.
The algebra, parity cases, and strict bounds have passed an independent
proof audit.

Let \(S\ge32\) be a power of two. Keep the original Hilbert ranks and
place each parity label at a distinct column divisible by \(S\), with
increasing rank differences giving horizontal separation at least \(S\)
times the rank difference. Arbitrary local choices
\(x_r=S(Mr+\xi_r)\), \(0\le\xi_r<M\), are allowed.

**Theorem.** If
\[
 S^4\ge1024h,
 \tag{1}
\]
there is no mixed four-point support whose black side has a nonzero
horizontal component. A remaining mixed support must have its black
side equal to the two points of a single label column. It is then exactly
an opposite-parity vertical P-rival.

The placement also has no tilted black right angle, by Theorem 2 of the
placement note. Thus the general mixed side/diagonal family is not a
second obstruction at this stride: its remaining part is the vertical
P-family. This does not remove that family, and it does not handle
supports involving filler points.

## 1. Geometric formulation

Write the black side as \(A,B\), and the black diagonal as \(C,D\).
All four black points are distinct. Put
\[
 U=B-A,\qquad V=D-C,\qquad
 T=\frac{C+D-A-B}{2}.
\]
The two common corners are \(A+T,B+T\). The required equations are
\[
 |U|^2=|V|^2,\qquad U\cdot T=0.
 \tag{2}
\]
The first rectangle has positive area, so \(T\ne0\), and the two
diagonals of the second rectangle must not coincide.

For any distinct same-parity black points, Hilbert locality gives
\[
 (\Delta y)^2<\alpha|\Delta x|,\qquad \alpha=\frac{64}{S}.
 \tag{3}
\]
The inequality also holds when \(\Delta y=0\). Such points cannot share
a column, because each column has only one black point of each parity.
Every nonzero horizontal difference is a multiple of \(S\).

Since \(S\) is even, equality of the norms in (2) implies that the
vertical components of \(U\) and \(V\) have the same parity. There are
two cases.

## 2. Both paired segments have even vertical component

Both endpoints of each paired segment have the same parity.
Let their positive horizontal spans be \(X,Z\), with vertical
components \(Y,W\). If \(X\ne Z\), then
\[
 |X^2-Z^2|\ge S(X+Z),
 \qquad
 |Y^2-W^2|<\alpha\max(X,Z).
\]
This contradicts equal norms, because \(S\ge\alpha\).
Thus \(X=Z\), and \(|Y|=|W|\).

Orient both segments with positive horizontal component. If \(W=Y\),
the black diagonal is the same segment as the common-corner diagonal,
so the second rectangle degenerates. The only genuine case has
\(W=-Y\ne0\). Translate coordinates to write
\[
 A=(0,a),\ B=(X,b),\ C=(Z_0,c),\
 D=(Z_0+X,c-Y),\qquad Y=b-a.
\]
The perpendicularity equation becomes
\[
 XZ_0+Y(c-b)=0.
 \tag{4}
\]
The second rectangle is axis-aligned.

If the two paired segments have different parities, \(c-b\) is odd.
Equation (4) and \(S^2\mid XZ_0\) give \(S^2\mid Y\).
Also \(Z_0\ne0\), since otherwise (4) would require \(c=b\), contrary
to parity. By (3),
\[
 |c-b|=\frac{X|Z_0|}{|Y|}
 >\frac{S|Y|}{\alpha}
 \ge\frac{S^4}{64}.
 \tag{5}
\]
This is impossible under (1).

If all four black points have the same parity, \(Z_0\ne0\) because the
points \(A,C\) are distinct. Apply (3) to \(A,B\) and to \(B,C\).
Squaring (4) gives
\[
 X Z_0^2<\alpha^2|Z_0-X|
 \le\alpha^2(X+|Z_0|)
 \le\frac{2\alpha^2}{S}X|Z_0|.
\]
Consequently \(|Z_0|<2\alpha^2/S\), contradicting
\(|Z_0|\ge S\) and \(S^2>2\alpha^2\).
This excludes the even-component case.

## 3. Both paired segments have odd vertical component

Orient \(C,D\) so that \(A,C\) have the same parity and \(B,D\) have
the other parity. Write
\[
 U=(X,Y),\quad C-A=(m,p),\quad D-B=(n,q).
\]
Here \(Y\) is odd, \(p,q\) are even, and
\[
 p^2<\alpha|m|,\qquad q^2<\alpha|n|.
 \tag{6}
\]
We assume \(X\ne0\); the vertical black-side case is retained below.
All of \(X,m,n\) are nonzero multiples of \(S\).

Perpendicularity is
\[
 X(m+n)+Y(p+q)=0.
 \tag{7}
\]
Neither \(m+n\) nor \(p+q\) is zero: otherwise both are zero and
\(T=0\). Since \(Y\) is odd, (7) gives
\[
 S^2\mid(p+q),\qquad |p+q|\ge S^2.
 \tag{8}
\]
Set \(M=\max(|m|,|n|)\). Equation (6) then implies
\[
 |p+q|<2\sqrt{\alpha M},
 \qquad \sqrt M>\frac{S^2}{2\sqrt\alpha}.
 \tag{9}
\]

If \(|m+n|\ge M/2\), equations (7) and (9) yield
\[
 |Y|=\frac{|X||m+n|}{|p+q|}
 >\frac{S\sqrt M}{4\sqrt\alpha}
 >\frac{S^3}{8\alpha}=\frac{S^4}{512}.
 \tag{10}
\]
This contradicts \(|Y|\le h-1\).

It remains that \(|m+n|<M/2\). Now \(m,n\) have opposite signs,
so \(|n-m|\ge M\). Equal norms and (7), after eliminating \(Y\),
give the exact identity
\[
 4X(mq-np)=\bigl((n-m)^2+(q-p)^2\bigr)(p+q).
 \tag{11}
\]
In particular \(mq-np\ne0\). Substitution back into (7) gives
\[
 |Y|=
 \frac{\bigl((n-m)^2+(q-p)^2\bigr)|m+n|}
 {4|mq-np|}.
 \tag{12}
\]
Use \(|m+n|\ge S\) and
\[
 |mq-np|<2M\sqrt{\alpha M}.
\]
Then
\[
 |Y|>\frac{S\sqrt M}{8\sqrt\alpha}
 >\frac{S^3}{16\alpha}=\frac{S^4}{1024},
 \tag{13}
\]
again contradicting (1). This finishes the nonvertical case.

## 4. What the remaining vertical case is

If \(X=0\), the two black points \(A,B\) occupy a single label column,
so their row difference is odd. The perpendicular translation \(T\)
is horizontal. Thus the common corners \(A+T,B+T\) form a vertical
segment with exactly the same two rows as that label.

The other black pair \(C,D\) has that segment's midpoint and integral
length \(|A_y-B_y|<h\). Its endpoints have opposite parity. This is
precisely the vertical P-rival supported by the owner label \(\{A_y,B_y\}\).
The explicit surviving rival in Section 6 of the placement note has this
form. No filler choice can remove such a collision.

Taking \(S\) to be the least power of two at least
\(\max\{32,(1024h)^{1/4}\}\) preserves width \(O(h^{9/4})\), including
any fixed number of private choices. The unresolved task is to exclude
the P-rivals and the filler supports without a growing stride.
