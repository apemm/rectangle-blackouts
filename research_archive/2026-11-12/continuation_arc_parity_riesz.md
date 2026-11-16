# A parity-sensitive Riesz criterion for arc classes

12 November 2026. This continues the audit of
`arc_classes_monotone_partition.md`. The original source is unchanged.

Independent review completed for the Fourier-sign lemma, the general
partition-function criterion, and the arithmetic obstruction linked below.

The Riesz argument does not need full bounded-coefficient dissociation.
It only needs the absence of bounded zero relations whose coefficient sum
is odd. This weaker hypothesis tolerates the reflection quartets responsible
for the obstruction in
[the dissociated-deletion audit](continuation_arc_riesz_beta_audit.md).

The strengthened lemma is valid, but its linear-deletion target also fails.
The companion [odd-deletion obstruction](continuation_arc_odd_deletion_obstruction.md)
proves the lower bound in
\[
 \Omega\!\bigl(h\log\log\log\log h\bigr)\
 \le\ \sum_T\beta_{\mathrm{odd}}(T,h)\
 \le\ O(h\log h).
 \tag{1}
\]
The four iterated logarithms refer to sufficiently large heights. These
estimates do not settle either the arc palette or the partition-function
ratio criterion in Section 3.

## 1. The Fourier signs

Let \(m\ge1\) be an integer. Define
\[
 \mu_m=4^{-m}\binom{2m}{m},\qquad
 g_m(x)=\frac{\sin^{2m}(\pi x)}{\mu_m}.
\]
Writing \(e(x)=\exp(2\pi i x)\), the binomial formula gives
\[
 g_m(x)=\sum_{c=-m}^{m}(-1)^c a_{m,c}e(cx),
 \qquad
 a_{m,c}=\frac{\binom{2m}{m+c}}{\binom{2m}{m}}\ge0,
 \qquad a_{m,0}=1.
 \tag{2}
\]
In particular, \(g_m\) is nonnegative and has mean one.

The normalization satisfies
\[
 \mu_m\ge\frac1{2\sqrt m}.
 \tag{3}
\]
This follows by induction from \(\mu_1=1/2\) and
\[
 \frac{\mu_{m+1}}{\mu_m}=\frac{2m+1}{2m+2}
 \ge\sqrt{\frac m{m+1}}.
\]
The squared inequality is \((2m+1)^2\ge4m(m+1)\).

For a finite set \(D\) of nonzero integers, put
\[
 G_D(\theta)=\prod_{d\in D}g_m(d\theta),\qquad
 Z_D=\int_0^1G_D(\theta)\,d\theta.
 \tag{4}
\]
Use \(G_\varnothing=Z_\varnothing=1\). Every \(Z_D\) is positive,
without a relation hypothesis: the product is positive away from finitely
many points of the circle.

The exact constant-term formula is
\[
 Z_D=
 \sum_{\substack{c\in\{-m,\ldots,m\}^{D}\\
                  \sum_{d\in D}c_dd=0}}
 (-1)^{\sum_dc_d}\prod_{d\in D}a_{m,c_d}.
 \tag{5}
\]
Thus the relevant sign depends on the coefficient sum, not on whether the
relation is nontrivial.

## 2. The strengthened lemma

Say that \(D\) satisfies the **even-relation condition at cap \(m\)** if
\[
 \sum_{d\in D}c_dd=0,\quad c_d\in\mathbb Z,\quad |c_d|\le m
 \quad\Longrightarrow\quad
 \sum_{d\in D}c_d\equiv0\pmod2.
 \tag{6}
\]
Nonzero relations are allowed.

**Lemma.** Suppose (6) holds and \(D\) has \(k\) elements. If
\[
 0<\delta\le\frac12,\qquad
 2k\sqrt m\,\sin^{2m}(\pi\delta)<1,
 \tag{7}
\]
then some real \(\theta\) satisfies
\[
 \|\theta d\|\ge\delta\qquad(d\in D).
 \tag{8}
\]

**Proof.** Under (6), every summand of (5) is nonnegative. The zero
coefficient vector contributes one, so \(Z_D\ge1\). If \(E\subseteq D\),
every constant term for \(Z_E\) occurs in \(Z_D\) by setting the other
coefficients to zero. The added coefficient factors are \(a_{m,0}=1\).
Consequently
\[
 1\le Z_E\le Z_D.
 \tag{9}
\]

For \(d\in D\), let \(B_d=\{\theta:\|\theta d\|<\delta\}\).
By (3),
\[
 g_m(d\theta)
 \le b_m(\delta):=2\sqrt m\,\sin^{2m}(\pi\delta)
 \qquad(\theta\in B_d).
\]
Nonnegativity and (9) give
\[
 \int_{B_d}G_D
 \le b_m(\delta)\int_{B_d}G_{D\setminus\{d\}}
 \le b_m(\delta)Z_{D\setminus\{d\}}
 \le b_m(\delta)Z_D.
 \tag{10}
\]
The union of the \(k\) bad sets has \(G_D\)-mass less than \(Z_D\) by
(7). Its complement has positive mass and contains a point satisfying
(8). \(\square\)

Changing a frequency \(d\) to \(-d\) without creating a duplicate does
not affect this condition. Replacing its relation coefficient \(c_d\) by
\(-c_d\) changes the coefficient sum by an even integer. The same argument
holds for indexed frequencies if their indices are preserved.
It does not justify a subsequent deduplication: merging equal frequencies
can change the coefficient cap. The application below defines its
condition directly on the positive, deduplicated distance set.

## 3. A partition-function criterion without a relation hypothesis

For nonempty \(D\), define
\[
 R_D(m)=\max_{d\in D}\frac{Z_{D\setminus\{d\}}}{Z_D}.
 \tag{11}
\]
The first two inequalities of (10) hold for every \(D\). Therefore
\[
 b_m(\delta)
 \sum_{d\in D}\frac{Z_{D\setminus\{d\}}}{Z_D}<1
 \tag{12}
\]
is sufficient for (8). A simpler sufficient condition is
\[
 2k\sqrt m\,\sin^{2m}(\pi\delta)\,R_D(m)<1.
 \tag{13}
\]
This form allows odd relations. It isolates an analytic alternative to
deleting their frequencies: control the ratios in (11).

The even-relation condition proves \(R_D(m)\le1\), by (9).
For arbitrary \(D\), positivity of \(Z_D\) alone does not imply that ratio
bound. No uniform bound for (11) on the full arithmetic distance sets is
claimed here.

## 4. The precise conditional deletion target

Use the actual finite diagonal distances. With
\[
 A=\lceil h/2\rceil,\qquad K=\lfloor h/2\rfloor,\qquad T=2s+1,
\]
put
\[
 I_s=[\max(0,-s),\,\min(A,K-s))\cap\mathbb Z,\qquad
 n_T=|I_s|,
\]
where \(-(A-1)\le s\le K-1\). Define
\[
 D_T(h)=
 \left\{|d|:\ d\ne0,\quad |d|<n_T,\quad
 20d^2+4Td+T^2=L^2,\quad 0<L<h\right\}.
 \tag{14}
\]
The two signs of \(d\) are tested before taking absolute values. Duplicate
positive distances are removed.

For \(k\ge1\), let \(m(k)\) be the least positive integer with
\[
 2k\sqrt{m(k)}<2^{m(k)}.
 \tag{15}
\]
Let \(m(0)=1\). Define \(\beta_{\mathrm{odd}}(T,h)\) as the minimum
number of deletions from \(D_T(h)\) leaving a set \(E\) that satisfies
(6) at cap \(m(|E|)\). The empty retained set is allowed.
The dependence of the cap on the **retained** cardinality is part of the
definition.

For nonempty \(E\), the lemma with \(\delta=1/4\) gives four half-open
arc classes for the slots \(i\in I_s\):
\[
 \left\lfloor4\{\theta i\}\right\rfloor\in\{0,1,2,3\}.
 \tag{16}
\]
Two slots in one such arc have circular separation strictly less than
\(1/4\). Hence their difference is not in \(E\).

The distance graph of the removed positive gaps has an increasing-order
greedy coloring with at most \(\beta_{\mathrm{odd}}(T,h)+1\) colors.
Each slot has at most one earlier neighbor for each removed gap. Taking
the product coloring with (16) yields at most
\[
 4\bigl(\beta_{\mathrm{odd}}(T,h)+1\bigr)
 \tag{17}
\]
classes for that diagonal. The same bound is valid if \(E\) is empty.

Each class remains a subset of one constant-offset diagonal. It therefore
inherits the source's monotonicity and no-right-angle property. The
coloring removes every within-class P conflict. There are \(h-1\)
nonempty offset diagonals, so
\[
 \chi_{\mathrm{mon},P}(h)
 \le4\sum_T\bigl(\beta_{\mathrm{odd}}(T,h)+1\bigr).
 \tag{18}
\]
In particular,
\[
 \sum_T\beta_{\mathrm{odd}}(T,h)=O(h)
 \quad\Longrightarrow\quad
 \chi_{\mathrm{mon},P}(h)=O(h).
 \tag{19}
\]
The implication (19) is valid, but its premise is false by (1).
Thus this particular deletion criterion cannot prove a linear partition.
The direct ratio criterion (13) remains available. Any resulting monotone
P partition would still leave the other collision types and the filler
problem to separate arguments.

## 5. Why the reflection obstruction no longer applies

For \(5\mid T\), the quadratic in (14), with zero also allowed, is
invariant under
\[
 d\longmapsto-d-T/5.
 \tag{20}
\]
Two complete signed reflection pairs give a relation with coefficients
\((1,1,-1,-1)\). Its coefficient sum is zero. The absolute-gap version
used in the deletion lower bound has the form
\[
 d_1-e_1-d_2+e_2=0,
 \tag{21}
\]
again with coefficient sum zero. These relations are permitted by (6),
at every cap.

The exceptional signed gap \(-T/5\), when it is present, gives a different
relation:
\[
 d+d'-(-T/5)=0.
 \tag{22}
\]
Its coefficient sum is one. In positive-distance notation this becomes
the corresponding sum or difference relation with the anchor \(|T|/5\);
its coefficient sum remains odd. Removing that one anchor removes this
particular family of odd relations. It does not prove that the remaining
set satisfies (6).

Thus the established \(\Omega(h\log h)\) lower bound for deletion to full
dissociation does not yield that lower bound for
\(\beta_{\mathrm{odd}}\). The companion obstruction instead uses the
primitive two-term relation between opposite-parity endpoints of each
reflection edge, once the retained-set cap becomes large enough.

## 6. A linear lower bound for the new deletion cost

Let \(t\) be a positive odd integer with \(29t<h\), and set \(T=11t\).
The three signed gaps \(2t,-3t,5t\) satisfy
\[
\begin{aligned}
20(2t)^2+4(11t)(2t)+(11t)^2&=(17t)^2,\\
20(-3t)^2+4(11t)(-3t)+(11t)^2&=(13t)^2,\\
20(5t)^2+4(11t)(5t)+(11t)^2&=(29t)^2.
\end{aligned}
\tag{23}
\]
They meet the actual diagonal cutoff. Here \(s=(11t-1)/2\ge0\), and
\[
 n_T=K-s\ge\frac{h-11t}{2}>9t>5t.
 \tag{24}
\]
Hence \(D_{11t}(h)\) contains \(\{2t,3t,5t\}\). The relation
\[
 2t+3t-5t=0
 \tag{25}
\]
has coefficients in \(\{-1,0,1\}\) and odd coefficient sum. Every retained
set satisfying (6) must lose at least one of those three elements.
Therefore
\[
 \beta_{\mathrm{odd}}(11t,h)\ge1.
 \tag{26}
\]
There are \(h/58+O(1)\) eligible positive odd values of \(t\).
This gives a direct linear lower bound. The stronger lower bound in (1)
uses the additional argument in the companion note.

Deleting the whole set gives
\[
 \sum_T\beta_{\mathrm{odd}}(T,h)
 \le\sum_T|D_T(h)|=O(h\log h).
 \tag{27}
\]
The last estimate can be seen directly from the associated integer right
triangles with legs \(4|d|\), \(|T+2d|\), and hypotenuse \(L<h\).
Euclid's parametrization bounds their number by
\[
 O\!\left(\sum_{u\le\sqrt h}\sum_{1\le v<u}
                 \frac{h}{u^2+v^2}\right)
 =O(h\log h).
 \tag{28}
\]
The finitely many sign choices change only the constant. The degenerate
odd leg cannot occur because \(T\) is odd.

## 7. Why the coefficient cap matters

There is an exact description if (6) is required for **all** integer
relations, with no coefficient bound:
\[
 \text{every zero relation has even coefficient sum}
 \quad\Longleftrightarrow\quad
 \nu_2(d)\text{ is constant on }D.
 \tag{29}
\]
Here \(\nu_2(d)=\nu_2(|d|)\).

For sufficiency, divide all frequencies by their common power of two.
They become odd, and the relation reduced modulo two gives
\(\sum_dc_d=0\pmod2\).

For necessity, take positive absolute frequencies \(a,b\), let
\(g=\gcd(a,b)\), and use
\[
 (b/g)a-(a/g)b=0.
 \tag{30}
\]
If their 2-adic valuations differ, exactly one of \(a/g,b/g\) is odd.
The coefficient sum in (30) is odd.

The bounded condition is weaker. For example, \(\{1,8\}\) satisfies
(6) at cap \(m(2)=3\), despite its different valuations: every nonzero
relation has a coefficient of magnitude at least eight. Therefore (29)
does not settle the finite-cap deletion target in (19).

Reflection pairs also illustrate this distinction. Since \(T/5\) is odd,
the two absolute distances in a complete nonexceptional pair have
opposite parity. Their primitive two-term relation is odd-sum, but its
coefficients can exceed \(m(|E|)\). The four-term reflection relation has
small coefficients and even sum. Neither fact alone determines the new
deletion cost.

## 8. Status and the remaining target

The complete written Fourier-sign lemma and ratio criterion have passed
independent review. The proofs in Sections 1--3 are elementary and do not
use a probabilistic independence assertion.

The strengthened criterion permits even-sum relations, but deleting all
bounded odd-sum relations still has a superlinear total cost.
Two concrete questions remain:

1. What is the true order of the finite-cap odd-relation deletion cost
   between the bounds in (1)?
2. Can the ratios \(R_{D_T(h)}(m)\) be controlled directly, allowing odd
   relations instead of deleting them?

Neither deletion obstruction rules out a linear arc palette.
The ratio criterion isolates a sufficient analytic estimate that does not
discard additive relations.
