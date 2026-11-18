# Linear-width joins for two narrow bands of rows

Fix a lower interval \(I\) and an upper interval \(J\) in the rows \(1,\ldots,h\). Each has diameter at most \(c\), where \(1\le c\le D=h-1\). Use odd rows in \(I\) and even rows in \(J\). Suppose
\[
 2\max I-\min J<1,\qquad 2\min J-\max I>h .
\]
Write \(P\) for any set of black singleton cells on these rows, with at most one point in each column. An interval of columns can be missing. The following linear bound allows the values in both bands to vary.

## Bounds on the support of a failure

A tilted rectangle with three black corners has horizontal span at most \(2cD\). Two such rectangles with the same missing corner have combined span at most \(4cD\).

To see this, take the legs at the black right angle. If either leg has both endpoints in one band, the product of the absolute horizontal components equals the product of the absolute vertical components. This product is at most \(cD\). Both horizontal components are positive in absolute value, so each is at most \(cD\). If neither leg is within a band, the two nonpivot vertices are in the other band. The displayed inequalities put the completion outside the strip.

A mixed side/diagonal presentation with four black points has horizontal span at most \(5cD\), including both common corners. Let \(U=B-A\) be the black side and \(V=F-E\) the black diagonal. Write \(H=E+F-A-B\). As in the [locality proof](linear_collar_locality.md), \(|U|=|V|\), \(U\cdot H=0\), and the common corners are \((E+F\pm U)/2\). In a nondegenerate mixed support \(H\ne0\) and \(V\ne\pm U\). Indeed, in the first case the common corners would be \(A,B\). In the second case they would be \(E,F\). Both black pair displacements have nonzero horizontal component because \(P\) contains at most one point per column.

The sum of the four black rows is even, by integrality of the common corners. Thus zero, two or four black points come from the upper band. There are two types of pairings.

* If both pairs lie within bands, \(|U_y|,|V_y|\le c\). If \(U_y\ne0\) and \(|U_x|>2cD\), then \(|H_x|=|U_yH_y/U_x|<1\). Thus \(H_x=H_y=0\), impossible. If \(U_y=0\), then \(V_y\ne0\) and \((|U_x|-|V_x|)(|U_x|+|V_x|)=V_y^2\le c^2\). In either case \(|U_x|\le2cD\), \(|V_x|\le |U| \le 3cD\), and \(|H_x|\le2cD\).
* Otherwise both pairs run between the two bands. Orient both from low to high, and put \(d_1=U_y,d_2=V_y\). Then \(|d_1-d_2|\le 2c\) and \(|H_y|\le2c\). If \(d_1\ne d_2\), then the positive integers \(|U_x|\) and \(|V_x|\) are distinct. The absolute difference of their squares is \(|d_1^2-d_2^2|\le4cD\), so each is at most \(4cD\). If \(d_1=d_2\), their absolute horizontal components agree. A value greater than \(2cD\) gives \(|H_x|<1\) by perpendicularity, again forcing \(H=0\). In both cases \(|H_x|\le2cD\).

The midpoints differ horizontally by at most \(cD\). Every corner lies within \(2cD\) of one of them. This proves the bound.

A fully black tilted rectangle satisfies the first bound. An axis rectangle cannot be fully black in a singleton graph. Two-white collisions of the same type require a fully black rectangle. An alternative vertical diagonal to a black diagonal has horizontal span at most \(D\) on the black diagonal. When a row-pair owner is elsewhere, the bound is for the local test, as in the [locality proof](linear_collar_locality.md).

## Joining profiles

Consider any number of successive pieces. Piece \(i\) uses only two rows \(L_i\in I\) and \(B_i\in J\), with one black point per column in any order. Suppose that each chosen pair of levels excludes in-strip vertical rivals relative to the full parity partition. A sufficient condition, for \(d_i=B_i-L_i\), is the absence of positive integers \(X,Z\) satisfying
\[
  X^2+d_i^2=Z^2,\qquad Z\le B_i+L_i-2,\qquad Z\le2h-B_i-L_i .
\]
These are the two strip boundaries for the vertical alternative. Distances within a single row do not produce a vertical alternative corresponding to an opposite-parity owner.

Put \(G=5cD+1\). Between consecutive profiles add \(G\) columns at \(L_i\), followed by \(G\) columns at \(L_{i+1}\). This yields a valid singleton background relative to all parity owners. One can continue the two ends indefinitely at their respective lower rows.

For each cut, any local test of span at most \(5cD\) touching its central change sees only an ordered step between two low odd rows. Those points form a coordinatewise chain after vertical reflection if necessary. They have no tilted triangle or mixed support, by the chain argument in [the collar note](../2026-11-15/quadratic_width_round/continuation_lipschitz_collar_graphs.md). They have no opposite-parity vertical rival. Every local test missing the changes sees at most one two-level profile, including any neighboring constant columns at its own low value. The outside-completion inequalities and opposite row parity give the two-level validity theorem of that note. The assumed vertical-rival exclusion applies. The span estimates prove the assertion for arbitrarily many pieces.

For fixed \(L\), only \(O_L(\sqrt h)\) possible high rows \(B\) in the whole strip fail the displayed sufficient condition. In a failure put \(\delta=Z-(B-L)\). Then \(1\le\delta\le2(L-1)\), and \(X^2=\delta(2(B-L)+\delta)\). For each of these finitely many positive \(\delta\), one has \(X=O_L(\sqrt h)\), and \(X,\delta\) determine \(B\). In particular, high rows differing from a common chosen center by prescribed bounded offsets can all avoid these forbidden sets for a fixed finite collection of low levels. Any separate good-row requirements for the underlying cores still apply.

As a finite check, I used a \(14\times32\) grid. Columns 1 to 4 used rows \(\{1,10\}\), and columns 29 to 32 used \(\{3,12\}\). The two middle runs had 12 columns each, at row 1 and then row 3. For each of the 256 endpoint assignments I generated rectangles by pairing diagonals of equal length and midpoint and compared all 76,356 presentations. All were distinct. These guards are shorter than the proved sufficient value.

The proof concerns singleton backgrounds whose black points lie in the two bands. It supplies joins between those backgrounds. Doubles or core points outside the bands can still interact across a cut and require their own argument.

## Extension to blocks with doubles

Allow up to two cells in a column and require that each double uses one lower odd row and one upper even row. Keep the same bands and outside-completion conditions. The tilted-triple proof applies without change. In the mixed proof, a nonvertical black side \(U\) still has \(|U_x|\ge1\). The bounds allow \(V_x=0\), since a nonzero difference of the squares of two nonnegative integers still bounds each integer. Thus every mixed case with a nonvertical black side retains the \(5cD\) bound.

It remains to interpret a vertical black side \(U\). Its column contains a double, so \(U\) has odd vertical length. The common visible corners are a vertical segment with that same row pair, translated horizontally from the black side. The black diagonal \(V\) and this vertical segment have the same midpoint and length. Its two endpoints and the visible segment occupy at most \(D\) columns of horizontal span, because \(|V|=|U|\le D\). The row pair must be an edge of the prescribed final partition. A local vertical-alternative test with all final owners therefore excludes this mixed case even if the actual double column is remote. Here, as throughout, a nondegenerate mixed support has \(H\ne0\).

Consequently the same linear guards join clean blocks carrying actual doubles, under the following hypotheses.

1. Each block lies in the two bands and is clean relative to the same final parity-pair graph when continued on both sides in its own constant low row \(L_i\).
2. All block row pairs are distinct and belong to the prescribed parity graph. This supplies the axis ownership and axis-axis checks.
3. Between blocks use the two \(G\)-column guards from the preceding construction.

A local failure touching a central low-row change stays in the monotone singleton step. Every other bounded local failure is contained in one of the extended blocks. A vertical remote owner is covered by the final graph in the first hypothesis. This proves the gluing assertion for the doubles as well. Applying it to all labels would still require suitable blocks for the remaining row ranges.
