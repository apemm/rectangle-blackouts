# A total order from Hilbert cross ranks

15 November 2026. The inverse Hilbert rank has a strict cross-comparison
order on all coordinate pairs. This rules out balanced row and column
sums in every nontrivial square rank submatrix, and excludes the exact
opposite-leg cancellation pattern for three paired edge types. A
quantitative form is stable under controlled coordinate and rank errors.
It is not a general six-cycle exclusion.

## 1. The cross-comparison order

Let \(R_N(x,y)\) be the inverse rank of the standard Hilbert order on
\(\{0,\ldots,N-1\}^2\), with \(N\) a power of two. Define, for
distinct coordinate pairs \(p=(a,b)\), \(q=(a',b')\),
\[
                    p\prec q
             \quad\Longleftrightarrow\quad
                    R_N(a,b')<R_N(a',b).             \tag{1}
\]
Then \(\prec\) is a strict total order.

Here is an induction proof. At side two the Hilbert quadrant digits are
\[
 q(0,0)=0,\quad q(0,1)=1,\quad q(1,1)=2,\quad q(1,0)=3.
\]
If the top bits of the two first coordinates differ, both cross ranks
whose first coordinate has bit zero precede both with bit one. If these
bits agree, comparison of the second-coordinate bits reverses within
the first-coordinate-zero half and preserves order within its one half.
Thus different self-quadrants are strictly ordered
\[
                         01\prec00\prec10\prec11.   \tag{2}
\]
This top-digit comparison is independent of the lower bits.

Inside one self-quadrant, both cross points belong to the same Hilbert
quadrant. Its recursive coordinate map is an affine symmetry of the
smaller square. If that map does not swap coordinates, the cross
comparison is exactly the smaller-square comparison of the transformed
self-pairs. If it swaps coordinates, it is the reverse of that
comparison: the first cross point becomes \((A',B)\), while the second
becomes \((A,B')\). Reflections in either coordinate merely transform
the pairs bijectively. By induction each self-quadrant therefore has a
strict total order, possibly reversed. Concatenating them in (2) proves
the claim. The base case \(N=1\) is vacuous.

This proof permits repeated first coordinates or repeated second
coordinates; only identical self-pairs are excluded from a strict
comparison.

## 2. No balanced square rank submatrix

Take distinct first coordinates \(a_1,\ldots,a_m\) and distinct second
coordinates \(b_1,\ldots,b_m\), with \(m\ge2\). The multiset of row
sums of \((R_N(a_i,b_j))\) differs from its multiset of column sums.

Suppose otherwise, and match each row sum to an equal column sum by a
permutation \(\pi\). Apply (1) to the self-pairs
\(p_i=(a_i,b_{\pi(i)})\), and choose their least member \(p_m\).
For every \(j\ne m\),
\[
                R_N(a_m,b_{\pi(j)})
                    <R_N(a_j,b_{\pi(m)}).
\]
Sum these inequalities and add the common diagonal entry. The row sum
at \(a_m\) is strictly less than the column sum at \(b_{\pi(m)}\),
contradicting their match.

The same proof works for multisets of coordinates whenever the matched
self-pairs are not all identical, but the distinct-coordinate statement
is sufficient here.

## 3. A quantitative deficit

The standard Hilbert locality bound gives
\[
 \max(|x-x'|,|y-y'|)^2
                    \le16|R_N(x,y)-R_N(x',y')|.      \tag{3}
\]
For completeness, choose the least \(q\) with \(4^q\) at least the
positive rank gap. The intervening rank interval meets at most two
consecutive level-\(q\) blocks. Their coordinate squares are adjacent,
so the maximum coordinate difference is below \(2^{q+1}\).
For \(q\ge1\), \(4^{q+1}<16\) times the rank gap; the one-step
case is immediate.

For the least self-pair \(p_m\), every cross-rank difference has the
same positive sign. Hence its column-minus-row deficit is at least
\[
 \sum_{j\ne m}\bigl[R_N(a_j,b_m)-R_N(a_m,b_j)\bigr]
       \ge {1\over16}\sum_{j\ne m}\|p_j-p_m\|_\infty^2.       \tag{4}
\]
If the diameter of the self-pair set is \(D\), one member is at
distance at least \(D/2\) from \(p_m\). Thus some matched deficit is
at least \(D^2/64\). This remains an obstruction if each displayed
rank is perturbed by a uniformly bounded amount: for fixed \(m\), the
perturbation of the deficit is only a fixed multiple of that amount.

## 4. Three paired edge types with opposite legs

Consider six distinct objects in direct Hilbert rank order. Suppose their
edge-coordinate points \((i_v,j_{v+1})\), in cyclic order, consist of
three types \(A,B,C\), each appearing twice. Each type has its own
first-coordinate value and its own second-coordinate value, distinct
from the values of the other types. Suppose also that the two signed
horizontal rank increments belonging to each type sum to zero.

Write \(g_v\) for the type of edge \(v\). Object \(v\) then has raw
cell \((i_{g_v},j_{g_{v-1}})\). Adjacent equal edge types would have
opposite consecutive increments and return to the same column after two
steps, which is impossible for six distinct objects. A repeated directed
type transition would repeat the same raw object. Thus the six
transitions are exactly all six directed nonloop transitions among
\(A,B,C\).

For each type \(t\), cancellation of its two increments now reads
\[
        \sum_{u\ne t} R_N(i_u,j_t)
                     =\sum_{u\ne t}R_N(i_t,j_u).    \tag{5}
\]
These are the matched row/column-sum equalities of a three-by-three rank
submatrix. Section 2 rules them out. The conclusion needs no norm
equations: it excludes this horizontal cancellation geometry before
testing Pythagorean lengths.

It does not exclude unequal representations of a shared P height whose
signed horizontal increments fail to cancel pairwise.

## 5. A stable version for small edge-type clusters

Here is an explicit conditional extension. Let actual scaled column
coordinates be
\[
                       z_v=R_N(i_v,j_v)+e_v,
                       \qquad |e_v|\le J,            \tag{6}
\]
where \(J\) is fixed. A fixed overall column scale is suppressed.
Assume every surviving P edge has \(|z_{v+1}-z_v|\ge q_*\), with
\(q_*=h^{1-o(1)}\). Suppose six edge indices can be partitioned into
three pairs of types, whose edge-coordinate points are within distance
\(r\) of three integer raw-grid centers \((I_t,J_t)\). Centers can be
rounded inside the grid at a cost of at most one in \(r\). Assume the two signed horizontal
increments of each type cancel exactly.

Choose dyadic scales \(L,H_0\) satisfying
\[
 r\ll L\ll H_0,\qquad H_0^2+2J<q_*.
\]
Remove genuine objects in either of these deterministic raw-grid strips:

* distance at most \(2r+2\) from a side-\(L\) tile boundary;
* distance at most \(C L\) from a side-\(H_0\) tile boundary, for a
  sufficiently large fixed constant \(C\).

There are at most
\[
                 C'N^2\left({r+1\over L}+{L\over H_0}\right)  \tag{7}
\]
removed objects. They are a prescribed label set; safe erasure and
relocation remain separate requirements.

After this removal, the stated six-cycle cancellation pattern is
impossible. To prove this, adjacent occurrences of the same type are
excluded as before. Up to cyclic rotation and renaming, a double-occurrence
word on three types with no equal neighbors has either all opposite
positions paired, namely \(ABCABC\), or all six directed transitions
distinct. Indeed, if some type occurs two steps apart, write the word
\(ABA\cdots\); avoiding adjacent equal types forces the remaining
three positions to be \(CBC\). If no pair is two steps apart, all pairs
are three steps apart.

In the \(ABCABC\) case, objects \(v\) and \(v+3\) are within
\(2r\) in both raw coordinates, so the first boundary exclusion puts
them in the same side-\(L\) tile. Therefore their \(z\)-coordinates
differ by at most \(L^2+2J\). Opposite increments imply
\(z_v+z_{v+3}\) is independent of \(v\). Hence all six \(z\)'s lie
in an interval of length \(L^2+2J\), contradicting the minimum P gap.

In the distinct-transition case, replace each object by its reference
cell \((I_{g_v},J_{g_{v-1}})\). The first boundary exclusion puts each
actual and reference cell in one side-\(L\) tile, so its \(z\)-value
differs from the reference Hilbert rank by at most \(L^2+J\). Thus
the three cancellation equalities (5) hold for the reference ranks with
error at most \(4(L^2+J)\).

If the center diameter is \(D\), (4) forces
\(D^2\le256(L^2+J)\). Consequently all six actual raw cells have
coordinate extents at most \(C_1L\), for a fixed \(C_1\). The second
boundary exclusion, with \(C>C_1+2\), puts them in one side-\(H_0\)
tile. Their column span is then at most \(H_0^2+2J<q_*\), another
contradiction. If two center coordinates coincide, the same quantitative
cross-order argument still applies unless all centers coincide; in that
last case the small-diameter conclusion is immediate.

For \(r=h^{o(1)}\), choose \(H_0=h^{1/2-o(1)}\) under the stated
minimum-gap bound and \(L\asymp\sqrt{(r+1)H_0}\). The deterministic
set (7) has size \(h^{7/4+o(1)}\). More generally, radius
\(r=h^\delta\), fixed \(0\le\delta<1/2\), gives
\(h^{7/4+\delta/2+o(1)}\). This eliminates the exact pairwise
horizontal cancellation branch of that clustered six-cycle problem,
not all near-equal-height norm representations.

## 6. Verification and scope

The recursive cross-comparison proof was checked independently. A
separate exact checker,
[check_hilbert_cross_order_independent.py](check_hilbert_cross_order_independent.py),
compares an iterative Hilbert rank table against an independently
recursive cross-order key. Its saved
[results](check_hilbert_cross_order_independent.json) report all 558,558
pair comparisons through side 32 passing. This is a check of the
recursion, not a substitute for the induction.

An earlier exploratory enumeration found no balanced three-by-three rank
submatrix at sides 4, 8, and 16; Section 2 now proves its absence for every
side and every square size. The six-cycle consequences concern the
explicit cancellation and provenance hypotheses above. Neither an
arbitrary P six-cycle nor a complete blackout construction has been ruled
out or constructed.

The complete saved proof passed an independent written review, including
the inverse-locality constant, all-size row/column-sum obstruction, the
two possible three-pair words, the common-center argument, both boundary
strips, and their optimized count. The integer-center requirement above
records a clarification from that review.
