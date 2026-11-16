# Opposite-role cap cost is a same-coordinate boundary condition

15 November 2026. The literal Hilbert child maps identify the expensive
opposite-role cap positions. They lie on boundary strips in the SAME
coordinate as the currently selected point. They do not thin the other
coordinate's multiplicity along each row. This corrects the proposed
other-coordinate repair argument.

The elementary weighted divisor count below reaches only `h^(2+o(1))`
for raw common-arm six supports. It supplies neither a strict power
saving nor a compatible sequence of cap repairs.

## 1. Exact high-cost set inside one Hilbert square

A nontrivial aligned Hilbert square has two endpoint corners. Their
common coordinate is its cap role. Fix a selected coordinate role alpha,
and seek a cap of the other role beta. Ignore bad-row restrictions for
this geometric statement.

Let Q have dyadic side L>=2 and cap role alpha. In its local standard
orientation, the endpoints have a common Y coordinate at the lower face.
Children 0 and 3 swap the coordinate roles. Children 1 and 2 retain them.

A leaf has no beta-cap ancestor of side between 2 and L if and only if
every child digit down to its side-two ancestor is 1 or 2. Its final leaf
digit is unrestricted. Thus the set is EXACTLY the two rows next to
the face opposite Q's common endpoint coordinate. It contains 2L leaves.

Conjugating by Q's orientation proves the general version: it is a strip
of width two in coordinate alpha, not coordinate beta. If Q itself has
cap role beta, the high-cost set in Q is empty.

For the whole N-square at scale L, every high-cost leaf consequently has
its alpha coordinate in

`B_L={x: x mod L is 0,1,L-2, or L-1}`.                (1)

The exact orientation may discard some listed values. In particular,
`|B_L|<=4N/L`. A fixed permitted coordinate value can still have Theta(N)
rank visits. There is no justified replacement of that multiplicity by
N/L.

This statement considers nontrivial square caps. A leaf with a good
opposite option can already switch at zero cap-area cost. Bad-row
requirements can only increase the cost of finding a usable cap.

## 2. Nearby raw partners can share the boundary condition

Consider raw same-parity parked-six supports on one common injective
mechanical arm. The two partners have coordinate difference at most
`W=C sqrt(K)`, by physical hub locality. If both require geometric
opposite-role caps larger than side L, their coordinates lie in B_L.

For `L>4W+C`, the intersection of B_L with a W-neighborhood of any one
of its points contains only O(1) values. Both partners can lie at the
same boundary, so their two conditions are correlated. The number of
ordered partner ranks is at most

`C N^2 (N/L)=C N^3/L`.                              (2)

Their raw coordinate difference is then bounded by an absolute constant.
The corresponding physical difference v is also bounded, because arm
gaps are bounded. This improves the O(sqrt(K)) enumeration of v at
these scales, but does not produce an L^(-2) partner count.

The missing additional restriction is the boundary condition on a hub
whose rank is fixed by the physical-divisor equation. It must not be
treated as independent of the partner positions.

## 3. What the existing physical-divisor estimate proves

Let D_h be the maximal divisor count for integers of size O(K^2 h^2).
For fixed offsets, (2), the divisor enumeration, and the O(1) values of
v give at most `C h^3 D_h/L` positional candidates. The two prescribed
nonconstant rows have probability `CK/h^2`. Including O(K^2) offset
pairs therefore gives

`E N_(all four geometric costs > L^2)
 <= C h K^3 D_h/L`, for `L>C sqrt(K)`.               (3)

Only the necessary restrictions on the two partners were used, so (3)
is also valid when the hubs are required to have high cost. It does not
exploit that extra requirement.

Let C_min be the smallest geometric opposite-role cap area among the
four core points, capped at N^2 if a role is absent all the way to the
root. Dyadic layer summation with (3), and the original raw count at
smaller scales, gives only

`E sum_supports C_min
 <= C h^2 K^3 D_h + C h K^5 D_h
 =h^(2+o(1))`                                      (4)

for polylogarithmic K. The artificial cap at N^2 must not be read as
the existence of an opposite-role cap. In the raw V-map long-support
setting, a partner on the root's far boundary is on its fixed anchor
plateau and cannot be a long partner; this can eliminate the absent-role
case, but does not improve the exponent in (4).

## 4. The remaining repair requirements

A stronger budget needs a joint estimate using the hub boundary after
the divisor relation fixes its rank, or a different repair operation.
The same-coordinate boundary condition alone gives only one factor L^(-1).

This analysis also ignores whether the candidate cap row is good.
Even a favorable weighted area estimate would not by itself prove that
overlapping parity-cap changes can be chosen compatibly, or that the
changes avoid all supports in the compiled virtual-option union.

The estimate is restricted to raw common-arm partners. Selected-cap
coordinate plateaus and arbitrary unequal branches require their own
weighted count. No occupancy-preserving repair theorem is claimed.

Independent review: pending.
