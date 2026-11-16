# Six paired horizontal legs reduce to unequal representations

15 November 2026. In the critical three-pair six-cycle pattern, assuming
that each pair has equal absolute horizontal legs is now enough to mark
a subquadratic set of genuine endpoints meeting every such cycle. An
arithmetic-progression incidence estimate handles adjacent equal types;
the cross-rank theorem handles the all-opposite case.

This does not count all six-cycles. The remaining branch has unequal
absolute horizontal legs in at least one pair of nearby edge-coordinate
points. Safe erasure and singleton consistency remain separate.

## 1. Arithmetic progressions with nearby source coordinates

Work in the central genuine multiscale model. Suppose three distinct
objects, in directed order \(0,1,2\), have equal consecutive signed
horizontal increments:
\[
                            x_1-x_0=x_2-x_1\ne0.     \tag{1}
\]
Assume the first edge is an actual P and the first two odd raw coordinates
satisfy \(|i_0-i_1|\le r\). Then the expected number of such triples is
at most
\[
                             h^{3/2+o(1)}(r+1),      \tag{2}
\]
uniformly for \(1\le r\le C\sqrt h\). Requiring the second edge to be
P or imposing additional row equalities can only reduce this count.

There are \(O(h^2)\) middle objects. Actual P restricts the first object's
raw rank to an \(O(h)\) interval around the middle, so its cell lies in
an \(O(\sqrt h)\) box. Its first coordinate lies in a band of width
\(O(r+1)\), leaving \(O((r+1)\sqrt h)\) possible cells. The first
column determines the third by (1). Fixed bounded provenance permits
only \(O(1)\) originating ranks at that column.

For each first horizontal gap, norm factorization gives \(h^{o(1)}\)
possible signed heights. Each prescribed cross-parity height has
probability \(O(1/h)\): condition on one parity field and offset, then
the other parity's genuine central row equation leaves only \(O(1)\)
offset values. The independent anchor sampling may also be conditioned
upon. This proves (2), without multiplying the two edge probabilities.

Marking all genuine objects in these triples costs the same order as
(2). It may be included in the existing joint nonnegative-cost objective.
The conclusion concerns the genuine objects, not all singleton points
remaining after their pairs are relocated.

## 2. The sign classification needs an adjacent-type case

Let the six directed edge indices have types \(A,B,C\), each twice.
Suppose the two signed horizontal increments of each type have the same
nonzero absolute value. Call that type *equal* if its two signed values
agree, and *opposite* otherwise.

If the two occurrences of a type are adjacent, opposite values would
return to the same column after two steps. Thus any adjacent same-type
pair in a simple six-cycle is equal and gives exactly an AP of the form
(1). If its two edge-coordinate points are within a cluster of radius
\(r\), their source odd raw coordinates are within \(2r\), so (2)
handles every such case.

After those cases are removed, no equal types are adjacent. Classify the
number of equal types.

* Exactly one is impossible: the total horizontal displacement would be
  twice that type's nonzero increment.
* Exactly two, say \(A,B\), force their common signed values to be
  negatives. Some \(A\) and \(B\) must be adjacent: otherwise the two
  \(C\)'s divide the four \(A,B\) positions into two runs, each of
  length at most one because neither equal neighbors nor \(AB\)
  neighbors would be allowed. That adjacency returns to the same column
  after two steps.
* If all three are equal, their signed values sum to zero. A cyclic word
  using all three types and no equal neighbors contains three consecutive
  distinct types. Their three increments sum to zero, again repeating a
  column.

Thus every remaining simple cycle has all three types opposite. This
classification uses exact horizontal increments, not their norm heights.
It therefore applies whenever each paired P vector has equal absolute
horizontal leg, even if the two signed heights are merely close.

## 3. Use the stable cross-rank exclusion

Assume the minimum surviving P gap is \(q_*=h^{1-o(1)}\), and the
genuine columns have fixed bounded rank provenance. Let the three pairs
of edge-coordinate points have radius \(r=h^{o(1)}\). The stable
theorem in
[the cross-rank note](continuation_hilbert_cross_rank_order.md), Section 5,
marks a deterministic raw-grid boundary set of size
\(h^{7/4+o(1)}\) meeting every all-opposite cycle of this type.

Combine that set with the AP endpoints from (2). Suitable joint field
choices have a total exceptional genuine set of size
\[
                               h^{7/4+o(1)}          \tag{3}
\]
meeting every three-pair central P six-cycle whose two absolute horizontal
legs agree in each pair. For radius \(r=h^\delta\), fixed
\(0\le\delta<1/2\), the corresponding bounds are
\[
                    h^{3/2+\delta+o(1)}
                     +h^{7/4+\delta/2+o(1)},         \tag{4}
\]
both subquadratic. Relocation multiplies these costs by the previously
specified \(h^{o(1)}\) factor only when its separate hypotheses apply.

Consequently a surviving genuine six-cycle in this clustered regime must
have unequal absolute horizontal legs in at least one pair. For exact
paired raw coordinates, their signed heights are equal; this is precisely
the branch using different Pythagorean representations of a shared
height. With nonzero radius, the paired heights differ by \(O(r)\), so
the remaining arithmetic problem is correspondingly a nearby-height one.

## 4. Why the AP step cannot simply be omitted

Hilbert geometry alone permits an adjacent-equal sign pattern. At side
32, take self-types
\[
                  A=(31,17),\quad B=(7,19),\quad C=(18,6).
\]
The \(AACBBC\) raw objects and their exact standard Hilbert ranks are

| Object cell | Rank |
| --- | ---: |
| \((31,6)\) | 1003 |
| \((31,17)\) | 764 |
| \((18,17)\) | 525 |
| \((7,6)\) | 43 |
| \((7,19)\) | 282 |
| \((18,19)\) | 521 |

Their signed increments, including the closing increment, are
\[
                  -239,-239,-482,239,239,482.
\]
Types \(A,B\) are equal and type \(C\) is opposite, with all six raw
objects distinct. This is an exact Hilbert rank certificate, checked by
the standard iterative distance-to-cell recurrence. It is **not** a
Pythagorean or in-strip P certificate: the three norm requirements have
not been established. Its role is to show why distinct objects do not
by themselves rule out adjacent equal types.

The AP estimate supplies the missing step without making that false
geometric inference.

## Review status

The cross-rank theorem and its stable boundary reduction were independently
reviewed. The complete saved reduction passed a separate written review,
including the AP candidate count, its single-edge probability, the corrected
sign classification, and the boundary-set combination. The six example
ranks were also recomputed using a separate iterative Hilbert routine.
