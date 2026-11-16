# A role-sensitive extension theorem for occupied square tiles

15 November 2026. A \(4\times4\) tile can always absorb three previously
assigned arithmetic constraint types when their current-coordinate roles
split \(2+1\). More generally, the following sufficient inequalities retain
the role counts separately instead of using only their sum.

## 1. Precise statement

There are \(k^2\) labels \((i,j)\in\{0,\ldots,k-1\}^2\), to be
placed bijectively in \(k^2\) slots. Each earlier arithmetic type has:

1. a partial matching between the current slots and an already assigned
   earlier tile's slots;
2. a constraint on one current label coordinate and one earlier coordinate;
3. a partial bijection between the two sets of coordinate values.

Let \(a\) types concern the current first coordinate and \(b\) types concern
the second. A bijective assignment avoiding every type exists if
\[
 k\ge2a,\qquad k\ge a+2b.                                  \tag{1}
\]
The coordinates can be interchanged before applying (1). In particular:

* \(k=4\) permits role counts \((2,1)\) or \((1,2)\).
* \(k=6\) permits \((3,1)\) and \((2,2)\).
* \(k=8\) permits \((4,2)\).
* If \(4\mid k\), counts \((k/2,k/4)\) permit \(3k/4\) earlier types.

These are sufficient conditions. They do not bound how many types actually
meet a tile in the P graph.

## 2. The two incidence bounds

Make a bipartite graph between current labels and slots, with an edge for
each allowed placement. Put \(N=k^2\).

For a fixed current label and one type, its corresponding earlier row value
occurs in at most \(k\) earlier labels. Their assigned slots pull back
through a partial matching. Thus one type forbids at most \(k\) slots
for that label, and each label has at least
\[
 N-k(a+b)                                                    \tag{2}
\]
allowed slots.

For a fixed current first-coordinate value, one first-coordinate type
forbids that value at at most \(k\) slots. Across all such types, the value
is forbidden at at most \(ak\) slots. The corresponding second-coordinate
bound is \(bk\). At any one slot, at most \(a\) first-coordinate values
and at most \(b\) second-coordinate values are forbidden. That slot therefore
allows at least
\[
 (k-a)(k-b)                                                  \tag{3}
\]
labels.

## 3. Hall's condition

Suppose a label set \(U\) violates Hall's condition. Write \(u=|U|\),
and let \(Z\) be the slots outside its neighborhood, with \(z=|Z|\).
Then
\[
 z>N-u.                                                      \tag{4}
\]
Equation (2) gives
\[
 u>N-k(a+b)\ge kb,
\]
where the last inequality uses \(k\ge a+2b\). Some first-coordinate
row of \(U\) therefore contains more than \(b\) labels. At any slot in
\(Z\), the second-coordinate types alone cannot forbid all of those labels.
Their common first-coordinate value must be forbidden at every such slot.
The incidence bound gives \(z\le ak\), hence
\[
 u>N-ak=k(k-a)\ge ka.                                       \tag{5}
\]
The last inequality uses \(k\ge2a\).

Some second-coordinate column of \(U\) consequently contains more than
\(a\) labels. Its second-coordinate value must be forbidden at every slot
of \(Z\). Thus \(z\le bk\), and
\[
 u>N-bk=k(k-b).                                              \tag{6}
\]
But every slot of \(Z\), which is nonempty by (4), allows at least the
number in (3), all outside \(U\). Therefore
\[
 u\le N-(k-a)(k-b)=k(a+b)-ab.                                \tag{7}
\]
Finally,
\[
 k(k-b)-\bigl(k(a+b)-ab\bigr)
   =k(k-a-2b)+ab\ge0,
\]
contradicting (6)–(7). Hall's theorem supplies the required permutation.

## 4. Consequence for the occupied scaffold

The fixed signed P types in
[`continuation_packed_triangles_and_hall.md`](continuation_packed_triangles_and_hall.md)
have exactly these partial-matching and partial-row-bijection properties.
If the typed tile graph admits an ordering whose earlier role counts satisfy
(1) at every tile, successive applications of this theorem give a joint
assignment of all tile permutations. Complete arithmetic occupancy is
preserved.

This improves the earlier sufficient bound of at most two arbitrary types
for a \(4\times4\) tile. It remains conditional on such an ordering.
The arithmetic result of at most four types per tile pair does not imply
the required earlier-role count. The theorem does not cover constraints
with several current labels or several as-yet-unassigned tiles.

No finite computation or external analytic theorem is used. The only graph
input is Hall's matching criterion, whose obstruction is excluded directly.

Independent review: the complete written proof, including zero role counts
and the conditional scaffold consequence, passed a separate check.

## 5. Prescribed placements can use the slack

Suppose \(p\) distinct labels have already been assigned to \(p\) distinct
slots, and those placements avoid all earlier types. The remaining labels
still admit a bijective assignment if, after possibly exchanging coordinates,
\[
 p\le\min\{k(k-a-2b),\ k(k-2a)\}.                         \tag{8}
\]
The assertion prescribes valid placements, not merely lists of arbitrary
allowed values.

Remove the prescribed labels and slots, and put \(N'=k^2-p\). Each remaining
label has at least \(N'-k(a+b)\) available slots. A Hall obstruction
\(U,Z\) would therefore satisfy
\[
 u>N'-k(a+b)\ge kb.
\]
The first-row argument from Section 3 gives \(z\le ak\), so
\[
 u>N'-ak\ge ka.
\]
The second-coordinate argument then gives \(u>N'-bk\). A slot in \(Z\)
allows at least \((k-a)(k-b)-p\) remaining labels. Consequently
\[
 u\le N'-\bigl((k-a)(k-b)-p\bigr).
\]
This contradicts the preceding strict lower bound, since (8) implies
\[
 (k-a)(k-b)-p-bk=k(k-a-2b)+ab-p\ge0.
\]
The row-resource bounds remain valid after slots are removed, and each
coordinate still has at most \(k\) labels. This proves the claim.

For a \(4\times4\) tile with one earlier type in each coordinate, (8)
allows any four valid prescribed placements. This gives a boundary condition
that a future gluing argument can use. It does not prove that an appropriate
global decomposition or compatible set of boundary placements exists.

Independent review: Section 5 and its four-prescribed-placement corollary
passed a separate check, including the validity and disjointness hypotheses
on the prescribed pairs.
