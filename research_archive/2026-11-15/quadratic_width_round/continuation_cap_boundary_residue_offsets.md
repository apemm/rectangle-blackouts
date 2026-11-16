# Offset residues bound every cap by the bad-row count

15 November 2026. The independent-arm cap construction admits a stronger
size bound than the node-by-node union estimate. The common endpoint of
a large Hilbert square lies on a coarse coordinate boundary. Those
boundaries can all be made good by excluding a small set of offset
residues. This keeps a fixed positive proportion of the original offset
choices and preserves every previously proved upper probability bound.

## 1. The boundary-coordinate set

Use an aligned Hilbert square of dyadic side N. A dyadic node of side
a has coordinate ranges [u,u+a-1] and [v,v+a-1], with u and v divisible
by a. Its two endpoint corners share one coordinate. That common
coordinate is one of u,u+a-1,v,v+a-1.

Fix a dyadic L dividing N. For every node of side at least L, its common
coordinate belongs to

`G_L={mL,mL-1} intersect [0,N-1]`.                    (1)

This statement is unchanged by the swaps and reflections in the Hilbert
recursion. There are at most 2N/L+1 distinct values in (1) per coordinate
role. Counting the nodes themselves loses their repeated use of these
values.

## 2. Remove the bad offset residues

Condition on one parity's two arm fields and its good physical anchor.
Write its unshifted total row map as F(z), so the raw coordinate k has
physical value F(k-U). Its forbidden physical row set has size at most b.
The common anchor is good. Each other value has at most one preimage on
each arm. Consequently

`Z={z: F(z) is forbidden}` has `|Z|<=2b`.             (2)

The same conclusion holds for the mechanical and multiscale arm models,
including the fixed base and anchor insertions. Bad-row enlargement for
the fixed interpolation and permutation constants is included in b.

Exclude the following residues for U modulo L:

`R={-z,-z-1 mod L: z in Z}`.                         (3)

There are at most 4b such residues. If U avoids R and c belongs to G_L,
then c-U cannot belong to Z. Thus EVERY cap node of side at least L has
a good original common endpoint value.

Choose L to be the least dyadic integer at least `16 max(1,b)`. For the
construction b=o(h), N=Theta(h), and the original offset interval I has
length Theta(h). Thus L=o(|I|) and L divides N for all sufficiently large
h. At most

`|R| (|I|/L+1) <= |I|/4+4b`

offsets in I are excluded. At least |I|/2 remain for all sufficiently
large h. Sample U uniformly from those remaining offsets. The choice is
made separately for each parity, conditional on that parity's own arm
fields and anchor.

This is a finite deterministic restriction, not a search for favorable
cap configurations. It can be implemented by listing Z, forming (3),
and enumerating the allowed offsets in I.

## 3. Cap selection and its area budget

Use the all-bad-node rule from
[the good-cap menu](continuation_boundary_preference_and_good_cap_menu.md):
cover every bad-cap node and every doubly-bad leaf by its first good
ancestor, then keep maximal chosen nodes.

Every selected node has side at most L. Indeed a node of side L is
already good, so a bad descendant never needs an ancestor larger than L.
There are no bad nodes of side at least L to generate larger choices.
The selected caps remain disjoint, preserve the endpoint comparison, and
retain the two complete-menu properties in the cited note.

Their expected total area remains

`O(h b log(2h))`.                                    (4)

To see this without a new dependence argument, compare probability laws.
Conditional on all fields and anchors, the new one-parity offset law
has density at most two relative to the old uniform law on I. With two
independent parity families, the joint density is at most four. Apply
this bound to the original nonnegative bad-node area sum, including the
bad leaves. This proves (4).

In particular, for `b=h^(5/6+o(1))`, every selected cap now has side

`L_*=h^(5/6+o(1))`,                                  (5)

with certainty under the restricted offset law. The earlier cutoff
`h^(11/12+epsilon)` and its separate large-cap failure event are not
needed for this cap construction.

## 4. Probability estimates survive the restriction

For every nonnegative random variable X depending on the entire core,

`E_new X <=4 E_old X`.                               (6)

This follows from the pointwise conditional density bound, even though
the allowed offset residues depend on the arm fields. It also holds
after fixing either parity's full parameter family: the other parity's
density bound is still at most two.

Therefore the prescribed-row sampling bounds, the random-anchor
estimates, the physical-divisor candidate counts, and the full compiled
support incidence bounds remain valid up to a fixed factor. One need
not claim that an offset remains independent of its own arm fields.
Independence between the two complete parity parameter families is
preserved, since their restrictions are separate.

The same argument applies to a fixed number of profile cores. Constants
can depend on that number. It does not automatically apply to a number
of cores growing with h.

## 5. Scope

This is a size and sampling improvement for the existing cap scaffold.
It does not select singleton parities to avoid every residual support,
or prove that additional opposite-role cap promotions have small total
area. Promotions can use ancestors much larger than L, even though the
initial selected caps are all small. Any later cap replacement must also
control the new supports it introduces.

The argument is made before arbitrary object permutations. Those
permutations retain the existing fixed locality bounds, but a later cap
repair still needs its own endpoint or enlarged-candidate verification.

Independent review: the complete written argument passed two independent
reviews. They checked the grids across all depths, signed V-map
preimages, excluded residues, the surviving offset proportion, and the
conditional density comparison. No own-field independence is asserted.
