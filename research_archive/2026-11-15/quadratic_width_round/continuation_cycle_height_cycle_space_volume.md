# Height constraints from the full coordinate cycle space

15 November 2026. Independently reviewed proof. The height-first
cycle count can use alternating-sum constraints as well as pairwise
height differences. This removes the loss from a coordinate-cluster
pattern of type K(2,3). It does not yet give a subquadratic bound for all
six-cycles or a construction.

## 1. Fixed patterns and threshold graphs

Fix a directed central P cycle on k objects, with k independent of h.
Its edge heights are Y_v = b_(v+1) - a_v. Use the two raw-coordinate
order paths from the mixed-path probability theorem: the odd coordinates
are i_v, and the cyclically shifted even coordinates are j_(v+1).
Every path edge has weight one plus its coordinate gap. Write Q_0 and
Q_1 for their products, tau for the minimum-product tree in their union,
and K = Q_0 Q_1 / tau.

All raw coordinate differences are at most R = C_k sqrt(h). Increase R
by a fixed factor when needed. At threshold t, keep the order-path edges
of weight at most t. Their component partitions have a(t) and b(t)
blocks. The union of the two order paths has c(t) components.

Form a bipartite MULTIGRAPH G_t. Its vertices are the two sets of blocks.
Each edge index v contributes one edge from its odd block to its shifted
even block. Parallel edges retain their multiplicity. It has k edges,
a(t)+b(t) nonisolated vertices, and c(t) connected components. Its
incidence rank is

    r(t) = a(t) + b(t) - c(t).

This uses the signed incidence matrix, oriented from odd to even.
The elementary tree-product identities give

    log K = integral_1^R (r(t)-1) dt/t,
    log tau = integral_1^R (c(t)-1) dt/t.                 (1)

Indeed the logarithm of a path product is the integral of its number of
threshold components minus one. The same identity holds for a minimum
spanning tree of the union, as one sees by merging threshold components.
Endpoints of the step functions do not affect the integral.

Choose an edge index e to be the eventual closing edge of the directed
P cycle. Remove e from G_t and discard isolated vertices. Let r_e(t) be
the rank of the remaining incidence matrix. Deleting one edge decreases
incidence rank exactly when that edge is a bridge. Therefore

    r_e(t) = r(t) - 1_{e is a bridge in G_t}.             (2)

The bridge convention includes an isolated single-edge component.
Parallel edges are not bridges.

## 2. Every coordinate-cluster circulation constrains heights

Each block of a threshold coordinate partition has physical row diameter
at most C_k t. This follows from bounded successive row gaps and the fact
that a block has at most k raw coordinates with successive gaps at most t.
Choose one representative physical row for each block. For every edge v,

    Y_v = potential(even block of v)
          - potential(odd block of v) + O_k(t).         (3)

Consequently every simple cycle circulation z of G_t satisfies

    |sum_v z_v Y_v| <= C_k t,                           (4)

where z has coefficients in {-1,0,1}. A pair of parallel edges is a
two-edge circulation, giving the earlier pairwise height constraint.
Equation (4) also includes independent four-edge relations in K(2,3).

Apply this to the graph with e removed, so that (4) only involves the
k-1 free heights. As t increases, coordinate blocks merge. The cycle
spaces of these multigraphs are nested: identifying incidence-matrix rows
can enlarge its kernel and cannot remove an existing circulation.

For sufficiently large t all odd coordinates belong to one block and
all even coordinates belong to one block. The remaining graph consists
of k-1 parallel edges. Its cycle space then has dimension k-2, and it is
exactly the space of coefficient vectors whose coordinates sum to zero.

## 3. A nested linear-volume estimate

First fix the coordinate orders and dyadic bins of all their adjacent
gaps. There are only a fixed power of log(h) such choices for fixed k.
They determine a nested sequence of coordinate partitions up to fixed
factors in all relevant scales. All statements in this section concern
this deterministic bin and precede sampling or height enumeration.

Build a basis of the cycle space incrementally. At each threshold where
its dimension increases, add simple cycle vectors from the current graph
until they span its cycle space. The resulting k-2 independent vectors
z_1,...,z_(k-2) have coefficients in {-1,0,1}. Let t_i >= 1 be the
threshold at which z_i was added, using dyadic upper bounds. There are
at most k-2 additions, regardless of the number of dyadic levels.

Choose one free height as an additional coordinate. The linear map from
the k-1 free heights to this height and the k-2 values z_i dot Y is
invertible. Its determinant is a nonzero integer, and its inverse has
entries bounded in terms of k alone. The distinguished height has O(h)
possible values. Equations (4) constrain the other coordinates to
intervals of lengths O_k(t_i). A bounded-distortion lattice-box count
therefore gives at most

    C_k h product_i t_i                                (5)

integer height tuples. This is an upper bound; parity and norm conditions
have not yet been imposed. One elementary justification for the lattice
count is to surround each integer input point by a unit cube. Their
images have disjoint interiors and fixed positive volume, and lie in the
target box enlarged by a constant depending only on k.

Let B_e = product_i t_i, ignoring fixed factors from dyadic rounding.
Dimension counting gives the equivalent integral formula

    log B_e = integral_1^R (r_e(t)-1) dt/t + O_k(1).     (6)

To check it, the cycle-space dimension at t is (k-1)-r_e(t).
Exactly k-2 basis vectors have appeared at the final scale. The number
whose appearance scale exceeds t is thus r_e(t)-1. Integrating that
count gives the logarithm of the product of their appearance scales.
Replacing the original gaps by dyadic upper bounds changes only a fixed
number of product factors by fixed constants.

Combining (1), (2), and (6) yields

    B_e / K <= C_k exp(-integral_1^R
                              1_{e is a bridge in G_t} dt/t).  (7)

Unlike the earlier pairwise-distance tree bound, (7) never incurs a loss
when the coordinate incidence graph has two independent cycles.

## 4. Count actual P candidates after choosing the heights

Rotate the directed cycle so that e is its closing edge. Enumerate all
k-1 free heights first using (5). For each nonzero odd height Y, the
factorization

    (L-X)(L+X) = Y^2

gives h^{o(1)} possible signed horizontal legs X of an actual in-strip P.
Choose the first physical column in O(h^2) ways, then recover successive
columns from the chosen signed legs. The last horizontal leg is fixed by
closure, and its signed norm height has h^{o(1)} possibilities. Repeated
objects, invalid rows, and candidates outside the chosen coordinate bin
can all be discarded.

There are therefore at most h^{3+o(1)} B_e candidates in that bin.
The independently reviewed joint sampling bound is h^{-1+o(1)}/K.
Their expected number is at most

    h^{2+o(1)} B_e / K.                                (8)

The direct coordinate count still gives h^{1+o(1)} tau in the same bin.
Both estimates can be used, taking their smaller value. The choices of
closing edge, coordinate orders, dyadic bins, and bounded provenance forms
only contribute fixed or polylogarithmic factors.

## 5. The first remaining six-cycle pattern

Under vertex identifications, the endpoints of an edge on a cycle remain
joined by a walk avoiding that edge, so it cannot become a bridge.
Thus each bridge indicator in (7) is nonincreasing with t. Choose e whose
bridge indicator survives to the largest scale. At every threshold, e
is a bridge exactly when some edge is a bridge.

If there is no bridge, each connected component has at least two edges.
For k edges this gives c(t) <= floor(k/2). For k=6 the critical possibility
is three disjoint pairs of parallel edges. It has c(t)=3 and no bridge.
The K(2,3) pattern has c(t)=1 and no bridge, so it is no longer the costly
case for the strengthened height count.

For six edges the pointwise inequality

    c(t)-1 <= 2 + 3 * 1_{some bridge exists}

gives tau <= C R^2 (K/B_e)^3. Using R=O(sqrt(h)) in (8) and balancing
with h^{1+o(1)} tau gives only h^{2+o(1)}. A power saving still needs
additional information about the three parallel-pair cluster pattern,
or a stronger arithmetic closing estimate. The lemma does not prove
such a saving by itself.

The P model restrictions of the preceding notes remain: fixed cycle
length, genuine central objects, fixed bounded provenance multiplicity,
and independent parity fields. Arbitrary cap or anchor vertices and
singleton assignment are outside this argument.

## Review status

The complete saved proof passed an independent written audit. The review
checked the nested circulation spaces, the adapted integer basis, the
lattice-box count, the height-first reconstruction, and monotone bridge
death. It also checked dyadic rounding through the interleaving of actual
and rounded cycle spaces: their birth scales differ by at most a factor
two, and there are at most k-2 such scales. The six-cycle power-saving
gap remains explicit.
