# A bounded R2s row coloring would preserve every label and every slot

15 November 2026. A bounded coloring of the R2s row-pair graph is a
sufficient replacement for the R2s row deletion at the occupied-core
stage. The color classes need not have bounded gaps. Endpoint interval
filling retains all labels of each color product and gives a uniform
same-parity norm gap after one fixed slowdown.

The required uniform coloring remains unproved. The exact row-one graph
contains triangles, so two colors do not suffice. Finite enumeration
through row-minus-one 262144 finds no three-core, but this is evidence
only. This reduction does not control P or the other residual families.

## 1. Define the row graph before choosing columns

Fix one constant-sea profile and its ambient height h. Within each
parity pool, connect two distinct rows if they can be the two core rows
of a nondegenerate crossed same-sea R2s support, with all corners in the
strip and with

\[
                         |\Delta y|^2\le2|\Delta x|.
 \tag{1}
\]

Include the actual sea-column congruences, but allow arbitrary horizontal
translations and column distances. Common corners can have either color:
the four black symmetric-difference points already force the collision.
Equal core rows cannot produce a nondegenerate crossed R2s support.

For row-one sea, the lower core row is the side owner and the positive
offset formulas below give the complete graph. At another fixed low sea,
the additional negative-offset supports must also be included. The
row-one enumeration alone does not enumerate those other profile graphs.

Their additional negative offsets need only a fixed palette. Assume,
as in the bulk profiles here, that every core row lies above the fixed
low sea s. The in-strip common row implies
`0<|delta|<=2(s-1)`. In a fixed row residue r0 modulo four, add the color

\[
 {y-r_0\over4}\pmod {\lfloor(s-1)/2\rfloor+1}.
\]

This separates every negative-offset pair. For positive offsets, the
vertical translation `y -> y-s+1` reduces to the row-one graph at the
translated strip height. Consequently a uniform K-color theorem for the
positive row-one graphs gives at most
`K*(floor((s-1)/2)+1)` colors for the full graph at fixed s. Sea three
costs only a factor two. Vertical reflection gives the analogous result
for a sea within a fixed distance of the top boundary.
If rows below the low sea are also included, those finitely many boundary
rows can instead receive separate colors. They are not included in the
displayed exact palette factor.

Suppose the odd and even row graphs have proper colorings with c0 and c1
colors. Partition the original Cartesian label family into its nonempty
color products. These products cover every original pair exactly once.
Within a product, all selected odd rows have one odd color and all
selected even rows have one even color.

## 2. Fill each color product without row-gap assumptions

Use the original physical arithmetic row pools, with step four, as
coordinate axes. Embed their complete rectangle in a padded side-N
Hilbert square, where `N=O(h)`. This step does not compress either color
class into a new index list. Let G be the Hilbert ranks of the genuine
labels in one nonempty color product.

Anchor each rank r in G at fine index `Mr`, with relative physical column
`4Mr`. Translate the whole core by four to use positive board columns.
Retain its genuine double there. Between consecutive anchors `u<v`, put
the odd row of u at fine indices in the first half of the interval and
the even row of v in the second half. Before the first anchor, use its
even row; after the last anchor, use its odd row. Every other fine index
has exactly one selected point. All selected values belong to the
appropriate color class.

The proof of
[the endpoint interval lemma](continuation_good_pair_interval_filling.md)
uses only the values at retained anchors. It therefore applies directly
on this uniformly slowed anchor set, without defining any intermediate
total row functions. For either parity, associate a selected point to
its copied anchor. Two distinct associated anchors are separated by at
most twice the distance between the selected fine indices.

The Hilbert coordinate bound and row step four give

\[
 |\Delta y|^2<256|\Delta r|
\]

between original anchors. Consequently, any two selected points of the
same parity, at fine distance q, satisfy

\[
                      |\Delta y|^2<{512\over M}q.
 \tag{2}
\]

Equal copied values satisfy the desired bound trivially. Choose the fixed
integer `M=128`. Since the physical column distance is `4q`, (2) is
strictly stronger than (1). There are no isolated seam exceptions.

In particular, every nonhorizontal same-parity distance is nonintegral:
its squared vertical component is smaller than `2|Delta x|`, whereas
the next square above `|Delta x|^2` differs by `2|Delta x|+1`. The same
parity points lie strictly inside the horizontal cone. The established
cone argument therefore excludes same-parity right triangles and
nondegenerate same-parity side/diagonal mixed supports.

No crossed R2s support remains in this core. If one existed, its two
core rows would define an edge of the graph in Section 1 and would have
the same color, contradicting properness.

This works with arbitrarily long missing intervals in either color
class. Those intervals change which endpoint is copied, not the locality
constant or the width. It also creates no extra double label.

## 3. Coverage, occupancy, and limitations

Use all fine indices `0,...,MN^2-1`, so the exact width of each core
is `m=4MN^2`. Give every nonarithmetic column its prescribed constant sea point.
Every arithmetic column has a genuine double or the singleton just
specified. The core is fully occupied at spacing four. If its width is m
and its color product has q genuine labels, its black-point count is
exactly `m+q`.

Each color product needs `O(h^2)` width, with an absolute slowdown
independent of its row gaps. Thus at most `c0*c1` cores cover the whole
profile in width at most `4M c0 c1 N^2=O(c0*c1*h^2)`, retaining every
label exactly once.
For a fixed collection of profiles with uniformly bounded palettes, this
is a quadratic occupied-core construction with no R2s-driven relocation.

Retaining every label globally does not make every arithmetic slot a
double. The color-product padding and the slowed intervals contain
singletons, including forced odd singleton choices under this rule.
Their P constraints have not disappeared. No old cap counting theorem
is claimed for their potentially large nearest-anchor provenance.

The assertion concerns separate cores. Valid joins and collars still
need their stated endpoint hypotheses. P, three-core triangles,
four-core mixed supports, and parked-six coincidences remain open.
The adaptive nearest-anchor provenance can be large, so the earlier
random-cap incidence estimates do not automatically transfer.

## 4. Exact factor enumeration for the row-one graph

Put `n=y-1`, with target row `n+delta+1`. The audited horizontal-half
classification gives `T>=delta>0` and `U<=n`. Define

\[
 a=X-T>0,\quad b=U-X>0,\qquad
 4ab=T^2+\delta^2,\qquad n={T(T+a+b)\over\delta}.
 \tag{3}
\]

Here delta is a positive multiple of four and T is even. Conversely,
these positive integers reconstruct the exact support once its
divisibility, strip, norm-gap, and sea-column tests pass. In particular,
`X=T+a`, `U=T+a+b`, and the other sea column is `T+b`.

For a row-minus-one bound H, locality gives `delta^2<2H`.
Also `U>2T`, so `T^2<H*delta/2`. Enumerating delta and T in these
ranges, then the positive divisors a of `(T^2+delta^2)/4`, is complete.
The isolated seam has no positive-offset realization.

The [enumerator](probe_r2s_row_pair_graph.py) uses this factorization.
An [independent small check](check_r2s_row_pair_graph_small.py) instead
enumerates every positive divisor `U | n*delta`, every delta up to `H-n`,
and both signs of the square root for V. Their complete support sets and
edge counts agree at H=64,128,256,512.

At H=262144 the complete finite graph has 15174 edges and degeneracy two.
Its biconnected blocks are 15150 single edges, four triangles, and three
four-cycles. Thus this finite graph is a cactus and is outerplanar.
No edge lies in two simple cycles. The saved summary includes all seven
cyclic blocks and their 24 exact support witnesses. This stronger finite
observation does not prove a uniform cactus or coloring theorem.
By residue of n, the observed counts are:

| n modulo four | Edges | Incident vertices | Degeneracy | Triangles |
|---|---:|---:|---:|---:|
| 0 | 3454 | 6463 | 1 | 0 |
| 1 | 2820 | 5308 | 1 | 0 |
| 2 | 6197 | 10771 | 2 | 4 |
| 3 | 2703 | 5065 | 1 | 0 |

The compatible odd row pool above sea one uses `n=2 mod4`; even pools
use n odd. The n=0 class is an additional arithmetic overgraph, not a
required odd profile for this sea.

These are finite observations, not uniform degree or color bounds.
Results are saved in [the full summary](r2s_row_pair_graph_262144.json)
and [the residue summary](r2s_row_pair_graph_residue_summary.json).

## 5. Explicit obstructions to two elementary coloring arguments

The three actual odd rows

\[
                         22251,\quad22271,\quad22307
\]

form a row-graph triangle. For increasing pairs, the witnesses
`(X,U,T,V)` are respectively

\[
 (2220,2225,200,-2015),\quad
 (2176,2225,560,-1567),\quad
 (1456,1530,524,-858).
\]

They pass the actual sea residues, strip tests, and norm gap.
Thus any placement-independent row coloring requires at least three
colors. This is a row-graph triangle: the three witnesses need not occur
simultaneously at one triple of columns.

Uniform outgoing degree at most two is also false. The source `n=16575`
has the following six target values and witnesses:

| Target n | X | U | T | V |
|---:|---:|---:|---:|---:|
| 16591 | 800 | 850 | 312 | -438 |
| 16599 | 888 | 975 | 408 | -393 |
| 16607 | 992 | 1105 | 480 | -399 |
| 16623 | 2192 | 2210 | 360 | -1814 |
| 16635 | 3820 | 3825 | 260 | -3555 |
| 16731 | 14364 | 14365 | 180 | -14183 |

Finally, the relevant n=2 class already has an increasing path of length
four: `168510,168750,168950,168970,169006`. A short directed-height
argument does not explain the observed three-colorability. A bounded
color theorem, or a growing-chromatic obstruction, remains the target.

The [direct geometric checker](check_r2s_row_graph_witnesses.py) verifies
these 13 individual supports by their rectangle diagonals, sea residues,
strip bounds, and all 52 common-corner colorings. Its
[saved result](check_r2s_row_graph_witnesses.json) does not depend on the
row-graph enumeration.

Independent written review of Sections 1--3 passed the arbitrary-gap
anchor argument, the slowdown constants, proper-color retention,
exact occupancy and excess count, and the stated singleton, provenance,
and collar limitations. The fixed-low-sea extension has also passed
independent review under its stated above-sea bulk hypothesis. The finite enumeration has the independent
small-range check described above.
