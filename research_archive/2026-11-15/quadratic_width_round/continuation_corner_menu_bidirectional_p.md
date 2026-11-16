# Bidirectional P remains sparse for the two-corner cap menu

15 November 2026. A cap target whose two virtual coordinates are copied
from one corner still admits the \(h^{3/2+o(1)}\) genuine-source
bidirectional-P bound. The proof uses a global reciprocal-distance
packing estimate and does not require only one projected coordinate.

This transfers one P estimate to the
[boundary-clean two-corner menu](continuation_boundary_clean_movable_caps.md).
It does not solve forced singleton constraints or justify arbitrary
pairings of corners from unrelated cap nodes.

## 1. Scope and candidate pairs

The padded raw Hilbert square has side \(N=\Theta(h)\). A retained
genuine central source at raw rank \(r\) has raw cell \(z_r\).
It lies outside every selected cap. At a target rank \(s\) inside a
selected dyadic cap \(Q\), a complete virtual pair in the new menu
is copied from one of the two endpoint corners \(c_Q\) of that
same cap. The common-coordinate cap value and one opposite endpoint
value are precisely the two coordinates of this corner.

Count the two directed norm constraints
\[
                         b_s-a_r=Y_1,\qquad
                         b_r-a_s=Y_2.                \tag{1}
\]
The signed heights and all potential cap forms are enumerated before
row sampling. An actual in-strip P has horizontal span below \(h\).
Consequently, for the fixed-stride order,
\[
                              |s-r|\le C h.          \tag{2}
\]
The same bound, with a different constant, holds for bounded fine
expansions and bounded provenance errors when a target pair comes
from one such cap corner and its genuine source base lies outside \(Q\).
No transfer to arbitrary multi-origin interpolation is asserted.

For each fixed pair of ranks, norm factorization leaves only
\(h^{o(1)}\) signed pairs \((Y_1,Y_2)\). Keeping these choices costs
only that factor.

## 2. The reciprocal-distance probability

First suppose both target coordinates are nonconstant row forms at
the corner's raw indices. Condition on one parity's full parameters.
The other parity then has two prescribed row values, at its source
index and corner index. The reviewed two-row kernel gives
\[
 {h^{o(1)}\over h(1+|z_r^{(1)}-c_Q^{(1)}|)}
 \quad\hbox{or}\quad
 {h^{o(1)}\over h(1+|z_r^{(2)}-c_Q^{(2)}|)}.
\]
Take the smaller bound, without multiplying the two conditional
estimates:
\[
 \Pr((1))\le
 {h^{o(1)}\over h(1+\|z_r-c_Q\|_\infty)}.             \tag{3}
\]
The source-outside-cap condition ensures \(z_r\ne c_Q\), though the
added one in the denominator also covers bounded-error versions.
The kernel holds for the independent-arm and multiscale fields.
The residue-restricted offset law changes it by at most a constant.

If a target coordinate is a fixed sampled anchor, condition on all
anchors first. One equation in (1) prescribes a genuine source row
in the opposite parity, costing \(O(1/h)\) through its offset.
After fixing that parity's full parameters, the other equation
prescribes the other genuine source row, costing another \(O(1/h)\).
Thus anchor forms have probability \(O(h^{-2})\) under the original
law, and the same order after bounded-density restriction.
Their \(h^{3+o(1)}\) total rank and form candidates contribute
\(h^{1+o(1)}\).

## 3. A packing bound that avoids a facing-corner condition

For any set \(A\) of \(m\) distinct integer grid cells and any fixed
integer grid cell \(c\),
\[
                  \sum_{z\in A}{1\over1+\|z-c\|_\infty}
                          \le C\sqrt m.             \tag{4}
\]
Indeed at most \(C R^2\) grid cells are within distance \(R\) of \(c\).
The cells of smallest distances maximize the sum; summing square
shells up to radius \(O(\sqrt m)\), or ordering the distances,
proves (4).

Fix a potential side-\(a\) cap \(Q\), whose rank interval has length
\(a^2\). A source outside this interval can have (2) with a target
inside it only if it lies in one of the two exterior rank intervals
of length \(Ch\). There are \(O(h)\) such sources and their raw cells
are distinct. For each source, there are at most
\(\min(a^2,Ch)\) possible target ranks. Therefore (4) gives
\[
 \sum_{\substack{r\notin Q,\ s\in Q\\|r-s|\le Ch}}
          {1\over1+\|z_r-c_Q\|_\infty}
                \le C\min(a^2,h)\sqrt h.             \tag{5}
\]
This holds for either corner, regardless of its distance to the
source-side boundary. In particular no assumption about which
corner faces the source is needed for the count.

## 4. Sum all potential caps before selection

At side \(a\), there are \(N^2/a^2\) potential aligned cap nodes
and at most two target corners each. Combine (3) and (5):
\[
 \mathbb E N_{2,a}
 \le h^{o(1)}
       {N^2\over a^2}\,
       {\min(a^2,h)\sqrt h\over h}
 \le h^{3/2+o(1)}.                                   \tag{6}
\]
For \(a>\sqrt h\) the bound decreases with \(a\).
There are \(O(\log h)\) dyadic depths. Thus all nonconstant cap
corner targets together satisfy
\[
                \mathbb E N_{\rm bidirectional}
                        \le h^{3/2+o(1)}.             \tag{7}
\]
Add the lower-order anchor term and the previously reviewed raw-target
case. This proves the same bound for all target forms in this menu.
It also bounds the incident genuine source labels.

The deterministic candidate count retains every potential cap and
corner. Cap selection, boundary cleanliness and the allowed bridge
position are discarded before probability estimates. The source
condition \(r\notin Q\) is only a necessary geometric condition of
an actual retained-source/selected-cap pair, so it is safe to retain
in the overcount.

## 5. What the extension does not do

The count uses one paired corner from one cap. It does not permit
independent choices of two unrelated coordinate projections.
The movable menu's partial same-parity locality and occupancy still
require its own endpoint argument.

The estimate can enter a joint cost objective and the established
genuine-endpoint pruning when its separate occupancy and relocation
conditions are met. It does not bound every P edge from a newly
forced barrier point, eliminate longer forced paths, or prove a
complete support repair.

Independent review: the complete written proof passed a separate
check of the global grid packing, exterior source intervals, target
multiplicity, cap-depth summation, nonconstant conditional kernels,
anchor conditioning, and retained one-corner provenance scope.
