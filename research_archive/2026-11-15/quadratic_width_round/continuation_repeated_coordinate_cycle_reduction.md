# Product gaps and the remaining central P four-cycles

15 November 2026. Under the multiscale row sampling, repeated-coordinate
rectangles are not the critical four-cycle case. For every fixed cycle
length, cycles using at most two raw coordinates in one parity have
expected count \(h^{3/2+o(1)}\). A further consequence of the genuine
minimum P gap removes four-cycles whose two raw coordinate extents are
both at most \(h^{1/2-\epsilon}\). The unresolved range has a large
coordinate extent and two intermediate product gaps.

These are incidence bounds for genuine central objects. They do not
choose singleton parities or supply a repair for arbitrary residual
supports.

## 1. Fixed-length sampling and counting conventions

Use the independent parity fields and offsets of
[the multiscale sampling theorem](continuation_multiscale_row_sampling.md).
The underlying padded Hilbert square has side \(N=\Theta(h)\).
Consider a directed P cycle on \(k\) distinct genuine central objects,
where \(k\ge2\) is fixed independently of \(h\). Its raw cells are
\((i_r,j_r)\), and its signed P heights obey
\[
 b_{r+1}-a_r=Y_r,\qquad r\pmod k.                         \tag{1}
\]
For each parity \(\alpha\), sort its \(k\) raw coordinates, retaining
repetitions, and write the adjacent nonnegative gaps as
\(d_{\alpha,1},\ldots,d_{\alpha,k-1}\). Set
\[
 Q_\alpha=\prod_{\nu=1}^{k-1}(1+d_{\alpha,\nu}).           \tag{2}
\]

The three-row sampling proof extends to every fixed \(k\):
\[
 \Pr(\text{\(k\) prescribed rows in one parity})
 \le {C_k\log^{2(k-1)}(2h)\over hQ_\alpha}.               \tag{3}
\]
To see this, first group coordinates whose successive gaps are bounded
by a sufficiently large fixed constant. The omitted factors in (2)
are bounded constants depending only on \(k\). Choose one representative
from each group. If the prescribed event is possible, its distinct target
rows have the same order and their successive distances are comparable
to the corresponding large raw gaps. Select one dyadic slope variable
inside each of these disjoint target intervals. Each coefficient has
magnitude at least the target gap divided by \(C\log^2(2h)\).
Conditioning on all other field variables leaves independent
one-dimensional strips. Finally the field permits only \(O_k(1)\)
offset values. This proves (3), including repeated coordinates and
bounded target errors. The intervals are selected from fixed target
rows, before sampling this parity's field.

Condition on the entire opposite-parity field to fix the targets in
(1). Applying (3) in each direction and taking the smaller bound gives
\[
 \Pr(\text{specified cycle heights})
 \le {h^{o(1)}\over h\max(Q_0,Q_1)}.                     \tag{4}
\]
The two bounds are not multiplied.

An actual P edge has horizontal span less than \(h\). A fixed-length
cycle therefore lies in a rank interval of length \(O_k(h)\). Hilbert
locality places all its raw cells within coordinate distance
\[
 H=C_k\sqrt h                                                   \tag{5}
\]
of the first cell. For any fixed rank tuple, factorization of the fixed
nonzero horizontal legs gives only \(h^{o(1)}\) possible tuples of
signed P heights. All these divisor choices precede the row sampling.

The statements allow a fixed finite union of bounded-error genuine
central provenance forms. A raw cell must have bounded multiplicity.
Bounded copies of one object are excluded as actual P neighbors by the
usual own-gap cutoff tending to infinity. Arbitrary cap forms, anchor
objects, and growing cycle lengths are not included.

## 2. A small product in either parity is enough

For every \(T\ge1\),
\[
 \mathbb E\#\{\text{central \(k\)-cycles}:
                   \min(Q_0,Q_1)\le T\}
             \le h^{1+o(1)}T.                         \tag{6}
\]

It suffices to impose \(Q_0\le T\). Translate the first raw cell to the
origin. Sorting the first-coordinate values and recording the location
of the distinguished zero leaves only \(O_k(1)\) orders. The number of
nonnegative gap tuples satisfying
\(\prod_\nu(1+d_\nu)\le T\) is
\[
 O_k\bigl(T(1+\log T)^{k-2}\bigr).                     \tag{7}
\]
This is the elementary summatory divisor bound, proved by induction
using \(\sum_{n\le T}1/n\le1+\log T\).

Condition on this parity's field, and apply the other parity's estimate
in (3). The sum over its coordinate gap tuples is bounded by
\[
 \sum_{0\le d_1,\ldots,d_{k-1}\le 2H}
       {1\over\prod_\nu(1+d_\nu)}
       =O_k(\log^{k-1}(2h)).                           \tag{8}
\]
There are \(O(h^2)\) first cells and \(h^{o(1)}\) height tuples for each
rank tuple. Equations (3), (7), and (8) give (6). We have counted a
superset of the actual Hilbert rank tuples, so no distributional
independence of Hilbert coordinates is used.

If one parity uses at most two distinct raw coordinates, the number
of its gap tuples is only \(O_k(H)\): at most one sorted gap is nonzero.
The same proof yields
\[
 \mathbb E\#\{\text{central \(k\)-cycles with at most two
                 raw coordinates in one parity}\}
             \le h^{3/2+o(1)}.                         \tag{9}
\]
For one distinct coordinate, the bound is \(h^{1+o(1)}\).
In particular, a four-cycle on the corners of an arbitrary raw
coordinate rectangle is already covered by (9). The rectangle need
not lie in one local permutation tile; no P two-cycle removal is used.

## 3. The arithmetic high-product bound

The all-direction arithmetic count for fixed \(k\) is
\[
 \#\{\text{rank and signed-height candidates}\}
                 \le h^{k/2+2+o(1)}.                  \tag{10}
\]
Choose the first object in \(O(h^2)\) ways and the second in \(O(h)\)
ways. The first signed height has divisor-many choices. On consecutive
cycle edges, the signed heights differ by \(O_k(\sqrt h)\), by locality
within each parity. Each of the next \(k-2\) heights therefore has
\(O_k(\sqrt h)\) choices; its norm factorization gives divisor-many
horizontal legs and fixes the next column. The closing edge has only
divisor-many signed heights. This proves (10) without a fixed direction
palette.

Combining (4) and (10),
\[
 \mathbb E\#\{\text{central \(k\)-cycles}:
                    \max(Q_0,Q_1)>T\}
              \le {h^{k/2+1+o(1)}\over T}.             \tag{11}
\]
Thus for four-cycles, any fixed \(\epsilon>0\) leaves only
\[
 h^{1-\epsilon}<Q_0,Q_1\le h^{1+\epsilon}              \tag{12}
\]
outside a family of expected size \(h^{2-\epsilon+o(1)}\).
This sharpens the location of the elementary \(h^2\) barrier; it does
not yet improve the total four-cycle count.

## 4. The genuine minimum gap removes small coordinate extents

Suppose the preceding genuine-source cleanup guarantees that every
surviving actual P edge has fine rank gap at least
\[
                         q_*(h)=h^{1-o(1)}.           \tag{13}
\]
Assume the fine order is obtained from the fixed Hilbert order by a
bounded expansion and bounded-size permutations, as in the reviewed
scaffold. Any aligned raw Hilbert square of side \(L\) occupies a
contiguous interval of \(L^2\) raw ranks. Consequently the fine rank
diameter of all its objects is at most \(C(L^2+1)\), with fixed \(C\).

Choose a dyadic \(L=h^{1/2-o(1)}\) with
\(C(L^2+1)<q_*(h)\). No surviving P edge can have both endpoints in
one such square. If an edge has both raw coordinate differences at most
\(D<L/3\), its first cell must lie within distance \(D+O(1)\) of an
aligned grid boundary. Otherwise both endpoints lie in the same square.
Rotate the ordered cycle to put this edge first, costing only \(k\)
choices. In particular this applies when the cycle's two coordinate
extents are at most \(D\).
The number of eligible first cells is at most
\[
 C N^2{D+1\over L}.                                    \tag{14}
\]
This restriction is deterministic, independent of the sampled row
fields. It applies only as a necessary condition for surviving cycles;
all other cleanup conditions may be discarded in upper bounds.

Every bound in Sections 2--3 was obtained by first choosing that first
raw cell. Restricting this choice by (14) multiplies both the low-product
and the arithmetic high-product estimates by
\((D+1)/L\). For four-cycles take \(T=h\): (6) covers
\(\min(Q_0,Q_1)\le h\), and (11) covers its complement. Therefore
\[
 \mathbb E\#\{\text{surviving central four-cycles having an edge
              with both raw coordinate differences}\le D\}
       \le h^{2+o(1)}{D+1\over L}.                    \tag{15}
\]
For every fixed \(\epsilon>0\), choosing
\(D=h^{1/2-\epsilon}\) gives \(h^{2-\epsilon+o(1)}\).

Thus a remaining critical four-cycle has, up to arbitrarily small
fixed exponent margins, both product gaps of order \(h\) and at least
one raw coordinate extent of order \(h^{1/2}\). In fact each cycle edge
must change at least one raw coordinate by that order. This is compatible with
several tight coordinate clusters. No assertion is made that such
clusters are impossible, P-realizable, or removable by a local matching.

## 5. Limits and next target

The useful next target is the interaction between the two sorted
coordinate orders in the range (12), with a large extent as above.
The separate-parity kernel (4) forgets this interaction. A joint
sampling estimate that uses independent field variables from both
parities could improve it, but would require a proof with target
intervals fixed before the corresponding variables are sampled.

All conclusions here concern a fixed number of genuine central
objects. They leave forced singleton paths, cycles through caps or
anchors, and safe occupancy-preserving repair outside their scope.

Independent review: the complete written note passed a separate review
of the fixed-length sampling, low-product harmonic sum, repeated
coordinates, arithmetic height count, and the one-short-edge
minimum-gap refinement. The four-cycle barrier described here is
subsequently resolved at the incidence level by
[the mixed-tree and close-height argument](continuation_central_four_cycle_bound.md).
