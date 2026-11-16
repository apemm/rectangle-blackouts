# A local reachability criterion for independent cap barriers

15 November 2026. The multi-anchor menu has an exact sufficient test
based on the global sum of weighted forced endpoint pairs. A local
version suffices when independent barrier variables have small incident
loads. The proof uses the full compiled reachability relation and the
elementary asymmetric local lemma.

This gives a conditional P-choice theorem. No local-load bound for the
current sampled scaffold, or control of the other support families,
is asserted.

## 1. Fixed menu and independent variables

Use the setting of
[the multi-anchor menu](continuation_multi_anchor_cap_menu.md).
Fix the sampled row functions, all good anchor ranks, and the compiled
P implication graph on singleton ranks. The graph includes every
odd-to-even forbidden pair from the entire menu before the independent
bridge positions are chosen.

There is one independent random variable Z_i for each nonempty movable
barrier. Each rank can be intrinsically forced to one parity by at most
one such variable. Odd and even intrinsic forces belong to different
cap-role families, so opposite-parity intrinsic forces use distinct
variables.

Retain all permanent forces from fixed genuine doubles and guard
conditions. Include every rank whose menu offers only one parity
independently of the bridge positions, including old-fill caps in a
hybrid construction. Assume that there is no forbidden P pair between two fixed
doubles, and no directed path from a permanently odd rank to a
permanently even rank. A path of length zero is included.

Let pi_O(r), pi_E(r) be the pointwise forcing bounds from the
multi-anchor note. Permanent forces have weight one and override any
intrinsic bound. A rank with no possible force of the specified parity
has weight zero.

## 2. Events and local loads

For every ordered pair r,s with r reaching s in the compiled graph,
consider the event

    E_(r,s) = {r is odd-forced and s is even-forced}.

Discard pairs with zero weight and the already excluded deterministic
permanent-to-permanent events. Each remaining event depends on one or
two independent barrier variables, and

    Pr(E_(r,s)) <= w_(r,s) := pi_O(r) pi_E(s).             (1)

For a variable Z_i, define its incident load by

    L_i = sum w_(r,s),                                    (2)

where the sum includes every event whose actual forcing test depends
on Z_i. A permanent force contributes no variable at that endpoint.
In particular, an event with one permanent endpoint is unary.

If

    max_i L_i <= 1/8,                                    (3)

then there is a simultaneous choice of all bridge positions with no
event E_(r,s).

Here is a direct local-lemma verification. Join two events when their
variable sets intersect. An event depends on at most two variables,
so the sum of weights of its neighboring events is at most 2 max L_i.
Set x_E=2w_E. Condition (3) implies x_E<=1/4 and

    product_(F neighbor E) (1-x_F)
       >= 1-sum_(F neighbor E) x_F
       >= 1-4 max L_i
       >= 1/2.

Thus Pr(E)<=x_E product_(F neighbor E)(1-x_F), which is the
asymmetric local-lemma hypothesis. The dependency assertion follows
from independence of disjoint sets of barrier variables. The finite
local lemma therefore gives positive probability that all events
are absent.

The same proof works with any upper bounds w_E for the event
probabilities and the corresponding variable loads. Formula (1)
is a convenient bound supplied by the independent opposite-role
barriers.

## 3. The resulting parity assignment

For a successful choice of the bridge positions, assign odd to every
singleton rank reachable from an actual odd force. Assign even to
every remaining singleton rank.

No actual even force lies in the odd closure, because its existence
would give an event E_(r,s). Thus every selected parity is available.
Permanent forces from genuine doubles and guards are respected.
The forward closure obeys every edge of the compiled P graph, so
the chosen filling is P-valid.

As in the global criterion, the compiled graph may include option
pairs that are never simultaneously offered. This only strengthens
the sufficient condition.

## 4. Why the load condition is different

A disjoint union of many small reachability components may have a
global sum of event weights greater than one while every variable
load remains below 1/8. Condition (3) then still gives a simultaneous
choice. It does not require one shared global probability budget.

This is not a claim that the graph actually decomposes that way.
Every reachable endpoint pair contributes to (2), including paths
of arbitrary length. Fixed-length dirty-path incidence bounds cannot
replace (2) without a separate control of the remaining reachability.

The statement concerns the independent positions of barriers after
the row functions and cap menu have been fixed. It neither asserts
conditional independence of the original sampled fields after cap
selection nor changes the previously stated deterministic provenance
requirements. Higher-arity rectangle supports and external relocation
remain separate obligations.

Independent review: the complete saved theorem passed a separate
written review. The one-/two-variable dependency graph, weight and
neighbor-product constants, permanent forces, and full forward-closure
assignment were checked. The all-length local-load estimate remains
an explicit hypothesis.

