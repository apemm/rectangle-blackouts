# Bidirectional P for rank-dependent cap projection pairs

15 November 2026. The genuine-source bidirectional-P estimate does not
require a target's two projected coordinates to form one cap corner.
A target-first packing argument permits any deterministic coordinate
pair attached to that target rank, with an explicit menu-size factor.

This extends the two-corner estimate to the multi-anchor face menu.
It does not solve the remaining parity-choice or support-repair problem.

## 1. Hypotheses

Let the raw Hilbert grid have side N=Theta(h). At most a fixed number
of genuine source candidates correspond to each raw cell. Every retained
genuine source lies outside every selected cap containing the target
object.

For each potential aligned cap Q and target rank s in its interval,
supply a deterministic menu of at most J(h) pairs

    c_(Q,s,j)=(c0,c1),    1<=j<=J(h).                      (1)

The pair may depend on Q, s, and j. Its two coordinates may come from
different ancestor faces. The menu must be specified before row sampling
and independently of the genuine source rank. Enumerated arm branches
and bounded physical row errors can be included in its fixed factors.

Assume the existing multiscale or independent-arm two-row kernel,
uniformly in fixed target values and conditional on the sampled anchors.
Assume genuine source coordinates are nonanchor forms. The original
bounded-density offset restriction is permitted.

Actual in-strip P limits the source/target rank separation to Ch.
For a fixed bounded fine expansion, use the coarse origins and enlarge
C by a fixed factor. Near the cap ends an O(1) ambiguity in those origins
can be included in the exterior source window. No arbitrary growing
rank displacement is included here.

## 2. Probability for one projected pair

For a fixed source r, target s, and menu pair c, enumerate the signed
norm heights in

    b_s-a_r=Y1,    b_r-a_s=Y2.                             (2)

Their number is h^o(1), uniformly in the rank pair, by the existing
integer norm factorization bound.

If both target forms are nonconstant, condition first on one parity's
full parameters. The other parity has two prescribed row targets, at
its genuine source index and its specified target index. Interchanging
the conditioning parities and taking the smaller of the two bounds
gives

    Pr((2)) <= h^o(1) /
       [h(1+||z_r-c||_infinity)],                         (3)

where z_r is the source raw cell. The two conditional estimates are
not multiplied. Formula (3) is uniform in the pair c, including repeated
coordinate indices.

If at least one target form is a fixed sampled anchor, condition on all
anchors. Its equation prescribes the opposite genuine source row and
costs O(1/h). After fixing that parity's full parameters, the second
equation prescribes the other genuine source row and costs O(1/h).
Thus anchor-containing target pairs have probability O(h^-2).

These are exactly the probability arguments in
[the corner-menu proof](continuation_corner_menu_bidirectional_p.md).
They did not use a corner relation between c0 and c1.

## 3. Sum sources separately for each target

For any m distinct integer grid cells A and any fixed grid point c,

    sum_(z in A) 1/(1+||z-c||_infinity) <= C sqrt(m).        (4)

The estimate is uniform in c. At most O(R^2) cells lie in a square
of radius R around c, so ordering distances or summing shells proves it.

Fix a potential side-a cap Q and one target s. The possible genuine
source ranks outside Q with |r-s|<=Ch form a set of O(h) ranks.
Their raw cells are distinct, apart from the permitted bounded
multiplicity. For EACH menu pair c_(Q,s,j), (4) therefore gives

    sum_r 1/(1+||z_r-c_(Q,s,j)||_infinity) <= C sqrt(h).    (5)

Now sum over target ranks. If s has any exterior source within distance
Ch, it lies within Ch of one of the two ends of Q's rank interval.
Thus there are only O(min(a^2,h)) such targets. Combining with (5),

    sum_(s in Q, r outside Q, |r-s|<=Ch)
       1/(1+||z_r-c_(Q,s,j)||_infinity)
       <= C min(a^2,h) sqrt(h),                          (6)

for any one deterministic choice of pair at each s. Summing menus
multiplies (6) by J(h).

This is the change in summation order. The projected pair may vary
arbitrarily with s. It need not be a single fixed corner for all target
ranks, nor even lie inside Q. It must not be selected as a function of
r without being counted in the per-target menu.

## 4. Sum potential caps before selection

There are N^2/a^2 potential side-a caps. Divide (6) by h using (3).
At one depth, the expected nonanchor bidirectional-P count is at most

    J(h) h^o(1) (N^2/a^2) min(a^2,h) sqrt(h)/h
       <= J(h) h^(3/2+o(1)).                             (7)

The logarithmic number of cap depths is absorbed by h^o(1).
The total rank/form list for anchor-containing targets has size at most
J(h) h^(3+o(1)), and its O(h^-2) probability adds only
J(h) h^(1+o(1)).

Cap selection and its field dependence have been discarded only after
enumerating the deterministic menus. Keeping the necessary condition
that a retained genuine source lies outside its target's selected cap
is legitimate. No independence after cap selection is asserted.

## 5. Apply to the multi-anchor menu

The prefix-face lemma gives O((G+1)log h) deterministic coordinate
forms at each target. Enumerating the two coordinates separately gives
at most O((G+1)^2 log^2 h) pair forms, with the cap Q and its possible
trigger witnesses counted separately when needed.

Hence G=h^o(1) retains the h^(3/2+o(1)) genuine-source
bidirectional-P estimate for the coarse multi-anchor menu. The same is
true under a fixed fine expansion whose cap-contained target origins
have the stated deterministic finite menus.

This is a counting theorem, not a proof that bidirectional constraints
can be repaired while retaining occupancy. It also does not count
all one-way forced paths or general higher-arity supports. Those
remain separate from the projection-pair extension.

Independent review: the complete saved statement passed two independent
written reviews. These checked the minimum of conditional kernels,
sequential anchor bounds, target-first grid packing, target boundary
count, source-independent menus, and fixed fine-origin qualifications.

