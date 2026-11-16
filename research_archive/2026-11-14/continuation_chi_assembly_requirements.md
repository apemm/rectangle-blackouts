# What a chromatic bound must supply to the board

Date: 2026-11-14. Status: elementary graph statements proved below. Board
consequences are conditional on the cited assembly and relocation inputs.

An upper bound on \(\chi(G_T[\tau])\) is enough to produce the primary
P-free classes. The rigid placement does not require equitable classes or
list coloring. The additional requirement is control of monochromatic
auxiliary pairs, or a refinement that separates those pairs.

## 1. The geometric inputs

The compatibility check in `heavy_diagonals_sharp.md`, proof of
Proposition 3, lists these class properties:

- Every class is a subset of one \((T,\tau)\) and is independent in
  \(G_T[\tau]\).
- The number of classes per \((T,\tau)\) has a common upper bound.
- Restricting a class preserves the properties used by the geometry.
- Any random choices are independent across diagonals, are made before the
  prime choice, and satisfy the marginal bounds needed for relocation.

The current position rule in `consolidated_board_menu.md`, (B5), assigns a
separate position to each color index. It does not constrain the size of a
color class. Empty classes can be omitted or kept as empty positions.

Thus a proved proper coloring with \(c_T\) colors gives the primary class
input directly. It does not need an equitable coloring theorem or a
list-coloring theorem. It does not, by itself, give the marginal bounds
in Proposition 3(b).

## 2. A chromatic bound does not imply pair decorrelation

Let \(G\) be the complete \(c\)-partite graph, with each part containing
at least two vertices. Then \(\chi(G)=c\). Every proper coloring using
exactly \(c\) colors is constant on each part. Consequently two vertices
in one part have the same color with probability one under any probability
law on proper \(c\)-colorings.

This refutes a generic replacement of the degree hypothesis by a chromatic
hypothesis in the estimate
\[
\Pr(\chi(v)=\chi(w))\le\frac{1}{B-\Delta(G)}.
\]
The current proof conditions on every color except one and counts available
colors. It uses the degree bound, not only the existence of a coloring.

A universally valid alternative is refinement. Start from any fixed proper
\(c\)-coloring. Give each vertex an independent uniform secondary color
from \(\{1,\ldots,K\}\). The ordered pair of colors is proper, uses at
most \(cK\) classes, and satisfies
\[
\Pr(\text{two distinct vertices have the same refined color})\le1/K.
\]
The construction is independent across diagonals when its secondary choices
are. This is sufficient for the existing marginal relocation bookkeeping,
but the class count is multiplicative.

## 3. A deterministic refinement for capped auxiliary degree

**Lemma.** Suppose \(G\) has a proper \(c\)-coloring, and \(H\) has an
ordering in which every vertex has at most \(d\) earlier neighbors. Then
\[
\chi(G\cup H)\le c(d+1).                               \tag{1}
\]

Proof. Restrict \(H\) to each color class of \(G\). The same ordering gives
back-degree at most \(d\) in that induced graph, so greedy coloring uses
at most \(d+1\) colors. Refine the original classes by these new colors.

The multiplication cannot be replaced by a general additive estimate.
Take the complete \(c\)-partite graph with parts of size \(d+1\), and let
\(H\) be a clique within each part. Then \(H\) has back-degree at most
\(d\), but \(G\cup H=K_{c(d+1)}\).

Apply (1) to the corrected form of Theorem DC in
`audit_degree_capped_colouring.md`. Color every light label, including the
exceptional set \(Y\), in the primary graph. Put auxiliary edges only
between vertices outside \(Y\). The exceptional vertices are isolated in
this auxiliary graph. Its retained part has back-degree
at most
\[
d=9(D-1)+6,
\]
coming from the nine capped coordinate families and the bounded
\(R_{FF}^{+}\) family. Any proper \(c_T\)-coloring of the primary graph can
therefore be refined into at most
\[
c_T\bigl(9(D-1)+7\bigr)                               \tag{2}
\]
classes that avoid all retained auxiliary edges. This requires no bound on
the primary graph's degree.

Keeping the \(Y\) vertices in the formal coloring is necessary: the
assembly's condition (Xi1) requires every light label to have a class, even
though \(Y\) is subsequently relocated. The same bound (2) holds with this
correction.

The exceptional set in DC depends on the arithmetic coordinate counts,
not on the primary coloring. Its stated weighted relocation estimate is
therefore unchanged by this refinement, provided DC's placement and
relocation hypotheses hold. The refined classes are deterministic and
fixed before the primes are chosen. The cited audit verifies the use of
weighted Theorem D for deterministic \(Y\). Its correction multiplies the
\(R_{FF}\) density contribution by at most 64, which changes only constants.

With \(D=\lceil(\log h)^\eta\rceil\), a primary bound
\(c_T\le C(\log h)^\gamma\) leads to at most
\(C_\eta(\log h)^{\gamma+\eta}\) refined classes. Since \(\eta>0\) can be
fixed arbitrarily small in DC, this refinement preserves a claimed power
saving in the primary chromatic exponent, up to an arbitrarily small loss.
At stride four this uses the corrected, audited DC statement. A menu
extension has an additional obligation: `audit_menu_sweep_classes.md`,
Section 4, explicitly marks Lemma M and Theorem DC as unused by the menu
board. They are not covered by that audit's stride transfer. The same point
appears as RA-4 in `consolidated_board_menu.md`. Therefore a menu-wide
consequence remains conditional on the stride-dependent moment estimates
and their assembly transfer.

## 4. What is still needed

A proposed improvement \(\chi(G_T[\tau])\ll\kappa_T\) has an assembly route
without equitable or list coloring. It must be combined with one of:

- a proper-coloring law with the required pair marginals;
- independent secondary colors, with the multiplicative palette cost;
- a capped-degree auxiliary refinement such as (2), with its exceptional
  relocation estimate.

The remaining arithmetic problem is to prove a useful primary chromatic
bound on the heavy diagonals. A bound on the minimum number of colors
alone must not be substituted into the uniform-coloring marginal estimate.
No new primary chromatic bound is proved in this note.
