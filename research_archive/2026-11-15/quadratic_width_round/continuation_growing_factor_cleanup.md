# A growing half-factor range can be removed with few labels

15 November 2026. In the original Hilbert rank placement, all P candidates
whose smaller half-factor is at most \(A\) can be removed by deleting
\(O(h^{7/4}A^{7/4})\) labels. This holds uniformly over all private choices.
For \(A=h^\eta\) with fixed \(0<\eta<1/7\), the deletion count is
\(o(h^2)\), even after multiplication by a fixed subpolynomial relocation
factor.

This is a P-only reduction. Literal deletion creates occupancy holes, but
the conditional singleton-stub implementation in Section 4 preserves a core
that was fully occupied initially. Neither version removes the large-factor
graph or proves a quadratic threshold.

The stronger bound obtained by retaining square divisibility is proved in
[`continuation_divisibility_factor_cleanup.md`](continuation_divisibility_factor_cleanup.md).
It replaces the factor (A^{7/4}) by (A^{3/4}\log(2A)), permits
(A=h^{1/3-o(1)}), and leaves actual in-strip P gaps at least
(h^{2/3-o(1)}) in the occupied triangular setting. The elementary argument
below remains valid as a weaker estimate.

## 1. Setting and deletion set

Fix an even stride \(S\) and a choice count \(M\ge1\), independent of
\(h\). Keep original Hilbert ranks and use
\[
 x_r=S(Mr+\xi_r),\qquad0\le\xi_r<M.
\]
For distinct ranks with difference \(d\ge1\), their positive slot gap is
\(q=Md+\delta\), with \(|\delta|\le M-1\). In particular \(q\ge d\).
The odd/even row indices satisfy the standard Hilbert bound
\[
 |T_v-U|<4\sqrt d
\]
at either endpoint, where \(T_v=j_v-i_v\) and \(U\) is the signed
cross-row index difference. The physical vertical leg is \(Y=|2U+1|<h\).

For a Pythagorean candidate let
\[
 a=(L-Y)/2\in\mathbb Z_{>0}.
\]
Since \(S\) is even and \(Y\) is odd, the hypotenuse \(L\) is odd and
\(a\) is an integer. The norm equation gives
\[
 S^2q^2=4a(Y+a),\qquad
 Y=\frac{S^2q^2}{4a}-a.                                    \tag{1}
\]
Assume \(1\le A\le h\). For each integer \(a\le A\), enumerate every
positive integer
\[
 q\le\frac{2\sqrt{a(h+a)}}{S}.
\]
Discard every nonintegral, nonpositive, or even candidate for \(Y\) in (1), and
discard those with \(Y\ge h\). For every remaining odd \(Y\), delete
all labels satisfying
\[
 \left|T_v-\frac{\pm Y-1}{2}\right|\le4\sqrt q+1            \tag{2}
\]
for either sign.

Any P candidate with \(a\le A\) has parameters in this list. Since
\(d\le q\), both endpoint labels lie in its band (2). Therefore no such
candidate remains, regardless of the private choices. No alternative-vertex
strip condition or axis-owner test was used, so the conclusion includes
the larger candidate system.

## 2. Count the deleted labels

One band (2) contains \(O(\sqrt q+1)\) diagonals, each with at most \(h\)
labels. Since \(A\le h\), the upper bound on \(q\) is \(O_S(\sqrt{ah})\).
Thus the union is bounded by
\[
 \begin{aligned}
 |E_A|
 &\le C_{S,M}h\sum_{1\le a\le A}
                 \sum_{1\le q\le C_S\sqrt{ah}}(\sqrt q+1)\\
 &\le C_{S,M}h\sum_{1\le a\le A}(ah)^{3/4}\\
 &\le C_{S,M}h^{7/4}A^{7/4}.                               \tag{3}
 \end{aligned}
\]
Overlaps only reduce the count. The proof deliberately ignores the extra
divisibility restrictions in (1), so it does not require a divisor estimate.

For \(A=h^\eta\), (3) is
\[
 |E_A|=O\left(h^{7(1+\eta)/4}\right)=o(h^2)
 \quad\text{if }0<\eta<1/7.
\]
For example, \(A=h^{1/14}\) gives \(|E_A|=O(h^{15/8})\).
Under a separately applicable relocation estimate with internal cost
\(O((|E_A|+1)T(h)^2)\), where \(T(h)=h^{o(1)}\), that internal cost
is still \(o(h^2)\). Compatibility and collars remain separate hypotheses.

## 3. Relation to the other reductions

This deletion can be combined with the \(O(h^{3/2})\) multiple-leg
deletion while retaining every original rank of each surviving label.
The resulting candidate P graph has at most one slot value per cross role
for each label pair, and contains only half-factors \(a>h^\eta\).

There is no claim that this residual graph has bounded degree, bounded
chromatic number, or a solution with bounded \(M\). In particular, the
deletion creates holes in the original filled scaffold. FW and other
nonmonotone filler families must be recomputed if this reduced graph is
used in a board construction.

The elementary count is also not asserted to be sharp. A sharper average
bound for the level sets
\(\#\{r:j(r+d)-i(r)=U\}\) could reduce the band cost. The present proof
uses only the uniform Hilbert locality estimate.

Independent review: the complete count, uniformity over private choices,
and the stated P-only scope passed a separate audit.

## 4. Preserve occupied cores by retaining even stubs

The construction in
[`continuation_odd_stub_exception_repair.md`](continuation_odd_stub_exception_repair.md)
removes the occupancy obstruction for a fully occupied H7-compatible core.
Erase only the odd point of each label in \(E_A\), retain its original even
point as a singleton stub, and relocate the complete original pair in the
cited exceptional-label windows. Every targeted P candidate loses its odd
endpoint because both of its labels belong to \(E_A\).

All arithmetic slots stay nonempty and no row-\(F\) source is restored.
The existing FW exclusion therefore survives. The original rank or slot
geometry is unchanged, and the final number of black points remains
\(m+q_h\) after the relocated pairs are counted. Residual P must still
include every surviving even endpoint, including stubs. One must not remove
the exceptional vertices from that residual graph.

The companion note proves the same band count from any fixed physical
Hölder locality bound \(|\Delta a|,|\Delta b|\le C\sqrt q\).
It therefore applies to the occupied packed triangles and the random filtered
pack lists, with constants independent of height. Combining it with the
growing short-gap band leaves only
\[
 q>h^{1/2-o(1)},\qquad (L-|Y|)/2>h^\eta
\]
in the P family, for fixed \(0<\eta<1/7\).

This conditional implementation uses the unchanged full final row-pair graph,
the cited relocation and collar inputs, and avoidance of the surviving mixed
families. It does not make an originally sparse private-choice layout fully
occupied. The companion proof and this transfer received an independent
written audit.
