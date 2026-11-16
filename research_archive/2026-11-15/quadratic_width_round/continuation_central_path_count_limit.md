# What the central P sampling bounds give for paths

15 November 2026. The mixed-tree method applies to a prescribed directed
P path, but its present counts do not make paths of any fixed positive
length subquadratically rare. This note records the two precise losses
relative to cycles. It does not assert a lower bound for actual path
incidence.

## 1. Path variables and the probability kernel

Work with distinct genuine central objects in the
[multiscale row model](continuation_multiscale_row_sampling.md).
A path with \(k\ge2\) directed edges has \(k+1\) objects and equations
\[
                   b_{v+1}-a_v=Y_v,\quad 0\le v<k.    \tag{1}
\]
The \(k\) odd source coordinates and the \(k\) even target coordinates
define two sorted weighted paths on the edge indices. Set
\[
 Q_0=\prod(1+\text{successive odd-source gap}),\qquad
 Q_1=\prod(1+\text{successive even-target gap}).       \tag{2}
\]
The unused even coordinate of object 0 and unused odd coordinate of
object \(k\) are not included in these products.

For fixed norm heights, the fixed-target proof of
[the mixed-tree lemma](continuation_mixed_path_tree_probability.md)
applies without a cycle:
\[
 \Pr((1))\le {h^{o(1)}\tau\over hQ_0Q_1}
             \le {h^{o(1)}\over h\max(Q_0,Q_1)}.       \tag{3}
\]
Every target in a parity is specified after fixing the opposite
parity's source tuple. For the joint proof, fix the complete odd-source
tuple first and sum independent fixed-target parity masses. No sampling
of an unused endpoint row is imposed or charged.

## 2. The missing closing constraint

Actual P edges have horizontal span below \(h\), and \(k\) is fixed.
Choose the first object in \(O(h^2)\) ways, the second in \(O(h)\),
and the first signed height by norm factorization. Every subsequent
height differs from its predecessor by \(O_k(\sqrt h)\), by locality
within each parity. Its norm factorization fixes the next horizontal
leg up to a divisor factor. There are now \(k-1\) such free heights.
Thus
\[
 \#\{\text{path rank-and-height candidates}\}
                  \le h^{k/2+5/2+o(1)}.              \tag{4}
\]
For a \(k\)-cycle there are only \(k-2\) free heights; the final
horizontal leg is already fixed and its height has divisor-many choices.
The path count loses a factor \(\sqrt h\).

For one edge, the uniform-offset argument gives a more explicit bound.
Condition on the odd field and its offset. Each prescribed even target
has \(O(1)\) admissible even offsets, so the probability is \(O(1/h)\).
The number of integer right triangles with hypotenuse at most \(h\)
is \(O(h\log(2h))\): parameterize a primitive direction by \(m>n\),
sum at most \(h/(m^2+n^2)\) dilations, and sum over
\(m,n=O(\sqrt h)\). Therefore
\[
                         \mathbb E N_{\rm edges}
                            \le C h^2\log(2h).       \tag{5}
\]
The fixed horizontal lattice and in-strip ownership conditions can
only reduce this count. Equation (5) is an upper bound, not a claim
that a comparable number of actual edges must occur.

## 3. The two unmatched endpoint coordinates

Translate the first raw cell to the origin. All path objects are within
raw-coordinate distance \(H=C_k\sqrt h\). If \(Q_0\le T\), the
odd-source gap tuples number \(O_k(T\log^{k-2}(2h))\). Apply the
even-target sampling estimate and sum its inverse gap product
harmonically.

There are two extra free raw-coordinate choices: the location of the
first even target relative to the fixed initial even coordinate, and
the final object's unused odd coordinate. Each has \(O(H)\) choices.
Once these and the two sampled coordinate lists are fixed, every raw
cell is fixed. Norm-height multiplicities remain \(h^{o(1)}\).
Consequently
\[
 \mathbb E\#\{\text{\(k\)-edge paths}:\min(Q_0,Q_1)\le T\}
                     \le h^{2+o(1)}T.                \tag{6}
\]
This is a safe grid overcount. Repeated cells and impossible Hilbert
rank orders may be discarded. No lower bound is inferred from the
two free-coordinate factors.

## 4. The corresponding dyadic estimate remains above two

For completeness, repeat the close-height and tree-exchange split of
[the fixed-cycle theorem](continuation_fixed_cycle_dyadic_bound.md).
In a bin \(Z\le\max(Q_0,Q_1)<2Z\), choose
\[
                         R=C_k h^{1/4}Z^{1/(2(k-1))}.
\]
A close pair of edge-coordinate points gives two heights within
\(O(R)\). In the original path order, the later member of the selected
pair is never the first edge. Its height is free and can be restricted
after the earlier one is known. One \(\sqrt h\) choice becomes \(O(R)\).
The remaining case gives the same tree exchange as for cycles.
Both contributions are bounded by
\[
                  h^{k/2+5/4+o(1)}
                         Z^{-(2k-3)/(2k-2)}.         \tag{7}
\]
No change of directed geometric edges is needed.

Combining (6) and (7) yields
\[
 \mathbb E N_{{\rm path},k}
 \le h^{\,2+(2k-3)(k-1)/(2(4k-5))+o(1)}.             \tag{8}
\]
For two and three edges the exponents are \(13/6\) and \(17/7\).
These bounds are not subquadratic. This demonstrates a limitation of
the current estimates, not the impossibility of a sharper path theorem.

## 5. Height-first counting gives a quadratic upper bound

There is a sharper upper bound for paths with two or three edges.
Use the fixed coordinate-gap bins, threshold partitions and ultrametric
\(D\) from
[the height-first cycle theorem](continuation_height_first_five_cycle_bound.md).
Let \(M\) be the minimum \(D\)-tree product on all \(k\) edge indices.
Let \(\tau\) be the union-path minimum tree product and
\(K=Q_0Q_1/\tau\).

For a path, every height is free. Enumerate them together along a
\(D\)-tree in \(O_k(hM)\) ways, then choose the first object and
factor each fixed nonzero height to enumerate successive horizontal
legs. This gives \(h^{3+o(1)}M\) candidates and therefore
\[
                     \mathbb E N_{\rm bin}
                              \le h^{2+o(1)}M/K.     \tag{9}
\]
There is no closing edge whose height can be omitted.

Let \(\beta(t)\) be the cycle rank of the simple bipartite incidence
graph of the two threshold coordinate partitions. The threshold
identities now give
\[
                  \log(M/K)=\int_1^{C_k\sqrt h}
                                      \beta(t)\,{dt\over t}\ge0.
                                                               \tag{10}
\]
Unlike the cycle calculation, there is no subtraction from deleting
a singleton vertex. Thus the forest-incidence case has \(M=K\)
and places this upper-bound method exactly at the quadratic scale.

With \(k\le3\) edges the incidence graph has at most three simple
edges, so it is always a forest. Summing the subpolynomial number of
gap bins gives the improved bound
\[
 \mathbb E\#\{\text{central paths with two or three edges}\}
                                 \le h^{2+o(1)}.     \tag{11}
\]
This is stronger than the corresponding values in (8), but is still
an upper bound. Equations (9)--(10) do not prove that quadratic
incidence is attained.

The full cycle-space estimate removes the remaining loss \(M/K\).
Use [the nested circulation-volume lemma](continuation_cycle_height_cycle_space_volume.md),
but do not delete a closing edge index. At threshold \(t\), form the
bipartite multigraph of the two coordinate partitions, retaining one
edge for each of the \(k\) path heights. Its signed incidence rank is
\(r(t)=c_0(t)+c_1(t)-c_U(t)\). Row variation within coordinate blocks
gives
\[
                 |z\cdot Y|\le C_k t
\]
for every simple cycle circulation \(z\) of this multigraph.
The cycle spaces are nested as the partitions merge. At the largest
scale the \(k\) edges are parallel, and their cycle space is the
\((k-1)\)-dimensional zero-sum subspace.

Choose an adapted cycle basis, recording the scale \(t_i\) at which
each of its \(k-1\) vectors appears. One distinguished height and
the corresponding circulation values are independent integer
linear coordinates with distortion bounded in terms of \(k\).
The lattice-box count therefore gives at most
\[
 C_k h\prod_{i=1}^{k-1}t_i=O_k(hK)
 \tag{12}
\]
height tuples, because
\[
 \log\prod_i t_i
     =\int_1^{C_k\sqrt h}(r(t)-1)\,{dt\over t}+O_k(1)
     =\log K+O_k(1).
 \tag{13}
\]
The dyadic-bin rounding is harmless: each birth scale changes by
at most a fixed factor, and there are only \(k-1\) such scales.

Enumerate all heights first, choose the first object, and factor
their norms to recover the subsequent horizontal legs. Equation
(12) gives \(h^{3+o(1)}K\) candidates per bin. The mixed probability
kernel is \(h^{-1+o(1)}/K\). Hence, for every fixed \(k\ge1\),
\[
 \mathbb E\#\{\text{central genuine P paths with \(k\) edges}\}
                              \le h^{2+o(1)}.
 \tag{14}
\]
The subpolynomial number of bins and fixed provenance choices is
included in the error exponent. There is no bridge or singleton
subtraction in (13), since every path height is free. Thus this
stronger argument still supplies no power saving.

## 6. The next combinatorial object

A single long directed path need not obstruct a compatible selection
of singleton parities or private slots. A deficient choice witness may
instead require several parallel paths interacting with the same
objects. Such a witness imposes joint row equations not present in
(1). The relevant next question is whether its additional constraints
give a stronger sampling bound while retaining actual positions,
shared row variables, and the prescribed choices.

This note does not reduce Hall failure to an unspecified abstract
ladder. That reduction, and the geometry of any candidate witness,
must be established before using a ladder count in the construction.

Independent review: the full written note passed a separate check of
the fixed-target kernel, free-height and endpoint-coordinate counts,
single-edge upper bound, and optimized path exponents. The review
retains the stated distinction between a counting limitation and an
actual lower bound or Hall obstruction. The height-first and full
cycle-space extension in Section 5 also passed an independent written
review: all path heights are free, the adapted birth-product is (K),
and no additional endpoint-coordinate enumeration enters that count.
