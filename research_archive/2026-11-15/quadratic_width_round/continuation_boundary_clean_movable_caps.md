# Boundary-clean caps and a movable two-corner menu

15 November 2026. Requiring every boundary row of a selected cap to be
good costs the same expected area as the original cap selection. This
refinement is compatible with the original one-coordinate cap filling.
It also permits a separate movable two-corner menu. The latter preserves
occupancy and locality, but changes the potential support family and
does not automatically inherit every earlier P estimate.

## 1. Boundary-clean selection

Before capping, let f_0 and f_1 be the two total physical row functions
on the Hilbert rank interval. Each is C-Hölder with exponent one half.
For an aligned node Q, let its two coordinate intervals be
`[u,u+a-1]` and `[v,v+a-1]`. Call Q boundary-clean when the four
physical values associated with u,u+a-1,v,v+a-1 are all good.
At a leaf this means that both row options are good.

Declare every other node dirty, including the leaves. The padded root
is boundary-clean. For every dirty node, choose its first boundary-clean
ancestor, then retain the inclusion-maximal chosen nodes. These selected
nodes are disjoint. Each has a dirty child, so

`sum_selected |Q| <= 4 sum_dirty |R|`.                 (1)

The sum includes dirty leaves. A fixed node is dirty with probability
at most Cb/h under the original offset law: there are at most four
boundary values, and each bad physical value has at most two unshifted
V-map preimages. At each depth the node areas sum to N^2=Theta(h^2).
Thus the expected selected area is

`O(h b log(2h))`.                                     (2)

Use the [residue-restricted offset law](continuation_cap_boundary_residue_offsets.md)
with L_0 the least dyadic integer at least 16 max(1,b). Every node of
side at least L_0 is boundary-clean, because all four boundary
coordinates lie on the two L_0-grids. Hence every selected node has
side at most L_0. The density bound of at most four transfers (2) to
this new law.

Every dirty leaf is covered. Outside the selected nodes, both original
row values are therefore good. Every strict ancestor of a selected node
is boundary-clean: a dirty ancestor would generate a larger selected
boundary-clean ancestor.

## 2. The compatible original filling

Initially keep the original filling rule. A selected node Q has one
common-coordinate role alpha. Replace that coordinate throughout Q by
its common endpoint value. Retain the other total coordinate function
there. This changes at most one coordinate at any rank, since the
selected nodes are disjoint.

All the original cap arguments still apply. The common value is good;
both options are good outside the selected nodes; and every rank has a
good option. At each nongenuine rank choose exactly one point, with the
previous even preference when desired. Genuine pairs inside selected
nodes are relocated. Every genuine pair outside them retains its old
rows and rank.

The total coordinate functions remain uniformly Hölder. The number of
intrinsically forced odd ranks under even preference is still bounded
by the original bad-even coordinate lines. The established P counts
using at most one projected coordinate per coarse object remain within
their original scope. Replacing the old cap selection by boundary-clean
selection only changes its area constant and its deterministic
potential ancestor list.

This is the compatible refinement. The following menu is an optional
further change, not an assertion that all those P conclusions transfer.

## 3. A movable opposite-role bridge inside each selected node

Write the rank interval of Q as `[ell,u]`, with T=u-ell=|Q|-1.
Its alpha endpoint values agree. Its other role beta has two good
endpoint values B_ell=f_beta(ell) and B_u=f_beta(u), by boundary
cleanliness. Put g=|B_u-B_ell|. The original Hölder bound gives
`g^2<=C^2 T`.

If g=0, offer the common beta value throughout Q. If g>0 and T>=16,
put

`d=ceil(g^2/(4C^2))`,

and choose an integer p in

`[ell+ceil(T/4), ell+floor(3T/4)-d]`.                  (3)

Offer B_ell on `[ell,p]` and B_u on `[p+d,u]`. Do not offer beta on
the intervening d-1 ranks. Offer the good common alpha value everywhere
in Q. Thus every rank is occupied after choosing one available option.
For T<16 retain the compatible original filling from Section 2.

The set in (3) has at least T/8 integer choices. The unavailable beta
barrier has length strictly less than g^2/(4C^2), and at most T/4.
At least three quarters of a long selected node therefore receive both
parity options. A return node, with g=0, receives both everywhere.

Choose one point at every rank of Q, even when both options are offered.
No new double label is introduced. All genuine pairs of Q were already
relocated, so this menu has no additional label or excess cost.

## 4. Uniform locality for all bridge choices

The proof is the two-endpoint extension argument from
[the movable-barrier lemma](continuation_movable_forced_barriers.md).
It does not require the old interior values to be bad: those values
are being removed from this new menu.

For a fixed parity, treat all selected rank intervals simultaneously.
On a common-role interval the replacement is constant and its endpoint
values agree. On a nonreturn opposite-role interval use the two assigned
anchors in (3). Within such an interval, different assigned rows are
separated by at least d ranks and have difference at most 2C sqrt(d).

For points in different intervals, compare their assigned original
anchors. A left-anchor insertion lies within the first three quarters
of its interval, and a right-anchor insertion lies within the last three
quarters. The distance between the assigned anchors is at most four
times the distance between the inserted points. Return intervals use
the facing endpoint, since both endpoint values agree. The original
C-Hölder bound therefore proves a 2C-Hölder bound for every partial
parity function, uniformly over all choices of p and all singleton
selections.

The small-node convention retains original values in the opposite role
and a return cap in the common role. Original points use themselves as
anchors, so the same comparison includes these nodes.

At the fixed anchor endpoint guards, both original coordinate functions
are constant. The construction makes no change there. Any locality
dependent row filter and physical stride must be chosen using the
inflated fixed constant before defining the good rows.

## 5. Candidate provenance and the count that does transfer

A new beta value in Q is an endpoint-corner value of Q. At a fixed rank
and fixed ancestor depth, each parity has at most two such coordinate
candidates. Their raw coordinates lie on the two grids of that depth.
For side a and fixed coordinate c, at most O(Na) ranks receive this
candidate. The total rank mass at that depth is O(N^2).

These are the same upper bounds used for the original potential cap
rows. Enumerating all corner candidates before sampling covers every
bridge position and every selected cap, at a fixed multiplicative cost
per depth. The new selection does not need to be conditioned upon.

Consequently the previously proved one-parity prescribed-row kernels,
near-pair cap mass bounds, and physical-divisor long-six lists apply to
this enlarged corner menu. The all-parity long-six incidence arguments
also retain their separate field laws: each corner value is a function
of its own parity parameters. The maximum candidate side is L_0. The
fixed locality inflation changes constants, not the stated exponents.

This transfer concerns the compiled support union. It does not mean that
selecting the new options creates no supports.

## 6. What remains to be solved

Both coordinates of a virtual pair can now be projected to corners of
the same cap. The previous bidirectional-P argument explicitly assumes
at most one projected coordinate in its base pair. A separate
[global corner-packing proof](continuation_corner_menu_bidirectional_p.md)
now extends that estimate to the paired endpoint corners used here.
It does not justify arbitrary unrelated coordinate projections. The old
intrinsically forced-stub estimate also used its specific bad-coordinate
witness, which a new opposite-role barrier need not have.

The menu is not a monotone erasure of the original two-function support
union. It may introduce P or higher-arity supports through copied corner
values. These must be tested in the enlarged union. A movable barrier
need not avoid an arbitrary marked set: a fixed positive fraction of an
interval may contain marked points at every possible placement.

Thus Section 2 is a compatible improvement of the audited scaffold.
Sections 3–5 establish a richer occupancy-preserving geometric menu and
its long-six candidate counts. They do not prove simultaneous residual
avoidance or a quadratic construction.

Independent review: two separate written reviews passed the dirty-child
area charge, boundary-clean endpoints, movable interval construction,
global partial-parity 2C-Hölder comparison, and enlarged corner candidate
masses. The distinct P-count and repair scopes were checked explicitly.
