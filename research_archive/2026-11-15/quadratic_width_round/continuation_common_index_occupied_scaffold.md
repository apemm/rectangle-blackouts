# Common-index triangular cores remove FW and bounded-gap P

15 November 2026. The square-filtered H7 row blocks can be replaced by a
constant number of completely occupied triangular runs. This uses the same
good index list for the two row classes. It removes FW and P candidates with
slot gaps up to \(h^{1/4}\), while preserving the same-parity locality
exclusion. The removed labels still number only \(O(h^{3/2})\). Using the
full positional-relocation budget extends the cutoff to
\(h^{1/2-o(1)}\) at quadratic total width, as detailed in Section 6.

This is a conditional construction reduction. Long P, the two label-only
families, R2s, and 6PT remain. The statement does not transfer the old
four-system candidate decomposition to the new ordering.

## 1. Inputs and the exact row set

Use the corrected H7 profile reduction and its cited relocation and gluing
inputs. The relevant sources are
[`hilbert_sea_design_h7.md`](../../2026-11-14/hilbert_sea_design_h7.md),
`audit_hilbert_sea_design_h7.md`,
and the square filters in
[`filled_mod7_profile_cover.md`](../../2026-11-09/full_problem_push/filled_mod7_profile_cover.md),
Section 5. The new ordering and bounded-gap lemma are proved in
[`continuation_hole_free_rectangles_and_triangles.md`](continuation_hole_free_rectangles_and_triangles.md).

Fix one odd/even residue pair modulo \(D=28\). Write its rows as
\[
 a=a_0+Dk,\qquad b=b_0+Dk,
\]
where \(1\le a_0,b_0\le D\), \(a_0\) is odd and \(b_0\) is even.
Choose one corrected AP4 profile for this residue pair. Its rows obey
\[
 L\le28,\quad 2000\le F\le23952,\quad h-H\le783,
\]
the mod-seven conditions, and
\(L\equiv F\equiv a_0+2\), \(H\equiv b_0+2\pmod4\).

First take a common consecutive integer range \(I_h\) on which both
\(a_0+Dk\) and \(b_0+Dk\) lie in a sufficiently deep bulk interval.
The depth is a fixed constant, enlarged below if necessary. Remove from
\(I_h\) every index for which either row fails any of that profile's
one-label square filters. Let
\[
 V_h=\{v_0<v_1<\cdots<v_{n-1}\}
\tag{1}
\]
be the remaining common list. Both physical rows indexed by each \(v_i\)
are safe. Every label in the complete product
\[
 \{(a_0+Dv_i,b_0+Dv_j):0\le i,j<n\}                           \tag{2}
\]
therefore has the required one-label safety for this profile.

The filters are exactly a fixed finite collection of
\[
 j(r-L+j),\quad j(r-F+j),\quad j(H-r+j)
 \quad\text{being squares},                                  \tag{3}
\]
with \(j\le L-1,F-1,h-H\), respectively. Testing both physical rows
only doubles this fixed number of families. The profile choices may vary
with \(h\), but all these bounds remain absolute.

The square-filter gap lemma gives an absolute constant \(G\) such that,
after enlarging the fixed bulk margin,
\[
 i'-i\le v_{i'}-v_i\le G(i'-i)\quad(i<i').                    \tag{4}
\]
Indeed, every fixed test removes at most one member of a sufficiently short
fixed block of candidate indices, once its square argument is sufficiently
large. More explicitly, if there are at most \(B\) tests after testing both
rows, use bulk distance at least
\(C_0+J_{\max}+(D(B+1))^2+1\) from the ambient boundary and take
\(G=B+1\), where \(J_{\max}\) is the largest filter parameter.
Each test also removes only \(O(\sqrt h)\) indices. Consequently
\[
 n=h/D-O(\sqrt h)-O(1).                                      \tag{5}
\]

The labels omitted from the original residue-pair grid have at least one
index outside the common range or outside \(V_h\). There are
\(O(h^{3/2})\) of them. This count includes the extra labels sacrificed
solely to synchronize the two good lists. There is no assertion that the
two independently filtered row lists were initially identical.

## 2. Two genuine occupied runs

Fix constants \(b,Q\ge1\). A block permutation may rearrange labels inside
each consecutive rank block of at most \(b\) labels. Choose a power of two
\(\sigma\) so large that
\[
 \sigma>\frac{49G^2(2b-1)}{16},\qquad S=8D^2\sigma.           \tag{6}
\]
All constants are independent of \(h\). Choose an integer \(c\ge1\)
with
\[
 Dc>|b_0-a_0|+7D\sqrt{(2b-1)Q}
                +\frac{S^2Q^2}{4}-1.                        \tag{7}
\]
For all sufficiently large \(h\), \(n>c\).

Retain the two index triangles
\[
 U=\{(i,j):j-i\ge c\},\qquad
 V=\{(i,j):i-j\ge c\}
\tag{8}
\]
inside \([0,n-1]^2\). Order each by the triangular recursion of the
companion note, and map its coordinates through the common list (1).
Put its labels in the consecutive columns
\[
 x_0, x_0+S, \ldots, x_0+S(N-1),                           \tag{9}
\]
where \(N=(n-c)(n-c+1)/2\). Here \(x_0\) is an allowed period-zero
origin. Every arithmetic slot in (9) contains one genuine double label.
The optional block permutations preserve complete occupancy.

Only \((2c-1)n+O(c^2)=O(h)\) labels of (2) fall in the discarded diagonal
band. Their removal creates no holes because each retained triangle receives
its own freshly indexed full run. This is a new order, rather than a
compression of old Hilbert ranks.

## 3. Locality and short P

The unpermuted triangular order has squared index displacement at most 49
times the rank gap. If two labels occupy ranks differing by \(q\) after
the block permutations, their original ranks differ by at most
\[
 q+2(b-1)\le(2b-1)q.
\]
Using (4), their same-parity physical row difference \(Y\) satisfies
\[
 Y^2\le49D^2G^2(2b-1)q<2Sq=2|X|.                            \tag{10}
\]
Thus the same-parity integer-length exclusion and the same-parity angle and
mixed-support consequences used in H7 remain available. Their hypotheses
use the inequality and the arithmetic slot stride, not the exact Hilbert
recursion. Quantitative thresholds depending on an effective locality
parameter must be recomputed from (10).

For a P candidate with \(q\le Q\), every coordinate index changes by at
most
\(K=7\sqrt{(2b-1)Q}\). In the upper triangle, if one label has indices
\((i,j)\) and the other \((i',j')\), then
\[
 j-i'\ge c-K,\qquad j'-i\ge c-K.
\]
By the lower bound in (4), both directed even-to-odd physical row gaps are
at least \(D(c-K)-|b_0-a_0|\). They exceed \(S^2Q^2/4-1\) by (7).
The same argument, with signs reversed, applies to the lower triangle.
But an odd vertical leg \(Y\) of an integer right triangle with horizontal
leg \(Sq\) must satisfy
\[
 |Y|\le S^2q^2/4-1.
\]
Therefore neither run has any P candidate with \(q\le Q\), in either
cross-parity orientation. This excludes even candidates whose alternative
vertical diagonal would not fit the ambient strip.

The role of the common list is essential: its lower bound in (4) compares
\(v_j\) with \(v_{i'}\) directly. Two unrelated filtered lists do not
have this property without an additional drift estimate.

## 4. Full occupancy removes FW

Consider a parked triangle whose label vertex is \(A=(x_e,y)\), whose other
same-parity label point is \(C=A+(X,\delta)\), and whose sea point is
\(B=A+(\xi,F-y)\). Its completion is
\(W=C+(\xi,F-y)\), and
\[
 X\xi=-\delta(F-y).                                         \tag{11}
\]
If \(W\) belongs to an occupied arithmetic column in the same run, then
\(S\mid\xi\), as well as \(S\mid X\). The H7 alignment gives
\(v_2(F-y)\le1\) and \(7\nmid(F-y)\). Since \(S\) has only prime
factors two and seven,
\[
 S^2/2\mid\delta.                                           \tag{12}
\]
The case \(\delta=0\) forces \(\xi=0\), placing the sea point in
\(A\)'s occupied double column. It is impossible. Since \(F<S^2/2\),
an in-strip completion of row \(F+\delta\) forces \(\delta>0\).
All bulk label rows lie above \(F\), so (11) gives \(X\xi>0\).

The source column \(x_e+\xi\) is therefore strictly between the occupied
columns \(x_e\) and \(x_e+X+\xi=x_W\). It is another arithmetic slot
of the same full run. Its filler point in row \(F\) was removed when its
double label was inserted. Thus \(B\) cannot be black. FW is absent.

This uses complete interval occupancy, not a deletion-monotonicity claim.
Separate runs must still receive the usual collars and separation before
the core-local conclusion is used globally.

## 5. The resulting conditional reduction

There are 196 odd/even residue pairs modulo 28. Apply this construction to
each, with one safe AP4 profile and two full runs. At most 392 ordinary cores
are needed. Each has width \(O(h^2)\), and their total width is \(O(h^2)\)
because their number and the stride are absolute constants. All omitted
labels together number \(O(h^{3/2})\).

Retain the following inputs explicitly:

1. The cited positional relocation result for an arbitrary exceptional
   subfamily of \(n_E\) labels, with width
   \(O((n_E+1)T(h)^2)+O(h^2)\), where \(T(h)=h^{o(1)}\).
2. The corrected H7 one-label theorem and the cited filled collars and
   separation argument, using the full final parity row-pair graph.
3. A choice of the bounded within-run permutations avoiding the remaining
   families \(\mathrm P_{q>Q},\Lambda_3,\Lambda_4,\mathrm{R2s},\mathrm{6PT}\).

Under these inputs, the usual full-board criterion yields width \(O(h^2)\).
Indeed, \(n_E=O(h^{3/2})\) makes the internal relocation cost
\(h^{3/2+o(1)}=o(h^2)\), the constant number of collars costs \(O(h^2)\),
and (10)–(12) remove the previously identified same-parity and FW families.
The collars and separation localize every cross-core support as in the cited
H7 reduction. They are not omitted from the width count.

The remaining hypothesis in item 3 is open. In particular, the new orders
need their own P and mixed-support analysis. The immutable fixed-slot
obstructions from the original Hilbert squares do not automatically embed
after the triangular reordering and synchronized row filtering.

The proved advance is independent of that open hypothesis: arithmetic row
filters, arbitrary non-power-of-two sizes, and a short-P diagonal band
can all be handled with a constant number of genuine fully occupied local
runs. Neither padding holes nor a band-dependent locality constant remains
in this reduction.

## 6. A growing short-P cutoff within the quadratic budget

The proof of Sections 2–4 does not require \(Q\) or \(c\) to remain fixed.
Only the stride \(S\), the permutation block size \(b\), and the filter-gap
constant \(G\) must be fixed. The locality constant is independent of the
triangle's side length and of the removed band. Taking the least integer
\(c=c_h\) that satisfies (7) gives
\[
 c_h=O(Q(h)^2+\sqrt{Q(h)}+1).                                 \tag{13}
\]
Provided \(c_h<n\), the exceptional count becomes
\[
 n_E=O(h^{3/2}+hQ(h)^2+h).                                   \tag{14}
\]

In particular, \(Q(h)=\lfloor h^{1/4}\rfloor\) retains
\(n_E=O(h^{3/2})\). More generally, for any fixed \(0<\epsilon<1/2\),
\(Q(h)=\lfloor h^{1/2-\epsilon}\rfloor\) gives an internal relocation
cost \(h^{2-2\epsilon+o(1)}+h^{3/2+o(1)}=o(h^2)\).

For a near-square-root cutoff with strictly lower-order internal relocation,
take the function \(T(h)\ge1\) appearing in the cited positional estimate
and fix a constant \(\eta>0\) after the stride. For example, take
\(\eta=1/S\), so the leading band constant in (13) does not grow with
\(S\). Put
\[
 Q(h)=\left\lfloor\frac{\eta\sqrt h}{T(h)\log(2h)}\right\rfloor.
\tag{15}
\]
Equations (5) and (13) give \(c_h=o(n)\), hence \(c_h<n/4\) for all
sufficiently large \(h\). All constants, including \(S\), are fixed
before taking this limit. Since \(T(h)=h^{o(1)}\),
the cutoff is \(h^{1/2-o(1)}\), and
\[
 n_ET(h)^2
 =O\left(h^{3/2}T(h)^2+\frac{h^2}{\log^2(2h)}+hT(h)^2\right)
 =o(h^2).                                                     \tag{16}
\]
Thus the conditional quadratic-width reduction remains valid with all
\(\mathrm P_{q\le Q(h)}\) removed and only larger slot gaps left in the
P family. No logarithmic or subpolynomial factor is hidden in the width:
the diagonal-band deletion is explicitly charged in (16).

For example, if the positional lemma is stated using a maximal-divisor
factor \(\tau^*(h)\), take \(T(h)=\max(1,\tau^*(h))\). The argument
uses that exact factor, rather than assuming that all subquadratic exceptional
sets have negligible relocation cost. For large enough \(h\), \(Q(h)>15\),
so all P pairs internal to any sixteen consecutive slots are already excluded
in every residue block. The separate sixteen-label local theorem is not
needed for this conclusion.

Independent review: the square-filter/common-list argument, exceptional
count, locality transfer, and cited-input scope passed a separate audit.
Section 6's full growing-cutoff deduction and exact relocation charge also
passed that independent audit. The rectangular and triangular order proof
was checked separately by another reader.
