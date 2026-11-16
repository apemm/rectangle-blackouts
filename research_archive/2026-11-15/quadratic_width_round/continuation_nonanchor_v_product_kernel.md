# A product-gap row kernel on both nonconstant V arms

15 November 2026. For a fixed number of prescribed nonanchor rows, the
multiscale V-map has the same product-gap probability bound as one
central arm. The two arms share an offset, but their independent fields
supply a prefix constraint across the arm split. This extends the
dirty-witness path argument to nonanchor cap and corner forms.

## 1. Prescribed rows and raw indices

Condition on the sampled good anchor. Use the original offset law first:
U is uniform on a fixed integer interval of length Theta(h), independent
of the two arm fields. The residue-restricted law is treated by bounded
density at the end.

Fix k raw indices, where k is independent of h, and k prescribed
nonanchor physical rows. Enumerate their bounded row/index errors first.
Repeated indices with inconsistent target rows are discarded. Other
repetitions contribute factors one to the gap product.

Write the sorted indices as

`x_1<=...<=x_k`, `Q=product_(j<k)(1+x_(j+1)-x_j)`.     (1)

The claim is

`Pr(all prescribed rows) <= C_k log^(2(k-1))(2h)/(h Q)` (2)

up to an additional fixed logarithmic factor if needed for the model's
bounded provenance convention. All statements concern nonconstant arm
forms. A fixed physical anchor plateau is not one of these forms.

The inverse occurrence relation on either arm is

`F_arm(y)=distance of x from U+O(1)`,                 (3)

where y is the target height above the fixed common base, in profile
index units. The fixed base and anchor insertions change this relation
only by O(1). Each counting function has derivative between fixed
positive constants. Its multiscale variables on disjoint dyadic
physical intervals are independent. A target interval of length t
contains such a variable with coefficient at least
`c t/log^2(2h)`.

## 2. All targets on one arm

This is the reviewed central proof, with the raw order reversed on the
left arm. Consecutive target heights have differences comparable to the
corresponding raw gaps, unless the gap is bounded. Choose one dyadic
variable inside each nontrivial target-height gap. These intervals are
disjoint. Their row-count differences give independent bounded-width
constraints, each costing at most C log^2(h)/(1+raw gap).

The target nearest the common base has its prefix disjoint from those
selected intervals. Once the fields are fixed, its equation allows O(1)
offsets U. This costs C/h. Multiplication proves (2).

## 3. Targets on both arms

Fix a possible split between x_j and x_(j+1). There are only k-1 such
splits, and an actual realization has at most one of them. Within each
arm choose the disjoint target-gap variables from Section 2. There are
k-2 internal gaps in total.

Let y_L and y_R be the prescribed heights of the two targets nearest
the common base, one on each arm. Let

`d=x_(j+1)-x_j`.

Any admissible realization of (3) satisfies

`d=F_L(y_L)+F_R(y_R)+O(1)`.

Since both counting functions have derivatives bounded above and below,
one of y_L,y_R is at least c d-O(1). Choose that arm as the long-prefix
arm, using only these fixed target heights. If d is bounded, the desired
factor 1/(1+d) is a constant and this step can be omitted.

On the long-prefix arm choose a dyadic variable inside the physical
interval from the base to its nearest prescribed row. Its coefficient
is at least c d/log^2(h). It is disjoint from every selected internal
gap interval on that arm, because those intervals lie beyond its nearest
target. It is also independent of every variable on the other arm.

Condition on all unselected variables. The short-prefix arm's nearest
target equation determines O(1) choices of U. Its value does not depend
on any selected internal-gap variable: those intervals lie beyond that
nearest target. The offset therefore contributes C/h. For each such U,
the long-prefix target equation restricts its selected variable to an
interval of length O(log^2(h)/d).

Finally impose the k-2 internal row-count difference equations. Their
chosen variables have disjoint supports and diagonal nonzero
coefficients. None of them changes either nearest-target prefix.
Multiplying their strip bounds with the offset and long-prefix bounds
gives (2). This calculation does not claim that U is independent after
the nearest-target equation has been imposed.

Sum the finitely many possible splits and bounded-error choices. This
changes C_k only. The case of a target at the base is covered by the
bounded-prefix convention and the other arm's long prefix.

## 4. Mixed norm patterns and a forbidden-row witness

Fix a directed norm pattern with a fixed number of edges, all sampled
endpoint values being nonanchors. Build its two sorted coordinate paths
and products Q_0,Q_1 exactly as in the
[mixed-tree bound](continuation_mixed_path_tree_probability.md).
Let tau be the minimum product spanning tree in their union. The
fixed-target argument and (2) give the same joint kernel

`h^o(1) tau/(h Q_0 Q_1)`.                            (4)

The physical row-counting step needs only the global Lipschitz upper
bound in raw indices. Rows on different arms need not be monotone in
one common direction. Each tree edge still restricts its row difference
to an interval of O(1+raw gap) integer values.

If an additional specified raw coordinate in one parity must lie in a
deterministic forbidden set of at most b physical rows, the
[dirty-witness augmentation](continuation_dirty_witness_path_kernel.md)
applies without change. Insert the witness index into that parity's
sorted path. Its gap-product increase is comparable to one plus its
distance to the nearest old index. Attach the witness through that
nearest index and root the physical tuple at its forbidden row. The
extra tree width cancels the extra probability denominator. Thus (4)
improves to

`b h^o(1) tau/(h^2 Q_0 Q_1)`.                        (5)

The witness is automatically nonanchor, since all anchors are good.
Repeated-index and bounded-error cases use gap factor one.

## 5. Fixed-length nonanchor paths touching selected caps

Take any fixed path length k. Each physical rank has only O(log h)
potential cap/corner forms, before cap selection. All sampled rows used
by the path are required to be nonanchors. Charge one selected-cap
endpoint to one dirty-child boundary coordinate. Its possible ancestor,
child, and coordinate forms add only a fixed power of log(h).

The full cycle-space height-volume argument in
[the central path note](continuation_central_path_count_limit.md)
uses only bounded row variation within raw-coordinate clusters. This
holds on the entire V-map. The effective coordinate extent can now be
O(h), rather than O(sqrt h); no loss results because the full birth-
product K cancels with the mixed probability kernel.

More explicitly, for a fixed bin of the coordinate orders and adjacent
gaps, put K=Q_0Q_1/tau. The nested circulation basis leaves at most
O_k(hK) possible signed height tuples. Choose the first physical column
in O(h^2) ways and factor each height's norm to recover successive
columns. At each recovered rank choose one of its logarithmically many
potential row forms, discarding those outside the fixed bin. There are
at most h^(3+o(1))K candidates. Equation (5) bounds their expected
contribution by

`h^(1+o(1)) b`.                                      (6)

Summing the subpolynomial number of bins proves (6) for every fixed k.
Cap sizes cause no additional rank multiplicity in this height-first
enumeration: the physical rank sequence was already recovered from the
chosen horizontal legs. The same proof covers the compatible original
cap filling and the paired-corner menu under their deterministic
candidate-form conventions.

## 6. Scope of the path conclusion

Every endpoint row in (6) must be nonanchor. A path that uses a fixed
anchor value needs a separate kernel. The path length is fixed before
h grows; no estimate for an arbitrarily long closure is inferred.

The count includes optional row choices from the compiled nonanchor
union. It does not assert that a consistent singleton assignment exists,
or that deleting every path incidence preserves fullness. In particular,
rarity for each fixed path length does not eliminate a longer forced
path from an odd-forced cap point to an even-forced one.

All inputs are used under the old independent-offset law and transferred
to the residue-restricted law by its bounded joint density. Cap
selection and branch eligibility are not conditioned upon in the upper
bounds. The finite profile count is harmless; paths crossing distinct
profile cores require their own interface argument.

Independent review: two complete written reviews passed the shorter-arm
offset fiber, disjoint prefix and internal-gap variables, repeated and
bounded gaps, bounded insertion errors, and complementary-field signs.
The reviewers also checked the mixed-tree and full height-volume
transfer to deterministic cap menus without cap-area multiplicity.
