# A parity-localized partition-regularity argument for the odd P graph

15 November 2026. New proof adaptation, independently reviewed. This is not a direct quotation of a published theorem and is not a refereed result. Two separate source-level reviews checked the adaptation. The detailed [independent audit](continuation_odd_p_partition_regularity_independent_audit.md) records the published hypotheses, the CRT and concentration steps, the spectral kernel, and the limit order.

Let
\[
 R(m,n)=m^2-n^2,\qquad T(m,n)=m^2+mn-n^2.
 \tag{1}
\]
**Theorem.** Every finite coloring of the positive odd integers has monochromatic \(u<v\) satisfying
\[
 u^2+4(v-u)^2=w^2
 \tag{2}
\]
for some positive integer \(w\). The proof below localizes the parameters to \(m\) odd and \(n\) even.

## 1. Published inputs and what needs extension

Use Frantzikinakis, Klurman, and Moreira, [*Partition regularity of generalized Pythagorean pairs*, version 3](https://arxiv.org/html/2407.08360v3). The inputs are their Theorem 3.1, linear concentration Proposition 4.7, irreducible quadratic concentration Proposition 4.9, and the spectral reduction preceding Theorem 2.6.

Theorem 1.12's footnote covers a reducible/irreducible pair after a linear substitution, but does not by itself establish the parameter parity required here. Case (ii) of Theorem 2.4 assumes two irreducible forms. Its proof uses variable CRT offsets, not a fixed offset \((1,0)\).

The extension proved here supplies explicit CRT offsets for (1). It applies linear concentration to the two factors of \(R\), quadratic concentration to \(T\), and one multiplicative average. It uses the revised real logarithmic-ratio weight, with the limits in the published order.

## 2. Explicit CRT localization

Fix an integer \(r\ge2\). Let \(\mathcal F_r\) contain all primes dividing \(2r!\). For an integer \(K\) tending to infinity, put
\[
 Q=Q_K=\prod_{p\le K}p^{2K}.
\]
For every prime \(p\le K\) outside \(\mathcal F_r\), choose an integer
\[
 K/4<\ell_p\le K/2,
\]
and set
\[
 c=\prod_{\substack{p\le K\\p\notin\mathcal F_r}}p^{\ell_p}.
 \tag{3}
\]
Write \(\Psi_{r,K}\) for the finite set of these \(c\)'s.

Choose \(a,b\in[Q]\) by the following conditions modulo each \(p^{2K}\).

- If \(p\in\mathcal F_r\), take \(a\equiv1,\ b\equiv0\).
- Otherwise take \(b\equiv1,\ a\equiv1+p^{\ell_p}\).

For sufficiently large \(K\), these imply
\[
\begin{split}
 &a\equiv1,\quad b\equiv0\pmod{r!},\\
 &\gcd(a-b,Q)=c,\quad \gcd(a+b,Q)=1,\\
 &\gcd(T(a,b),Q)=1.
\end{split}
 \tag{4}
\]
Indeed, at a prime outside \(\mathcal F_r\), \(a-b\) has exact valuation \(\ell_p\), while \(a+b\equiv2\) and \(T(a,b)\equiv1\pmod p\). At every exceptional prime both linear factors and \(T\) are \(1\pmod p\). No Hensel lifting or discriminant distinction is needed for this construction.

In particular \(a\) is odd and \(b\) is even. Every parameter pair
\[
 m'=Qm+a,\qquad n'=Qn+b
 \tag{5}
\]
has the desired parity.

The exponent range in (3) is deliberate. Both \(Q\) and \(Q/c\) belong to the set \(\Phi_K\) in Proposition 4.7: every prime exponent is strictly greater than \(K\) and at most \(2K\). Meanwhile \(\Psi_{r,K}\) is asymptotically invariant under multiplication by each fixed prime outside \(\mathcal F_r\).

## 3. Weights and aperiodic functions

For \(\delta>0\), let \(F_\delta\) be the nonnegative continuous trapezoid supported on \([-\delta,\delta]\), equal to one on the middle half. Put
\[
 w_\delta(m,n)=
 F_\delta\!\left(\log\frac{R(m,n)}{T(m,n)}\right)
 \mathbf1_{\{R(m,n)>0,\ T(m,n)>0\}},
\]
and normalize it to \(\widetilde w_\delta=w_\delta/\mu_\delta\), where
\[
 \mu_\delta=\lim_{N\to\infty}N^{-2}\sum_{m,n\le N}w_\delta(m,n)>0.
 \tag{6}
\]
The limit exists by homogeneity and Riemann integration. It is positive because \(R/T\to1\) as \(n/m\to0^+\). The weight is bounded for each fixed \(\delta\), and its mean tends to one.

For a completely multiplicative \(f:\mathbb N\to\mathbb S^1\), extended by \(f(-n)=f(n)\) and \(f(0)=0\), define
\[
 L_{r,\delta,K,N}(f,c)=
 \mathbb E_{m,n\le N}\widetilde w_\delta(m,n)
 f(R(Qm+a,Qn+b))\overline{f(T(Qm+a,Qn+b))}.
 \tag{7}
\]
The offsets are those belonging to \(c\).

If \(f\) is aperiodic, Theorem 3.1 applies to the two independent linear forms \(m-n,m+n\), and the irreducible quadratic form \(T\), whose discriminant is \(5\). It gives vanishing for cone indicators. On \(m>n>0\), the ratio
\[
 \frac{R(m,n)}{T(m,n)}
 =\frac{1-z^2}{1+z-z^2},\qquad z=n/m,
\]
is continuous and strictly decreasing in \(z\in(0,1)\). Approximate the bounded weight by finitely many homogeneous cone indicators. This gives
\[
 \lim_{N\to\infty}L_{r,\delta,K,N}(f,c)=0
 \tag{8}
\]
for every fixed \(r,\delta,K,c\). Replacing a cone in \((m,n)\) by its translate in (5) costs density zero.

## 4. The two concentration formulas

Suppose \(f\sim\chi(n)n^{it}\) in the ordinary pretentious distance, where \(\chi\) has period \(q\). Fix \(r\) sufficiently large that \(q\mid r!\). Set
\[
 z_f(p)=f(p)\overline{\chi(p)}p^{-it},\qquad
 F_N(f,K)=\sum_{K<p\le N}\frac{z_f(p)-1}{p}.
 \tag{9}
\]
For the irreducible form \(T\), write
\[
 G_N(f,K)=
 \sum_{K<p\le N}\frac{\omega_T(p)}p(z_f(p)-1).
 \tag{10}
\]
Here \(\omega_T(p)\le2\), and away from finitely many primes it equals \(0\) or \(2\).

Factor the first translated form as
\[
 R(Qm+a,Qn+b)
 =c\left(\frac Qc(m-n)+\frac{a-b}c\right)
       \left(Q(m+n)+a+b\right).
 \tag{11}
\]
The slopes \(Q/c,Q\) belong to \(\Phi_K\), and each offset is coprime to its slope. The first offset has absolute value at most \(Q/c\). For the second, reduce \(a+b\) modulo \(Q\), absorbing at most one unit shift in \(m+n\).

Apply Proposition 4.7 to the two factors. An average over \(m-n\) is bounded by a one-dimensional average up to \(N\); one over \(m+n\) is bounded by twice an average up to \(2N\). Replacing \(F_{2N}\) by \(F_N\) costs \(o(1)\): Cauchy–Schwarz bounds their difference by the pretentious-distance tail times \((\sum_{N<p\le2N}1/p)^{1/2}\), and this last sum is bounded. Fixed unit shifts in the Archimedean factor also cost \(o(1)\).

Complete multiplicativity and (4) therefore give
\[
 f(R(Qm+a,Qn+b))
 =
 \widetilde f(c)\,Q^{2it}R(m,n)^{it}
 \exp(2F_N(f,K))+o_{L^1}(1),
 \tag{12}
\]
where
\[
 \widetilde f(c)=f(c)\overline{\chi(c)}c^{-it}.
\]
The \(L^1\) error tends to zero in the order \(N\to\infty\), then \(K\to\infty\), uniformly over \(c\in\Psi_{r,K}\). To obtain the character factor, use
\[
 \chi((a-b)/c)\chi(a+b)
 =\chi(R(a,b)/c)=\overline{\chi(c)},
\]
because \(R(a,b)\equiv1\pmod{r!}\).

Ordinary pretentiousness also implies \(T\)-pretentiousness with the same \(\chi,t\). Proposition 4.9 applies with normalization divisor \(1\), because \(T(a,b)\) is coprime to \(Q\). It gives
\[
 f(T(Qm+a,Qn+b))
 =
 Q^{2it}T(m,n)^{it}\exp(G_N(f,K))+o_{L^1}(1),
 \tag{13}
\]
with the same order and uniformity. Its character factor is one since \(T(a,b)\equiv1\pmod{r!}\).

Equations (12)–(13) are used only on the positive cone selected by the weight. In fact positivity survives the shifts exactly: on this cone \(m>n\), so \(Q(m-n)+a-b\ge1\), because \(a,b\in[Q]\). Thus both translated forms are positive.

## 5. One multiplicative average removes the remaining phase

For fixed \(\delta\), combine (12)–(13):
\[
 L_{r,\delta,K,N}(f,c)
 =\widetilde f(c)\,M_{\delta,K,N}(f)+o(1),
 \tag{14}
\]
uniformly in \(c\), where
\[
 M_{\delta,K,N}(f)=
 e^{\,2F_N(f,K)+\overline{G_N(f,K)}}
 \mathbb E_{m,n\le N}\widetilde w_\delta(m,n)
 \left(\frac{R(m,n)}{T(m,n)}\right)^{it}.
 \tag{15}
\]
This quantity does not depend on \(c\), and its modulus is at most \(1+o_N(1)\). Both real exponential parts are nonpositive.

There are two cases.

If \(z_f(p_0)\ne1\) at some prime \(p_0\notin\mathcal F_r\), the product average over (3) has
\[
 \mathbb E_{c\in\Psi_{r,K}}\widetilde f(c)\longrightarrow0.
 \tag{16}
\]
The factor at \(p_0\) is a geometric average of consecutive powers of a fixed unit complex number other than one, over an interval whose length tends to infinity. All other factors have modulus at most one. Thus the average of (14) tends to zero, first in \(N\), then in \(K\).

If \(z_f(p)=1\) at every prime outside \(\mathcal F_r\), both sums (9) and (10) vanish for \(K\) beyond this finite set. On the support of the weight,
\[
 \left|(R/T)^{it}-1\right|\le |t|\delta.
\]
The averaged correlation therefore tends to one as \(\delta\to0\), after the previous limits.

Consequently every pretentious \(f\) has
\[
 \liminf_{r\to\infty}\liminf_{\delta\to0^+}
 \liminf_{K\to\infty}\liminf_{N\to\infty}
 \mathbb E_{c\in\Psi_{r,K}}\Re L_{r,\delta,K,N}(f,c)\ge0.
 \tag{17}
\]
For \(f=1\), the value is one. Aperiodic functions have value zero by (8).

Unlike the two-irreducible argument, no matching of distinct pretentious characters on common splitting primes is needed. The reducible form supplies a simple root at \(m=n\) for every odd prime, and \(T(1,1)=1\). That permits the single average over every prime outside a finite set.

## 6. Spectral positivity retains the localization

Use the published spectral reduction in its usual form. A positive-multiplicative-density cell supplies a finite positive Borel measure \(\sigma\) on completely multiplicative functions, with
\[
 \sigma(\{1\})>0,\qquad
 \int f(v)\overline{f(w)}\,d\sigma(f)\ge0
 \quad(v,w\in\mathbb N).
 \tag{18}
\]
A positive value of this kernel at \(v,w\) gives a nonempty common multiplicative translate into the cell.

The absolute values of the averages in (7) are bounded by the mean of the normalized weight, tending to one independently of \(r,K,c\). Apply Fatou successively in the displayed order in (17), using a sequence \(\delta\downarrow0\). The atom at \(1\) gives a strictly positive lower bound after integration. Hence some finite \(r,\delta,K,c\) has positive averaged kernel for the parameter pairs (5).

The selected weight is nonnegative, and the translated forms are positive everywhere on its support. Some \(m',n'\) of the form (5) therefore satisfy
\[
 R(m',n')>0,\quad T(m',n')>0,\quad
 \int f(R(m',n'))\overline{f(T(m',n'))}\,d\sigma(f)>0.
 \tag{19}
\]
They have \(m'\) odd and \(n'\) even. They are positive, and
\(T(m',n')-R(m',n')=m'n'>0\), so their form values are distinct.

This step does not discard the CRT restriction by passing to unrestricted parameters. It extracts the positive pair directly from one of the localized averages.

## 7. Odd monochromatic pairs and the graph consequence

Given a finite coloring \(c_{\rm odd}\) of positive odd integers, color every positive integer \(n\) by the color of its odd part. Choose a cell with positive multiplicative density, and apply Section 6. There are positive integers \(k,m',n'\), with \(m'\) odd and \(n'\) even, for which
\[
 kR(m',n'),\qquad kT(m',n')
\]
have the same extended color.

The two form values are odd. Write \(k=2^e k_0\) with \(k_0\) odd. Then
\[
 u=k_0R(m',n'),\qquad v=k_0T(m',n')
\]
are distinct positive odd integers of the same original color. The identity
\[
 R(m,n)^2+4(T(m,n)-R(m,n))^2=(m^2+n^2)^2
\]
proves (2).

Thus the graph on positive odd integers joining \(u<v\) when (2) holds has no finite proper coloring. Equivalently, for each fixed number of colors it has a finite noncolorable induced subgraph, by the elementary compactness argument for graph colorings.

This concerns the stated graph and any construction that genuinely requires a bounded proper coloring of all of it. There is no quantitative height bound for the finite obstruction, and no general lower bound for \(m_h\). The theorem does not address slot-dependent or adaptive constructions that avoid embedding the entire graph.

