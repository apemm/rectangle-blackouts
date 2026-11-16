# Odd-point erasure repairs P exceptions without creating filler holes

15 November 2026. A P-only exceptional label set need not be emptied from a
fully occupied core. Erase its odd black points, retain its original even
points as singleton stubs, and relocate the complete pairs in separate valid
windows. This preserves the no-F-source argument, same-parity locality, and
the exact excess count. It also makes a growing small-half-factor deletion
compatible with the occupied triangular scaffold.

This removes targeted P families, not the remaining P graph or the other
mixed supports. It does not repair pre-existing padding or private-choice
holes, and it does not remove bad even rows in an arbitrary R2s row deletion.

## 1. Erasure cannot create a rectangle collision

For a fixed ambient board and black set \(B\), the presentation of a
rectangle \(R\) is \(R\setminus B\). For distinct rectangles \(R,S\),
\[
 R\setminus B=S\setminus B
 \quad\Longleftrightarrow\quad R\mathbin\triangle S\subseteq B.
\tag{1}
\]
Thus every collision after replacing \(B\) by a subset \(B'\) already
existed for \(B\). Newly white common corners do not affect this conclusion.
An all-black rectangle is also impossible to create by erasure.

The distinction from deleting a label and restoring its sea filler is
essential: restoring a filler adds a black point, so that operation is not
covered by (1). The present operation adds no point inside the core.

## 2. The stub operation and its exact hypotheses

Start with an H7-compatible core whose arithmetic interval
\[
 x_0+S\{0,1,\ldots,N-1\}
\tag{2}
\]
contains one genuine odd/even double label at every slot. Its rows satisfy
the profile's residue, alignment, bulk, and one-label conditions. Its full
label placement satisfies the required same-parity locality bound, uniformly
over any within-tile choices still being considered.

Let \(E\) be a set of its labels. For each \(e=(a_e,b_e)\in E\), with
\(a_e\) odd and \(b_e\) even, remove \((x_e,a_e)\) and keep
\((x_e,b_e)\). No filler point is restored. Relocate the complete pair
\((a_e,b_e)\) later, in the cited separate exceptional-label construction.

Suppose every targeted P candidate has its odd endpoint in a label of
\(E\). Then that candidate loses a black endpoint and is absent from the
erased core. In particular, it is enough to choose \(E\) containing both
endpoint labels of every targeted candidate, as the diagonal-band deletion
lemmas do.

This does not remove a P candidate merely because its even endpoint belongs
to \(E\). The directional odd-endpoint coverage condition must be checked.
The full final parity row-pair graph is still used for all virtual rival
tests. Relocating an owner does not authorize dropping its rival tests.

## 3. Occupancy, parked triangles, and the residual criterion

Every slot of (2) remains nonempty, and no slot contains a row-\(F\) filler.
The surviving even row is a bulk label row, so it is different from \(F\).
Same-parity locality is preserved by restriction to the remaining points.

The FW argument only needs this absence of row-\(F\) points, not two black
points at each slot. For a parked triangle with vertex \(A=(x_e,y)\),
other same-parity label point \(C=A+(X,\delta)\), and sea point
\(A+(\xi,F-y)\), its completion is
\(W=C+(\xi,F-y)\) and
\[
 X\xi=-\delta(F-y).                                         \tag{3}
\]
If \(W\) lies at a slot of (2), then \(S\mid\xi\), and the usual H7
alignment gives \(S^2/2\mid\delta\). The zero case places the supposed
sea point in \(A\)'s slot. A negative value puts \(F+\delta\) below the
strip because \(F<S^2/2\). Thus any in-strip case has \(\delta>0\).
Since \(y>F\), equation (3) gives \(X\xi>0\). The sea source lies at
the arithmetic slot strictly between \(x_e\) and \(x_W\), where no
row-\(F\) point exists. This is a contradiction, whether those slots hold
doubles or singleton stubs.

The other H7 geometric sieves use the surviving points' row residues,
alignment, bulk inequalities, and locality. Erasing points preserves those
hypotheses. Every surviving three-, four-, or six-point black support was
already a black support in the original full-double core. For compiled
overgraphs, retain the original geometric supports rather than introducing
new occupancy-dependent permissions after erasure.

Parked PT completions outside the arithmetic slots lie in unchanged sea
columns, so their white/parking status is unchanged. A completion at an
arithmetic slot is excluded by the preceding FW argument. This also handles
the only potential concern that erasing a label point might unpark a triangle.

Accordingly, the corrected H7 full-final-graph criterion still reduces the
erased core to the surviving untargeted P, \(\Lambda_3\), \(\Lambda_4\),
R2s, and 6PT supports. A sufficient condition is to avoid all the untargeted
families in the original full-double candidate overgraph. Erasure can kill
additional supports, but cannot require a larger overgraph.

The external relocation and the joins are separate inputs. Use valid
exceptional-label windows relative to the same full final row-pair graph,
with the cited filled collars and separation. Those inputs control newly
available rectangles involving external columns and distant axis owners;
they are not consequences of the fixed-board monotonicity statement (1).

## 4. The excess is exactly restored

If a core has width \(m_0\) and \(N\) doubles, it contains \(m_0+N\)
black points. Erasing the odd points of \(E\) changes this to
\(m_0+N-|E|\). An external filled window of width \(m_E\) with exactly
the relocated pairs has \(m_E+|E|\) points. Filled collars add one point
per column. Therefore the combined board still has
\[
 m+N
\]
points. Applying this to all cores restores every original parity pair
exactly once as a double column. The old stub is a singleton, not a duplicate
row-pair edge. If the full family has \(q_h\) labels, the final count is
exactly \(m+q_h\).

## 5. A growing half-factor range can be erased in this way

Suppose the original full-double core has stride \(S\) and uniform physical
locality
\[
 |a_e-a_f|,\ |b_e-b_f|\le C\sqrt q
\tag{4}
\]
whenever its two slots differ by \(q\). Here \(C,S\) are fixed constants;
the packed triangular scaffold satisfies this for every within-tile
permutation. Let the odd/even points of a P candidate have vertical magnitude
\(Y\), integer hypotenuse \(L\), and smaller half-factor
\[
 a=(L-Y)/2.
\]
For \(4\mid S\), this is a positive integer, and
\[
 S^2q^2=4a(Y+a),\qquad
 Y=S^2q^2/(4a)-a.                                           \tag{5}
\]

Fix \(1\le A\le h\). For every integer \(a\le A\), enumerate
\(q\le2\sqrt{a(h+a)}/S\), retaining the positive odd integral values
\(Y<h\) in (5). Put in \(E_A\) every label whose own signed row gap
\(b_e-a_e\) is within \(C\sqrt q+1\) of either \(Y\) or \(-Y\)
for one of these parameter pairs.

Both endpoint labels of every candidate with half-factor at most \(A\)
belong to \(E_A\). For example, if its odd endpoint is \(a_e\) and its
even endpoint is \(b_f\), then
\[
 |(b_e-a_e)-(b_f-a_e)|=|b_e-b_f|\le C\sqrt q,
\]
and the other endpoint follows from the odd-row version of (4).

For each integer signed row gap, at most \(h\) parity labels exist.
Consequently
\[
 |E_A|
 \le C_1h\sum_{a\le A}\sum_{q\le C_2\sqrt{ah}}(\sqrt q+1)
 =O(h^{7/4}A^{7/4}).                                        \tag{6}
\]
This count does not require equally spaced row lists or the original Hilbert
rank formula. It uses only physical locality (4). Filtering the label family
can only reduce the count.

Take \(A=\lfloor h^\eta\rfloor\), with fixed \(0<\eta<1/7\). Then
\(E_A\) has size \(O(h^{7(1+\eta)/4})\), and its internal relocation
cost \(|E_A|T(h)^2\) is \(o(h^2)\) for the cited
\(T(h)=h^{o(1)}\). Erasing only its odd points removes every such P
candidate while preserving arithmetic occupancy and the FW exclusion.

Combined with the common-index triangular band, this leaves only P
candidates satisfying both
\[
 q>Q(h)=h^{1/2-o(1)},\qquad a>h^\eta,
\]
besides the other four residual families. There are still only constantly
many ordinary and exceptional windows. The full-board width implication
remains conditional on avoiding those residual families and on the cited
relocation/collar inputs.

The same erasure rule applies to any other P-only deletion theorem whose
exception set contains the odd endpoint of every targeted candidate. It does
not require that exception set to be a Cartesian product or a diagonal band.

## 6. The remaining actual P events have larger gaps

This elementary refinement is superseded by
[the square-divisibility refinement](continuation_divisibility_factor_cleanup.md),
which retains the same stub operation and improves the half-factor cutoff
to \(h^{1/3-o(1)}\) and the remaining actual slot gap to
\(h^{2/3-o(1)}\). The estimates below remain valid but are weaker.

The subpower relocation cost permits the sharper choice
\[
 A=\left\lfloor
 \frac{\eta h^{1/7}}{T(h)^{8/7}\log(2h)^{8/7}}
 \right\rfloor=h^{1/7-o(1)},                                \tag{7}
\]
where \(\eta>0\) is fixed. Equation (6) then gives
\[
 |E_A|T(h)^2=O(h^2/\log^2 h)=o(h^2).                         \tag{8}
\]
The floor is positive for all sufficiently large \(h\).

Use the occupied triangular scaffold with
\(Q=\lfloor\eta_0\sqrt h/(T(h)\log(2h))\rfloor\), and choose its
deleted index band of width \(c_h=\Theta(Q^2)\). The constants absorb the
fixed stride and row step. Thus \(c_h=h^{1-o(1)}\), while the number of
band labels and their relocation cost remain those already proved in
[the common-index scaffold](continuation_common_index_occupied_scaffold.md).

For an actual in-strip P rival, its vertical alternative diagonal has length
\(L\le h-1\). Hence \(X=S q\le h-1\), so (4) changes a row by only
\(O(\sqrt h)\) between the two endpoint labels. The common increasing row
list and the index band therefore give
\[
 Y\ge c_1c_h-O(\sqrt h)\ge c_2c_h=h^{1-o(1)}.               \tag{9}
\]
The same conclusion holds for the random color-list scaffold: its additional
prefix discrepancy is \(O(\sqrt h\log h)=o(c_h)\).

After the erasure in (7), every surviving actual P event has \(a>A\).
Combining (5) and (9) yields
\[
 q=\frac{2\sqrt{a(Y+a)}}S\ge\frac{2\sqrt{A Y}}S
   =h^{4/7-o(1)}.                                          \tag{10}
\]
Its other near-axis gap also satisfies
\[
 L-X=\frac{Y^2}{L+X}\ge\frac{Y^2}{2h}=h^{1-o(1)}.            \tag{11}
\]
These conclusions concern actual P rivals with both alternative corners in
the strip. They do not assert \(L\le h\), or (9)--(11), for the larger
arithmetic candidate family with out-of-strip alternative corners.

## Review record

The odd-stub theorem and its physical-row factor-band count were independently
reviewed on 15 November 2026. The review checked the collision identity,
directional P coverage, unchanged off-lattice parking, the no-F-source proof,
external-owner scope, and the exact \(m+q_h\) count. The quantitative
refinement (7)--(11) was checked separately against the common-index and
random color-list scaffold bounds.
