# Local factor budgets for Hilbert P constraints

14 November 2026. This note turns the fixed-factor lemma into local and
average-degree criteria. It also gives a conservative unconditional
choice bound for the full P family. That bound is not competitive with
the existing full-board threshold.
All stated results have passed
[independent audit](continuation_hilbert_factor_choices_audit.md).

Keep the Hilbert placement
\[
 x_e=S(Mr_e+\xi_e),\qquad 0\le\xi_e<M,
 \tag{1}
\]
with fixed even \(S\ge32\), original padded ranks, and one odd and one even
row per label. All same-parity nonhorizontal integral distances are
excluded for every choice. Only opposite-parity P constraints are treated
below. The other mixed supports remain outside these conclusions.

## 1. The complete candidate multigraph

For fixed \(M\), form the following finite constraint family before
assigning any choices. For each pair \(r_e<r_f\), include
\[
 \xi_f-\xi_e=\delta,\qquad -(M-1)\le\delta\le M-1,
 \tag{2}
\]
whenever this difference makes a cross-parity black pair have integral
length \(L\le h-1\). One can additionally require that the alternate
vertical diagonal lies in the strip; retaining the larger family is
convenient and is harmless.

Deduplicate identical triples \((e,f,\delta)\). Different values of
\(\delta\) on the same label pair remain different constraints, so the
underlying graph is a multigraph. Each constraint forbids at most one
choice at either endpoint once the other endpoint has been assigned.

Every constraint has at least one geometric witness, with smaller
half-factor
\[
 a=(L-|y|)/2\in\mathbb N.
 \tag{3}
\]
For a vertex subset \(U\), let \(F^-_U(e;M)\) count the distinct factors
occurring in witnesses to constraints from \(e\) to earlier labels in
\(U\). Count all witness factors if a constraint has several witnesses.

The fixed-factor, fixed-role, fixed-side lemma in
[the factor-choice note](continuation_hilbert_factor_one_choices.md),
Section 7, gives
\[
 b^-_U(e;M)\le4F^-_U(e;M),
 \tag{4}
\]
where \(b^-_U\) counts earlier constraints, including different forbidden
differences on one pair. The four comes from two parity roles and at most
two possible earlier ranks for each role's unique slot gap.

## 2. A vertexwise criterion

For this already chosen \(M\), if
\[
 M>4\max_e F^-_V(e;M),
 \tag{5}
\]
increasing-rank greedy assignment avoids every P constraint.
At each step, (4) bounds the number of forbidden current values.

This criterion can use different local factor sets at different labels.
There is no requirement that all labels share one global set of \(R\)
factors. In particular, a uniform bound \(F^-_V(e;M)\le R\) suffices even
when the union of these factor sets is large.

The dependence on \(M\) is explicit. Equation (5) is a sufficient
condition on the full candidate family for that value of \(M\); it is not
a proof that such a bounded \(M\) exists uniformly in \(h\).

## 3. A criterion using averages on every induced subgraph

Define
\[
 \mathcal B(M)=
 \max_{\varnothing\ne U\subseteq V}
 \frac1{|U|}\sum_{e\in U}F^-_U(e;M).
 \tag{6}
\]
Summing (4), every induced constraint multigraph satisfies
\[
 |E(U)|\le4\sum_{e\in U}F^-_U(e;M).
 \tag{7}
\]
Its average degree is at most \(8\mathcal B(M)\). Thus it has a vertex
of degree at most \(\lfloor8\mathcal B(M)\rfloor\).
Deleting such vertices successively and assigning choices in reverse
order proves the following criterion:
\[
 M>8\mathcal B(M)
 \quad\Longrightarrow\quad
 \text{all P constraints admit a choice assignment.}
 \tag{8}
\]

This is a genuine refinement when a few vertices have many incident
factors but every induced subgraph has small average factor count.
Equivalently, if deleting vertices of constraint degree less than \(M\)
leaves a nonempty core \(U\), then
\[
 \frac1{|U|}\sum_{e\in U}F^-_U(e;M)\ge M/8.
 \tag{9}
\]
Every failure of this elimination procedure therefore identifies a
subgraph with a quantitatively large average factor count.

One global average on \(V\) does not suffice. Abstractly, take \(K_t\)
and add isolated vertices until there are \(t^2\) vertices. Give each
clique edge its own factor label and the constraint \(\xi_f=\xi_e\).
Each factor family is only one edge, and the global average in (6)
without the maximum over \(U\) is below \(1/2\). Yet \(t\) choices are
necessary. This is not a construction inside the Hilbert P graph. It
shows why the incidence estimate (4) alone cannot replace (6) by one
global average.

Nor does (8) automatically permit variable slot widths at average cost.
The factor-uniqueness proof compares candidates using the common block
width \(M\). A nonuniform-width construction needs a new separation
argument.

## 4. An unconditional bound from the local row window

Let
\[
 Q=\left\lfloor\frac{h-1}{S}\right\rfloor,\qquad
 D_h=\max_{1\le n<h}\tau(n^2),
 \tag{10}
\]
where \(\tau\) counts positive divisors.
An actual P constraint has horizontal distance \(X\le L\le h-1\).
Writing \(q=X/S\), its positive rank gap \(d\) satisfies
\[
 Md-(M-1)\le q\le Q.
 \]
Thus
\[
 d\le W:=\left\lfloor\frac{Q+M-1}{M}\right\rfloor
 \le Q/M+1.
 \tag{11}
\]
Hilbert locality confines each coordinate of an earlier candidate partner
to fewer than \(8\sqrt W+1\) possible integer values.

For either cross-parity role, fix the partner row and let \(Y\) be the
absolute vertical separation. It is nonzero and odd. The equation
\[
 X^2+Y^2=L^2
 \quad\Longleftrightarrow\quad
 (L-X)(L+X)=Y^2
 \tag{12}
\]
has at most \(\tau(Y^2)/2\) solutions with \(X>0,L>0\).
For a fixed \(X\), the slot gap \(q=X/S\) permits at most two earlier
ranks and one forbidden difference at each, by the slot calculation
in the factor-choice note.

After summing the two parity roles, the number of earlier constraints
at any label is therefore at most
\[
 (16\sqrt W+2)D_h
 \le16D_h\sqrt{Q/M}+18D_h.
 \tag{13}
\]
This bound does not require estimating how many distinct factors occur.

In particular, the explicit choice
\[
 M=\left\lceil64D_h+(4096D_h^2Q)^{1/3}\right\rceil+1
 \tag{14}
\]
is larger than (13). Indeed, \(18D_h<18M/64\) and
\(16D_h\sqrt{Q/M}<M/4\).
Increasing-rank greedy assignment therefore excludes the full P family.

At fixed stride \(S\), this is
\[
 M=h^{1/3+o(1)},\qquad
 \text{width }h^{7/3+o(1)}.
 \tag{15}
\]
It simultaneously retains the Hilbert same-parity distance exclusion.
It does not remove the remaining mixed supports, and is not a new
improvement of the full-board threshold.

## 5. Elementary size of the divisor bound

For completeness, \(D_h=h^{o(1)}\) needs only an elementary split.
Put \(L=\log h\), and write \(n=\prod p^{e_p}<h\).
For primes \(p\le\sqrt L\), there are at most \(\sqrt L\) factors and
each \(e_p\le L/\log2\). Their contribution to
\(\log\tau(n^2)=\sum_p\log(2e_p+1)\) is
\[
 O(\sqrt L\log L).
 \]
For \(p>\sqrt L\), use \(2e+1\le3^e\) and
\(\sum e_p\le2L/\log L\). Their contribution is \(O(L/\log L)\).
The first displayed bound is also \(O(L/\log L)\) for sufficiently
large \(h\). Consequently
\[
 D_h\le\exp\!\left(O\!\left(\frac{\log h}{\log\log h}\right)\right).
 \tag{16}
\]
No distribution result for divisor values is used in (15).

## 6. The exact remaining target

The fixed-factor theorem has reduced the local problem to the number
and arrangement of different factors, rather than the number of
solutions belonging to one factor.
Either of the following would give a constant-choice P repair:

- a constant \(M\) satisfying (5) uniformly in \(h\);
- a constant \(M\) satisfying the induced-subgraph criterion (8).

Neither bound is proved here. The conservative estimate (13) loses
information by counting every integer-distance solution for every row
in the Hilbert neighborhood. Improving that count to a bounded local
or induced-subgraph factor budget is the arithmetic and geometric step
still missing.
