# Continuing the construction and saturated lower bound

11 November 2026. The main result of this pass is a valid all-double construction for every sufficiently large height and every width up to a constant times h squared divided by log-squared h. It also gives a counting estimate for a prescribed-degree family. The saturated threshold and the general O(h) monotone P partition remain open.

## 1. A proved range of all-double boards

There are absolute constants c>0 and h_0 such that, for every h>=h_0 and every integer

\[
 h\le m\le \frac{c h^2}{(1+\log h)^2},
\]

a valid h by m blackout exists with exactly two black cells per column. Therefore

\[
 \boxed{f(h,m)\ge2m}
\]

throughout this range.

The result holds for any prescribed balanced row partition A,B. Each column has one black row in each part. Within each part P, the row degrees can be any prescribed allocation of floor(m/|P|) and ceiling(m/|P|), with sum m.

The proof uses two random bijections from columns to labeled copies of the rows. The prescribed copies enforce the row degrees. A permutation local lemma excludes hidden rectangles and all remaining four- and six-cell collision supports.

The useful improvement over the first square argument is a uniform count for a long rectangle. Two axis rectangles sharing one corner would require a triangle of row pairs, which the fixed bipartition excludes. The remaining six-cell shapes include a tilted rectangle. The axis-side four-cell count uses the elementary bound

\[
 \sum_{L\le X}r_2(L^2)\le4X(1+\log X)^2.
\]

Together these give a local event load bounded by

\[
 C\left[
 \frac{m}{h^2}(1+\log h)^2
 +h^{-1/2}(1+\log h)^2
 +\frac{(1+\log h)^4}{h}
 \right].
\]

The first term is small in the stated range. The other two tend to zero. The copies of each row do not introduce an extra degree factor in this calculation.

See [the full proof](continuation_near_quadratic_all_double.md) and the independent audit.

This is an existence proof, not an explicit arithmetic placement. It covers both parities of h. It permits tilted singleton presentations when they have no competing axis owner.

## 2. A counting estimate for this family

Fix the row partition and one permitted row-degree allocation d_r. Let B count valid all-double boards with those restrictions. In the range of Section 1,

\[
 e^{-Cm}\frac{(m!)^2}{\prod_r d_r!}
 \le B\le
 \frac{(m!)^2}{\prod_r d_r!}.
\]

If h<=m=o(h squared / log-squared h), the loss is exp(-o(m)). Equivalently,

\[
 \boxed{\log B
 =2\log(m!)-\sum_r\log(d_r!)+o(m).}
\]

The factor in the denominator is exact: each physical board has precisely the product of d_r! realizations with labeled row copies. The local lemma supplies the probability lower bound.

This counts the restricted all-double family. It is not the requested number a_h(m) of maximum blackouts.

The separate [regular-square theorem](continuation_regular_square_local_lemma.md) proves that, for every fixed d, all sufficiently large squares have a valid blackout with exactly d black cells in every row and column. In particular, valid two-regular squares exist at every sufficiently large size. Their unrestricted count B_n satisfies

\[
 \log B_n=2n\log n-2n+o(n).
\]

This eliminates broad minimum-row-degree obstructions to all-double boards.

## 3. Progress on a correlated monotone partition

An adaptive queue construction gives exact monotone P-free partitions at the tested heights. Each class has strictly increasing j and Lipschitz constant one. Selected certificates are:

| Height | Number of classes |
| ---: | ---: |
| 32 | 61 |
| 64 | 149 |
| 128 | 347 |
| 256 | 774 |
| 512 | 1725 |

The height-512 certificate covers all 65,536 labels. An independent checker tested both orientations of every P norm for all 2,247,332 pairs within its classes. Nine saved certificates passed exact coverage, monotonicity, Lipschitz, and P checks.

The queue model starts C tokens in each row, then moves one served token up a row in each column. It needs at most CK+A-1 classes. A path dynamic program chooses moves while retaining a legal choice for the next column. What remains unproved is a capacity C independent of height. Finite successes do not establish an O(h) theorem.

See [the queue method and results](continuation_monotone_queue_experiments.md), [the compact certificates](continuation_monotone_queue_certificates.json), and [the independent check](continuation_monotone_certificates_check.json).

There is also a proved obstruction to fixed doubly periodic successor templates. A cyclic template eventually contains an in-strip Pythagorean conflict. An acyclic template has only bounded-length paths. With bounded step size, a height-dependent template giving O(h) classes needs period at least a constant times h to the one-fifth. This applies to that precise template model, not to adaptive queues or arbitrary colorings. See [the periodic-routing proof](continuation_monotone_periodic_routing.md).

## 4. The saturated lower bound needs more than cycle rank

Complete balanced row-pair layouts at heights 5, 6, and 7 can have zero cycle rank for every tilted primitive direction pair and still contain a fatal corner triple. Exact certificates show that zero cycle rank discards relevant local information.

A sharper possible target is:

> An all-double board with distinct, triangle-free row pairs and no tilted rectangle containing three black corners has width at most its height.

This remains a conjecture. It would exclude saturated boards for h>=5, since q_h>h. The height-four endpoint has a complete 72-case certificate, with the surviving corner-free orders excluded by a mixed two-white collision.

The 45-degree version of the conjecture is false. A checked 6 by 7 example avoids every 45-degree corner triple but fails at another slope. Small all-slope solver exclusions are evidence only and have no independently checked UNSAT proofs.

See [the saturation reductions and exact counterexamples](continuation_saturation_reductions.md). The [cyclic staircase family](continuation_cyclic_staircase_obstruction.md) gives a separate analytical illustration of why mixed two-white collisions must be retained.

## 5. The remaining gap

The new all-double construction reaches order h squared / log-squared h doubles. Saturation needs all q_h, of order h squared. At that density, the current local-lemma load bound no longer supplies a small constant. No quadratic equality-threshold bound follows.

The next construction step is to remove or coordinate the axis/tilted six-cell collisions and axis-side mixed four-cell collisions responsible for the leading load. The adaptive monotone queue supplies a concrete alternative to the failed independent thinning, but has no uniform-capacity proof yet.

For the lower bound, individual tilted corner triples and mixed two-white collisions must enter alongside complete row-pair coverage. The cycle-rank budget alone is insufficient.

No general dominance theorem, exact formula for f at all widths, or optimal-blackout counting formula was proved in this pass. All work is uncommitted. Existing manuscripts and earlier reports were left unchanged.
