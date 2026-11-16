# A bad-row witness in the joint path kernel

15 November 2026. A prescribed bad-row witness improves the central
mixed-tree probability by \(b/h\), where \(b\) is the size of its
deterministic bad-row set. Combined with the full height-volume
argument, this bounds fixed-length paths carrying such a witness by
\(b h^{1+o(1)}\). The witness index must come from a predetermined
finite menu. It is not an additional freely chosen row coordinate.

The statement also isolates a useful cap-provenance reduction. Projected
corner indices do not themselves cost a factor \(h\). The independently
reviewed [two-arm kernel](continuation_nonanchor_v_product_kernel.md)
supplies the joint row estimate for all nonanchor V-map forms, extending
the path bound across both arms. Section 5 includes constant anchors
at a loss of \(h/E\) per parity. None of these counts proves a safe
singleton repair or reachability closure.

## 1. Fixed equations and a deterministic witness

Fix \(k\) cross-parity equations
\[
                  B_v-A_v=Y_v,\qquad 1\le v\le k,
                  \tag{1}
\]
at deterministic raw indices \(i_v\) and \(j_v\). The heights \(Y_v\)
are fixed integers. The two parity row fields and their offsets are
independent. Each field has bounded positive row gaps and the joint
prescribed-row estimate
\[
 \Pr\{F_\alpha(t_1)=y_1,\ldots,F_\alpha(t_m)=y_m\}
 \le \frac{h^{o(1)}}{h\prod_{\nu=1}^{m-1}
                      (1+|t_{\nu+1}-t_\nu|)}
 \tag{2}
\]
for fixed \(m\), with the indices sorted. The error factor is a fixed
power of \(\log(2h)\). Bounded integer errors may be fixed first.

Let \(P_0,P_1\) be the sorted-index paths on the \(k\) equation
indices, with weights one plus their raw gaps. Write \(Q_0,Q_1\)
for the path products, \(\tau\) for the minimum-product tree in
their union, and
\[
                         K=Q_0Q_1/\tau.
                         \tag{3}
\]
Repeated indices are allowed, with corresponding weight one. The
[mixed-tree theorem](continuation_mixed_path_tree_probability.md)
gives probability at most \(h^{-1+o(1)}/K\) for (1).

Choose a parity \(\alpha\), a deterministic additional index \(w\),
and a deterministic physical row set \(\mathcal B_\alpha\) of size
at most \(b\). Then
\[
 \Pr\{(1),\ F_\alpha(w)\in\mathcal B_\alpha\}
                  \le \frac{b\,h^{o(1)}}{h^2K}.
                  \tag{4}
\]
No index is selected after observing its own row field. A finite menu
depending on the deterministic rank-and-height candidate is handled by
a union bound, as specified below.

## 2. Insert the witness and root the tree at its row

It suffices to take \(\alpha=0\). Put
\[
                    D=1+\min_v|w-i_v|.
\]
Inserting \(w\) into the sorted odd indices changes their gap product
from \(Q_0\) to \(Q'_0\), where
\[
                       \tfrac12D Q_0\le Q'_0\le D Q_0.
                       \tag{5}
\]
If \(w\) lies outside the index range, the ratio is exactly \(D\).
If it splits a gap into lengths \(a,c\), assume \(a\le c\). The
ratio is
\[
 \frac{(1+a)(1+c)}{1+a+c},
\]
which lies between \((1+a)/2\) and \(1+a=D\). If the index repeats,
the added weight is one and the same statement holds.

Fix a witness target \(z\in\mathcal B_0\) and all original odd
targets \(A_v\). Equation (1) fixes the even targets. Independence
and (2) bound the mass of this full target tuple by
\[
                   \frac{h^{o(1)}}{h^2D Q_0Q_1}.
                   \tag{6}
\]
Take a minimum-product tree from (3), attach the witness to a
nearest-index odd vertex with edge weight \(D\), and root the
enlarged tree at its physical value \(z\). Every other tree edge
allows \(O(w_e)\) values for its child. For an even-path edge, the
fixed \(Y_v\)'s merely translate its permitted difference interval.
Thus there are at most
\[
                              C_k bD\tau
                              \tag{7}
\]
possible target tuples. Summing (6) proves (4).

When the witness repeats an existing index, root at that vertex
instead; there is no new free row value. When the witness has even
parity, its attached equation vertex is rooted at \(A_v=z-Y_v\).
Again the prescribed height translates an interval and changes no
count.

All targets and the intervals used for (2) are fixed before either
field is sampled. The summation over targets comes afterward. In
particular, this proof does not condition one parity on a
field-dependent target from that same parity.

## 3. Fixed-length actual P paths

Consider directed paths with \(k\) actual P edges, where \(k\) is
fixed, in the central genuine model. There are \(O(h^2)\) possible
first object columns. The horizontal gap and nonzero odd height of
every actual in-strip P are \(O(h)\).

For each deterministic rank-and-height path candidate, permit at most
\(W(h)=h^{o(1)}\) choices of a parity and witness index. This menu
may depend on the candidate ranks, fixed provenance choices, and fixed
geometric data. It must be specified without looking at the sampled
fields or offsets. The bad-row sets remain deterministic.

For each fixed coordinate-order and dyadic-gap bin, the full
[cycle-space height-volume argument](continuation_cycle_height_cycle_space_volume.md),
applied without deleting an edge index, gives at most
\[
                             h^{1+o(1)}K
                             \tag{8}
\]
possible tuples of all \(k\) signed heights. In detail, the threshold
incidence multigraph has \(k\) edges, its final circulation space has
dimension \(k-1\), and an adapted circulation basis has birth-product
\(K\). One height is free over \(O(h)\) values; the other basis
coordinates have product volume \(K\).

After choosing the heights, choose the first column. For each height
\(Y\ne0\), factor
\[
                          (L-X)(L+X)=Y^2.
\]
There are \(h^{o(1)}\) possible signed horizontal legs of an actual
in-strip P. They recover every later column successively. A fixed
column has bounded provenance multiplicity. The number of candidates
in the bin is therefore at most \(h^{3+o(1)}K\). Apply (4), sum over
the witness menu and the fixed-power logarithmic set of bins, and get
\[
 \mathbb E\#\{\text{actual \(k\)-edge paths with a permitted bad witness}\}
                              \le b h^{1+o(1)}.
                              \tag{9}
\]
There is no extra endpoint-coordinate enumeration in this height-first
count. For \(b=h^{5/6+o(1)}\), the bound is \(h^{11/6+o(1)}\).
Marking all genuine vertices of these fixed-length paths has the same
order of incidence cost. It does not establish a compatible parity
assignment after marking or relocation.

The estimate remains valid under the bounded-density offset restriction
from
[the cap residue theorem](continuation_cap_boundary_residue_offsets.md):
apply (9) under the original independent law, then use its uniform
density comparison. Independence within a parity need not survive the
restricted law.

## 4. Cap provenance without an extra endpoint factor

A fixed original Hilbert rank belongs to one dyadic ancestor per depth.
For a prospective selected cap, its endpoint coordinates and the four
boundary coordinates of each immediate child are deterministic grid
indices. Consequently the choices

* of an ancestor cap;
* of the cap corner or bounded-size fallback raw point used at an endpoint;
* of a dirty child and its bad boundary coordinate

give only \(O(\log h)\) choices at that rank, up to fixed factors.
For a path of fixed length, choosing such forms at its vertices and
one witness still gives \(h^{o(1)}\) choices. There is no free \(h\)
factor for the witness index and no additional \(L^2\) factor for a
cap of side \(L\). The actual rank inside a cap has already been
counted by the first-column and horizontal-leg enumeration.

This observation gives the following precise extension of (9).
At each physical column allow a deterministic \(h^{o(1)}\)-sized
menu of effective raw indices for each endpoint parity. Assume that,
for the chosen forms in one candidate, all the indices of a parity,
including its witness if any, use a single nonconstant monotone arm
with bounded row gaps and the joint estimate (2). Assume the two
parity arms are independent under the original law. Then (9) still
holds for the resulting candidate paths.

Indeed, form the two order paths from these effective indices. Their
largest gaps may now be \(O(h)\), rather than \(O(\sqrt h)\). This
does not change (8): the full circulation birth-product is still
exactly \(K\), and only \(O_k(\log h)\) dyadic levels are possible.
The bounded-gap row maps still give every circulation its required
physical height constraint. Once physical heights and the first column
are fixed, the later physical columns are fixed as before; the origin
menus add only \(h^{o(1)}\) possibilities.

A selected cap implies that one of its immediate children is dirty.
If all rows used by that candidate and its chosen dirty witness fall
in the stated common-arm regime, discard the remaining cap-selection
conditions and apply (9). This is an upper bound using deterministic
ancestor menus, not conditioning on selected caps.

The [two-arm product kernel](continuation_nonanchor_v_product_kernel.md)
now proves (2) for a tuple spread across both nonconstant arms of a
parity. A prefix variable on one arm supplies the reciprocal gap across
the split, independently of the internal-gap variables. Its Section 5
therefore extends (9) to all nonanchor paths touching selected caps.
Section 5 treats constant-anchor rows separately. Arbitrary menus
chosen after seeing the row fields remain outside the argument.

## 5. Constant anchors through an artificial index

Suppose each parity has one independently sampled good anchor \(A_\alpha\)
with maximum atom at most \(h^{o(1)}/E\), where \(E\le h\). The
anchors are independent of the two parity field families. The
nonanchor estimates hold uniformly after conditioning on their values.
All effective nonanchor indices lie in an interval of length \(O(h)\).

For each parity introduce one artificial index at distance \(\Theta(h)\)
beyond that interval, and assign every occurrence of its constant anchor
to this same index. Fixed bounded row errors may be enumerated first;
repeated anchor targets must agree after removing those errors.

Let \(\widehat Q_\alpha\) be the sorted-gap product after this
augmentation. If that parity has both anchor and nonanchor targets,
then
\[
          \widehat Q_\alpha\asymp h Q_{\alpha,\mathrm{non}},
\]
and its fixed-target point mass is at most
\[
 \frac{h^{o(1)}}{E}\,
 \frac{h^{o(1)}}{h Q_{\alpha,\mathrm{non}}}
       \le \frac{h^{o(1)}(h/E)}
                    {h\widehat Q_\alpha}.
       \tag{10}
\]
There is only one anchor atom, however often the anchor is used.
If every target of that parity is the anchor, then
\(\widehat Q_\alpha=1\), and its atom bound is again exactly of
the form on the right of (10). A parity without anchor targets
has no \(h/E\) loss.

On an artificial-to-nonconstant edge, the physical row difference
ranges over only \(O(h)\) values, comparable to its artificial gap
weight. All other row-difference intervals are unchanged. Thus the
mixed-tree tuple count and the full cycle-space height-volume bound
apply to these augmented index paths.

A dirty-row witness remains nonanchor because all anchors are good.
Insert its actual effective index into the augmented path. The
gap-insertion calculation (5) is unchanged, including when the
old parity targets consisted only of anchors. The witness's bad-row
root still gives the factor \(b/h\).

Consequently paths with anchors in exactly \(a\in\{0,1,2\}\)
parities satisfy
\[
 \mathbb E\#\{\text{fixed-length P paths carrying a permitted
                 dirty witness}\}
       \le b h^{1+o(1)}(h/E)^a.
       \tag{11}
\]
This covers all deterministic cap/corner endpoint forms in the
two-arm model, including constant endpoints. Anchor and branch
eligibility, selected-cap conditions, and all other restrictions
may be discarded in taking the upper bound. The proof first uses
the original independent law and then its bounded-density
residue restriction.

For \(b=h^{5/6+o(1)}\), take \(E=h^{17/18}\). The exponents in
(11) are, respectively,
\[
                  \frac{11}{6},\qquad
                  \frac{17}{9},\qquad
                  \frac{35}{18}.
                  \tag{12}
\]
The initial top-crop cost \(O(hE)\) also has exponent \(35/18\).
These are incidence and initial relocation budgets, not an assertion
that all counted paths can be removed compatibly.

There is a useful anchor exclusion for paths containing a retained
genuine double. Every actual P edge has horizontal span at most
\(h\), so a fixed-length path has total span \(O_k(h)\).
Both parity points of that double lie below the genuine top crop,
at least \(2E-O(1)\) from the upper boundary. Any constant anchor
lies within \(E+O(1)\) of that boundary. The global same-parity
Hölder bound would then require
\[
                        E-O(1)\le C_k\sqrt h.
\]
This is impossible when \(E/\sqrt h\to\infty\). Hence a fixed-length
path containing a retained genuine double has no anchor endpoint
at all. Its dirty-witness incidence uses the first bound in (12),
without retuning the anchor window for this subfamily.

## 6. Scope

The gain in (4) is a sampling gain for a specified geometric witness.
It cannot be applied to an unrestricted existential bad row by
silently summing \(h\) possible raw indices. Ancestor witnesses avoid
that loss because their menu is logarithmic and deterministic for a
fixed rank candidate.

The result controls each fixed path length. It neither bounds all
path lengths at once nor rules out a path between forced singleton
states. Such a reachability statement, or a separate occupancy-preserving
repair, remains necessary.

## Review status

Sections 1--4 passed an independent written review.
The review checked the two-sided gap-insertion ratio, the even-witness
root shift, full birth-product cancellation, and logarithmic cap menus
without an extra cap-area or endpoint-index factor. The later two-arm
kernel and its nonanchor cap-path consequence were also independently
reviewed. Section 5 passed a complete written review covering the
artificial-anchor mass, constant-only parity, witness insertion,
height-volume cancellation, all three displayed exponents, and the
retained-genuine anchor exclusion.
