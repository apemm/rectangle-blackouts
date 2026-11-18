# A linear locality bound for singleton graphs and a quadratic obstruction at a constant tail

Write \(D=h-1\). Coordinates are (column, row). The two results concern different parts of a collar. The first gives the width of the tests inside a background with bounded slope. The second applies to an endpoint of the two-level profile used in the [November 15 collar](../2026-11-15/quadratic_width_round/continuation_lipschitz_collar_graphs.md).

## 1. Locality for a graph of singleton rows

Let \(P\) contain at most one black point per column. Suppose \(C\ge1\) and every \(A,B\in P\) satisfies
\[
 |A_y-B_y|\le C|A_x-B_x|.
\]
The set of columns can have gaps. The following bounds concern rectangles contained in the height-\(h\) strip.

1. A tilted rectangle with three black corners has horizontal span at most \(2CD\). Two such rectangles with the same missing corner have combined span at most \(4CD\).
2. A mixed side/diagonal presentation with four distinct black points has horizontal span at most \(3CD\), including the two common corners.
3. A black diagonal with an alternative vertical diagonal has horizontal span at most \(D\). This measures the local diagonal. The column owning a prescribed row pair elsewhere can be farther away.

For the first assertion let \((s,u),(t,v)\) be the legs at the black right angle. Then \(st=-uv\) and both legs join black points. Hence \(|s|\le C|v|\le CD\) by applying the slope condition to \((t,v)\). The same inequality holds for \(|t|\). The rectangle has span at most \(|s|+|t|\). Two rectangles with a common corner meet there, so their spans add.

For the second assertion let \(A,B\) be the black side and \(E,F\) the black diagonal. Orient \(U=B-A\) and \(V=F-E\) so their horizontal components are positive. Put
\[
 H=E+F-A-B,\qquad J=U-V .
\]
The two common corners are \((E+F\pm U)/2\). Thus \(H\cdot U=0\). Since \(|U|=|V|\), also \(J\cdot(U+V)=0\).

Suppose \(U_x>CD\) and \(U_x+V_x>2CD\). The two perpendicularities imply
\[
 |H_x|\le |H_y|\, |U_y|/U_x,\qquad
 |J_x|\le |J_y|\, |U_y+V_y|/(U_x+V_x).
\]
Both ratios are strictly below \(1/C\). Write \(B_1=E-A\) and \(B_2=F-B\). Then \(H=B_1+B_2\) and \(J=B_1-B_2\). The real identity \(|u+v|+|u-v|=2\max(|u|,|v|)\) gives
\[
 \max_i |(B_i)_x| < C^{-1}\max_i |(B_i)_y| .
\]
If both vertical components vanish, the preceding inequalities already force both \(B_i=0\). Otherwise the displayed strict inequality contradicts the slope condition. This proves \(U_x\le CD\) or \(U_x+V_x\le2CD\). In the first case \(V_x\le |U|\le \sqrt{C^2+1}D\). Hence both horizontal components are at most \(2CD\) in either case.

The black-pair midpoints differ by \(H/2\). The slope condition on \(U\) gives \(|H_x|/2\le C|H_y|/2\le CD\). Every corner lies within \(CD\) horizontally of one of the two midpoints. This proves the claimed bound. Finally, a possible vertical diagonal has length at most \(D\), which proves the third assertion.

These estimates let tests with an external parity-pair owner use a \(4CD+1\) guard whenever the entire local background under comparison satisfies the same slope condition. The hypothesis concerns every pair of black points in that background. In particular, a double column, or a jump of order \(h\) in adjacent columns, requires a separate argument.

## 2. Where an eventual constant tail can start

Suppose \((x,B)\) and \((x+s,L)\) are black, where \(s>0\) and \(d=B-L>0\) is odd. Fix a row \(T>B\). Suppose \(s\mid d(T-B)\), and put
\[
 X=d(T-B)/s.
\]
Assume the grid contains columns \(x+X\) and \(x+X+s\). If both are row-\(T\) singletons and the board contains the double \(\{T,T-d\}\), then the board has two rectangles with the same presentation.

Indeed, the vectors \((s,-d)\) and \((X,T-B)\) are perpendicular at \((x,B)\). The three black corners \((x,B),(x+s,L),(x+X,T)\) complete at
\[
 W=(x+X+s,T-d).
\]
Since \(T>B\), its row exceeds \(L\) and belongs to the strip. Its column contains just the black point in row \(T\), so the presentation of this tilted rectangle is \(\{W\}\). Let \(c\) be the column of the double \(\{T,T-d\}\). Then \(c\ne x+X+s\), since the latter is a singleton. The axis rectangle with columns \(c,x+X+s\) and rows \(T,T-d\) has the same presentation \(\{W\}\). It is distinct from the tilted rectangle regardless of whether \(c\) coincides with an earlier column.

Every equality board for the ordinary parity partition contains this double because \(d\) is odd. In a board continued to the right by a permanent row-\(T\) singleton tail, the tail cannot start at or before \(x+X\). For adjacent high and low cells, \(s=1\), this gives the lower bound \((B-L)(T-B)\) measured from the high cell. It also applies to a finite board whenever the proposed tail includes both required columns.

In the archived low-sea profile the high row \(B\) occurs at multiples of four and the adjacent column contains the low row \(L\). Take \(T=h\). If \(L=O(1)\) and \(3h/4<B<7h/8\), the bound is \(\Omega(h^2)\) from the last such pair. It holds for every choice of the intervening singleton rows. It concerns an eventual constant top tail with those two anchors. A reusable nonconstant background or endpoints with a smaller height difference require a different analysis.
