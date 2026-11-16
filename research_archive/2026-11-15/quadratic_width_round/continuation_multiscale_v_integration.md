# Multiscale fields in the independent-arm scaffold

15 November 2026. The independent-arm V scaffold can use a separate
multiscale row field on each arm. Its geometric construction and long-six
counts survive, while the same sampling also gives the reviewed
`h^(3/2+o(1))` bidirectional-P and `h^(7/4+o(1))` genuine central
three-cycle incidence bounds.

The reciprocal-index estimates below replace the former global affine
approximation. A multiscale occurrence list does not satisfy one formula
`p_i=alpha i+O(1)` with a single random alpha.

## 1. Field assignment and coverage

Use the complementary row word from
[the multiscale sampling theorem](continuation_multiscale_row_sampling.md).
On a fixed physical residue-index interval `[0,H)`, its cumulative field
F has derivative between 1/3 and 2/3. The two central classes use F=C
and F=x-C from one field. They partition the retained original rows,
and both occurrence lists have gaps at most three.

For each central class, assign a fresh independent field to its left
arm. The left arm carries no genuine labels. The odd and even parity
field families are independent. Complementary central classes within
one parity remain dependent; no proof multiplies their probabilities.
There are a fixed number of class products, so their counts can be
summed without independence between those products.

Sample the good near-edge anchors independently of all fields. Define
each field on the fixed original pool, before truncating at the sampled
anchor. Insert the common base and anchor when absent. For every
nonconstant occurrence, the uniform inverse-count relation is

`F(y)=i+O(1)`,                                      (1)

where y is its physical residue index. Bounded insertions and bounded
physical row perturbations only change the fixed error in (1).
Injected occurrences are nongenuine in classes where the original row
was absent.

Use the top crop, central continuation, fixed padded sizes, fixed offset
ranges, and independent arms of
[the V-map construction](continuation_independent_arm_v_map.md).
The retained original parity labels are still covered exactly once.
All left-arm and continuation objects are padding.

## 2. A local field variable replaces the global slope

The multiscale field assigns an independent bounded-density variable
to every dyadic interval. Every target interval of length d>=4 contains
one such interval of length at least d/4. Its variable changes the
integral across that interval by a coefficient of magnitude at least

`c d/log^2(2h)`.                                    (2)

Variables inside disjoint target intervals are independent. A prefix
`[0,y]` has the same property with d=y. All target intervals used below
are fixed before the relevant arm field is sampled, after conditioning
on the anchor and any opposite-parity information.

For a central-arm candidate at raw or cap index k, a target physical
residue value y gives

`F_C(y)+U=k+O(1)`.

For a left-arm candidate it gives

`F_L(y)-U=-k+O(1)`.                                 (3)

For any fixed field, either equation allows O(1) integer offsets U.
This fact, not a global affine formula, supplies the offset factor 1/h.

## 3. Two-row and three-row probabilities

For two candidates on the same arm, subtract (3). The target-row
interval has length comparable to the raw index gap if the event is
possible. A local variable from (2) and the bounded offset fiber give

`Pr(two prescribed rows | anchors)
 <= C log^2(2h)/[h(1+|k_1-k_2|)]`.                  (4)

Bounded gaps use the single-offset estimate instead.

For opposite arms, U lies between k_1 and k_2. Split the event according
to which arm distance is at least half their gap. Condition on the other
arm field. Its prescribed target fixes O(1) values of U. For each value,
the long-arm target height above the common base is comparable to its
arm distance. A dyadic variable in that target prefix has coefficient
at least `c|k_1-k_2|/log^2(2h)`. The long-arm field is independent of
the conditioned field. This proves (4) across the arms as well.

No independence of bounded approximation errors is used. Each event is
contained in the specified integral strips; after fixing the field,
the possible offset fibers have uniformly bounded size.

For long parked-six counting, one additionally needs the far-partner
three-row estimate. Suppose a hub and a partner are on one arm, their
prescribed row difference is at least `ch/K`, and the other partner is
on the independent arm at height at least R above the common base.
Choose a local variable in the first target gap. It gives a factor
`O(K log^2 h/h)`. The first-arm field then leaves O(1) offsets U.
Conditional on those values, a prefix variable in the other arm gives
`O(log^2 h/R)`. Therefore

`Pr(the three prescribed rows | anchors)
 <= C K log^4(2h)/(h^2 R)`.                         (5)

The fourth prescribed row can be discarded. In the reciprocal-distance
variant, physical closeness of opposite-arm partners forces both heights
to be at least a fixed multiple of their raw index distance d, except
when `d=O(sqrt(K))`. Use R=cd in (5); at the smaller distances use (4).

The target gaps and prefixes in this proof are fixed by the deterministic
physical-divisor candidate list. They are not selected after observing
the same field. Ancestors and bounded local row forms are enumerated
before imposing cap selection.

## 4. Every long-six bound transfers with logarithmic factors

The physical-divisor identities and partner counts depend on integer
rows, bounded gaps, locality, and fixed candidate indices. These properties
hold unchanged. Equation (4) gives the prescribed long-triangle bound
`K h^(-2+o(1))`. Equation (5) supplies the extra far-arm factor in the
nonanchor count. Random-anchor hubs use (4) conditional on the anchor
value fixed by their divisor list.

Consequently the reviewed incidence bounds remain

| Family | Bound with E=h^(23/24), L_*=h^(15/16) |
| --- | --- |
| Same-parity, no anchor endpoints | h^(31/16+o(1)) |
| Same-parity, anchor hub | h^(95/48+o(1)) |
| Opposite parities, including anchor hubs | h^(13/12+o(1)) |

The opposite-parity proof multiplies only events in independent parity
field families. It does not condition on the selected caps.

Only powers of log h have been added to the sampling estimates. The
retained polynomial K-powers in
[the polynomial-window theorem](continuation_polynomial_long_six_window.md)
are unchanged. Its positive exponent saving for every fixed
`0<kappa<1/42`, at span `h^(2-kappa)`, therefore remains valid after
the same retuning of the anchor window and cap cutoff.

## 5. Geometry, P cleanup, and endpoint compatibility

Conditional on the fields, each strictly increasing arm has at most one
preimage of each nonanchor bad physical row. The V-map has at most two.
The cap-area expectation, large-cap probability, and deterministic
forced-odd count therefore retain their previous orders. Both arms
have uniformly bounded gaps and meet at a common base, so the global
coordinate Lipschitz bound and cap endpoint comparisons also survive.

The top crop, good-anchor pools, enlarged bad-row filters, cleared
fixed-size permutations, sparse interpolation, occupied columns, and
prime-gap guarded collars consequently transfer exactly as deterministic
steps in [the mechanical integration](continuation_mechanical_v_scaffold_integration.md).
All residual systems still include the arithmetic anchor extensions.

The genuine-source small-factor P cleanup uses only the strict occurrence
list and its O(1) offset preimages for a prescribed row. The exceptional
nonconstant odd source uses that same offset count together with the
independent even bad-row restriction. Anchor odd sources use their
near-edge location. None of these arguments requires global affinity.
Thus the forced-odd incidence remains `h^(95/48+o(1))` with the displayed
parameters, and the surviving genuine-source actual P gap remains
`h^(1-o(1))` after the reviewed ordered erasures and relocation input.

## 6. The additional P cycle estimates and their scope

For a bidirectional P template incident to a genuine source, condition
on one parity family and apply (4) to the other parity's two prescribed
rows. Interchanging parities and taking the minimum gives the reciprocal
maximum-coordinate-distance kernel. The reviewed cap-projection sum
then gives `h^(3/2+o(1))` genuine endpoints. If a target coordinate is a
fixed anchor, sequentially specifying the two genuine source rows costs
O(h^(-2)) instead. The one-base-pair representation and source-outside-cap
conditions are retained.

For three genuine central objects, the multiscale theorem uses two
independent dyadic variables in adjacent prescribed target gaps. Its
all-direction three-row estimate and grid count give

`E(number of genuine central P three-cycles) <= h^(7/4+o(1))`.

This statement includes all determinant sizes and all P directions.
It does not include cycles containing arbitrary singleton cap or anchor
objects. Both the two-cycle and three-cycle estimates mark only their
incident genuine endpoints; they do not choose the residual singleton
parities or prove the absence of longer directed paths or cycles.

The four geometric residual systems, safe support repair, and the
external relocation hypotheses remain open obligations. The supplement
does not assert a complete quadratic construction.

Independent review: the complete supplement passed a separate written
review of the inverse-count formulation, same-arm integral strip,
opposite-arm conditioning, independent far-arm prefix variable,
deterministic target selection, long-six kernel transfers, and the
genuine-source, anchor, occupancy, and collar dependencies. No global
affine approximation is used in this alternative sampling model.
