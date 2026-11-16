# An integer-offset Hilbert tile can need more than three private choices

15 November 2026. This exact certificate disproves the stronger
all-integer-offset S=32,M=3 private-tile conjecture. It does not
disprove solvability of the original aligned per-scale systems:
the required row offset is not divisible by the tile side.

All four protected labels occupy their actual canonical Hilbert ranks.
The obstruction is an actual-integer K4, rather than only a certified
modular contradiction. Every choice assignment fails already on one
of six equal-choice constraints.

## 1. Four exact ranks and the row offset

Let the tile side be n=8192. Its four protected points and ranks are:

| Index | Raw coordinate | Hilbert rank |
|---|---|---:|
| 0 | (3166,4705) | 32778237 |
| 1 | (5728,5215) | 35923967 |
| 2 | (4192,7777) | 39069697 |
| 3 | (6752,6241) | 42215427 |

The ranks form an arithmetic progression with step

\[
 d=3145730,\qquad c=512,\qquad C=2561.
 \tag{1}
\]

Put

\[
 B_0={(32\cdot3d)^2\over8c}=22265138774025,
 \tag{2}
\]

\[
 T={B_0-1\over2}-C=11132569384451.
 \tag{3}
\]

The tile's odd and even rows are 2i+1 and 2(T+j)+2. At rank r, its two
points occupy column 32(3r+xi_r), where xi_r is any of 0,1,2.

The distinction from an aligned canonical type is exact:

\[
                       T\bmod8192=5635,\qquad T\bmod8=3.
 \tag{4}
\]

A canonical side-n type has its two coordinate origins divisible by n,
so its row-index offset is divisible by n. This certificate does not
meet that condition. It applies when an independent integer shift is
allowed between the two row pools, as in the stronger all-offset tile
question.

## 2. All six constraints

Direct the six label pairs as

\[
       0\to1,\quad2\to0,\quad3\to0,\quad
       1\to2,\quad1\to3,\quad2\to3.
 \tag{5}
\]

If u->v is one of these pairs and m=|v-u|, the displayed raw coordinates
satisfy

\[
                         j_v-i_u=C-cm^2.
 \tag{6}
\]

When xi_(r_u)=xi_(r_v), the odd point of label u and the even point of
label v therefore have the norm vector

\[
 X=96dm,\qquad Y=B_0-1024m^2,\qquad L=B_0+1024m^2,
                       \qquad X^2+Y^2=L^2.
 \tag{7}
\]

All Y are positive. Explicitly:

| Roles u->v | m | X | Y | L |
|---|---:|---:|---:|---:|
| 0->1,1->2,2->3 | 1 | 301990080 | 22265138773001 | 22265138775049 |
| 2->0,1->3 | 2 | 603980160 | 22265138769929 | 22265138778121 |
| 3->0 | 3 | 905970240 | 22265138764809 | 22265138783241 |

Every pair of the four labels thus forbids equality of its private
choices. Four labels cannot receive pairwise different values from
three choices. This proves unsatisfiability of the candidate tile
system without needing any owner argument or any other black cells.

## 3. Owners and actual presentations

The alternative owner of edge u->v is

\[
                         (i_u-cm^2,j_v+cm^2).
 \tag{8}
\]

In the edge order (5), these are

\[
 (2654,5727),\ (2144,6753),\ (2144,9313),\
 (5216,8289),\ (3680,8289),\ (3680,6753).
 \tag{9}
\]

Three owners lie beyond the original side-8192 tile in the second
coordinate. To obtain a complete-owner board certificate, use the
full canonical Hilbert square of side 32768, with the same row offset
T and the same private-slot rule. The original lower-left tile is
reached through two initial quadrant-zero descents; their two swaps
cancel. Hence all four protected coordinates and ranks stay exactly
as listed. Every owner in (9) lies in the larger square.

A strip height

\[
 h=2T+2\cdot32768=22265138834438
 \tag{10}
\]

contains every row and every alternative. Each owner is distinct from
the four protected labels. The usual black-symmetric-difference
argument applies: if an owner occupies the common midpoint, the
corresponding tilted rectangle is hidden; otherwise it and the owner's
axis rectangle have equal presentations. Filling common corners or
adding arbitrary further black points cannot repair this collision.

This is an actual invalid-board statement for the independently shifted
row pools. It does not imply that these labels survive any row filter,
that an unshifted canonical type contains the same clique, or that
higher-family choices in a proposed construction must retain this tile.

## 4. How the example was verified

A finite bit-carry search produced the exact candidate. The verification
uses only the four coordinates and ranks above, not the search program.
An independent iterative Hilbert routine verifies the rank-to-cell
identities, and a separate inverse routine verifies the reverse lookup.
The checker then verifies all six norm identities and owner coordinates.

Finally it enumerates all 81 private assignments to the four labels.
For the first equal-choice pair, it tests all three choices of that
owner and all four colorings of the two common corners. All 81 assignments
fail, and all 972 resulting presentation checks pass.

Files: [checker](check_unaligned_hilbert_k4_certificate.py) and
[exact results](check_unaligned_hilbert_k4_certificate.json).

The full certificate passed an independent written review and exact rerun.
The independent reader used separate forward/inverse Hilbert implementations
and an ordered-diagonal rectangle test without importing this checker or
its geometry helpers. All 81 assignments and 972 presentations passed.
