# An actual recursive Hilbert collision

14 November 2026. The recursive address and collision proof have been
independently reviewed. The fixed-stride Hilbert order has a recursive
mixed axis/tilted collision, in addition to the vertical P-rival
already recorded in the placement note. This uses the actual order,
not just its Holder estimate.

## The four ranks

Let \(S=2^e\), \(e\ge3\), and put
\[
 u=S^2/2,\quad R=2u,\quad q=4u^2=S^4,\quad h=2q,
 \qquad \rho=u^4+8u^2,\quad t=2u^2.
\]
Use the whole \(q\)-square of labels and columns \(x_r=Sr\).
Write
\[
 I=u^2+2u,\qquad J=2u.
\]
The recursive Hilbert order has the exact values
\[
\begin{array}{c|c}
\text{rank}&(i,j)\\ \hline
\rho&(I,J)\\
\rho+1&(I+1,J)\\
\rho+t-1&(I+u-1,J+u)\\
\rho+t&(I+u,J+u).
\end{array}
\tag{1}
\]

To check the aligned block in (1), follow the quadrant address
\[
 0,\ 1,\ \underbrace{0,\ldots,0}_{2e-3\text{ times}},\ 2
\]
from the \(q\)-square to a square of side \(R\).
Quadrant zero swaps the two coordinates; quadrants one and two
preserve orientation. The total number of swaps is \(2e-2\), which
is even. Thus the block has identity orientation.
The first quadrant-one contribution to its starting rank is \(u^4\),
and the last quadrant-two contribution is \(8u^2\).
Its spatial origin is \((I,J)\).

The exponent of \(R=2^{2e}\) is even. Hence its first two points are
\((0,0),(1,0)\). At the boundary between its second and third
quadrants, the last and first points are \((u-1,u),(u,u)\).
This proves (1).

## The collision

Put \(a=2I+1\) and \(b=2J+2\). Choose the following four black points:
\[
\begin{aligned}
 A&=(S\rho,a),&
 B&=(S(\rho+1),b),\\
 D&=(S(\rho+t-1),b+2u),&
 C&=(S(\rho+t),a+2u).
\end{aligned}
\]
Let
\[
 P=(S(\rho+t-1),a+2u),\qquad
 Q=(S(\rho+t),b+2u).
\]
The point \(P\) is white: the odd point of its column has row
\(a+2u-2\), and its even point has row \(b+2u\).
The point \(Q\) is black, being the even point of the column containing
\(C\).

Since \(b-a=1-t\), the two side vectors of \(ABQP\) are
\[
 (S,1-t),\qquad (S(t-1),2u).
\]
Their dot product is
\[
 S^2(t-1)+(1-t)2u=0,
\]
because \(2u=S^2\). They are nonzero, so this is a tilted rectangle.
The four points \(C,D,P,Q\) form an axis-aligned rectangle.
Both rectangles have presentation exactly \(\{P\}\).
All their rows and columns are inside the board.

Thus the unmodified Hilbert placement is invalid at height \(2S^4\)
for every power-of-two stride \(S\ge8\).
The same configuration also contains a black tilted right angle,
at \(B\) with endpoints \(A,Q\).
It is therefore relevant to the all-label corner-triple obstruction,
not only to four-point mixed supports.

This family does not contradict the growing-stride exclusion:
its height is much larger than \(S^4/64\), let alone \(S^4/1024\).

## What this does not rule out

The four ranks have two parities, and the collision is not asserted to
survive every finite classification of labels or a change of local
choices. The result rules out treating the unmodified Hilbert order
as automatically free of mixed collisions or black right angles.

The [sparse exact checker](check_hilbert_recursive_mixed.py) evaluates
only the required Hilbert ranks. Its
[output](hilbert_recursive_mixed_check.json) verifies the family for
\(S=8,16,32,64,128,256\). In these six instances the eight points in
the four labels have no nonhorizontal integral distance between
different columns. Thus no P edge among just these four labels explains
the displayed obstruction. This finite observation is not used in the
proof for all \(S\), and it makes no claim about P edges to other labels.

The same checker independently verifies the three actual P-rivals at
height \(4096\) in the choice-evidence note, including the three Hilbert
ranks, their coordinates, the lengths, all completion rows, and the two
owner ranks. All three owners differ from their respective midpoint
columns.
