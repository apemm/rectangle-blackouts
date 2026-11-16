# Random near-edge anchors control long six-point hubs

15 November 2026. A random near-edge anchor supplies an additional atom
bound for long same-parity parked-six supports containing an anchor.
The expected count is `h^(95/48+o(1))` under the stated nonconstant
partner sampling estimate. This includes unequal cap depths.
It does not provide an occupancy-preserving repair of every support.

## 1. Anchor location and sampling

Fix a low constant sea row `s=O(1)`, with all core rows above s.
Sample the parity's good anchor A independently of its mechanical
parameters and coordinate offset, from `[h-E,h-2]`, where

`E=h^(23/24)`, `sup_a Pr(A=a) <= h^o(1)/E`.             (1)

[The anchor-pool lemma](continuation_random_top_anchor_pools.md) supplies
this estimate, including the prime-gap even anchor. Conditional insertion
of A preserves the uniform row-sampling bounds.

For a support of span greater than `h^2/K`, with K polylogarithmic, the
local-anchor reduction gives sea offsets xi_1,xi_2 and hub gap t with

`|xi_i|,|t|<=CK`, `xi_1-xi_2=St`, `t!=0`,

`delta>=ch/K`, `|v|<=C sqrt(K)`.                       (2)

The partners have rows y,y+v and hubs y+delta,y+v+delta. Positivity of
delta follows because the white completion has row s+delta. A negative
delta has bounded magnitude and cannot satisfy the long-increment bound.

No anchor can be a partner: its in-strip hub would give
`delta<=h-A<=E=o(h/K)`. Exchange the triangles so the first hub is the
anchor. Both partners then have nonconstant candidate formulas.

Assume the following uniform conditional estimate for two deterministic
nonconstant indices c_1,c_2 and prescribed physical values:

`Pr(two prescribed rows | A)
 <= h^o(1)/[h(1+|c_1-c_2|)]`.                         (3)

[The triangle sampling lemma](continuation_mechanical_triangle_sampling.md)
proves (3) for the common stretch and all nonconstant fold branches.
The independent-arm V-map has its own proof in its assembly note.
Cap boundary indices are allowed: their selection conditions are discarded
after the fixed candidates have been enumerated, not conditioned upon.

## 2. Cap-row energy with multiplicity

At dyadic side L, let M_L(c) count every rank in each possible cap node
at its specified boundary coordinate c. Count both boundary choices.
For N=Theta(h),

`M_L(c)<=CNL`, `sum_c M_L(c)<=CN^2`.                    (4)

Its support lies in two grids of step L. Raw points are included at L=1.
For fixed c_1, the reciprocal sum on either step-L_2 grid is bounded by
`C[1+log(2N)/L_2]`. Using (4) and then interchanging the two depths gives

`sum_(c_1,c_2) M_(L_1)(c_1) M_(L_2)(c_2)/(1+|c_1-c_2|)
 <= CN^3[min(L_1,L_2)+log(2N)]`.                       (5)

All rank multiplicities inside a cap remain in (5). Summing over dyadic
depths at most L_* gives

`total weighted partner mass <= CN^3[L_*+log^3(2N)]`,   (6)

because the dyadic double sum of min(L_1,L_2) is O(L_*).

## 3. Divisibility fixes the physical anchor

Fix partner ranks p_1,p_2, their boundary-coordinate candidates, and the
sea offsets. Put Delta=p_1-p_2+t. The exact physical identities are

`S^2 t(r-p_1)=S xi_2 Delta-delta v`,

`delta | S xi_1 xi_2 Delta`.                           (7)

Long span and hub locality exclude Delta=0, by
[the partner-divisor argument](continuation_stretched_partner_divisor_count.md).
Enumerate every signed divisor delta and the O(sqrt(K)) possible integer
values of v. They determine the first hub rank:

`r=p_1+[S xi_2 Delta-delta v]/(S^2 t)`.                (8)

Reject noninteger and out-of-range ranks. Its anchor row is then fixed
before sampling any random parameter:

`A=s+delta+S xi_1(r-p_1)/delta`.                       (9)

The partners must have rows A-delta and A+v-delta. Condition on the
anchor value in (9), then apply (3). The candidate probability is at most

`h^o(1)/[h E(1+|c_1-c_2|)]`.                          (10)

This is a justified conditional product. The anchor may change the
inserted lists, but (3) is uniform in that anchor. Neither its index nor
cap selection is assumed independent of the equations.

The divisor arguments have size O(K^2 h^2). Their divisor counts, the
O(K^2) offset choices, and the O(sqrt(K)) values of v are h^o(1).
Summing (10) with (6) proves

`E N_anchor <= h^(2+o(1)) L_*/E`.                      (11)

There is no first-hub ancestor factor: its actual constant value is fixed
directly by (9). Dropping its selection condition enlarges the count.

## 4. Subquadratic bound and scope

Choose `L_*=h^(15/16)` up to a dyadic factor. With
`b=h^(5/6+o(1))` bad rows, the bad-child cap bound gives

`Pr(some selected cap has side>L_*)
 <= Chb/L_*^2 = h^(-1/24+o(1))`.                      (12)

Equation (11) gives

`E N_anchor <= h^(2+15/16-23/24+o(1))
             = h^(95/48+o(1)) = o(h^2)`.               (13)

Both bounds are unconditional. Joint parameter selection can exclude
large caps and retain this incidence bound alongside other nonnegative
budget estimates. No triangle probability is conditioned on excluding
large caps. Bounded finite interpolation unions change only the stated
subpolynomial factors when their row-form representation is verified.

Reflection gives the high-sea result with anchors near the lower edge.
Nonconstant unequal-branch supports still need their own positional
count. Incidence control and an admissible full-board repair remain
separate obligations.

Independent review: the full proof passed a separate written review.
The review checked the retained cap rank multiplicities, deterministic
physical-anchor value, conditioning before the uniform partner estimate,
large-cap exception, and the exponent 95/48. Bounded anchor and row
perturbations are included only through the stated fixed finite unions.
