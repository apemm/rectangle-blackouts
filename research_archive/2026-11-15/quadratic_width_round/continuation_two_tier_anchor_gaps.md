# Two-tier good-row gaps and a hybrid cap menu

15 November 2026. A fixed gap moment gives a quantitative budget for
marking rows in long good-anchor gaps. On the remaining gaps, intermediate
anchors give short forced barriers. A hybrid menu uses the original cap
filling on long-gap caps, so this refinement requires no additional cap
cover or relocated labels.

The marking budget is not an occupancy-preserving repair theorem.
The hybrid menu does not show that every marked point can be erased,
and no full P reachability estimate is inferred.

## 1. Keep the moment order fixed

Let an admissible row pool have size O(h). Suppose a deterministic set
of good physical anchors brackets that pool, and its consecutive gap
lengths g satisfy, for one FIXED 1<gamma<3/2,

    sum g^gamma <= C_gamma h (log(2h))^A.                   (1)

Here A and C_gamma are fixed. The good family must obey the required
profile residue, half-strip, and row filters.

The input in
[the semigroup gap note](continuation_full_good_semigroup_gap_bounds.md)
has A=3(gamma-1)/4 before any harmless fixed thinning or dilation.
It applies directly to the specified odd-row family. A separately
prescribed residue of the even-row family still needs its stated
arithmetic input.

For G>=1, let T_G be the union of physical row intervals in anchor
gaps longer than G. The elementary inequality
g<=G^(1-gamma)g^gamma gives

    |T_G| <= C_gamma h G^(1-gamma) (log(2h))^A.             (2)

Endpoint cuts can be bracketed by the neighboring full-family anchors.
Intersecting the gap intervals with the row pool only decreases (2).

At most O(h) complete labels use any one row. Consequently the number
of complete labels incident to T_G is at most

    C_gamma h^2 G^(1-gamma) (log(2h))^A.                   (3)

For G=h^theta with fixed theta>0, this is
h^(2-theta(gamma-1)+o(1)). It is a count of labels that can be marked
for external placement. Erasing their core points may break occupancy,
so (3) does not itself authorize such an erasure.

In particular, fix 0<epsilon<1/2 and put G=h^(1/2-epsilon).
The exact exponent in (3) is

    2-(1/2-epsilon)(gamma-1).                              (4)

If gamma=3/2-eta with fixed 0<eta<1/2, this equals

    7/4+epsilon/2+eta/2-epsilon*eta.                        (5)

The endpoint gamma=3/2 is not an input theorem and is not substituted
into (4).

## 2. Transfer to actual sampled classes is a separate hypothesis

A bounded-gap physical row subsequence can skip all isolated good
anchors. Thus (1) does not automatically bound bad runs in a mechanical
or multiscale class.

A sufficient transfer is that each class contain a specified good
anchor subfamily with the same moment bound. Bounded deterministic
thinning and alternating allocation preserve (1), up to constants:
a new gap is a sum of a bounded number of retained gaps, and convexity
applies. A greedy minimum-spacing thinning also preserves the moment:
each new gap is at most a fixed additive constant plus one original
gap, and those original gaps can be charged injectively.

The balanced-anchor planting construction supplies the class-membership
step when its bounded-prefix and bounded-gap hypotheses have been
verified. This note uses that step only through the preceding explicit
membership condition. The geometric constants and the deterministic
bad-row filter must be fixed for the enlarged adjacent-gap constant.

On a monotone arm, a raw bad run lies between two class anchors.
Its raw length is at most their physical separation, up to a fixed
rescaling. The runs between one pair of anchors are disjoint, so their
gamma-powers sum to at most a constant times that physical gap's
gamma-power. The two arms add only a fixed factor. A run crossing the
common turn is the union of at most two end runs and obeys the same
bound by convexity, provided the endpoint bracketing is included.

This proves the corresponding raw-run moment under the membership
hypothesis. No assumption that an arbitrary sparse physical good set
already lies in every sampled class is used.

## 3. Short gaps remove one specific propagation mechanism

Consider the multi-anchor construction inside a selected boundary-clean
cap, with its common good parity still available everywhere. Suppose
every maximal bad raw run in the opposite coordinate interval has
length at most G. If adjacent physical raw-map increments are bounded
by a fixed D, every individual forced barrier has width

    w <= C_D (G+1)^2.                                      (6)

This is the all-span bridge estimate in
[the multi-anchor menu](continuation_multi_anchor_cap_menu.md).
For G=h^(1/2-epsilon), every barrier has width
O(h^(1-2epsilon)).

For a P subsystem known to have slot gaps q_*=h^(1-o(1)), (6) is
o(q_*). A single barrier therefore cannot meet every residue modulo
any such P gap. This excludes the sufficient single-barrier propagation
criterion from
[the local obstruction](continuation_movable_cap_p_propagation.md).

Several barriers can still propagate together. Also the known
genuine-source long-gap cleanup does not give q_* for every P edge
incident to a cap singleton. Neither issue is removed by (6).

## 4. A hybrid menu needs no new cap cover

Start with the already selected disjoint boundary-clean caps. Fix G.
For each cap Q inspect the bad runs in its opposite-coordinate interval.

* If every such run has length at most G, use its multi-anchor menu.
* Otherwise retain exactly its original compatible one-coordinate
  singleton filling.

Outside these caps retain the original scaffold. The decision is made
from the sampled fields and good-row sets, before any independent
bridge positions are chosen.

Every original genuine label in a selected cap was already relocated.
The hybrid operation adds no relocated label and creates no empty
rank. Every offered row is good. The partial same-parity square-root
Hölder constant is at most the common constant from the multi-anchor
extension, uniformly over which caps use either rule and over all
bridge choices. This follows by treating an original common-coordinate
cap as a return interval and using the same facing-anchor comparison
on the other cap subdivisions.

The caps retained under the old rule are not charged by (3).
A cap containing a long bad run may extend far beyond the rows in that
run. Other bad boundary values can postpone a clean ancestor. Thus a
small physical long-gap set does not, without an additional argument,
bound the area of a new cap cover around that set.

All old-fill exceptional events retain their original dirty-child
witness in the full deterministic Bad set of size b. No smaller
witness set is inferred from the sampled long-run decision.

## 5. Deterministic candidate menus before sampling

For a fixed potential cap Q and rank r, its directed running coordinate
record is determined by the original Hilbert traversal. On a short-run
cap, the two good indices whose first hits bracket r are within G+1
of that record. The appended exit interval is a return and adds only
the exit value.

Consequently each rank has at most O((G+1) log h) deterministic raw
coordinate candidates, including the old cap forms, when all potential
ancestors are enumerated. The enumeration precedes all field sampling,
cap selection, class eligibility, and bridge choices. It is permissible
to discard those conditions only after replacing the actual event by
this full candidate union.

This yields a conditional counting principle. Suppose a fixed-arity
incidence proof is uniform over the resulting deterministic
raw-coordinate forms, including the required locality and mass bounds.
If at most t forms are selected, replacing a logarithmic menu by this
one costs at most O((G+1)^t), in addition to any geometric factor that
the proof explicitly requires.

For example, an independently established bound h^(2-rho+o(1)) with
fixed rho>0 remains subquadratic after this union when G=h^epsilon
and t*epsilon<rho. This example does not certify that every earlier
P or six-support proof is uniform over the enlarged forms. In
particular, a theorem requiring a paired endpoint corner cannot be
applied to unrelated running-record projections without a new check.

The underlying parity fields remain sampled independently before the
bounded-density offset restriction. The hybrid choice does not make
them conditionally independent after its own selection event. Existing
bad-row kernels must therefore use their independent deterministic
candidate and witness menus, not condition on being a short-run cap.

## 6. A subpolynomial threshold can pay a relocation tariff

Keep gamma>1 and A fixed in (1). Suppose the variable part of an
external relocation tariff is n_E T(h)^2, where T(h)>=1 and
T(h)=h^o(1). Choose

    G(h)=ceil([T(h)^2 (log(2h))^(A+2)]^(1/(gamma-1))).     (7)

Then G=h^o(1), and the marked-label count in (3) satisfies

    n_E T(h)^2=O_gamma(h^2/(log(2h))^2).                  (8)

This concerns the variable tariff only. Fixed joining or collar costs
remain as stated in the external relocation theorem, and a safe core
replacement is still required before relocating these labels.

There is also a growing-arity compatibility observation. Put

    X(h)=log h/log(2G(h)),
    k(h)=floor(min{sqrt(log log h), X(h)^(1/3)}).           (9)

For sufficiently large h, k(h) tends to infinity. Moreover
k(h)^2 log(2G)=o(log h). Thus even a menu overhead G^(O(k^2))
is h^o(1). The other explicit overheads in
[the growing dirty-path estimate](continuation_growing_dirty_cap_paths.md),
including D_h^k and the order and strip factors, are also h^o(1)
for this choice.

This is a parameter compatibility statement. It applies only after the
geometric and sampling estimates have been verified uniformly for the
hybrid candidate menu. It does not establish the full reachability
condition or justify removing the long-gap region.

## 7. Remaining repair obligation

The hybrid construction offers additional good parities on a controlled
class of caps. It preserves the original occupied scaffold on the
others. To use it for repair, one must still control the compiled
support union and establish a parity assignment, for example through
the full weighted reachability condition in the multi-anchor note.

Fixed-length or slowly growing dirty-path bounds do not by themselves
establish that condition. The marking estimate (3), the barrier estimate
(6), and the candidate-menu principle address different parts of this
problem and are not combined into a full-board claim here.

Independent review: Sections 1--5 passed a complete separate written
review, including the exact exponents, sampled-class condition, hybrid
occupancy, original dirty witness, and deterministic menu qualifications.
Section 6 also passed two independent algebraic reviews, including the
polylogarithmic tariff, endpoint convention, growing-arity overhead,
and the distinction between counting and safe replacement.

