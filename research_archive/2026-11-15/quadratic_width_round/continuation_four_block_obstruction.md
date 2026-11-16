# Every permutation of one four-label block can force a P-rival

15 November 2026. Consecutive blocks of four do not repair the
full-occupancy Hilbert proposal. One aligned two-square already forces
a genuine P-rival under all 24 permutations. The proof also applies to
an H7 residue block, with the configuration arbitrarily far from the
boundary. It does not assume the earlier excursion decomposition.

Independent review checked the matching proof, the common-corner
whiteness, the owner, and the H7 bulk specialization. A separate run
of the checker passed all 2304 joint block permutations in four cases.

## 1. A four-point matching obstruction

Let four objects be indexed by \(\{0,1\}^2\). Mark the objects with
first coordinate 1 by \(A\), and those with second coordinate 0 by
\(B\). There is one object of each incidence type: both marks,
only \(A\), only \(B\), and neither.

Place the four objects in slots \(0,1,2,3\). The pairs of slots at
distance two form the perfect matching \(\{0,2\},\{1,3\}\).
Every placement has one matched pair whose endpoints carry opposite
marks \(A,B\).

Indeed, the object carrying both marks must be matched to the object
carrying neither mark, or its matched pair already has the required
marks. If those two objects are matched, the other edge matches the
\(A\)-only object to the \(B\)-only object. This proves the claim
for all 24 placements without enumerating them.

## 2. An actual rectangle collision

Let \(D\) be a positive even integer. Label \((i,j)\) has black
rows \(1+Di\) and \(D+Dj\). Every label receives one column,
and the columns are the consecutive arithmetic slots \(Sn\).
Labels may be permuted within their aligned Hilbert rank blocks of
size four.

Assume that \(S^2/D\) is an even integer at least four. Choose even
\(I,J\) with
\[
 J-I=S^2/D.
\tag{1}
\]
The label square
\[
 \{I,I+1\}\times\{J,J+1\}
\tag{2}
\]
is an aligned two-square. Therefore its four Hilbert ranks form one
aligned block \(R,R+1,R+2,R+3\), regardless of its orientation.

Set
\[
 a=1+D(I+1),\qquad b=D(J+1).
\]
In (2), two labels carry row \(a\), two carry row \(b\), and one
carries both. The matching argument supplies black points
\(C,D'\) in these rows at physical slots separated by two. Their
row difference is \(b-a=S^2-1\), and hence
\[
 |CD'|^2=(2S)^2+(S^2-1)^2=(S^2+1)^2.
\tag{3}
\]
If \(x\) is their midpoint column, the vertical diagonal with the
same midpoint and length has endpoints
\[
 P=(x,a-1),\qquad Q=(x,b+1).
\tag{4}
\]
The midpoint is one of the two internal slots of the protected block.
Every label in that block has its odd row in
\(\{1+DI,1+D(I+1)\}\) and its even row in
\(\{D(J+1),D(J+2)\}\). Consequently neither common row in (4)
is black there. The separation in (1) also keeps these row sets
disjoint from the common rows.

The common-row owner is
\[
 (i_*,j_*)=(J+1,I).
\tag{5}
\]
It lies outside the protected square. Its entire rank block is
disjoint from the protected four ranks, so arbitrary permutations
of that other block cannot place the owner at column \(x\).
At the owner's column its two black points, together with \(P,Q\),
form a nondegenerate axis rectangle. Equation (3) gives a second,
tilted rectangle with diagonal \(CD'\) and opposite diagonal
\(PQ\). Both rectangles have presentation \(\{P,Q\}\).

The argument permits all permutations in every other block. Additional
black fillers cannot distinguish the two rectangles: their symmetric
difference consists of the four black points \(C,D'\) and the
owner's two points.

## 3. Full-grid and H7 instances

For the usual full-grid layout, take \(D=2\), a power of two
\(S\ge256\), \(I=0\), \(J=S^2/2\), Hilbert side \(n=S^2\),
and height \(h=2n\). These choices satisfy (1). Stride
\(S\ge32(2\cdot4-1)=224\) retains the earlier same-parity
distance exclusion under four-label permutations. Thus the obstruction
occurs even when that exclusion is preserved.

For H7, take \(D=28\), row bases 1 and 28, and
\[
 S=6272\sigma,\qquad \sigma\ge8\text{ a power of two}.
\]
These strides retain the H7 locality bound for four-label blocks.
Choose any sufficiently large even \(I\), put \(J=I+S^2/D\),
and choose a power-of-two Hilbert side \(n>J+2\). The owner in
(5) then belongs to the same residue block. Increasing \(I\) and
the padding above \(J\) puts every protected label and the owner
outside any prescribed fixed row boundary margin. For the margin
100000, \(I=4000\) and
\[
 n>J+2+\lceil100000/28\rceil
\]
suffice, with height \(h=28n\).

The precise layout hypothesis is that the four protected labels occupy
their original consecutive four slots, in any order, and that their
owner is retained elsewhere. A scheme that cuts through the protected
block or restarts ranks can escape this statement. The theorem does
not rule out permutations of sixteen-label blocks or a different
layout family.

## 4. Exact verification

The companion checker uses forward and inverse Hilbert routines with
different recursions. It verifies the aligned block, examines all 24
permutations, and for each one checks every permutation of the owner's
four-label block. It checks black endpoints, white common corners,
both rectangles, and equal presentations. The proof is the matching
argument; the computation checks the geometric implementation.
