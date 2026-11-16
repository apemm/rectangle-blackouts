# Separate actual-good anchors from buffered permutation eligibility

15 November 2026. Good-anchor gap estimates need not hold after the
forbidden row set is enlarged by a fixed interpolation radius. The
enlargement can instead be used only to decide which genuine doubles
may move. Boundary-clean caps are selected using the actual forbidden
rows. This preserves the good-anchor input and permits bounded physical
row jumps in the interpolation proof.

There is one new bookkeeping requirement: interpolation can create an
intrinsically forced odd singleton outside the caps. Such a rank has a
deterministic near-bad nonanchor witness. It must be included in the
compiled exceptional-source family. This note does not prove a
simultaneous residual choice or an occupancy-preserving repair.

## 1. Two row sets with different purposes

Work in the row-index coordinates for which physical rows have the form
\(\rho_\alpha+4z\), for roles \(\alpha=0,1\). Let \(B_\alpha\)
be the actual forbidden row-index set in the already chosen profile
pool. Its definition must be one for which the explicit good-family
criterion is valid. Bulk and half-strip restrictions define the pool;
an additional filter that removes good anchors needs its own check.

Use \(B_\alpha\), without a buffer, for:

* selecting and planting the explicit good anchors;
* testing the raw row lists and selecting boundary-clean caps;
* deciding which virtual row options are intrinsically good.

Let \(f_0,f_1\) be the two total coordinate functions after the
compatible one-coordinate cap filling. Assume their common Hölder
constant is \(C_0\). Fix a permutation block size \(k\), and set
\[
 C_1=C_0\sqrt{2k-1},\qquad
 D=\max\{1,\lceil C_1\rceil\},\qquad
 B_\alpha^{+D}=\{z:\operatorname{dist}(z,B_\alpha)\le D\}.
                                                               \tag{1}
\]
Only genuine doubles whose two coordinates avoid \(B_\alpha^{+D}\)
may move. Fix every cap, singleton, and other genuine double.

In particular, a genuine double using a row in
\(B_\alpha^{+D}\setminus B_\alpha\) can remain at its original rank.
It need not be relocated or declared unavailable. If some separate
placement policy relocates these labels, their literal-good virtual
options may still be used for singleton filling. There are only
\(O(h(|B_0|+|B_1|))\) such labels, but their number alone does not
authorize an unsafe point erasure.

## 2. Boundary-clean caps give safe unchanged edges

Before capping, consecutive Hilbert ranks change at most one raw
coordinate. A sampled or planted scalar row map can turn this into a
physical index jump of magnitude up to a fixed \(D_0\), rather than
a unit jump. A plateau can remove the change. The two coordinate maps
still act separately.

The boundary-clean cap selection covers every leaf having an actual
bad option. Outside the selected caps both original options are good.
Inside a selected cap \(Q\), its common coordinate is replaced by a
constant good value and its other coordinate remains the original
scalar row function. At either boundary rank of \(Q\), the replaced
coordinate equals its original value, and both original endpoint
options are good.

It follows that every consecutive edge of the capped coarse functions
has at most one varying coordinate. Whenever a coordinate varies, the
other coordinate is constant and good:

* Inside a cap, a surviving change is in the noncommon role, while the
  common role is the good constant.
* Outside caps, both original endpoint pairs are good. Their constant
  role is therefore good.
* Across a cap boundary, or between adjacent caps, the endpoint pairs
  are their original pairs and are both good. The original Hilbert edge
  changes only one coordinate.

This includes folded maps, V-arm plateaus, and bounded physical
increments produced by anchor planting. It uses boundary cleanliness;
a merely common-coordinate-good cap does not supply the same boundary
argument.

## 3. Interpolation with separately buffered movable doubles

Let \(\pi\) permute the eligible genuine objects within their fixed
blocks and fix all other ranks. Put \(g_\alpha=f_\alpha\circ\pi\).
For distinct ranks,
\[
 |\pi(r)-\pi(s)|\le(2k-1)|r-s|,
 \qquad
 |g_\alpha(r)-g_\alpha(s)|\le C_1\sqrt{|r-s|}.          \tag{2}
\]
An edge is changed when at least one endpoint is moved. On a changed
edge choose such an endpoint. In each role its value is outside
\(B_\alpha^{+D}\), and the other endpoint is at distance at most
\(D\). Every integer between the two values therefore avoids
\(B_\alpha\). Both coordinates can be interpolated through good
values, even when the other endpoint is a frozen buffer-only object.
No additional one-block guard or buffered condition on that frozen
endpoint is needed.

On an unchanged edge, Section 2 gives a constant good role. Walk the
other coordinate monotonically through unit row-index steps. Intermediate
values of that coordinate may be bad, but the constant good role keeps
every fine slot occupied.

Use the separated mesh from
[the permutation interpolation theorem](continuation_permuted_step_four_interpolation.md),
with \(G=8D\) and \(M=32D^2\). Its estimates for one or more unit
changes and for rank distances at least \(M\) use only (2), the bound
\(D\) on adjacent coordinate differences, and the fixed mesh spacing.
They do not use the old unit-jump hypothesis for occupancy.
Consequently the same conclusions hold:
\[
 |\Delta y|^2\le2|\Delta x|
\]
for every same-role pair except the isolated adjacent
\((\pm4,\pm4)\) seams. The norm-gap, isolated-triangle, and horizontal-cone
exclusions remain valid. Every spacing-four column has a good option,
and each retained genuine double occurs only at its own anchor.

The finer potential row values still have boundedly many origins:
\[
             f_\alpha(v)+e,\qquad |v-r|\le k,\quad |e|\le D.
                                                               \tag{3}
\]
The constants are independent of height. All previous cautions about
actual Hilbert identities, candidate provenance, and prior rank-specific
option erasures remain in force.

## 4. The new near-bad interpolation singleton family

A changed edge has both fine options good, so it creates no intrinsic
forced parity. On an unchanged edge outside cap interiors, the even
coordinate can cross an actual bad row despite having good coarse
endpoint values. Its constant odd coordinate then supplies the only
good option at that fine rank.

Thus the statement that all initial forced-odd points lie in caps is
not retained. However, an actually changing even edge that crosses
\(B_1\) has a coarse even endpoint in
\[
                        B_1^{+D_0}.                        \tag{4}
\]
This is a deterministic set of size \(O(|B_1|)\).
For the V-map with one clamped anchor per parity, choose an endpoint
having a nonconstant raw form: two clamped endpoint forms would have
the same anchor value and the even edge would not change. An endpoint
whose value happens to equal the anchor may still use its valid
nonconstant boundary formula. Across a cap boundary, the endpoint
equals its original raw pair, so the same choice is available.

Each fine source has only a fixed number of candidate coarse edges
and endpoints before sampling. Each bad or near-bad nonanchor physical
row has only boundedly many raw preimages on the two monotone arms.
Consequently these new off-cap sources occupy \(O_{k,D_0}(h|B_1|)\)
fine ranks, before any subsequent option deletions.

For probability estimates, (4) is a small deterministic target set at
a fixed nonanchor coordinate index, after the finite origin menu has
been enumerated. It is therefore an admissible witness in
[the dirty-witness kernel](continuation_dirty_witness_path_kernel.md)
and [its two-arm version](continuation_nonanchor_v_product_kernel.md).
Those kernels do not require every member of the witness set itself
to be forbidden. Their repeated-index cases are retained. A bound
covering only points in selected caps must be enlarged explicitly to
include this family; it is not transferred just by calling it a cap
event.

## 5. What this resolves for good-anchor moments

The sampled raw bad runs relevant to literal cap selection and to the
multi-anchor good lists are now runs of \(B_\alpha\). Planting anchors
from the audited residue classes therefore supplies the corresponding
raw-run moments, provided those anchors avoid every actual filter in
\(B_\alpha\). No moment estimate is claimed for \(B_\alpha^{+D}\).
Buffer-only frozen genuine objects do not delete anchors or create new
bad raw-coordinate runs.

Inside a selected cap all objects remain fixed. Its original raw
traversal and first-hit anchor order are therefore unchanged by the
permutations outside it. The
[multi-anchor cap menu](continuation_multi_anchor_cap_menu.md) can use
the literal good set for its stated partial-locality and barrier
conclusions, and its short-run deterministic menu has the same
\(O((G_{\rm run}+1)\log h)\) bound as before.

That optional menu is a separate support union. It can introduce copied
rows and requires its existing provenance and geometry checks before
transferring a full fine-grid theorem. In particular, a multi-anchor
partial function is not silently substituted for the two total
one-coordinate cap functions in Sections 2--3. The separation proved
here resolves the buffer-versus-anchor issue; it does not remove that
pre-existing optional-menu obligation.

All literal-good points satisfying the established refined geometry
remain subject to the same four residual geometric families. The new
bookkeeping is the off-cap near-bad source family and the restricted
movement of buffer-only objects, not a proof that those residual
constraints can all be avoided.

Independent review: the complete saved proof passed two separate written
reviews. They checked the boundary-clean edge cases, one-endpoint
clearance on changed edges, the unchanged mesh estimates and isolated
seams, finite candidate origins, the nonanchor near-bad witness and
\(O(hb)\) count, and the explicit separation of the optional partial
multi-anchor menu from the total-function interpolation theorem.
