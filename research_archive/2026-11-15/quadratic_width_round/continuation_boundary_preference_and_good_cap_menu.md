# Boundary preference and a complete good-cap menu

15 November 2026. Two modifications make the repair problem more precise.
First, the original cap budget can cover every bad-cap node, leaving all
geometric cap ancestors outside the selected regions usable. Second,
boundary preference fills every slot without trying to force an opposite
cap at a stubborn intersection.

These statements concern the coarse Hilbert core and its two total
virtual coordinate functions. A cap repair changes those functions;
arbitrary later permutations require a separate endpoint check.

## 1. Restricted-role repair can still force the root

Use the globally coordinate-swapped standard Hilbert square of side
N=2n. Its root has common first coordinate X. For every 1<=k<n, the
cell `(k,n-1)` lies in the first child, whose common-coordinate role is
Y. Every subsequent nontrivial proper ancestor of that cell also has
role Y: its descent uses only middle children, which preserve orientation.

Suppose X=k is the single bad opposite coordinate and the Y option at
the cell is good. The row n-1 lies in the coarse boundary set B_L for
EVERY dyadic L<=n. Removing its Y point and insisting on an X cap forces
the root. The root is good in the padded construction, but its area and
genuine-label loss are Theta(N^2).

This is a positive-probability offset obstruction. For example, put
N=8m and use offsets U_X in `[2m,5m]`. A fixed interior bad genuine
index j<m has k=U_X+j<4m=N/2 on a fixed positive fraction of offsets.
The root X value is the good anchor. With no Y bad rows, the Y option is
good. Thus even one bad opposite row defeats a subquadratic expected
budget for this restricted-role rule at boundary intersections.

The obstruction concerns this rule, not every possible repair.

## 2. Cover all bad-cap nodes at the original area cost

Declare every nontrivial dyadic node bad-cap when its original common
endpoint value is a forbidden physical row. Also retain the original
doubly-bad-leaf coverage requirement. The root is good-cap.

For EVERY bad-cap node, take its first good ancestor. Add the ancestors
chosen for doubly-bad leaves, then retain the inclusion-maximal chosen
nodes. They are disjoint. Every selected node P has a bad child, so

`sum_selected |P| <= 4 sum_bad_nodes |Q|`.             (1)

Here the bad-node sum includes doubly-bad leaves, each with area one.
This covers selected side-two nodes whose bad child is a leaf. Their
expected contribution is at most O(b^2), hence fits the bound below.

For the independent-arm core each potential node is bad for probability
O(b/h), conditional on the field and anchor choices used in the original
offset calculation. Summing area over depths gives

`E sum_selected |P| <= C h b log(2h)`.                (2)

Thus this stronger selection has the same relocation exponent as the
original construction. It supplies two deterministic properties:

* Every nontrivial cap ancestor of an uncovered rank is good.
* Every strict ancestor of a maximal selected cap is good.

For the second assertion, a bad ancestor would itself generate a larger
chosen good ancestor, contradicting maximality.

These are usable endpoint statements for the TOTAL virtual functions.
Fix a dyadic node R of role beta. An existing beta-cap either contains
R, lies inside R, or is disjoint. In the first case the beta function is
constant on R. In the second, any smaller cap containing an endpoint of
R preserves the original value there, because that endpoint is also an
endpoint of the smaller node. Laminarity excludes partial overlap.
Therefore the two beta endpoint values of R still agree. If R was
originally good, its common value remains good.

The first property resolves the good-row issue for geometric cap choices
outside selected caps. Inside a selected cap, an opposite-role descendant
can still be bad. Taking the first opposite-role ancestor ABOVE that cap
avoids bad values, but its area can be large. Section 1 remains relevant.

## 3. A full boundary-preference filling without new caps

Fix a dyadic boundary scale L, and write

`B_L={j: j mod L is 0,1,L-2,L-1}`.                   (3)

Its size is at most 4N/L. These are RAW coordinate indices. They are not
the projected current cap values.

At a rank, call a good virtual option nonboundary when its raw Hilbert
coordinate is outside B_L. If there is a nonboundary good option, choose
one. Retain a genuine double only when both raw coordinates are outside
B_L and both genuine points were already retainable. If there is no
nonboundary good option, choose any good option. At the designated
constant-anchor endpoint guards retain the prescribed even anchor.

Every rank is occupied, every selected row is good, and no virtual
coordinate function changes. Thus all same-parity locality inequalities
remain valid. Only genuine labels meeting one of the raw boundary strips
are newly converted to singletons. Their number is at most

`C N^2/L`.                                           (4)

The fixed endpoint guards contain only anchor points; long parked
triangles cannot use them as partners.

Let alpha be a selected nonanchor option whose raw alpha coordinate lies
in B_L. Unless the other raw coordinate also lies in B_L, the opposite
virtual option must be bad. A bad opposite virtual value can occur only
where its original opposite raw value is bad, since opposite-role caps
replace values only by good rows.

Conditional on the opposite-parity parameters, let T be the union of
B_L and those bad opposite raw coordinates. The V-map has at most two
preimages of each nonanchor bad row, so

`|T| <= 4N/L+2b`.                                    (5)

Every retained nonanchor high-boundary point therefore lies in the raw
Cartesian set

`B_L(current coordinate) x T(opposite coordinate)`.

In particular its rank set has size

`O(Nb/L+N^2/L^2)`.                                   (6)

This rule keeps the stubborn singletons from Section 1 instead of forcing
large opposite-role caps at them.

## 4. Cap provenance retains the restricted rank mass

Assume every selected cap has side at most L_*<L. For a current-role cap
candidate of side a<=L_*, let M_a(c) count ranks in the Cartesian set
from Section 3 whose candidate current value is the boundary coordinate
c of that node. Raw candidates use a=1.

An aligned side-a interval meets only O(1) raw rows of B_L, since a<L
and the scales are dyadic. For a fixed c, at most two current-coordinate
intervals occur. Summing the opposite-coordinate intersections of their
nodes over the transverse partition counts at most |T| raw values.
Consequently

`M_a(c)<=C|T|`, `sum_c M_a(c)<=C(N/L)|T|`.             (7)

The support remains in two grids of step a. There is NO factor a in
the first bound: the boundary predicate restricts the raw current
coordinate before projection. Testing only `c in B_L` instead would
allow all a raw rows and would not prove (7).

The geometric cap-cost condition also uses raw coordinates. A projected
current point does not invalidate it: the desired opposite-role cap
still has equal TOTAL endpoint values by the laminar argument in
Section 2. Goodness is a separate issue.

## 5. Same-parity long-six supports with two stubborn partners

Use the independent-arm sampling, with K polylogarithmic, and first
condition on the opposite-parity parameters determining T. The current
parity fields and anchor retain their original sampling law.

For same-arm partners, near physical rows imply their candidate indices
are O(sqrt(K))-close. Equation (7) bounds their weighted rank mass by
`(N/L)|T|^2 h^o(1)` after depth summation. For opposite arms, the
reciprocal-distance kernel gives the same bound. Indeed, for a fixed
first index, the second step-a grid contributes at most
`C|T|[1+log(2N)/a]`; the near-distance part costs only a polylogarithmic
factor. All rank multiplicities remain included.

The physical-divisor list fixes the hubs, the increment, and the bounded
hub difference before sampling the current parity. The existing
nonanchor and random-anchor sampling bounds therefore give respectively

`E N_two_stubborn,nonanchor <= h^o(1) |T|^2/(hL)`,

`E N_two_stubborn,anchor <= h^o(1) |T|^2/(LE)`.         (8)

Cap and arm forms are enumerated before conditioning on their selection.
Both partners are nonanchors by the long-increment geometry. The bound
is uniform in the opposite-parity parameters, so it can be averaged.

For example, keep E=h^(23/24), L_*=h^(15/16), and take dyadic
`L=h^(91/96)` up to a bounded factor. With b=h^(5/6+o(1)), the two
bounds in (8) are at most

`h^(-9/32+o(1))` and `h^(-23/96+o(1))`.               (9)

Thus with probability tending to one there is no same-parity long-six
support whose two partners are both stubborn. Combine this event with
the existing small-cap and cost objectives by joint selection.

Every remaining same-parity long-six support has a partner outside its
raw current boundary set. It therefore has an opposite-role GEOMETRIC
cap of side at most L. If the partner is outside the selected cap union,
Section 2 makes this a good cap. A partner inside a selected cap can
still have a bad opposite-role descendant, so that case remains open.

## 6. Regeneration and the remaining repair problem

Boundary preference chooses only points from the fixed total virtual
option union. It creates no support outside the corresponding compiled
union. It can nevertheless make a previously unselected support actual.
Equation (8) is applied to that full union and the stated pruning rule,
not only to a prior default filling.

An additional cap changes an entire option function. Its new supports
must be included in an enlarged compiled union, and overlapping caps
can undo earlier parity erasures. Neither (1) nor (8) proves a compatible
selection of such repairs. The lemmas establish occupancy, quantitative
exception sets, and a restricted-support absence statement; they do not
prove complete residual avoidance or a quadratic construction.

Independent review: Sections 3–5 passed a separate written review of
the conditioning, raw-coordinate mass bound, reciprocal-distance sums,
and both exponents. The all-bad-node covering argument also passed an
independent conceptual review; the bad-leaf term in (1) is explicit.
