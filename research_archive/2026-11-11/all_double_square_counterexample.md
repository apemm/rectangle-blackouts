# A valid all-double square exists

11 November 2026. There is a valid 7 by 7 blackout with two black
cells in every column. Thus the literal no-singleton question has a
positive answer even when the height is the smaller dimension.
This example does not settle the saturated equality case.

## 1. The board

From left to right, take the black row pairs
\[
 \boxed{17,\quad67,\quad15,\quad35,\quad36,\quad23,\quad12.}
\]
Here 17 means rows one and seven. Equivalently, the black cells are
marked by X below. Rows are listed from one to seven.

```text
X . X . . . X
. . . . . X X
. . . X X X .
. . . . . . .
. . X X . . .
. X . . X . .
X X . . . . .
```

Every column has exactly two black cells, and there are fourteen
black cells altogether. Its row-pair graph contains the five-cycle
1,7,6,3,2,1. Consequently, validity of a dense all-double board does
not force that row-pair graph to be a forest.

## 2. A finite verification certificate

A rectangle is identified by its white corner set. A white set with
at least three corners determines a unique rectangle: its three
points have a unique right-angle vertex and therefore a unique
fourth corner. It suffices to check every presentation of size at
most two.

The board has the following presentation counts.

| White corners | Axis rectangles | Tilted rectangles | Total |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 20 | 5 | 25 |
| 2 | 116 | 43 | 159 |
| 3 or 4 | 305 | 151 | 456 |
| All | 441 | 199 | 640 |

The complete list of all 184 rectangles with at most two white
corners is in
[all_double_7x7_weak_rectangles.md](all_double_7x7_weak_rectangles.md).
Each row lists its white set and its black set, so the full rectangle
can be checked directly. All listed white sets are distinct,
including between the axis and tilted tables. The machine-readable
copy is [all_double_7x7_certificate.json](all_double_7x7_certificate.json).

For completeness, there are \(\binom72^2=441\) axis rectangles.
Every tilted rectangle has a unique lowest vertex. Its two upward
side vectors are (a,b) and (−c,d), where
\[
 a,b,c,d>0,\qquad ac=bd,\qquad a+c\le6,\quad b+d\le6.
\]
There are 31 such quadruples. Each gives exactly
\((7-a-c)(7-b-d)\) translations in the square, and these counts sum
to 199. This supplies a short exhaustive parameterization of the
tilted table. The certificate file includes the 31 quadruples.

The standard-library verifier
[verify_all_double_7x7.py](verify_all_double_7x7.py) checks all three
descriptions: equal diagonals with common midpoint, perpendicular
sides, and the positive side-vector parameterization. They generate
the same rectangle set. It then checks every actual white set.
No solver is used in this verification.

The discovery search used the exact clauses
\[
 \bigvee_{v\in R\mathbin{\triangle}R'}\neg b_v
 \qquad(R\ne R'),
\]
together with exactly two black cells per column. Its saved output is
[all_double_square_h7.json](all_double_square_h7.json). These search
records are separate from the explicit finite verification.

## 3. Why the saturated question remains open

For h=7 the equality family has \(q_h=12\) doubles, one for every
edge of a complete balanced bipartite row graph. This example has
only seven doubles and its row graph is not bipartite. It therefore
does not prove \(m_7=q_7\), and gives no equality-threshold lower or
upper bound.

In a saturated all-double board, every white cell does have exactly
one axis rectangle with that singleton presentation. If its row
lies in one part, use the opposite-part black row in its column.
Their row pair occurs in exactly one other column. The same-part
black row supplies no second rival.

That premise fails here. For example, the tilted rectangle
\[
 \{(1,3),(3,1),(3,5),(5,3)\}
\]
has singleton white presentation (1,3). Column one contains rows
one and seven, but neither row pair 13 nor 37 occurs. There is no
axis rectangle with the same singleton presentation. This is an
explicit reason why a no-three-black-tilted-rectangle argument for
saturated boards cannot be applied to arbitrary all-double boards.

The stronger question of a valid saturated h by q_h all-double
board, for some h at least four, remains unresolved by this work.

## 4. A bipartite example at height eight

The restriction to a bipartite row-pair graph does not restore a
no-singleton conclusion. A valid 8 by 8 example is
\[
 14,\quad16,\quad47,\quad27,\quad67,\quad12,\quad78,\quad18.
\]
Every pair has opposite physical parity. Its row graph is exactly
\(K_{2,4}\), with parts {1,7} and {2,4,6,8}. Rows three and five
have no black cells. The three independent rectangle descriptions
agree on all 1192 rectangles, and their white presentations are
distinct. The checker and result are
[verify_all_double_8x8.py](verify_all_double_8x8.py) and
[all_double_8x8_independent_check.json](all_double_8x8_independent_check.json).

This example uses eight of the sixteen edges required by a saturated
balanced row family at height eight. The missing complete-family
hypothesis is still essential.

## 5. Every row can be used

Unused rows are also unnecessary. Another valid 8 by 8 word is
\[
 38,\quad16,\quad78,\quad14,\quad67,\quad18,\quad12,\quad58.
\]
Its row degrees are (4,1,1,1,1,2,2,4). The word uses every row, but
has several rows of degree one. A 9 by 9 example is
\[
 12,\quad34,\quad14,\quad56,\quad67,\quad78,\quad18,\quad89,\quad39,
\]
whose row degrees are (3,1,2,2,1,2,2,3,2).

Both pass the three independent geometric descriptions, with 1192
and 2044 rectangles respectively. The standalone checker is
[verify_saved_all_double.py](verify_saved_all_double.py). Results are
[all_double_rows_used_h8_independent_check.json](all_double_rows_used_h8_independent_check.json)
and [all_double_rows_used_h9_independent_check.json](all_double_rows_used_h9_independent_check.json).
These positive results still do not impose a saturated row-pair
family.

## 6. Limited negative search evidence

The same exact SAT encoding returned the following exclusions.

| Square height | Additional condition | Result | Total elapsed seconds |
|---:|---|---|---:|
| 6 | None | UNSAT | 0.266 |
| 7 | Every pair has opposite physical parity | UNSAT | 0.937 |
| 8 | Every row has at least two black cells | UNSAT | 5.953 |
| 9 | Every row has at least two black cells | UNSAT | 82.922 |

In the last two rows, the column condition fixes the total at 2h,
so every row would have exactly two black cells. These are completed
solver computations, not independently checked formal UNSAT
certificates. They imply no general degree-two obstruction.
The saved records identify CaDiCaL 1.9.5 through the `cadical195`
backend of python-sat 1.9.dev21:
[height six](all_double_square_h6.json),
[parity height seven](parity_all_double_square_h7.json),
[two-regular height eight](all_double_two_regular_h8.json), and
[two-regular height nine](all_double_two_regular_h9.json).

The original requested time limits used a Python timer calling an
unsupported CaDiCaL interrupt method. The height-nine call therefore
exceeded its requested 20-second limit and completed normally after
82.922 seconds. That failed limit is recorded explicitly. The runner
now uses a separate process for hard termination, but no further SAT
run was made after this change. All discovery and verification files
remain uncommitted.
