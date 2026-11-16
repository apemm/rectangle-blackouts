# Physical square packs and a Hall extension rule

15 November 2026. The common-index triangular scaffold can retain complete
physical \(4\times4\) label tiles. This preserves constant-stride locality
and full occupancy. After the growing short-P exclusion, each tile pair has
at most two P arithmetic types per parity role. A tile can always be assigned
after its predecessors if at most two types come from those predecessors.

The last condition is a sufficient condition, not a proved property of the
whole constraint graph. No simultaneous full-board construction follows yet.

## 1. Retain complete physical packs

Use the profile, common physical index range, and square filters in
[`continuation_common_index_occupied_scaffold.md`](continuation_common_index_occupied_scaffold.md).
Instead of retaining individual common-good indices, partition physical
indices into aligned packs
\[
 \{4k,4k+1,4k+2,4k+3\}.
\]
Retain a pack only if all four indices are common-good. Discard the at most
two incomplete packs at the ends of the common range.

There are \(O(\sqrt h)\) bad packs. A fixed larger bulk margin also gives a
constant upper bound on consecutive bad packs. To see this directly, let
\(B\) be the number of square tests after testing both physical row classes.
Make the margin absorb the largest filter parameter \(J_{\max}\), and large
enough that solutions of each individual test differ
by more than \(4D(B+1)\). Among \(B+1\) consecutive packs, each test
then removes at most one index and hence spoils at most one pack. At least
one whole pack remains.

List the retained pack origins as
\[
 w_0<w_1<\cdots<w_{n-1},\qquad 4\mid w_i.
\]
For an absolute constant \(G\),
\[
 4(j-i)\le w_j-w_i\le4G(j-i)\quad(i<j),\qquad
 n=h/(4D)-O(\sqrt h)-O(1).                                  \tag{1}
\]
The product of pack \(i\) and pack \(j\) is the genuine physical tile
\[
 \{(w_i+u,w_j+v):0\le u,v\le3\}.                            \tag{2}
\]
Every label in (2) is one-label-safe for the fixed profile. Discarding labels
outside the product of retained packs costs \(O(h^{3/2})\) labels.

## 2. Macrotriangle locality allows arbitrary tile permutations

Order the macrotiles \((i,j)\) in either triangle \(j-i\ge c\) or
\(i-j\ge c\) using the triangle order with constant 49. Each macrotile
receives sixteen consecutive arithmetic slots. Within each tile, choose any
permutation of its sixteen labels. Every arithmetic slot is occupied.

Let two labels have final slot-rank distance \(d\ge1\), and let their
macrotiles have rank distance \(t\). If \(t=0\), either physical index
changes by at most three. If \(t=1\), the macrotriangle path's consecutive
points differ by at most one in each coordinate. Equation (1) gives a
physical index change at most \(4G+3\le7G\). Thus its square is at most
\(49G^2d\).

For \(t\ge2\), the macrotriangle locality gives physical index change at
most \(28G\sqrt t+3<32G\sqrt t\), while
\[
 d\ge16t-15\ge8t.
\]
In every case the squared same-parity physical row displacement obeys
\[
 Y^2<128D^2G^2d.                                             \tag{3}
\]
Choose a fixed power of two \(\sigma\ge8G^2\) and put
\(S=8D^2\sigma\). Then (3) implies \(Y^2<2Sd=2|X|\), for every
choice of the within-tile permutations. Full occupancy removes FW exactly
as in the common-index scaffold.

## 3. Growing short-P exclusion still works

If a pair of slots has distance at most \(Q\), its macrotiles have rank
distance at most
\[
 T_Q=\left\lceil Q/16\right\rceil.
\]
In the upper triangle the even pack index of either label exceeds the odd
pack index of the other by at least \(c-7\sqrt{T_Q}\). The internal
physical offsets \(u,v\in\{0,1,2,3\}\) cost at most three. Hence both
directed cross-row gaps exceed the maximum possible P vertical leg whenever
\[
 4Dc>|b_0-a_0|+D\bigl(28\sqrt{T_Q}+3\bigr)+S^2Q^2/4-1.       \tag{4}
\]
The lower triangle has the same conclusion with signs reversed.

Taking the least integer \(c\) in (4) costs \(O(hQ^2+h)\) labels.
The same choice
\[
 Q(h)=\left\lfloor\frac{\eta\sqrt h}{T(h)\log(2h)}\right\rfloor
 =h^{1/2-o(1)}
\tag{5}
\]
therefore preserves the \(O(h^2)\) total budget, with \(o(h^2)\) internal
relocation cost. Here \(T(h)^2\) is the factor in the cited positional
relocation estimate, not a suppressed constant.

For large enough \(h\), \(Q(h)>15\). Thus every individual tile is already
internally P-free under every permutation. This conclusion covers every H7
residue pair; it does not require the separate sixteen-label local theorem
for bases 1 and 28.

## 4. At most four long-P types per tile pair

Assume \(S>18D^2\), which can be incorporated into the fixed choice of
\(\sigma\). Apply
[`continuation_long_p_tile_pair_bound.md`](continuation_long_p_tile_pair_bound.md).
The horizontal and vertical candidate ranges for a fixed tile-pair role have
widths at most \(30S\) and \(6D\). The integer-cone lemma implies that
once \(Sq>100(30S+6D)^8\), at most two distinct Pythagorean vectors occur
in that role. Since (5) tends to infinity, every remaining candidate
eventually satisfies this condition.

There is also only one sign of the vertical difference in a fixed role's
candidate window. Indeed, an integer hypotenuse at horizontal length \(X\)
requires \(Y^2\ge2X+1\), so at the displayed threshold \(Y>3D\).
A signed row-difference interval of length \(6D\) cannot contain both a
positive and a negative candidate of magnitude greater than \(3D\).

Consequently each P vector determines one signed cross-index difference,
not two. There are at most two types per role, hence at most four types
between an unordered pair of tiles. A type consists of a fixed physical
slot offset and a fixed difference between one row index of each tile.
The slot relation is a partial matching between the sixteen slots. The row
relation is a partial translation between the four row indices.

This arithmetic sparsity is uniform in height. It does not give a bound on
the number of other tiles adjacent to one tile.

## 5. An extension lemma for square-tile permutations

Consider one tile with labels \((i,j)\in\{0,\ldots,k-1\}^2\), to be put
bijectively in \(k^2\) slots. Assume all earlier tiles have already been
assigned. A constraint type is allowed here if:

1. its slot relation to a fixed earlier tile is a partial matching;
2. its row relation constrains one coordinate of the current label against
   one coordinate of the earlier label;
3. that row relation is a partial bijection between the \(k\) row values.

Fixed signed P types have these properties. A fixed same-parity row-difference
type also has them, irrespective of whether it came from P or another
pair-support overgraph.

Suppose at most \(t\le\lfloor k/2\rfloor\) types constrain the new tile.
Then a bijective assignment avoiding all of them exists.

Form the bipartite graph between labels and slots, with an edge for an
allowed placement. Fix one label. Under one type, the required earlier row
value appears in at most \(k\) of the earlier tile's labels. The partial
slot matching therefore forbids at most \(k\) current slots. Every label
has at least
\[
 k^2-tk\ge k^2/2                                             \tag{6}
\]
allowed slots.

At one current slot, a type forbids at most one value of one label coordinate.
If \(t_1\) types concern the first coordinate and \(t_2\) the second,
at least
\[
 (k-t_1)(k-t_2)
 \ge k(k-t_1-t_2)\ge k^2-tk\ge k^2/2                       \tag{7}
\]
labels remain. Multiple types can repeat a forbidden value, which only
improves this estimate.

A balanced bipartite graph on \(N+N\) vertices with minimum degree at least
\(N/2\) has a perfect matching. For completeness, a left subset of size
at most \(N/2\) has at least that many neighbors. If a larger subset had
fewer neighbors than vertices, a vertex outside its neighborhood would have
degree less than \(N/2\). This is Hall's condition. Equations (6)–(7)
therefore give the desired permutation.

For \(k=4\), any two previously assigned arithmetic types can be absorbed,
regardless of their parity roles and regardless of the earlier permutations.
In particular, if the graph of remaining typed constraints has an ordering
in which each tile meets at most two types from earlier tiles, all tiles
can be assigned successively while preserving complete occupancy.

The cone bound gives at most four types *per tile pair*. It does not imply
this weighted-degeneracy condition. Establishing such an ordering, using
more of the relation structure, or finding a different simultaneous rule
remains open. Higher-arity supports involving several labels of the current
tile are not covered by the extension lemma.

## 6. Three types extend when both coordinates occur

For a \(4\times4\) tile, three earlier types are always absorbable if two
concern one coordinate and the third concerns the other. This improves the
untyped two-type rule. It holds for arbitrary earlier assignments and for the
same partial-matching/partial-bijection hypotheses.

Assume that two types concern the first coordinate. At each slot at least
two first-coordinate values and at least three second-coordinate values
remain. One first-coordinate value can be forbidden at no more than eight
slots in total; one second-coordinate value can be forbidden at no more
than four slots. One fixed label can therefore be forbidden at no more than
twelve slots.

To verify Hall from the slot side, take a nonempty slot set \(U\), let
\(u=|U|\), and let \(V\) be the union of its allowed labels. If \(V\)
contains all sixteen labels there is nothing to prove. Otherwise an absent
label is forbidden at every slot of \(U\), so \(u\le12\).
Let \(r\) be the number of first-coordinate values represented in \(V\).
Every slot permits at least two such values, so \(r\ge2\).

- If \(r=4\), each represented value appears with at least three second
  values, so \(|V|\ge12\ge u\).
- If \(r=3\), the omitted first-coordinate value is forbidden throughout
  \(U\), so \(u\le8\), while \(|V|\ge9\).
- If \(r=2\), both represented first-coordinate values are allowed at
  every slot of \(U\). The omitted values give \(u\le8\). For \(u\le6\)
  the six labels at any one slot suffice. If \(u>6\), the single
  second-coordinate type cannot forbid a fixed value throughout \(U\),
  because it forbids that value at at most four slots. Thus both represented
  first-coordinate values occur with all four second values, giving
  \(|V|=8\ge u\).

Hall's condition follows. Interchanging the two coordinates covers the other
mixed-role split. A successive construction therefore works if every tile
has either at most two earlier types, or exactly three earlier types with
both coordinate roles represented.

The role condition cannot be removed from this abstract lemma. Here are
three full slot-matching types, all concerning the first coordinate. Their
forbidden first-coordinate values in the sixteen slots are
\[
\begin{array}{c|cccc|cccc|cccc|cccc}
1&2&2&3&3&0&0&0&0&1&1&1&1&2&2&3&3\\
2&2&2&3&3&1&1&1&1&2&2&3&3&0&0&0&0\\
3&2&2&3&3&2&2&3&3&0&0&0&0&1&1&1&1.
\end{array}
\]
Each row contains every value four times and hence is the coordinate word
of a valid earlier tile permutation. Use identity row bijections and
identity slot matchings. In each of the final twelve slots, both values
0 and 1 are forbidden. The eight current labels with first coordinate
0 or 1 would therefore have to fit in the first four slots. This violates
Hall. It is an exact obstruction to a universal three-same-role extension
rule for abstract types; no geometric realization by P candidates is claimed.

Independent review: the physical-pack count, locality constant 128, growing
short-P cutoff, and two-type Hall lemma passed separate proof audits. The
mixed-role three-type lemma was derived independently by two readers; its
same-role counterexample records the limit of the abstract assertion.
