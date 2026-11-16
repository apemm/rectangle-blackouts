# Two local choices remove every factor-one P constraint

14 November 2026. The factor-one family needs only two local choices.
Any \(R\) prescribed factors can be removed with \(4R+1\) choices at a
fixed stride, including within the period-seven profile placement.
The full P family and the other rectangle supports remain unresolved.
All stated results have passed
[independent audit](continuation_hilbert_factor_choices_audit.md).

Use the Hilbert ranks from
[the placement note](continuation_hilbert_placement.md). For each retained
label \(e=(i_e,j_e)\), its odd and even rows are \(2i_e+1\) and \(2j_e+2\).
Retain the original padded ranks \(r_e\), and place its column at
\[
 x_e=S(Mr_e+\xi_e),\qquad \xi_e\in\{0,\ldots,M-1\},
 \tag{1}
\]
where \(S\ge8\) is an even integer and \(M\ge2\).
Taking \(S=32\) also preserves the same-parity integral-distance exclusion.

Call a Pythagorean cross-parity pair **factor one** if its horizontal
distance \(X>0\), absolute vertical distance \(Y\), and integral diagonal
length \(L\) satisfy
\[
 \frac{L-Y}{2}=1.
 \tag{2}
\]
Equivalently,
\[
 Y=X^2/4-1,\qquad L=X^2/4+1.
 \tag{3}
\]

**Theorem.** There is a choice of the \(\xi_e\) in (1) that excludes
every factor-one pair, whether or not its vertical completion lies in
the strip. In fact only the two values \(\xi_e=0,1\) are needed.

Thus two choices suffice for this entire family, uniformly in the
height and in the retained subset of labels.

## 1. Candidate constraints include all local assignments

Form a graph on the retained labels. Join \(e,f\) when some choices
\(\xi_e,\xi_f\in\{0,\ldots,M-1\}\) make one of their two cross-parity
pairs satisfy (3). This graph is defined before any choices are made.
It includes constraints whose completion lies outside the board.

Suppose \(r_e<r_f\), and write
\[
 d=r_f-r_e,\qquad
 q=M d+\xi_f-\xi_e.
 \tag{4}
\]
Then \(q\) is a positive integer, \(X=S q\), and
\[
 q\ge M(d-1)+1\ge d.
 \tag{5}
\]
The Hilbert estimate therefore gives, for either coordinate,
\[
 |i_f-i_e|,\ |j_f-j_e|<4\sqrt d\le4\sqrt q.
 \tag{6}
\]
These bounds apply separately to each candidate assignment. They do not
require that different candidate assignments coexist.

## 2. A fixed label has only one candidate absolute gap

Fix \(e=(i,j)\), and set \(T=j-i\) and \(A=S^2/8\ge8\).
For any candidate neighbor \(f\), the signed difference
of the even row and the odd row has one of the forms
\[
 y=2T+2z+1,\qquad
 z=j_f-j\quad\hbox{or}\quad z=-(i_f-i).
 \tag{7}
\]
By (6), \(|z|<4\sqrt q\). Equation (3) gives a sign
\(\epsilon\in\{-1,1\}\) for which
\[
 T=\epsilon A q^2-\frac{\epsilon+1}{2}-z.
 \tag{8}
\]

Consider any two candidates at \(e\), including candidates with different
neighbors, roles, or local assignments.
If their signs agree but \(q_1\ne q_2\), then
\[
 A|q_1^2-q_2^2|
 =|z_1-z_2|<4(\sqrt{q_1}+\sqrt{q_2}).
 \tag{9}
\]
For distinct positive integers,
\[
 |q_1^2-q_2^2|\ge q_1+q_2
 \ge\sqrt{q_1}+\sqrt{q_2}.
\]
This contradicts \(A\ge8\).

If the signs differ, (8) instead gives
\[
 A(q_1^2+q_2^2)
 \le 1+|z_1|+|z_2|
 <1+4(\sqrt{q_1}+\sqrt{q_2}).
 \tag{10}
\]
Since \(\sqrt q\le q^2\) for \(q\ge1\) and
\(q_1^2+q_2^2\ge2\), the right side is at most
\[
 \frac92(q_1^2+q_2^2),
\]
again a contradiction.

Consequently every candidate edge at \(e\) has the same absolute
slot gap \(q_e\) and the same sign in (8).
Along a candidate edge \(ef\), \(q_e=q_f\), since both refer to the
same absolute horizontal distance divided by \(S\).
Every nontrivial connected component of the candidate graph therefore
has one fixed gap \(q\).

## 3. An explicit two-choice assignment

Treat each nontrivial candidate component separately, using its fixed
gap \(q\). If \(M\nmid q\), set \(\xi_e=0\) throughout that component.
Every resulting slot difference is divisible by \(M\), so none equals
\(q\).

If \(q=M d_0\), the only possible positive rank difference for a candidate
edge is \(d_0\). Indeed, (4) and
\(|\xi_f-\xi_e|\le M-1\) give this directly. Set
\[
 \xi_e=\left\lfloor r_e/d_0\right\rfloor\bmod2.
 \tag{11}
\]
Two ranks at difference \(d_0\) receive opposite choices. Their actual
slot gap is therefore \(q+1\) or \(q-1\), never \(q\).

Assign zero to isolated labels. Every pair that could satisfy (3) for
the final choices was already included in the candidate graph.
The construction removes all its candidate constraints, proving the theorem.

For \(M=2\), the rule says: use zero on odd-\(q\) components, and use
(11) on even-\(q\) components. At \(S=32,M=2\), the full padded placement
has width below \(64Q^2=O(h^2)\), where \(Q\) is the padding side length.
The same-parity distance exclusion remains valid because the original
rank separation is retained.

## 4. The candidate graph also has two earlier neighbors

For a candidate edge \(ef\) with \(r_e<r_f\), (4) implies
\[
 |M(r_f-r_e)-q|\le M-1.
 \tag{12}
\]
For a fixed integer \(q\), the positive integer \(r_f-r_e\) has at most
two possibilities:
\[
 \left\lfloor q/M\right\rfloor,\qquad
 \left\lceil q/M\right\rceil,
 \tag{13}
\]
with zero discarded and duplicates removed.
Each rank contains at most one retained label. Thus each label has
at most two earlier neighbors in the full candidate graph.

Assign the choices in increasing rank. An earlier neighbor \(e\) of the
current label \(f\) can forbid only
\[
 \xi_f=q-M(r_f-r_e)+\xi_e.
 \tag{14}
\]
There is at most one forbidden value from that neighbor, even if both
cross-parity roles supplied the candidate edge.
There are at most two earlier neighbors, so at least one of the \(M\ge3\)
choices remains. This proves the theorem.

This gives an alternative increasing-rank greedy proof for \(M\ge3\).
The componentwise construction in Section 3 proves the stronger \(M=2\)
statement.

## 5. What the theorem does and does not settle

For any fixed placement (1), its actual factor-one graph is even simpler.
Each component has a fixed absolute slot gap \(q\), and its edges join
occupied integer slots at distance \(q\). Thus each component is a path
or an isolated vertex. In particular it is bipartite.
The candidate graph used in the proof can have more edges, because it
combines mutually incompatible local assignments. The two-earlier-neighbor
bound is the property that permits the greedy assignment.

The factor-one hypothesis is substantive. In general write
\[
 a=(L-Y)/2,\qquad b=(L+Y)/2,\qquad ab=X^2/4.
\]
Larger \(a\) produce different parabolic equations. The present argument
does not combine their constraints into a bounded number of earlier
neighbors. Establishing such control, or replacing it with another
constant-choice argument, remains necessary for the full P family.

This theorem also says nothing about mixed supports or tilted black
right angles that are not factor-one vertical rivals.

The two-choice conclusion cannot be combined freely across factors.
The explicit five-label obstruction in
[the two-choice counterexample](continuation_hilbert_two_choice_obstruction.md)
uses only the smaller half-factors \(1\) and \(245\), since its two
Pythagorean triples have
\[
 (1025-1023)/2=1,\qquad (1525-1035)/2=245.
\]
Those two families together already defeat all binary choices at
\(S=32,h=2048\). This is consistent with the finite-family bounds below.

## 6. Any fixed collection of sufficiently small factors

The same method covers more than factor one. Fix an integer \(a\ge1\)
with
\[
 a\le S^2/32,
 \tag{15}
\]
and consider candidates for which the smaller half-factor is \(a\):
\[
 a=(L-|y|)/2,\qquad
 |y|=\frac{S^2q^2}{4a}-a>0.
 \tag{16}
\]
Put \(A=S^2/(8a)\ge4\). Equation (8) becomes
\[
 T=\epsilon A q^2-\frac{\epsilon a+1}{2}-z,
 \qquad |z|<4\sqrt q.
 \tag{17}
\]

**Fixed-factor lemma.** At any fixed label, all candidates satisfying
(16) have the same absolute slot gap \(q\). Their signs need not agree.

For equal signs, the proof is (9), now using \(A\ge4\).
For opposite signs and distinct \(q_1>q_2\), subtracting (17) gives
\[
 A(q_1^2+q_2^2)-a=z_+-z_-.
 \tag{18}
\]
The smaller-factor condition in (16) implies
\(2Aq_2^2>a\). Hence the positive left side of (18) is strictly larger
than
\[
 A(q_1^2-q_2^2)
 \ge4(\sqrt{q_1}+\sqrt{q_2}),
\]
whereas its right side has smaller absolute value. This is impossible.
That proves uniqueness of \(q\).

The fixed-factor candidate components again have a common gap, so the
two-choice rule in Section 3 removes all constraints for this one \(a\).
More generally, let \(\mathcal A\) be a collection of \(R\) positive
integers satisfying (15). Each factor contributes at most two earlier
candidate constraints at a label, each forbidding at most one current
choice. Thus
\[
 M\ge2R+1
 \tag{19}
\]
permits increasing-rank greedy elimination of every factor in
\(\mathcal A\) simultaneously.

For example, at \(S=32\), this applies to every \(a\le32\).
Since \(S\) is a power of two, an even smaller half-factor is divisible
by \(S^2/4=256\): the two half-factors have opposite parity and their
product is \(S^2q^2/4\). Therefore only the 16 odd values below 32 occur
in this range, and \(M=33\) suffices for their simultaneous removal.

For any fixed cutoff \(A_0\), choose a power of two
\[
 S\ge\max\{32,\sqrt{32A_0}\}.
\]
Then all smaller half-factors \(a\le A_0\) can be eliminated at a total
width cost \(O(A_0^{3/2}h^2)\). In particular the cost remains \(O(h^2)\)
for a fixed cutoff. This is a finite-factor statement, not a uniform
bound after allowing \(A_0\) to grow without paying its displayed cost.

## 7. Arbitrary fixed factors at a fixed stride

A more local comparison removes the restriction (15), at the cost of
doubling the greedy bound. This also improves the preceding cutoff cost.

**Finite-factor theorem.** Let \(S\ge8\) be any fixed even integer.
For any set \(\mathcal A\) of \(R\) positive integers, the choice
\[
 M\ge4R+1
 \tag{20}
\]
admits an increasing-rank greedy assignment that removes every P pair
whose smaller half-factor belongs to \(\mathcal A\).
There is no restriction on the magnitudes of these factors.
At \(S=32\), the width is \(O(Rh^2)\), while the same-parity
integral-distance exclusion is preserved.

Fix a focal label, a cross-parity role from (7), and one horizontal side
of the focal column. Consider two candidates with distinct absolute
slot gaps \(q_1>q_2\), and put \(\Delta=q_1-q_2\ge1\).
Let \(d_1,d_2\) be their positive rank distances from the focal label.
Their separate assignments satisfy
\[
 |M(d_1-d_2)-\Delta|\le2M-2.
\]
Consequently
\[
 |d_1-d_2|
 \le\frac{\Delta+2M-2}{M}<\Delta+1.
\]
The rank distances are integers, so
\[
 |d_1-d_2|\le\Delta.
 \tag{21}
\]
Because the candidates are on the same side, their mutual rank distance
is exactly \(|d_1-d_2|\). Because their parity roles are the same,
\(z_1-z_2\) is a difference of a single Hilbert coordinate.
Thus
\[
 |z_1-z_2|\le4\sqrt{|d_1-d_2|}
 \le4\sqrt\Delta.
 \tag{22}
\]
The zero-distance case in this inequality just says \(z_1=z_2\).

Now fix the factor \(a\), and again put \(A=S^2/(8a)\), without
assuming \(A\ge4\). Since \(a\) is the smaller half-factor and
\(|y|>0\),
\[
 S q_i>2a,\qquad
 A(q_1+q_2)>S/2\ge4.
 \tag{23}
\]
If the signs in (17) agree, that equation and (23) give
\[
 |z_1-z_2|=A(q_1^2-q_2^2)>4\Delta,
\]
contradicting (22).
If the signs differ, the same smaller-factor inequality gives
\[
 A(q_1^2+q_2^2)-a
 >A(q_1^2-q_2^2)>4\Delta,
\]
again contradicting (22). Therefore this fixed factor, role, and side
have a unique candidate slot gap \(q\).

For earlier neighbors there is only one side and there are two parity
roles. Each of their at most two gaps permits at most two earlier ranks
by (12)--(13). For each such rank, factor, and role, the fixed gap
forbids at most one current choice by (14).
Thus at most four choices are forbidden per factor, and at most \(4R\)
across \(\mathcal A\). This proves (20).

In particular every smaller half-factor \(a\le A_0\) can be removed in
\(O(A_0h^2)\) width at fixed stride 32. The unresolved issue is to control
all factors with a bounded total number of choices, not to handle any
one fixed factor or fixed finite collection.

## 8. The same choices within a profile block

The finite-factor construction is compatible with the profile version of
the Hilbert placement. Suppose the two row progressions are
\[
 a_e=a_0+d i_e,\qquad b_e=b_0+d j_e,
 \tag{24}
\]
where \(d\) is a positive even integer and the two offsets have opposite
parity. Retain the same Hilbert ranks and columns (1).
For a focal label, write \(T=b_e-a_e\) for its physical row gap.
The two cross-parity roles give
\[
 y=T+d z,\qquad z=\Delta j\ \hbox{or}\ -\Delta i.
\]
For smaller half-factor \(a\), the candidate equation is
\[
 T=\epsilon\left(\frac{S^2q^2}{4a}-a\right)-d z.
 \tag{25}
\]

For candidates with fixed factor, role, and side, (21)--(22) still apply.
The quadratic difference in (25) is greater than \(S\Delta\), by the
smaller-factor condition \(Sq_i>2a\). The coordinate error is at most
\(4d\sqrt\Delta\). Thus
\[
 S\ge4d
 \tag{26}
\]
proves the arbitrary-factor theorem with the same \(M\ge4R+1\).

For the stronger componentwise two-choice argument, comparison of all
roles and sides is valid when
\[
 \frac{S^2}{4a}\ge4d,
 \quad\hbox{equivalently}\quad
 a\le\frac{S^2}{16d}.
 \tag{27}
\]
The equal-sign proof uses
\(|z_1-z_2|<4(\sqrt{q_1}+\sqrt{q_2})\).
For opposite signs and distinct gaps, subtract \(2a\) and use the
smaller-factor inequality just as in Section 6. Hence each candidate
component has one gap, and Section 3 applies without change.

In the period-seven profile placement, \(d=14\) and \(S=1568\).
Conditions (26) and (27) hold for factor one, so two choices remove
that family while every selected column remains divisible by seven.
The same-parity distance exclusion is preserved because this stride is
the original \(8d^2\), and every choice retains its minimum rank
separation. Thus this corollary uses the existing admissible profile
columns. It does not assert that the remaining P factors or mixed
supports have been removed.
