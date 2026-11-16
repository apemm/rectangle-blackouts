# Four prescribed tile ranks can defeat three private choices

15 November 2026. The large-offset Beatty theorem applies to every order
of a Cartesian label tile in its stated regime. That all-order scope
cannot extend to every offset of order s^4. The example below gives an
actual three-choice obstruction with all six alternative owners inside
the same tile. Its half-factor class has reduced multipliers1,2,3.

This is not a Hilbert-order obstruction. The four prescribed labels
occupy ranks far apart while their coordinate diameter stays bounded
as the tile grows. No full locality or filtered-scaffold claim is made.

## 1. The tile and the four ranks

Fix S divisible by four and put c=S^2/8, an integer. Take any integer
s>9c and an odd multiple q of3 satisfying

\[
                 q>3S/2,\qquad 3\le q\le s^2-1.
 \tag{1}
\]

Let d=q/3 and T=(q^2-1)/2. The full tile has labels

\[
 (i,j)\in\{0,\ldots,s-1\}^2,
 \qquad a_i=2i+1,\quad b_j=2(T+j)+2,
 \tag{2}
\]

in a strip of height h=2T+2s=q^2-1+2s. Put the following four labels
at ranks0,d,2d,3d respectively:

\[
 z_0=c(6,0),\quad z_1=c(2,5),\quad
 z_2=c(4,1),\quad z_3=c(9,3).
 \tag{3}
\]

Every other label can occupy any unused rank. Give each label an
arbitrary private choice xi_r in{0,1,2}, and place its two points at

\[
                            x_r=S(3r+\xi_r).
 \tag{4}
\]

No choice vector makes this complete-label board valid, even if
arbitrary additional filler points are supplied.

## 2. Every pair forbids equal choices

Direct the six edges on the four displayed labels as

\[
       0\to1,\quad1\to2,\quad2\to0,\quad
       3\to0,\quad3\to1,\quad2\to3.
 \tag{5}
\]

For an edge u->v, put m=|v-u|. Its coordinates in (3) satisfy

\[
                         j_v-i_u=-c m^2.
 \tag{6}
\]

If xi_(ud)=xi_(vd), the horizontal separation of the odd point of
z_u and the even point of z_v is S m q. Their vertical separation is

\[
 Y_m=q^2-2c m^2=q^2-{S^2m^2\over4}>0.
 \tag{7}
\]

The exact norm identity is

\[
 (S m q)^2+Y_m^2
                    =\left(q^2+{S^2m^2\over4}\right)^2.
 \tag{8}
\]

Thus every pair of the four labels forbids equality of its choices.
Three choices cannot give distinct values to four labels, so at least
one of these six P vectors is unavoidable. This is an actual-integer
obstruction, not merely a failure of certified modular constraints.

## 3. Every alternative owner is already present

The smaller half-factor in (8) is A_m=S^2m^2/4=2c m^2. The alternative
vertical pair has rows

\[
             a_{i_u}-A_m=a_{i_u-cm^2},\qquad
             b_{j_v}+A_m=b_{j_v+cm^2}.
 \tag{9}
\]

The six owner labels, in the edge order (5), are

\[
 c(5,6),\quad c(1,2),\quad c(0,4),\quad
 c(0,9),\quad c(5,9),\quad c(3,4).
 \tag{10}
\]

They are distinct from each other and from the four protected labels.
All their coordinates lie between0 and9c, hence inside the tile.
Consequently every alternative row lies in[1,h], and its complete axis
owner is retained regardless of the other private choices.

The midpoint column of the norm pair is integral because S is divisible
by four. If its owner is at that midpoint, the tilted rectangle is
hidden. Otherwise the tilted rectangle and the owner's axis rectangle
have black symmetric difference and therefore equal presentations.
This argument is unchanged by filling either common corner or by adding
any other black points. It proves the board obstruction claimed above.

## 4. Consequence for the thin-block method

Choose the odd multiple q of3 immediately below s^2. Then q=s^2+O(1)
and

\[
                         T=(1/2+o(1))s^4.
 \tag{11}
\]

The three smaller half-factors are S^2/4,S^2,9S^2/4. Their square-root
multipliers are S/2,S,3S/2, so after gcd normalization they are1,2,3.
The fixed-menu theorem's cutoff a<S^2 excludes the latter two; there
is no conflict with that theorem. The growing-menu theorem explicitly
requires odd normalized multipliers, which this example violates.

This rules out an unrestricted all-order extension at the coefficient
1/2 in (11). It does not determine the optimal cutoff coefficient,
show that any canonical Hilbert block is unsatisfiable, or rule out
changing the placement order or the number of choices. In particular,
the true four per-scale Hilbert systems remain open.

## 5. Exact check

The companion checker verifies all81 assignments to the four protected
labels in each saved case. For the first equal-choice pair it checks
all three choices of the owner and all four colorings of the common
corners, including the norm, owner rows, and both rectangle presentations.
It does not enumerate or claim a Hilbert embedding.

Files: [checker](check_arbitrary_order_four_label_obstruction.py) and
[results](check_arbitrary_order_four_label_obstruction.json).

## Review status

The full note passed an independent written review. The independent reader
also imported and reran all four sparse cases without rewriting outputs:
324 assignments and3,888 common-corner colorings passed.
