# Terminal Hilbert orientation alone does not exclude right angles

14 November 2026. At stride \(S=32\), three labels with the same
terminal Hilbert orientation contain an in-strip black right angle.
This rules out the four terminal orientation classes as a complete
right-angle exclusion rule. A second exact example below also survives
the simultaneous addition of the lowest three coordinate and rank bits.
Arbitrarily many fixed low bits remain outside this conclusion.

## Orientation convention

In the standard recursion, quadrant zero has linear part
\((x,y)\mapsto(y,x)\), quadrants one and two have the identity linear
part, and quadrant three has linear part
\((x,y)\mapsto(-y,-x)\). Compose the linear parts down to the
individual cell. The resulting terminal state is one of identity,
coordinate swap, minus identity, or minus coordinate swap.

## An exact configuration

Take \(q=2^{24}=16777216\) and \(h=2q=33554432\).
The macro-cell \((9983,1)\) in the \(2^{14}\)-square has rank
\(247398398\) and identity terminal orientation. Its quadrant address
is
\[
 32233233333332.
\]
Replace that cell by its square of side \(1024\). Within this square,
the following three local ranks have the stated coordinates and
coordinate-swap orientation:

| Local rank | Quadrant address | Local coordinates |
|---:|---|---|
| 22 | `0000000112` | \((7,1)\) |
| 61 | `0000000331` | \((1,6)\) |
| 524244 | `1333333110` | \((504,518)\) |

Thus the global ranks and label coordinates are

| Rank | Label \((i,j)\) |
|---:|---|
| 259416022581270 | \((10222599,1025)\) |
| 259416022581309 | \((10222593,1030)\) |
| 259416023105492 | \((10223096,1542)\) |

Use the odd point \(A\) of the first label and the even points
\(B,C\) of the other two labels. At \(B\), their displacement vectors are
\[
 A-B=(-1248,20443137),\qquad
 C-B=(16773856,1024).
\]
The identity
\[
 20443137=39\cdot524183
\]
shows that their dot product is zero: the horizontal factors are
\(32\cdot39\) and \(32\cdot524183\).

The fourth corner has row \(20446223\), which lies in \([1,h]\),
and its column lies strictly between the first and last displayed
columns. All four columns are distinct. Therefore this is an actual
tilted right angle in the finite strip. Each of its three black
points belongs to a label in the same terminal orientation class.

Embedding this square into the third quadrant of the next Hilbert
square adds a common rank offset and a common translation to both
label coordinates. It preserves orientation, the right angle, and
row containment. The obstruction therefore also occurs at every
height \(33554432\cdot2^j\), \(j\ge0\).

## Adding the lowest three bits still leaves an angle

The following larger example has one common terminal orientation and
one common residue modulo eight for each of the rank, first coordinate,
and second coordinate. Put
\[
 u=2^{21},\quad R=2u=2^{22},\quad Q=2^{16},\quad
 q=QR=2^{38},\quad h=2q=2^{39}.
\]
In the macro-square of side \(Q\), the cell
\((2^{14}+1,1)\) has identity orientation and rank \(2^{28}+2\).
Its address is zero, one, thirteen zeros, and two. Refining this cell
to side \(R\) gives a block with origin
\[
 (I,J)=(2^{36}+2^{22},2^{22}),\qquad I-J=u^2/64.
\]
Its three selected local ranks and coordinates are
\[
\begin{array}{c|c}
76&(1,11)\\
140&(9,11)\\
2u^2-1204&(u-47,u+11).
\end{array}                                                   \tag{1}
\]
All three have terminal orientation minus coordinate swap. The exact
recursion verifies (1); the sparse checker records their full global
ranks as well.

Take the odd point \(A\) of the first label and the even points
\(B,C\) of the other two. The rank gaps at \(B\) are \(64\) and
\(2u^2-1344\). The corresponding row gaps are
\[
 y_A-y_B=2(I-J)-21=u^2/32-21,\qquad y_C-y_B=2u.
\]
Since \(S=32\) and \(u=2^{21}\),
\[
 \frac{S^2\cdot64\,(2u^2-1344)}{2u}
   =\frac{2u^2-1344}{64}
   =u^2/32-21.
\]
This is exactly the right-angle identity at \(B\).
The fourth corner has row \(137451536387\), which is in \([1,2^{39}]\),
and its column lies strictly between the extreme black columns.

The three global signatures are all
\[
 (r\bmod8,i\bmod8,j\bmod8)=(4,1,3).
\]
They also share the terminal orientation. Therefore every class rule
that is a function only of these three residues and the terminal
orientation places this angle in one class. The conclusion includes
rules using any subset of these bits.

Third-quadrant embedding again gives infinitely many heights. For a
fixed larger residue modulus, this example makes no claim.

## Verification and scope

[The sparse exact checker](check_hilbert_recursive_mixed.py) independently
evaluates the three global ranks, composes their orientation states,
and checks the right angle and fourth-corner containment. The table is
an exact finite certificate, not a numerical approximation.

The [dyadic-residue obstruction](continuation_hilbert_dyadic_residue_obstruction.md)
is separate: it defeats every fixed residue rule but has two terminal
orientations. These results do not prove that every combined rule
using arbitrarily many fixed bits must fail. No claim is made about
arbitrary finite colorings or local column choices.
