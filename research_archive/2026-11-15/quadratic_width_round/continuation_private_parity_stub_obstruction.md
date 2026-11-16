# Nonempty odd/even stubs cannot fill every private slot

15 November 2026. The proposed all-even private-slot filler fails.
Allowing each unused slot to choose the odd or even row does not
repair it in general. An explicit Hilbert pair defeats every such
filler for every fixed private palette size \(M\), including the
H7 row step.

The obstruction is a directed two-cycle of zero-offset P constraints.
It does not come from losing occupancy or same-parity locality.

Independent review checked the directed-path criterion, both Hilbert
orientations, all four owners, the midpoint rows, and the bulk scope.
The companion checker passes 3114 local assignments in nine cases.

## 1. The zero-offset subsystem has an exact order interpretation

Label \(r\) has odd row \(a_r\), even row \(b_r\), and private
columns
\[
 S(Mr+t),\qquad 0\le t<M.
\]
At each private slot choose a nonempty subset of its two rows.
Every label must have both rows present in at least one private slot.

Make a directed graph on labels, with \(r\to s\) when the
zero-offset cross-pair satisfies
\[
 [SM(s-r)]^2+(b_s-a_r)^2=L^2.
\tag{1}
\]
Here \(r\ne s\), and the graph records the P exclusions under
consideration. At any fixed offset \(t\), exclusion of this type
requires that the odd row at \(r\) and even row at \(s\) are
not both present.

For this subsystem alone, nonempty private-slot fillings with a
double at every label exist if and only if the directed graph is
acyclic and its longest directed path has at most \(M\) vertices.

To prove necessity, suppose a label has both rows at offset \(t\).
Every successor along a directed path must then carry only its odd
row at that offset. Thus no successor can also be double there.
A directed cycle would forbid its labels from being double at any
offset. On a directed path, at most one label can be double at each
offset, so the path has at most \(M\) vertices.

Conversely, in an acyclic graph let \(\ell(r)\) be the number of
vertices in a longest path ending at \(r\). At offset \(t\),
numbered \(1,\ldots,M\), put only the even row when
\(\ell(r)<t\), both rows when \(\ell(r)=t\), and only the odd
row when \(\ell(r)>t\). Every edge has
\(\ell(r)<\ell(s)\), so (1) never has both forbidden endpoints.

For an all-even filler, the obstruction is still simpler: the target
even row exists at every offset, so any outgoing edge (1) forbids
every possible double position of its odd source.

This is a statement about the selected P subsystem. Genuine rectangle
collisions require in-strip completions and an available owner.
The next section supplies those conditions uniformly over all choices.

## 2. A directed two-cycle for every M

Use an even row step \(D\), bases 1 and \(D\), and a stride
\(S\) such that
\[
 D_0=\frac{(SM)^2}{8D}
\]
is an even integer at least two. This includes every \(M\ge1\)
for \(D=2,8\mid S\), and for \(D=28,S=6272\sigma\).

Choose a large macro Hilbert square and an even anchor \(K\).
The macro-cells \((K,D_0+K)\) and
\((K+1,D_0+K+1)\) have opposite terminal orientation classes.
One has class \(\{I,\alpha\}\), where
\(\alpha(x,y)=(7-y,7-x)\) on a side-eight square. Refine that
cell to a side-eight block with origin \((I,J)\) and rank start
\(B\). Then
\[
 J-I=(SM)^2/D.
\tag{2}
\]

In identity orientation, labels \(A,B'\) at local ranks 2 and 4
have cells
\[
 A=(I+1,J+1),\qquad B'=(I+2,J).
\]
Their two directed cross-row differences are equal:
\[
 b_{B'}-a_A=b_A-a_{B'}=D(J-I)-1=(SM)^2-1.
\]
Both directions therefore satisfy
\[
 X=2SM,\qquad Y=(SM)^2-1,
 \qquad L=(SM)^2+1,
 \qquad X^2+Y^2=L^2.
\tag{3}
\]

In orientation \(\alpha\), the two cells are
\[
 A=(I+6,J+6),\qquad B'=(I+7,J+5).
\]
Again both cross differences equal \(D(J-I)-1\), so (3)
holds in both directions. This gives a directed two-cycle for every
\(M\), without restricting the parity of \(M\).

## 3. Both alternatives are genuine under every filler choice

Choose any private offset \(t\) where \(A\) is double. The
same-offset slot of \(B'\) is nonempty. If it contains the even
row, use \(A\to B'\); if it contains only the odd row, use
\(B'\to A\). In either case the black endpoints have (3), and
their midpoint column is
\[
 S\bigl(M(B+3)+t\bigr).
\tag{4}
\]

The common rows and their owners are as follows:

| Orientation and edge | Common rows | Owner \((i,j)\) |
|---|---|---|
| Identity, \(A\to B'\) | \(D(I+1),\ 1+D(J+1)\) | \((J+1,I)\) |
| Identity, \(B'\to A\) | \(D(I+2),\ 1+D(J+2)\) | \((J+2,I+1)\) |
| \(\alpha\), \(A\to B'\) | \(D(I+6),\ 1+D(J+6)\) | \((J+6,I+5)\) |
| \(\alpha\), \(B'\to A\) | \(D(I+7),\ 1+D(J+7)\) | \((J+7,I+6)\) |

The midpoint belongs to private block \(B+3\). Its available
rows are \(1+D(I+1),D(J+1)\) in identity orientation, and
\(1+D(I+7),D(J+7)\) in orientation \(\alpha\). Neither
common row appears there, for either edge, regardless of which
nonempty subset is used in that slot.

Every owner lies outside the whole side-eight block, since
\(J-I\ge16\). It is double at some private slot outside (4).
Its two black points and the common corners form an axis rectangle,
while the selected cross-pair forms a tilted rectangle with the same
presentation. Additional black fillers cannot separate the two
presentations.

All rows fit in a sufficiently large padded square. Increasing the
even anchor \(K\) and the upper padding puts all source and owner
rows beyond any prescribed fixed boundary margin. Thus the result
also has a bulk H7 realization.

## 4. Scope and consequences

The filler retains the original same-parity locality estimate. For
distinct labels at original rank distance \(d\), any two private
slots differ by at least
\[
 Md-(M-1)\ge d.
\]
Repeated stubs from one label lie on one horizontal row. The failure
is therefore caused by the two directed P relations, not a loss of
the original geometric exclusions.

For fixed \(S,M\), this explicit pair has bounded rank gap.
A growing short-P deletion can remove this particular pair. The
all-even inheritance mechanism also applies to long zero-offset
P edges from the translated-density construction, with base stride
\(SM\). The existence of a surviving long directed cycle after
all proposed deletions is a separate question.

Allowing empty private slots, different filler rows, or moving the
relevant doubles out of these blocks is outside the obstruction.
For nonempty stubs restricted to the label's own two rows, however,
acyclicity and bounded directed-path height are necessary even before
the nonzero-offset and higher-support constraints are considered.
