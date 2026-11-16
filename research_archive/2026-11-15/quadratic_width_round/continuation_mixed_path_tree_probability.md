# Joint row sampling through a minimum-product tree

15 November 2026. The two parity fields can be used jointly without
choosing physical intervals adaptively in both fields. Fixing the odd-row
tuple first makes both target-row events deterministic, so their
probabilities multiply. A spanning-tree count then controls the number of
possible odd tuples. This gives a stronger probability bound for every
fixed central P-cycle pattern.

## 1. Fixed patterns and two weighted paths

Use [the multiscale row field](continuation_multiscale_row_sampling.md),
with independent fields and offsets for the two parity pools. Condition
on the independently sampled anchors. Let \(k\ge2\) be fixed. Consider
\(k\) genuine central objects with deterministic raw cells
\((i_v,j_v)\), \(0\le v<k\), and a fixed directed cycle permutation
\(\sigma\). Fix the signed norm heights \(Y_v\) for the edge
requirements
\[
                         b_{\sigma(v)}-a_v=Y_v.     \tag{1}
\]
All constants may depend on fixed \(k\), the profile spacing, and the
uniform bounded-error/provenance constants. The result does not include
arbitrary folds or cap-constant vertices.

Build two Hamiltonian paths on the vertex set \(\{0,\ldots,k-1\}\).
The odd path \(P_0\) lists the vertices in increasing \(i_v\).
The even path \(P_1\) lists them in increasing \(j_{\sigma(v)}\).
Ties may be resolved arbitrarily. Give consecutive edges the weights
\[
 w_0(uv)=1+|i_u-i_v|,\qquad
 w_1(uv)=1+|j_{\sigma(u)}-j_{\sigma(v)}|.             \tag{2}
\]
Let
\[
                 Q_0=\prod_{e\in P_0}w_e,
                 \qquad Q_1=\prod_{e\in P_1}w_e.    \tag{3}
\]
Parallel edges with different weights are retained in the union
multigraph. Define
\[
 \tau=\min\left\{\prod_{e\in T}w_e:
                   T\text{ is a spanning tree of }P_0\cup P_1\right\}.
                                                               \tag{4}
\]
The joint probability of (1) is at most
\[
                   {h^{o(1)}\tau\over h Q_0Q_1}.     \tag{5}
\]
The subpolynomial factor here is a fixed power of \(\log(2h)\), with
constants depending on \(k\). Both paths are eligible trees, so
\(\tau\le\min(Q_0,Q_1)\). Thus (5) includes the previous
\(h^{-1+o(1)}/\max(Q_0,Q_1)\) bound.

## 2. Prescribed-row masses

For any fixed \(k\) raw indices and prescribed physical rows, the
single-parity argument in Section 3 of the multiscale note gives
\[
 \Pr(\text{all prescribed rows})
       \le {C_k\log^{2(k-1)}(2h)\over h Q},          \tag{6}
\]
where \(Q\) is the product of one plus the sorted adjacent raw gaps.
For each large gap choose one dyadic interval contained in its prescribed
physical gap. The intervals are disjoint and chosen before that parity's
field is sampled. The corresponding slope variables are independent;
successive row-count differences give independent bounded-width strips.
The first row then leaves only \(O(1)\) possible offsets. Bounded raw
gaps contribute only a fixed factor and require no separate slope
variable. This also handles repeated raw coordinates.

Fix an integer physical odd-row tuple
\(a=(a_0,\ldots,a_{k-1})\). The required even tuple in (1) is now
specified by \(b_{\sigma(v)}=a_v+Y_v\). Conditional on the anchors,
the odd and even row-field events are independent. Applying (6) to both
gives
\[
 \Pr(\text{this tuple and (1)})
             \le {C_k\log^{4(k-1)}(2h)\over h^2Q_0Q_1}.        \tag{7}
\]
This multiplication is between two independent parity fields for fixed
targets. No physical target or selected interval is chosen after seeing
its own field. The sum over target tuples is taken afterward.

## 3. Count the feasible odd tuples

The occurrence lists have successive physical gaps between two fixed
positive constants. Hence each consecutive odd-path edge gives a
constraint
\[
                  a_v-a_u\in I_{uv},\qquad
                  |I_{uv}\cap\mathbb Z|\le C w_0(uv),         \tag{8}
\]
with orientation chosen from the sorted raw indices. The interval is
deterministic. For an even-path edge, substitute (1) into the analogous
bound for the even rows:
\[
                  a_v-a_u\in J_{uv}-(Y_v-Y_u),\qquad
                  |J_{uv}\cap\mathbb Z|\le C w_1(uv).         \tag{9}
\]
The signed heights only translate these intervals. Fixed row errors
enlarge them by a constant and preserve the displayed bounds.

Take any spanning tree \(T\) in the union. Its root row has \(O(h)\)
possible in-strip integer values. Given a parent's value, its child has
at most \(Cw_e\) choices by (8) or (9). The remaining edges impose
additional conditions and may be discarded. Therefore the number of
feasible tuples is at most
\[
                         C_k h\prod_{e\in T}w_e.     \tag{10}
\]
Choose the tree minimizing that product and sum (7). This proves (5).

For bounded-error central provenance forms, first fix the finitely many
integer error choices and base origins. The same argument applies and
the finite union changes only the constant. Original genuine-row
eligibility, bad-row exclusions, and cap-clearing conditions can be
discarded in an upper bound; they are not conditioned upon. This does not
allow a target to be an unrelated opposite-parity-dependent row function.

## 4. A quantitative gain from crossing row clusters

For vertices \(u,v\), let \(B_0(u,v)\) be the largest edge weight on
their unique path in \(P_0\). If \(e=uv\) is an edge of \(P_1\),
then adding \(e\) to \(P_0\) and removing a largest edge of the cycle
gives
\[
                       \tau\le Q_0\,{w_1(e)\over B_0(u,v)}.   \tag{11}
\]
There is a symmetric formula with the parities exchanged. In particular,
if a small gap of one row ordering crosses a gap at least \(R\) times
larger in the other ordering, (5) improves the corresponding conditional
one-parity bound by a factor \(R\).

For an equivalent cluster statement, let \(\mathcal P_\alpha(t)\)
be the connected-component partition of the path \(P_\alpha\) after
retaining edges with weight at most \(t\). If no replacement in (11),
in either direction, gives a factor greater than \(R\ge1\), then
\[
 \mathcal P_0(t)\text{ refines }\mathcal P_1(Rt),
 \qquad
 \mathcal P_1(t)\text{ refines }\mathcal P_0(Rt)
                    \quad\text{for every }t.        \tag{12}
\]
Indeed every retained edge in one path has its endpoints connected in
the other path by edges of weight at most \(R\) times its own weight.
Conversely, a failure of either refinement exhibits such a replacement
gain greater than \(R\).

With \(R=1\), equality of the two cluster partitions at every threshold
means that both paths are minimum-product spanning trees. To verify this
without a separate graph theorem, choose a smallest-weight edge crossing
the current component partition and merge its endpoints. The threshold
partitions determine the number of merges at each weight. Each path has
exactly those merges and hence the same minimum product. The converse
also follows from (11): any edge whose endpoints need a larger edge in
the other path would strictly improve that path. Thus the exact absence
of a gain is agreement of the two small-gap cluster hierarchies.

The comparison concerns vertices of the edge equations: the even path
uses \(j_{\sigma(v)}\), not \(j_v\). Losing this cyclic reindexing
would change the claimed geometry.

## 5. What the four-cycle reduction gives

For fixed four-cycles, the preceding min-product and arithmetic counts
leave the regime
\[
                 h^{1-\varepsilon}<Q_0,Q_1<h^{1+\varepsilon}.
                                                               \tag{13}
\]
There are at most \(h^{4+o(1)}\) actual rank-and-height candidates.
If (11) supplies a gain \(R=h^\delta\), then (5) bounds their total
expected contribution by
\[
                           h^{2+\varepsilon-\delta+o(1)}.     \tag{14}
\]
Thus any fixed \(\delta>\varepsilon\) gives a power saving for that
subfamily. The still-critical patterns have the two cluster hierarchies
aligned to within the corresponding scale factor, as in (12).

This is a genuine remaining case. For example, give both paths the same
vertex order and weights \((R,1,R)\). Their products and the minimum
tree product are all \(R^2\), so (5) gives no improvement over the
one-parity bound. These gap data arise from odd raw coordinates
\((0,R-1,R-1,2R-2)\) and from the same ordered values for
\((j_{\sigma(0)},\ldots,j_{\sigma(3)})\).
The example only shows that the gap/tree information alone cannot force
a gain. It is not asserted to be an actual in-strip P-cycle, a valid
Hilbert embedding with its required rank gaps, or an obstruction to the
construction.

The bound therefore replaces an adaptive two-field interval proposal by
a rigorous fixed-target argument and isolates compatible cluster patterns.
The subsequent [four-cycle theorem](continuation_central_four_cycle_bound.md)
handles those patterns by a close-height arithmetic count and obtains
\(h^{43/22+o(1)}\) for all central genuine four-cycles. Longer cycles
and the singleton choice problem are not resolved by the tree bound alone.

## Review status

The point-mass input was independently reviewed in the multiscale note.
The joint tree-volume bound and cluster classification passed a separate
independent written review. That review checked fixed-target conditional
independence, translated interval widths, repeated coordinates and parallel
edges, both directions of the threshold refinement, and the cyclic shift
in the even-coordinate order.
