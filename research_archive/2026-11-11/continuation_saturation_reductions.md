# What the saturated lower bound still needs

11 November 2026. This continuation isolates a stronger local target
and gives exact counterexamples to weaker cycle-based replacements.
It does not prove that every saturated all-double board is invalid.

## 1. The exact local reduction

Fix h at least four, put q=floor(h^2/4), and place every edge of a
complete balanced bipartite row graph exactly once in q consecutive
double columns. The row partition can be arbitrary.

Every white cell has exactly one axis rectangle with that singleton
presentation. Indeed, its row lies in one part, and precisely one
of the two black rows in its column lies in the other part. The
corresponding row pair has a unique owner elsewhere.

Consequently a valid saturated board cannot contain a tilted
rectangle with exactly three black corners. A hidden rectangle is
also impossible on boards with both dimensions at least four, by
the previously proved hidden-rectangle lemma. See
[hidden_rectangles_and_exact_hypergraph.md](../2026-11-09/full_problem_push/hidden_rectangles_and_exact_hypergraph.md).
Thus every tilted rectangle has at most two black corners.

Conversely, under that corner condition, tilted rectangles have no
empty or singleton presentation. Axis presentations are already
distinct because the row graph is complete bipartite with unique
pair owners. Three white corners determine their rectangle. Hence
the only remaining comparisons concern equal two-white
presentations, with at least one tilted rectangle.

This gives an exact reduction for the saturated problem:

* exclude every in-board tilted corner triple;
* exclude the remaining two-white collisions.

In particular, six-black-support comparisons are unnecessary after
the entire corner-triple condition is imposed. Two rectangles with
only one common corner could share a white presentation only if
each had at least three black corners. The tilted member would
violate that condition.

## 2. Zero cycle rank loses local corner information

The all-slope cycle budget is necessary, but zero cycle rank is
strictly weaker than the corner condition. This gap occurs in
saturated examples beyond height four.

The following complete parity families have zero cycle rank in
every non-axis primitive direction pair:

| Height | Width | Column pairs |
|---:|---:|---|
| 5 | 6 | 45,34,25,14,23,12 |
| 6 | 9 | 12,36,16,56,34,23,14,25,45 |
| 7 | 12 | 56,47,16,14,45,34,12,36,25,67,27,23 |

They are not valid boards. For the height-five example, the tilted
rectangle
\[
 R=\{(1,4),(4,1),(5,2),(2,5)\}
\]
has singleton white presentation (2,5). Its black right-angle legs
at (4,1) are (−3,3) and (1,1). The axis rectangle
\[
 A=\{(1,4),(1,5),(2,4),(2,5)\}
\]
has exactly the same white presentation.

The forest assertion has a finite complete certificate. For primitive
a,b>0, use the line labels
\[
 u=bx-ay,\qquad v=ax+by.
\]
Each black point is one edge joining its u-line and v-line. If a or
b exceeds h−1, one family of lines contains at most one black point
per line, so a cycle is impossible. It suffices to check
1≤a,b≤h−1 with gcd(a,b)=1. The height-five table is:

| (a,b) | Occupied line vertices | Components | Edges |
|---|---:|---:|---:|
| (1,1) | 14 | 2 | 12 |
| (1,2) | 17 | 5 | 12 |
| (1,3) | 20 | 8 | 12 |
| (1,4) | 22 | 10 | 12 |
| (2,1) | 16 | 4 | 12 |
| (2,3) | 23 | 11 | 12 |
| (3,1) | 24 | 12 | 12 |
| (3,2) | 20 | 8 | 12 |
| (3,4) | 22 | 10 | 12 |
| (4,1) | 23 | 11 | 12 |
| (4,3) | 22 | 10 | 12 |

In every row, edges minus vertices plus components is zero.
The analogous complete lists at heights six and seven are saved in
[continuation_saturation_zero_rank_examples.json](continuation_saturation_zero_rank_examples.json).
The independent checker
[continuation_saturation_zero_rank_examples.py](continuation_saturation_zero_rank_examples.py)
also verifies the complete row family, enumerates all rectangles in
three ways, and identifies the local failures. No SAT result is used
in these certificates.

Thus a proof that every saturated placement has positive tilted
cycle rank is false in the stated all-height form. One must retain
individual corner triples or use additional mixed information.

## 3. A sharper structural target

The following conjecture would suffice for all heights at least five:

> If an h by m board has exactly two black cells per column, distinct
> row pairs forming a triangle-free graph, and at most two black
> corners in every in-board tilted rectangle, then m≤h.

The row-graph assumptions are exactly the axis-validity conditions
for an all-double board. The conjecture does not assume a row
partition. The cyclic staircase shows that equality m=h is possible
under these necessary conditions; its mixed collision still prevents
full validity.

Since q_h>h for h≥5, the conjecture would exclude every saturated
board at those heights. A valid all-double board can have m≥h when
tilted singleton presentations are permitted, so those examples do
not refute the conjecture. The regular-board local lemma also permits
tilted corner triples, unlike the conjecture's hypotheses.

The bound does not follow from the 45-degree corner condition alone.
A 6 by 7 counterexample to that weaker statement is
\[
 56,23,46,24,16,36,12.
\]
Its row pairs are distinct and triangle-free, and each of its 70
45-degree rectangles has at most two black corners. A different
slope supplies the failure:
\[
 \{(5,1),(6,3),(4,4),(3,2)\}
\]
is a tilted rectangle with singleton white presentation (3,2).
Its legs at (6,3) are (−1,−2) and (−2,1). The competing axis
rectangle uses columns three and four, rows two and four.

## 4. The height-four endpoint

At height four, q_4=4, so the conjectured bound alone would not
exclude saturation. This remaining case has a short finite check.
There are three balanced row partitions and 24 orders per partition.
The square has only eight tilted rectangles.

For parts {1,2} or {1,4}, none of the 24 orders avoids all tilted
corner triples. For part {1,3}, exactly these four orders do:
\[
 12,23,34,14;\quad14,12,23,34;\quad
 14,34,23,12;\quad34,23,12,14.
\]
They are reflections of one another. In the first word the tilted
rectangle
\[
 \{(1,2),(2,1),(3,4),(4,3)\}
\]
and the axis rectangle
\[
 \{(2,1),(2,3),(4,1),(4,3)\}
\]
share the white pair {(2,1),(4,3)}. Hence all four orders fail.
The 72-case classification and the height-six weaker-condition
counterexample are independently checked in
[continuation_saturation_relaxation_certificates.py](continuation_saturation_relaxation_certificates.py).
Its output is [the certificate record](continuation_saturation_relaxation_certificates.json).

## 5. Computational evidence, not a proof of the conjecture

An exact necessary-condition model uses point variables, exactly
two black points per column, unique row-pair owner variables, and
clauses forbidding triangles in the row-pair graph. It then forbids
every three-corner subset of every tilted rectangle. Positive side
vectors (a,b),(−c,d), with ac=bd and their full bounding box in the
board, enumerate the tilted rectangles completely.

With no prescribed row partition, the h by (h+1) model returned
UNSAT for h=6,7,8,9,10. Heights eleven and twelve reached their hard
20-second process limits and returned UNKNOWN. The completed runs
have no independently verified formal UNSAT proof. They remain
computational evidence only.

The model and saved results have prefix
`continuation_saturation_excess_width_`. Earlier fixed-parity
saturated relaxations and the cubic height-eight relaxation are
also retained, with their narrower hypotheses. No general lower
bound beyond q_h is claimed from these runs.
