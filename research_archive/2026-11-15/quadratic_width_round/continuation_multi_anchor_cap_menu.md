# A multi-anchor cap menu and its weighted path criterion

15 November 2026. Intermediate good opposite rows split a cap's single
forced barrier into barriers charged to squared bad-row gaps. This
preserves occupancy and partial same-parity locality. It also gives an
exact sufficient criterion for the P implication system, expressed in
terms of weighted reachability in a compiled graph.

Neither the required arithmetic gap estimate nor the weighted
reachability bound is established for the current row filters. The new
anchors also need a provenance audit before transferring the earlier
incidence counts.

## 1. A bridge formula valid at every interval length

Let f be C-Hölder with exponent one half on integer ranks. Let ell<u
have good endpoint values, put L=u-ell, and g=|f(u)-f(ell)|. If g=0,
offer that constant good row throughout the interval.

For g>0, set

`d=ceil(g^2/(4C^2))`.

Since g^2<=C^2 L, one has 1<=d<=ceil(L/4). Choose p from

`[max(ell,ell+ceil(L/4)-d), ell+floor(3L/4)]`.          (1)

Offer the left endpoint value through p and the right endpoint value
from p+d onwards. The d-1 intervening ranks have no option in this
parity. The other cap parity remains available there.

The range in (1) is nonempty and has at least L/2 integer choices.
Its upper endpoint plus d is at most u. Every left-anchor insertion
lies in the first three quarters of the interval, and every right-anchor
insertion lies in the last three quarters. The facing-anchor proof
therefore gives a global 2C-Hölder bound when this operation is applied
to any disjoint family of interval interiors.

The exact forced-barrier length is

`w=d-1<g^2/(4C^2)`.                                  (2)

There is no small-interval remainder. In particular g<=2C gives w=0.
Independent uniform choices of p give the pointwise bound

`Pr(r remains unavailable)<=min(1,g^2/(2C^2 L))`.      (3)

The sharper w divided by the number of choices in (1) may replace (3).
For a return interval it is zero.

## 2. Intermediate anchors inside a boundary-clean cap

Let Q be a selected boundary-clean Hilbert node with common-coordinate
role alpha. Its original beta-coordinate runs between the two opposite
coordinate faces. Reverse that coordinate if necessary, so the entry
face is at raw index z_0 and the exit face at z_m>z_0.

List every raw beta index in [z_0,z_m] whose original physical value
is good. Let them be z_0<z_1<...<z_m, relabeling the final subscript
if necessary. Take their first-hit ranks along the traversal of Q.
These ranks are ordered: consecutive Hilbert cells change a coordinate
by at most one, so the traversal cannot first hit a higher level without
first hitting every intermediate level. Append the final rank of Q
if the exit face was first hit earlier. That last interval is a return.

On each consecutive pair of these good anchor ranks apply Section 1 to
the original beta function. Offer the good common alpha value everywhere
in Q. At every rank choose one available singleton. All original genuine
labels of Q were already relocated, so no additional label is lost.

Apply the construction independently on the disjoint selected caps.
For either parity, the common-role caps are return intervals and the
opposite-role subdivisions use original good endpoints. The same
global 2C comparison applies across every interval. Every rank remains
occupied, and every selected row is good.

## 3. Squared bad-run energy controls the barriers

Let D bound the physical difference at adjacent raw indices of either
V-map, and enlarge C if needed so C>=D. If consecutive good raw indices
are adjacent, their endpoint-row gap is at most D and (2) gives no
forced barrier.

Otherwise they enclose one maximal bad raw run of length g>=1. Their
physical endpoint difference is at most D(g+1), so their barrier has
length at most

`D^2(g+1)^2/(4C^2) <= (D^2/C^2) g^2`.                (4)

Thus for one cap

`W_Q <= C' sum_(bad runs inside its beta interval) g^2`. (5)

The maximum individual barrier is at most C'(G+1)^2 when G bounds the
largest bad raw run. This is a statement about bad runs in the actual
sampled coordinate lists, not merely their physical row-set cardinality.

There is also a global deterministic bound. Fix one maximal bad raw
run of length g. A boundary-clean coordinate interval containing part
of that run must contain the entire run. At dyadic side a>g, at most
one aligned interval in that coordinate contains it, and it participates
in at most N/a Hilbert nodes through the other coordinate. Therefore
its contribution to (5), even summed over ALL potential cap scales, is
at most

`C N g^2 sum_(a dyadic, a>g) 1/a <= C' N g`.          (6)

Sum over both roles. Since the total number of bad raw indices is at
most 2b per role, all selected caps together satisfy

`sum_Q W_Q <= C N b`.                                (7)

This bound includes the actual cap multiplicity. It does not assume
that a projected coordinate represents only one raw row.

For a P subsystem whose every slot gap is at least q_*, a condition
`G^2=o(q_*)` prevents any ONE barrier from meeting every residue of a
P gap, so it removes the specific single-barrier propagation mechanism
in [the two-corner obstruction](continuation_movable_cap_p_propagation.md).
It does not exclude propagation through several barriers, or supply
a lower bound q_* for every cap-stub P edge.

## 4. An exact sufficient weighted reachability test

Fix the sampled row functions and the good anchor lists. Before choosing
the independent bridge positions, compile the directed P graph on the
singleton ranks. Include an edge r->s whenever an odd option at r and
an even option at s from the entire menu form a forbidden P pair.
This union graph can overcount options that do not occur simultaneously.
That is harmless for a sufficient condition.

Fixed genuine doubles contribute permanent forces: every out-neighbor
of their odd point is forced odd, and every in-neighbor of their even
point is forced even. Denote these deterministic force sets by F_O and
F_E. Include any externally prescribed singleton or endpoint-guard
parities in the corresponding permanent force set. Also include every
rank whose menu offers only one parity independently of the bridge
positions, such as a retained fixed filling in a hybrid cap. Assume that the
compiled P family contains no forbidden pair
between two fixed genuine doubles.

For a rank that can lie in an odd-common cap's beta barrier, let pi_O(r)
be the bound (3) for that interval. Set pi_O(r)=1 on F_O, and zero at
other ranks that cannot be intrinsically odd-forced. Define pi_E
symmetrically. If a permanent force is present, its value one takes
precedence over a smaller barrier probability.

Odd and even intrinsic barriers belong to different cap-role families;
their independent position choices are therefore independent. For every
ordered rank pair (r,s), the probability that r is odd-forced and s is
even-forced is at most pi_O(r) pi_E(s). Permanent forces fit the same
statement.

Consequently the condition

`sum_(r reaches s in the compiled graph) pi_O(r) pi_E(s) <1` (8)

guarantees some bridge choices with no directed path from an odd-forced
rank to an even-forced rank. Reachability includes paths of length zero.
To prove this, count such forced ordered pairs and take expectation.

For those bridge choices, assign odd to every singleton rank reachable
from the actual odd forces, and even to every other rank. No even force
lies in the odd closure. Every chosen parity is available, all permanent
double-induced forces are met, and no compiled P implication is violated.
This constructs a P-valid singleton assignment under (8).

The argument uses full reachability, not only paths up to a fixed or
slowly growing length. It does not claim that (8) follows from the
current dirty-path incidence bounds. Other geometric support families
also remain to be checked.

## 5. Arithmetic provenance remains separate

The first-hit anchor ranks depend on the sampled good index set. A fixed
rank can have many potential copied anchors as that set varies. The
logarithmic deterministic ancestor menu of the two-corner construction
is therefore not automatically retained.

If bad raw runs have length at most G, each copied opposite coordinate
lies within G+1 of the deterministic running coordinate record of Q
at that rank. This gives an O(G) candidate menu per cap depth. It is
subpolynomial only if G=h^o(1); a weaker gap bound must pay its explicit
menu factor in any probability estimate.

Thus (5)–(8) are geometric and conditional combinatorial results. A
numerical bound on the actual R2s good-row gaps or the weighted graph,
plus compatible treatment of the enlarged support union, is still
required for a construction theorem. The first-hit construction uses
the literal coarse Hilbert traversal before arbitrary local object
permutations; a subsequent permutation needs its stated locality and
provenance check.

Independent review: the complete saved statement passed two separate
written reviews. These checked the all-span rounding, ordered first
hits, global squared-run charging, independent opposite-role barriers,
permanent forces, full reachability criterion, and the enlarged
provenance menu. The arithmetic and repair limitations remain as stated.
