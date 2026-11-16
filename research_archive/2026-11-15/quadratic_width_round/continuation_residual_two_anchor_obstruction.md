# Two prescribed boundary choices need not extend after band deletion

15 November 2026. The original Hilbert P system has a realizable three-label
module whose exact integer relation on two boundary labels excludes only
the pair \((1,1)\). All three labels survive the multiple-leg band deletion.
There is also an actual full-grid realization in height 65536, with the
required axis owners surviving that deletion.

This is a boundary-extension obstruction. The three-label system itself is
solvable. It does not refute three-choice solvability of the four canonical
systems, a larger fixed choice palette, or a method that tracks the exact
two-terminal relation.

## 1. The three-label module

Use \(S=32,M=3\), with columns
\[
 x_r=32(3r+\xi_r),\qquad \xi_r\in\{0,1,2\}.
\]
Consider an aligned side-32 Hilbert block of type \((32,-40,\mathrm{id})\).
In its local rank coordinates, take
\[
 c=192,\qquad a=210,\qquad b=597.
\]
Their local cells, in the standard recursion, are respectively
\[
 (7,15),\qquad (6,10),\qquad (16,31).
\]
The block's row-index offset is \(j_0-i_0=-1280\). Direct evaluation
of the two cross-parity roles gives these Pythagorean identities:

| Pair | Forbidden difference | Horizontal leg | Vertical leg | Hypotenuse |
|---|---:|---:|---:|---:|
| \(c,a\) | \(\xi_a-\xi_c=-1\) | 1696 | 2553 | 3065 |
| \(c,a\) | \(\xi_a-\xi_c=1\) | 1760 | 2541 | 3091 |
| \(c,b\) | \(\xi_b-\xi_c=0\) | 38880 | 2511 | 38961 |

Each row satisfies \(X^2+Y^2=L^2\). Checking the five possible integer
differences in both roles gives no additional constraint on these pairs,
and no constraint on \(a,b\).

Thus the exact subsystem is
\[
 \xi_a-\xi_c\notin\{-1,1\},\qquad \xi_b\ne\xi_c.       \tag{1}
\]
If \(\xi_a=\xi_b=1\), choices \(\xi_c=0,2\) violate the first
condition, while \(\xi_c=1\) violates the second. Conversely every
other pair of anchor values extends. If \(\xi_a=1\), use
\(\xi_c=1\) when \(\xi_b\ne1\). If \(\xi_a\in\{0,2\}\),
choose the member of \(\{0,2\}\) different from \(\xi_b\).
Therefore the two-terminal relation is exactly
\[
 \mathcal R_{a,b}=\{0,1,2\}^2\setminus\{(1,1)\}.       \tag{2}
\]
Every single prescribed anchor value extends, and every pairwise relation
has full projections. Those facts do not imply simultaneous extension of
two anchors.

The integer solution set also lacks the global cyclic-shift symmetry of
the stronger certified system. For example, \((\xi_c,\xi_a,\xi_b)=(2,0,0)\)
satisfies (1), but adding one modulo three gives \((0,1,1)\), which fails.
Thus a modulo-three normalization of boundary colors cannot be transferred
to the integer system without an additional argument.

## 2. Survival of the multiple-leg deletion

The endpoint diagonals \(T=j-i\) are
\[
 T_c=-1272,\qquad T_a=-1276,\qquad T_b=-1265.
\]
The deletion rule in
[`continuation_p_sparse_multiple_legs.md`](../continuation_p_sparse_multiple_legs.md)
removes labels within
\[
 |T\mp Y/2|\le4\sqrt{2Y+1}+1                              \tag{3}
\]
of an exceptional odd vertical leg \(Y\). Here exceptional means that
two horizontal legs divisible by 32 differ by at most 128.

The independently enumerated range in
[`continuation_three_leg_spacing.md`](../continuation_three_leg_spacing.md)
contains no exceptional \(Y<4096\). For \(Y\ge4096\), the lower
edge of either absolute-value band is at least
\[
 Y/2-4\sqrt{2Y+1}-1
 \ge2048-4\sqrt{8193}-1>1684.
\]
The function on the left is increasing in this range. Thus none of the
three labels lies in any deletion band, at any ambient height.
The two forbidden differences on \(c,a\) come from different vertical
legs, not from two close horizontal legs for the same vertical leg.

## 3. An actual retained full-grid realization

Take \(h=65536\) and the Hilbert square of side \(32768\). The aligned
block beginning at global rank
\[
 R=895295488
\]
has origin \((16960,15680)\) and the required identity orientation.
The three actual cells are
\[
 H(R+c)=(16967,15695),\quad
 H(R+a)=(16966,15690),\quad
 H(R+b)=(16976,15711).
\]
The odd and even physical rows of \((i,j)\) are \(2i+1,2j+2\).
Prescribe \(\xi_{R+a}=\xi_{R+b}=1\). The three choices of the central
label give these in-strip vertical presentations:

| \(\xi_{R+c}\) | Common rows | Axis-owner cell | Owner rank |
|---:|---:|---:|---:|
| 0 | 31117, 34208 | (15558, 17103) | 536125635 |
| 1 | 13199, 52160 | (6599, 26079) | 399679850 |
| 2 | 31126, 34191 | (17095, 15562) | 895262931 |

For each row of the table, the owner column differs from the midpoint
column for every owner choice in \(\{0,1,2\}\). The tilted rectangle
and the axis rectangle therefore have symmetric difference consisting
only of the two prescribed black endpoints and the owner's two black
points. Their presentations agree regardless of all other black cells.

The owner diagonals are \(1545,19480,-1533\). An independent exact
enumeration finds precisely
\[
 \{8463,15575,25389\}
\]
as the exceptional odd vertical legs below 65536. None of the six source
and owner diagonals lies in their bands. Hence the actual three-way
obstruction remains after the specified deletion, with original ranks
kept, even if the deleted labels are subsequently placed elsewhere.

## 4. Checks and research consequence

[`check_residual_two_anchor_obstruction.py`](check_residual_two_anchor_obstruction.py)
uses its own recursive point and inverse-rank functions. It checks all 27
integer assignments, the exact two-terminal relation, all three norm
identities, every owner choice, and equality of the two presentations.
It also enumerates all exceptional \(Y<h\) through the divisors of
\(Y^2\), and tests band membership without floating-point arithmetic.
The saved output is
[`check_residual_two_anchor_obstruction.json`](check_residual_two_anchor_obstruction.json).

The search that found the module examined all offset types of aligned
blocks of sides 8, 16, and 32. It found no zero-offset \(K_4\) and no
integer-unsatisfiable \(K_{2,t}\) subsystem using only pairs with at most
two forbidden integer differences in those tested types. These
negative search results are finite evidence only. The obstruction proved
here is the explicit relation (2), not a conclusion drawn from that search.

A viable boundary induction must preserve enough information to exclude
incompatible anchor pairs such as \((1,1)\), or choose the anchors jointly.
The multiple-leg deletion and the three-label solvability lemma alone do
not supply unrestricted two-anchor extension.

Independent review: the written theorem and its exact checker passed a
separate audit. The review recomputed the forbidden sets, all nine anchor
relations, source and owner ranks, the norm and presentation certificates,
the exceptional-leg enumeration, and all six band-survival checks.
