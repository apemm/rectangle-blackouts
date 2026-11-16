# Removing multiple-leg pairs costs few labels

15 November 2026. Fix an even stride \(S\) and a choice count \(M\ge3\).
Use the original Hilbert ranks and columns
\[
 x_r=S(Mr+\xi_r),\qquad 0\le\xi_r<M.
\]
The two black rows of label \((i,j)\) are \(2i+1,2j+2\), inside
\(\{1,\ldots,h\}\). All constants below can depend on \(S,M\).
At \(S\ge32\), the usual same-parity distance exclusion is preserved.

**Theorem.** There is a deterministic set of \(O_{S,M}(h^{3/2})\)
labels whose deletion leaves at most two integer forbidden differences
on every remaining pair of labels. More precisely, each cross-parity
role then contributes at most one slot value.

For \(M=3\), every remaining subsystem on at most three labels is
integer-solvable. The same assertion holds for \(M>3\) if those three
labels use the allowed subset \(\{0,1,2\}\).

This is a P-only deletion theorem. Deleted labels still need positions
in a complete construction, and interactions with fillers and other
supports are not treated. No new threshold bound is claimed.

An independent reader checked the completed proof, including the
integer reduction to the Pell equation, the positive-orbit estimate,
the label count, and the three-label consequence. No correction was needed.

## 1. Two nearby legs have bounded horizontal size

Put \(H=2S(M-1)\). Call a positive odd \(Y\) exceptional when it has
two positive horizontal legs \(X<X+g\), both divisible by \(S\),
with \(1\le g\le H\). Let their hypotenuses be \(L_1<L_2\), and
write \(f=L_2-L_1\). Then \(f\) is a positive integer and \(f<g\),
because \(x\mapsto\sqrt{x^2+Y^2}\) has derivative strictly below one.

Subtracting the norm identities gives
\[
 2gX+g^2=2fL_1+f^2.
\]
Since \(f<g\) and \(L_1<X+Y\),
\[
 (g-f)X<fY.
\]
Thus
\[
 X<HY.
\tag{1}
\]

Suppose these two legs occur in the same rank-pair slot interval.
The smaller is \(X=S(Md+\delta)\), where \(|\delta|\le M-1\).
Equation (1) implies
\[
 d\le\frac{X}{SM}+\frac{M-1}{M}<2Y+1.
\tag{2}
\]
The last inequality uses \(H=2S(M-1)\).

## 2. A weighted form of the fixed-gap Pell count

Let \(\mathcal E_H\) be the set of exceptional \(Y\), allowing all
integer horizontal legs rather than requiring divisibility by \(S\).
The fixed-gap Pell argument gives the stronger weighted estimate
\[
 \sum_{\substack{Y\in\mathcal E_H\\Y<h}}\sqrt Y
   =O_H(\sqrt h).
\tag{3}
\]
In particular, retaining the usual extra factor \(\log h\) from the
unweighted count is unnecessary here.
The orbit reduction is the one in Lemma Q of
`hilbert_energy_bound_false.md`; the geometric sum is the additional step.

For completeness, fix \(1\le f<g\le H\), put \(z=2X+g\), and use
\[
 (g^2-f^2)(z^2-f^2)=(2fY)^2.
\tag{4}
\]
Write \(g^2-f^2=m^2D\) with \(D\) squarefree. Divisibility in (4)
gives an integer \(u\) such that
\[
 z^2-Du^2=f^2,\qquad Y=\frac{mD}{2f}u.
\tag{5}
\]
When \(D=1\), factoring \((z-u)(z+u)=f^2\) leaves finitely many
solutions. When \(D>1\), let \(\varepsilon>1\) be a norm-one unit
with integer coefficients in \(\mathbb Z[\sqrt D]\). As in the fixed-gap Pell proof, multiplication by
\(\varepsilon\) partitions the positive solutions into finitely many
orbits
\[
 z_n+u_n\sqrt D=\beta\varepsilon^n,
\]
with representatives \(f\le\beta<f\varepsilon\). There are only
finitely many representatives because both their integer coefficients
are bounded in this interval.

The standard existence theorem for that positive integer unit is the
only external input here; see
[the formal statement of Pell unit existence](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html#Pell.exists_of_not_isSquare).
The orbit reduction and the weighted estimate are derived in this note.

For the terms with \(u_n>0\), conjugation gives
\[
 u_n=\frac{\beta\varepsilon^n-f^2/(\beta\varepsilon^n)}{2\sqrt D},
 \qquad u_{n+1}>\varepsilon u_n.
\]
Thus the square roots of the positive \(Y_n\) in one orbit grow by
at least the fixed ratio \(\sqrt\varepsilon>1\). Their sum up to
\(Y_n<h\) is at most a constant times \(\sqrt h\). The finitely many
orbits, and finitely many pairs \((f,g)\), prove (3). Congruence and
divisibility restrictions only remove solutions.

## 3. Delete narrow diagonal bands

For each exceptional \(Y<h\), delete every label whose diagonal
\(T=j-i\) satisfies at least one of
\[
 |T-Y/2|\le4\sqrt{2Y+1}+1,
 \qquad |T+Y/2|\le4\sqrt{2Y+1}+1.
\tag{6}
\]
Each band contains \(O(\sqrt Y)\) integer diagonals. Each diagonal
contains at most \(h\) labels, so (3) bounds the deleted set by
\(O_{S,M}(h^{3/2})\).

To see that every multiple-leg pair is covered, write its signed cross
diagonal as \(U=j_e-i_o\), so \(|2U+1|=Y\). Hilbert locality gives,
for either endpoint \(v\),
\[
 |T_v-U|<4\sqrt d.
\]
Since \(U=(\pm Y-1)/2\), equation (2) puts both endpoints in (6).
Consequently no surviving role has two distinct slot values. The two
roles together contribute at most two forbidden integer differences.

The three-label conclusion is now
[the integer three-choice lemma](continuation_three_label_integer_lemma.md).
For \(M>3\), differences outside \(\{-2,-1,0,1,2\}\) do not affect
assignments in the subset \(\{0,1,2\}\).

## 4. Remaining use in a full construction

This isolates multiplicity caused by nearby Pythagorean legs in a
subquadratic number of labels. It does not bound the chromatic number,
core number, or integer solvability of the remaining graph: even one
forbidden difference per pair can form a larger obstruction.

A complete quadratic-width construction still needs both a solution
for that remaining graph and a compatible placement of the deleted
labels. Any proposed relocation argument must account for its
interaction with the retained labels, profiles, and collars.
