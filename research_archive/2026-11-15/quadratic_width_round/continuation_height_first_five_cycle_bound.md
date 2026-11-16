# Height-first counting for central P cycles through length five

15 November 2026. Enumerating the nonclosing signed heights before their
horizontal legs avoids the chronological loss in the earlier close-height
argument. Combined with the mixed-tree probability kernel, this gives
expected central genuine P-cycle counts
\[
              N_3\le h^{5/3+o(1)},\qquad
              N_4\le h^{11/6+o(1)},\qquad
              N_5\le h^{15/8+o(1)}.                  \tag{1}
\]
The notation means upper bounds on expectations. All directions and
repeated coordinates are included. These are incidence bounds under the
multiscale sampling, not singleton assignments or a full construction.

## 1. Fixed coordinate-gap bins

Use the central genuine model of
[the multiscale note](continuation_multiscale_row_sampling.md) and
[the mixed-tree kernel](continuation_mixed_path_tree_probability.md).
Fix \(k\in\{3,4,5\}\), and index the directed edges cyclically by
\(v\pmod k\). The requirements are
\[
                        b_{v+1}-a_v=Y_v.             \tag{2}
\]
Order the edge indices once by \(i_v\), and once by \(j_{v+1}\).
These give paths \(P_0,P_1\) on the same \(k\) vertices. The shift
in the second ordering is essential.

An actual fixed-length cycle has all raw coordinates in an
\(O_k(\sqrt h)\) box. Choose a dyadic bin for each of the \(2k-2\)
weights one plus a consecutive coordinate gap. Denote the bin's lower
dyadic endpoint by \(w_e\), so the actual weight is in
\([w_e,2w_e)\). Each \(w_e\ge1\) and
\[
                              w_e\le N=C_k\sqrt h.   \tag{3}
\]
There are only \(h^{o(1)}\) combinations of these bins and the finitely
many coordinate orders. Repeated coordinates have weight one and cause
no exception.

Within a fixed bin, define
\[
 Q_\alpha=\prod_{e\in P_\alpha}w_e,\qquad
 \tau=\min_{T\text{ spanning tree of }P_0\cup P_1}
                   \prod_{e\in T}w_e,\qquad
 K={Q_0Q_1\over\tau}.                               \tag{4}
\]
Parallel edges of the path union retain their separate weights. Replacing
actual weights by these dyadic representatives changes all products by
only a factor depending on \(k\). The reviewed kernel therefore gives,
for each specified rank-and-height candidate,
\[
                              \Pr((2))\le {h^{o(1)}\over hK}.  \tag{5}
\]

There is also a direct coordinate count for this bin. Fix the first raw
cell, in \(O(h^2)\) ways. In each parity, the consecutive gap choices
number at most a constant times their product \(Q_\alpha\). Their
order and the distinguished first coordinate determine all raw cells.
Hilbert inversion determines their ranks. For each fixed rank tuple,
norm factorization gives only \(h^{o(1)}\) signed-height tuples.
Thus (5) yields
\[
                     \mathbb E N_{\rm bin}\le h^{1+o(1)}\tau. \tag{6}
\]
This is stronger than restricting only one parity's product.

## 2. A deterministic hierarchy for the edge-coordinate points

For two vertices \(u,v\), let \(D(u,v)\) be the maximum of the edge
weights on their path in \(P_0\) and on their path in \(P_1\). It is
an ultrametric on the labeled vertices: each path-bottleneck distance is
an ultrametric, and their maximum is one as well. Distinct labels may have
distance one; no zero distance is needed.

The actual raw-coordinate differences are at most \(2(k-1)D(u,v)\).
Uniform bounded physical row gaps and bounded central errors then imply
the deterministic necessary condition
\[
                              |Y_u-Y_v|\le C_kD(u,v).          \tag{7}
\]
This hierarchy depends only on the prescribed bin and coordinate orders,
not on any sampled row field.

Let \(M\) be the minimum product of edge distances of a spanning tree
in the complete graph with distances \(D\). Choose a vertex \(v_*\)
with largest nearest-neighbor distance
\[
              d_* =\max_v\min_{u\ne v}D(u,v).        \tag{8}
\]
Let \(B\) be the minimum tree product on the other \(k-1\) vertices.
Then
\[
                                  B=M/d_*.          \tag{9}
\]
Indeed, at every threshold below \(d_*\), the omitted vertex is a
singleton in the ultrametric partition, so removing it reduces the
component count by one. At every larger threshold its component has
another vertex, and deletion does not change the component count.
The usual threshold formula for a minimum-product spanning tree proves
(9). A direct proof of that formula is recalled in Section 4.

## 3. Enumerate all free heights first

Cyclically rotate the pattern so that \(v_*\) is the closing edge.
The other \(k-1\) signed heights are now enumerated before any horizontal
leg. Root a minimum-product \(D\)-tree on those vertices. Its root
height has \(O(h)\) possible in-strip integer values. By (7), each
child has \(O(D(u,v))\) possible values once its parent is fixed.
Hence there are at most
\[
                                  C_k hB            \tag{10}
\]
possible tuples of nonclosing signed heights.

For each such tuple, choose the first object in \(O(h^2)\) ways.
Each specified nonzero odd height \(Y\) has only \(h^{o(1)}\)
horizontal P legs: factor
\[
                              (L-X)(L+X)=Y^2.
\]
Choose the legs in cyclic order. They determine all subsequent columns
and hence the object ranks, up to the fixed bounded multiplicity of the
model. The closing horizontal gap is now fixed; its possible signed
heights are again divisor-many. Reject any candidate not in the strip,
not in the prescribed gap bin, or with coincident forbidden columns.

This produces at most \(h^{3+o(1)}B\) candidates. It does not require
the selected height-tree order to agree with the cyclic order: all its
heights have already been chosen before leg factorization begins.
Together with (5), it gives
\[
                     \mathbb E N_{\rm bin}\le h^{2+o(1)}B/K.  \tag{11}
\]
The closing height is not counted as a free parameter. This is the step
that removes the earlier chronological restriction.

## 4. Threshold partitions and the simple incidence graph

For \(1\le t\le N\), let the threshold component partitions of the
two paths have \(c_0(t),c_1(t)\) blocks. Let

* \(c_U(t)\) be the component count of their union graph;
* \(c_I(t)\) be the number of nonempty intersections of one block from
  each partition;
* \(s(t)\) equal one when at least one such intersection contains
  exactly one original vertex, and zero otherwise.

The intersections are exactly the threshold components for \(D\).
The integral identities for the products are
\[
 \log\tau=\int_1^N(c_U(t)-1)\,{dt\over t},
\]
\[
 \log K=\int_1^N(c_0(t)+c_1(t)-c_U(t)-1)\,{dt\over t},
\]
\[
 \log B=\int_1^N(c_I(t)-1-s(t))\,{dt\over t}.        \tag{12}
\]
For the first identity, process edges in increasing weight. Just after
threshold \(t\), a minimum tree has \(k-c_U(t)\) accepted edges and
therefore \(c_U(t)-1\) edges still above threshold. Integrating this
number against \(dt/t\) sums their logarithms. The path and ultrametric
versions give the other identities, using (9) and
\(\log d_* =\int_1^N s(t)\,dt/t\). Threshold ties have measure zero.

Form the **simple** bipartite incidence graph whose vertices are the
blocks of the two path partitions and whose edges are their nonempty
intersections. An edge carries the number of original vertices in that
intersection as its multiplicity, but is included only once in the
simple graph. It has \(c_I\) edges, \(c_0+c_1\) vertices, and
\(c_U\) components. Write its cycle rank as
\[
                         \beta=c_I-c_0-c_1+c_U.      \tag{13}
\]
Thus (12) gives the exact identity
\[
                       \log(K/B)=\int_1^N(s(t)-\beta(t))\,{dt\over t}.
                                                               \tag{14}
\]
Parallel original vertices are recorded in the multiplicities and in
\(s\); they must not be counted as parallel edges when computing
\(\beta\). Using a multigraph cycle rank here would be incorrect.

## 5. The five-vertex combinatorial inequality

For \(k=5\), the simple incidence graph has at most five edges.
It is bipartite and therefore has cycle rank at most one. Indeed a
cycle needs at least four edges, and a simple bipartite component of
cycle rank two needs at least six; two cyclic components need at least
eight.

If \(\beta=1\), a cyclic component uses at least four nonempty
intersections and hence at least four of the original five vertices.
At least one intersection is a singleton, so \(s=1\), and at most one
additional union component is possible: \(c_U\le2\).
If \(s=0\), every intersection has at least two original vertices.
Then \(c_I\le2\), again giving \(c_U\le2\), and \(\beta=0\).
Consequently
\[
               g(t):=s(t)-\beta(t)\in\{0,1\},
               \qquad c_U(t)-1\le1+3g(t).           \tag{15}
\]
Integrating (15) with (12)--(14) proves
\[
                     \log\tau\le\log N+3\log(K/B),
                     \qquad {B\over K}\le(N/\tau)^{1/3}.      \tag{16}
\]
In particular \(B\le K\), since the integrand in (14) is nonnegative.

Use (6) when \(\tau\le h^{7/8}\). Otherwise use (11), (16), and
\(N=O(\sqrt h)\). Both cases give
\[
 \mathbb E N_{\rm bin}
  \le h^{o(1)}\min\{h\tau,\ h^{13/6}\tau^{-1/3}\}
  \le h^{15/8+o(1)}.                                \tag{17}
\]
Summing over the subpolynomial number of bins proves the P five-cycle
bound in (1).

## 6. The smaller cycle lengths

For \(k=4\), the same simple incidence graph has \(\beta\le1\).
When \(\beta=1\), all four vertices belong to its cyclic component,
so \(s=1\) and \(c_U=1\). When \(s=0\), there are at most two
intersection blocks and hence \(c_U\le2\). Therefore
\[
                       c_U-1\le1+2(s-\beta),
                       \qquad B/K\le(N/\tau)^{1/2}.            \tag{18}
\]
The two bounds in (6), (11) now give
\[
            \min\{h\tau,h^{9/4}\tau^{-1/2}\}h^{o(1)}
                       \le h^{11/6+o(1)},            \tag{19}
\]
balanced at \(\tau=h^{5/6}\).

For \(k=3\), the incidence graph is a forest, so \(\beta=0\).
If \(s=0\), all three vertices lie in one intersection block and
\(c_U=1\). Hence \(c_U-1\le2s\), which gives
\(B/K\le\tau^{-1/2}\). Thus
\[
               \min\{h\tau,h^2\tau^{-1/2}\}h^{o(1)}
                        \le h^{5/3+o(1)},           \tag{20}
\]
balanced at \(\tau=h^{2/3}\).

## 7. Scope and the next obstruction

All proofs are for fixed central genuine patterns with the bounded-error,
bounded-multiplicity qualifications of the mixed-tree theorem. They do
not condition on selected caps or successful cleanup. The incidence
bounds can be placed in a joint nonnegative-cost objective, subject to
the separate safe-erasure and relocation hypotheses.

For six vertices, the simple incidence graph can already be \(K_{2,3}\).
It then has cycle rank two while every intersection is a singleton,
so \(s-\beta=-1\). The nonnegative-integrand argument behind (16)
therefore does not extend to arbitrary lengths. This is a limitation of
this proof, not a realized P-cycle or an obstruction to quadratic width.
Noncentral objects, longer cycles, and consistent singleton choices
remain separate tasks.

## Review status

The mixed-tree probability and row-field inputs were independently
reviewed earlier. The complete saved proof passed a separate independent
written review, including gap-bin comparability, the deleted-vertex
ultrametric identity, height enumeration before every horizontal leg,
the simple-graph cycle rank with intersection multiplicities, all threshold
integrals, and the three optimized exponents. The threshold derivation
was also independently checked in parallel by another reader.
