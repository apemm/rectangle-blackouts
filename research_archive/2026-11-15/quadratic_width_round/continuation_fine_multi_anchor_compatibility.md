# Fine-grid compatibility of the short-run multi-anchor menu

15 November 2026. A slower constant mesh makes the multi-anchor cap menu
compatible with the spacing-four geometry. No preliminary parity holes
are added outside the modified caps. The only remaining unit seams are
unchanged seams of the original interpolation.

A running-coordinate record in a Hilbert node is a face of a descendant
ancestor of the current rank. Consequently the short-run menu has a
shifted face-grid representation. This restores its one-parity mass
estimates. A new target-first packing argument also transfers the
genuine-source bidirectional-P count without pretending that two
projected coordinates form one corner.

## 1. A slow full interpolation with an additive unit error

Use the literal-good/buffered-motion separation from
[the separation theorem](continuation_actual_good_anchor_separation.md).
After the permitted fixed-block permutations, let the total coarse
row-index functions have Hölder constant \(C_1\), and choose an integer
\(D\ge\max(1,C_1)\). Adjacent coordinate differences are then at most
\(D\). All selected cap objects remain fixed.

Set
\[
 \epsilon_0=1/64,\qquad G_0=256D,\qquad M=4096D^2.
                                                               \tag{1}
\]
Anchor coarse rank \(r\) at fine rank \(Mr\). On each coarse edge,
move each coordinate monotonically through unit index steps at its
first required times \(Mr+jG_0\), \(1\le j\le D\), and then hold
its final value. Both coordinates may change at the same mesh time.
On a changed edge both coordinates are actual-good. On an unchanged
edge a constant good role is available by the boundary-clean argument.
Thus this full interpolation has a good option at every fine rank,
without adding any scheduled holes.

Write its total row-index functions as \(F_\alpha\). For all fine
ranks \(t,u\), with \(q=|t-u|\),
\[
 |F_\alpha(t)-F_\alpha(u)|^2\le \epsilon_0q+1.          \tag{2}
\]
For \(q\ge M\) the stronger bound
\[
 |F_\alpha(t)-F_\alpha(u)|^2\le\epsilon_0q              \tag{3}
\]
holds. Indeed, for \(q\le M\), at most \(2D\) unit changes of a
coordinate occur between the points. If their number is \(j\ge2\),
\[
 j^2\le4D(j-1),\qquad q\ge G_0(j-1),
\]
which gives the bound \(\epsilon_0q\). Zero or one change contributes
at most one. For \(q\ge M\), comparison with the two coarse left
anchors gives the bound
\((4C_1^2+8D^2)q/M\le12D^2q/M<\epsilon_0q\).

Every coordinate is constant on a neighborhood of each coarse anchor
of radius at least \(G_0-1\). All changes on the preceding edge finish
by \((r-1)M+DG_0\), and the next possible change is at \(rM+G_0\).
The original unit seams of each role are separated by at least \(G_0\).

## 2. First-hit anchors and the fine bridge

Let a selected boundary-clean cap have coarse interval
\([\ell,u]\). Its modified fine interval is \([M\ell,Mu]\).
Its common role remains a constant good row throughout this interval.
In the other role, take the original coarse first-hit sequence of
good raw-coordinate levels, in their directed order across the cap.
Append the exit rank if its raw level was first visited earlier.
The appended interval is a return interval.

All these anchor times are coarse multiples of \(M\). Distinct
consecutive anchors \(a<b\) therefore have \(L=b-a\ge M\), and
their row-index values \(A,B\) satisfy
\[
                         g^2:=|B-A|^2\le\epsilon_0L. \tag{4}
\]
For \(g=0\), offer that constant row throughout. Otherwise put
\[
 d=\left\lceil\frac{g^2}{4\epsilon_0}\right\rceil
       \le L/4,
\]
where \(L\) is a multiple of four, and choose independently
\[
 p\in [a+L/4,\ a+3L/4-d]\cap\mathbb Z.                \tag{5}
\]
Offer \(A\) through \(p\), and \(B\) from \(p+d\).
The intervening \(d-1\) ranks have no option in this role. The
common cap role stays available there. The set in (5) has at least
\(L/4\) choices.

The left and right plateaus extend at least \(L/4\) from their
respective interval endpoints. For unequal rows, \(d\ge16\).
Every offered row is actual-good. Original genuine labels in these
caps were already relocated; this modification loses no further label.
Outside the modified cap intervals keep the original fine options.
One may apply the modification only on short-run caps and retain the
compatible original filling on all other caps.

## 3. Exact square bounds and isolated seams

Consider selected points of one fixed role. Within one bridge interval,
points assigned different endpoint rows are separated by at least \(d\),
so their squared index difference is at most \(4\epsilon_0q\).
Points assigned the same row have difference zero.

For points in different copied intervals, or with one point outside the
copied intervals, choose their associated original fine anchors.
The facing-endpoint comparison bounds their original rank distance by
\(4q\). Unchanged points are their own anchors. Applying (2) gives
\[
                   |\Delta z|^2\le4\epsilon_0q+1.     \tag{6}
\]
If the integer \(|\Delta z|\ge2\), then
\[
 |\Delta z|^2-1\ge\tfrac34|\Delta z|^2,
 \qquad
 |\Delta z|^2\le\tfrac{16}{3}\epsilon_0q<q/2.          \tag{7}
\]
If \(|\Delta z|=1\), the desired bound
\(|\Delta z|^2\le q/2\) holds for every \(q\ge2\).

There is no new unit seam at \(q=1\). Inside a bridge, unequal
endpoint options are separated by \(d\ge16\). Consecutive bridges
agree on their quarter-length plateaus around the shared anchor.
At a cap boundary, the copied endpoint plateau meets the original
mesh's constant coarse-anchor guard. The common cap role is unchanged.
These arguments also cover adjacent caps and return intervals.

Hence the only possible \(q=1,|\Delta z|=1\) pairs are unchanged
unit seams of the original interpolation. They remain separated by
at least \(G_0\) in each role. In physical coordinates
\((x,y)=(4t,\rho_\alpha+4z)\), all other same-role pairs obey
\[
                            |\Delta y|^2\le2|\Delta x|. \tag{8}
\]
The established norm-gap, isolated-seam triangle, and horizontal-cone
mixed-support exclusions therefore apply. In particular, the optional
menu now has the full spacing-four geometry, not merely a partial
Hölder estimate. All columns remain occupied.

No new forced points have been introduced outside modified caps.
The old near-bad off-cap interpolation sources remain exactly as
described in the separation theorem.

## 4. Barrier lengths and their bookkeeping

Each bridge barrier has length
\[
                  w=d-1<g^2/(4\epsilon_0).            \tag{9}
\]
Its pointwise unavailability probability is at most
\(\min(1,g^2/(\epsilon_0L))\), under the uniform choice in (5).
Opposite-role cap families still use independent bridge variables.
The full-reachability and local-load choice criteria apply with these
new probability bounds.

If the raw row maps have adjacent index increments at most \(D_0\),
and consecutive good raw levels enclose a bad run of length \(v\),
then \(g\le D_0(v+1)\). Every short-run bridge consequently has
width \(O((G_{\rm run}+1)^2)\).

Unlike the earlier coarse menu, adjacent good raw levels need not
give a zero fine barrier: their physical rows can differ, and (9)
can give a bounded positive width. For a cap of side \(a_Q\), the
additional constant contribution is \(O(a_Q)\). The run charging
from the multi-anchor note therefore gives
\[
 \sum_Q w_Q\le C\left(\sum_Qa_Q+Nb\right)
             \le C\left(A_{\rm cap}+Nb\right),         \tag{10}
\]
where \(A_{\rm cap}=\sum_Qa_Q^2\), and \(b\) bounds the bad raw
coordinate cardinality in each role. For a cap sample with the
established \(A_{\rm cap}=O(hb\log h)\), this is still subquadratic.
The earlier deterministic \(CNb\) bound is not claimed unchanged.

## 5. Running extrema are ancestor faces

Here is the deterministic provenance fact needed for the new rows.
Fix a Hilbert node \(Q\) and a rank \(r\) in it. The maximum, or
minimum, of either raw coordinate over the prefix of \(Q\) ending
at \(r\) is a coordinate face of some dyadic ancestor \(R\) of \(r\)
with \(R\subseteq Q\). A leaf is allowed.

To prove this, let \(C\) be the child of \(Q\) containing \(r\).
The prefix consists of complete earlier children and a prefix of \(C\).
For the maximum, a complete child's coordinate maximum is either
the upper outer face of \(Q\) or the face just below its midpoint.
Relative to \(C\), this is an outer face of \(Q\), a face of \(C\),
or below the whole coordinate range of \(C\), in which case it cannot
beat the current prefix. If the prefix of \(C\) wins, recurse.
The minimum argument reverses the inequalities. This does not depend
on the Hilbert orientation or the order of the four children.

For an anchor interval containing a fine rank \(t\), use the coarse
rank \(\lfloor t/M\rfloor\). Its directed running record lies between
the two successive good raw levels. If the intervening bad run has
length at most \(G_{\rm run}\), either copied anchor index is within
\(G_{\rm run}+1\) of that record. The appended return uses the exit
face. Therefore every new scalar row is of the form
\[
 f_\alpha(c+e),\qquad
 c\text{ a face of an ancestor of the current coarse rank},\quad
 |e|\le G_{\rm run}+1.                                \tag{11}
\]
The common cap coordinate has the same form with \(e=0\).
Taking the union over all potential caps does not add a second
independent ancestor choice to (11): all the resulting \(R\)'s are
already ancestors of the current rank. There are
\(O((G_{\rm run}+1)\log h)\) scalar candidates before field sampling,
cap selection, or bridge choices. Hybrid old-fill values add only
their existing raw/corner candidates and bounded interpolation shifts.

## 6. The shifted face-grid mass bounds

Fix a dyadic side \(a\) and a shift \(e\). At that depth the candidate
indices lie in the union of the two translated grids
\[
                       ma+e,\qquad ma-1+e.
\]
For each such index, at most \(CNa\) coarse ranks have the corresponding
ancestor face; fine ranks change this by the fixed factor \(M\).
The total rank mass at that depth is \(O(N^2)\). All relevant sides
are at most the original selected-cap cutoff, since \(R\subseteq Q\).

For two fixed shifts and sides \(a,b\), the number of pairs of ranks
whose effective indices differ by at most \(W\) is at most
\[
                      C N^3\bigl(W+\min(a,b)\bigr).    \tag{12}
\]
For example, if \(a\le b\), there are \(O(N/b)\) coarse-grid values
on the second side and at most \(O(1+W/a)\) first-grid values near
each. Multiplying by the masses \(O(Na)\) and \(O(Nb)\) proves
(12). Arbitrary fixed translations of the grids do not change this
argument. The same annular summation yields the corresponding
reciprocal-distance bounds.

Thus the scalar cap-grid mass estimates used in the long-six counts
survive, after an explicit \(G_{\rm run}^{O(1)}\) union over the
finitely many point shifts. At a fixed arity, a choice
\(G_{\rm run}=h^{o(1)}\) changes only the \(h^{o(1)}\) loss.
The prescribed-row kernels are applied to each deterministic shifted
index before any selection event is imposed. Actual close-row or
long-support conditions still come from the geometry in Section 3.

## 7. The two P transfers and the remaining scope

The two virtual coordinates of a cap rank can now come from different
ancestor levels. They need not form one endpoint corner of any single
cap. The new
[rank-dependent target-pair theorem](continuation_rank_dependent_cap_p_pairs.md)
handles this directly. For each potential cap \(Q\), target rank \(s\),
and deterministic coordinate-pair candidate \(c(Q,s)\), sum reciprocal
distances over the \(O(h)\) possible genuine source cells outside \(Q\).
The sum is \(O(\sqrt h)\), uniformly in the pair \(c(Q,s)\).
Only \(O(\min(a_Q^2,h))\) target ranks can meet such exterior sources.
The original cap-depth summation therefore gives
\[
       \mathbb E N_{\rm bidirectional}
            \le G_{\rm run}^{O(1)}h^{3/2+o(1)}.        \tag{13}
\]
The deterministic pair menu is fixed before sampling and independently
of the genuine source rank. This is the required new argument; the
old one-corner hypothesis is not asserted.

The
[all-cap dirty-child P estimate](continuation_dirty_child_cap_p_incidence.md)
also transfers after the explicit shift union. Enumerate the actual
cap ancestor and its dirty-child boundary witness, in addition to (11).
For nonanchor endpoints, a bad witness row \(z\in B\) at raw distance
\(d\) from its same-parity endpoint gives a two-row factor
\(C/[h(1+d)]\). Their physical row difference is \(O(1+d)\)
under the bounded-gap V map. Summing those endpoint values cancels
the distance denominator; the independent opposite endpoint contributes
\(C/h\). The result is \(Cb/h^2\) for each fixed form list.
The anchor cases retain \(Cb/(hE)\) and the in-strip span bound
\(O(\sqrt{Eh})\). Hence
\[
 \mathbb E N_{\rm cap\text{-}P}
       \le G_{\rm run}^{O(1)}h^{o(1)}
                    \left(hb+\frac{h^{3/2}b}{\sqrt E}\right).
                                                               \tag{14}
\]
The literal bad-row target set and its deterministic child witnesses
are unchanged. No paired-corner assertion is needed. Off-cap
near-bad interpolation sources keep their separate witness from the
separation theorem.

Likewise, a short or growing path estimate does not establish full
reachability. The fine geometry, shifted-grid incidence transfer,
barrier choice criterion, and safe external relocation remain distinct
parts of the construction. The theorem supplies a compatible menu and
does not solve its residual P, three-point, four-point, or parked-six
constraints.

Independent review: the complete geometry and grid-mass proof passed
two separate written reviews, including the explicit constants,
coarse-anchor bound, integer absorption, absence of new seams,
additional cap-side barrier charge, and the prefix-face origins.
The two P transfers in Section 7 were also checked independently
against their fixed-target and dirty-witness proofs. The full
construction and repair limitations remain as stated.
