# Almost all side-16 offset systems have a greedy proof

15 November 2026. Of the 215,640 nonempty complete-offset systems for
the ordinary side-16 Hilbert tile, stride 32, and three private choices,
215,634 are gain-weighted 2-degenerate. Only six offsets leave a
nonempty weighted 3-core. Three of these cores have immediate colorings.
The other three are genuinely three-connected, contain several gains,
and are not colorable with only two of the three colors.

This gives a structural explanation for most of the finite certificate
table. It does not establish a degeneracy theorem for arbitrary tile size.

For sides 4 and 8, every nonempty offset system is weighted
2-degenerate: all 2,003 and 22,339 offsets, respectively. Their complete
internal P solvability therefore needs only reverse greedy coloring.

## 1. The constructive peeling lemma

For each ordered pair r<s, collect its forbidden residues into
`G_rs subset Z/3`. A color assignment must satisfy

\[
                 \xi_s-\xi_r\notin G_{rs}.
\]

Give this pair weight `|G_rs|`. Repeated events with the same residue
contribute only one unit. If a vertex has total incident weight at most
two, remove it. After the remaining graph is colored, at most two of
its three colors are forbidden by its retained neighbors. Choose any
remaining color and continue in reverse removal order.

Consequently, every coloring of the weighted 3-core extends to the
whole system. An empty core gives a direct greedy construction, with
no constraint search. This lemma allows arbitrary gains and arbitrary
underlying graphs.

One useful infinite family follows immediately. If a candidate system
uses a single positive slot gap q, every rank has at most two later
neighbors, at differences `floor(q/3)` and `ceil(q/3)` when those are
positive. There is one forbidden residue on each such pair. Peeling
the least rank proves certified three-choice solvability, independently
of which label pairs realize the gap. More generally the same proof
works whenever at most two weighted forward constraints occur at each
rank. This concerns all offsets having that structural property, not
only the finite tile table.

## 2. The complete side-16 core table

The [structural checker](probe_private_tile_gain_cores.py) reconstructs
the systems with the independent Euclid generator from the
[complete-offset audit](continuation_all_offset_private_tiles_audit.md).
It performs weighted peeling and records the exact surviving vertices
and gains in [the core data](private_tile_gain_cores_side16.json).
The smaller-size results are saved separately for
[side 4](private_tile_gain_cores_side4.json) and
[side 8](private_tile_gain_cores_side8.json).

| Offset T | Core vertices | Core edges | Gain counts (0,1,2) | Simple coloring |
|---:|---:|---:|---:|---|
| -1461 | 6 | 9 | (0,9,0) | constant zero |
| 3201 | 6 | 9 | (3,0,6) | two constant triangles |
| -1740 | 15 | 25 | (0,17,8) | constant zero |
| 1732 | 47 | 87 | (4,64,19) | three colors needed |
| -1733 | 58 | 109 | (19,62,28) | three colors needed |
| -1739 | 66 | 120 | (15,73,32) | three colors needed |

All remaining core edges have a single gain. Thus contraction of pairs
with two forbidden residues is not needed in this table. Such a pair
would force the unique remaining color difference, but none survives
to these cores.

At T=3201 the core vertices are

\[
                 (27,28,29),\qquad(181,182,183).
\]

Each displayed triple is a triangle with forbidden gain 2 on its
increasing-rank edges. The three corresponding matching edges between
the triples have forbidden gain 0. Give the first triple color zero
and the second triple color one. This is a hand proof for the core,
then the peeling lemma handles every other vertex of that offset.
The same proof works for any two constant-color clusters whose internal
constraints exclude only nonzero differences and whose cross constraints
exclude only zero.

The first six-vertex core is also a triangular prism as an unlabelled
graph, but all its gains are 1. Its constant coloring is therefore
immediate. The 15-vertex core also has no zero gain.

## 3. What the larger cores rule out

[Direct separator checks](private_core_structure.json) find no one- or
two-vertex separator in any of the six cores. In particular, ordinary
two-terminal series/parallel decomposition does not explain them.
The minimum underlying degree is three. The three larger cores have
maximum degrees 6, 6, and 7, respectively.

An exact binary-color implication check rejects the three larger
cores. Translation symmetry of the colors means it is enough to test
the color set `{0,1}`: every two-element subset of `Z/3` is a translate
of this set. Their valid saved three-color assignments remain checked
by the complete-offset audit.

All three larger cores have the same rank-gap/gain menu:

\[
\begin{split}
 &(20,1),(21,1),(25,0),(33,1),(34,1),\\
 &(44,2),(45,2),(107,1),(108,1),(116,0).
\end{split}
\tag{1}
\]

The actual slot gaps and positive vertical differences are only

\[
\begin{array}{c|rrrrrr}
q&61&75&100&134&322&348\\
Y&3465&3465&3471&3465&3465&3473\\
(L-Y)/2&256&375&625&1024&3703&4096.
\end{array}
\tag{2}
\]

The [exact norm extraction](private_core_norms.json) checks these data
against the actual cells and both cross roles. The difficult finite
cores are therefore concentrated around one short vertical interval,
with several different half-factors. They are outside the bounded
half-factor regime of the asymptotic thin-block theorem.

The [rational interval test](probe_private_core_beatty.py) also finds no
open interval satisfying the phase-independent Beatty criterion for
every pair in (1). This only rules out that sufficient criterion for
the whole menu. It does not rule out a phase-specific Beatty assignment,
a different periodic rule, or the actual sparse label graphs, which
are already certified solvable.

## 4. A compact exceptional coloring

The 47-vertex core at T=1732 admits a particularly short check. Start
with zero everywhere, set ranks 18 and 213 to color 2, and set ranks
38 and 39 to color 1. These four changes satisfy all 87 core edges.
The core data and its checked original certificate give this assignment
directly. Reverse weighted peeling extends it to all 256 vertices.

For the remaining two cores the saved assignments give finite solutions,
but no comparable structural coloring rule has been proved here.
The data point toward the geometric realization of the six-gap menu,
rather than a series/parallel reduction or a generic three-gap theorem,
as the next useful invariant.

## 5. A compact certificate without search

The [compact certificate](private_tiles_peeling_certificate.json)
contains only the 198 colors on the six exceptional cores. The
[standalone verification](check_private_tiles_peeling_certificate.py)
regenerates all complete-offset systems, independently performs weighted
peeling with directed adjacency gains, colors each exceptional core from
that small certificate, and greedily extends it in reverse removal order.
It then checks every original modular constraint.

The [saved run](check_private_tiles_peeling_certificate.json) passes all
215,640 offsets and all 4,290,580 candidate constraints. Its normal
verification does not read the large table of 133,470 assignments or
invoke a search solver. The `--extract` option was used only once to
copy the six core assignments into the compact certificate. The full
constraint digest again agrees with the independent complete-offset audit.

This structural computation is new and awaits an independent rerun.
It uses no larger tile than the already certified side-16 tile.
