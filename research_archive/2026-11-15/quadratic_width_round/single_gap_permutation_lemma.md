# A sixteen-label permutation for any one gap and row difference

15 November 2026. This is a finite combinatorial lemma for the
full-occupancy model. It does not solve constraints between different
permutation blocks.

Consider the sixteen labels (i,j) in {0,1,2,3}^2 and sixteen physical
slots numbered 0 through 15. Fix a slot gap q in {1,...,15} and an
integer row-index difference u. For every two slots at distance q,
forbid both cross relations

\[
 j_{\rm right}-i_{\rm left}=u,
 \qquad j_{\rm left}-i_{\rm right}=u.
\]

**Lemma.** There is a permutation of all sixteen labels that avoids
both relations at every such pair. In fact both differences can be
required to differ from u modulo four.

## Explicit proof

The following cyclic list contains every ordered pair in Z_4^2 once:

\[
\begin{split}
 &(0,0),(1,2),(1,3),(0,2),(0,3),(2,3),(0,1),(2,1),\\
 &(3,1),(3,2),(1,0),(2,0),(3,0),(1,1),(2,2),(3,3).
\end{split}
\tag{1}
\]

For each consecutive pair (i,j),(i',j'), including the closing pair,
both j'-i and j-i' are nonzero modulo four. This is a direct check of
the sixteen displayed joins. Replace every second coordinate j by
j+u modulo four, using its representative in {0,1,2,3}. The result
is still a list of all sixteen labels, and at every join both cross
differences avoid u modulo four.

The graph on the slots whose edges join positions at distance q is a
disjoint union of paths:

\[
 r,r+q,r+2q,\ldots\le15,
 \qquad 0\le r<q.
\]

List these paths one after another, in any order and in either
orientation for each path. Put the transformed list (1) into the
resulting sequence of sixteen slots. Every distance-q edge now joins
two consecutive entries from one segment of (1), so it satisfies the
required exclusions. There are no distance-q edges between different
paths. This proves the lemma.

The start of (1) can also be rotated, or the whole cycle reversed.
These give additional assignments without weakening the proof.

## Use and limitations

For a 4-by-4 block of row labels, an internal P family that has just
one slot gap q and one signed cross-row index difference u can always
be avoided. The statement is independent of the orientation in which
the original Hilbert block was traversed: every permutation of its
sixteen labels is allowed.

Arithmetic classification is still needed before applying this lemma
to all P constraints of a block. Two different gaps or two different
row-index targets are not covered by this proof. Constraints involving
labels in other blocks are also not covered. No gluing or full-board
theorem is asserted.

The supplementary checker [check_single_gap_cycle.py](check_single_gap_cycle.py)
verifies the explicit cycle and all 60 pairs (q,u mod4), then checks
the corresponding exact integer exclusions for -3<=u<=3. Its finite
checks support the displayed construction; the path decomposition
proves the general statement directly.
